---
title: 클라이언트 앱 접근 권한 얻기
description: 인증과 인가의 기초에 익숙해지기
menu:
  docs:
    weight: 30
    parent: client
---

## 인증과 인가 {#auth}

지금까지는 공개 정보를 다뤘지만 모든 정보가 공개되는 것은 아닙니다. 일부 정보는 누가 요청하는지 감사하고 필요하면 접근 권한을 취소하거나 거부할 수 있도록, 보기 전에 권한이 필요합니다.

이때 [OAuth]({{< relref "spec/oauth" >}})를 사용합니다. OAuth는 요청이 특정 클라이언트에서 왔음을 _인증(확인)_하고 요청한 동작이 서버의 접근 제어 정책에 따라 _인가(허용)_되었는지 보장하는 데 사용할 액세스 토큰을 생성하는 메커니즘입니다.

## 애플리케이션 만들기 {#app}

먼저 나중에 액세스 토큰을 생성할 수 있도록 애플리케이션을 등록해야 합니다. 다음과 같이 만들 수 있습니다.

```bash
curl -X POST \
	-F 'client_name=Test Application' \
	-F 'redirect_uris=urn:ietf:wg:oauth:2.0:oob' \
	-F 'scopes=read write push' \
	-F 'website=https://myapp.example' \
	https://mastodon.example/api/v1/apps
```

위 예제에서는 클라이언트 이름과 웹사이트를 지정했으며, 해당하는 경우 게시물에 표시됩니다. 특히 다음 두 매개변수에 주목합니다.

- `redirect_uris`는 “대역 외” 토큰 생성으로 설정되어 있어 생성된 토큰을 수동으로 복사하여 붙여 넣어야 합니다. 리디렉션 URI를 여러 개 정의할 수 있어서 매개변수 이름이 `redirect_uris`이지만, 토큰을 생성할 때는 이 목록에 포함된 URI 하나를 제공해야 합니다.
- `scopes`는 나중에 요청할 수 있는 권한을 정의합니다. 다만 나중에 요청하는 범위는 등록한 범위의 일부일 수도 있습니다. 자세한 내용은 [OAuth 범위]({{< relref "api/oauth-scopes" >}})를 확인합니다.

[POST /api/v1/apps]({{< relref "methods/apps#create-request-example" >}})에 설명된 대로 같은 엔드포인트에 JSON 본문을 POST하여 애플리케이션을 만들 수도 있습니다.

{{< hint style="info" >}}
마스토돈 4.3.0부터는 [`/.well-known/oauth-authorization-server`]({{< relref "methods/oauth#authorization-server-metadata" >}}) 엔드포인트에 요청하여 서버가 지원하는 `scopes` 및 기타 정보를 알아낼 수 있습니다.
{{< /hint >}}

[CredentialApplication]({{< relref "entities/application#CredentialApplication" >}}) 엔터티가 반환되지만, 지금 필요한 것은 `client_id`와 `client_secret`뿐입니다.

`client_id`와 `client_secret` 값은 액세스 토큰을 생성하는 데 사용하므로 나중을 위해 캐시해야 합니다. 애플리케이션 등록의 자세한 내용은 [POST /api/v1/apps]({{< relref "methods/apps#create" >}})를 확인합니다.

{{< hint style="warning" >}}
`client_id`와 `client_secret` 속성은 비밀번호처럼 취급합니다. 실수로 자격 증명이 노출되지 않도록 캐시에 저장할 때 암호화하는 것을 권장합니다.
{{< /hint >}}

## 인증 코드 흐름 예제 {#flow}

이제 애플리케이션이 있으므로 요청을 해당 클라이언트 애플리케이션으로 인증할 액세스 토큰을 얻어 봅니다. 다음과 같이 [POST /oauth/token]({{< relref "methods/oauth#token" >}})을 사용합니다.

```bash
curl -X POST \
	-F 'client_id=your_client_id_here' \
	-F 'client_secret=your_client_secret_here' \
	-F 'redirect_uri=urn:ietf:wg:oauth:2.0:oob' \
	-F 'grant_type=client_credentials' \
	https://mastodon.example/oauth/token
```

다음 사항에 주목합니다.

- `client_id`와 `client_secret`은 애플리케이션 등록 시 응답 텍스트로 제공되었습니다.
- `redirect_uri`는 애플리케이션 등록 시 정의한 URI 중 하나여야 합니다.
- `grant_type`으로 `client_credentials`를 요청하며, 기본적으로 `read` 범위가 부여됩니다.

이 메서드는 [Token]({{< relref "entities/token" >}}) 엔터티로 응답합니다. 필요한 값은 `access_token`입니다. 액세스 토큰을 얻으면 로컬 캐시에 저장합니다.

{{< hint style="warning" >}}
`access_token`은 비밀번호처럼 취급합니다. 실수로 자격 증명이 노출되지 않도록 캐시에 저장할 때 이 값을 암호화하는 것을 권장합니다.
{{< /hint >}}

요청에서 사용하려면 OAuth가 필요한, 즉 공개적으로 접근할 수 없는 API 호출에 HTTP 헤더 `Authorization: Bearer <access_token>`을 추가합니다.

[GET /api/v1/apps/verify_credentials]({{< relref "methods/apps#verify_credentials" >}})를 호출하여 얻은 자격 증명이 작동하는지 확인해 봅니다.

```bash
curl \
	-H 'Authorization: Bearer <access_token>' \
	https://mastodon.example/api/v1/apps/verify_credentials
```

토큰을 얻고 요청 형식을 올바르게 구성했다면 세부 정보가 `client_secret` 속성이 없는 [Application]({{< relref "entities/application" >}}) 엔터티로 반환됩니다.

## 인증으로 할 수 있는 일 {#methods}

인증된 클라이언트 애플리케이션에서는 [GET /api/v1/accounts/:id/following]({{< relref "methods/accounts#following" >}})과 [GET /api/v1/accounts/:id/followers]({{< relref "methods/accounts#followers" >}})로 계정의 관계를 볼 수 있습니다. 또한 일부 서버는 보통 공개되는 메서드에도 인증을 요구하므로, 공개 메서드를 시험하면서 인증 오류를 만났다면 이제 해당 메서드도 작동할 것입니다.
