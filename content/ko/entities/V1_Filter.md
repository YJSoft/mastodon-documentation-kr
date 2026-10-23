---
title: V1 필터 (V1::Filter)
description: 사용자에게 표시하지 않을 게시물을 결정하는 사용자 정의 필터를 나타냅니다. 하나의 키워드 또는 구문을 포함합니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/v1_filter/",
  "/entities/V1_Filter",
  "/api/entities/v1_filter/",
  "/api/entities/V1_Filter",
]
---

## 예시 {#example}

```json
{
  "id": "8449",
  "phrase": "test",
  "context": [
    "home",
    "notifications",
    "public",
    "thread"
  ],
  "whole_word": false,
  "expires_at": "2019-11-26T09:08:06.254Z",
  "irreversible": true
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 필터 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
2.4.3 - 추가

### `phrase` {#phrase}

**설명:** 필터링할 텍스트입니다.\
**유형:** 문자열\
**버전 이력:**\
2.4.3 - 추가

### `context` {#context}

**설명:** 필터를 적용할 문맥입니다.\
**유형:** 배열: 문자열 (열거형 하나 이상)\
`home` = 홈 타임라인과 리스트\
`notifications` = 알림 타임라인\
`public` = 공개 타임라인\
`thread` = 게시물 상세 화면에서 펼친 글타래\
`account` = 프로필을 볼 때\
**버전 이력:**\
2.4.3 - 추가\
3.1.0 - `account` 추가

### `expires_at` {#expires_at}

**설명:** 필터 적용이 종료되는 시각입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜와 시각](/api/datetime-format#datetime)), 만료되지 않는 필터는 null\
**버전 이력:**\
2.4.3 - 추가

### `irreversible` {#irreversible}

**설명:** 홈과 알림에서 일치하는 엔터티를 서버가 삭제해야 하는지 나타냅니다. [필터 구현 지침]({{< relref "api/guidelines#filters" >}})을 참고하세요.\
**유형:** 불리언\
**버전 이력:**\
2.4.3 - 추가

### `whole_word` {#whole_word}

**설명:** 필터가 단어 경계를 고려해야 하는지 나타냅니다. [필터 구현 지침]({{< relref "api/guidelines#filters" >}})을 참고하세요.\
**유형:** 불리언\
**버전 이력:**\
2.4.3 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="api/guidelines#filters" caption="필터 구현 지침" >}}

{{< page-relref ref="methods/filters#v1" caption="v1 필터 API" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/v1/filter_serializer.rb" caption="app/serializers/rest/v1/filter_serializer.rb" >}}



