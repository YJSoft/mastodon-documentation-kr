---
title: OAuth API 메서드
description: OAuth 토큰을 생성하고 관리합니다.
menu:
  docs:
    name: OAuth
    parent: methods-apps
    identifier: methods-oauth
aliases: ["/methods/oauth", "/api/methods/oauth", "/methods/apps/oauth"]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 사용자 인가 {#authorize}

```http
GET /oauth/authorize HTTP/1.1
```

사용자에게 인가 양식을 표시합니다. 승인하면 인가 코드를 생성하여 반환한 다음 원하는 `redirect_uri`로 리디렉션하거나, `urn:ietf:wg:oauth:2.0:oob`가 요청되었으면 인가 코드를 표시합니다. 이 코드는 사용자 수준 메서드에 접근할 토큰을 요청할 때 사용할 수 있습니다.

**반환:** 문자열(URL) 또는 HTML 응답\
**OAuth:** 공개\
**버전 이력:**\
0.1.0 - 추가\
2.6.0 - `force_login` 추가\
3.5.0 - `lang` 추가\
4.3.0 - PKCE 매개변수 지원 추가\
5.0.0 - `prompt` 및 `invite_code` 매개변수 추가

#### 요청 {#request}

##### 쿼리 매개변수 {#query-parameters}

response_type
: {{<required>}} 문자열. `code`로 설정해야 합니다.

client_id
: {{<required>}} 문자열. 앱 등록 시 얻은 클라이언트 ID입니다.

redirect_uri
: {{<required>}} 문자열. 사용자를 리디렉션할 URI를 설정합니다. 이 매개변수를 `urn:ietf:wg:oauth:2.0:oob`로 설정하면 대신 인가 코드를 표시합니다. 앱 등록 시 선언한 `redirect_uris` 중 하나와 일치해야 합니다.

scope
: 문자열. 공백(쿼리 매개변수를 사용하는 경우 더하기 기호)으로 구분한 요청 [OAuth 범위]({{< relref "api/oauth-scopes" >}}) 목록입니다. 앱 등록 시 선언한 `scopes`의 부분집합이어야 합니다. 생략하면 기본값은 `read`입니다.

state
: 문자열. 사용자가 인가 요청을 승인하거나 거절할 때 서버에 전달할 임의의 값입니다.

code_challenge
: 문자열. 인가 요청의 [PKCE 코드 챌린지]({{< relref "spec/oauth#pkce" >}})입니다.

code_challenge_method
: 문자열. 마스토돈이 PKCE에 지원하는 유일한 코드 챌린지 방식인 `S256`이어야 합니다.

force_login
: 불리언. 사용자가 다시 로그인하도록 강제합니다. 같은 서버의 여러 계정으로 인가하려면 필요합니다.

lang
: 문자열. 인가 양식을 표시할 때 사용할 ISO 639-1 두 글자 언어 코드입니다.

prompt
: 문자열(열거형, `create`, `login` 중 하나). OpenID Connect의 `prompt`입니다.\
`create` = 로그인 대신 가입 절차로 진입합니다. 이미 로그인한 사용자는 먼저 로그아웃하라는 안내를 받습니다.\
`login` = 사용자에게 다시 로그인을 요구합니다. 이미 로그인했다면 먼저 로그아웃하라는 안내를 받습니다.

invite_code
: 문자열. 가입 초대를 따를 때 `prompt=create`와 함께 사용할 초대 코드입니다. 초대 코드는 `https://example.com/invite/:invite_code` 형태의 마스토돈 초대 URL에서 마지막 경로 부분입니다.

#### 응답 {#response}

##### 200: 성공 {#200-ok}

인가 코드는 `code`라는 쿼리 매개변수로 반환됩니다.

{{< hint style="warning" >}}
`code` 쿼리 매개변수를 비밀번호처럼 취급하고 요청 로그에 기록되지 않도록 해야 합니다.
{{< /hint >}}

```http
redirect_uri?code=qDFUEaYrRK5c-HNmTCJbAzazwLRInJ7VHFat0wcMgCU
```

state 매개변수를 사용했다면 클라이언트가 리디렉션될 때 URI에도 포함됩니다.

```http
redirect_uri?code=qDFUEaYrRK5c-HNmTCJbAzazwLRInJ7VHFat0wcMgCU&state=example
```

##### 400: 클라이언트 오류 {#400-client-error}

인가 코드가 올바르지 않거나 이미 사용되었으면 요청이 실패합니다.

```json
{
  "error": "invalid_grant",
  "error_description": "The provided authorization grant is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client."
}
```

---

## 토큰 얻기 {#token}

```http
POST /oauth/token HTTP/1.1
```

공개되지 않은 API 호출에 사용할 액세스 토큰을 얻습니다.

**반환:** [Token]({{< relref "entities/token" >}})\
**OAuth:** 공개\
**버전 이력:**\
0.1.0 - 추가\
4.3.0 - PKCE 매개변수 지원 추가

#### 요청 {#request-1}

##### 폼 데이터 매개변수 {#form-data-parameters}

grant_type
: {{<required>}} 문자열. 사용자 수준 접근을 얻기 위해 `code`를 제공하는 경우 `authorization_code`로 설정합니다. 그렇지 않으면 앱 수준 접근만 얻도록 `client_credentials`로 설정합니다.

code
: {{<required>}} 문자열. [인가 요청](#authorize)이 승인된 뒤 리디렉션에서 얻은 사용자 인가 코드입니다. `redirect_uri`로 `urn:ietf:wg:oauth:2.0:oob`를 사용하면 사용자에게 직접 표시될 수도 있습니다.

client_id
: {{<required>}} 문자열. 앱 등록 시 얻은 클라이언트 ID입니다.

client_secret
: {{<required>}} 문자열. 앱 등록 시 얻은 클라이언트 시크릿입니다.

redirect_uri
: {{<required>}} 문자열. [인가 요청](#authorize)에 사용한 `redirect_uri`와 일치해야 합니다.

code_verifier
: 문자열. 인가 요청에서 [PKCE]({{< relref "spec/oauth#pkce" >}})를 사용했다면 필수입니다. 인가 요청에서 `code_challenge_method`를 사용하여 `code_challenge`를 생성한 코드 검증자입니다.

scope
: 문자열. `grant_type`이 `client_credentials`일 때 요청하는 OAuth 범위 목록이며 공백(쿼리 매개변수에서는 더하기 기호)으로 구분합니다. 애플리케이션 생성 시 요청한 범위의 부분집합이어야 합니다. 생략하면 기본값은 `read`입니다. `grant_type`이 `authorization_code`이면 효과가 없습니다.

#### 응답 {#response-1}

##### 200: 성공 {#200-ok-1}

나중에 인증이 필요한 메서드에서 사용할 수 있도록 `access_token`을 저장하세요. API 호출 시 `Bearer <access_token>` 값을 HTTP `Authorization` 헤더로 전달해야 합니다.

{{< hint style="warning" >}}
`access_token`을 비밀번호처럼 취급하세요. 자격 증명 노출을 방지하려면 캐시에 저장할 때 암호화하는 것을 권장합니다.\
\
또한 `code` 매개변수가 로그에 기록되지 않도록 해야 합니다.
{{< /hint >}}

```json
{
  "access_token": "ZA-Yj3aBD8U8Cm7lKUp-lm9O9BmDgdhHzDeqsY8tlL0",
  "token_type": "Bearer",
  "scope": "read write follow push",
  "created_at": 1573979017
}
```

##### 400: 클라이언트 오류 {#400-client-error-1}

앱 등록 시 포함하지 않은 범위를 요청하면 요청이 실패합니다.

```json
{
  "error": "invalid_scope",
  "error_description": "The requested scope is invalid, unknown, or malformed."
}
```

##### 401: 인증되지 않음 {#401-unauthorized}

client_id와 client_secret이 일치하지 않거나 유효하지 않으면 요청이 실패합니다.

```json
{
  "error": "invalid_client",
  "error_description": "Client authentication failed due to unknown client, no client authentication included, or unsupported authentication method."
}
```

---

## 토큰 취소 {#revoke}

```http
POST /oauth/revoke HTTP/1.1
```

액세스 토큰을 취소하여 더 이상 사용할 수 없게 합니다.

**반환:** 없음\
**OAuth:** 공개\
**버전 이력:**\
0.1.0 - 추가

#### 요청 {#request-2}

##### 폼 데이터 매개변수 {#form-data-parameters-1}

client_id
: {{<required>}} 문자열. 앱 등록 시 얻은 클라이언트 ID입니다.

client_secret
: {{<required>}} 문자열. 앱 등록 시 얻은 클라이언트 시크릿입니다.

token
: {{<required>}} 문자열. 무효화할, 이전에 얻은 토큰입니다.

#### 응답 {#response-2}

##### 200: 성공 {#200-ok-2}

제공한 토큰이 내 소유이면 API 호출은 빈 응답을 제공합니다. 멱등 작업이므로 여러 번 호출해도 성공을 반환합니다.

```json
{}
```

##### 403: 금지됨 {#403-forbidden}

내 소유가 아닌 토큰을 제공하거나 토큰을 전혀 제공하지 않으면 API 호출은 403 오류를 반환합니다.

```json
{
  "error": "unauthorized_client",
  "error_description": "You are not authorized to revoke this token"
}
```

---

## 사용자 정보 조회 {#userinfo}

```http
GET /oauth/userinfo HTTP/1.1
```

현재 인증된 사용자에 대한 표준 OIDC [클레임](https://www.iana.org/assignments/jwt/jwt.xhtml#claims)을 가져옵니다.\
**참고:** [OIDC 명세](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo)와의 호환성을 위해 `POST` 요청으로도 이 엔드포인트를 사용할 수 있습니다.

**OAuth:** 사용자 토큰 + `profile` 범위\
**버전 이력:**\
4.4.0 - 추가

#### 응답 {#response-3}

##### 200: 성공 {#200-ok-3}

```json
{
  "iss": "http://social.example/",
  "sub": "http://social.example/users/john_mastodon",
  "name": "John Mastodon",
  "preferred_username": "john_mastodon",
  "profile": "http://social.example/@john_mastodon",
  "picture": "http://cdn.social.example/media/accounts/avatars/112/570/037/924/789/254/original/d746f9fb43a5705f.jpg"
}
```

인증된 사용자의 클레임은 다음과 같습니다.
* `iss`는 [OAuth 서버 구성]({{< relref "methods/oauth#authorization-server-metadata" >}})의 `issuer`와 일치합니다.
* `sub`는 ActivityPub Actor 문서의 URI입니다.
* `name`은 프로필의 표시 이름입니다. 사용자 지정 이모지의 단축 코드가 포함될 수 있습니다.
* `preferred_username`은 프로필의 사용자명입니다. 예를 들어 `@john_mastodon@social.example` 계정의 `preferred_username`은 `john_mastodon`입니다.
* `profile`은 프로필 페이지의 URL입니다(사람이 보도록 의도한 URL).
* `picture`는 프로필 사진 URL입니다(기본 프로필 사진 URL일 수도 있음).

Account 엔터티의 [`id`]({{< relref "entities/Account#id">}})는 전역적으로 고유하다는 보장이 없어 사용하는 애플리케이션에서 충돌이 발생할 수 있으므로, `sub` 클레임에는 ActivityPub Actor 문서의 URI를 사용합니다.

##### 401: 인증되지 않음 {#401-unauthorized-1}

액세스 토큰이 유효하지 않으면 반환합니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 403: 금지됨 {#403-forbidden-1}

액세스 토큰에 `profile` 범위가 없으면 반환합니다.

```json
{
  "error": "This action is outside the authorized scopes"
}
```

---

## OAuth 서버 구성 탐색 {#authorization-server-metadata}

```http
GET /.well-known/oauth-authorization-server HTTP/1.1
```

[RFC 8414](https://datatracker.ietf.org/doc/html/rfc8414#section-3.2)에 정의된 마스토돈 서버의 OAuth 2 인가 서버 메타데이터를 반환합니다.

현재 [동적 클라이언트 등록](https://oauth.net/2/dynamic-client-registration/)용 표준 `registration_endpoint` 엔드포인트를 지원하지 않으므로 [POST /api/v1/apps]({{< relref "methods/apps#create" >}})를 가리키는 비표준 추가 속성 `app_registration_endpoint`를 포함합니다.

이 엔드포인트가 공개하는 속성은 서로 다른 마스토돈 버전 간 `scopes` 협상 등 마스토돈 API와의 통합을 개선하는 데 도움이 됩니다.

{{< hint style="info" >}}
**예:** `profile` 범위를 사용하면서 해당 범위가 없어 `read:accounts`가 필요한 이전 마스토돈 서버도 지원하려고 합니다. 이 엔드포인트에 요청하여 서버의 범위 지원 여부를 알아볼 수 있습니다.
{{< /hint >}}

**반환:** 위 설명에 따른 JSON\
**OAuth:** 공개\
**버전 이력:**\
4.3.0 - 추가\
4.4.0 - `userinfo_endpoint` 추가\
5.0.0 - `prompt_values_supported` 추가

#### 응답 {#response-4}

##### 200: 성공 {#200-ok-4}

```json
{
  "issuer": "https://social.example/",
  "service_documentation": "https://docs.joinmastodon.org/",
  "authorization_endpoint": "https://social.example/oauth/authorize",
  "token_endpoint": "https://social.example/oauth/token",
  "app_registration_endpoint": "https://social.example/api/v1/apps",
  "revocation_endpoint": "https://social.example/oauth/revoke",
  "userinfo_endpoint": "https://social.example/oauth/userinfo",
  "scopes_supported": [
    "read",
    "write",
    "write:accounts",
    "write:blocks",
    "write:bookmarks",
    "write:conversations",
    "write:favourites",
    "write:filters",
    "write:follows",
    "write:lists",
    "write:media",
    "write:mutes",
    "write:notifications",
    "write:reports",
    "write:statuses",
    "read:accounts",
    "read:blocks",
    "read:bookmarks",
    "read:favourites",
    "read:filters",
    "read:follows",
    "read:lists",
    "read:mutes",
    "read:notifications",
    "read:search",
    "read:statuses",
    "follow",
    "push",
    "profile",
    "admin:read",
    "admin:read:accounts",
    "admin:read:reports",
    "admin:read:domain_allows",
    "admin:read:domain_blocks",
    "admin:read:ip_blocks",
    "admin:read:email_domain_blocks",
    "admin:read:canonical_email_blocks",
    "admin:write",
    "admin:write:accounts",
    "admin:write:reports",
    "admin:write:domain_allows",
    "admin:write:domain_blocks",
    "admin:write:ip_blocks",
    "admin:write:email_domain_blocks",
    "admin:write:canonical_email_blocks"
  ],
  "response_types_supported": ["code"],
  "response_modes_supported": ["query", "fragment", "form_post"],
  "code_challenge_methods_supported": [
    "S256"
  ],
  "grant_types_supported": [
    "authorization_code",
    "client_credentials"
  ],
  "token_endpoint_auth_methods_supported": [
    "client_secret_basic",
    "client_secret_post"
  ],
  "prompt_values_supported": [
    "create",
    "login"
  ]
}
```

##### 이전 마스토돈 버전 – 404: 찾을 수 없음 {#older-mastodon-versions--404-not-found}

마스토돈 4.3.0 이전 버전에서 이 엔드포인트를 요청하면 `404 Not Found` 오류가 발생합니다.

지원되는 OAuth 2 엔드포인트, 인가 흐름, 범위를 동적으로 탐색하는 대신 해당 서버의 지원 내용을 "추측"해야 합니다.

[서버 메타데이터 엔드포인트]({{< relref "methods/instance#v2" >}})의 `version` 필드를 해석해 실행 중인 마스토돈 버전을 알아내는 대체 방법을 고려할 수 있지만, 이는 매우 불안정하여 권장하지 않습니다.

---

## 함께 보기 {#see-also}

{{< page-relref ref="methods/apps#create" caption="POST /api/v1/apps" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/oauth/authorizations_controller.rb" caption="app/controllers/oauth/authorizations_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/oauth/authorized_applications_controller.rb" caption="app/controllers/oauth/authorized_applications_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/oauth/tokens_controller.rb" caption="app/controllers/oauth/tokens_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/oauth/userinfo_controller.rb" caption="app/controllers/oauth/userinfo_controller.rb" >}}
