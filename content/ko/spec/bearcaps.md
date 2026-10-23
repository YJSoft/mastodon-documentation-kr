---
title: Bearcap
description: URL과 접근에 필요한 Bearer 토큰을 결합한 URI 체계입니다.
menu:
  docs:
    weight: 60
    parent: spec
---

## Bearcap이란 무엇인가요? {#intro}

일부 경우 리소스가 공개적으로 제공되지 않아 성공적으로 가져오려면 토큰이 필요할 수 있습니다. 보통 다음과 같이 `Bearer` 토큰을 포함한 HTTP `Authorization` 헤더를 사용합니다.

```http
GET https://example.com/foo
Authorization: Bearer <token>
```

Bearcap은 다음과 같이 토큰을 포함하여 리소스에 연결하는 방법을 제공합니다.

```text
bear:?t=<token>&u=https://example.com/foo'
```

Bearcap을 HTTP 요청으로 변환하려면 `u` 매개변수로 요청을 보내고 `t` 매개변수를 `Authorization` 헤더의 `Bearer` 토큰으로 첨부합니다.

## 마스토돈은 Bearcap을 어떻게 사용하나요? {#usage}

v3.3.0부터 마스토돈은 수신한 Activity의 Bearcap 역참조를 지원합니다. 아직 Activity를 보낼 때는 Bearcap을 사용하지 않습니다.
