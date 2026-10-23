---
title: 알림 (Notification)
description: 사용자와 관련된 이벤트의 알림을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/notification",
  "/entities/Notification",
  "/api/entities/notification",
  "/api/entities/Notification",
]
---

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 알림 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
0.9.9 - 추가

### `type` {#type}

**설명:** 알림을 발생시킨 이벤트 유형입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`mention` = 누군가 게시물에서 나를 멘션했습니다.\
`status` = 내가 알림을 켠 사람이 게시물을 올렸습니다.\
`reblog` = 누군가 내 게시물을 부스트했습니다.\
`follow` = 누군가 나를 팔로우했습니다.\
`follow_request` = 누군가 나에게 팔로우를 요청했습니다.\
`favourite` = 누군가 내 게시물에 좋아요를 눌렀습니다.\
`poll` = 내가 참여하거나 만든 투표가 종료되었습니다.\
`update` = 내가 부스트한 게시물이 수정되었습니다.\
`admin.sign_up` = 누군가 가입했습니다(선택적으로 관리자에게 전송).\
`admin.report` = 새 신고가 접수되었습니다.\
`severed_relationships` = 중재나 차단으로 인해 일부 팔로우 관계가 단절되었습니다.\
`moderation_warning` = 중재자가 내 계정에 조치를 취했거나 경고를 보냈습니다.\
`quote` = 누군가 내 게시물을 인용했습니다.\
`quoted_update` = 내가 인용한 게시물이 수정되었습니다.\
`added_to_collection` = 누군가 나를 컬렉션에 추가했습니다.\
`collection_update` = 내가 소개된 컬렉션이 갱신되었습니다.\
**버전 이력:**\
0.9.9 - 추가\
2.8.0 - `poll` 추가\
3.1.0 - `follow_request` 추가\
3.3.0 - `status` 추가\
3.5.0 - `update`와 `admin.sign_up` 추가\
4.0.0 - `admin.report` 추가\
4.3.0 - `severed_relationships`와 `moderation_warning` 추가\
4.5.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 7) - `quote`와 `quoted_update` 추가\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - `added_to_collection`과 `collection_update` 추가

### `group_key` {#group_key}

**설명:** 유사한 알림이 공유하는 그룹 키로, 알림 그룹화 기능에 사용합니다. 내부 구조를 해석하지 않아야 하지만, 그룹화되지 않은 알림의 `group_key`는 `ungrouped-{notification_id}` 형태라고 가정할 수 있습니다.\
**유형:** 문자열\
**버전 이력:**\
4.3.0 - 추가

### `created_at` {#created_at}

**설명:** 알림의 타임스탬프입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
0.9.9 - 추가

### `account` {#account}

**설명:** 알림을 발생시킨 동작을 수행한 계정입니다.\
**유형:** [Account]({{< relref "entities/Account" >}})\
**버전 이력:**\
0.9.9 - 추가

### `status` {{%optional%}} {#status}

**설명:** 알림 대상 게시물입니다. 알림의 `type`이 `favourite`, `reblog`, `status`, `mention`, `poll`, `update`, `quote`, `quoted_update`일 때 첨부합니다. `quoted_update`의 경우 수정된 게시물 자체 대신, 해당 게시물을 인용한 내 게시물을 첨부합니다.\
**유형:** [Status]({{< relref "entities/Status" >}})\
**버전 이력:**\
0.9.9 - 추가

### `report` {{%optional%}} {#report}

**설명:** 알림 대상 신고입니다. 알림의 `type`이 `admin.report`일 때 첨부합니다.\
**유형:** [Report]({{< relref "entities/Report" >}})\
**버전 이력:**\
4.0.0 - 추가

### `event` {{%optional%}} {#relationship_severance_event}

**설명:** 팔로우 관계 단절을 일으킨 이벤트 요약입니다. 알림의 `type`이 `severed_relationships`일 때 첨부합니다.\
**유형:** [RelationshipSeveranceEvent]({{< relref "entities/RelationshipSeveranceEvent" >}})\
**버전 이력:**\
4.3.0 - 추가

### `moderation_warning` {{%optional%}} {#moderation_warning}

**설명:** 알림을 발생시킨 중재 경고입니다. 알림의 `type`이 `moderation_warning`일 때 첨부합니다.\
**유형:** [AccountWarning]({{< relref "entities/AccountWarning" >}})\
**버전 이력:**\
4.3.0 - 추가

#### `fallback` {{%optional%}} {#fallback-optional}

**설명:** 클라이언트가 지원하지 않을 수 있는 일부 알림 유형에 제공하는 대체 정보입니다. 일부 알림 유형에서만, 그리고 조회 시 `supported_types` 매개변수를 사용한 경우에만 제공됩니다.\
**유형:** [NotificationFallback]({{< relref "entities/NotificationFallback" >}})\
**버전 이력:**\
4.6.0 - 추가

#### `collection` {{%optional%}} {#collection-optional}

**설명:** 알림 대상 컬렉션입니다. 알림의 `type`이 `added_to_collection` 또는 `collection_update`일 때 첨부합니다.\
**유형:** [Collection]({{< relref "entities/Collection" >}})\
**버전 이력:**\
4.6.0 - 추가

## 예시 {#examples}

### 멘션 {#mention}

```json

  {
    "id": "34975861",
    "type": "mention",
    "created_at": "2019-11-23T07:49:02.064Z",
    "account": {
      "id": "971724",
      "username": "zsc",
      "acct": "zsc",
      // ...
    },
    "status": {
      "id": "103186126728896492",
      "created_at": "2019-11-23T07:49:01.940Z",
      "in_reply_to_id": "103186038209478945",
      "in_reply_to_account_id": "14715",
      // ...
    }
  }
```

### 좋아요 {#favourite}

```json
  {
    "id": "34975535",
    "type": "favourite",
    "created_at": "2019-11-23T07:29:18.903Z",
    "account": {
      "id": "297420",
      "username": "haskal",
      "acct": "haskal@cybre.space",
      // ...
    },
    "status": {
      "id": "103186046267791694",
      "created_at": "2019-11-23T07:28:34.210Z",
      // ...
      "account": {
        "id": "14715",
        "username": "trwnh",
        "acct": "trwnh",
        // ...
      },
      // ...
    }
  }
```

## 함께 보기 {#see-also}

{{< page-relref ref="methods/notifications" caption="notifications API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/notification_serializer.rb" caption="app/serializers/rest/notification_serializer.rb" >}}



