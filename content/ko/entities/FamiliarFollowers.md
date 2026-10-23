---
title: 아는 팔로워 (FamiliarFollowers)
description: 내가 팔로우하는 사람 중 다른 특정 사용자도 팔로우하는 사람들의 부분집합을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/familiarfollowers",
  "/entities/FamiliarFollowers",
  "/api/entities/familiarfollowers",
  "/api/entities/FamiliarFollowers",
]
---

## 예시 {#example}

```json
[
  {
    "id":"1",
    "accounts":[
      {
        "id":"1087990",
        "username":"moss",
        "acct":"moss@goblin.camp",
        // ...
      },
      {
        "id":"1092723",
        "username":"vivianrose",
        "acct":"vivianrose",
        // ...
      },
      // ...
    ]
  },
  {
    "id":"2",
    "accounts":[]
  }
]
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 Account ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
3.5.0 - 추가

### `accounts` {#accounts}

**설명:** 내가 팔로우하는 계정 중 이 계정도 팔로우하는 계정입니다.\
**유형:** 배열: [Account]({{< relref "entities/Account" >}})\
**버전 이력:**\
3.5.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/accounts#familiar_followers" caption="GET /api/v1/accounts/:id/familiar_followers" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/familiar_followers_serializer.rb" caption="app/serializers/rest/familiar_followers_serializer.rb" >}}