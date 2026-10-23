---
title: 관리자용 이메일 도메인 차단 (Admin::EmailDomainBlock)
description: 가입에 사용할 수 없는 이메일 도메인을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/admin-emaildomainblock",
  "/entities/Admin-EmailDomainBlock",
  "/entities/admin_emaildomainblock",
  "/entities/Admin_EmailDomainBlock",
  "/api/entities/admin-emaildomainblock",
  "/api/entities/Admin-EmailDomainBlock",
  "/api/entities/admin_emaildomainblock",
  "/api/entities/Admin_EmailDomainBlock",
]
---

## 예시 {#example}

```json
{
  "id": "1",
  "domain": "foo",
  "created_at": "2022-11-16T06:09:36.176Z",
  "history": [
    {
      "day": "1668556800",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668470400",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668384000",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668297600",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668211200",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668124800",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668038400",
      "accounts": "0",
      "uses": "0"
    }
  ]
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 EmailDomainBlock ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.0.0 - 추가

### `domain` {#domain}

**설명:** 가입에 사용할 수 없는 이메일 도메인입니다.\
**유형:** 문자열\
**버전 이력:**\
4.0.0 - 추가

### `created_at` {#created_at}

**설명:** 이 이메일 도메인의 가입이 금지된 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
4.0.0 - 추가

### `history` {#history}

**설명:** 주어진 날짜들(보통 지난 일주일)의 사용 통계입니다.\
**유형:** 배열: 해시\
**버전 이력:**\
4.0.0 - 추가

#### `history[][day]` {#history-day}

**설명:** 해당 날짜 자정의 UNIX 타임스탬프입니다.\
**유형:** 문자열 (UNIX 타임스탬프)\
**버전 이력:**\
4.0.0 - 추가

#### `history[][accounts]` {#history-accounts}

**설명:** 해당 날짜에 이 이메일 도메인을 사용하여 시도한 계정 가입 횟수입니다.\
**유형:** 문자열 (정수에서 변환)\
**버전 이력:**\
4.0.0 - 추가

#### `history[][uses]` {#history-uses}

**설명:** 해당 날짜에 이 이메일 도메인을 사용하여 시도한 IP별 가입 횟수입니다.\
**유형:** 문자열 (정수에서 변환)\
**버전 이력:**\
4.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref page="methods/admin/email_domain_blocks" caption="admin/email_domain_blocks API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/admin/email_domain_block_serializer.rb" caption="app/serializers/rest/admin/email_domain_block_serializer.rb" >}}