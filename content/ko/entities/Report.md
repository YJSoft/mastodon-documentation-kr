---
title: 신고 (Report)
description: 사용자 및/또는 게시물에 대해 접수된 신고로, 중재자의 조치 대상입니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/report",
  "/entities/Report",
  "/api/entities/report",
  "/api/entities/Report",
]
---

## 예시 {#example}

```json
{
  "id": "48914",
  "action_taken": false,
  "action_taken_at": null,
  "category": "spam",
  "comment": "Spam account",
  "forwarded": false,
  "created_at": "2022-08-25T09:56:16.763Z",
  "status_ids": [
    "108882889550545820"
  ],
  "collection_ids": [],
  "rule_ids": null,
  "target_account": {
    "id": "108366849347798387",
    "username": "Baluke",
    "acct": "Baluke",
    "display_name": "Baluke Dental Studios",
    "locked": false,
    "bot": false,
    "discoverable": false,
    "group": false,
    "created_at": "2022-05-26T00:00:00.000Z",
    "note": "<p>Baluke Dental Studios is a full service dental lab offering fabrication, staining, and digital services. Advanced technologies and a meticulous process ensure reduced chair time, lower costs, and better patient outcomes with beautiful smiles. Talk to a representative today.</p><p><a href=\"https://baluke.com/\" target=\"_blank\" rel=\"nofollow noopener noreferrer\"><span class=\"invisible\">https://</span><span class=\"\">baluke.com/</span><span class=\"invisible\"></span></a></p>",
    "url": "https://mastodon.social/@Baluke",
    "avatar": "https://files.mastodon.social/accounts/avatars/108/366/849/347/798/387/original/dbcfe99ed5def0f4.png",
    "avatar_static": "https://files.mastodon.social/accounts/avatars/108/366/849/347/798/387/original/dbcfe99ed5def0f4.png",
    "header": "https://static-cdn.mastodon.social/headers/original/missing.png",
    "header_static": "https://static-cdn.mastodon.social/headers/original/missing.png",
    "followers_count": 0,
    "following_count": 0,
    "statuses_count": 38,
    "last_status_at": "2022-08-25",
    "emojis": [],
    "fields": []
  }
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 신고 ID입니다.\
**유형:** 문자열 (정수에서 변환)\
**버전 이력:**\
1.1.0 - 추가

### `action_taken` {#action_taken}

**설명:** 아직 조치를 취했는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
1.1.0 - 추가

### `action_taken_at` {#action_taken_at}

**설명:** 신고에 대한 조치를 취한 시각입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜와 시각](/api/datetime-format#datetime)) 또는 null\
**버전 이력:**\
4.0.0 - 추가

### `category` {#category}

**설명:** 신고의 일반적인 사유입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`spam` = 원치 않거나 반복되는 콘텐츠\
`legal` = 불법 콘텐츠\
`violation` = 특정 규칙 위반\
`other` = 기타 사유\
**버전 이력:**\
4.0.0 - 추가\
4.2.0 - `legal` 분류 추가

### `comment` {#comment}

**설명:** 신고 사유입니다.\
**유형:** 문자열\
**버전 이력:**\
4.0.0 - 추가

### `forwarded` {#forwarded}

**설명:** 신고가 원격 도메인에 전달되었는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.0.0 - 추가

### `created_at` {#created_at}

**설명:** 신고 생성 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
4.0.0 - 추가

### `status_ids` {#status_ids}

**설명:** 추가 맥락을 제공하기 위해 신고에 첨부한 게시물의 ID입니다.\
**유형:** {{<nullable>}} 배열: 문자열 (정수에서 변환), 또는 null\
**버전 이력:**\
4.0.0 - 추가

### `collection_ids` {#collection_ids}

**설명:** 추가 맥락을 제공하기 위해 신고에 첨부한 추천 컬렉션의 ID입니다.\
**유형:** {{<nullable>}} 배열: 문자열 (정수에서 변환), 또는 null\
**버전 이력:**\
4.6.0 - 추가

### `rule_ids` {#rule_ids}

**설명:** 이 신고에서 위반했다고 인용한 규칙의 ID입니다.\
**유형:** {{<nullable>}} 배열: 문자열 (정수에서 변환), 또는 null\
**버전 이력:**\
4.0.0 - 추가

### `target_account` {#target_account}

**설명:** 신고된 계정입니다.\
**유형:** [Account]({{< relref "entities/account" >}})\
**버전 이력:**\
4.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/reports" caption="reports API 메서드" >}}

{{< page-relref ref="entities/Notification#report" caption="Notification (`report` 속성)" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/report_serializer.rb" caption="app/serializers/rest/report_serializer.rb" >}}



