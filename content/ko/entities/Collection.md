---
title: 컬렉션 (Collection)
description: 사용자가 다른 사람에게 팔로우를 추천하는 계정 모음을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/collection",
  "/entities/Collection",
  "/entities/wrappedcollection",
  "/entities/WrappedCollection",
  "/api/entities/collection",
  "/api/entities/Collection",
  "/api/entities/wrappedcollection",
  "/api/entities/WrappedCollection",
]
---

## 예시 {#example}

```json
{
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
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 컬렉션 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.6.0 - 추가

### `account_id` {#account_id}

**설명:** 이 컬렉션을 관리하는 계정의 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.6.0 - 추가

### `uri` {#uri}

**설명:** 컬렉션의 ActivityPub 식별자입니다(연합에 사용됩니다).\
**유형:** 문자열 (URL)\
**버전 이력:**\
4.6.0 - 추가

### `url` {#url}

**설명:** 컬렉션 HTML 페이지의 URL입니다(웹 인터페이스 URL).\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
4.6.0 - 추가

### `name` {#name}

**설명:** 컬렉션 이름입니다.\
**유형:** 문자열\
**버전 이력:**\
4.6.0 - 추가

### `description` {#description}

**설명:** 컬렉션의 선택적 설명입니다.\
**유형:** {{<nullable>}} 문자열 (HTML)\
**버전 이력:**\
4.6.0 - 추가

### `language` {#language}

**설명:** 이 컬렉션의 기본 언어입니다.\
**유형:** {{<nullable>}} 문자열 (ISO 639-1 두 글자 언어 코드) 또는 null\
**버전 이력:**\
4.6.0 - 추가

### `local` {#local}

**설명:** 컬렉션이 이 서버에서 생성되었는지, 원격 서버에 있는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.6.0 - 추가

### `sensitive` {#sensitive}

**설명:** 컬렉션에 민감한 콘텐츠가 포함되었다고 표시되었는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.6.0 - 추가

### `discoverable` {#discoverable}

**설명:** 컬렉션을 소유자의 프로필, 검색 결과, 추천에 표시할지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.6.0 - 추가

### `tag` {#tag}

**설명:** 이 컬렉션을 설명하는 하나의 해시태그입니다.\
**유형:** {{<nullable>}} [ShallowTag]({{< relref "entities/ShallowTag" >}})\
**버전 이력:**\
4.6.0 - 추가

### `created_at` {#created_at}

**설명:** 컬렉션 생성 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
4.6.0 - 추가

### `updated_at` {#updated_at}

**설명:** 컬렉션의 마지막 갱신 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
4.6.0 - 추가

### `item_count` {#item_count}

**설명:** 이 컬렉션의 항목 수입니다.\
**유형:** 정수\
**버전 이력:**\
4.6.0 - 추가

### `items` {#items}

**설명:** 이 컬렉션의 항목입니다.\
**유형:** 배열: [CollectionItem]({{< relref "entities/CollectionItem" >}})\
**버전 이력:**\
4.6.0 - 추가

## WrappedCollection 엔터티 {#WrappedCollection}

일반적인 [Collection]({{< relref "entities/Collection" >}})을 래퍼 객체로 감싸 확장성을 제공하며, [CollectionWithAccounts]({{< relref "entities/CollectionWithAccounts" >}}) 및 API의 다른 부분과 일관성을 유지합니다.

### 예시 {#example-1}

```json
{
  "collection": {
    "id": "116131056935959117",
    "account_id": "113668893442515793",
    "uri": "https://example.com/ap/113668893442515793/collections/116131056935959117",
    "url": "https://example.com/collections/116131056935959117",
    "name": "Excellent people",
    // ...
  }
}
```

### `collection` {#collection}

**설명:** 실제 컬렉션입니다.\
**유형:** [Collection]({{< relref "entities/Collection" >}})\
**버전 이력:**\
4.6.0 - 추가

## Collections 엔터티 {#Collections}

[Collection]({{< relref "entities/Collection" >}}) 엔터티 목록을 객체로 감싸 확장성을 제공하고 API의 다른 부분과 일관성을 높입니다.

### 예시 {#example-2}

```json
{
  "collections": [
    {
      "id": "116131056935959117",
      "account_id": "113668893442515793",
      "uri": "https://example.com/ap/113668893442515793/collections/116131056935959117",
      "url": "https://example.com/collections/116131056935959117",
      "name": "Excellent people",
      // ...
    },
    // ...
  ]
}
```

### `collections` {#collections}

**설명:** 컬렉션 목록입니다.\
**유형:** 배열: [Collection]({{< relref "entities/Collection" >}})\
**버전 이력:**\
4.6.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/collections" caption="collections API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/collection_serializer.rb" caption="app/serializers/rest/collection_serializer.rb" >}}
