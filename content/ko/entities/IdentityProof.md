---
title: 신원 증명 (IdentityProof)
description: 외부 신원 제공자의 증명을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/identityproof",
  "/entities/IdentityProof",
  "/api/entities/identityproof",
  "/api/entities/IdentityProof",
]
---

{{< hint style="danger" >}}
신원 증명은 3.5.0 이상에서 폐기 예정이 되었습니다. 이전에는 Keybase가 유일한 증명 제공자였지만, Zoom에 인수된 이후 Keybase 개발이 완전히 중단되었습니다.
{{< /hint >}}

```json
{
  "provider": "Keybase",
  "provider_username": "gargron",
  "updated_at": "2019-07-21T20:14:39.596Z",
  "proof_url": "https://keybase.io/gargron/sigchain#5cfc20c7018f2beefb42a68836da59a792e55daa4d118498c9b1898de7e845690f",
  "profile_url": "https://keybase.io/gargron"
}
```

## 속성 {#attributes}

### `provider` {#provider}

**설명:** 신원 제공자의 이름입니다.\
**유형:** 문자열\
**버전 이력:**\
2.8.0 - 추가

### `provider_username` {#provider_username}

**설명:** 신원 제공자 서비스에서 사용하는 계정 소유자의 사용자명입니다.\
**유형:** 문자열\
**버전 이력:**\
2.8.0 - 추가

### `updated_at` {#updated_at}

**설명:** 신원 증명의 마지막 갱신 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
2.8.0 - 추가

### `proof_url` {#proof_url}

**설명:** 신원 제공자가 호스팅하는 신원 증명서 링크입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
2.8.0 - 추가

### `profile_url` {#profile_url}

**설명:** 신원 제공자에 있는 계정 소유자의 프로필 URL입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
2.8.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/accounts#identity_proofs" caption="GET /api/v1/accounts/:id/identity_proofs" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/pull/17045" caption="Keybase 연동 제거 (#17045)" >}}





