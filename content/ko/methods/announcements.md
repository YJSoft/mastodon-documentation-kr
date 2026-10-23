---
title: 공지 API 메서드
description: 관리자가 설정한 공지에 관한 메서드입니다.
menu:
  docs:
    name: 공지
    parent: methods-instance
    identifier: methods-announcements
aliases: [
  "/methods/announcements",
  "/api/methods/announcements",
  "/methods/instance/announcements",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 모든 공지 조회 {#get}

```http
GET /api/v1/announcements HTTP/1.1
```

관리자가 설정한 현재 활성 공지를 모두 확인합니다.

**반환:** 배열: [Announcement]({{< relref "entities/announcement">}})\
**OAuth:** 사용자 토큰\
**버전 이력:**\
3.1.0 - 추가

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

현재 활성 공지입니다.

```json
[
  {
    "id": "8",
    "content": "<p>Looks like there was an issue processing audio attachments without embedded art since yesterday due to an experimental new feature. That issue has now been fixed, so you may see older posts with audio from other servers pop up in your feeds now as they are being finally properly processed. Sorry!</p>",
    "starts_at": null,
    "ends_at": null,
    "all_day": false,
    "published_at": "2020-07-03T01:27:38.726Z",
    "updated_at": "2020-07-03T01:27:38.752Z",
    "read": true,
    "mentions": [],
    "statuses": [],
    "tags": [],
    "emojis": [],
    "reactions": [
      {
        "name": "bongoCat",
        "count": 9,
        "me": false,
        "url": "https://files.mastodon.social/custom_emojis/images/000/067/715/original/fdba57dff7576d53.png",
        "static_url": "https://files.mastodon.social/custom_emojis/images/000/067/715/static/fdba57dff7576d53.png"
      },
      {
        "name": "thonking",
        "count": 1,
        "me": false,
        "url": "https://files.mastodon.social/custom_emojis/images/000/098/690/original/a8d36edc4a7032e8.png",
        "static_url": "https://files.mastodon.social/custom_emojis/images/000/098/690/static/a8d36edc4a7032e8.png"
      },
      {
        "name": "AAAAAA",
        "count": 1,
        "me": false,
        "url": "https://files.mastodon.social/custom_emojis/images/000/071/387/original/AAAAAA.png",
        "static_url": "https://files.mastodon.social/custom_emojis/images/000/071/387/static/AAAAAA.png"
      },
      {
        "name": "🤔",
        "count": 1,
        "me": true
      }
    ]
  }
]
```

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 공지 읽음 표시 {#dismiss}

```http
POST /api/v1/announcements/:id/dismiss HTTP/1.1
```

사용자가 공지를 읽음으로 표시할 수 있게 합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:accounts`\
**버전 이력:**\
3.1.0 - 추가

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 데이터베이스의 Announcement ID입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}
```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-1}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found}

지정한 ID의 Announcement가 없습니다.

```json
{
  "error": "Record not found"
}
```

---

## 공지에 반응 추가 {#put-reactions}

```http
PUT /api/v1/announcements/:id/reactions/:name HTTP/1.1
```

이모지로 공지에 반응합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:favourites`\
**버전 이력:**\
3.1.0 - 추가\
5.0.0 - 반응을 비활성화할 수 있으며 이 경우 이 엔드포인트는 400 오류 반환

#### 요청 {#request-2}

##### 경로 매개변수 {#path-parameters-1}

:id
: {{<required>}} 문자열. 데이터베이스의 Announcement ID입니다.

:name
: {{<required>}} 문자열. 유니코드 이모지 또는 사용자 지정 이모지의 단축 코드입니다.

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

```json
{}
```

##### 400: 잘못된 요청 {#400-bad-request}

이 공지에는 반응이 활성화되어 있지 않습니다.

```json
{
  "error": "Emoji reactions are currently not supported on this server"
}
```

##### 401: 인증되지 않음 {#401-unauthorized-2}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-1}

지정한 ID의 Announcement가 없습니다.

```json
{
  "error": "Record not found"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

```json
{
  "error": "Validation failed: Name is not a recognized emoji"
}
```

---

## 공지에서 반응 제거 {#delete-reactions}

```http
DELETE /api/v1/announcements/:id/reactions/:name HTTP/1.1
```

공지에 대한 이모지 반응을 취소합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:favourites`\
**버전 이력:**\
3.1.0 - 추가\
5.0.0 - 반응을 비활성화할 수 있으며 이 경우 이 엔드포인트는 400 오류 반환

#### 요청 {#request-3}

##### 경로 매개변수 {#path-parameters-2}

:id
: {{<required>}} 문자열. 데이터베이스의 Announcement ID입니다.

:name
: {{<required>}} 문자열. 유니코드 이모지 또는 사용자 지정 이모지의 단축 코드입니다.

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-3}
##### 200: 성공 {#200-ok-3}

```json
{}
```

##### 400: 잘못된 요청 {#400-bad-request-1}

이 공지에는 반응이 활성화되어 있지 않습니다.

```json
{
  "error": "Emoji reactions are currently not supported on this server"
}
```

##### 401: 인증되지 않음 {#401-unauthorized-3}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-2}

지정한 ID의 Announcement가 없습니다.

```json
{
  "error": "Record not found"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-1}

```json
{
  "error": "Validation failed: Name is not a recognized emoji"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/announcements_controller.rb" caption="app/controllers/api/v1/announcements_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/announcements/reactions_controller.rb" caption="app/controllers/api/v1/announcements/reactions_controller.rb" >}}
