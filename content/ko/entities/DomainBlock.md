---
title: 도메인 차단 (DomainBlock)
description: 서버가 차단한 도메인을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/domainblock",
  "/entities/DomainBlock",
  "/api/entities/domainblock",
  "/api/entities/DomainBlock",
]
---

## 예시 {#example}

```json
{
  "domain":"daji******.com",
  "digest":"3752f63a7079d60c2de5dceb8bd7608e86a15544eb78a494a482041c3684b37f",
  "severity":"suspend",
  "comment":"Inappropriate content"
}
```

## 속성 {#attributes}

### `domain` {#domain}

**설명:** 차단된 도메인입니다. 가려져 있거나 일부 문자가 숨겨져 있을 수 있습니다.\
**유형:** 문자열\
**버전 이력:**\
4.0.0 - 추가

### `digest` {#digest}

**설명:** 도메인 문자열의 SHA256 해시 다이제스트입니다.\
**유형:** 문자열 (SHA256)\
**버전 이력:**\
4.0.0 - 추가

### `severity` {#severity}

**설명:** 도메인 차단 수준입니다.\
**유형:** 문자열 (열거형, 다음 중 하나)\
`silence` = 이 도메인의 사용자를 타임라인, 글타래, 알림에서 숨깁니다(해당 사용자를 팔로우하는 경우 제외).\
`suspend` = 이 도메인에서 들어오는 메시지를 거절하고 완전히 삭제합니다.\
**버전 이력:**\
4.0.0 - 추가

### `comment` {{%optional%}} {#comment}

**설명:** 도메인 차단의 선택적 사유입니다.\
**유형:** 문자열\
**버전 이력:**\
4.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/instance#domain_blocks" caption="GET /api/v1/instance/domain_blocks" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/domain_block_serializer.rb" caption="app/serializers/rest/domain_block_serializer.rb" >}}
