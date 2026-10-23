---
title: 계정으로 로그인하기
description: 사용자의 인가를 얻어 사용자를 대신하여 작업을 수행하는 방법
menu:
  docs:
    weight: 40
    parent: client
---

## 범위 설명 {#scopes}

앱을 등록할 때와 사용자에게 인가를 받을 때, 생성할 토큰에 정확히 어떤 작업 권한을 부여할지 정의해야 합니다. 이를 위해 [OAuth 범위]({{< relref "api/oauth-scopes" >}})를 사용합니다. 각 API 메서드에는 연결된 범위가 있으며, 인가에 사용하는 토큰이 해당 범위로 생성된 경우에만 호출할 수 있습니다.

사용자에게 인가를 받을 때 `scope` 쿼리 매개변수는 앱 생성 시 지정한 범위의 부분집합이어야 합니다. 지금까지의 예제에서는 앱 생성 시 `read write push`를 범위로 지정했지만, [세분화된 범위]({{< relref "api/oauth-scopes#granular-scopes" >}})로 앱에 실제로 필요한 접근 권한만 요청하는 것이 좋습니다.

전체 범위 목록은 [OAuth 범위]({{< relref "api/oauth-scopes" >}})를 확인합니다. 각 API 메서드 문서에도 호출에 필요한 OAuth [토큰 유형]({{< relref "api/oauth-tokens" >}})과 범위가 명시되어 있습니다. 범위는 계층적이므로, 엔드포인트가 `read:statuses`를 지정하고 `read` 접근 권한이 있다면 해당 엔드포인트를 사용할 수 있습니다.

{{< page-relref ref="api/oauth-scopes" caption="OAuth 범위" >}}

## **인가 코드 흐름 예제** {#flow}

앞서 본 인증 흐름과 비슷하지만 이번에는 사용자에게서도 인가를 받아야 합니다.

### 클라이언트 ID와 비밀 키 {#client}

먼저 클라이언트 애플리케이션을 아직 등록하지 않았다면 이전 페이지의 [애플리케이션 만들기]({{< relref "client/token#app" >}})를 보거나, 메서드의 전체 문서인 [POST /api/v1/apps]({{< relref "methods/apps#create" >}})를 바로 확인합니다. 애플리케이션의 `client_id`와 `client_secret`이 필요합니다.

### 사용자 인가 받기 {#login}

사용자에게 인가를 받으려면 브라우저에서 다음 쿼리 매개변수로 [GET /oauth/authorize]({{< relref "methods/oauth#authorize" >}})를 요청합니다.

```bash
https://mastodon.example/oauth/authorize
?client_id=CLIENT_ID
&scope=read+write+push
&redirect_uri=urn:ietf:wg:oauth:2.0:oob
&response_type=code
```

다음 사항에 주목합니다.

* `client_id`는 애플리케이션 등록 시 얻었습니다.
* `scope`는 앱에 등록된 범위의 부분집합이어야 합니다. 필요한 권한만 요청하는 것이 좋습니다. 자세한 내용은 [OAuth 범위]({{< relref "api/oauth-scopes" >}})를 확인합니다.
* `redirect_uri`는 앱에 등록한 URI 중 하나입니다.

이 예제에서는 계속 “대역 외” 방식을 사용하므로 결과 코드를 직접 복사하여 붙여 넣어야 합니다. 하지만 제어할 수 있는 URI로 애플리케이션을 등록했다면 리디렉션 URI의 요청 처리기가 쿼리 매개변수 `code`로 코드를 받습니다. 자세한 내용은 API 메서드 문서의 응답 절을 확인합니다.

{{< hint style="warning" >}}
`code` 쿼리 매개변수는 비밀번호처럼 취급하며 요청 로그에 기록되지 않도록 해야 합니다.
{{< /hint >}}

### 토큰 얻기 {#token}

이제 인가 `code`가 있으므로 인가한 사용자로 요청을 인증할 액세스 토큰을 얻어 봅니다. 앞서와 같이 [POST /oauth/token]({{< relref "methods/oauth#token" >}})을 사용하되 방금 얻은 인가 코드를 전달합니다.

```bash
curl -X POST \
	-F 'grant_type=authorization_code' \
	-F 'client_id=your_client_id_here' \
	-F 'client_secret=your_client_secret_here' \
	-F 'redirect_uri=urn:ietf:wg:oauth:2.0:oob' \
	-F 'code=user_authzcode_here' \
	https://mastodon.example/oauth/token
```

다음 사항에 주목합니다.

- `grant_type`으로 `authorization_code`를 요청합니다.
- `client_id`와 `client_secret`은 애플리케이션 등록 시 응답 텍스트로 제공되었습니다.
- `redirect_uri`는 애플리케이션 등록 시 정의한 URI 중 하나여야 합니다.
- `code`는 한 번만 사용할 수 있습니다. 새 토큰이 필요하다면 위의 [사용자 인가 받기]({{< relref "client/authorized#login" >}}) 단계를 반복하여 사용자가 다시 인가하도록 해야 합니다.

이 메서드는 [Token]({{< relref "entities/token" >}}) 엔터티로 응답합니다. 필요한 값은 `access_token`입니다. 액세스 토큰을 얻으면 로컬 캐시에 저장합니다.

