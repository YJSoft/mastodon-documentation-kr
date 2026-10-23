---
title: 대화 (Conversation)
description: “개인 메시지” 공개 범위의 대화를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/conversation",
	"/entities/Conversation",
  "/api/entities/conversation",
	"/api/entities/Conversation",
]
---

## 예시 {#example}

```json
{
  "id": "418450",
  "unread": true,
  "accounts": [
    {
      "id": "482403",
      "username": "amic",
      "acct": "amic@nulled.red",
      // ...
    }
  ],
  "last_status": {
    "id": "103196583826321184",
    "created_at": "2019-11-25T04:08:24.000Z",
    "in_reply_to_id": "103196540587943467",
    "in_reply_to_account_id": "14715",
    // ...
  }
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 대화 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
2.6.0 - 추가

### `unread` {#unread}

**설명:** 대화가 현재 읽지 않음으로 표시되어 있는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.6.0 - 추가

### `accounts` {#accounts}

**설명:** 대화 참여자입니다.\
**유형:** 배열: [Account]({{< relref "entities/Account" >}})\
**버전 이력:**\
2.6.0 - 추가

### `last_status` {#last_status}

**설명:** 대화의 마지막 게시물입니다.\
**유형:** {{<nullable>}} [Status]({{< relref "entities/Status" >}})\
**버전 이력:**\
2.6.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/conversations" caption="conversations API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/conversation_serializer.rb" caption="app/serializers/rest/conversation_serializer.rb" >}}





