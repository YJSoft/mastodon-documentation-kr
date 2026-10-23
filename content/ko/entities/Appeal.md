---
title: 이의 제기 (Appeal)
description: 중재 조치에 대한 이의 제기입니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/Appeal",
  "/api/entities/Appeal",
]
---

## 속성 {#attributes}

### `text` {#text}

**설명:** 중재 대상 계정이 중재자에게 보낸 이의 제기 내용입니다.\
**유형:** 문자열\
**버전 이력:**\
4.3.0 - 추가

### `state` {#state}

**설명:** 이의 제기 상태입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`approved` = 중재자가 이의 제기를 승인했습니다.\
`rejected` = 중재자가 이의 제기를 거절했습니다.\
`pending` = 이의 제기가 제출되었지만 아직 승인되거나 거절되지 않았습니다.\
**버전 이력:**\
4.3.0 - 추가
