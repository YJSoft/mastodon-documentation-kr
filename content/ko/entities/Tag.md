---
title: 태그 (Tag)
description: 게시물 콘텐츠에 사용된 해시태그를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/tag",
  "/entities/Tag",
  "/api/entities/tag",
  "/api/entities/Tag",
]
---

## 예시 {#example}

```json
{
  "id": "802",
  "name": "nowplaying",
  "url": "https://mastodon.social/tags/nowplaying",
  "history": [
    {
      "day": "1574553600",
      "uses": "200",
      "accounts": "31"
    },
    {
      "day": "1574467200",
      "uses": "272",
      "accounts": "39"
    },
    {
      "day": "1574380800",
      "uses": "345",
      "accounts": "40"
    },
    {
      "day": "1574294400",
      "uses": "366",
      "accounts": "46"
    },
    {
      "day": "1574208000",
      "uses": "226",
      "accounts": "32"
    },
    {
      "day": "1574121600",
      "uses": "217",
      "accounts": "42"
    },
    {
      "day": "1574035200",
      "uses": "214",
      "accounts": "34"
    }
  ],
  "following": false,
  "featuring": false
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 해시태그 ID입니다. 중재 도구와 관리자 API용 URL을 구성하는 데 유용합니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
3.5.0 - 관리자 API에 추가
4.3.1 - 공개 API에 추가

### `name` {#name}

**설명:** # 기호 뒤의 해시태그 값입니다.\
**유형:** 문자열\
**버전 이력:**\
0.9.0 - 추가

### `url` {#url}

**설명:** 서버의 해시태그 링크입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
0.9.0 - 추가

### `history` {#history}

**설명:** 주어진 날짜들(보통 지난 일주일)의 사용 통계입니다.\
**유형:** 배열: 해시\
**버전 이력:**\
2.4.1 - 추가

#### `history[][day]` {#history-day}

**설명:** 해당 날짜 자정의 UNIX 타임스탬프입니다.\
**유형:** 문자열 (UNIX 타임스탬프)\
**버전 이력:**\
2.4.1 - 추가

#### `history[][uses]` {#history-uses}

**설명:** 해당 날짜의 태그 사용 횟수입니다.\
**유형:** 문자열 (정수에서 변환)\
**버전 이력:**\
2.4.1 - 추가

#### `history[][accounts]` {#history-accounts}

**설명:** 해당 날짜에 태그를 사용한 총 계정 수입니다.\
**유형:** 문자열 (정수에서 변환)\
**버전 이력:**\
2.4.1 - 추가

### `following` {{%optional%}} {#following}

**설명:** 현재 토큰으로 인증된 사용자가 이 태그를 팔로우하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.0.0 - 추가

### `featuring` {{%optional%}} {#featuring}

**설명:** 현재 토큰으로 인증된 사용자가 프로필에 이 태그를 소개하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.4.0 - 추가

## Admin::Tag 속성 {#admin}

```json
{
  "id": "802",
  "name": "caturday",
  "url": "https://mastodon.example/tags/caturday",
  "history": [
    {
      "day": "1669507200",
      "accounts": "53",
      "uses": "56"
    },
    {
      "day": "1669420800",
      "accounts": "142",
      "uses": "171"
    },
    {
      "day": "1669334400",
      "accounts": "11",
      "uses": "11"
    },
    {
      "day": "1669248000",
      "accounts": "8",
      "uses": "9"
    },
    {
      "day": "1669161600",
      "accounts": "8",
      "uses": "20"
    },
    {
      "day": "1669075200",
      "accounts": "11",
      "uses": "11"
    },
    {
      "day": "1668988800",
      "accounts": "17",
      "uses": "22"
    }
  ],
  "trendable": true,
  "usable": true,
  "requires_review": false
}
```

### `trendable` {#trendable}

**설명:** 해시태그가 유행에 표시되도록 승인되었는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
3.5.0 - 추가

### `usable` {#usable}

**설명:** 해시태그의 자동 링크가 비활성화되지 않았는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
3.5.0 - 추가

### `requires_review` {#requires_review}

**설명:** 해시태그의 유행 표시 승인 또는 거절을 아직 검토하지 않았는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
3.5.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="entities/Search#hashtags" caption="Search (`tags` 속성)" >}}

{{< page-relref ref="methods/tags" caption="tags API 메서드" >}}

{{< page-relref ref="methods/featured_tags#suggestions" caption="GET /api/v1/featured_tags/suggestions" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/tag_serializer.rb" caption="app/serializers/rest/tag_serializer.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/admin/tag_serializer.rb" caption="app/serializers/rest/admin/tag_serializer.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/models/tag.rb" caption="app/models/tag.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/models/trends/history.rb" caption="app/models/trends/history.rb" >}}
