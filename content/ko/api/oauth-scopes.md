---
title: OAuth 범위
description: API에서 수행할 수 있는 작업 권한을 정의합니다.
menu:
  docs:
    weight: 20
    parent: api
---

## OAuth 범위 {#oauth-scopes}

API 접근은 여러 OAuth 범위로 나뉩니다. 이는 [액세스 토큰]({{< relref "api/oauth-tokens" >}})에 등록하고 요청한 범위에 따라 API 클라이언트가 할 수 있는 작업을 제한합니다. 마스토돈의 범위에는 계층이 있습니다. 예를 들어 `read` 범위를 요청하면 자동으로 `read:accounts`에도 접근할 수 있습니다. 하지만 **애플리케이션에 필요한 최소한의 범위만 요청하는 것을 권장합니다**. 예를 들어 리스트와 현재 사용자 프로필 읽기만 필요하다면 `read` 대신 `profile read:lists`를 범위로 사용해야 합니다.

{{< hint style="info" >}}
현재 인증된 사용자의 상세 정보만 가져오려면 `profile` 범위를 사용합니다. 이 범위는 [`GET /api/v1/accounts/verify_credentials`]({{< relref "methods/accounts#verify_credentials" >}}) 엔드포인트에만 접근할 수 있습니다.\
이 범위는 마스토돈 4.3에 추가되었으므로 사용할 때 아래 “마스토돈 서버가 지원하는 OAuth 범위 확인” 지침을 따르는 것이 좋습니다.
{{</ hint >}}

### 마스토돈 서버가 지원하는 OAuth 범위 확인 {#discovering-oauth-scopes-supported-by-a-given-mastodon-server}

