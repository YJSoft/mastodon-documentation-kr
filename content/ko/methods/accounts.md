---
title: 계정 API 메서드
description: 계정과 프로필에 관한 메서드입니다.
menu:
  docs:
    name: 계정
    parent: methods
    identifier: methods-accounts
aliases: [
  "/methods/accounts",
  "/api/methods/accounts"
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 계정 등록 {{%deprecated%}} {#create}

```http
POST /api/v1/accounts HTTP/1.1
```

사용자와 계정 레코드를 생성합니다. 요청을 시작한 앱에 대한 계정 액세스 토큰을 반환합니다. 앱은 나중에 사용할 수 있도록 이 토큰을 저장하고, 사용자가 이메일 받은편지함의 링크를 클릭하여 계정을 확인할 때까지 기다려야 합니다.

OAuth 애플리케이션과 생성된 사용자 계정 간의 관계가 저장됩니다.

**반환:** [Token]({{< relref "entities/token" >}})\
**OAuth:** 앱 토큰 + `write:accounts`\
**버전 이력:**\
2.7.0 - 추가\
3.0.0 - `reason` 매개변수 추가\
3.4.0 - 실패 응답에 `details` 추가\
4.4.0 - `date_of_birth` 매개변수 추가\
5.0.0 - [OAuth 가입 절차]({{< relref "methods/oauth#authorize" >}})를 권장하며 사용 중단 예정

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <app_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

username
: {{<required>}} 문자열. 계정에 사용할 사용자명입니다.

email
: {{<required>}} 문자열. 로그인에 사용할 이메일 주소입니다.

password
: {{<required>}} 문자열. 로그인에 사용할 비밀번호입니다.

agreement
: {{<required>}} 불리언. 사용자가 로컬 규칙, 약관, 정책에 동의하는지 여부입니다. 이 매개변수를 TRUE로 설정하기 전에 사용자에게 해당 내용을 제시하여 동의를 받아야 합니다.

locale
: {{<required>}} 문자열. 전송할 확인 이메일의 언어입니다.

reason
: 문자열. 가입에 수동 승인이 필요한 경우 중재자가 이 내용을 검토합니다.

date_of_birth
: 문자열([날짜](/api/datetime-format#date)). 서버에 최소 연령 요건이 있으면 필수입니다.

#### 응답 {#response}

##### 200: 성공 {#200-ok}

```json
```

##### 401: 인증되지 않음 {#401-unauthorized}

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

`details` 매개변수에는 발견된 모든 오류가 포함됩니다. 오류가 발생한 매개변수를 키로, 발견된 모든 오류의 배열을 값으로 사용하는 해시 구조입니다.

오류 응답 예:

```json
{
  "error": "Validation failed: Password can't be blank, Username must contain only letters, numbers and underscores, Agreement must be accepted",
  "details": {
    "password": [
      {
        "error": "ERR_BLANK",
        "description": "can't be blank"
      }
    ],
    "username": [
      {
        "error": "ERR_INVALID",
        "description": "must contain only letters, numbers and underscores"
      }
    ],
    "agreement": [
      {
        "error": "ERR_ACCEPTED",
        "description": "must be accepted"
      }
    ]
  }
}
```

다음과 같은 오류가 발생할 수 있습니다.

ERR_BLOCKED
: 이메일 제공업체가 허용되지 않는 경우

ERR_UNREACHABLE
: 이메일 주소가 DNS(MX, A, AAAA)를 통해 어떤 IP로도 해석되지 않는 경우

ERR_TAKEN
: 사용자명이나 이메일이 이미 사용 중인 경우

ERR_RESERVED
: 사용자명이 예약된 이름인 경우(예: "webmaster" 또는 "admin")

ERR_ACCEPTED
: 약관에 동의하지 않은 경우

ERR_BLANK
: 필수 속성이 비어 있는 경우

ERR_INVALID
: 속성의 형식이 잘못된 경우(예: 잘못된 문자 또는 유효하지 않은 이메일 주소)

ERR_TOO_LONG
: 속성이 글자 수 제한을 초과한 경우

ERR_TOO_SHORT
: 속성이 최소 글자 수에 미치지 못한 경우

ERR_INCLUSION
: 속성이 허용된 값에 속하지 않는 경우(예: 지원하지 않는 로캘)

##### 429: 요청 빈도 제한됨 {#429-rate-limited}

```json
{
  "error": "Too many requests"
}
```

---

## 계정 자격 증명 확인 {#verify_credentials}

```http
GET /api/v1/accounts/verify_credentials HTTP/1.1
```

사용자 토큰이 작동하는지 확인합니다.

**반환:** [CredentialAccount]({{< relref "entities/Account#CredentialAccount">}})\
**OAuth:** 사용자 토큰 + `profile` 또는 `read:accounts`\
**버전 이력:**\
0.0.0 - 추가\
4.3.0 - `profile` 범위 추가\
5.0.0 - `allow_nonfunctional` 매개변수 추가

#### 요청 {#request-1}

##### 쿼리 매개변수 {#query-parameters}

allow_nonfunctional
: 불리언. 계정이 정상 작동하지 않는 경우(예: 승인 또는 확인되지 않은 경우)에도 계정 정보를 가져올지 여부입니다. 기본값은 `false`입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}

##### 200: 성공 {#200-ok-1}

다른 사람의 계정에서는 볼 수 없는 추가 속성 `source`에 주목하세요. 또한 `source`에는 일반 텍스트를 사용하며, 이에 대응하는 `note`, `fields` 등의 속성에는 HTML을 사용합니다.

```json
{
  "id": "14715",
  "username": "trwnh",
  "acct": "trwnh",
  "display_name": "infinite love ⴳ",
  "locked": false,
  "bot": false,
  "created_at": "2016-11-24T10:02:12.085Z",
  "note": "<p>i have approximate knowledge of many things. perpetual student. (nb/ace/they)</p><p>xmpp/email: a@trwnh.com<br /><a href=\"https://trwnh.com\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"\">trwnh.com</span><span class=\"invisible\"></span></a><br />help me live: <a href=\"https://liberapay.com/at\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"\">liberapay.com/at</span><span class=\"invisible\"></span></a> or <a href=\"https://paypal.me/trwnh\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"\">paypal.me/trwnh</span><span class=\"invisible\"></span></a></p><p>- my triggers are moths and glitter<br />- i have all notifs except mentions turned off, so please interact if you wanna be friends! i literally will not notice otherwise<br />- dm me if i did something wrong, so i can improve<br />- purest person on fedi, do not lewd in my presence<br />- #1 ami cole fan account</p><p>:fatyoshi:</p>",
  "url": "https://mastodon.social/@trwnh",
  "avatar": "https://files.mastodon.social/accounts/avatars/000/014/715/original/34aa222f4ae2e0a9.png",
  "avatar_static": "https://files.mastodon.social/accounts/avatars/000/014/715/original/34aa222f4ae2e0a9.png",
  "header": "https://files.mastodon.social/accounts/headers/000/014/715/original/5c6fc24edb3bb873.jpg",
  "header_static": "https://files.mastodon.social/accounts/headers/000/014/715/original/5c6fc24edb3bb873.jpg",
  "followers_count": 821,
  "following_count": 178,
  "statuses_count": 33120,
  "last_status_at": "2019-11-24T15:49:42.251Z",
  "indexable": true,
  "roles": [],
  "source": {
    "privacy": "public",
    "sensitive": false,
    "spoiler_field": false,
    "language": "",
    "note": "i have approximate knowledge of many things. perpetual student. (nb/ace/they)\r\n\r\nxmpp/email: a@trwnh.com\r\nhttps://trwnh.com\r\nhelp me live: https://liberapay.com/at or https://paypal.me/trwnh\r\n\r\n- my triggers are moths and glitter\r\n- i have all notifs except mentions turned off, so please interact if you wanna be friends! i literally will not notice otherwise\r\n- dm me if i did something wrong, so i can improve\r\n- purest person on fedi, do not lewd in my presence\r\n- #1 ami cole fan account\r\n\r\n:fatyoshi:",
    "fields": [
      {
        "name": "Website",
        "value": "https://trwnh.com",
        "verified_at": "2019-08-29T04:14:55.571+00:00"
      },
      {
        "name": "Sponsor",
        "value": "https://liberapay.com/at",
        "verified_at": "2019-11-15T10:06:15.557+00:00"
      },
      {
        "name": "Fan of:",
        "value": "Punk-rock and post-hardcore (Circa Survive, letlive., La Dispute, THE FEVER 333)Manga (Yu-Gi-Oh!, One Piece, JoJo's Bizarre Adventure, Death Note, Shaman King)Platformers and RPGs (Banjo-Kazooie, Boktai, Final Fantasy Crystal Chronicles)",
        "verified_at": null
      },
      {
        "name": "Main topics:",
        "value": "systemic analysis, design patterns, anticapitalism, info/tech freedom, theory and philosophy, and otherwise being a genuine and decent wholesome poster. i'm just here to hang out and talk to cool people!",
        "verified_at": null
      }
    ],
    "follow_requests_count": 0,
    "attribution_domains": [],
    "hide_collections": false,
    "discoverable": false,
    "indexable": true
  },
  "emojis": [
    {
      "shortcode": "fatyoshi",
      "url": "https://files.mastodon.social/custom_emojis/images/000/023/920/original/e57ecb623faa0dc9.png",
      "static_url": "https://files.mastodon.social/custom_emojis/images/000/023/920/static/e57ecb623faa0dc9.png",
      "visible_in_picker": true
    }
  ],
  "fields": [
    {
      "name": "Website",
      "value": "<a href=\"https://trwnh.com\" rel=\"me nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"\">trwnh.com</span><span class=\"invisible\"></span></a>",
      "verified_at": "2019-08-29T04:14:55.571+00:00"
    },
    {
      "name": "Sponsor",
      "value": "<a href=\"https://liberapay.com/at\" rel=\"me nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"\">liberapay.com/at</span><span class=\"invisible\"></span></a>",
      "verified_at": "2019-11-15T10:06:15.557+00:00"
    },
    {
      "name": "Fan of:",
      "value": "Punk-rock and post-hardcore (Circa Survive, letlive., La Dispute, THE FEVER 333)Manga (Yu-Gi-Oh!, One Piece, JoJo&apos;s Bizarre Adventure, Death Note, Shaman King)Platformers and RPGs (Banjo-Kazooie, Boktai, Final Fantasy Crystal Chronicles)",
      "verified_at": null
    },
    {
      "name": "Main topics:",
      "value": "systemic analysis, design patterns, anticapitalism, info/tech freedom, theory and philosophy, and otherwise being a genuine and decent wholesome poster. i&apos;m just here to hang out and talk to cool people!",
      "verified_at": null
    }
  ],
  "role": {
    "id": "-99",
    "name": "",
    "permissions": "65536",
    "color": "",
    "highlighted": false
  }
}
```

##### 401: 인증되지 않음 {#401-unauthorized-1}

토큰이 유효하지 않거나 올바르지 않으면 자격 증명 확인에 실패합니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 403: 금지됨 {#403-forbidden}

현재 사용자 계정이 비활성화되어 있거나, 확인된 이메일 주소가 없거나, 승인 대기 중입니다.

```json
{
  "error": "Your login is currently disabled"
}
```

```json
{
  "error": "Your login is missing a confirmed e-mail address"
}
```

```json
{
  "error": "Your login is currently pending approval"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-1}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 계정 자격 증명 수정 {#update_credentials}

```http
PATCH /api/v1/accounts/update_credentials HTTP/1.1
```

사용자의 표시 정보와 환경설정을 수정합니다.

**반환:** [CredentialAccount]({{< relref "entities/Account#CredentialAccount">}})\
**OAuth:** 사용자 토큰 + `write:accounts`\
**버전 이력:**\
1.1.1 - 추가\
2.3.0 - `locked` 매개변수 추가\
2.4.0 - `source[privacy,sensitive]` 매개변수 추가\
2.4.2 - `source[language]` 매개변수 추가\
2.7.0 - `discoverable` 매개변수 추가\
4.1.0 - `hide_collections` 매개변수 추가\
4.2.0 - `indexable` 매개변수 추가\
4.4.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 3) - `attribution_domains` 매개변수 추가\
4.5.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 7) - `quote_policy` 매개변수 추가\
4.6.1 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 11) - `avatar_description` 및 `header_description` 매개변수 추가\
5.0.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 12) - `source[spoiler_field]` 매개변수 추가

#### 요청 {#request-2}

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-1}

display_name
: 문자열. 프로필에 사용할 표시 이름입니다.

note
: 문자열. 계정 소개입니다.

avatar
: `multipart/form-data`로 인코딩한 아바타 이미지입니다.

avatar_description
: 문자열. 접근성을 위한 아바타의 일반 텍스트 설명입니다.

header
: `multipart/form-data`로 인코딩한 헤더 이미지입니다.

header_description
: 문자열. 접근성을 위한 헤더의 일반 텍스트 설명입니다.

locked
: 불리언. 팔로우 요청에 수동 승인이 필요한지 여부입니다.

bot
: 불리언. 계정에 봇 표시가 있는지 여부입니다.

discoverable
: 불리언. 프로필 디렉터리에 계정을 표시할지 여부입니다.

hide_collections
: 불리언. 팔로워와 팔로잉 계정을 숨길지 여부입니다.

indexable
: 불리언. 누구나 공개 게시물을 검색할 수 있게 할지 여부입니다.

attribution_domains[]
: 문자열 배열. 이 계정을 작성자로 표시하도록 허용할 웹사이트 도메인입니다. 최대 10개입니다.

fields_attributes
: 해시. 설정할 프로필 필드입니다. 이 해시의 키는 문자열로 변환한 정수이며(정확한 정숫값은 중요하지 않습니다), 값은 `name`과 `value`를 포함하는 또 다른 해시입니다. 기본적으로 최대 4개 필드입니다([Instance#max_profile_fields]({{< relref "entities/Instance#max_profile_fields" >}})에 명시).

fields_attributes[:index][name]
: 문자열. 프로필 필드 이름입니다. 기본적으로 최대 255자입니다([Instance#profile_field_name_limit]({{< relref "entities/Instance#profile_field_name_limit" >}})에 명시).

fields_attributes[:index][value]
: 문자열. 프로필 필드 값입니다. 기본적으로 최대 255자입니다([Instance#profile_field_value_limit]({{< relref "entities/Instance#profile_field_value_limit" >}})에 명시).

source[privacy]
: 문자열(열거형, `public`, `unlisted`, `private` 중 하나). 작성하는 게시물의 기본 공개 범위입니다.

source[sensitive]
: 불리언. 작성하는 게시물을 기본적으로 민감한 콘텐츠로 표시할지 여부입니다.

source[language]
: 문자열. 작성하는 게시물에 사용할 기본 언어입니다(ISO 639-1).

source[quote_policy]
: 문자열(열거형, `public`, `followers`, `nobody` 중 하나). 새 게시물의 기본 인용 정책입니다.

source[spoiler_field]
: 불리언. 새 게시물에 기본적으로 콘텐츠 경고를 추가할지 여부입니다.

#### 응답 {#response-2}

##### 200: 성공 {#200-ok-2}

계정 필드를 수정하려면 다음 예처럼 해시를 구성해야 합니다.

```json
{
  "fields_attributes": {
    "0": {
      "name": "Website",
      "value": "https://trwnh.com"
    },
    "1": {
      "name": "Sponsor",
      "value": "https://liberapay.com/at"
    },
    // ...
  }
}
```

쿼리 매개변수로 작성하면 요청은 다음과 같을 수 있습니다.

```http
PATCH https://mastodon.example/api/v1/accounts/update_credentials
?fields_attributes[0][name]=Website
&fields_attributes[0][value]=https://trwnh.com
&fields_attributes[1][name]=Sponsor
&fields_attributes[1][value]=https://liberapay.com/at
&...
```

정수 인덱스의 실제 값은 중요하지 않으며, 제공된 순서대로 필드가 채워집니다. 예:

```json
{
  "fields_attributes": {
    "420": {
      "name": "1st",
      "value": "field"
    },
    "69": {
      "name": "2nd",
      "value": "field"
    },
    "1312": {
      "name": "3rd",
      "value": "field"
    },
    "-99999999999999999999999999999999": {
      "name": "4th",
      "value": "field"
    },
  }
}
```

먼저 accounts/verify_credentials를 사용해 `source` 매개변수에서 일반 텍스트 표현을 가져온 다음, 사용자가 이를 편집하고 이 API로 제출하게 해야 합니다. 서버가 이에 대응하는 HTML을 생성합니다.

```json
{
  "id": "14715",
  "username": "trwnh",
  "acct": "trwnh",
  "display_name": "infinite love ⴳ",
  "locked": false,
  "bot": false,
  "created_at": "2016-11-24T10:02:12.085Z",
  "note": "<p>i have approximate knowledge of many things. perpetual student. (nb/ace/they)</p><p>xmpp/email: a@trwnh.com<br /><a href=\"https://trwnh.com\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"\">trwnh.com</span><span class=\"invisible\"></span></a><br />help me live: <a href=\"https://liberapay.com/at\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"\">liberapay.com/at</span><span class=\"invisible\"></span></a> or <a href=\"https://paypal.me/trwnh\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"\">paypal.me/trwnh</span><span class=\"invisible\"></span></a></p><p>- my triggers are moths and glitter<br />- i have all notifs except mentions turned off, so please interact if you wanna be friends! i literally will not notice otherwise<br />- dm me if i did something wrong, so i can improve<br />- purest person on fedi, do not lewd in my presence<br />- #1 ami cole fan account</p><p>:fatyoshi:</p>",
  "url": "https://mastodon.social/@trwnh",
  "avatar": "https://files.mastodon.social/accounts/avatars/000/014/715/original/34aa222f4ae2e0a9.png",
  "avatar_static": "https://files.mastodon.social/accounts/avatars/000/014/715/original/34aa222f4ae2e0a9.png",
  "header": "https://files.mastodon.social/accounts/headers/000/014/715/original/5c6fc24edb3bb873.jpg",
  "header_static": "https://files.mastodon.social/accounts/headers/000/014/715/original/5c6fc24edb3bb873.jpg",
  "followers_count": 834,
  "following_count": 182,
  "statuses_count": 33760,
  "last_status_at": "2019-12-01T00:12:08.731Z",
  "indexable": true,
  "roles": [],
  "source": {
    "privacy": "public",
    "sensitive": false,
    "spoiler_field": false,
    "language": "",
    "note": "i have approximate knowledge of many things. perpetual student. (nb/ace/they)\r\n\r\nxmpp/email: a@trwnh.com\r\nhttps://trwnh.com\r\nhelp me live: https://liberapay.com/at or https://paypal.me/trwnh\r\n\r\n- my triggers are moths and glitter\r\n- i have all notifs except mentions turned off, so please interact if you wanna be friends! i literally will not notice otherwise\r\n- dm me if i did something wrong, so i can improve\r\n- purest person on fedi, do not lewd in my presence\r\n- #1 ami cole fan account\r\n\r\n:fatyoshi:",
    "fields": [
      {
        "name": "Website",
        "value": "https://trwnh.com",
        "verified_at": "2019-08-29T04:14:55.571+00:00"
      },
      {
        "name": "Sponsor",
        "value": "https://liberapay.com/at",
        "verified_at": "2019-11-15T10:06:15.557+00:00"
      },
      {
        "name": "Fan of:",
        "value": "Punk-rock and post-hardcore (Circa Survive, letlive., La Dispute, THE FEVER 333)Manga (Yu-Gi-Oh!, One Piece, JoJo's Bizarre Adventure, Death Note, Shaman King)Platformers and RPGs (Banjo-Kazooie, Boktai, Final Fantasy Crystal Chronicles)",
        "verified_at": null
      },
      {
        "name": "Main topics:",
        "value": "systemic analysis, design patterns, anticapitalism, info/tech freedom, theory and philosophy, and otherwise being a genuine and decent wholesome poster. i'm just here to hang out and talk to cool people!",
        "verified_at": null
      }
    ],
    "follow_requests_count": 0,
    "attribution_domains": [],
    "hide_collections": false,
    "discoverable": false,
    "indexable": true
  },
  "emojis": [
    {
      "shortcode": "fatyoshi",
      "url": "https://files.mastodon.social/custom_emojis/images/000/023/920/original/e57ecb623faa0dc9.png",
      "static_url": "https://files.mastodon.social/custom_emojis/images/000/023/920/static/e57ecb623faa0dc9.png",
      "visible_in_picker": true
    }
  ],
  "fields": [
    {
      "name": "Website",
      "value": "<a href=\"https://trwnh.com\" rel=\"me nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"\">trwnh.com</span><span class=\"invisible\"></span></a>",
      "verified_at": "2019-08-29T04:14:55.571+00:00"
    },
    {
      "name": "Sponsor",
      "value": "<a href=\"https://liberapay.com/at\" rel=\"me nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"\">liberapay.com/at</span><span class=\"invisible\"></span></a>",
      "verified_at": "2019-11-15T10:06:15.557+00:00"
    },
    {
      "name": "Fan of:",
      "value": "Punk-rock and post-hardcore (Circa Survive, letlive., La Dispute, THE FEVER 333)Manga (Yu-Gi-Oh!, One Piece, JoJo&apos;s Bizarre Adventure, Death Note, Shaman King)Platformers and RPGs (Banjo-Kazooie, Boktai, Final Fantasy Crystal Chronicles)",
      "verified_at": null
    },
    {
      "name": "Main topics:",
      "value": "systemic analysis, design patterns, anticapitalism, info/tech freedom, theory and philosophy, and otherwise being a genuine and decent wholesome poster. i&apos;m just here to hang out and talk to cool people!",
      "verified_at": null
    }
  ],
  "role": {
    "id": "-99",
    "name": "",
    "permissions": "65536",
    "color": "",
    "highlighted": false
  }
}
```

##### 401: 인증되지 않음 {#401-unauthorized-2}

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-2}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 계정 가져오기 {#get}

```http
GET /api/v1/accounts/:id HTTP/1.1
```

프로필 정보를 확인합니다.

**반환:** [Account]({{< relref "entities/Account">}})\
**OAuth:** 공개\
**버전 이력:**\
0.0.0 - 추가\
2.4.0 - 계정이 정지되었으면 410 반환\
3.3.0 - 410 대신 `suspended: true`인 Account 반환

#### 요청 {#request-3}
##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-3}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-3}
##### 200: 성공 {#200-ok-3}

Account 레코드가 반환됩니다. 로컬 사용자의 `acct`에는 도메인 이름이 포함되지 않습니다.

###### 로컬 사용자 {#local-user}

```json
{
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
  "followers_count": 318699,
  "following_count": 453,
  "statuses_count": 61013,
  "last_status_at": "2019-11-30T20:02:08.277Z",
  "emojis": [],
  "indexable": true,
  "roles": [
    {
      "id": "3",
      "name": "Owner",
      "color": "#ff3838"
    }
  ],
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
}
```

###### 원격 사용자 {#remote-user}

```json
{
  "id": "23634",
  "username": "noiob",
  "acct": "noiob@awoo.space",
  "display_name": "shork",
  "locked": false,
  "bot": false,
  "created_at": "2017-02-08T02:00:53.274Z",
  "note": "<p>:ms_rainbow_flag:​ :ms_bisexual_flag:​ :ms_nonbinary_flag:​ <a href=\"https://awoo.space/tags/awoo\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>awoo</span></a>.space <a href=\"https://awoo.space/tags/admin\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>admin</span></a> ~ <a href=\"https://awoo.space/tags/bi\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>bi</span></a> ~ <a href=\"https://awoo.space/tags/nonbinary\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>nonbinary</span></a> ~ compsci student ~ likes video <a href=\"https://awoo.space/tags/games\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>games</span></a> and weird/ old electronics and will post obsessively about both ~ avatar by <span class=\"h-card\"><a href=\"https://weirder.earth/@dzuk\" class=\"u-url mention\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>dzuk</span></a></span></p>",
  "url": "https://awoo.space/@noiob",
  "avatar": "https://files.mastodon.social/accounts/avatars/000/023/634/original/6ca8804dc46800ad.png",
  "avatar_static": "https://files.mastodon.social/accounts/avatars/000/023/634/original/6ca8804dc46800ad.png",
  "header": "https://files.mastodon.social/accounts/headers/000/023/634/original/256eb8d7ac40f49a.png",
  "header_static": "https://files.mastodon.social/accounts/headers/000/023/634/original/256eb8d7ac40f49a.png",
  "followers_count": 553,
  "following_count": 405,
  "statuses_count": 28982,
  "last_status_at": "2019-12-01T00:39:57.264Z",
  "indexable": true,
  "roles": [],
  "emojis": [
    {
      "shortcode": "ms_rainbow_flag",
      "url": "https://files.mastodon.social/custom_emojis/images/000/028/691/original/6de008d6281f4f59.png",
      "static_url": "https://files.mastodon.social/custom_emojis/images/000/028/691/static/6de008d6281f4f59.png",
      "visible_in_picker": true
    },
    {
      "shortcode": "ms_bisexual_flag",
      "url": "https://files.mastodon.social/custom_emojis/images/000/050/744/original/02f94a5fca7eaf78.png",
      "static_url": "https://files.mastodon.social/custom_emojis/images/000/050/744/static/02f94a5fca7eaf78.png",
      "visible_in_picker": true
    },
    {
      "shortcode": "ms_nonbinary_flag",
      "url": "https://files.mastodon.social/custom_emojis/images/000/105/099/original/8106088bd4782072.png",
      "static_url": "https://files.mastodon.social/custom_emojis/images/000/105/099/static/8106088bd4782072.png",
      "visible_in_picker": true
    }
  ],
  "fields": [
    {
      "name": "Pronouns",
      "value": "they/them",
      "verified_at": null
    },
    {
      "name": "Alt",
      "value": "<span class=\"h-card\"><a href=\"https://cybre.space/@noiob\" class=\"u-url mention\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>noiob</span></a></span>",
      "verified_at": null
    },
    {
      "name": "Bots",
      "value": "<span class=\"h-card\"><a href=\"https://botsin.space/@darksouls\" class=\"u-url mention\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>darksouls</span></a></span>, <span class=\"h-card\"><a href=\"https://botsin.space/@nierautomata\" class=\"u-url mention\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>nierautomata</span></a></span>, code for <span class=\"h-card\"><a href=\"https://botsin.space/@awoobot\" class=\"u-url mention\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>awoobot</span></a></span>",
      "verified_at": null
    },
    {
      "name": "Website",
      "value": "<a href=\"http://shork.xyz\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">http://</span><span class=\"\">shork.xyz</span><span class=\"invisible\"></span></a>",
      "verified_at": "2019-11-23T20:25:47.907+00:00"
    }
  ]
}
```

###### 정지된 사용자 {#suspended-user}

```json
{
  "id": "14",
  "username": "stigatle",
  "acct": "stigatle@quitter.no",
  "display_name": "",
  "locked": false,
  "bot": false,
  "discoverable": false,
  "group": false,
  "created_at": "2016-03-18T10:04:51.700Z",
  "note": "",
  "url": "https://quitter.no/stigatle",
  "avatar": "https://mastodon.social/avatars/original/missing.png",
  "avatar_static": "https://mastodon.social/avatars/original/missing.png",
  "header": "https://mastodon.social/headers/original/missing.png",
  "header_static": "https://mastodon.social/headers/original/missing.png",
  "followers_count": 0,
  "following_count": 0,
  "statuses_count": 0,
  "last_status_at": null,
  "suspended": true,
  "emojis": [],
  "fields": []
}
```

##### 401: 인증되지 않음 {#401-unauthorized-3}

서버가 허용 목록 모드이며 Authorization 헤더가 없거나 유효하지 않은 경우

```json
{
  "error": "This API requires an authenticated user"
}
```

##### 404: 찾을 수 없음 {#404-not-found}

계정이 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

##### 410: 제거됨 {#410-gone}

계정이 정지되었습니다(2.4.0부터 3.3.0 전까지).

---

## 여러 계정 가져오기 {#index}

```http
GET /api/v1/accounts HTTP/1.1
```

여러 프로필의 정보를 확인합니다.

**반환:** 배열: [Account]({{< relref "entities/Account">}})\
**OAuth:** 공개\
**버전 이력:**\
4.3.0 - 추가

#### 요청 {#request-4}
##### 헤더 {#headers-4}

##### 쿼리 매개변수 {#query-parameters-1}

id[]
: 문자열 배열. 계정 ID입니다.

##### 헤더 {#headers-5}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-4}
##### 200: 성공 {#200-ok-4}

요청한 계정 중 확인과 승인이 완료된 계정의 [Account]({{< relref "entities/Account">}}) 레코드가 반환됩니다. 계정이 없거나 확인되지 않은 경우 요청한 수보다 적은 레코드가 반환될 수 있습니다.

`id=2`인 계정이 없을 때 `id[]=1&id[]=2`를 사용한 호출 예:

```json
[
  {
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
    "followers_count": 318699,
    "following_count": 453,
    "statuses_count": 61013,
    "last_status_at": "2019-11-30T20:02:08.277Z",
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
  }
]
```

##### 401: 인증되지 않음 {#401-unauthorized-4}

서버가 허용 목록 모드이며 Authorization 헤더가 없거나 유효하지 않은 경우

```json
{
  "error": "This API requires an authenticated user"
}
```

---

## 계정의 게시물 가져오기 {#statuses}

```http
GET /api/v1/accounts/:id/statuses HTTP/1.1
```

지정한 계정이 작성한 게시물입니다.

**반환:** 배열: [Status]({{< relref "entities/status">}})\
**OAuth:** 공개(공개 게시물만), 또는 사용자 토큰 + `read:statuses`(사용자에게 열람 권한이 있는 비공개 게시물)\
**버전 이력:**\
0.0.0 - 추가\
1.4.2 - `only_media` 및 `exclude_replies` 추가\
1.6.0 - `pinned` 추가\
2.6.0 - `min_id` 추가\
2.7.0 - `exclude_reblogs` 추가 및 인증 없는 사용 허용\
2.8.0 - `tagged` 매개변수 추가\
3.3.0 - 이제 `min_id`와 `max_id` 동시 사용 가능

#### 요청 {#request-5}
##### 경로 매개변수 {#path-parameters-1}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-6}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-2}

max_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 작습니다. 결과의 상한을 설정합니다.

since_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 큽니다. 결과의 하한을 설정합니다.

min_id
: 문자열. 이 ID보다 바로 다음으로 새로운 결과를 반환합니다. 이 ID에 커서를 설정하고 앞으로 페이지를 이동합니다.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 게시물 20개이며 최대 40개입니다.

only_media
: 불리언. 첨부 파일이 없는 게시물을 제외합니다.

exclude_replies
: 불리언. 다른 계정에 대한 답글인 게시물을 제외합니다.

exclude_reblogs
: 불리언. 응답에서 부스트를 제외합니다.

pinned
: 불리언. 고정된 게시물만 포함합니다. 기본값은 모든 게시물을 포함하는 false입니다. 반환 결과 순서에서 고정된 게시물에 특별한 우선순위를 부여하지 않습니다.

tagged
: 문자열. 특정 해시태그를 사용하는 게시물로 필터링합니다.

#### 응답 {#response-5}
##### 200: 성공 {#200-ok-5}

```json
[
  {
    "id": "108880211901672326",
    "created_at": "2022-08-24T22:29:46.493Z",
    "in_reply_to_id": "108880209317577809",
    "in_reply_to_account_id": "103641",
    "sensitive": false,
    // ...
  },
  // ...
]
```

##### 401: 인증되지 않음 {#401-unauthorized-5}

서버가 허용 목록 모드이며 Authorization 헤더가 없거나 유효하지 않은 경우

허용 목록 모드의 응답 예:

```json
{
  "error": "This API requires an authenticated user"
}
```

2.7.0 이전의 응답 예:

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-1}

계정이 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

##### 410: 제거됨 {#410-gone-1}

계정이 정지되었습니다(2.4.0부터 3.3.0 전까지).

---

## 계정의 팔로워 가져오기 {#followers}

```http
GET /api/v1/accounts/:id/followers HTTP/1.1
```

계정 소유자가 관계망을 숨기지 않은 경우 지정한 계정을 팔로우하는 계정입니다.

**반환:** 배열: [Account]({{< relref "entities/Account">}})\
**OAuth:** 공개\
**버전 이력:**\
0.0.0 - 추가\
3.3.0 - 이제 `min_id`와 `max_id` 동시 사용 가능\
4.0.0 - 더 이상 앱 토큰 + `read:accounts`가 필요하지 않음

#### 요청 {#request-6}
##### 경로 매개변수 {#path-parameters-2}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-7}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-3}

max_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

since_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

min_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 계정 40개이며 최대 80개입니다.

#### 응답 {#response-6}
##### 200: 성공 {#200-ok-6}

limit=2인 출력 예입니다.

```json
[
  {
    "id": "1020382",
    "username": "atul13061987",
    "acct": "atul13061987",
    "display_name": "",
    // ...
  },
  {
    "id": "1020381",
    "username": "linuxliner",
    "acct": "linuxliner",
    "display_name": "",
    // ...
  }
]
```

Follow ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <https://mastodon.example/api/v1/accounts/14715/followers?limit=2&max_id=7486869>; rel="next", <https://mastodon.example/api/v1/accounts/14715/followers?limit=2&since_id=7489740>; rel="prev"
```

##### 401: 인증되지 않음 {#401-unauthorized-6}

Authorization 헤더가 없거나 유효하지 않거나, 서버가 허용 목록 모드이며 토큰에 인증된 사용자가 없는 경우입니다.

허용 목록 모드의 응답 예:

```json
{
  "error": "This API requires an authenticated user"
}
```

헤더가 없거나 토큰이 유효하지 않을 때의 응답 예:

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-2}

계정이 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

##### 410: 제거됨 {#410-gone-2}

계정이 정지되었습니다(2.4.0부터 3.3.0 전까지).

---

## 계정의 팔로잉 가져오기 {#following}

```http
GET /api/v1/accounts/:id/following HTTP/1.1
```

계정 소유자가 관계망을 숨기지 않은 경우 지정한 계정이 팔로우하는 계정입니다.

**반환:** 배열: [Account]({{< relref "entities/Account">}})\
**OAuth:** 공개\
**버전 이력:**\
0.0.0 - 추가\
3.3.0 - 이제 `min_id`와 `max_id` 동시 사용 가능\
4.0.0 - 더 이상 앱 토큰 + `read:accounts`가 필요하지 않음

#### 요청 {#request-7}
##### 경로 매개변수 {#path-parameters-3}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-8}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-4}

max_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

since_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

min_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 계정 40개이며 최대 80개입니다.

#### 응답 {#response-7}
##### 200: 성공 {#200-ok-7}

limit=2인 출력 예입니다.

```json
[
  {
    "id": "963410",
    "username": "gautambhatia",
    "acct": "gautambhatia",
    "display_name": "Gautam Bhatia"
    // ...
  },
  {
    "id": "1007400",
    "username": "seafrog",
    "acct": "seafrog@glitterkitten.co.uk",
    "display_name": "🐓🦃 Heck Partridge 🤠 🦆"
    // ...
  }
]
```

Follow ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <https://mastodon.example/api/v1/accounts/1/followers?limit=2&max_id=7628164>; rel="next", <https://mastodon.example/api/v1/accounts/1/followers?limit=2&since_id=7628165>; rel="prev"
```

##### 401: 인증되지 않음 {#401-unauthorized-7}

Authorization 헤더가 없거나 유효하지 않거나, 서버가 허용 목록 모드이며 토큰에 인증된 사용자가 없는 경우입니다.

허용 목록 모드의 응답 예:

```json
{
  "error": "This API requires an authenticated user"
}
```

헤더가 없거나 토큰이 유효하지 않을 때의 응답 예:

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-3}

계정이 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

##### 410: 제거됨 {#410-gone-3}

계정이 정지되었습니다(2.4.0부터 3.3.0 전까지).

---

## 계정의 추천 태그 가져오기 {#featured_tags}

```http
GET /api/v1/accounts/:id/featured_tags HTTP/1.1
```

이 계정이 추천하는 태그입니다.

**반환:** 배열: [FeaturedTag]({{< relref "entities/featuredtag">}})\
**OAuth:** 공개\
**버전 이력:**\
3.3.0 - 추가

#### 요청 {#request-8}
##### 경로 매개변수 {#path-parameters-4}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-9}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-8}
##### 200: 성공 {#200-ok-8}

```json
[
  {
    "id": "627",
    "name": "nowplaying",
    "statuses_count": 36,
    "last_status_at": "2019-11-15T07:14:43.524Z"
  }
]
```

---

## 이 계정을 포함하는 리스트 가져오기 {#lists}

```http
GET /api/v1/accounts/:id/lists HTTP/1.1
```

이 계정을 추가한 사용자의 리스트입니다.

**반환:** 배열: [List]({{< relref "entities/list">}})\
**OAuth:** 사용자 토큰 + `read:lists`\
**버전 이력:**\
2.1.0 - 추가

#### 요청 {#request-9}
##### 경로 매개변수 {#path-parameters-5}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-10}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-9}
##### 200: 성공 {#200-ok-9}

계정이 리스트에 포함되어 있으면 해당 엔터티를 반환합니다. 계정이 내 리스트 어디에도 포함되어 있지 않으면 빈 배열을 반환합니다.

```json
[
  {
    "id": "13694",
    "title": "dev"
  }
]
```

```json
[]
```

##### 401: 인증되지 않음 {#401-unauthorized-8}

Authorization 헤더가 없거나 유효하지 않거나, 서버가 허용 목록 모드이며 토큰에 인증된 사용자가 없는 경우입니다.

허용 목록 모드의 응답 예:

```json
{
  "error": "This API requires an authenticated user"
}
```

헤더가 없거나 토큰이 유효하지 않을 때의 응답 예:

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-4}

계정이 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

##### 410: 제거됨 {#410-gone-4}

계정이 정지되었습니다(2.4.0부터 3.3.0 전까지).

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-3}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 계정 팔로우 {#follow}

```http
POST /api/v1/accounts/:id/follow HTTP/1.1
```

지정한 계정을 팔로우합니다. 부스트 표시 여부나 알림 활성화 여부를 수정하는 데도 사용할 수 있습니다.

**반환:** [Relationship]({{< relref "entities/relationship">}})\
**OAuth:** 사용자 토큰 + `write:follows`\
**버전 이력:**\
0.0.0 - 추가\
3.3.0 - `notify` 추가\
3.5.0 - `follow` 범위 사용 중단 예정. 이제 `write`도 추가로 허용\
4.0.0 - `languages` 추가

#### 요청 {#request-10}
##### 경로 매개변수 {#path-parameters-6}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-11}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-2}

reblogs
: 불리언. 홈 타임라인에서 이 계정의 부스트를 받을지 여부입니다. 기본값은 true입니다.

notify
: 불리언. 이 계정이 게시물을 작성하면 알림을 받을지 여부입니다. 기본값은 false입니다.

languages[]
: 문자열 배열(ISO 639-1 두 글자 언어 코드). 수신할 게시물을 이 언어들로 필터링합니다. 생략하면 이 계정이 작성한 모든 언어의 게시물을 받습니다.

#### 응답 {#response-10}
##### 200: 성공 {#200-ok-10}

팔로우에 성공했거나 이미 팔로우 중입니다.

```json
{
  "id": "3",
  "following": true,
  "showing_reblogs": false,
  "notifying": false,
  "followed_by": false,
  "blocking": false,
  "blocked_by": false,
  "muting": false,
  "muting_notifications": false,
  "requested": false,
  "domain_blocking": false,
  "endorsed": false
}
```

##### 403: 금지됨 {#403-forbidden-1}

차단한 계정 또는 나를 차단한 계정을 팔로우하려는 경우입니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-4}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 계정 팔로우 해제 {#unfollow}

```http
POST /api/v1/accounts/:id/unfollow HTTP/1.1
```

지정한 계정의 팔로우를 해제합니다.

**반환:** [Relationship]({{< relref "entities/relationship">}})\
**OAuth:** 사용자 토큰 + `write:follows`\
**버전 이력:**\
0.0.0 - 추가\
3.5.0 - `follow` 범위 사용 중단 예정. 이제 `write`도 추가로 허용

#### 요청 {#request-11}
##### 경로 매개변수 {#path-parameters-7}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-12}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-11}
##### 200: 성공 {#200-ok-11}

팔로우 해제에 성공했거나 이미 팔로우하지 않는 상태입니다.

```json
{
  "id": "3",
  "following": false,
  "showing_reblogs": false,
  "notifying": false,
  "followed_by": false,
  "blocking": false,
  "blocked_by": false,
  "muting": false,
  "muting_notifications": false,
  "requested": false,
  "domain_blocking": false,
  "endorsed": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-9}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-5}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 팔로워에서 계정 제거 {#remove_from_followers}

```http
POST /api/v1/accounts/:id/remove_from_followers HTTP/1.1
```

팔로워에서 지정한 계정을 제거합니다.

**반환:** [Relationship]({{< relref "entities/relationship">}})\
**OAuth:** 사용자 토큰 + `write:follows`\
**버전 이력:**\
3.5.0 - 추가

#### 요청 {#request-12}
##### 경로 매개변수 {#path-parameters-8}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-13}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-12}
##### 200: 성공 {#200-ok-12}

팔로워에서 제거했거나 해당 계정이 이미 나를 팔로우하지 않는 상태입니다.

```json
{
  "id": "3",
  "following": false,
  "showing_reblogs": false,
  "notifying": false,
  "followed_by": false,
  "blocking": false,
  "blocked_by": false,
  "muting": false,
  "muting_notifications": false,
  "requested": false,
  "domain_blocking": false,
  "endorsed": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-10}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-6}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 계정 차단 {#block}

```http
POST /api/v1/accounts/:id/block HTTP/1.1
```

지정한 계정을 [차단]({{< relref "user/moderating#block">}})합니다.

{{< hint style="info" >}} 차단이 사용자의 타임라인에 적용되기 전에 호출이 반환될 수 있습니다. 클라이언트는 캐시된 타임라인 사본에서 차단한 계정을 제거하고 잠시 클라이언트 내에서 차단을 적용할 수 있습니다.
{{< /hint >}}

**반환:** [Relationship]({{< relref "entities/relationship">}})\
**OAuth:** 사용자 토큰 + `write:blocks`\
**버전 이력:**\
0.0.0 - 추가\
3.5.0 - `follow` 범위 사용 중단 예정. 이제 `write`도 추가로 허용

#### 요청 {#request-13}
##### 경로 매개변수 {#path-parameters-9}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-14}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-13}
##### 200: 성공 {#200-ok-13}

차단에 성공했거나 이미 차단된 계정입니다.

```json
{
  "id": "3",
  "following": false,
  "showing_reblogs": false,
  "notifying": false,
  "followed_by": false,
  "blocking": true,
  "blocked_by": false,
  "muting": false,
  "muting_notifications": false,
  "requested": false,
  "domain_blocking": false,
  "endorsed": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-11}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-7}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 계정 차단 해제 {#unblock}

```http
POST /api/v1/accounts/:id/unblock HTTP/1.1
```

지정한 계정의 차단을 해제합니다.

**반환:** [Relationship]({{< relref "entities/relationship">}})\
**OAuth:** 사용자 토큰 + `write:blocks`\
**버전 이력:**\
0.0.0 - 추가\
3.5.0 - `follow` 범위 사용 중단 예정. 이제 `write`도 추가로 허용

#### 요청 {#request-14}
##### 경로 매개변수 {#path-parameters-10}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-15}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-14}
##### 200: 성공 {#200-ok-14}

차단 해제에 성공했거나 이미 차단되지 않은 상태입니다.

```json
{
  "id": "3",
  "following": false,
  "showing_reblogs": false,
  "notifying": false,
  "followed_by": false,
  "blocking": false,
  "blocked_by": false,
  "muting": false,
  "muting_notifications": false,
  "requested": false,
  "domain_blocking": false,
  "endorsed": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-12}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-8}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 계정 뮤트 {#mute}

```http
POST /api/v1/accounts/:id/mute HTTP/1.1
```

지정한 계정을 뮤트합니다. 클라이언트는 이 계정의 게시물과 알림을 수신하면(예: 홈 타임라인의 부스트를 통해) 이를 필터링해야 합니다.

**반환:** [Relationship]({{< relref "entities/relationship">}})\
**OAuth:** 사용자 토큰 + `write:mutes`\
**버전 이력:**\
0.0.0 - 추가\
3.3.0 - `duration` 추가\
3.5.0 - `follow` 범위 사용 중단 예정. 이제 `write`도 추가로 허용

#### 요청 {#request-15}
##### 경로 매개변수 {#path-parameters-11}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-16}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-3}

notifications
: 불리언. 게시물과 함께 알림도 뮤트할지 여부입니다. 기본값은 true입니다.

duration
: 숫자. 뮤트를 유지할 시간(초)입니다. 기본값은 0(무기한)입니다.

#### 응답 {#response-15}
##### 200: 성공 {#200-ok-15}

뮤트에 성공했거나 이미 뮤트된 계정입니다. notifications=false로 이 API 메서드를 다시 호출하여 게시물만 뮤트하도록 관계를 수정할 수 있습니다.

```json
{
  "id": "3",
  "following": false,
  "showing_reblogs": false,
  "notifying": false,
  "followed_by": false,
  "blocking": false,
  "blocked_by": false,
  "muting": true,
  "muting_notifications": true,
  "requested": false,
  "domain_blocking": false,
  "endorsed": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-13}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-9}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 계정 뮤트 해제 {#unmute}

```http
POST /api/v1/accounts/:id/unmute HTTP/1.1
```

지정한 계정의 뮤트를 해제합니다.

**반환:** [Relationship]({{< relref "entities/relationship">}})\
**OAuth:** 사용자 토큰 + `write:mutes`\
**버전 이력:**\
0.0.0 - 추가\
3.5.0 - `follow` 범위 사용 중단 예정. 이제 `write`도 추가로 허용

#### 요청 {#request-16}
##### 경로 매개변수 {#path-parameters-12}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-17}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-16}
##### 200: 성공 {#200-ok-16}

뮤트 해제에 성공했거나 이미 뮤트되지 않은 상태입니다.

```json
{
  "id": "3",
  "following": false,
  "showing_reblogs": false,
  "notifying": false,
  "followed_by": false,
  "blocking": false,
  "blocked_by": false,
  "muting": false,
  "muting_notifications": false,
  "requested": false,
  "domain_blocking": false,
  "endorsed": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-14}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-10}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 프로필에서 계정 추천 {{%deprecated%}} {#pin}

```http
POST /api/v1/accounts/:id/pin HTTP/1.1
```

사용자의 추천 프로필에 지정한 계정을 추가합니다. (추천 프로필은 현재 사용자 본인의 공개 프로필에 표시됩니다.)

**반환:** [Relationship]({{< relref "entities/relationship">}})\
**OAuth:** 사용자 토큰 + `write:accounts`\
**버전 이력:**\
2.5.0 - 추가\
4.0.0 - 이제 이 메서드 호출은 멱등적임\
4.4.0 - `/api/v1/accounts/:id/endorse`를 권장하며 사용 중단 예정

#### 요청 {#request-17}
##### 경로 매개변수 {#path-parameters-13}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-18}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-17}
##### 200: 성공 {#200-ok-17}

추천에 성공했거나 이미 추천 중입니다.

```json
{
  "id": "1",
  "following": true,
  "showing_reblogs": true,
  "notifying": false,
  "followed_by": true,
  "blocking": false,
  "blocked_by": false,
  "muting": false,
  "muting_notifications": false,
  "requested": false,
  "domain_blocking": false,
  "endorsed": true
}
```

##### 401: 인증되지 않음 {#401-unauthorized-15}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 403: 금지됨 {#403-forbidden-2}

토큰에 필수 범위가 없습니다.

```json
{
  "error": "This action is outside the authorized scopes"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-11}

이 계정을 팔로우하고 있지 않습니다.

```json
{
  "error": "Validation failed: You must be already following the person you want to endorse"
}
```

또는 토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

또는 (4.0 이전에는) 계정이 이미 추천되어 있을 수 있습니다.

```json
{
  "error": "Duplicate record"
}
```

##### 500: 서버 오류 {#500-server-error}

계정이 이미 추천된 경우 간혹 반환될 수 있습니다.

---

## 프로필에서 계정 추천 해제 {{%deprecated%}} {#unpin}

```http
POST /api/v1/accounts/:id/unpin HTTP/1.1
```

사용자의 추천 프로필에서 지정한 계정을 제거합니다.

**반환:** [Relationship]({{< relref "entities/relationship">}})\
**OAuth:** 사용자 + `write:accounts`\
**버전 이력:**\
2.5.0 - 추가\
4.4.0 - `/api/v1/accounts/:id/unendorse`를 권장하며 사용 중단 예정

#### 요청 {#request-18}
##### 경로 매개변수 {#path-parameters-14}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-19}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-18}
##### 200: 성공 {#200-ok-18}

추천 해제에 성공했거나 이미 추천하지 않는 계정입니다.

```json
{
  "id": "1",
  "following": true,
  "showing_reblogs": true,
  "notifying": false,
  "followed_by": true,
  "blocking": false,
  "blocked_by": false,
  "muting": false,
  "muting_notifications": false,
  "requested": false,
  "domain_blocking": false,
  "endorsed": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-16}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-12}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 추천 계정 가져오기 {#endorsements}

```http
GET /api/v1/accounts/:id/endorsements HTTP/1.1
```

현재 사용자가 프로필에서 추천하는 계정입니다.

**반환:** 배열: [Account]({{< relref "entities/account" >}})\
**OAuth:** 공개\
**버전 이력:**\
4.4.0 - 추가

#### 요청 {#request-19}
##### 경로 매개변수 {#path-parameters-15}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-20}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-5}

max_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

since_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 계정 40개이며 최대 80개입니다.

#### 응답 {#response-19}
##### 200: 성공 {#200-ok-19}

limit=2인 호출 예입니다.

```json
[
  {
    "id": "952529",
    "username": "alayna",
    "acct": "alayna@desvox.es",
    "display_name": "Alayna Desirae",
    "locked": true,
    "bot": false,
    "created_at": "2019-10-26T23:12:06.570Z",
    "note": "experiencing ________ difficulties<br>22y/o INFP in Oklahoma",
    "url": "https://desvox.es/users/alayna",
    "avatar": "https://files.mastodon.social/accounts/avatars/000/952/529/original/6534122046d050d5.png",
    "avatar_static": "https://files.mastodon.social/accounts/avatars/000/952/529/original/6534122046d050d5.png",
    "header": "https://files.mastodon.social/accounts/headers/000/952/529/original/496f1f817e042ade.png",
    "header_static": "https://files.mastodon.social/accounts/headers/000/952/529/original/496f1f817e042ade.png",
    "followers_count": 0,
    "following_count": 0,
    "statuses_count": 955,
    "last_status_at": "2019-11-23T07:05:50.682Z",
    "emojis": [],
    "fields": []
  },
  {
    "id": "832844",
    "username": "a9",
    "acct": "a9@broadcast.wolfgirl.engineering",
    "display_name": "vivienne :collar: ",
    "locked": true,
    "bot": false,
    "created_at": "2019-06-12T18:55:12.053Z",
    "note": "borderline nsfw, considered a schedule I drug by nixon<br>waiting for the year of the illumos desktop",
    "url": "https://broadcast.wolfgirl.engineering/users/a9",
    "avatar": "https://files.mastodon.social/accounts/avatars/000/832/844/original/ae1de0b8fb63d1c6.png",
    "avatar_static": "https://files.mastodon.social/accounts/avatars/000/832/844/original/ae1de0b8fb63d1c6.png",
    "header": "https://files.mastodon.social/accounts/headers/000/832/844/original/5088e4a16e6d8736.png",
    "header_static": "https://files.mastodon.social/accounts/headers/000/832/844/original/5088e4a16e6d8736.png",
    "followers_count": 43,
    "following_count": 67,
    "statuses_count": 5906,
    "last_status_at": "2019-11-23T05:23:47.911Z",
    "emojis": [
      {
        "shortcode": "collar",
        "url": "https://files.mastodon.social/custom_emojis/images/000/106/920/original/80953b9cd96ec4dc.png",
        "static_url": "https://files.mastodon.social/custom_emojis/images/000/106/920/static/80953b9cd96ec4dc.png",
        "visible_in_picker": true
      }
    ],
    "fields": []
  }
]
```

AccountPin ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <https://mastodon.example/api/v1/accounts/1/endorsements?limit=2&max_id=832844>; rel="next", <https://mastodon.example/api/v1/accounts/1/endorsements?limit=2&since_id=952529>; rel="prev"
```

##### 401: 인증되지 않음 {#401-unauthorized-17}

서버가 허용 목록 모드이며 Authorization 헤더가 없거나 유효하지 않은 경우

```json
{
  "error": "This API requires an authenticated user"
}
```

##### 404: 찾을 수 없음 {#404-not-found-5}

계정이 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---
## 프로필에서 계정 추천 {#endorse}

```http
POST /api/v1/accounts/:id/endorse HTTP/1.1
```

사용자의 추천 프로필에 지정한 계정을 추가합니다.

**반환:** [Relationship]({{< relref "entities/relationship">}})\
**OAuth:** 사용자 토큰 + `write:accounts`\
**버전 이력:**\
4.4.0 - 추가

#### 요청 {#request-20}
##### 경로 매개변수 {#path-parameters-16}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-21}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-20}
##### 200: 성공 {#200-ok-20}

추천에 성공했거나 이미 추천 중입니다.

```json
{
  "id": "1",
  "following": true,
  "showing_reblogs": true,
  "notifying": false,
  "followed_by": true,
  "blocking": false,
  "blocked_by": false,
  "muting": false,
  "muting_notifications": false,
  "requested": false,
  "domain_blocking": false,
  "endorsed": true
}
```

##### 401: 인증되지 않음 {#401-unauthorized-18}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 403: 금지됨 {#403-forbidden-3}

토큰에 필수 범위가 없습니다.

```json
{
  "error": "This action is outside the authorized scopes"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-13}

이 계정을 팔로우하고 있지 않습니다.

```json
{
  "error": "Validation failed: You must be already following the person you want to endorse"
}
```

또는 토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

또는 (4.0 이전에는) 계정이 이미 추천되어 있을 수 있습니다.

```json
{
  "error": "Duplicate record"
}
```

##### 500: 서버 오류 {#500-server-error-1}

계정이 이미 추천된 경우 간혹 반환될 수 있습니다.

---

## 프로필에서 계정 추천 해제 {#unendorse}

```http
POST /api/v1/accounts/:id/unendorse HTTP/1.1
```

사용자의 추천 프로필에서 지정한 계정을 제거합니다.

**반환:** [Relationship]({{< relref "entities/relationship">}})\
**OAuth:** 사용자 + `write:accounts`\
**버전 이력:**\
4.4.0 - 추가

#### 요청 {#request-21}
##### 경로 매개변수 {#path-parameters-17}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-22}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-21}
##### 200: 성공 {#200-ok-21}

추천 해제에 성공했거나 이미 추천하지 않는 계정입니다.

```json
{
  "id": "1",
  "following": true,
  "showing_reblogs": true,
  "notifying": false,
  "followed_by": true,
  "blocking": false,
  "blocked_by": false,
  "muting": false,
  "muting_notifications": false,
  "requested": false,
  "domain_blocking": false,
  "endorsed": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-19}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-14}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 프로필에 비공개 메모 설정 {#note}

```http
POST /api/v1/accounts/:id/note HTTP/1.1
```

사용자에 대한 비공개 메모를 설정합니다.

**반환:** [Relationship]({{< relref "entities/relationship">}})\
**OAuth:** 사용자 + `write:accounts`\
**버전 이력:**\
3.2.0 - 추가

#### 요청 {#request-22}
##### 경로 매개변수 {#path-parameters-18}

:id
: {{<required>}} 문자열. 계정 ID입니다.

##### 헤더 {#headers-23}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-4}

comment
: 문자열. 해당 사용자에 설정할 메모입니다. 빈 문자열을 제공하거나 이 매개변수를 생략하면 기존 메모를 지웁니다.

#### 응답 {#response-22}
##### 200: 성공 {#200-ok-22}

프로필 메모를 수정했습니다.

```json
{
  "id": "1",
  "following": true,
  "showing_reblogs": true,
  "notifying": false,
  "followed_by": true,
  "blocking": false,
  "blocked_by": false,
  "muting": false,
  "muting_notifications": false,
  "requested": false,
  "domain_blocking": false,
  "endorsed": false,
  "note": "this is a comment"
}
```

프로필 메모를 제거했습니다.

```json
{
  "id": "1",
  "following": true,
  "showing_reblogs": true,
  "notifying": false,
  "followed_by": true,
  "blocking": false,
  "blocked_by": false,
  "muting": false,
  "muting_notifications": false,
  "requested": false,
  "domain_blocking": false,
  "endorsed": false,
  "note": ""
}
```

##### 401: 인증되지 않음 {#401-unauthorized-20}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-15}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 다른 계정과의 관계 확인 {#relationships}

```http
GET /api/v1/accounts/relationships HTTP/1.1
```

지정한 계정을 팔로우, 차단, 뮤트하는지 등을 확인합니다.

**반환:** 배열: [Relationship]({{< relref "entities/Relationship">}})\
**OAuth:** 사용자 토큰 + `read:follows`\
**버전 이력:**\
0.0.0 - 추가\
4.3.0 - `with_suspended` 매개변수 추가
4.6.0 - `muting_expires_at` 추가

#### 요청 {#request-23}
##### 헤더 {#headers-24}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-6}

id[]
: 문자열 배열. 제공한 계정 ID에 대한 관계를 확인합니다.

with_suspended
: 불리언. 정지된 사용자에 대한 관계도 반환할지 여부입니다. 기본값은 false입니다.

#### 응답 {#response-23}
##### 200: 성공 {#200-ok-23}

`id[]=1&id[]=2`인 호출 예입니다.

```json
[
  {
    "id": "1",
    "following": true,
    "showing_reblogs": true,
    "notifying": false,
    "followed_by": true,
    "blocking": false,
    "blocked_by": false,
    "muting": false,
    "muting_notifications": false,
    "muting_expires_at": null,
    "requested": false,
    "domain_blocking": false,
    "endorsed": false
  },
  {
    "id": "2",
    "following": false,
    "showing_reblogs": false,
    "notifying": false,
    "followed_by": false,
    "blocking": false,
    "blocked_by": false,
    "muting": false,
    "muting_notifications": false,
    "muting_expires_at": "2026-02-12T13:45:25Z",
    "requested": false,
    "domain_blocking": false,
    "endorsed": false
  }
]
```

##### 401: 인증되지 않음 {#401-unauthorized-21}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-16}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 아는 팔로워 찾기 {#familiar_followers}

```http
GET /api/v1/accounts/familiar_followers HTTP/1.1
```

지정한 계정을 팔로우하는 모든 계정 중 내가 팔로우하는 계정만 필터링한 목록을 가져옵니다.

**반환:** 배열: [FamiliarFollowers]({{< relref "entities/FamiliarFollowers">}})\
**OAuth:** 사용자 토큰 + `read:follows`\
**버전 이력:**\
3.5.0 - 추가

#### 요청 {#request-24}
##### 헤더 {#headers-25}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-7}

id[]
: 문자열 배열. 제공한 계정 ID의 아는 팔로워를 찾습니다.

#### 응답 {#response-24}
##### 200: 성공 {#200-ok-24}

`id[]=1&id[]=2`인 호출 예입니다.

```json
[
  {
    "id":"1",
    "accounts":[
      {
        "id":"1087990",
        "username":"moss",
        "acct":"moss@goblin.camp",
        // ...
      },
      {
        "id":"1092723",
        "username":"vivianrose",
        "acct":"vivianrose",
        // ...
      },
      // ...
    ]
  },
  {
    "id":"2",
    "accounts":[]
  }
]
```

##### 401: 인증되지 않음 {#401-unauthorized-22}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-17}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 일치하는 계정 검색 {#search}

```http
GET /api/v1/accounts/search HTTP/1.1
```

사용자명 또는 표시 이름으로 일치하는 계정을 검색합니다.

**반환:** 배열: [Account]({{< relref "entities/Account">}})\
**OAuth:** 사용자 토큰 + `read:accounts`\
**버전 이력:**\
0.0.0 - 추가\
2.8.0 - `limit`, `offset`, `following` 추가

#### 요청 {#request-25}
##### 헤더 {#headers-26}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-8}

q
: {{<required>}} 문자열. 계정 검색어입니다.

limit
: 정수. 최대 결과 수입니다. 기본값은 계정 40개이며 최대 80개입니다.

offset
: 정수. 처음 n개 결과를 건너뜁니다.

resolve
: 불리언. WebFinger 조회를 시도합니다. 기본값은 false입니다. `q`가 정확한 주소일 때 사용하세요.

following
: 불리언. 팔로우하는 사용자로 검색을 제한합니다. 기본값은 false입니다.

#### 응답 {#response-25}
##### 200: 성공 {#200-ok-25}

사용자명 또는 표시 이름에 "trwnh"가 일치하는 계정입니다.

```json
[
  {
    "id": "14715",
    "username": "trwnh",
    "acct": "trwnh",
    "display_name": "infinite love ⴳ",
    // ...
  },
  {
    "id": "418714",
    "username": "trwnh",
    "acct": "trwnh@pixelfed.social",
    "display_name": "Abdullah Tarawneh",
    // ...
  },
  {
    "id": "419674",
    "username": "trwnh",
    "acct": "trwnh@write.as",
    "display_name": "trwnh",
    // ...
  },
  // ...
]
```

##### 503: 서비스 이용 불가 {#503-service-unavailable}

resolve=true이지만 user@domain 주소의 도메인 부분이 현재 접속 가능한 웹사이트가 아닌 경우입니다.

```json
{
  "error": "Remote data could not be fetched"
}
```

---

## WebFinger 주소로 계정 ID 조회 {#lookup}

```http
GET /api/v1/accounts/lookup HTTP/1.1
```

WebFinger 해석을 생략하고 사용자명을 빠르게 조회하여 사용 가능한지 확인합니다.

**반환:** [Account]({{< relref "entities/Account">}})\
**OAuth:** 사용자 토큰 + `read:accounts`\
**버전 이력:**\
3.4.0 - 추가

#### 요청 {#request-26}
##### 쿼리 매개변수 {#query-parameters-9}

acct
: {{<required>}} 문자열. 조회할 사용자명 또는 WebFinger 주소입니다.

#### 응답 {#response-26}
##### 200: 성공 {#200-ok-26}

`?acct=trwnh`인 호출 예입니다.

```json
{
  "id": "14715",
  "username": "trwnh",
  "acct": "trwnh",
  "display_name": "infinite love ⴳ",
  "locked": false,
  // ...
}
```

`?acct=trwnh@pixelfed.social`인 호출 예입니다.

```json
{
  "id": "418714",
  "username": "trwnh",
  "acct": "trwnh@pixelfed.social",
  "display_name": "Abdullah Tarawneh",
  "locked": false,
  // ...
}
```

##### 404: 찾을 수 없음 {#404-not-found-6}

사용자명 또는 주소에 대응하는 계정이 없습니다.

```json
{
  "error": "Record not found"
}
```

---

## 신원 증명 {{%deprecated%}} {#identity_proofs}

```http
GET /api/v1/accounts/:id/identity_proofs HTTP/1.1
```

**반환:** 배열: [IdentityProof]({{< relref "entities/identityproof">}})\
**OAuth:** 사용자 토큰\
**버전 이력:**\
2.8.0 - 추가\
3.5.0 - 사용 중단 예정. 이제 빈 배열 반환.

#### 요청 {#request-27}

##### 경로 매개변수 {#path-parameters-19}

:id
: {{<required>}} 문자열. 계정 ID입니다.

#### 응답 {#response-27}
##### 200: 성공 {#200-ok-27}

```json
[
  {
    "provider": "Keybase",
    "provider_username": "gargron",
    "updated_at": "2019-07-21T20:14:39.596Z",
    "proof_url": "https://keybase.io/gargron/sigchain#5cfc20c7018f2beefb42a68836da59a792e55daa4d118498c9b1898de7e845690f",
    "profile_url": "https://keybase.io/gargron"
  }
]
```

##### 404: 찾을 수 없음 {#404-not-found-7}

계정이 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

##### 410: 제거됨 {#410-gone-5}

계정이 정지되었습니다(2.4.0부터 3.3.0 전까지).

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-18}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/accounts_controller.rb" caption="app/controllers/api/v1/accounts_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/accounts/credentials_controller.rb" caption="app/controllers/api/v1/accounts/credentials_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/accounts/familiar_followers_controller.rb" caption="app/controllers/api/v1/accounts/familiar_followers_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/accounts/featured_tags_controller.rb" caption="app/controllers/api/v1/accounts/featured_tags_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/accounts/follower_accounts_controller.rb" caption="app/controllers/api/v1/accounts/follower_accounts_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/accounts/following_accounts_controller.rb" caption="app/controllers/api/v1/accounts/following_accounts_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/accounts/identity_proofs_controller.rb" caption="app/controllers/api/v1/accounts/identity_proofs_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/accounts/lists_controller.rb" caption="app/controllers/api/v1/accounts/lists_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/accounts/lookup_controller.rb" caption="app/controllers/api/v1/accounts/lookup_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/accounts/notes_controller.rb" caption="app/controllers/api/v1/accounts/notes_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/accounts/pins_controller.rb" caption="app/controllers/api/v1/accounts/pins_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/accounts/relationships_controller.rb" caption="app/controllers/api/v1/accounts/relationships_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/accounts/search_controller.rb" caption="app/controllers/api/v1/accounts/search_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/accounts/statuses_controller.rb" caption="app/controllers/api/v1/accounts/statuses_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/models/account_statuses_filter.rb" caption="app/models/account_statuses_filter.rb" >}}
