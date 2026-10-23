---
title: 관계 단절 이벤트 (RelationshipSeveranceEvent)
description: 팔로우 관계를 단절시킨 중재 또는 차단 이벤트의 요약입니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/RelationshipSeveranceEvent",
  "/api/entities/RelationshipSeveranceEvent",
]
---

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 관계 단절 이벤트 ID입니다.\
**유형:** 문자열 (정수에서 변환)\
**버전 이력:**\
4.3.0 - 추가

### `type` {#type}

**설명:** 이벤트 유형입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`domain_block` = 중재자가 도메인 전체를 정지했습니다.\
`user_domain_block` = 사용자가 도메인 전체를 차단했습니다.\
`account_suspension` = 중재자가 특정 계정을 정지했습니다.\
**버전 이력:**\
4.3.0 - 추가

### `purged` {#purged}

**설명:** 기반 문제가 삭제되어 단절된 관계 목록을 사용할 수 없는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.3.0 - 추가

### `target_name` {#target_name}

**설명:** 중재/차단 이벤트 대상의 이름입니다. 이벤트 유형에 따라 도메인 이름이나 사용자 핸들입니다.\
**유형:** 문자열\
**버전 이력:**\
4.3.0 - 추가

### `followers_count` {#followers_count}

**설명:** 이벤트로 인해 제거된 팔로워 수입니다.\
**유형:** 정수\
**버전 이력:**\
4.3.0 - 추가

### `following_count` {#following_count}

**설명:** 이벤트로 인해 사용자가 팔로우를 중단한 계정 수입니다.\
**유형:** 정수\
**버전 이력:**\
4.3.0 - 추가

### `created_at` {#created_at}

**설명:** 이벤트가 발생한 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
4.3.0 - 추가
