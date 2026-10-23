---
title: 환경설정 API 메서드
description: 클라이언트 간에 공유할 공통 동작 환경설정입니다.
menu:
  docs:
    name: 환경설정
    parent: methods-accounts
    identifier: methods-preferences
aliases: [
  "/methods/preferences",
  "/api/methods/preferences",
  "/methods/accounts/preferences",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 사용자 환경설정 조회 {#get}

```http
GET /api/v1/preferences HTTP/1.1
```

사용자가 계정 설정에서 정의한 환경설정입니다.

**반환:** 키와 값으로 구성된 환경설정\
**OAuth:** 사용자 토큰 + `read:accounts`\
**버전 이력:**\
2.8.0 - 추가\
4.1.0 - `reading:autoplay:gifs` 추가\
4.5.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 7) - `posting:default:quoted_policy` 추가

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

```json
{
  "posting:default:visibility": "public",
  "posting:default:sensitive": false,
  "posting:default:language": null,
  "posting:default:quote_policy": "followers",
  "posting:default:spoiler_field": false,
  "reading:expand:media": "default",
  "reading:expand:spoilers": false,
  "reading:autoplay:gifs": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/preferences_controller.rb" caption="app/controllers/api/v1/preferences_controller.rb" >}}
