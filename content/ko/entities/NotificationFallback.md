---
title: 알림 대체 정보 (NotificationFallback)
description: 사용자와 관련된 이벤트의 알림을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/NotificationFallback",
  "/api/entities/NotificationFallback",
]
---

## 속성 {#attributes}

### `title` {#title}

**설명:** 현지화된 알림 대체 제목입니다. 예를 들어 “Alice님이 나를 컬렉션에 추가했습니다”입니다.\
**유형:** 문자열 (HTML)\
**버전 이력:**\
4.6.0 - 추가

### `summary` {#summary}

**설명:** 현지화된 알림 대체 요약입니다. 예를 들어 “현재 앱은 최신 마스토돈 버전을 지원하지 않습니다. 모든 기능을 사용하려면 마스토돈 웹 앱에 로그인하세요.”입니다.\
**유형:** {{<nullable>}} 문자열 (HTML)\
**버전 이력:**\
4.6.0 - 추가

### `details` {#details}

**설명:** 현지화된 알림 상세 정보로, 예를 들어 알림을 클릭할 때 표시합니다.\
**유형:** {{<nullable>}} 문자열 (HTML)\
**버전 이력:**\
4.6.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/notifications" caption="notifications API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/concerns/notification_fallback_concern.rb" caption="app/serializers/concerns/notification_fallback_concern.rb" >}}



