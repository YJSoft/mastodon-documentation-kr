---
title: 계정 경고 (AccountWarning)
description: 특정 계정에 대한 중재 경고입니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/AccountWarning",
  "/api/entities/AccountWarning",
]
---

## 속성 {#attributes}

### `id` {#id}

**설명:** 계정 경고 ID입니다.\
**유형:** 문자열 (정수에서 변환)\
**버전 이력:**\
4.3.0 - 추가

### `action` {#action}

**설명:** 계정에 취한 조치입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`none` = 조치를 취하지 않았으며 단순한 경고입니다.\
`disable` = 계정이 비활성화되었습니다.\
`mark_statuses_as_sensitive` = 대상 계정의 특정 게시물이 민감함으로 표시되었습니다.\
`delete_statuses` = 대상 계정의 특정 게시물이 삭제되었습니다.\
`sensitive` = 대상 계정의 모든 게시물을 민감함으로 표시합니다.\
`silence` = 대상 계정이 제한되었습니다.\
`suspend` = 대상 계정이 정지되었습니다.\
**버전 이력:**\
4.3.0 - 추가

### `text` {#text}

**설명:** 중재자가 대상 계정에 보낸 메시지입니다.\
**유형:** 문자열\
**버전 이력:**\
4.3.0 - 추가

### `status_ids` {#status_ids}

**설명:** 경고와 관련된 게시물 ID 목록입니다. `action`이 `mark_statuses_as_sensitive` 또는 `delete_statuses`이면 조치 대상 게시물입니다. 조치가 `delete_statuses`이면 이의 제기 상태에 관계없이 복구할 수 없게 삭제되어 클라이언트에서 접근할 수 없습니다.\
**유형:** {{<nullable>}} 배열: 문자열 (정수에서 변환), 또는 null\
**버전 이력:**\
4.3.0 - 추가

### `target_account` {#target_account}

**설명:** 중재 결정의 대상 계정입니다. 이 `AccountWarning`이 [Notification](/entities/Notification/)에 포함되면 항상 해당 알림을 요청한 인증된 계정과 같습니다.\
**유형:** [Account]({{< relref "entities/Account" >}})\
**버전 이력:**\
4.3.0 - 추가

### `appeal` {#appeal}

**설명:** 대상 계정이 제출한 이의 제기입니다(있는 경우).\
**유형:** {{<nullable>}} [Appeal]({{< relref "entities/Appeal" >}}), 또는 null\
**버전 이력:**\
4.3.0 - 추가

### `created_at` {#created_at}

**설명:** 이벤트가 발생한 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
4.3.0 - 추가
