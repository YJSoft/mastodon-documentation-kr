---
title: OAuth 토큰
description: 이 문서 전반에서 사용하는 토큰 유형을 정의합니다.
menu:
  docs:
    weight: 15
    parent: api
---

## OAuth 토큰 {#oauth-tokens}

마스토돈은 앱 토큰과 사용자 토큰이라는 두 가지 OAuth 토큰 유형을 지원합니다. 이 문서 전반의 API 엔드포인트 `OAuth` 필드에서 이 토큰 유형을 참조합니다.

`OAuth` 필드에는 공개도 표시되며, 이 경우 API 엔드포인트에 접근할 때 OAuth 액세스 토큰을 제공할 필요가 없습니다.

토큰은 자동으로 만료되지 않습니다. 사용자가 삭제하거나 앱이 폐기할 때만 무효화됩니다.

### 앱 토큰 {#app-tokens}

앱 토큰을 받으려면 [클라이언트 자격 증명 부여 흐름]({{<relref "client/token#flow" >}})을 수행해야 합니다. OAuth 애플리케이션을 대신하여 API와 상호작용할 수 있는 토큰을 얻습니다. 현재 이 토큰 유형을 허용하는 API 엔드포인트는 다음뿐입니다.

- [`GET /api/v1/apps/verify_credentials`]({{<relref "methods/apps#verify_credentials" >}})
- [`POST /api/v1/accounts`]({{<relref "/methods/accounts#create" >}})

### 사용자 토큰 {#user-tokens}

사용자 토큰을 생성하려면 [인가 코드 부여 흐름]({{<relref "client/authorized#flow">}})을 수행해야 합니다. 접근 허용 요청을 승인한 사용자와 연결된 액세스 토큰을 얻습니다.

많은 마스토돈 API에 접근하려면 사용자 토큰과 특정 범위가 필요합니다.
