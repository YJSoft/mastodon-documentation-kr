---
title: 신원 증명 API 메서드
description: 신원 제공업체에서 사용합니다.
menu:
  docs:
    name: 신원 증명
    parent: methods
    identifier: methods-proofs
aliases: [
  "/methods/proofs",
  "/api/methods/proofs",
  "/methods/accounts/proofs",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

{{< hint style="danger" >}}
**사용 중단 예정**\
신원 증명은 3.5.0 이상에서 사용 중단 예정입니다. 이전의 유일한 증명 제공업체는 Keybase였지만 Zoom에 인수된 이후 개발이 완전히 중단되었습니다.
{{< /hint >}}

## 신원 증명 조회 {{%removed%}} {#get}

```http
GET /api/proofs HTTP/1.1
```

**반환:** 제공업체가 정의한 사용자 지정 응답\
**OAuth:** 공개\
**버전 이력:**\
2.8.0 - 추가

#### 요청 {#request}
##### 쿼리 매개변수 {#query-parameters}

provider
: 문자열. 조회할 신원 제공업체입니다. 현재 `keybase`만 지원합니다(대소문자 구분).

username
: 문자열. 선택한 신원 제공업체의 사용자명입니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

"keybase" `provider`를 통해 `username` "gargron"을 조회합니다.

```json
{
  "avatar": "https://files.mastodon.social/accounts/avatars/000/000/001/original/d96d39a0abb45b92.jpg",
  "signatures": [
    {
      "sig_hash": "5cfc20c7018f2beefb42a68836da59a792e55daa4d118498c9b1898de7e845690f",
      "kb_username": "gargron"
    }
  ]
}
```

##### 404: 찾을 수 없음 {#404-not-found}

`provider`에서 `username`의 신원 증명을 찾지 못했습니다.

```json
{
  "error": "Record not found"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/pull/17045" caption="Keybase 통합 제거 (#17045)" >}}
