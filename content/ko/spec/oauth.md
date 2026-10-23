---
title: OAuth
description: 인터넷의 토큰 기반 인증 및 인가를 위한 개방형 표준입니다.
menu:
  docs:
    weight: 50
    parent: spec
---

## OAuth란 무엇인가요? {#intro}

마스토돈 API에는 클라이언트 인증이나 사용자 인가가 필요한 메서드가 많습니다. 이를 위해 [RFC 6749](https://tools.ietf.org/html/rfc6749)에 설명된 인가 프레임워크 OAuth 2.0을 사용합니다. 리소스 소유자를 대신하여 타사 애플리케이션이 HTTP 서비스에 제한적으로 접근하도록 하며, 표준 인가 흐름으로 HTTP 요청에 사용할 클라이언트 액세스 토큰을 생성합니다.

마스토돈 웹사이트의 OAuth 토큰을 얻으려면 로그인 전에 사용자가 연결할 도메인을 지정할 수 있게 해야 합니다. 해당 도메인에서 [클라이언트 ID/비밀 키를 얻은]({{< relref "methods/apps#create" >}}) 다음 [일반 OAuth 2 절차를 진행합니다]({{< relref "methods/oauth" >}}).

## OAuth 2 클라이언트 유형 {#client-types}

OAuth 2는 인가 서버에 안전하게 인증할 수 있는 능력(즉, 클라이언트 자격 증명의 기밀을 유지하는 능력)에 따라 `confidential`과 `public` 두 클라이언트 유형을 정의합니다. 기밀 클라이언트는 [클라이언트 자격 증명 부여 흐름]({{<relref "client/token#flow" >}})을 사용할 수 있지만 공개 클라이언트는 사용할 수 없습니다.

현재 마스토돈은 기밀 클라이언트만 지원하지만 공개 클라이언트 지원을 추가하는 [작업이 진행 중입니다](https://github.com/mastodon/mastodon/pull/30329).

## 구현된 OAuth 2 엔드포인트 {#implementation}

다음 설명은 [Doorkeeper 문서](https://github.com/doorkeeper-gem/doorkeeper/wiki/API-endpoint-descriptions-and-examples)에서 가져왔습니다. 마스토돈은 Doorkeeper로 OAuth 2를 구현합니다. 이 엔드포인트의 사용법은 [OAuth API 문서]({{< relref "methods/oauth" >}})를 참고하세요.

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/config/initializers/doorkeeper.rb" caption="Doorkeeper 구성 초기화 코드" >}}

### 인가 서버 메타데이터 엔드포인트 ([RFC 8414](https://www.rfc-editor.org/rfc/rfc8414.html)) {#authorization-server-metadata}

마스토돈의 OAuth 2 서버 구성을 나타내는 JSON 문서를 반환합니다. [애플리케이션 등록]({{% relref "methods/apps#create" %}}) 또는 [액세스 토큰 요청]({{% relref "methods/oauth#token" %}})에 사용할 수 있는 `scopes`, 액세스 토큰 요청에 사용할 수 있는 `grant_types_supported`, `authorization_endpoint`와 `token_endpoint` 등 마스토돈 OAuth 서버와 상호작용할 여러 엔드포인트 정보를 포함합니다.

**버전 이력:**\
4.3.0 - 추가

{{< page-relref ref="methods/oauth#authorization-server-metadata" caption="GET /.well-known/oauth-authorization-server" >}}

### 동적 클라이언트 등록 엔드포인트 ([RFC 7591](https://www.rfc-editor.org/rfc/rfc7591.html)) {#dynamic-client-registration}

현재 마스토돈은 동적 클라이언트 등록 프로토콜을 지원하지 않지만 OAuth 애플리케이션을 등록하는 자체 엔드포인트는 지원합니다.

{{< page-relref ref="methods/apps#create" caption="POST /api/v1/apps" >}}

### 인가 엔드포인트 ([RFC 6749 절 3.1](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.1)) {#authorization}

사용자에게 인가 양식을 표시합니다. 승인되면 인가 코드를 생성하여 반환하고 원하는 `redirect_uri`로 리디렉션하거나, `urn:ietf:wg:oauth:2.0:oob`를 요청했다면 인가 코드를 표시합니다.

{{< page-relref ref="methods/oauth#authorize" caption="GET /oauth/authorize" >}}

### 토큰 엔드포인트 ([RFC 6749 절 3.2](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.2)) {#token}

액세스 토큰을 얻습니다. 마스토돈은 다음 OAuth 2 흐름을 지원합니다.

인가 코드 흐름
: 최종 사용자용

클라이언트 자격 증명 흐름
: 사용자를 대신하여 동작하지 않는 애플리케이션용

마스토돈은 과거 비밀번호 부여 흐름을 지원했지만 보안 문제로 OAuth 2 사양 작성자가 사용을 [권장하지 않으며](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics#name-resource-owner-password-cre), 이후 마스토돈의 향후 버전에서 제거되었습니다. 대신 해당 사용자용 OAuth 애플리케이션을 생성하고 발급된 액세스 토큰으로 API와 상호작용하는 것이 좋습니다.

{{< page-relref ref="methods/oauth#token" caption="POST /oauth/token" >}}

### 토큰 폐기 엔드포인트 ([RFC 7009 절 2](https://www.rfc-editor.org/rfc/rfc7009.html#section-2)) {#revoke}

액세스 토큰을 폐기하려면 클라이언트 자격 증명과 함께 여기에 POST 요청을 보냅니다.

{{< page-relref ref="methods/oauth#revoke" caption="POST /oauth/revoke" >}}

## OAuth 2 보안 고려 사항 {#oauth-2-security-considerations}

### 코드 교환 증명 키 (PKCE) {#pkce}

OAuth 2 [인가 코드 흐름]({{< relref ref="methods/oauth#authorize" >}})을 수행할 때 사용자가 애플리케이션으로 다시 리디렉션되는 과정의 인가 코드 보안을 높일 수 있는 추가 보안 메커니즘이 있습니다. 코드 교환 증명 키, 즉 PKCE(“픽시”로 발음)라고 하며 마스토돈 4.3.0 이상에서 지원합니다.

[OAuth 2 보안 최신 모범 사례](https://www.ietf.org/archive/id/draft-ietf-oauth-security-topics-27.html#name-pkce)에 따라 기밀 클라이언트와 공개 클라이언트 모두 인가 코드 흐름에 PKCE를 사용하는 것이 좋습니다.

{{< caption-link url="https://oauth.net/2/pkce/" caption="OAuth.net 웹사이트에서 PKCE 자세히 알아보기" >}}

### State 매개변수 {#state-parameter}

OAuth 2 [인가 코드 흐름]({{< relref ref="methods/oauth#authorize" >}})을 수행할 때 인가 엔드포인트의 [`state` 매개변수](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.1)로 혼동 공격과 사이트 간 요청 위조 공격을 방지할 수 있습니다. OAuth 인가 코드 흐름이 완료되면 리디렉션 URI를 통해 이 매개변수가 변경 없이 서버에 반환됩니다.

이 매개변수로 인가 코드 흐름을 통해 임의의 정보를 서버에 그대로 전달할 수도 있습니다. `state` 매개변수를 사용한다면 인가 코드 흐름을 완료하기 전(즉, 인가 코드를 액세스 토큰으로 교환하기 전)에 상태 값을 비교하거나 검증하는 것이 좋습니다.

## 흔히 주의할 점 {#gotchas}

- 마스토돈 REST API로 애플리케이션을 등록할 때는 `scopes` 매개변수가 있습니다. OAuth 엔드포인트와 상호작용할 때는 대신 `scope` 매개변수를 사용해야 하며, 그 값은 앱에 등록한 `scopes`의 부분집합이어야 합니다. 원래 집합에 없던 항목은 포함할 수 없습니다.
- 마스토돈 REST API로 애플리케이션을 등록할 때는 `redirect_uris` 매개변수가 있습니다. OAuth 엔드포인트와 상호작용할 때는 대신 `redirect_uri` 매개변수를 사용해야 하며, 그 값은 앱에 등록한 `redirect_uris` 중 하나여야 합니다.
