---
title: V1 서버 (V1::Instance)
description: 이 도메인에서 실행 중인 마스토돈 소프트웨어 서버를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/v1_instance",
  "/entities/V1_Instance",
  "/api/entities/v1_instance",
  "/api/entities/V1_Instance",
]
---

## 예시 {#example}

```json
{
  "uri":"mastodon.social",
  "title":"Mastodon",
  "short_description":"The original server operated by the Mastodon gGmbH non-profit",
  "description":"",
  "email":"staff@mastodon.social",
  "version":"3.5.3",
  "urls":{
    "streaming_api":"wss://mastodon.social"
  },
  "stats":{
    "user_count":812303,
    "status_count":38151616,
    "domain_count":25255
  },
  "thumbnail":"https://files.mastodon.social/site_uploads/files/000/000/001/original/vlcsnap-2018-08-27-16h43m11s127.png",
  "languages":[
    "en"
  ],
  "registrations":false,
  "approval_required":false,
  "invites_enabled":true,
  "configuration":{
    "accounts": {
      "max_featured_tags": 10
    },
    "statuses":{
      "max_characters":500,
      "max_media_attachments":4,
      "characters_reserved_per_url":23
    },
    "media_attachments":{
      "supported_mime_types":[
        "image/jpeg",
        "image/png",
        "image/gif",
        "image/webp",
        "video/webm",
        "video/mp4",
        "video/quicktime",
        "video/ogg",
        "audio/wave",
        "audio/wav",
        "audio/x-wav",
        "audio/x-pn-wave",
        "audio/vnd.wave",
        "audio/ogg",
        "audio/vorbis",
        "audio/mpeg",
        "audio/mp3",
        "audio/webm",
        "audio/flac",
        "audio/aac",
        "audio/m4a",
        "audio/x-m4a",
        "audio/mp4",
        "audio/3gpp",
        "video/x-ms-asf"
      ],
      "image_size_limit":10485760,
      "image_matrix_limit":16777216,
      "video_size_limit":41943040,
      "video_frame_rate_limit":60,
      "video_matrix_limit":2304000
    },
    "polls":{
      "max_options":4,
      "max_characters_per_option":50,
      "min_expiration":300,
      "max_expiration":2629746
    }
  },
  "contact_account":{
    "id":"1",
    "username":"Gargron",
    "acct":"Gargron",
    "display_name":"Eugen",
    "locked":false,
    "bot":false,
    "discoverable":true,
    "group":false,
    "created_at":"2016-03-16T00:00:00.000Z",
    "note":"\u003cp\u003eFounder, CEO and lead developer \u003cspan class=\"h-card\"\u003e\u003ca href=\"https://mastodon.social/@Mastodon\" class=\"u-url mention\"\u003e@\u003cspan\u003eMastodon\u003c/span\u003e\u003c/a\u003e\u003c/span\u003e, Germany.\u003c/p\u003e",
    "url":"https://mastodon.social/@Gargron",
    "avatar":"https://files.mastodon.social/accounts/avatars/000/000/001/original/dc4286ceb8fab734.jpg",
    "avatar_static":"https://files.mastodon.social/accounts/avatars/000/000/001/original/dc4286ceb8fab734.jpg",
    "header":"https://files.mastodon.social/accounts/headers/000/000/001/original/3b91c9965d00888b.jpeg",
    "header_static":"https://files.mastodon.social/accounts/headers/000/000/001/original/3b91c9965d00888b.jpeg",
    "followers_count":118944,
    "following_count":305,
    "statuses_count":72309,
    "last_status_at":"2022-08-24",
    "emojis":[
      
    ],
    "fields":[
      {
        "name":"Patreon",
        "value":"\u003ca href=\"https://www.patreon.com/mastodon\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"\u003e\u003cspan class=\"invisible\"\u003ehttps://www.\u003c/span\u003e\u003cspan class=\"\"\u003epatreon.com/mastodon\u003c/span\u003e\u003cspan class=\"invisible\"\u003e\u003c/span\u003e\u003c/a\u003e",
        "verified_at":null
      }
    ]
  },
  "rules":[
    {
      "id":"1",
      "text":"Sexually explicit or violent media must be marked as sensitive when posting"
    },
    {
      "id":"2",
      "text":"No racism, sexism, homophobia, transphobia, xenophobia, or casteism"
    },
    {
      "id":"3",
      "text":"No incitement of violence or promotion of violent ideologies"
    },
    {
      "id":"4",
      "text":"No harassment, dogpiling or doxxing of other users"
    },
    {
      "id":"5",
      "text":"No content illegal in Germany"
    },
    {
      "id":"7",
      "text":"Do not share intentionally false or misleading information"
    }
  ]
}
```

