---
title: 계정 정보가 포함된 컬렉션 (CollectionWithAccounts)
description: 사용자가 다른 사람에게 팔로우를 추천하는 계정 컬렉션과 전체 계정 데이터입니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/collectionwithaccounts",
  "/entities/CollectionWithAccounts",
  "/api/entities/collectionwithaccounts",
  "/api/entities/CollectionWithAccounts",
]
---

## 예시 {#example}

```json
{
  "accounts": [
    {
      "id": "113668893442515793",
      // ... Full `Account` entity for the collection owner
    },
    {
      "id": "112658193342215767",
      // ... Full `Account` entity for the first item in the collection
    },
    {
      "id": "117628196343117789",
      // ... Full `Account` entity for the second item in the collection
    }
  ],
  "collection": {
    "id": "116131056935959117",
    "account_id": "113668893442515793",
    "uri": "https://example.com/ap/113668893442515793/collections/116131056935959117",
    "url": "https://example.com/collections/116131056935959117",
    "name": "Excellent people",
    "description": "Well worth following",
    "language": "en",
    "local": true,
    "sensitive": false,
    "discoverable": true,
    "tag": {
      "name": "discovery",
      "url": "https://example.com/tags/discovery"
    },
    "item_count": 2,
    "items": [
      {
        "id": "116141056635954112",
        "account_id": "112658193342215767",
        "state": "accepted",
        "created_at": "2026-02-25T11:35:01.394Z"
      },
      {
        "id": "116141051635254139",
        "account_id": "117628196343117789",
        "state": "pending",
        "created_at": "2026-02-25T11:35:01.394Z"
      }
    ],
    "created_at": "2026-02-25T11:35:01.394Z",
    "updated_at": "2026-02-25T11:37:38.182Z"
  }
}
```

## 속성 {#attributes}

### `accounts` {#account_id}

**설명:** 컬렉션 소유자와 컬렉션에 포함된 모든 계정의 전체 계정 엔터티입니다.\
**유형:** 배열: [Account]({{< relref "entities/Account" >}})\
**버전 이력:**\
4.6.0 - 추가

### `collection` {#collection}

**설명:** 실제 컬렉션입니다.\
**유형:** [Collection]({{< relref "entities/Collection" >}})\
**버전 이력:**\
4.6.0 - 추가


## 함께 보기 {#see-also}

{{< page-relref ref="entities/Collection" caption="Collection 엔터티" >}}
{{< page-relref ref="entities/Account" caption="Account 엔터티" >}}
{{< page-relref ref="methods/collections" caption="collections API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/collection_with_accounts_serializer.rb" caption="app/serializers/rest/collection_with_accounts_serializer.rb" >}}
