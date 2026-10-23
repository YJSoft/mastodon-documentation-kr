---
title: 관리자용 도메인 허용 (Admin::DomainAllow)
description: 연합이 허용된 도메인을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/admin-domainallow",
  "/entities/Admin-DomainAllow",
  "/entities/admin_domainallow",
  "/entities/Admin_DomainAllow",
  "/api/entities/admin-domainallow",
  "/api/entities/Admin-DomainAllow",
  "/api/entities/admin_domainallow",
  "/api/entities/Admin_DomainAllow",
]
---

## 예시 {#example}

```json
{
	"id": "1",
	"domain": "mastodon.social",
	"created_at": "2022-09-14T21:23:02.755Z"
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 DomainAllow ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.0.0 - 추가

### `domain` {#domain}

**설명:** 연합이 허용된 도메인입니다.\
**유형:** 문자열\
**버전 이력:**\
4.0.0 - 추가

### `created_at` {#created_at}

**설명:** 도메인의 연합이 허용된 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
4.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref page="methods/admin/domain_allows" caption="admin/domain_allows API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/admin/domain_allow_serializer.rb" caption="app/serializers/rest/admin/domain_allow_serializer.rb" >}}