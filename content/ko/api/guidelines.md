---
title: 지침과 모범 사례
description: 마스토돈 앱 구현 시 기억해야 할 사항입니다.
menu:
  docs:
    weight: 10
    parent: api
---

## 로그인 {#login}

**사용자는 앱에서 어떤 마스토돈 서버에도 로그인할 수 있어야 합니다**. 즉, 서버 도메인을 요청하고 앱 등록 API로 OAuth2 자격 증명을 동적으로 얻어야 합니다.

{{< page-ref page="client/authorized" >}}

{{< page-relref ref="methods/oauth" caption="OAuth 메서드" >}}

{{< page-relref ref="api/oauth-scopes" caption="OAuth 범위" >}}

## 사용자명 {#username}

**사용자는 분산 구조를 알 수 있어야 합니다**. 예를 들어 `acct`를 어딘가에 표시하여 해당 사용자가 다른 서버에 속함을 알 수 있어야 합니다. 로컬 사용자의 `acct`는 `username`과 같고, 원격 사용자는 `username@domain`과 같습니다.

## API 응답의 ID 처리 {#id}

**ID는 항상 내부 구조를 해석하지 않는 문자열로 다루세요**.

기본 마스토돈의 엔터티 ID는 정수로 생성되며(보통 [Snowflake ID](https://en.wikipedia.org/wiki/Snowflake_ID)의 변형을 사용하지만, 이전 ID나 내부 전용 ID는 자동 증가 정수일 수 있습니다), API 응답 직렬화기가 문자열로 변환합니다. 하지만 ID가 정수라는 뜻은 아니며 정수로 변환해서도 안 됩니다! 그렇게 하면 정수 오버플로 또는 변환 관련 오류로 클라이언트 앱이 제대로 동작하지 않을 수 있습니다.

비공식 마스토돈 API 구현이 숫자로 된 어휘 형식이나 숫자 자체를 사용한다는 보장은 없습니다. 예를 들어 [Flake](https://github.com/boundary/flake) 같은 ID 생성 알고리즘은 62진수 알파벳으로 인코딩한 128비트 정수를 생성하므로 ID에 문자가 포함됩니다. 또 다른 예로 HTTPS URI를 사용하는 ID 생성 알고리즘은 숫자를 전혀 나타내지 않습니다.

다만 기본 마스토돈은 숫자의 문자열 표현을 ID로 사용하므로 다음과 같이 시간순으로 정렬할 수 있습니다.

1. 길이로 정렬합니다. 최신 게시물은 ID가 더 깁니다.
2. 사전순으로 정렬합니다. 최신 게시물은 위치별로 비교했을 때 적어도 한 자리의 숫자가 더 큽니다.

일반적으로 클라이언트는 ID를 정렬할 필요가 없습니다. API 응답 생성 전에 ID를 정렬하는 것은 서버의 책임입니다. 마스토돈은 보통 데이터베이스 삽입 시각의 역순으로 API 응답을 정렬하지만, 검색 결과나 유행 같은 일부 API 응답은 관련성에 따라 정렬할 수 있습니다.

## API 응답 페이지네이션 {#pagination}

많은 API 메서드에서 `limit`, `max_id`, `min_id`, `since_id` 같은 매개변수로 페이지네이션하여 더 많은 정보를 가져올 수 있습니다.

limit
: 반환할 최대 결과 수입니다. 보통 기본 제한과 최대 제한이 있으며 API 메서드에 따라 다릅니다.

max_id
: 문자열입니다. 반환하는 모든 결과는 이 ID보다 작습니다. 사실상 결과의 상한을 설정합니다.

since_id
: 문자열입니다. 반환하는 모든 결과는 이 ID보다 큽니다. 사실상 결과의 하한을 설정합니다.

min_id
: 문자열입니다. 이 ID 바로 다음의 결과를 반환합니다. 사실상 이 ID에 커서를 두고 앞으로 페이지네이션합니다(v2.6.0부터 사용 가능).

예를 들어 클라이언트가 특정 매개변수로 `https://mastodon.example/api/v1/accounts/1/statuses`를 가져오면 마스토돈은 각 경우 다음 결과를 반환합니다.

- `?max_id=1`을 설정하면 `1`보다 이전 ID의 게시물이 없으므로 게시물을 반환하지 않습니다.
- `?since_id=1`을 설정하면 `1` 이후의 게시물이 많으므로 최신 게시물을 반환합니다.
- `?min_id=1`을 설정하면 `min_id`가 커서를 `1`에 두고 앞으로 페이지네이션하므로 가장 오래된 게시물을 반환합니다.

일부 API 메서드는 API 응답에 공개되지 않고 백엔드와 데이터베이스만 아는 엔터티 ID를 사용합니다(보통 Account를 참조하는 Follow 엔터티나 Status를 참조하는 Favourite 엔터티처럼 다른 엔터티를 참조할 때 그렇습니다). 이를 해결하기 위해 마스토돈은 이 매개변수의 값이 미리 채워진 “다음” 및/또는 “이전” 페이지 링크를 반환할 수 있습니다. 다음 가상의 API 호출과 응답을 살펴보세요.

```http
GET /api/v1/endpoint HTTP/1.1
Host: mastodon.example
Authorization: Bearer <access_token>
```
```http
HTTP/1.1 200 OK
Link: <https://mastodon.example/api/v1/endpoint?max_id=7163058>; rel="next", <https://mastodon.example/api/v1/endpoint?min_id=7275607>; rel="prev"

[
  {
    "//": "some Entity"
  },
  "more Entities in an Array"
]
```

이 경우 HTTP `Link` 헤더를 가져와 다음 또는 이전 페이지 링크를 분석할 수 있습니다. HTTP 헤더 분석은 [RFC 9651](https://www.rfc-editor.org/rfc/rfc9651)을, 특히 `Link` 헤더는 [RFC 8288](https://datatracker.ietf.org/doc/rfc8288/)을 참고하세요. `next` 링크 관계를 따라가면 다음 페이지가, `prev` 링크 관계를 따라가면 이전 페이지가 표시됩니다.

## 폐기 예정 기능 {#deprecations}

마스토돈은 API를 드물게 제거하지만 때때로 제거할 수 있습니다. 따라서 마스토돈 릴리스를 확인하고 폐기 예정 API에 주의를 기울이는 것이 좋습니다.

또한 구현자가 폐기 예정 API 사용을 발견하도록 마스토돈 4.4.0은 [RFC9745](https://datatracker.ietf.org/doc/html/rfc9745)에 정의된 `Deprecation` 헤더를 사용합니다. 라이브러리와 애플리케이션 개발자는 이 헤더를 확인하고 개발 환경에서 경고를 표시하여 API가 제거되기 전에 발견하는 것이 좋습니다.

## 서식 {#formatting}

원격 서버 콘텐츠의 일반 텍스트는 제공되지 않으며, 일반 텍스트 구문 규칙은 마스토돈과 다른 연합우주 애플리케이션 사이에서 크게 다를 수 있습니다. 게시물 콘텐츠 같은 특정 속성에는 **마스토돈은 정리된 HTML을 제공합니다**. 자세한 내용은 [HTML 정리]({{< relref "spec/activitypub#sanitization" >}})를 참고하세요. 콘텐츠에는 다음 태그가 나타날 수 있습니다.

* `<p>`
* `<br>`
* `<span>`
* `<a>`

{{< page-relref ref="spec/activitypub#sanitization" caption="ActivityPub > HTML 정리" >}}

### 멘션, 해시태그, 사용자 지정 이모지 {#tags}

멘션과 해시태그는 `<a>` 태그입니다. 사용자 지정 이모지는 일반 텍스트 단축 코드 형식을 유지합니다. 이러한 엔터티에 의미를 부여하고, 멘션된 프로필을 웹페이지 대신 앱 안에서 여는 등의 특별 처리를 추가할 수 있도록 [Status]({{< relref "entities/Status" >}})에 메타데이터를 포함하며, 이를 특정 태그와 연결할 수 있습니다.

{{< page-relref ref="entities/Status" caption="Status 엔터티" >}}

{{< page-relref ref="entities/Status#mentions" caption="Status#mentions" >}}

{{< page-relref ref="entities/Status#tags" caption="Status#tags" >}}

{{< page-relref ref="entities/Status#emojis" caption="Status#emojis" >}}

### 링크 줄이기 {#links}

마스토돈의 링크는 URL 단축 서비스를 사용하여 줄이지 않으며 URL 단축 서비스 사용은 강하게 권장하지 않습니다. 텍스트의 URL은 항상 23자로 계산하며 시각적으로 줄여 표시하도록 되어 있습니다. 이를 위해 링크를 다음과 같이 마크업합니다.

```html
<a href="https://example.com/page/that/is/very/long">
  <span class="invisible">https://</span>
  <span class="ellipsis">example.com/page</span>
  <span class="invisible">/that/is/very/long</span>
</a>
```

`invisible` 클래스의 span은 숨길 수 있습니다. 가운데 span은 계속 표시하도록 되어 있습니다. URL이 그다지 길지 않으면 클래스가 없을 수 있고, 그렇지 않으면 `ellipsis` 클래스가 있습니다. 마크업에는 줄임표(`…`) 문자를 삽입하지 않으므로, 앱에서 필요하면 직접 삽입해야 합니다.

## 필터 {#filters}

### 서버 측 필터링 (v2, 마스토돈 4.0 이상) {#server-filtered}

필터가 Status에 적용되면 해당 FilterResult를 `filtered` 속성에 포함합니다. 클라이언트는 이 속성의 일치 항목을 확인하고 의도한 필터 동작을 적용해야 합니다.

하지만 클라이언트 구현에서 자체 규칙 일치를 수행하면 서버에서 게시물을 다시 가져오지 않고도 필터 변경을 소급 적용할 수 있습니다. 이때 필터링 시스템 확장(예: `status_matches`)을 처리할 수 있도록 `keyword_matches` 이외의 속성이 있는 `filtered` 항목을 무시하지 않도록 주의해야 합니다.

일치한 필터는 맥락(`home`, `notifications`, `public`, `thread`, `profile`)과 만료 날짜에 따라 걸러야 합니다.

활성 상태의 일치한 필터 중 적어도 하나의 `filter_action`이 `hide`이면 게시물을 전혀 표시하면 안 됩니다. 그렇지 않고 적어도 하나의 `filter_action`이 `warn`이면 경고와 함께 게시물을 숨기고, 사용자에게 어떤 필터가 일치했는지 알린 뒤 게시물을 볼 수 있게 해야 합니다(정확히 일치한 키워드 대신 `title`로 필터를 식별합니다).

확장을 위해 알 수 없는 `filter_action` 값은 `warn`으로 처리해야 합니다.

### 클라이언트 측 필터링 (v1, 마스토돈 4.0 이전) {#client-filtered}

클라이언트는 API가 반환한 필터를 기반으로 직접 텍스트를 필터링해야 합니다. 서버는 `home`과 `notifications` 맥락에서 `irreversible` 필터를 적용하지만, **나머지 필터링은 여전히 클라이언트의 책임입니다**! 어떤 이유로든 `irreversible` 필터가 게시물을 제거하지 않았다면 클라이언트가 여전히 필터링해야 합니다.

만료된 필터를 서버가 삭제하지는 않습니다. 더 이상 적용하면 안 되지만, 사용자가 만료 시각을 갱신하여 필터를 다시 활성화할 수 있으므로 서버에 계속 저장합니다. 원한다면 최종적으로 이 필터를 삭제하는 것은 사용자의 몫입니다.

`whole_word`가 true이면 클라이언트 앱은 다음을 수행해야 합니다.

* 앱의 ‘단어 구성 문자’를 정의합니다. 공식 구현에서는 JavaScript의 `[A-Za-z0-9_]`와 Ruby의 `[[:word:]]`를 사용합니다. Ruby는 POSIX 문자 클래스(Letter | Mark | Decimal_Number | Connector_Punctuation)를 사용합니다.
* 구문이 단어 문자로 시작하고 일치 범위 바로 앞 문자도 단어 문자이면 일치하지 않는 것으로 처리해야 합니다.
* 구문이 단어 문자로 끝나고 일치 범위 바로 뒤 문자도 단어 문자이면 일치하지 않는 것으로 처리해야 합니다.

자세한 내용은 마스토돈 소스 코드의 `app/javascript/mastodon/selectors/index.js`와 `app/lib/feed_manager.rb`를 확인하세요.

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/javascript/mastodon/selectors/index.js" caption="app/javascript/mastodon/selectors/index.js" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/feed_manager.rb" caption="app/lib/feed_manager.rb" >}}

## 미디어 썸네일 자르기용 초점 {#focal-points}

다양한 앱과 사용자 인터페이스를 지원하기 위해 서버 측 미리보기 이미지는 자르지 않습니다. 따라서 앱에서 이미지를 잘라야 합니다. 초점을 사용하면 이미지를 적절하게 자를 때 특정 부분이 잘린 화면 안에 항상 들어오도록 할 수 있습니다. [이미지 초점 정의 안내](https://github.com/jonom/jquery-focuspoint#1-calculate-your-images-focus-point)를 참고하세요. 요약하면, 부동소수점 수는 왼쪽에서 오른쪽 또는 아래에서 위로 -1.0부터 1.0까지입니다. (0,0)은 이미지 중앙입니다. (0.5, 0.5)는 오른쪽 위 사분면의 중앙이고, (-0.5, -0.5)는 왼쪽 아래 사분면의 중앙입니다. 참고로 마스토돈 프런트엔드의 썸네일은 주로 16:9입니다.

{{< figure src="assets/focal-points.jpg" caption="다양한 초점과 해당 좌표의 예시입니다." >}}
