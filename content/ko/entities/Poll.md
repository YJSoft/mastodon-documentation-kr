---
title: 투표 (Poll)
description: 게시물에 첨부된 투표를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/poll",
  "/entities/Poll",
  "/api/entities/poll",
  "/api/entities/Poll",
]
---

## 예시 {#example}

```json
{
  "id": "34830",
  "expires_at": "2019-12-05T04:05:08.302Z",
  "expired": true,
  "multiple": false,
  "votes_count": 10,
  "voters_count": null,
  "voted": true,
  "own_votes": [
    1
  ],
  "options": [
    {
      "title": "accept",
      "votes_count": 6
    },
    {
      "title": "deny",
      "votes_count": 4
    }
  ],
  "emojis": []
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 투표 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
2.8.0 - 추가

### `expires_at` {#expires_at}

**설명:** 투표 종료 시각입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜와 시각](/api/datetime-format#datetime)), 종료되지 않는 투표는 null\
**버전 이력:**\
2.8.0 - 추가

### `expired` {#expired}

**설명:** 현재 투표가 만료되었는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.8.0 - 추가

### `multiple` {#multiple}

**설명:** 투표에서 복수 선택을 허용하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.8.0 - 추가

### `votes_count` {#votes_count}

**설명:** 받은 표 수입니다.\
**유형:** 정수\
**버전 이력:**\
2.8.0 - 추가

### `voters_count` {#voters_count}

**설명:** 복수 선택 투표에 참여한 고유 계정 수입니다.\
**유형:** {{<nullable>}} 정수, `multiple`이 false이면 null\
**버전 이력:**\
2.8.0 - 추가

### `options` {#options}

**설명:** 투표에서 선택할 수 있는 답변입니다.\
**유형:** 배열: [Poll::Option](#Option)\
**버전 이력:**\
2.8.0 - 추가

### `emojis` {#emojis}

**설명:** 투표 선택지를 표시하는 데 사용할 사용자 지정 이모지입니다.\
**유형:** 배열: [CustomEmoji]({{< relref "entities/CustomEmoji" >}})\
**버전 이력:**\
2.8.0 - 추가

### `voted` {{%optional%}} {#voted}

**설명:** 사용자 토큰으로 호출한 경우, 인증된 사용자가 투표했는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.8.0 - 추가

### `own_votes` {{%optional%}} {#own_votes}

**설명:** 사용자 토큰으로 호출한 경우, 인증된 사용자가 선택한 항목입니다. `options`의 인덱스 값 배열을 포함합니다.\
**유형:** 배열: 정수\
**버전 이력:**\
2.8.0 - 추가

## Poll::Option 속성 {#Option}

### `title` {#option-title}

**설명:** 투표 선택지의 텍스트 값입니다.\
**유형:** 문자열\
**버전 이력:**\
2.8.0 - 추가

#### `votes_count` {#option-votes_count}

**설명:** 이 선택지가 받은 총 표 수입니다.\
**유형:** {{<nullable>}} 정수, 결과가 아직 공개되지 않았으면 null\
**버전 이력:**\
2.8.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="entities/Status#poll" caption="Status (`poll` 속성)" >}}

{{< page-relref ref="methods/polls" caption="polls API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/poll_serializer.rb" caption="app/serializers/rest/poll_serializer.rb" >}}





