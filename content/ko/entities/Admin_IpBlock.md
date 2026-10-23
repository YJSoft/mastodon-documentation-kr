---
title: 관리자용 IP 차단 (Admin::IpBlock)
description: 가입에 사용할 수 없는 IP 주소 범위를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/admin-ipblock",
  "/entities/Admin-IpBlock",
  "/entities/admin_ipblock",
  "/entities/Admin_IpBlock",
  "/api/entities/admin-ipblock",
  "/api/entities/Admin-IpBlock",
  "/api/entities/admin_ipblock",
  "/api/entities/Admin_IpBlock",
]
---

## 예시 {#example}

```json
{
  "id": "1",
  "ip": "8.8.8.8/32",
  "severity": "no_access",
  "comment": "",
  "created_at": "2022-11-16T07:22:00.501Z",
  "expires_at": null
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 DomainBlock ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.0.0 - 추가

### `ip` {#ip}

**설명:** 연합이 허용되지 않는 IP 주소 범위입니다.\
**유형:** 문자열 (IP 주소 및 접두사)\
**버전 이력:**\
4.0.0 - 추가

### `severity` {#severity}

**설명:** 이 IP 차단에 연결된 정책입니다.\
**유형:** 문자열 (열거형, 다음 중 하나)\
`sign_up_requires_approval` = 이 IP 범위에서 가입하면 대기 중인 계정이 생성됩니다.\
`sign_up_block` = 이 IP 범위의 모든 가입을 거절합니다.\
`no_access` = 이 IP 범위의 모든 활동을 완전히 거절합니다.\
**버전 이력:**\
4.0.0 - 추가

### `comment` {#comment}

**설명:** 이 IP 차단에 기록된 사유입니다.\
**유형:** 문자열\
**버전 이력:**\
4.0.0 - 추가

### `created_at` {#created_at}

**설명:** IP 차단 생성 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
4.0.0 - 추가

### `expires_at` {#expires_at}

**설명:** IP 차단 만료 시각입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
4.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref page="methods/admin/ip_blocks" caption="admin/ip_blocks API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/admin/ip_block_serializer.rb" caption="app/serializers/rest/admin/ip_block_serializer.rb" >}}