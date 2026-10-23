---
title: 이메일 API 메서드
description: 필요하면 새 이메일 주소로 새 확인 이메일을 요청합니다.
menu:
  docs:
    name: 이메일
    parent: methods-apps
    identifier: methods-emails
aliases: [
  "/methods/emails",
  "/api/methods/emails",
  "/methods/apps/emails",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 확인 이메일 재전송 {#confirmation}

```http
POST /api/v1/emails/confirmations HTTP/1.1
```

새 확인 이메일을 다시 보냅니다. 이메일을 제공하면 확인 이메일을 다시 보내기 전에 미확인 사용자의 이메일을 변경합니다.

**반환:** 없음\
**OAuth:** 미확인 사용자를 생성한 클라이언트에 발급된 사용자 토큰\
**버전 이력:**\
3.4.0 - 추가

#### 요청 {#request}
##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

email
: 문자열. 제공하면 확인 이메일을 다시 보내기 전에 미확인 사용자의 이메일을 변경합니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

```json
{}
```

##### 403: 금지됨 {#403-forbidden}

토큰과 연결된 클라이언트가 미확인 사용자를 소유하지 않습니다.

```json
{
	"error": "This method is only available to the application the user originally signed-up with"
}
```

또는 사용자가 이미 이메일을 확인했습니다.

```json
{
  "error": "This method is only available while the e-mail is awaiting confirmation"
}
```

---

## 함께 보기 {#see-also}

{{< page-relref ref="methods/apps#create" caption="POST /api/v1/apps" >}}

{{< page-relref ref="methods/accounts#create" caption="POST /api/v1/accounts" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/emails/confirmations_controller.rb" caption="app/controllers/api/v1/emails/confirmations_controller.rb" >}}
