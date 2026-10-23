---
title: 알림 정책 (NotificationPolicy)
description: 사용자의 알림 필터링 정책을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/NotificationPolicy",
]
---

## 속성 {#attributes}

### `for_not_following` {#for_not_following}

**설명:** 사용자가 팔로우하지 않는 계정의 알림을 `accept`, `filter`, `drop` 중 어떻게 처리할지 나타냅니다. `drop`은 기반 활동을 막지 않고 알림 객체 생성을 완전히 방지하며, `filter`는 필터링된 것으로 표시하고, `accept`는 처리에 영향을 주지 않습니다.\
**유형:** 문자열 (`accept`, `filter`, `drop` 중 하나)\
**버전 이력:**\
4.3.0 - 추가

### `for_not_followers` {#for_not_followers}

**설명:** 사용자를 팔로우하지 않는 계정의 알림을 `accept`, `filter`, `drop` 중 어떻게 처리할지 나타냅니다. `drop`은 기반 활동을 막지 않고 알림 객체 생성을 완전히 방지하며, `filter`는 필터링된 것으로 표시하고, `accept`는 처리에 영향을 주지 않습니다.\
**유형:** 문자열 (`accept`, `filter`, `drop` 중 하나)\
**버전 이력:**\
4.3.0 - 추가

### `for_new_accounts` {#for_new_accounts}

**설명:** 지난 30일 이내에 생성된 계정의 알림을 `accept`, `filter`, `drop` 중 어떻게 처리할지 나타냅니다. `drop`은 기반 활동을 막지 않고 알림 객체 생성을 완전히 방지하며, `filter`는 필터링된 것으로 표시하고, `accept`는 처리에 영향을 주지 않습니다.\
**유형:** 문자열 (`accept`, `filter`, `drop` 중 하나)\
**버전 이력:**\
4.3.0 - 추가

### `for_private_mentions` {#for_private_mentions}

**설명:** 개인 멘션 알림을 `accept`, `filter`, `drop` 중 어떻게 처리할지 나타냅니다. `drop`은 기반 활동을 막지 않고 알림 객체 생성을 완전히 방지하며, `filter`는 필터링된 것으로 표시하고, `accept`는 처리에 영향을 주지 않습니다. 사용자가 시작한 개인 멘션의 답글과 사용자가 팔로우하는 계정은 이 값에 관계없이 항상 허용합니다.\
**유형:** 문자열 (`accept`, `filter`, `drop` 중 하나)\
**버전 이력:**\
4.3.0 - 추가

### `for_limited_accounts` {#for_limited_accounts}

**설명:** 중재자가 제한한 계정의 알림을 `accept`, `filter`, `drop` 중 어떻게 처리할지 나타냅니다. `drop`은 기반 활동을 막지 않고 알림 객체 생성을 완전히 방지하며, `filter`는 필터링된 것으로 표시하고, `accept`는 처리에 영향을 주지 않습니다.\
**유형:** 문자열 (`accept`, `filter`, `drop` 중 하나)\
**버전 이력:**\
4.3.0 - 추가

### `summary` {#summary}

**설명:** 필터링된 알림의 요약입니다.\
**유형:** 해시\
**버전 이력:**\
4.3.0 - 추가

### `summary[pending_requests_count]` {#pending_requests_count}

**설명:** 사용자에게 해제하지 않은 필터링된 알림을 보낸 서로 다른 계정 수입니다. 최대 100입니다.\
**유형:** 정수\
**버전 이력:**\
4.3.0 - 추가

### `summary[pending_notifications_count]` {#pending_notifications_count}

**설명:** 해제하지 않은 필터링된 알림의 총수입니다. 정확하지 않을 수 있습니다.\
**유형:** 정수\
**버전 이력:**\
4.3.0 - 추가

## 예시 {#example}

```json

{
  "for_not_following": "accept",
  "for_not_followers": "accept",
  "for_new_accounts": "accept",
  "for_private_mentions": "drop",
  "for_limited_accounts": "filter",
  "summary": {
    "pending_requests_count": 0,
    "pending_notifications_count": 0
  }
}

```

## 함께 보기 {#see-also}

{{< page-relref ref="methods/notifications" caption="notifications API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/notification_policy_serializer.rb" caption="app/serializers/rest/notification_policy_serializer.rb" >}}
