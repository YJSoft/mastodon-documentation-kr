---
title: 관리자용 도메인 차단 (Admin::DomainBlock)
description: 연합이 제한된 도메인을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/admin-domainblock",
  "/entities/Admin-DomainBlock",
  "/entities/admin_domainblock",
  "/entities/Admin_DomainBlock",
  "/api/entities/admin-domainblock",
  "/api/entities/Admin-DomainBlock",
  "/api/entities/admin_domainblock",
  "/api/entities/Admin_DomainBlock",
]
---

## 예시 {#example}

```json
{
  "id": "1",
  "domain": "example.com",
  "digest": "a379a6f6eeafb9a55e378c118034e2751e682fab9f2d30ab13d2125586ce1947",
  "created_at": "2022-11-16T08:15:34.238Z",
  "severity": "noop",
  "reject_media": false,
  "reject_reports": false,
  "private_comment": null,
  "public_comment": null,
  "obfuscate": false
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 DomainBlock ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.0.0 - 추가

### `domain` {#domain}

**설명:** 연합이 허용되지 않는 도메인입니다.\
**유형:** 문자열\
**버전 이력:**\
4.0.0 - 추가

### `digest` {#digest}

**설명:** 연합이 허용되지 않는 도메인의 sha256 16진수 다이제스트입니다.\
**유형:** 문자열\
**버전 이력:**\
4.3.0 - 추가

### `created_at` {#created_at}

**설명:** 도메인의 연합이 차단된 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
4.0.0 - 추가

### `severity` {#severity}

**설명:** 이 도메인 차단에 적용할 정책입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`silence` = 이 도메인의 계정 게시물을 기본적으로 숨깁니다.\
`suspend` = 이 도메인에서 들어오는 모든 데이터를 거절합니다.\
`noop` = 아무것도 하지 않습니다. 미디어나 신고를 거절하는 데 사용할 수 있습니다.\
**버전 이력:**\
4.0.0 - 추가

### `reject_media` {#reject_media}

**설명:** 이 도메인의 미디어 첨부 파일을 거절할지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.0.0 - 추가

### `reject_reports` {#reject_reports}

**설명:** 이 도메인의 신고를 거절할지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.0.0 - 추가

### `private_comment` {#private_comment}

**설명:** \
**유형:** {{<nullable>}} 문자열\
**버전 이력:**\
4.0.0 - 추가

### `public_comment` {#public_comment}

**설명:** \
**유형:** {{<nullable>}} 문자열\
**버전 이력:**\
4.0.0 - 추가

### `obfuscate` {#obfuscate}

**설명:** 이 도메인 차단을 공개할 때 도메인을 가릴지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref page="methods/admin/domain_blocks" caption="admin/domain_blocks API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/admin/domain_block_serializer.rb" caption="app/serializers/rest/admin/domain_block_serializer.rb" >}}
