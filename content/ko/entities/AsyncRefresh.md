---
title: 비동기 새로고침 (AsyncRefresh)
description: 비동기 새로고침 상태입니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/AsyncRefresh",
  "/api/entities/AsyncRefresh",
]
---

## 예시 {#example}

```json
{
  "async_refresh": {
    "id": "ImNvbnRleHQ6MTEzNjQwNTczMzAzNzg1MTc4OnJlZnJlc2gi--c526259eb4a1f3ef0d4b91cf8c99bf501330a815",
    "status": "running",
    "result_count": 2
  }
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 비동기 새로고침 ID입니다.\
**유형:** 문자열\
**버전 이력:**\
4.4.0 - 추가

### `status` {#status}

**설명:** 비동기 새로고침의 상태입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`running` = 비동기 새로고침을 수행하는 백그라운드 작업이 아직 실행 중이며 새로운 결과가 나올 수 있습니다.\
`finished` = 이 비동기 새로고침을 수행하는 백그라운드 작업이 종료되었으며 해당 작업에서 새로운 결과를 기대할 수 없습니다.\
**버전 이력:**\
4.4.0 - 추가

### `result_count` {#result_count}

**설명:** 이 비동기 새로고침으로 이미 생성하거나 가져온 결과 수입니다(선택적).\
**유형:** {{<nullable>}} 정수\
**버전 이력:**\
4.4.0 - 추가