마스토돈 4.3.0부터 [RFC 8414](https://tools.ietf.org/html/rfc8414)의 `GET /.well-known/oauth-authorization-server` 엔드포인트 지원이 추가되어 서버가 지원하는 범위와 엔드포인트, 부여 흐름 등 다른 OAuth 관련 정보를 확인할 수 있습니다.

OAuth 애플리케이션에서 여러 마스토돈 버전을 지원하려면 이 엔드포인트를 사용하는 것이 좋습니다.

`GET /.well-known/oauth-authorization-server` 엔드포인트 요청이 404를 반환하면 서버가 4.3 이전 버전을 실행한다고 가정할 수 있습니다. 이 경우 애플리케이션에 필요한 구체적인 범위와 지원하려는 마스토돈 버전 범위에서 공통으로 사용할 수 있는 최소 범위를 확인해야 합니다.

{{< hint style="info" >}}
**예시:** `profile` 범위를 사용하면서, 이 범위가 없어 대신 `read:accounts`가 필요한 이전 마스토돈 서버도 지원하려 합니다. 이 엔드포인트에 요청하여 서버가 해당 범위를 지원하는지 확인할 수 있습니다.
{{< /hint >}}

{{< page-relref ref="methods/oauth#authorization-server-metadata" caption="GET /.well-known/oauth-authorization-server" >}}

### 여러 범위를 동시에 요청할 수 있습니다 {#multiple-scopes-can-be-requested-at-the-same-time}

애플리케이션 생성 시 `scopes` 매개변수에 공백으로 구분한 여러 범위를 지정할 수 있습니다. 인가 단계에서는 `scope` 쿼리 매개변수로 같은 작업을 할 수 있습니다.

{{< hint style="danger" >}}
애플리케이션 생성 시 저장한 범위 집합에는 인가 요청에서 요청할 모든 범위가 포함되어야 합니다. 그렇지 않으면 인가에 실패합니다.
{{< /hint >}}

{{< hint style="info" >}}
`scope`와 `scopes`의 차이에 주의하세요. `scope`는 표준 OAuth 매개변수 이름이므로 OAuth 메서드에서 사용합니다. 마스토돈 자체 REST API는 더 적절한 이름인 `scopes`를 사용합니다.
{{< /hint >}}

인가 요청에 `scope`를 지정하지 않거나 애플리케이션 생성 요청에 `scopes`를 지정하지 않으면 생성된 액세스 토큰/앱에 기본 범위가 할당됩니다. 마스토돈 4.3 기준으로 현재는 `read`이지만 향후 변경될 수 있습니다.

{{< page-relref ref="methods/apps#create" caption="POST /api/v1/apps" >}}

### 버전 이력 {#versions}

- 0.9.0 - read, write, follow 범위 추가
- 2.4.0 - 푸시 알림용 push 범위 추가
- 2.4.3 - 세분화된 범위 추가 [#7929](https://github.com/mastodon/mastodon/pull/7929)
- 2.6.0 - `read:reports` 폐기 예정으로 지정(사용하지 않는 스텁) [#8736/adcf23f](https://github.com/mastodon/mastodon/pull/8736/commits/adcf23f1d00c8ff6877ca2ee2af258f326ae4e1f)
- 2.6.0 - `write:conversations` 추가 [#9009](https://github.com/mastodon/mastodon/pull/9009)
- 2.9.1 - 관리 및 중재 범위 추가 [#9387](https://github.com/mastodon/mastodon/pull/9387)
- 3.1.0 - 북마크 범위 추가 [#7107](https://github.com/mastodon/mastodon/pull/7107)
- 3.5.0 - `follow` 범위를 폐기 예정으로 지정하고 세분화된 범위로 대체 [#17678](https://github.com/mastodon/mastodon/pull/17678)
- 4.1.0 - 차단과 허용을 위한 관리자 범위 추가 [#20918](https://github.com/mastodon/mastodon/pull/20918)
- 4.3.0 - 현재 인증된 사용자 정보만 가져오는 `profile` 범위 추가 [#29087](https://github.com/mastodon/mastodon/pull/29087), [#30357](https://github.com/mastodon/mastodon/pull/30357)' 및 (실험적) `crypto`[^crypto] 범위 제거
- 4.6.0 - `read:collection`과 `write:collection` 범위 추가 [#37049](https://github.com/mastodon/mastodon/pull/37049)

## 상위 범위 목록 {#list-of-high-level-scopes}

다음 범위 대신 아래 표 오른쪽 열에 표시된 [세분화된 범위](#granular-scopes)를 사용하는 것이 좋습니다.

- `read`
- `write`
- `follow` {{%deprecated%}}
- `admin:read`
- `admin:write`

현재 인증된 사용자 정보만 필요하다면 `profile` 범위를 사용합니다.

### `profile` {#profile}

현재 인증된 사용자의 최소한의 정보에만 접근할 수 있습니다. 이 범위로 다음 엔드포인트를 사용할 수 있습니다.
* [`GET /api/v1/accounts/verify_credentials`]({{< relref "methods/accounts#verify_credentials" >}})
* [`GET /oauth/userinfo`]({{< relref "methods/oauth#userinfo" >}}) (4.4.0에 추가)

### `read` {#read}

다른 사용자를 포함한 데이터 읽기 권한을 부여합니다. `read`를 요청하면 아래 표 오른쪽 열에 표시된 [세분화된 범위](#granular-scopes)도 부여됩니다.

### `write` {#write}

데이터 쓰기 권한을 부여합니다. `write`를 요청하면 아래 표 오른쪽 열에 표시된 [세분화된 범위](#granular-scopes)도 부여됩니다.

### `push` {#push}

[웹 푸시 API 구독]({{< relref "methods/push" >}}) 접근 권한을 부여합니다. 마스토돈 2.4.0에 추가되었습니다.

### `follow` {#follow}

{{< hint style="danger" >}}
**폐기 예정**\
이 범위는 3.5.0 이상에서 폐기 예정이 되었습니다. 대신 [세분화된 범위](#granular-scopes)를 개별적으로 요청하거나 필요에 따라 `read`/`write` 범위를 요청해야 합니다.
{{< /hint >}}

관계 관리 권한을 부여합니다. `follow`를 요청하면 아래 표 오른쪽 열에 표시된 [세분화된 범위](#granular-scopes)도 부여됩니다.

### `admin:read` 및 `admin:write` {#admin}

관리 및 중재 API에 사용합니다. 마스토돈 2.9.1에 추가되었습니다.

`admin:read` 또는 `admin:write`를 요청하면 아래 표 오른쪽 열에 표시된 [세분화된 범위](#granular-scopes)도 부여됩니다.

{{< hint style="info" >}}
단독 `admin` 범위는 제공되지 않습니다.
{{< /hint >}}

## 세분화된 범위 {#granular-scopes}

`scope`를 `read write follow push`로 설정하여 모든 항목에 완전한 접근 권한이 반드시 필요한 경우가 아니라면 세분화된 범위를 사용하는 것이 좋습니다.

| 범위                      | 세분화된 범위                         |
| :------------------------ | :----------------------------------- |
| `profile`                 |                                      |
| `push`                    |                                      |
| `read`                    |                                      |
|                           | `read:accounts`                      |
|                           | `read:blocks`                        |
|                           | `read:bookmarks`                     |
|                           | `read:collections`                   |
|                           | `read:favourites`                    |
|                           | `read:filters`                       |
|                           | `read:follows`                       |
|                           | `read:lists`                         |
|                           | `read:mutes`                         |
|                           | `read:notifications`                 |
|                           | `read:search`                        |
|                           | `read:statuses`                      |
| `write`                   |                                      |
|                           | `write:accounts`                     |
|                           | `write:blocks`                       |
|                           | `write:bookmarks`                    |
|                           | `write:collections`                  |
|                           | `write:conversations`                |
|                           | `write:favourites`                   |
|                           | `write:filters`                      |
|                           | `write:follows`                      |
|                           | `write:lists`                        |
|                           | `write:media`                        |
|                           | `write:mutes`                        |
|                           | `write:notifications`                |
|                           | `write:reports`                      |
|                           | `write:statuses`                     |
| `follow` {{%deprecated%}} |                                      |
|                           | `read:blocks`                        |
|                           | `read:follows`                       |
|                           | `read:mutes`                         |
|                           | `write:blocks`                       |
|                           | `write:follows`                      |
|                           | `write:mutes`                        |
| `admin:read`              |                                      |
|                           | `admin:read:accounts`                |
|                           | `admin:read:canonical_email_blocks`  |
|                           | `admin:read:domain_allows`           |
|                           | `admin:read:domain_blocks`           |
|                           | `admin:read:email_domain_blocks`     |
|                           | `admin:read:ip_blocks`               |
|                           | `admin:read:reports`                 |
| `admin:write`             |                                      |
|                           | `admin:write:accounts`               |
|                           | `admin:write:canonical_email_blocks` |
|                           | `admin:write:domain_allows`          |
|                           | `admin:write:domain_blocks`          |
|                           | `admin:write:email_domain_blocks`    |
|                           | `admin:write:ip_blocks`              |
|                           | `admin:write:reports`                |

[^crypto]: 마스토돈 3.2.0부터 4.3.0까지는 종단 간 암호화 API용 `crypto` 범위를 지원했습니다. 이 기능은 문서화되거나 완전히 구현된 적이 없으며 버전 4.3.0에서 제거되었습니다. 이 범위로 등록된 애플리케이션은 서버를 4.3.0 이상으로 업그레이드할 때 해당 범위가 제거됩니다.
