---
title: 관리자용 계정 (Admin::Account)
description: 주어진 계정의 관리자 수준 정보입니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/admin-account",
  "/entities/Admin-Account",
  "/entities/admin_account",
  "/entities/Admin_Account",
  "/api/entities/admin-account",
  "/api/entities/Admin-Account",
  "/api/entities/admin_account",
  "/api/entities/Admin_Account",
]
---

## 예시 {#example}

```json
{
  "id": "108965278956942133",
  "username": "admin",
  "domain": null,
  "created_at": "2022-09-08T23:03:26.762Z",
  "email": "admin@mastodon.local",
  "ip": "192.168.42.1",
  "role": {
    "id": 3,
    "name": "Owner",
    "color": "",
    "position": 1000,
    "permissions": 1,
    "highlighted": true,
    "created_at": "2022-09-08T22:48:07.983Z",
    "updated_at": "2022-09-08T22:48:07.983Z"
  },
  "confirmed": true,
  "suspended": false,
  "silenced": false,
  "sensitized": true,
  "disabled": false,
  "approved": true,
  "locale": null,
  "invite_request": null,
  "ips": [
    {
      "ip": "192.168.42.1",
      "used_at": "2022-09-15T01:38:58.851Z"
    }
  ],
  "account": {
    "id": "108965278956942133",
    "username": "admin",
    "acct": "admin",
    "display_name": "",
    "locked": false,
    "bot": false,
    "discoverable": null,
    "group": false,
    "created_at": "2022-09-08T00:00:00.000Z",
    "note": "",
    "url": "http://mastodon.local/@admin",
    "avatar": "http://mastodon.local/avatars/original/missing.png",
    "avatar_static": "http://mastodon.local/avatars/original/missing.png",
    "header": "http://mastodon.local/headers/original/missing.png",
    "header_static": "http://mastodon.local/headers/original/missing.png",
    "followers_count": 0,
    "following_count": 0,
    "statuses_count": 0,
    "last_status_at": null,
    "emojis": [],
    "fields": []
  }
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 계정 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
2.9.1 - 추가

### `username` {#username}

**설명:** 계정의 사용자명입니다.\
**유형:** 문자열\
**버전 이력:**\
2.9.1 - 추가

### `domain` {#domain}

**설명:** 원격 계정인 경우 계정의 도메인입니다.\
**유형:** {{<nullable>}} 문자열, 로컬 계정은 null\
**버전 이력:**\
2.9.1 - 추가

### `created_at` {#created_at}

**설명:** 계정이 처음 발견된 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
2.9.1 - 추가

### `email` {#email}

**설명:** 계정에 연결된 이메일 주소입니다.\
**유형:** 문자열\
**버전 이력:**\
2.9.1 - 추가

### `ip` {#ip}

**설명:** 이 계정에 마지막으로 로그인할 때 사용한 IP 주소입니다.\
**유형:** {{<nullable>}} 문자열\
**버전 이력:**\
2.9.1 - 추가\
3.5.0 - 버그로 인해 반환 형식이 문자열에서 [Admin::Ip]({{< relref "entities/Admin_Ip" >}})로 변경됨\
4.0.0 - 버그 수정으로 반환 형식이 다시 문자열로 변경됨

### `ips` {#ip}

**설명:** 이 계정에 연결된 알려진 모든 IP 주소입니다.\
**유형:** 배열: [Admin::Ip]({{< relref "entities/Admin_Ip" >}})\
**버전 이력:**\
3.5.0 - 추가

### `locale` {#locale}

**설명:** 계정의 로캘입니다.\
**유형:** 문자열 (ISO 639-1 두 글자 언어 코드)\
**버전 이력:**\
2.9.1 - 추가

### `invite_request` {#invite_request}

**설명:** 초대 요청 시 기재한 사유입니다(가입에 수동 승인이 필요한 서버).\
**유형:** {{<nullable>}} 문자열\
**버전 이력:**\
2.9.1 - 추가

### `role` {#role}

**설명:** 계정의 현재 역할입니다.\
**유형:** [Role]({{<relref "entities/role">}})\
**버전 이력:**\
2.9.1 - 추가됨. 문자열 반환(열거형, `user` `moderator` `admin` 중 하나)\
4.0.0 - 이제 Role 엔터티 사용

### `confirmed` {#confirmed}

**설명:** 계정이 이메일 주소를 확인했는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.9.1 - 추가

### `approved` {#approved}

**설명:** 현재 계정이 승인되었는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.9.1 - 추가

### `disabled` {#disabled}

**설명:** 현재 계정이 비활성화되었는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.9.1 - 추가

### `sensitized` {#sensitized}

**설명:** 현재 계정이 민감함으로 표시되었는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.0.0 - 추가

### `silenced` {#silenced}

**설명:** 현재 계정이 제한(숨김)되었는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.9.1 - 추가

### `suspended` {#suspended}

**설명:** 현재 계정이 정지되었는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.9.1 - 추가

### `account` {#account}

**설명:** 계정의 사용자 수준 정보입니다.\
**유형:** [Account]({{< relref "entities/account" >}})\
**버전 이력:**\
2.9.1 - 추가

### `created_by_application_id` {{%optional%}} {#created_by_application_id}

**설명:** 해당하는 경우, 이 계정을 생성한 [Application]({{< relref "entities/application" >}})의 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
2.9.1 - 추가

### `invited_by_account_id` {{%optional%}} {#invited_by_account_id}

**설명:** 해당하는 경우, 이 사용자를 초대한 [Account]({{< relref "entities/account" >}})의 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
2.9.1 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/admin/accounts" caption="admin/accounts API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/admin/account_serializer.rb" caption="app/serializers/rest/admin/account_serializer.rb" >}}
