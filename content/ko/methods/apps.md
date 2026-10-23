---
title: 앱 API 메서드
description: OAuth 토큰을 얻는 데 사용할 클라이언트 애플리케이션을 등록합니다.
menu:
  docs:
    name: 앱
    parent: methods
    identifier: methods-apps
aliases: ["/methods/apps", "/api/methods/apps"]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 애플리케이션 생성 {#create}

```http
POST /api/v1/apps HTTP/1.1
```

OAuth2 자격 증명을 얻을 새 애플리케이션을 생성합니다.

{{< hint style="danger" >}}
4.3 이전 마스토돈에서는 특정 조건에서 OAuth 애플리케이션이 "정리"되어 데이터베이스에서 제거될 수 있었습니다. 이 경우 마스토돈 서버는 애플리케이션의 `client_id`와 `client_secret`을 인식하지 못합니다.\
이 애플리케이션 자동 제거 기능은 마스토돈 4.3에서 삭제되었습니다.\
\
4.3 이전 버전의 해결 방법은 애플리케이션을 등록한 직후 [클라이언트 자격 증명]({{< relref "client/Token#flow" >}}) 토큰을 요청하는 것이었습니다. 이렇게 하면 애플리케이션이 항상 활성 액세스 토큰을 갖게 되어 영구적으로 제거되지 않습니다.
{{< /hint >}}

{{< hint style="info" >}}
현재 마스토돈은 기밀 클라이언트의 프로비저닝만 지원합니다. 따라서 [CredentialApplication]({{< relref "entities/Application#CredentialApplication" >}}) 엔터티에서 항상 `client_secret`과 `client_secret_expires_at` 속성을 받습니다.\
\
자세한 내용은 [OAuth 2 클라이언트 유형]({{< relref "spec/oauth#client-types" >}})을 참고하세요.
{{< /hint >}}

**반환:** [CredentialApplication]({{< relref "entities/Application#CredentialApplication" >}})\
**OAuth:** 공개\
**버전 이력:**\
0.0.0 - 추가\
2.7.2 - 이제 `vapid_key` 반환\
4.3.0 - `vapid_key` 사용 중단 예정. [api/v2/instance]({{< relref "methods/Instance#v2">}}) 참고\
4.3.0 - 폼 데이터 매개변수에서 여러 `redirect_uris` 지원 추가\
4.3.0 - `redirect_uris` 응답 속성 추가\
4.3.0 - 여러 `redirect_uris`가 등록되면 URI가 아닐 수 있는 `redirect_uri` 응답 속성 사용 중단 예정. 대신 `redirect_uris` 사용\
4.3.0 - 엔터티 유형을 [Application]({{< relref "entities/Application">}})에서 [CredentialApplication]({{< relref "entities/Application#CredentialApplication">}})으로 변경\
4.4.0 - `client_secret_expires_at` 추가

#### 요청 {#create-request-example}

요청 예:

```http
POST /api/v1/apps HTTP/1.1
Content-Type: application/json

{
  "client_name": "Test Application",
  "redirect_uris": ["https://app.example/callback", "https://app.example/register"],
  "scopes": "read write push",
  "website": "https://app.example"
}
```

##### 폼 데이터 매개변수 {#form-data-parameters}

client_name
: {{<required>}} 문자열. 애플리케이션 이름입니다.

redirect_uris
: {{<required>}} 문자열 또는 문자열 배열. 인가 후 사용자를 리디렉션할 위치입니다. 웹페이지로 리디렉션하는 대신 사용자에게 인가 코드를 표시하려면 이 매개변수에 `urn:ietf:wg:oauth:2.0:oob`를 사용하세요.

scopes
: 문자열. 공백으로 구분한 범위 목록입니다. 생략하면 기본값은 `read`입니다. 사용 가능한 범위는 [OAuth 범위]({{< relref "api/oauth-scopes" >}})를 참고하세요.

website
: 문자열. 앱 홈페이지 URL입니다.

#### 응답 {#response}

##### 200: 성공 {#200-ok}

OAuth 토큰을 얻는 데 사용할 `client_id`와 `client_secret`을 캐시에 저장하세요.

{{< hint style="warning" >}}
`client_id`와 `client_secret` 속성을 비밀번호처럼 취급하세요. 자격 증명 노출을 방지하기 위해 캐시에 저장할 때 암호화하는 것을 권장합니다.
{{< /hint >}}

```json
{
  "id": "563419",
  "name": "Test Application",
  "website": "https://app.example",
  "scopes": ["read", "write", "push"],
  "redirect_uri": "urn:ietf:wg:oauth:2.0:oob",
  "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob"],
  "client_id": "TWhM-tNSuncnqN7DBJmoyeLnk6K3iJJ71KKXxgL1hPM",
  "client_secret": "ZEaFUFmF0umgBX1qKJDjaU99Q31lDkOU8NutzTOoliw",
  "client_secret_expires_at": 0
}
```

여러 리디렉션 URI를 사용하는 경우:

```json
{
  "id": "563419",
  "name": "Test Application",
  "website": "https://app.example",
  "scopes": ["read", "write", "push"],
  "redirect_uri": "https://app.example/callback\nhttps://app.example/register",
  "redirect_uris": [
    "https://app.example/callback",
    "https://app.example/register"
  ],
  "client_id": "TWhM-tNSuncnqN7DBJmoyeLnk6K3iJJ71KKXxgL1hPM",
  "client_secret": "ZEaFUFmF0umgBX1qKJDjaU99Q31lDkOU8NutzTOoliw",
  "client_secret_expires_at": 0
}
```

{{< hint style="info" >}}
위 예의 `redirect_uri` 속성은 4.3.0부터 사용 중단 예정이므로 사용하지 말고 대신 `redirect_uris` 속성을 사용해야 합니다.
{{< /hint >}}

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

필수 매개변수가 없거나 형식이 올바르지 않으면 요청이 실패합니다.

```json
{
  "error": "Validation failed: Redirect URI must be an absolute URI."
}
```

---

## 앱 작동 확인 {#verify_credentials}

```http
GET /api/v1/apps/verify_credentials HTTP/1.1
```

앱의 OAuth2 자격 증명이 작동하는지 확인합니다.

**반환:** [Application]({{< relref "entities/application" >}})\
**OAuth:** 앱 토큰\
**버전 이력:**\
2.0.0 - 추가\
2.7.2 - 이제 `vapid_key` 반환\
4.3.0 - `vapid_key` 사용 중단 예정. [api/v2/instance]({{< relref "methods/Instance#v2">}}) 참고\
4.3.0 - 이 API에 접근하기 위한 `read` 범위 요건 제거. 이제 유효한 앱 토큰이면 모두 사용 가능\
4.3.0 - `scopes` 및 `redirect_uris` 속성 추가

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 인증된 접근을 하려면 `Bearer <app_token>`을 이 헤더로 제공하세요. `<app_token>`은 [`/oauth/token`]({{< relref "methods/oauth#token" >}})이 반환한 `client_credential` 또는 `access_token`일 수 있습니다.

#### 응답 {#response-1}

##### 200: 성공 {#200-ok-1}

Authorization 헤더에 유효한 토큰을 제공하면 앱이 Application 엔터티로 반환됩니다.

```json
{
  "id": "563419",
  "name": "Test Application",
  "website": "https://app.example",
  "scopes": ["read", "write", "push"],
  "redirect_uri": "https://app.example/callback\nhttps://app.example/register",
  "redirect_uris": [
    "https://app.example/callback",
    "https://app.example/register"
  ],
  "vapid_key": "BMAIjoaMYTDbJtfrfocuzO8pzDHI47dzmw0rha6Y=",
}
```

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더의 토큰이 유효하지 않거나, 헤더 형식이 잘못되었거나, 헤더가 없으면 인증 실패를 나타내는 오류를 반환합니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/apps_controller.rb" caption="app/controllers/api/v1/apps_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/apps/credentials_controller.rb" caption="app/controllers/api/v1/apps/credentials_controller.rb" >}}
