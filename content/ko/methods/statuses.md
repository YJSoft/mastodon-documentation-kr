---
title: 게시물 API 메서드
description: 게시물을 게시하고 상호작용하며 정보를 조회합니다.
menu:
  docs:
    name: 게시물
    parent: methods
    identifier: methods-statuses
aliases: [
  "/methods/statuses",
  "/api/methods/statuses",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 새 게시물 작성 {#create}

```http
POST /api/v1/statuses HTTP/1.1
```

지정한 매개변수로 게시물을 게시합니다.

**반환:** [Status]({{<relref "entities/status">}}). `scheduled_at`이 있으면 대신 [ScheduledStatus]({{<relref "entities/scheduledstatus">}}) 반환.\
**OAuth:** 사용자 + `write:statuses`\
**버전 이력:**\
0.0.0 - 추가\
2.7.0 - `scheduled_at` 추가\
2.8.0 - `poll` 추가\
4.5.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 7) - `quoted_status_id` 및 `quote_approval_policy` 추가

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

Idempotency-Key
: 같은 게시물의 중복 제출을 방지하려면 이 헤더에 임의의 문자열을 제공하세요. 클라이언트 측에서 생성한 해시나 UUID 사용을 고려하세요. 멱등성 키는 최대 1시간 동안 저장됩니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

status
: {{<required>}} 문자열. 게시물의 텍스트 내용입니다. `media_ids`를 제공하면 선택 사항입니다. `status`를 제공하는 경우 `poll` 첨부는 선택 사항입니다.

media_ids[]
: {{<required>}} 문자열 배열. 미디어로 첨부할 Attachment ID를 포함합니다. 제공하면 `status`는 선택 사항이 되고 `poll`을 사용할 수 없습니다.

poll[options][]
: {{<required>}} 문자열 배열. 투표의 가능한 답변입니다. 제공하면 `media_ids`를 사용할 수 없고 `poll[expires_in]`을 제공해야 합니다.

poll[expires_in]
: {{<required>}} 정수. 투표를 열어둘 시간(초)입니다. 제공하면 `media_ids`를 사용할 수 없고 `poll[options]`를 제공해야 합니다.

poll[multiple]
: 불리언. 복수 선택을 허용할지 여부입니다. 기본값은 false입니다.

poll[hide_totals]
: 불리언. 투표가 끝날 때까지 투표수를 숨길지 여부입니다. 기본값은 false입니다.

in_reply_to_id
: 문자열. 답글인 경우 답글을 달 대상 게시물의 ID입니다.

sensitive
: 불리언. 게시물과 첨부 미디어를 민감한 콘텐츠로 표시할지 여부입니다. 기본값은 false입니다.

spoiler_text
: 문자열. 실제 내용 앞에 경고 또는 제목으로 표시할 텍스트입니다. 일반적으로 게시물은 이 필드 뒤에 접혀 표시됩니다.

visibility
: 문자열. 게시물의 공개 범위를 `public`, `unlisted`, `private`, `direct`로 설정합니다.

language
: 문자열. 이 게시물의 ISO 639-1 언어 코드입니다.

scheduled_at
: 문자열. 게시물을 예약할 [날짜와 시간](/api/datetime-format#datetime)입니다. 이 매개변수를 제공하면 Status 대신 ScheduledStatus를 반환합니다. 적어도 5분 이후여야 합니다.

quoted_status_id
: 문자열. 인용할 게시물이 있는 경우 해당 ID입니다. 게시물이 없거나, 작성자에게 접근 권한이 없거나, 마스토돈이 해석한 첨부 인용 정책상 인용이 금지되면 오류가 발생합니다. 개인 멘션(`direct` 공개 범위)을 제외한 모든 게시물은 작성자가 인용할 수 있습니다. `private` 게시물을 인용하면 인용 게시물의 `visibility`가 `private` 또는 `direct`로 제한됩니다(지정한 `visibility`가 `public` 또는 `unlisted`이면 대신 `private`을 사용). `direct` 공개 범위로 인용 게시물을 작성하면서 인용 대상의 작성자를 명시적으로 멘션하지 않으면 오류를 반환합니다. `status` 텍스트에 인용 대상 게시물 링크가 없으면 마스토돈은 이전 버전과의 호환성을 위해 `<p class="quote-inline">RE: <a href="…">…</a></p>` 문단을 앞에 추가합니다(마스토돈 웹 인터페이스에서는 이 문단을 숨깁니다).

quote_approval_policy
: 문자열(열거형 중 하나). 게시물을 인용할 수 있는 사람을 설정합니다. 생략하면 사용자의 [기본 설정](/entities/Account#source-quote_policy)을 사용합니다. `visibility`가 `private` 또는 `direct`이면 무시되며 이 경우 정책은 항상 `nobody`로 설정됩니다.\
`public` = 차단되지 않았다면 누구나 이 게시물을 인용할 수 있으며 인용을 자동 수락합니다.\
`followers` = 팔로워와 작성자만 이 게시물을 인용할 수 있으며 인용을 자동 수락합니다.\
`nobody` = 작성자만 게시물을 인용할 수 있습니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

선택한 매개변수로 게시물을 게시합니다.

```json
{
  "id": "103254962155278888",
  "created_at": "2019-12-05T11:34:47.196Z",
  // ...
  "content": "<p>test content</p>",
  // ...
  "application": {
    "name": "test app",
    "website": null
  },
  // ...
}
```

scheduled_at을 제공하면 대신 ScheduledStatus를 반환합니다.

```json
{
  "id": "3221",
  "scheduled_at": "2019-12-05T12:33:01.000Z",
  "params": {
    "text": "test content",
    "media_ids": null,
    "sensitive": null,
    "spoiler_text": null,
    "visibility": null,
    "scheduled_at": null,
    "poll": null,
    "idempotency": null,
    "in_reply_to_id": null,
    "application_id": 596551,
    "quoted_status_id": null,
    "quote_approval_policy": "followers"
  },
  "media_attachments": []
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

```json
{
  "error": "Validation failed: Text can't be blank"
}
```

---

## 게시물 하나 조회 {#get}

```http
GET /api/v1/statuses/:id HTTP/1.1
```

게시물 정보를 가져옵니다.

**반환:** [Status]({{< relref "entities/status" >}})\
**OAuth:** 공개 게시물은 공개, 비공개 게시물은 사용자 토큰 + `read:statuses`\
**버전 이력:**\
0.0.0 - 추가\
2.7.0 - 공개 게시물에 더 이상 토큰이 필요하지 않음

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-1}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

```json
{
  "id": "1",
  "created_at": "2016-03-16T14:44:31.580Z",
  "in_reply_to_id": null,
  "in_reply_to_account_id": null,
  "sensitive": false,
  "spoiler_text": "",
  "visibility": "public",
  "language": "en",
  "uri": "https://mastodon.social/users/Gargron/statuses/1",
  "url": "https://mastodon.social/@Gargron/1",
  "replies_count": 7,
  "reblogs_count": 98,
  "favourites_count": 112,
  "favourited": false,
  "reblogged": false,
  "muted": false,
  "bookmarked": false,
  "content": "<p>Hello world</p>",
  "reblog": null,
  "application": null,
  "account": {
    "id": "1",
    "username": "Gargron",
    "acct": "Gargron",
    "display_name": "Eugen",
    "locked": false,
    "bot": false,
    "created_at": "2016-03-16T14:34:26.392Z",
    "note": "<p>Developer of Mastodon and administrator of mastodon.social. I post service announcements, development updates, and personal stuff.</p>",
    "url": "https://mastodon.social/@Gargron",
    "avatar": "https://files.mastodon.social/accounts/avatars/000/000/001/original/d96d39a0abb45b92.jpg",
    "avatar_static": "https://files.mastodon.social/accounts/avatars/000/000/001/original/d96d39a0abb45b92.jpg",
    "header": "https://files.mastodon.social/accounts/headers/000/000/001/original/c91b871f294ea63e.png",
    "header_static": "https://files.mastodon.social/accounts/headers/000/000/001/original/c91b871f294ea63e.png",
    "followers_count": 320472,
    "following_count": 453,
    "statuses_count": 61163,
    "last_status_at": "2019-12-05T03:03:02.595Z",
    "emojis": [],
    "fields": [
      {
        "name": "Patreon",
        "value": "<a href=\"https://www.patreon.com/mastodon\" rel=\"me nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://www.</span><span class=\"\">patreon.com/mastodon</span><span class=\"invisible\"></span></a>",
        "verified_at": null
      },
      {
        "name": "Homepage",
        "value": "<a href=\"https://zeonfederated.com\" rel=\"me nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"\">zeonfederated.com</span><span class=\"invisible\"></span></a>",
        "verified_at": "2019-07-15T18:29:57.191+00:00"
      }
    ]
  },
  "media_attachments": [],
  "mentions": [],
  "tags": [],
  "emojis": [],
  "card": null,
  "poll": null
}
```

##### 401: 인증되지 않음 {#401-unauthorized-1}

서버가 인증된 가져오기 모드입니다.

```json
{
  "error": "This API requires an authenticated user"
}
```

##### 404: 찾을 수 없음 {#404-not-found}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

---

## 여러 게시물 조회 {#index}

```http
GET /api/v1/statuses HTTP/1.1
```

여러 게시물의 정보를 가져옵니다.

**반환:** 배열: [Status]({{< relref "entities/status" >}})\
**OAuth:** 공개 게시물은 공개, 비공개 게시물은 사용자 토큰 + `read:statuses`\
**버전 이력:**\
4.3.0 - 추가

#### 요청 {#request-2}

##### 쿼리 매개변수 {#query-parameters}

id[]
: 문자열 배열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-2}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

요청한 게시물의 [Status]({{< relref "entities/status" >}}) 레코드를 반환합니다. 요청한 게시물이 없거나 현재 자격 증명으로 접근할 수 없으면 요청한 수보다 적은 레코드가 반환될 수 있습니다.
`id=2`인 게시물이 없을 때 `id[]=1&id[]=2`를 사용한 호출 예:

```json
[
  {
    "id": "1",
    "created_at": "2016-03-16T14:44:31.580Z",
    "in_reply_to_id": null,
    "in_reply_to_account_id": null,
    "sensitive": false,
    "spoiler_text": "",
    "visibility": "public",
    "language": "en",
    "uri": "https://mastodon.social/users/Gargron/statuses/1",
    "url": "https://mastodon.social/@Gargron/1",
    "replies_count": 7,
    "reblogs_count": 98,
    "favourites_count": 112,
    "favourited": false,
    "reblogged": false,
    "muted": false,
    "bookmarked": false,
    "content": "<p>Hello world</p>",
    "reblog": null,
    "application": null,
    "account": {
      "id": "1",
      "username": "Gargron",
      "acct": "Gargron",
      "display_name": "Eugen",
      "locked": false,
      "bot": false,
      "created_at": "2016-03-16T14:34:26.392Z",
      "note": "<p>Developer of Mastodon and administrator of mastodon.social. I post service announcements, development updates, and personal stuff.</p>",
      "url": "https://mastodon.social/@Gargron",
      "avatar": "https://files.mastodon.social/accounts/avatars/000/000/001/original/d96d39a0abb45b92.jpg",
      "avatar_static": "https://files.mastodon.social/accounts/avatars/000/000/001/original/d96d39a0abb45b92.jpg",
      "header": "https://files.mastodon.social/accounts/headers/000/000/001/original/c91b871f294ea63e.png",
      "header_static": "https://files.mastodon.social/accounts/headers/000/000/001/original/c91b871f294ea63e.png",
      "followers_count": 320472,
      "following_count": 453,
      "statuses_count": 61163,
      "last_status_at": "2019-12-05T03:03:02.595Z",
      "emojis": [],
      "fields": [
        {
          "name": "Patreon",
          "value": "<a href=\"https://www.patreon.com/mastodon\" rel=\"me nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://www.</span><span class=\"\">patreon.com/mastodon</span><span class=\"invisible\"></span></a>",
          "verified_at": null
        },
        {
          "name": "Homepage",
          "value": "<a href=\"https://zeonfederated.com\" rel=\"me nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"\">zeonfederated.com</span><span class=\"invisible\"></span></a>",
          "verified_at": "2019-07-15T18:29:57.191+00:00"
        }
      ]
    },
    "media_attachments": [],
    "mentions": [],
    "tags": [],
    "emojis": [],
    "card": null,
    "poll": null
  }
]
```

##### 401: 인증되지 않음 {#401-unauthorized-2}

서버가 인증된 가져오기 모드입니다.

```json
{
  "error": "This API requires an authenticated user"
}
```

---

## 게시물 삭제 {#delete}

```http
DELETE /api/v1/statuses/:id HTTP/1.1
```

내 게시물 하나를 삭제합니다.

**반환:** 원본 `text` 및 `poll` 또는 `media_attachments`를 포함하는 [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `write:statuses`\
**버전 이력:**\
0.0.0 - 추가\
2.9.0 - 삭제 후 다시 작성에 사용할 원본 속성 반환\
4.4.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 4) - 선택적 매개변수 `delete_media` 추가

#### 요청 {#request-3}

##### 쿼리 매개변수 {#query-parameters-1}

delete_media
: 불리언. 게시물의 미디어 첨부 파일을 즉시 삭제할지 여부입니다. 생략하거나 `false`이면 새 게시물에서 재사용할 수 있도록 약 24시간 동안 보관할 수 있습니다.

##### 경로 매개변수 {#path-parameters-1}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-3}
##### 200: 성공 {#200-ok-3}

삭제 후 다시 작성 기능 등에서 게시물을 다시 게시하는 데 사용할 수 있는 특수 속성 `text` 및 `poll` 또는 `media_attachments`에 주목하세요. [POST /api/v1/statuses](#create)에서 `text`를 `status` 매개변수 값으로, `media_attachments[n]["id"]`를 `media_ids` 배열 매개변수로, `poll` 속성을 해당 매개변수(예: `poll[multiple]`, `poll[options]`)로 사용하고, 사용자 입력에 따른 새 `poll[expires_in]` 및 `poll[hide_totals]`를 사용하세요.

미디어 게시물 삭제 예:

```json
{
  "id": "103254193998341330",
  "created_at": "2019-12-05T08:19:26.052Z",
  "in_reply_to_id": null,
  "in_reply_to_account_id": null,
  "sensitive": false,
  "spoiler_text": "",
  "visibility": "public",
  "language": "en",
  "uri": "https://mastodon.social/users/trwnh/statuses/103254193998341330",
  "url": "https://mastodon.social/@trwnh/103254193998341330",
  "replies_count": 0,
  "reblogs_count": 0,
  "favourites_count": 0,
  "favourited": false,
  "reblogged": false,
  "muted": false,
  "bookmarked": false,
  "pinned": false,
  "text": "test",
  "reblog": null,
  "application": {
    "name": "Web",
    "website": null
  },
  "account": {
    "id": "14715",
    "username": "trwnh",
    "acct": "trwnh",
    "display_name": "infinite love ⴳ",
    // ...
  },
  "media_attachments": [
    {
      "id": "22345792",
      "type": "image",
      "url": "https://files.mastodon.social/media_attachments/files/022/345/792/original/57859aede991da25.jpeg",
      "preview_url": "https://files.mastodon.social/media_attachments/files/022/345/792/small/57859aede991da25.jpeg",
      "remote_url": null,
      "text_url": "https://mastodon.social/media/2N4uvkuUtPVrkZGysms",
      "meta": {
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
        },
        "focus": {
          "x": -0.27,
          "y": 0.51
        }
      },
      "description": "test media description",
      "blurhash": "UFBWY:8_0Jxv4mx]t8t64.%M-:IUWGWAt6M}"
    }
  ],
  "mentions": [],
  "tags": [],
  "emojis": [],
  "card": null,
  "poll": null
}
```

투표 삭제 예:

```json
{
  "id": "103254222827484720",
  "created_at": "2019-12-05T08:26:45.958Z",
  "in_reply_to_id": null,
  "in_reply_to_account_id": null,
  "sensitive": false,
  "spoiler_text": "",
  "visibility": "public",
  "language": "en",
  "uri": "https://mastodon.social/users/trwnh/statuses/103254222827484720",
  "url": "https://mastodon.social/@trwnh/103254222827484720",
  "replies_count": 0,
  "reblogs_count": 0,
  "favourites_count": 0,
  "favourited": false,
  "reblogged": false,
  "muted": false,
  "bookmarked": false,
  "pinned": false,
  "text": "test",
  "reblog": null,
  "application": {
    "name": "Web",
    "website": null
  },
  "account": {
    "id": "14715",
    "username": "trwnh",
    "acct": "trwnh",
    "display_name": "infinite love ⴳ",
    // ...
  },
  "media_attachments": [],
  "mentions": [],
  "tags": [],
  "emojis": [],
  "card": null,
  "poll": {
    "id": "34858",
    "expires_at": "2019-12-06T08:26:45.945Z",
    "expired": false,
    "multiple": false,
    "votes_count": 1,
    "voters_count": 1,
    "voted": true,
    "own_votes": [],
    "options": [
      {
        "title": "test 1",
        "votes_count": 1
      },
      {
        "title": "test 2",
        "votes_count": 0
      }
    ],
    "emojis": []
  }
}
```

##### 401: 인증되지 않음 {#401-unauthorized-3}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-1}

Status가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

## 문맥의 상위 및 하위 게시물 가져오기 {#context}

```http
GET /api/v1/statuses/:id/context HTTP/1.1
```

글타래에서 이 게시물 위아래의 게시물을 조회합니다.

마스토돈 4.5부터 이 엔드포인트를 조회하면 누락된 답글이 있는지 확인하고 가능하면 가져오는 비동기 백그라운드 작업이 시작될 수 있습니다. 이 경우 새 실험적 헤더 `Mastodon-Async-Refresh`가 응답에 추가될 수 있습니다. 자세한 설명은 [AsyncRefreshes]({{< relref "methods/async_refreshes" >}})를 참고하세요.

**반환:** [Context]({{< relref "entities/context" >}})\
**OAuth:** 공개 게시물은 상위 40개와 하위 60개, 최대 깊이 20까지 공개. 사용자 토큰 + `read:statuses`는 상위 4,096개와 하위 4,096개, 무제한 깊이 및 비공개 게시물 지원.\
**버전 이력:**\
0.0.0 - 추가\
4.0.0 - 인증되지 않은 요청 제한\
4.5.0 - 실험적 `Mastodon-Async-Refresh` 헤더 추가

#### 요청 {#request-4}

##### 경로 매개변수 {#path-parameters-2}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-4}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-4}
##### 200: 성공 {#200-ok-4}

```json
{
  "ancestors": [
    {
      "id": "103188938570975982",
      "created_at": "2019-11-23T19:44:00.124Z",
      "in_reply_to_id": null,
      "in_reply_to_account_id": null,
      // ...
    },
    {
      "id": "103188971072973252",
      "created_at": "2019-11-23T19:52:23.398Z",
      "in_reply_to_id": "103188938570975982",
      "in_reply_to_account_id": "634458",
      // ...
    },
    {
      "id": "103188982235527758",
      "created_at": "2019-11-23T19:55:08.208Z",
      "in_reply_to_id": "103188971072973252",
      "in_reply_to_account_id": "14715",
      // ...
    }
  ],
  "descendants": [
    {
      "id": "103189026958574542",
      "created_at": "2019-11-23T20:06:36.011Z",
      "in_reply_to_id": "103189005915505698",
      "in_reply_to_account_id": "634458",
      // ...
    }
  ]
}
```

##### 404: 찾을 수 없음 {#404-not-found-2}

게시물이 비공개이거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

## 게시물 번역 {#translate}

```http
POST /api/v1/statuses/:id/translate HTTP/1.1
```

게시물 내용을 특정 언어로 번역합니다. 공개 또는 조용한 공개 범위의 게시물만 번역할 수 있습니다.

**반환:** [Translation]({{< relref "entities/translation" >}})\
**OAuth:** 앱 토큰 + `read:statuses`\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-5}

##### 경로 매개변수 {#path-parameters-3}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 폼 데이터 매개변수 {#form-data-parameters-1}

lang
: 문자열(ISO 639-1 언어 코드). 게시물 내용을 이 언어로 번역합니다. 기본값은 사용자의 현재 로캘이며 로캘이 없으면 서버 기본값을 사용합니다.

##### 헤더 {#headers-5}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-5}

##### 200: 성공 {#200-ok-5}

콘텐츠 경고와 미디어가 있는 스페인어 게시물을 영어로 번역합니다.

```json
{
  "content": "<p>Hello world</p>",
  "spoiler_text": "Greatings ahead",
  "media_attachments": [
    {
      "id": 22345792,
      "description": "Status author waving at the camera"
    }
  ],
  "poll": null,
  "detected_source_language": "es",
  "provider": "DeepL.com"
}
```

투표가 있는 게시물을 영어로 번역합니다.

```json
{
  "content": "<p>Should I stay or should I go?</p>",
  "spoiler_text": null,
  "media_attachments": [],
  "poll": [
    {
      "id": 34858,
      "options": [
        {
          "title": "Stay"
        },
        {
          "title": "Go"
        }
      ]
    }
  ],
  "detected_source_language": "ja",
  "provider": "DeepL.com"
}
```

##### 404: 찾을 수 없음 {#404-not-found-3}

게시물이 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

##### 403: 금지됨 {#403-forbidden}

게시물에 다음 중 하나가 해당합니다.

- 공개 범위가 private 또는 direct
- 설정된 백엔드에서 대상 `lang`으로 번역할 수 없는 `language` 속성. 지원하지 않는 "동일 언어" 번역(예: `en`->`en`) 시도도 포함될 수 있습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 503: 서비스 이용 불가 {#503-service-unavailable}

번역 요청이 실패했습니다.

```json
{
  "error": "Service Unavailable"
}
```

---

## 게시물을 부스트한 사람 확인 {#reblogged_by}

```http
GET /api/v1/statuses/:id/reblogged_by HTTP/1.1
```

지정한 게시물을 부스트한 사람을 조회합니다.

**반환:** 배열: [Account]({{< relref "entities/account" >}})\
**OAuth:** 공개 게시물은 공개. 비공개 게시물은 사용자 토큰 + `read:statuses`.\
**버전 이력:**\
0.0.0 - 추가

#### 요청 {#request-6}

##### 경로 매개변수 {#path-parameters-4}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-6}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-2}

max_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

since_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 계정 40개이며 최대 80개입니다.

#### 응답 {#response-6}
##### 200: 성공 {#200-ok-6}

게시물을 부스트한 계정 목록입니다.

```json
[
  {
    "id": "711345",
    "username": "Norman_Doors",
    "acct": "Norman_Doors@witches.live",
    // ...
  },
  // ...
]
```

부스트한 Status ID는 일반적으로 미리 알 수 없으므로 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <https://mastodon.example/api/v1/statuses/109404970108594430/reblogged_by?limit=2&max_id=109406336446186031>; rel="next", <https://mastodon.example/api/v1/statuses/109404970108594430/reblogged_by?limit=2&since_id=109408462939099398>; rel="prev"
```

##### 404: 찾을 수 없음 {#404-not-found-4}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

---

## 게시물의 인용 확인 {#quotes}

```http
GET /api/v1/statuses/:id/quotes HTTP/1.1
```

게시물의 인용을 조회합니다.

**반환:** 배열: [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `read:statuses`.\
**버전 이력:**\
4.5.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 7) - 추가

#### 요청 {#request-7}

##### 경로 매개변수 {#path-parameters-5}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-7}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-3}

max_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

since_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 게시물 20개이며 최대 40개입니다.

#### 응답 {#response-7}
##### 200: 성공 {#200-ok-7}

요청한 게시물을 인용한 게시물 목록입니다.

```json
[
  {
    "id": "115107232286434584",
    "created_at": "2025-08-28T16:02:57.029Z",
    "quote": {
      "state": "accepted",
      "quoted_status": {
        "id":"115107231366664709",
        // ...
      },
    },
    // ...
  },
  {
    "id": "115107231976600838",
    "created_at": "2025-08-28T16:02:52.302Z",
    "quote": {
      "state": "accepted",
      "quoted_status": {
        "id":"115107231366664709",
        // ...
      },
    },
    // ...
  },
  // ...
]
```

인용한 Status ID는 일반적으로 미리 알 수 없으므로 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <https://mastodon.example/api/v1/statuses/109404970108594430/quotes?limit=2&max_id=109406336446186031>; rel="next", <https://mastodon.example/api/v1/statuses/109404970108594430/quotes?limit=2&since_id=109408462939099398>; rel="prev"
```

##### 404: 찾을 수 없음 {#404-not-found-5}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

##### 401: 인증되지 않음 {#401-unauthorized-4}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 게시물에 좋아요한 사람 확인 {#favourited_by}

```http
GET /api/v1/statuses/:id/favourited_by HTTP/1.1
```

지정한 게시물에 좋아요한 사람을 조회합니다.

**반환:** 배열: [Account]({{< relref "entities/account" >}})\
**OAuth:** 공개 게시물은 공개. 비공개 게시물은 사용자 토큰 + `read:statuses`.\
**버전 이력:**\
0.0.0 - 추가

#### 요청 {#request-8}

##### 경로 매개변수 {#path-parameters-6}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-8}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-4}

max_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

since_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 계정 40개이며 최대 80개입니다.

#### 응답 {#response-8}
##### 200: 성공 {#200-ok-8}

게시물에 좋아요한 계정 목록입니다.

```json
[
  {
    "id": "828600",
    "username": "fructose_dealer",
    "acct": "fructose_dealer@radical.town",
    // ...
  },
  // ...
]
```

Favourite ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <https://mastodon.example/api/v1/statuses/109419880690343548/favourited_by?limit=1&max_id=53286827>; rel="next", <https://mastodon.example/api/v1/statuses/109419880690343548/favourited_by?limit=1&since_id=53286827>; rel="prev"
```

##### 404: 찾을 수 없음 {#404-not-found-6}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

---

## 게시물 좋아요 {#favourite}

```http
POST /api/v1/statuses/:id/favourite HTTP/1.1
```

좋아요 목록에 게시물을 추가합니다.

**반환:** [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `write:favourites`\
**버전 이력:**\
0.0.0 - 추가

#### 요청 {#request-9}

##### 경로 매개변수 {#path-parameters-7}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-9}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-9}
##### 200: 성공 {#200-ok-9}

게시물에 좋아요했거나 이미 좋아요한 상태입니다.

```json
{
  "id": "99734435964706331",
  "created_at": "2018-03-23T17:38:40.700Z",
  // ...
  "favourited": true,
  "reblogged": false,
  "muted": false,
  "bookmarked": false,
  "pinned": false,
  // ...
}
```

##### 401: 인증되지 않음 {#401-unauthorized-5}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-7}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

---

## 게시물 좋아요 취소 {#unfavourite}

```http
POST /api/v1/statuses/:id/unfavourite HTTP/1.1
```

좋아요 목록에서 게시물을 제거합니다.

**반환:** [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `write:favourites`\
**버전 이력:**\
0.0.0 - 추가

#### 요청 {#request-10}

##### 경로 매개변수 {#path-parameters-8}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-10}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-10}
##### 200: 성공 {#200-ok-10}

게시물의 좋아요를 취소했거나 이미 좋아요하지 않은 상태입니다.

```json
{
  "id": "99734435964706331",
  "created_at": "2018-03-23T17:38:40.700Z",
  // ...
  "favourited": false,
  "reblogged": false,
  "muted": false,
  "bookmarked": false,
  "pinned": false,
  // ...
}
```

##### 401: 인증되지 않음 {#401-unauthorized-6}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-8}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

---

## 게시물 부스트 {#boost}

```http
POST /api/v1/statuses/:id/reblog HTTP/1.1
```

내 프로필에 게시물을 다시 공유합니다.

**반환:** [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `write:statuses`\
**버전 이력:**\
0.0.0 - 추가\
2.8.0 - `visibility` 매개변수 추가

#### 요청 {#request-11}

##### 경로 매개변수 {#path-parameters-9}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-11}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-2}

visibility
: 문자열(열거형, `public`, `unlisted`, `private` 중 하나). 기본값은 public입니다.

#### 응답 {#response-11}
##### 200: 성공 {#200-ok-11}

게시물을 부스트했습니다. 최상위 id가 바뀌었으며 부스트한 게시물의 id는 이제 `reblog` 속성 안에 있습니다. 최상위 id는 부스트 자체의 id입니다. 또한 부스트는 고정할 수 없습니다.

```json
{
  "id": "103254401326800919",
  "created_at": "2019-12-05T09:12:09.625Z",
  // ...
  "favourited": false,
  "reblogged": true,
  "muted": false,
  "bookmarked": false,
  // ...
  "reblog": {
    "id": "99734435964706331",
    "created_at": "2018-03-23T17:38:40.700Z",
    // ...
    "favourited": false,
    "reblogged": true,
    "muted": false,
    "bookmarked": false,
    "pinned": false,
    // ...
  },
  // ...
}
```

##### 401: 인증되지 않음 {#401-unauthorized-7}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-9}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

---

## 게시물 부스트 취소 {#unreblog}

```http
POST /api/v1/statuses/:id/unreblog HTTP/1.1
```

게시물의 재공유를 취소합니다.

**반환:** [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `write:statuses`\
**버전 이력:**\
0.0.0 - 추가

#### 요청 {#request-12}

##### 경로 매개변수 {#path-parameters-10}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-12}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-12}
##### 200: 성공 {#200-ok-12}

게시물 부스트를 취소했거나 이미 부스트하지 않은 상태입니다.

```json
{
  "id": "99734435964706331",
  "created_at": "2018-03-23T17:38:40.700Z",
  // ...
  "favourited": false,
  "reblogged": false,
  "muted": false,
  "bookmarked": false,
  "pinned": false,
  // ...
}
```

##### 401: 인증되지 않음 {#401-unauthorized-8}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-10}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

---

## 게시물 북마크 {#bookmark}

```http
POST /api/v1/statuses/:id/bookmark HTTP/1.1
```

게시물을 비공개로 북마크합니다.

**반환:** [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `write:bookmarks`\
**버전 이력:**\
3.1.0 - 추가

#### 요청 {#request-13}

##### 경로 매개변수 {#path-parameters-11}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-13}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-13}
##### 200: 성공 {#200-ok-13}

게시물을 북마크했거나 이미 북마크한 상태입니다.

```json
{
  "id": "99734435964706331",
  "created_at": "2018-03-23T17:38:40.700Z",
  // ...
  "favourited": false,
  "reblogged": false,
  "muted": false,
  "bookmarked": true,
  "pinned": false,
  // ...
}
```

##### 401: 인증되지 않음 {#401-unauthorized-9}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 게시물 북마크 취소 {#unbookmark}

```http
POST /api/v1/statuses/:id/unbookmark HTTP/1.1
```

비공개 북마크에서 게시물을 제거합니다.

**반환:** [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `write:bookmarks`\
**버전 이력:**\
3.1.0 - 추가

#### 요청 {#request-14}

##### 경로 매개변수 {#path-parameters-12}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-14}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-14}
##### 200: 성공 {#200-ok-14}

게시물 북마크를 취소했거나 이미 북마크하지 않은 상태입니다.

```json
{
  "id": "99734435964706331",
  "created_at": "2018-03-23T17:38:40.700Z",
  // ...
  "favourited": false,
  "reblogged": false,
  "muted": false,
  "bookmarked": false,
  "pinned": false,
  // ...
}
```

##### 401: 인증되지 않음 {#401-unauthorized-10}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-11}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

---

## 인용 게시물 철회 {#revoke_quote}

```http
POST /api/v1/statuses/:id/quotes/:quoting_status_id/revoke HTTP/1.1
```

게시물 `quoting_status_id`의 인용 인가를 철회하여 게시물 `id`를 분리합니다.

**반환:** [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `write:statuses`. 사용자 토큰은 게시물 `id`의 작성자 소유여야 합니다.\
**버전 이력:**\
4.5.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 7) - 추가

#### 요청 {#request-15}

##### 경로 매개변수 {#path-parameters-13}

:id
: {{<required>}} 문자열. 데이터베이스의 인용 대상 Status ID입니다.

:quoting_status_id
: {{<required>}} 문자열. 데이터베이스의 인용하는 Status ID입니다.

##### 헤더 {#headers-15}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-15}
##### 200: 성공 {#200-ok-15}

인용이 철회된 수정된 Status입니다.

```json
{
  "id": "115107232286434584",
  "created_at": "2025-08-28T16:02:57.029Z",
  "quote": {
    "state": "revoked",
    "quoted_status": null,
  },
  // ...
}
```

##### 404: 찾을 수 없음 {#404-not-found-12}

게시물이 없거나 비공개이거나 해당 인용이 없습니다.

```json
{
  "error": "Record not found"
}
```

##### 403: 금지됨 {#403-forbidden-1}

Status가 요청한 사용자의 소유가 아닙니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 401: 인증되지 않음 {#401-unauthorized-11}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 대화 뮤트 {#mute}

```http
POST /api/v1/statuses/:id/mute HTTP/1.1
```

이 게시물이 속한 글타래의 알림을 받지 않습니다. 내가 참여한 글타래여야 합니다.

**반환:** [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `write:mutes`\
**버전 이력:**\
1.4.2 - 추가

#### 요청 {#request-16}

##### 경로 매개변수 {#path-parameters-14}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-16}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-16}
##### 200: 성공 {#200-ok-16}

게시물의 대화를 뮤트했거나 이미 뮤트한 상태입니다.

```json
{
  "id": "99734435964706331",
  "created_at": "2018-03-23T17:38:40.700Z",
  // ...
  "favourited": false,
  "reblogged": false,
  "muted": true,
  "bookmarked": false,
  "pinned": false,
  // ...
}
```

##### 401: 인증되지 않음 {#401-unauthorized-12}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-13}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

---

## 대화 뮤트 해제 {#unmute}

```http
POST /api/v1/statuses/:id/unmute HTTP/1.1
```

이 게시물이 속한 글타래의 알림을 다시 받기 시작합니다.

**반환:** [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `write:mutes`\
**버전 이력:**\
1.4.2 - 추가

#### 요청 {#request-17}

##### 경로 매개변수 {#path-parameters-15}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-17}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-17}
##### 200: 성공 {#200-ok-17}

게시물의 대화 뮤트를 해제했거나 이미 뮤트하지 않은 상태입니다.

```json
{
  "id": "99734435964706331",
  "created_at": "2018-03-23T17:38:40.700Z",
  // ...
  "favourited": false,
  "reblogged": false,
  "muted": false,
  "bookmarked": false,
  "pinned": false,
  // ...
}
```

##### 401: 인증되지 않음 {#401-unauthorized-13}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-14}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

---

## 프로필에 게시물 고정 {#pin}

```http
POST /api/v1/statuses/:id/pin HTTP/1.1
```

내 공개 게시물 하나를 프로필 상단에 표시합니다.

**반환:** [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `write:accounts`\
**버전 이력:**\
1.6.0 - 추가\
3.5.0 - 이제 비공개 게시물 고정 가능

#### 요청 {#request-18}

##### 경로 매개변수 {#path-parameters-16}

:id
: {{<required>}} 문자열. 데이터베이스의 Status 로컬 ID입니다. 인증된 계정이 작성한 게시물이어야 합니다.

##### 헤더 {#headers-18}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-18}
##### 200: 성공 {#200-ok-18}

게시물을 고정했습니다. 부스트가 아니며 작성 계정이 내 계정인 게시물입니다.

```json
{
  "id": "99734435964706331",
  "created_at": "2018-03-23T17:38:40.700Z",
  // ...
  "favourited": false,
  "reblogged": false,
  "muted": false,
  "bookmarked": false,
  "pinned": true,
  // ...
  "reblog": null,
  // ...
  "account": {
    "id": "14715",
    "username": "trwnh",
    "acct": "trwnh",
    // ...
  },
  // ...
}
```

##### 401: 인증되지 않음 {#401-unauthorized-14}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-15}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-1}

Status가 내 소유가 아닌 경우:

```json
{
  "error": "Validation failed: Someone else's post cannot be pinned"
}
```

계정의 고정 게시물 수가 제한에 이미 도달한 경우(기본값은 5개, [Instance#max_pinned_statuses]({{< relref "entities/Instance#max_pinned_statuses" >}}) 참고):

```json
{
  "error": "Validation failed: You have already pinned the maximum number of posts"
}
```

3.5.0 이전에는 비공개 게시물을 원격 사이트에서 가져올 수 없고 반드시 전달되어야 했으므로 내 비공개 게시물을 고정할 수 없었습니다. (3.5.0에서는 계정을 대신하여 게시물을 가져오는 기능이 추가되었습니다.)

```json
{
  "error": "Validation failed: Posts that are only visible to mentioned users cannot be pinned"
}
```

---

## 프로필에서 게시물 고정 해제 {#unpin}

```http
POST /api/v1/statuses/:id/unpin HTTP/1.1
```

프로필 상단에서 게시물 표시를 해제합니다.

**반환:** [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `write:accounts`\
**버전 이력:**\
1.6.0 - 추가

#### 요청 {#request-19}

##### 경로 매개변수 {#path-parameters-17}

:id
: {{<required>}} 문자열. 데이터베이스의 Status 로컬 ID입니다.

##### 헤더 {#headers-19}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-19}
##### 200: 성공 {#200-ok-19}

게시물 고정을 해제했거나 이미 고정하지 않은 상태입니다.

```json
{
  "id": "99734435964706331",
  "created_at": "2018-03-23T17:38:40.700Z",
  // ...
  "favourited": false,
  "reblogged": false,
  "muted": false,
  "bookmarked": false,
  "pinned": false,
  // ...
  "reblog": null,
  // ...
  "account": {
    "id": "14715",
    "username": "trwnh",
    "acct": "trwnh",
    // ...
  },
  // ...
}
```

##### 401: 인증되지 않음 {#401-unauthorized-15}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-16}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

---

## 게시물 편집 {#edit}

```http
PUT /api/v1/statuses/:id HTTP/1.1
```

지정한 게시물을 편집하여 텍스트, 민감한 콘텐츠 여부, 미디어 첨부 파일, 투표를 변경합니다. 참고:

- 투표 선택지를 편집하거나 복수 선택 여부를 바꾸면 투표가 초기화됩니다.
- [ScheduledStatus]({{< relref "entities/scheduledstatus" >}})의 `scheduled_at` 속성을 편집하여 게시 날짜를 변경하려면 [예약 게시물 엔드포인트]({{< relref "methods/scheduled_statuses#update">}})를 사용하세요.

**반환:** [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `write:statuses`\
**버전 이력:**\
3.5.0 - 추가\
4.0.0 - `language` 추가\
4.5.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 7) - `quote_approval_policy` 추가

#### 요청 {#request-20}

##### 경로 매개변수 {#path-parameters-18}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-20}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-3}

status
: 문자열. 게시물의 일반 텍스트 내용입니다.

spoiler_text
: 문자열. 게시물의 일반 텍스트 제목 또는 콘텐츠 경고입니다.

sensitive
: 불리언. 게시물을 민감한 콘텐츠로 표시할지 여부입니다.

language
: 문자열. 게시물의 ISO 639-1 언어 코드입니다.

media_ids[]
: 문자열 배열. 미디어로 첨부할 Attachment ID를 포함합니다. 제공하면 `status`는 선택 사항이 되고 `poll`을 사용할 수 없습니다.

media_attributes[][]
: 문자열 배열. 각 배열은 id, description, focus를 포함합니다.

poll[options][]
: 문자열 배열. 투표의 가능한 답변입니다. 제공하면 `media_ids`를 사용할 수 없고 `poll[expires_in]`을 제공해야 합니다.

poll[expires_in]
: 정수. 투표를 열어둘 시간(초)입니다. 제공하면 `media_ids`를 사용할 수 없고 `poll[options]`를 제공해야 합니다.

poll[multiple]
: 불리언. 복수 선택을 허용할지 여부입니다. 기본값은 false입니다.

poll[hide_totals]
: 불리언. 투표가 끝날 때까지 투표수를 숨길지 여부입니다. 기본값은 false입니다.

quote_approval_policy
: 문자열(열거형 중 하나). 게시물을 인용할 수 있는 사람을 설정합니다. `visibility`가 `private` 또는 `direct`이면 무시되며 이 경우 정책은 항상 `nobody`로 설정됩니다. 정책을 변경해도 이전 인용은 무효화되지 않습니다.\
`public` = 차단되지 않았다면 누구나 이 게시물을 인용할 수 있으며 인용을 자동 수락합니다.\
`followers` = 팔로워와 작성자만 이 게시물을 인용할 수 있으며 인용을 자동 수락합니다.\
`nobody` = 작성자만 게시물을 인용할 수 있습니다.

#### 응답 {#response-20}
##### 200: 성공 {#200-ok-20}

게시물을 편집했습니다.

```json
{
  "id": "108942703571991143",
  "created_at": "2022-09-04T23:22:13.704Z",
  "in_reply_to_id": null,
  "in_reply_to_account_id": null,
  "sensitive": false,
  "spoiler_text": "",
  "visibility": "public",
  "language": "en",
  "uri": "https://mastodon.social/users/trwnh/statuses/108942703571991143",
  "url": "https://mastodon.social/@trwnh/108942703571991143",
  "replies_count": 3,
  "reblogs_count": 1,
  "favourites_count": 6,
  "edited_at": "2022-09-05T00:33:20.309Z",
  "favourited": false,
  "reblogged": false,
  "muted": false,
  "bookmarked": false,
  "pinned": false,
  "content": "<p>this is a status that has been edited multiple times to change the text, add a poll, and change poll options.</p>",
  "filtered": [],
  "reblog": null,
  "application": {
    "name": "SubwayTooter",
    "website": null
  },
  "account": {
    "id": "14715",
    "username": "trwnh",
    "acct": "trwnh",
    "display_name": "infinite love ⴳ",
    // ...
  },
  "media_attachments": [],
  "mentions": [],
  "tags": [],
  "emojis": [],
  "card": null,
  "poll": null
}
```

##### 401: 인증되지 않음 {#401-unauthorized-16}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-17}

게시물이 없거나, 비공개이거나, 내 소유가 아닙니다.

```json
{
  "error": "Record not found"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-2}

```json
{
  "error": "Validation failed: Text can't be blank"
}
```

---

## 게시물의 상호작용 정책 편집 {#edit_interaction_policy}

```http
PUT /api/v1/statuses/:id/interaction_policy HTTP/1.1
```

지정한 게시물의 상호작용 정책을 변경합니다. 현재는 인용 승인 정책을 변경하는 것을 의미합니다.

**반환:** [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `write:statuses`\
**버전 이력:**\
4.5.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 7) - 추가

#### 요청 {#request-21}

##### 경로 매개변수 {#path-parameters-19}

:id
: {{<required>}} 문자열. 데이터베이스의 Status ID입니다.

##### 헤더 {#headers-21}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-4}

quote_approval_policy
: 문자열(열거형 중 하나). 게시물을 인용할 수 있는 사람을 설정합니다. `visibility`가 `private` 또는 `direct`이면 무시되며 이 경우 정책은 항상 `nobody`로 설정됩니다. 정책을 변경해도 이전 인용은 무효화되지 않습니다.\
`public` = 차단되지 않았다면 누구나 이 게시물을 인용할 수 있으며 인용을 자동 수락합니다.\
`followers` = 팔로워와 작성자만 이 게시물을 인용할 수 있으며 인용을 자동 수락합니다.\
`nobody` = 작성자만 게시물을 인용할 수 있습니다.

#### 응답 {#response-21}
##### 200: 성공 {#200-ok-21}

게시물을 편집했습니다.

```json
{
  "id": "108942703571991143",
  "created_at": "2022-09-04T23:22:13.704Z",
  "in_reply_to_id": null,
  "in_reply_to_account_id": null,
  "sensitive": false,
  "spoiler_text": "",
  "visibility": "public",
  "language": "en",
  "uri": "https://mastodon.social/users/trwnh/statuses/108942703571991143",
  "url": "https://mastodon.social/@trwnh/108942703571991143",
  "replies_count": 3,
  "reblogs_count": 1,
  "favourites_count": 6,
  "edited_at": "2022-09-05T00:33:20.309Z",
  "favourited": false,
  "reblogged": false,
  "muted": false,
  "bookmarked": false,
  "pinned": false,
  "content": "<p>this is a status that has been edited multiple times to change the text, add a poll, and change poll options.</p>",
  "filtered": [],
  "reblog": null,
  "application": {
    "name": "SubwayTooter",
    "website": null
  },
  "account": {
    "id": "14715",
    "username": "trwnh",
    "acct": "trwnh",
    "display_name": "infinite love ⴳ",
    // ...
  },
  "media_attachments": [],
  "mentions": [],
  "tags": [],
  "emojis": [],
  "card": null,
  "poll": null,
  "quote_approval": {
    "automatic": ["public"],
    "manual": [],
    "current_user": "automatic",
  }
}
```

##### 401: 인증되지 않음 {#401-unauthorized-17}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-18}

게시물이 없거나, 비공개이거나, 내 소유가 아닙니다.

```json
{
  "error": "Record not found"
}
```

---

## 게시물 편집 이력 조회 {#history}

```http
GET /api/v1/statuses/:id/history HTTP/1.1
```

최초 및 현재 상태를 포함하여 알려진 모든 버전의 게시물을 가져옵니다.

**반환:** 배열: [StatusEdit]({{< relref "entities/statusedit" >}})\
**OAuth:** 공개 게시물은 공개, 비공개 게시물은 사용자 토큰 + `read:statuses`\
**버전 이력:**\
3.5.0 - 추가

#### 요청 {#request-22}

##### 경로 매개변수 {#path-parameters-20}

:id
: {{<required>}} 문자열. 데이터베이스의 Status 로컬 ID입니다.

##### 헤더 {#headers-22}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-22}
##### 200: 성공 {#200-ok-22}

```json
[
  {
    "content": "<p>this is a status that will be edited</p>",
    "spoiler_text": "",
    "sensitive": false,
    "created_at": "2022-09-04T23:22:13.704Z",
    "account": {
      "id": "14715",
      "username": "trwnh",
      "acct": "trwnh",
      "display_name": "infinite love ⴳ",
      // ...
    },
    "media_attachments": [],
    "emojis": []
  },
  {
    "content": "<p>this is a status that has been edited</p>",
    "spoiler_text": "",
    "sensitive": false,
    "created_at": "2022-09-04T23:22:42.555Z",
    "account": {
      "id": "14715",
      "username": "trwnh",
      "acct": "trwnh",
      "display_name": "infinite love ⴳ",
      // ...
    },
    "media_attachments": [],
    "emojis": []
  },
  {
    "content": "<p>this is a status that has been edited twice</p>",
    "spoiler_text": "",
    "sensitive": false,
    "created_at": "2022-09-04T23:22:55.956Z",
    "account": {
      "id": "14715",
      "username": "trwnh",
      "acct": "trwnh",
      "display_name": "infinite love ⴳ",
      // ...
    },
    "media_attachments": [],
    "emojis": []
  },
  {
    "content": "<p>this is a status that has been edited three times. this time a poll has been added.</p>",
    "spoiler_text": "",
    "sensitive": false,
    "created_at": "2022-09-05T00:01:48.160Z",
    "poll": {
      "options": [
        {
          "title": "cool"
        },
        {
          "title": "uncool"
        },
        {
          "title": "spiderman"
        }
      ]
    },
    "account": {
      "id": "14715",
      "username": "trwnh",
      "acct": "trwnh",
      "display_name": "infinite love ⴳ",
      // ...
    },
    "media_attachments": [],
    "emojis": []
  },
  {
    "content": "<p>this is a status that has been edited three times. this time a poll has been added.</p>",
    "spoiler_text": "",
    "sensitive": false,
    "created_at": "2022-09-05T00:03:32.480Z",
    "poll": {
      "options": [
        {
          "title": "cool"
        },
        {
          "title": "uncool"
        },
        {
          "title": "spiderman (this option has been changed)"
        }
      ]
    },
    "account": {
      "id": "14715",
      "username": "trwnh",
      "acct": "trwnh",
      "display_name": "infinite love ⴳ",
      // ...
    },
    "media_attachments": [],
    "emojis": []
  }
]
```

##### 404: 찾을 수 없음 {#404-not-found-19}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

---

## 게시물 원본 조회 {#source}

```http
GET /api/v1/statuses/:id/source HTTP/1.1
```

게시물을 편집할 수 있도록 원본 속성을 가져옵니다.

**반환:** [StatusSource]({{< relref "entities/statussource" >}})\
**OAuth:** 앱 토큰 + `read:statuses`\
**버전 이력:**\
3.5.0 - 추가

#### 요청 {#request-23}

##### 경로 매개변수 {#path-parameters-21}

:id
: {{<required>}} 문자열. 데이터베이스의 Status 로컬 ID입니다.

##### 헤더 {#headers-23}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-23}
##### 200: 성공 {#200-ok-23}

```json
{
  "id": "108942703571991143",
  "text": "this is a status that will be edited",
  "spoiler_text": ""
}
```

##### 401: 인증되지 않음 {#401-unauthorized-18}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-20}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

---

## 미리보기 카드 가져오기 {{%removed%}} {#card}

```http
GET /api/v1/statuses/:id/card HTTP/1.1
```

**반환:** [PreviewCard]({{< relref "entities/PreviewCard" >}})\
**OAuth:** 공개 게시물은 공개, 비공개 게시물은 사용자 토큰 + `read:statuses`\
**버전 이력:**\
0.0.0 - 추가\
2.6.0 - Status 엔터티에 포함된 card 속성을 권장하며 사용 중단 예정\
3.0.0 - 제거

#### 요청 {#request-24}

##### 경로 매개변수 {#path-parameters-22}

:id
: {{<required>}} 문자열. 데이터베이스의 Status 로컬 ID입니다.

##### 헤더 {#headers-24}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-24}
##### 200: 성공 {#200-ok-24}

```json
{
  "url": "https://www.youtube.com/watch?v=OMv_EPMED8Y",
  "title": "♪ Brand New Friend (Christmas Song!)",
  "description": "",
  "type": "video",
  "author_name": "YOGSCAST Lewis & Simon",
  "author_url": "https://www.youtube.com/user/BlueXephos",
  "provider_name": "YouTube",
  "provider_url": "https://www.youtube.com/",
  "html": "<iframe width=\"480\" height=\"270\" src=\"https://www.youtube.com/embed/OMv_EPMED8Y?feature=oembed\" frameborder=\"0\" allowfullscreen=\"\"></iframe>",
  "width": 480,
  "height": 270,
  "image": "https://files.mastodon.social/preview_cards/images/014/179/145/original/9cf4b7cf5567b569.jpeg",
  "embed_url": ""
}
```

##### 404: 찾을 수 없음 {#404-not-found-21}

게시물이 없거나 비공개입니다.

```json
{
  "error": "Record not found"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/statuses_controller.rb" caption="app/controllers/api/v1/statuses_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/statuses/bookmarks_controller.rb" caption="app/controllers/api/v1/statuses/bookmarks_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/statuses/favourited_by_accounts_controller.rb" caption="app/controllers/api/v1/statuses/favourited_by_accounts_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/statuses/favourites_controller.rb" caption="app/controllers/api/v1/statuses/favourites_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/statuses/histories_controller.rb" caption="app/controllers/api/v1/statuses/histories_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/statuses/mutes_controller.rb" caption="app/controllers/api/v1/statuses/mutes_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/statuses/pins_controller.rb" caption="app/controllers/api/v1/statuses/pins_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/statuses/reblogged_by_accounts_controller.rb" caption="app/controllers/api/v1/statuses/reblogged_by_accounts_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/statuses/reblogs_controller.rb" caption="app/controllers/api/v1/statuses/reblogs_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/statuses/sources_controller.rb" caption="app/controllers/api/v1/statuses/sources_controller.rb" >}}

