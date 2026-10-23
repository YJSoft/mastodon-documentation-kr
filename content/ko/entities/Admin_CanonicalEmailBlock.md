---
title: 관리자용 정규 이메일 차단 (Admin::CanonicalEmailBlock)
description: 정규화된 이메일 차단 항목(해시)을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/admin-canonicalemailblock",
  "/entities/Admin-CanonicalEmailBlock",
  "/entities/admin_canonicalemailblock",
  "/entities/Admin_CanonicalEmailBlock",
  "/api/entities/admin-canonicalemailblock",
  "/api/entities/Admin-CanonicalEmailBlock",
  "/api/entities/admin_canonicalemailblock",
  "/api/entities/Admin_CanonicalEmailBlock",
]
---

## 예시 {#example}

```json
{
	"id": "2",
	"canonical_email_hash": "b344e55d11b3fc25d0d53194e0475838bf17e9be67ce3e6469956222d9a34f9c"
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 이메일 차단 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.0.0 - 추가

### `canonical_email_hash` {#canonical_email_hash}

**설명:** 정규화된 이메일 주소의 SHA256 해시입니다.\
**유형:** 문자열 (SHA256)\
**버전 이력:**\
4.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/admin/canonical_email_blocks" caption="admin/canonical_email_blocks API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/admin/canonical_email_block_serializer.rb" caption="app/serializers/rest/admin/canonical_email_block_serializer.rb" >}}