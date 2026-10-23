---
title: 글타래 맥락 (Context)
description: 주어진 게시물 주변의 트리를 나타냅니다. 게시물 글타래를 재구성하는 데 사용합니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/context",
	"/entities/Context",
  "/api/entities/context",
	"/api/entities/Context",
]
---

## 예시 {#example}

```json
{
  "ancestors": [
    {
      "id": "103188938570975982",
      "created_at": "2019-11-23T19:44:00.124Z",
      "in_reply_to_id": null,
      // ...
    },
    {
      "id": "103188971072973252",
      "created_at": "2019-11-23T19:52:23.398Z",
      "in_reply_to_id": "103188938570975982",
      // ...
    },
    {
      "id": "103188982235527758",
      "created_at": "2019-11-23T19:55:08.208Z",
      "in_reply_to_id": "103188971072973252",
      // ...
    }
  ],
  "descendants": [
    {
      "id": "103189026958574542",
      "created_at": "2019-11-23T20:06:36.011Z",
      "in_reply_to_id": "103189005915505698",
      // ...
    }
  ]
}
```

## 속성 {#attributes}

### `ancestors` {#ancestors}

**설명:** 글타래의 상위 게시물입니다.\
**유형:** 배열: [Status]({{< relref "entities/Status" >}})\
**버전 이력:**\
0.6.0 - 추가

### `descendants` {#descendants}

**설명:** 글타래의 하위 게시물입니다.\
**유형:** 배열: [Status]({{< relref "entities/Status" >}})\
**버전 이력:**\
0.6.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/statuses#context" caption="GET /api/v1/statuses/:id/context" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/context_serializer.rb" caption="app/serializers/rest/context_serializer.rb" >}}