---
title: 관리자용 IP 주소 (Admin::Ip)
description: 사용자에 연결된 IP 주소를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/admin-ip",
  "/entities/Admin-Ip",
  "/entities/admin_ip",
  "/entities/Admin_Ip",
  "/api/entities/admin-ip",
  "/api/entities/Admin-Ip",
  "/api/entities/admin_ip",
  "/api/entities/Admin_Ip",
]
---

## 예시 {#example}

```json
{
	"ip": "192.168.42.1",
	"used_at": "2022-09-15T01:38:58.851Z"
}
```

## 속성 {#attributes}

### `ip` {#id}

**설명:** IP 주소입니다.\
**유형:** 문자열 (IP 주소)\
**버전 이력:**\
3.5.0 - 추가

### `used_at` {#used_at}

**설명:** 계정에서 IP 주소를 마지막으로 사용한 시각의 타임스탬프입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
3.5.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="entities/Admin_Account#ip" caption="Admin::Account (`ips` 속성)" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/admin/ip_serializer.rb" caption="app/serializers/rest/admin/ip_serializer.rb" >}}