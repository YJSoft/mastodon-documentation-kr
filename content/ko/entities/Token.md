---
title: 토큰 (Token)
description: API 인증과 동작 수행에 사용하는 OAuth 토큰을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/token",
  "/entities/Token",
  "/api/entities/token",
  "/api/entities/Token",
]
---

## 예시 {#example}

```json
{
  "access_token": "ZA-Yj3aBD8U8Cm7lKUp-lm9O9BmDgdhHzDeqsY8tlL0",
  "token_type": "Bearer",
  "scope": "read write follow push",
  "created_at": 1573979017
}
```

## 속성 {#attributes}

### `access_token` {#access_token}

**설명:** 인가에 사용할 OAuth 토큰입니다.\
**유형:** 문자열\
**버전 이력:**\
0.1.0 - 추가

### `token_type` {#token_type}

**설명:** OAuth 토큰 유형입니다. 마스토돈은 `Bearer` 토큰을 사용합니다.\
**유형:** 문자열\
**버전 이력:**\
0.1.0 - 추가

### `scope` {#scope}

**설명:** 이 토큰에 부여된 OAuth 범위이며 공백으로 구분합니다.\
**유형:** 문자열\
**버전 이력:**\
0.1.0 - 추가

### `created_at` {#created_at}

**설명:** 토큰 생성 시각입니다.\
**유형:** 숫자 (UNIX 타임스탬프)\
**버전 이력:**\
0.1.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="oauth-scopes" caption="OAuth 범위" >}}

{{< page-relref ref="methods/oauth" caption="OAuth 메서드" >}}

{{< page-ref page="client/token" >}}

{{< page-ref page="client/authorized" >}}