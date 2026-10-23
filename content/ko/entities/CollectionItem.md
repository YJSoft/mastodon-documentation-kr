---
title: 컬렉션 항목 (CollectionItem)
description: 컬렉션의 단일 항목을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/collectionitem",
  "/entities/CollectionItem",
  "/api/entities/collectionitem",
  "/api/entities/CollectionItem",
]
---

## 예시 {#example}

```json
{
  "id": "116141056635954112",
  "account_id": "112658193342215767",
  "state": "accepted",
  "created_at": "2026-02-25T11:35:01.394Z"
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 항목 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.6.0 - 추가

### `account_id` {#account_id}

**설명:** 이 항목이 나타내는 계정의 ID입니다.\
**유형:** {{<nullable>}} 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.6.0 - 추가

### `state` {#state}

**설명:** 항목의 현재 상태입니다.\
**유형:** 문자열 (열거형, 다음 중 하나)\
`pending` = 이 컬렉션에 추가되는 것에 대한 계정의 동의를 아직 확인하지 못했습니다.\
`accepted` = 계정이 이 컬렉션에 소개되는 데 동의했습니다.\
`rejected` = 계정이 이 컬렉션에 추가해 달라는 요청을 거절했습니다.\
`revoked` = 계정이 이 컬렉션에 소개되는 것에 대한 동의를 철회했습니다.\
**버전 이력:**\
4.6.0 - 추가

### `created_at` {#created_at}

**설명:** 항목이 컬렉션에 추가된 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
4.6.0 - 추가

## WrappedCollectionItem 엔터티 {#WrappedCollectionItem}

일반적인 [CollectionItem]({{< relref "entities/CollectionItem" >}})을 래퍼 객체로 감싸 [CollectionWithAccounts]({{< relref "entities/CollectionWithAccounts" >}}) 및 API의 다른 부분과 일관성을 유지합니다.

### 예시 {#example-1}

```json
{
  "collection_item": {
    "id": "116141056635954112",
    "account_id": "112658193342215767",
    "state": "accepted",
    "created_at": "2026-02-25T11:35:01.394Z"
  }
}
```

### `collection_item` {#collection_item}

**설명:** 실제 컬렉션 항목입니다.\
**유형:** [CollectionItem]({{< relref "entities/CollectionItem" >}})\
**버전 이력:**\
4.6.0 - 추가


## 함께 보기 {#see-also}

{{< page-relref ref="methods/collections" caption="collections API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/collection_item_serializer.rb" caption="app/serializers/rest/collection_item_serializer.rb" >}}