## 속성 {#attributes}

### `uri` {#uri}

**설명:** 서버의 WebFinger 도메인 이름입니다(URI/URL이 아님).\
**유형:** 문자열\
**버전 이력:**\
1.1.0 - 추가

### `title` {#title}

**설명:** 웹사이트 제목입니다.\
**유형:** 문자열\
**버전 이력:**\
1.1.0 - 추가

### `short_description` {#short_description}

**설명:** 관리자가 작성한 짧은 일반 텍스트 설명입니다.\
**유형:** 문자열\
**버전 이력:**\
2.9.2 - 추가

### `description` {#description}

**설명:** HTML을 허용하는 마스토돈 사이트 설명입니다.\
**유형:** 문자열\
**버전 이력:**\
1.1.0 - 추가

### `email` {#email}

**설명:** 문의할 때 연락할 수 있는 이메일입니다.\
**유형:** 문자열\
**버전 이력:**\
1.1.0 - 추가

### `version` {#version}

**설명:** 서버에 설치한 마스토돈 버전입니다.\
**유형:** 문자열\
**버전 이력:**\
1.3.0 - 추가

### `urls` {#urls}

**설명:** 클라이언트 앱에 유용한 URL입니다.\
**유형:** 해시\
**버전 이력:**\
1.4.2 - 추가

#### `urls[streaming_api]` {#streaming_api}

**설명:** 스트리밍 API에 연결할 WebSocket URL입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
1.4.2 - 추가

### `stats` {#stats}

**설명:** 서버에 포함된 정보량에 관한 통계입니다.\
**유형:** 해시\
**버전 이력:**\
1.6.0 - 추가

#### `stats[user_count]` {#user_count}

**설명:** 이 서버의 총 사용자 수입니다.\
**유형:** 정수\
**버전 이력:**\
1.6.0 - 추가

#### `stats[status_count]` {#status_count}

**설명:** 이 서버의 총 게시물 수입니다.\
**유형:** 정수\
**버전 이력:**\
1.6.0 - 추가

#### `stats[domain_count]` {#domain_count}

**설명:** 이 서버가 발견한 총 도메인 수입니다.\
**유형:** 정수\
**버전 이력:**\
1.6.0 - 추가

### `thumbnail` {#thumbnail}

**설명:** 웹사이트 배너 이미지입니다.\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
1.6.1 - 추가

### `languages` {#languages}

**설명:** 웹사이트와 운영진의 기본 언어입니다.\
**유형:** 배열: 문자열 (ISO 639-1 두 글자 코드)\
**버전 이력:**\
2.3.0 - 추가

### `registrations` {#registrations}

**설명:** 가입이 활성화되어 있는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.7.2 - 추가

### `approval_required` {#approval_required}

**설명:** 가입에 중재자 승인이 필요한지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.9.2 - 추가

### `invites_enabled` {#invites_enabled}

**설명:** 초대가 활성화되어 있는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
3.1.4 - 추가

### `configuration` {#configuration}

**설명:** 이 웹사이트에 설정된 값과 제한입니다.\
**유형:** 해시\
**버전 이력:**\
3.4.2 - 추가

#### `configuration[accounts]` {#accounts}

