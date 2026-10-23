---
title: 검색 (Search)
description: 검색 결과를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/results",
  "/entities/Results",
  "/entities/search",
  "/entities/Search",
  "/api/entities/results",
  "/api/entities/Results",
  "/api/entities/search",
  "/api/entities/Search",
]
---

## 예시 {#example}

q=cats limit=2 검색 예시의 일부

```json
{
  "accounts": [
    {
      "id": "180744",
      "username": "catstar",
      "acct": "catstar@catgram.jp",
      "display_name": "catstar",
      // ...
    },
    {
      "id": "214293",
      "username": "catsareweird",
      "acct": "catsareweird",
      "display_name": "Cats Are Weird",
      // ...
    }
  ],
  "statuses": [
    {
      "id": "103085519055545958",
      "created_at": "2019-11-05T13:23:09.000Z",
      // ...
      "content": "<p>cats<br>cats never change</p>",
      // ...
    },
    {
      "id": "101068121469614510",
      "created_at": "2018-11-14T06:31:48.000Z",
      // ...
      "spoiler_text": "Cats",
      // ...
      "content": "<p>Cats are inherently good at self-care. </p><p><a href=\"https://mspsocial.net/tags/cats\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>cats</span></a></p>",
      // ...
    },
    // ...
  ],
  "hashtags": [
    {
      "name": "cats",
      "url": "https://mastodon.social/tags/cats",
      "history": [
        {
          "day": "1574553600",
          "uses": "10",
          "accounts": "9"
        },
        // ...
      ]
    },
    {
      "name": "catsofmastodon",
      "url": "https://mastodon.social/tags/catsofmastodon",
      "history": [
        {
          "day": "1574553600",
          "uses": "6",
          "accounts": "5"
        },
        // ...
      ]
    }
  ],
  "collections": [
    {
      "id": "123456789012345678",
      "name": "Cats",
      "description": "Posters who are cats",
      // …
    }
  ]
}
```

## 속성 {#attributes}

### `accounts` {#accounts}

**설명:** 주어진 검색어와 일치하는 계정입니다.\
**유형:** 배열: [Account]({{< relref "entities/Account" >}})\
**버전 이력:**\
1.1.0 - 추가

### `statuses` {#statuses}

**설명:** 주어진 검색어와 일치하는 게시물입니다.\
**유형:** 배열: [Status]({{< relref "entities/Status" >}})\
**버전 이력:**\
1.1.0 - 추가

### `hashtags` {#hashtags}

**설명:** 주어진 검색어와 일치하는 해시태그입니다.\
**유형:** 배열: [Tag]({{< relref "entities/Tag" >}})\
**버전 이력:**\
1.1.0 - 추가\
2.4.1 - 문자열 배열을 반환하는 v1/search를 폐기 예정으로 지정하고, Tag 배열을 반환하는 v2/search 추가\
3.0.0 - v1/search 제거

### `collections` {#collections}

**설명:** 주어진 검색어와 일치하는 컬렉션입니다.\
**유형:** 배열: [Collection]({{< relref "entities/Collection" >}})\
**버전 이력:**\
4.6.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/search" caption="search API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/search_serializer.rb" caption="app/serializers/rest/search_serializer.rb" >}}