생성된 액세스 토큰의 `scope`는 [인가 요청]({{< relref "client/authorized#login" >}}) 중 승인한 범위가 됩니다.

{{< hint style="warning" >}}
`access_token`은 비밀번호처럼 취급합니다. 실수로 자격 증명이 노출되지 않도록 캐시에 저장할 때 이 값을 암호화하는 것을 권장합니다.
{{< /hint >}}

요청에서 사용하려면 OAuth가 필요한, 즉 공개적으로 접근할 수 없는 API 호출에 HTTP 헤더 `Authorization: Bearer <access_token>`을 추가합니다.

[GET /api/v1/accounts/verify_credentials]({{< relref "methods/accounts#verify_credentials" >}})를 호출하여 얻은 자격 증명이 작동하는지 확인해 봅니다.

```bash
curl \
	-H 'Authorization: Bearer <access_token>' \
	https://mastodon.example/api/v1/accounts/verify_credentials
```

토큰을 얻고 요청 형식을 올바르게 구성했다면 세부 정보가 `source` 매개변수를 포함한 [Account]({{< relref "entities/account" >}}) 엔터티로 반환됩니다.

## 인가한 사용자로 작업 수행하기 {#actions}

이제 인가한 사용자의 OAuth 토큰으로 토큰 범위 안의 모든 작업을 해당 사용자로 수행할 수 있습니다.

### 게시물 게시와 삭제 {#statuses}

- 게시물을 만드는 방법은 [POST /api/v1/statuses]({{< relref "methods/statuses#create" >}})를 확인합니다.
  - 미디어 첨부 파일을 만드는 방법은 [/api/v1/media]({{< relref "methods/media" >}})를 확인합니다.
  - 예약 게시물 관리는 [/api/v1/scheduled_statuses]({{< relref "methods/scheduled_statuses" >}})를 확인합니다.

### 타임라인과 상호작용하기 {#timelines}

- 타임라인 접근은 [/api/v1/timelines]({{< relref "methods/timelines" >}})를 확인합니다.
- 타임라인 위치를 저장하고 불러오는 방법은 [/api/v1/markers]({{< relref "methods/markers" >}})를 확인합니다.
- 게시물에 대한 작업은 [/api/v1/statuses]({{< relref "methods/statuses" >}})를 확인합니다.
  - 투표 보기와 투표 참여는 [/api/v1/polls]({{< relref "methods/polls" >}})를 확인합니다.
- [GET /api/v1/timelines/list/:list_id]({{< relref "methods/timelines#list" >}})에 사용할 리스트 ID를 얻으려면 [/api/v1/lists]({{< relref "methods/lists" >}})를 확인합니다.
- 개인 대화를 가져오는 방법은 [/api/v1/conversations]({{< relref "methods/conversations" >}})를 확인합니다.
- 좋아요 목록은 [/api/v1/favourites]({{< relref "methods/favourites" >}})를 확인합니다.
- 북마크 목록은 [/api/v1/bookmarks]({{< relref "methods/bookmarks" >}})를 확인합니다.

### 다른 사용자와 상호작용하기 {#accounts}

- 다른 사용자에 대한 작업은 [/api/v1/accounts]({{< relref "methods/accounts" >}})를 확인합니다.
- 팔로우 요청 처리는 [/api/v1/follow_requests]({{< relref "methods/follow_requests" >}})를 확인합니다.
- 뮤트 목록은 [/api/v1/mutes]({{< relref "methods/mutes" >}})를 확인합니다.
- 차단 목록은 [/api/v1/blocks]({{< relref "methods/blocks" >}})를 확인합니다.

### 알림 받기 {#notifications}

- 사용자 알림 관리는 [/api/v1/notifications]({{< relref "methods/notifications" >}})를 확인합니다.
- 푸시 알림 구독은 [/api/v1/push]({{< relref "methods/push" >}})를 확인합니다.

### 탐색 기능 {#discovery}

- 리소스 검색은 [/api/v2/search]({{< relref "methods/search#v2" >}})를 확인합니다.
- 팔로우할 추천 계정은 [/api/v1/suggestions]({{< relref "methods/suggestions" >}})를 확인합니다.

### 사용자 안전 기능 {#safety}

- 필터링할 키워드 관리는 [/api/v1/filters]({{< relref "methods/filters" >}})를 확인합니다.
- 차단한 도메인 관리는 [/api/v1/domain_blocks]({{< relref "methods/domain_blocks" >}})를 확인합니다.
- 신고 작성은 [/api/v1/reports]({{< relref "methods/reports" >}})를 확인합니다.
- 중재자 작업은 [/api/v1/admin]({{< relref "methods/admin" >}})를 확인합니다.

### 계정 정보 관리 {#manage}

- 사용자 프로필의 추천 계정 관리는 [/api/v1/endorsements]({{< relref "methods/endorsements" >}})를 확인합니다.
- 사용자 프로필의 추천 해시태그 관리는 [/api/v1/featured_tags]({{< relref "methods/featured_tags" >}})를 확인합니다.
- 사용자 환경설정 읽기는 [/api/v1/preferences]({{< relref "methods/preferences" >}})를 확인합니다.