**설명:** 계정 관련 제한입니다.\
**유형:** 해시\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[accounts][max_featured_tags]` {#max_featured_tags}

**설명:** 계정별 허용되는 최대 추천 태그 수입니다.\
**유형:** 정수\
**버전 이력:**\
4.0.0 - 추가

#### `configuration[statuses]` {#statuses}

**설명:** 게시물 작성 관련 제한입니다.\
**유형:** 해시\
**버전 이력:**\
3.4.2 - 추가

##### `configuration[statuses][max_characters]` {#max_characters}

**설명:** 게시물당 최대 허용 문자 수입니다.\
**유형:** 정수\
**버전 이력:**\
3.4.2 - 추가

##### `configuration[statuses][max_media_attachments]` {#max_media_attachments}

**설명:** 게시물에 추가할 수 있는 최대 미디어 첨부 파일 수입니다.\
**유형:** 정수\
**버전 이력:**\
3.4.2 - 추가

##### `configuration[statuses][characters_reserved_per_url]` {#characters_reserved_per_url}

**설명:** 게시물의 각 URL은 정확히 이 문자 수로 간주합니다.\
**유형:** 정수\
**버전 이력:**\
3.4.2 - 추가

#### `configuration[media_attachments]` {#media_attachments}

**설명:** 허용되는 첨부 파일에 관한 힌트입니다.\
**유형:** 해시\
**버전 이력:**\
3.4.2 - 추가

##### `configuration[media_attachments][supported_mime_types]` {#supported_mime_types}

**설명:** 업로드할 수 있는 MIME 유형을 포함합니다.\
**유형:** 배열: 문자열\
**버전 이력:**\
3.4.2 - 추가

##### `configuration[media_attachments][image_size_limit]` {#image_size_limit}

**설명:** 업로드한 이미지의 최대 크기(바이트)입니다.\
**유형:** 정수\
**버전 이력:**\
3.4.2 - 추가

##### `configuration[media_attachments][image_matrix_limit]` {#image_matrix_limit}

**설명:** 업로드 이미지의 최대 픽셀 수(너비 곱하기 높이)입니다.\
**유형:** 정수\
**버전 이력:**\
3.4.2 - 추가

##### `configuration[media_attachments][video_size_limit]` {#video_size_limit}

**설명:** 업로드한 동영상의 최대 크기(바이트)입니다.\
**유형:** 정수\
**버전 이력:**\
3.4.2 - 추가

##### `configuration[media_attachments][video_frame_rate_limit]` {#video_frame_rate_limit}

**설명:** 업로드한 동영상의 최대 프레임 속도입니다.\
**유형:** 정수\
**버전 이력:**\
3.4.2 - 추가

##### `configuration[media_attachments][video_matrix_limit]` {#video_matrix_limit}

**설명:** 업로드 동영상의 최대 픽셀 수(너비 곱하기 높이)입니다.\
**유형:** 정수\
**버전 이력:**\
3.4.2 - 추가

#### `configuration[polls]` {#polls}

**설명:** 투표 관련 제한입니다.\
**유형:** 해시\
**버전 이력:**\
3.4.2 - 추가

##### `configuration[polls][max_options]` {#max_options}

**설명:** 각 투표에서 허용하는 최대 선택지 수입니다.\
**유형:** 정수\
**버전 이력:**\
3.4.2 - 추가

##### `configuration[polls][max_characters_per_option]` {#max_characters_per_option}

**설명:** 각 투표 선택지에서 허용하는 문자 수입니다.\
**유형:** 정수\
**버전 이력:**\
3.4.2 - 추가

##### `configuration[polls][min_expiration]` {#min_expiration}

**설명:** 허용되는 최소 투표 기간(초)입니다.\
**유형:** 정수\
**버전 이력:**\
3.4.2 - 추가

##### `configuration[polls][max_expiration]` {#max_expiration}

**설명:** 허용되는 최대 투표 기간(초)입니다.\
**유형:** 정수\
**버전 이력:**\
3.4.2 - 추가

### `contact_account` {#contact_account}

**설명:** `email` 대신 연락할 수 있는 사용자입니다.\
**유형:** {{<nullable>}} [Account]({{< relref "entities/Account" >}}) 또는 null\
**버전 이력:**\
2.3.0 - 추가

### `rules` {#rules}

**설명:** 웹사이트 규칙의 항목별 목록입니다.\
**유형:** 배열: [Rule]({{< relref "entities/Rule" >}})\
**버전 이력:**\
3.4.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/instance#v1" caption="GET /api/v1/instance" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/v1/instance_serializer.rb" caption="app/serializers/rest/v1/instance_serializer.rb" >}}



