---
title: 관리자용 신고 (Admin::Report)
description: 접수된 신고의 관리자 수준 정보입니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/admin-report",
  "/entities/Admin-Report",
  "/entities/admin_report",
  "/entities/Admin_Report",
  "/api/entities/admin-report",
  "/api/entities/Admin-Report",
  "/api/entities/admin_report",
  "/api/entities/Admin_Report",
]
---

## 예시 {#example}

```json
{
  "id": "1",
  "action_taken": false,
  "action_taken_at": null,
  "category": "spam",
  "comment": "",
  "forwarded": false,
  "created_at": "2022-09-09T21:19:23.085Z",
  "updated_at": "2022-09-09T21:19:23.085Z",
  "account": {
    "id": "108965218747268792",
    "username": "admin",
    "domain": null,
    "created_at": "2022-09-08T22:48:07.985Z",
    "email": "admin@mastodon.local",
    // ...
    "account": {
      "id": "108965218747268792",
      "username": "admin",
      "acct": "admin",
      // ...
    }
  },
  "target_account": {
    "id": "108965430868193066",
    "username": "goody",
    "domain": null,
    "created_at": "2022-09-08T23:42:04.731Z",
    "email": "goody@mastodon.local",
    // ...
    "account": {
      "id": "108965430868193066",
      "username": "goody",
      "acct": "goody",
      // ...
    }
  },
  "assigned_account": null,
  "action_taken_by_account": null,
  "statuses": [],
  "rules": []
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 신고 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
2.9.1 - 추가

### `action_taken` {#action_taken}

**설명:** 이 신고를 해결하기 위한 조치를 취했는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.9.1 - 추가

### `action_taken_at` {#action_taken_at}

**설명:** 이 신고가 현재 해결된 경우, 조치를 취한 시각입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜와 시각](/api/datetime-format#datetime)) 또는 null\
**버전 이력:**\
2.9.1 - 추가

### `category` {#category}

**설명:** 신고 분류입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`spam` = 악의적이거나 가짜이거나 반복되는 콘텐츠\
`legal` = 불법 콘텐츠\
`violation` = 하나 이상의 구체적인 [`rules`](#rules)을 위반함\
`other` = 기본 분류(기타 모든 경우)\
**버전 이력:**\
3.5.0 - 추가\
4.2.0 - `legal` 분류 추가

### `comment` {#comment}

**설명:** 신고의 선택적 사유입니다.\
**유형:** 문자열\
**버전 이력:**\
2.9.1 - 추가

### `forwarded` {#forwarded}

**설명:** 신고가 원격 서버에 전달되었는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.0.0 - 추가

### `created_at` {#created_at}

**설명:** 신고 접수 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
2.9.1 - 추가

### `updated_at` {#updated_at}

**설명:** 이 신고에 대한 마지막 조치 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
2.9.1 - 추가

### `account` {#account}

**설명:** 신고를 접수한 계정입니다.\
**유형:** [Admin::Account]({{< relref "entities/Admin_Account" >}})\
**버전 이력:**\
2.9.1 - 추가

### `target_account` {#target_account}

**설명:** 신고 대상 계정입니다.\
**유형:** [Admin::Account]({{< relref "entities/Admin_Account" >}})\
**버전 이력:**\
2.9.1 - 추가

### `assigned_account` {#assigned_account}

**설명:** 이 신고를 배정받은 중재자의 계정입니다.\
**유형:** {{<nullable>}} [Admin::Account]({{< relref "entities/Admin_Account" >}}) 또는 null\
**버전 이력:**\
2.9.1 - 추가

### `action_taken_by_account` {#action_taken_by_account}

**설명:** 신고를 처리한 중재자의 계정입니다.\
**유형:** {{<nullable>}} [Admin::Account]({{< relref "entities/Admin_Account" >}}) 또는 null\
**버전 이력:**\
2.9.1 - 추가

### `statuses` {#statuses}

**설명:** 맥락을 제공하기 위해 신고에 첨부한 게시물입니다.\
**유형:** 배열: [Status]({{< relref "entities/Status" >}})\
**버전 이력:**\
2.9.1 - 추가

### `rules` {#rules}

**설명:** 맥락을 제공하기 위해 신고에 첨부한 규칙입니다.\
**유형:** 배열: [Rule]({{< relref "entities/Rule" >}})\
**버전 이력:**\
3.5.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref page="methods/admin/reports" caption="admin/reports API 메서드">}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/admin/report_serializer.rb" caption="app/serializers/rest/admin/report_serializer.rb" >}}



