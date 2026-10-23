---
title: 검색 API 메서드
description: 계정, 게시물, 해시태그의 콘텐츠를 검색합니다.
menu:
  docs:
    name: 검색
    parent: methods
    identifier: methods-search
aliases: [
  "/methods/search",
  "/api/methods/search",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 검색 수행 {#v2}

```http
GET /api/v2/search HTTP/1.1
```

지정한 매개변수로 계정, 게시물, 해시태그의 콘텐츠를 검색합니다. 조회하는 서버의 구체적인 백엔드 검색 구성에 따라 결과의 가용성이 달라집니다. 기본적으로 계정과 해시태그는 항상 검색할 수 있지만, 게시물은 ElasticSearch 백엔드가 있고 API 요청이 인증된 경우에만 검색할 수 있습니다(인증되지 않은 사용자는 전문 검색을 사용할 수 없습니다).

**반환:** [Search]({{< relref "entities/Search" >}})\
**OAuth:** 공개(`resolve` 또는 `offset` 없이), 또는 사용자 토큰 + `read:search`\
**버전 이력:**\
2.4.1 - 추가, 제한은 5로 고정\
2.8.0 - `type`, `limit`, `offset`, `min_id`, `max_id`, `account_id` 추가\
3.0.0 - `exclude_unreviewed` 매개변수 추가\
3.3.0 - `min_id`와 `max_id` 함께 사용 가능\
4.0.0 - 더 이상 사용자 토큰이 필수가 아님. 유효한 사용자 토큰이 없으면 `resolve` 또는 `offset` 매개변수를 사용할 수 없습니다.

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters}

q
: {{<required>}} 문자열. 검색어입니다.

type
: 문자열. `accounts`, `hashtags`, `statuses` 중 하나만 검색할지 지정합니다.

resolve
: 불리언. `type`에 `accounts`가 포함되거나 `q`가 HTTPS URL인 경우에만 관련이 있습니다. 첫 번째 경우 `true`이고 (a) 검색어가 원격 계정(예: `someaccount@someother.server`)이며 (b) 로컬 서버가 해당 계정을 모르면 [WebFinger](/spec/webfinger)로 `someother.server`의 계정을 해석하려고 시도합니다. 지연 시간은 늘어나지만 더 많은 결과를 찾습니다. `false`이면 서버가 알고 있는 계정만 반환합니다. 두 번째 경우 `true`이면 URL을 해석하여 일치하는 게시물, 계정, 컬렉션을 반환하려고 시도합니다. `false`이면 이 해석 과정을 건너뛰고 일반 검색을 수행합니다.

following
: 불리언. 사용자가 팔로우하는 계정만 포함할지 여부입니다. 기본값은 false입니다.

account_id
: 문자열. 제공하면 이 계정이 작성한 게시물만 반환합니다.

exclude_unreviewed
: 불리언. 검토되지 않은 태그를 제외할지 여부입니다. 기본값은 false입니다. 인기 태그를 찾으려면 true를 사용하세요.

max_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 작습니다. 결과의 상한을 설정합니다.

min_id
: 문자열. 이 ID보다 바로 다음으로 새로운 결과를 반환합니다. 이 ID에 커서를 설정하고 앞으로 페이지를 이동합니다.

limit
: 정수. 유형별로 반환할 최대 결과 수입니다. 기본값은 분류마다 20개이며 최대 40개입니다.

offset
: 정수. 처음 n개 결과를 건너뜁니다. `type`도 있을 때만 적용되며 그렇지 않으면 무시합니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

"cats"를 limit=2로 검색한 결과의 일부입니다.

```json
{
  "accounts": [
    {
      "id": "180744",
      "username": "catstar",
      "acct": "catstar@catgram.jp",
      "display_name": "catstar"
      // ...
    },
    {
      "id": "214293",
      "username": "catsareweird",
      "acct": "catsareweird",
      "display_name": "Cats Are Weird"
      // ...
    }
  ],
  "statuses": [
    {
      "id": "103085519055545958",
      "created_at": "2019-11-05T13:23:09.000Z",
      // ...
      "content": "<p>cats<br>cats never change</p>"
      // ...
    },
    {
      "id": "101068121469614510",
      "created_at": "2018-11-14T06:31:48.000Z",
      // ...
      "spoiler_text": "Cats",
      // ...
      "content": "<p>Cats are inherently good at self-care. </p><p><a href=\"https://mspsocial.net/tags/cats\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>cats</span></a></p>"
      // ...
    }
  ],
  "hashtags": [
    {
      "id": "205",
      "name": "cats",
      "url": "https://mastodon.social/tags/cats",
      "history": [
        {
          "day": "1574553600",
          "uses": "10",
          "accounts": "9"
        }
        // ...
      ]
    },
    {
      "id": "708",
      "name": "catsofmastodon",
      "url": "https://mastodon.social/tags/catsofmastodon",
      "history": [
        {
          "day": "1574553600",
          "uses": "6",
          "accounts": "5"
        }
        // ...
      ]
    }
  ]
}
```

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 검색 수행(v1) {{%removed%}} {#v1}

```http
GET /api/v1/search HTTP/1.1
```

**반환:** [Search]({{< relref "entities/Search" >}}), 단 `hashtags`는 Tag 배열 대신 문자열 배열\
**OAuth:** 사용자 토큰 + `read:search`\
**버전 이력:**\
1.1 - 추가, 제한은 5로 고정\
1.5.0 - 이제 인증 필요\
2.4.1 - [v2 검색](#v2)을 권장하며 사용 중단 예정\
2.8.0 - `limit`, 페이지네이션 및 계정 옵션 추가\
3.0.0 - 제거. 대신 [v2 검색](#v2) 사용

#### 요청 {#request-1}

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-1}

q
: {{<required>}} 문자열. 검색어입니다.

type
: 문자열. `accounts`, `hashtags`, `statuses` 중 하나만 검색할지 지정합니다.

resolve
: 불리언. WebFinger 조회를 시도할지 여부입니다. 기본값은 false입니다.

account_id
: 문자열. 제공하면 이 계정이 작성한 게시물만 반환합니다.

max_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 작습니다. 결과의 상한을 설정합니다.

min_id
: 문자열. 이 ID보다 바로 다음으로 새로운 결과를 반환합니다. 이 ID에 커서를 설정하고 앞으로 페이지를 이동합니다.

limit
: 정수. 유형별로 반환할 최대 결과 수입니다. 기본값은 분류마다 20개이며 최대 40개입니다.

offset
: 정수. 페이지네이션에 사용하는 검색 결과 오프셋입니다. 기본값은 0입니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

v1 검색은 해시태그를 Tag 엔터티가 아닌 문자열로 반환하므로 사용 중단 예정이 되었습니다.

```json
{
  "accounts": [...],
  "statuses": [...],
  "hashtags": ["cats","catsofmastodon"]
}
```

##### 401: 인증되지 않음 {#401-unauthorized-1}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 함께 보기 {#see-also}

{{< page-relref ref="methods/accounts#search" caption="GET /api/v1/accounts/search" >}}

{{< page-relref ref="methods/accounts#lookup" caption="GET /api/v1/accounts/lookup" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v2/search_controller.rb" caption="app/controllers/api/v2/search_controller.rb" >}}
