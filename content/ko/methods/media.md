---
title: 미디어 API 메서드
description: >-
  작성한 게시물에 미디어를 첨부합니다. 크기 및 형식 제한에 관한 자세한 내용은 마스토돈 사용하기 > 프로필에 게시하기 > 첨부 파일을 참고하세요.
menu:
  docs:
    name: 미디어
    parent: methods-statuses
    identifier: methods-media
aliases: [
  "/methods/media",
  "/api/methods/media",
  "/methods/statuses/media",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 미디어를 첨부 파일로 업로드(비동기) {#v2}

```http
POST /api/v2/media HTTP/1.1
```

새 게시물에 사용할 미디어 첨부 파일을 생성합니다. 용량이 큰 업로드는 백그라운드에서 전체 크기 미디어를 비동기적으로 처리합니다.

**반환:** [MediaAttachment]({{< relref "entities/MediaAttachment" >}}), 단 URL은 없음\
**OAuth:** 사용자 토큰 + `write:media`\
**버전 이력:**\
3.1.3 - 추가\
3.2.0 - `thumbnail` 매개변수 추가\
4.0.0 - 작은 미디어 형식(이미지)은 동기적으로 처리하며 202 대신 200 반환. 큰 미디어 형식(동영상, gifv, 오디오)은 계속 비동기적으로 처리하며 202 반환.

#### 요청 {#request}
##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

file
: {{<required>}} 객체. 멀티파트 폼 데이터로 인코딩한 첨부할 파일입니다. 파일에는 MIME 유형이 있어야 합니다.

thumbnail
: 객체. 멀티파트 폼 데이터로 인코딩한 첨부 미디어의 사용자 지정 썸네일입니다.

description
: 문자열. 접근성을 위한 미디어의 일반 텍스트 설명입니다.

focus
: 문자열. 쉼표로 구분한 두 부동소수점 수(x,y)이며 범위는 -1.0부터 1.0까지입니다. 자세한 내용은 [미디어 썸네일 자르기의 초점]({{< relref "api/guidelines#focal-points" >}})을 참고하세요.

#### 응답 {#response}

##### 200: 성공 {#200-ok}

MediaAttachment를 생성했으며 전체 크기 파일을 동기적으로 처리했습니다.

```json
{
  "id": "22348641",
  "type": "image",
  "url": "https://files.mastodon.social/media_attachments/files/022/348/641/original/e96382f26c72a29c.jpeg",
  "preview_url": "https://files.mastodon.social/media_attachments/files/022/348/641/small/e96382f26c72a29c.jpeg",
  "remote_url": null,
  "text_url": "https://mastodon.social/media/4Zj6ewxzzzDi0g8JnZQ",
  "meta": {
    "focus": {
      "x": -0.42,
      "y": 0.69
    },
    "original": {
      "width": 640,
      "height": 480,
      "size": "640x480",
      "aspect": 1.3333333333333333
    },
    "small": {
      "width": 461,
      "height": 346,
      "size": "461x346",
      "aspect": 1.3323699421965318
    }
  },
  "description": "test uploaded via api",
  "blurhash": "UFBWY:8_0Jxv4mx]t8t64.%M-:IUWGWAt6M}"
}
```

##### 202: 접수됨 {#202-accepted}

MediaAttachment를 생성했지만 전체 크기 파일은 아직 처리 중입니다. 미디어를 백그라운드에서 처리 중이므로 MediaAttachment의 `url`은 아직 null입니다. 하지만 `preview_url`은 사용할 수 있습니다. 미디어 첨부 파일 상태를 확인하려면 [`GET /api/v1/media/:id`](#get)를 사용하세요.

```json
{
  "id": "22348641",
  "type": "image",
  "url": null,
  "preview_url": "https://files.mastodon.social/media_attachments/files/022/348/641/small/cebc6d51be03e509.jpeg",
  "remote_url": null,
  "text_url": "https://mastodon.social/media/4Zj6ewxzzzDi0g8JnZQ",
  "meta": {
    "focus": {
      "x": -0.69,
      "y": 0.42
    },
    "original": {
      "width": 640,
      "height": 480,
      "size": "640x480",
      "aspect": 1.3333333333333333
    },
    "small": {
      "width": 461,
      "height": 346,
      "size": "461x346",
      "aspect": 1.3323699421965318
    }
  },
  "description": "test uploaded via api",
  "blurhash": "UFBWY:8_0Jxv4mx]t8t64.%M-:IUWGWAt6M}"
}
```

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

파일 또는 파일 유형이 지원되지 않거나 유효하지 않습니다.

```json
{
  "error": "Validation failed: File content type is invalid, File is invalid"
}
```

##### 500: 서버 오류 {#500-server-error}

첨부 파일의 썸네일을 생성할 수 없습니다.

```json
{
  "error": "Error processing thumbnail for uploaded media"
}
```

---

## 미디어 첨부 파일 가져오기 {#get}

```http
GET /api/v1/media/:id HTTP/1.1
```

처리 대상으로 접수된 이후, 게시물에 첨부하여 게시하기 전에 미디어 첨부 파일을 가져옵니다. 전체 크기 미디어의 처리가 완료되었는지 확인할 때 사용하세요.

**반환:** [MediaAttachment]({{< relref "entities/MediaAttachment" >}})\
**OAuth:** 사용자 토큰 + `write:media`\
**버전 이력:**\
3.1.3 - 추가

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 데이터베이스의 MediaAttachment ID입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

미디어 파일이 처리되었으며 처리된 미디어의 `url`을 사용할 수 있습니다.

```json
{
  "id": "22348641",
  "type": "image",
  "url": "https://files.mastodon.social/media_attachments/files/022/348/641/original/e96382f26c72a29c.jpeg",
  "preview_url": "https://files.mastodon.social/media_attachments/files/022/348/641/small/e96382f26c72a29c.jpeg",
  "remote_url": null,
  "text_url": "https://mastodon.social/media/4Zj6ewxzzzDi0g8JnZQ",
  "meta": {
    "focus": {
      "x": -0.42,
      "y": 0.69
    },
    "original": {
      "width": 640,
      "height": 480,
      "size": "640x480",
      "aspect": 1.3333333333333333
    },
    "small": {
      "width": 461,
      "height": 346,
      "size": "461x346",
      "aspect": 1.3323699421965318
    }
  },
  "description": "test uploaded via api, but updated",
  "blurhash": "UFBWY:8_0Jxv4mx]t8t64.%M-:IUWGWAt6M}"
}
```

##### 206: 부분 콘텐츠 {#206-partial-content}

미디어 첨부 파일을 아직 처리 중입니다.

##### 401: 인증되지 않음 {#401-unauthorized-1}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found}

MediaAttachment가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-1}

미디어 첨부 파일 처리 중 오류가 발생했습니다.


```json
{
  "error": "Validation failed: File content type is invalid, File is invalid"
}
```

---

## 미디어 첨부 파일 삭제 {#delete}

```http
DELETE /api/v1/media/:id
```

현재 게시물에 첨부되지 않은 미디어 첨부 파일을 삭제합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:media`\
**버전 이력:**\
- 4.4.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 4) - 추가

#### 요청 {#request-2}

##### 경로 매개변수 {#path-parameters-1}

:id
: {{<required>}} 문자열. 데이터베이스의 MediaAttachment ID입니다.

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

## 미디어 첨부 파일 수정 {#update}

```http
PUT /api/v1/media/:id HTTP/1.1
```

게시물에 첨부하여 게시하기 전에 MediaAttachment의 매개변수를 수정합니다.

**반환:** [MediaAttachment]({{< relref "entities/MediaAttachment" >}})\
**OAuth:** 사용자 토큰 + `write:media`\
**버전 이력:**\
0.0.0 - 추가\
2.3.0 - `focus` 매개변수 추가\
3.2.0 - `thumbnail` 추가

#### 요청 {#request-3}

##### 경로 매개변수 {#path-parameters-2}

:id
: {{<required>}} 문자열. 데이터베이스의 MediaAttachment ID입니다.

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-1}

thumbnail
: 객체. 멀티파트 폼 데이터로 인코딩한 첨부 미디어의 사용자 지정 썸네일입니다.

description
: 문자열. 접근성을 위한 미디어의 일반 텍스트 설명입니다.

focus
: 문자열. 쉼표로 구분한 두 부동소수점 수(x,y)이며 범위는 -1.0부터 1.0까지입니다. 자세한 내용은 [미디어 썸네일 자르기의 초점]({{< relref "api/guidelines#focal-points" >}})을 참고하세요.

#### 응답 {#response-2}

##### 200: 성공 {#200-ok-2}

`description`을 수정한 첨부 파일입니다.

```json
{
  "id": "22348641",
  "type": "image",
  "url": "https://files.mastodon.social/media_attachments/files/022/348/641/original/e96382f26c72a29c.jpeg",
  "preview_url": "https://files.mastodon.social/media_attachments/files/022/348/641/small/e96382f26c72a29c.jpeg",
  "remote_url": null,
  "text_url": "https://mastodon.social/media/4Zj6ewxzzzDi0g8JnZQ",
  "meta": {
    "focus": {
      "x": -0.42,
      "y": 0.69
    },
    "original": {
      "width": 640,
      "height": 480,
      "size": "640x480",
      "aspect": 1.3333333333333333
    },
    "small": {
      "width": 461,
      "height": 346,
      "size": "461x346",
      "aspect": 1.3323699421965318
    }
  },
  "description": "test uploaded via api, but updated",
  "blurhash": "UFBWY:8_0Jxv4mx]t8t64.%M-:IUWGWAt6M}"
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

첨부 파일이 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-2}

```json
{
  "error": "Validation failed: File content type is invalid, File is invalid"
}
```

---

## 미디어를 첨부 파일로 업로드(v1) {{%deprecated%}} {#v1}

```http
POST /api/v1/media HTTP/1.1
```

새 게시물에 사용할 첨부 파일을 생성합니다. 전체 크기 미디어의 처리가 완료된 후에 반환합니다.

**반환:** [MediaAttachment]({{< relref "entities/MediaAttachment" >}})\
**OAuth:** 사용자 토큰 + `write:media`\
**버전 이력:**\
0.0.0 - 추가\
2.3.0 - `focus` 매개변수 추가\
3.1.3 - [POST /api/v2/media](#v2)를 권장하며 사용 중단 예정. v2는 HTTP 202를 반환하고 반환되는 JSON 객체의 url이 null인 점을 제외하면 모든 면에서 v1과 동일합니다. 썸네일은 동기적으로 준비하지만 미디어 첨부 파일의 전체 버전은 백그라운드에서 처리하기 때문입니다.\
3.2.0 - `thumbnail` 매개변수 추가

#### 요청 {#request-4}
##### 헤더 {#headers-4}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-2}

file
: {{<required>}} 객체. 멀티파트 폼 데이터로 인코딩한 첨부할 파일입니다. 파일에는 MIME 유형이 있어야 합니다.

thumbnail
: 객체. 멀티파트 폼 데이터로 인코딩한 첨부 미디어의 사용자 지정 썸네일입니다.

description
: 문자열. 접근성을 위한 미디어의 일반 텍스트 설명입니다.

focus
: 문자열. 쉼표로 구분한 두 부동소수점 수(x,y)이며 범위는 -1.0부터 1.0까지입니다. 자세한 내용은 [미디어 썸네일 자르기의 초점]({{< relref "api/guidelines#focal-points" >}})을 참고하세요.

#### 응답 {#response-3}
##### 200: 성공 {#200-ok-3}

첨부 파일을 생성했습니다. 처리 실패로 파일을 올바르게 이해하지 못했더라도 MediaAttachment는 생성됩니다.

올바른 파일의 응답 예:

```json
{
  "id": "22348641",
  "type": "image",
  "url": "https://files.mastodon.social/media_attachments/files/022/348/641/original/cebc6d51be03e509.jpeg",
  "preview_url": "https://files.mastodon.social/media_attachments/files/022/348/641/small/cebc6d51be03e509.jpeg",
  "remote_url": null,
  "text_url": "https://mastodon.social/media/4Zj6ewxzzzDi0g8JnZQ",
  "meta": {
    "focus": {
      "x": -0.69,
      "y": 0.42
    },
    "original": {
      "width": 640,
      "height": 480,
      "size": "640x480",
      "aspect": 1.3333333333333333
    },
    "small": {
      "width": 461,
      "height": 346,
      "size": "461x346",
      "aspect": 1.3323699421965318
    }
  },
  "description": "test uploaded via api",
  "blurhash": "UFBWY:8_0Jxv4mx]t8t64.%M-:IUWGWAt6M}"
}
```

잘못된 파일로 인해 url이 "missing"인 응답 예:

```json
{
  "id": "22348456",
  "type": "unknown",
  "url": "https://mastodon.social/files/original/missing.png",
  "preview_url": "https://mastodon.social/files/small/missing.png",
  "remote_url": null,
  "text_url": "https://mastodon.social/media/Ao2nvQoQNHROpKgEyoA",
  "meta": {
    "focus": {
      "x": -0.69,
      "y": 0.42
    }
  },
  "description": "test uploaded via api",
  "blurhash": null
}
```

##### 401: 인증되지 않음 {#401-unauthorized-3}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-3}

파일 또는 파일 유형이 지원되지 않거나 유효하지 않습니다.

```json
{
  "error": "Validation failed: File content type is invalid, File is invalid"
}
```

---

## 함께 보기 {#see-also}

{{< page-relref ref="methods/instance" caption="GET /api/v2/instance (for obtaining configuration limits)">}}

{{< page-relref ref="entities/instance#media_attachments" caption="Instance#configuration[media_attachments]">}}

{{< page-relref ref="api/guidelines#focal-points" caption="미디어 썸네일 자르기의 초점" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/media_controller.rb" caption="app/controllers/api/v1/media_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v2/media_controller.rb" caption="app/controllers/api/v2/media_controller.rb" >}}
