---
title: 애플리케이션 (Application)
description: 계정 정보에 접근하거나 게시물을 올리는 등 REST API와 상호작용하는 애플리케이션을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/application",
	"/entities/Application",
  "/api/entities/application",
	"/api/entities/Application",
]
---

## 예시 {#example}

```json
{
  "id": "12348",
  "name": "Test Application",
  "website": "https://app.example",
  "scopes": ["read", "write", "push"],
  "redirect_uri": "https://app.example/callback\nhttps://app.example/register",
  "redirect_uris": [
    "https://app.example/callback",
    "https://app.example/register"
  ]
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 애플리케이션의 숫자 ID입니다.\
**유형:** 문자열\
**버전 이력:**\
0.9.9 - 추가

### `name` {#name}

**설명:** 애플리케이션 이름입니다.\
**유형:** 문자열\
**버전 이력:**\
0.9.9 - 추가

### `website` {{%optional%}} {#website}

**설명:** 애플리케이션에 연결된 웹사이트입니다.\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
0.9.9 - 추가\
3.5.1 - 이제 이 속성에 null 허용

### `scopes` {#scopes}

**설명:** 애플리케이션의 범위입니다. 등록한 `scopes` 문자열을 공백으로 분리한 값입니다.\
**유형:** 배열: 문자열\
**버전 이력:**\
4.3.0 - 추가

### `redirect_uris` {#redirect_uris}

**설명:** 애플리케이션에 등록된 리디렉션 URI입니다.\
**유형:** 배열: 문자열 (URL 또는 `"urn:ietf:wg:oauth:2.0:oob"` 값)\
**버전 이력:**\
4.3.0 - 추가

### `redirect_uri` {{%deprecated%}} {#redirect_uri}

**설명:** 애플리케이션에 등록된 리디렉션 URI를 단일 문자열로 저장한 값입니다. 여러 URI는 공백 문자로 구분합니다. 여러 리디렉션 URI가 등록되어 있으면 `\n` 문자가 포함될 수 있습니다.\
**유형:** 문자열\
**버전 이력:**\
0.0.0 - 추가\
4.3.0 - 여러 리디렉션 URI가 등록되면 이 속성 값이 올바른 URI가 아니므로 폐기 예정으로 지정. [`redirect_uris`]({{< relref "entities/Application#redirect_uris" >}})로 대체

### `vapid_key` {{%deprecated%}} {#vapid_key}

**설명:** 푸시 스트리밍 API에 사용합니다. [POST /api/v1/apps]({{< relref "methods/apps#create" >}})와 함께 반환됩니다. [WebPushSubscription#server_key]({{< relref "entities/WebPushSubscription#server_key" >}}) 및 [Instance#vapid_public_key]({{< relref "entities/Instance#vapid_public_key" >}})와 같습니다.\
**유형:** 문자열\
**버전 이력:**\
2.8.0 - 추가\
4.3.0 - 제거를 앞두고 폐기 예정으로 지정. 이 값(`configuration.vapid.public_key`)은 [api/v2/instance]({{< relref "methods/Instance#v2">}})를 참고하세요.

## CredentialApplication 속성 {#CredentialApplication}

모든 [Application](#attributes) 속성과 다음 속성입니다.

### `client_id` {#client_id}

**설명:** OAuth 토큰을 얻는 데 사용할 클라이언트 ID 키입니다.\
**유형:** 문자열\
**버전 이력:**\
0.9.9 - 추가\
4.3.0 - `Application`에서 `CredentialApplication`으로 이동

### `client_secret` {#client_secret}

**설명:** OAuth 토큰을 얻는 데 사용할 클라이언트 비밀 키입니다.\
**유형:** 문자열\
**버전 이력:**\
0.9.9 - 추가\
4.3.0 - `Application`에서 `CredentialApplication`으로 이동

### `client_secret_expires_at` {#client_secret_expires_at}

**설명:** 클라이언트 비밀 키의 만료 시각입니다. 현재는 항상 `0`을 반환하며, OAuth 클라이언트가 만료되지 않음을 나타냅니다.\
**유형:** 정수\
**버전 이력:**\
4.4.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/apps" caption="apps API 메서드" >}}

{{< page-relref ref="entities/Status#application" caption="Status (`application` 속성)" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/application_serializer.rb" caption="app/serializers/rest/application_serializer.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/credential_application_serializer.rb" caption="app/serializers/rest/credential_application_serializer.rb" >}}
