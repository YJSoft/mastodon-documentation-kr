---
title: 계정 (Account)
description: 마스토돈 사용자와 연결된 프로필을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/source/",
  "/entities/Source/",
  "/entities/field/",
  "/entities/Field/",
  "/entities/account",
  "/entities/Account",
  "/entities/credentialaccount",
  "/entities/CredentialAccount",
  "/entities/mutedaccount",
  "/entities/MutedAccount",
  "/entities/partialaccountwithavatar",
  "/entities/PartialAccountWithAvatar",
  "/api/entities/source/",
  "/api/entities/Source/",
  "/api/entities/field/",
  "/api/entities/Field/",
  "/api/entities/account",
  "/api/entities/Account",
  "/api/entities/credentialaccount",
  "/api/entities/CredentialAccount",
  "/api/entities/mutedaccount",
  "/api/entities/MutedAccount",
  "/api/entities/partialaccountwithavatar",
  "/api/entities/PartialAccountWithAvatar",
]
---

## 예시 {#example}

```json
{
  "id": "23634",
  "username": "noiob",
  "acct": "noiob@awoo.space",
  "display_name": "ikea shark fan account",
  "locked": false,
  "bot": false,
  "created_at": "2017-02-08T02:00:53.274Z",
  "note": "<p>:ms_rainbow_flag:​ :ms_bisexual_flagweb:​ :ms_nonbinary_flag:​ <a href=\"https://awoo.space/tags/awoo\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>awoo</span></a>.space <a href=\"https://awoo.space/tags/admin\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>admin</span></a> ~ <a href=\"https://awoo.space/tags/bi\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>bi</span></a> ~ <a href=\"https://awoo.space/tags/nonbinary\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>nonbinary</span></a> ~ compsci student ~ likes video <a href=\"https://awoo.space/tags/games\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>games</span></a> and weird/ old electronics and will post obsessively about both ~ avatar by <span class=\"h-card\"><a href=\"https://weirder.earth/@dzuk\" class=\"u-url mention\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>dzuk</span></a></span></p>",
  "url": "https://awoo.space/@noiob",
  "avatar": "https://files.mastodon.social/accounts/avatars/000/023/634/original/6ca8804dc46800ad.png",
  "avatar_static": "https://files.mastodon.social/accounts/avatars/000/023/634/original/6ca8804dc46800ad.png",
  "avatar_description": "a shark",
  "header": "https://files.mastodon.social/accounts/headers/000/023/634/original/256eb8d7ac40f49a.png",
  "header_static": "https://files.mastodon.social/accounts/headers/000/023/634/original/256eb8d7ac40f49a.png",
  "header_description": "sharks in the sea",
  "followers_count": 547,
  "following_count": 404,
  "statuses_count": 28468,
  "last_status_at": "2019-11-17",
  "indexable": true,
  "show_media": true,
  "show_media_replies": true,
  "show_featured": true,
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
      "value": "<span class=\"h-card\"><a href=\"https://botsin.space/@darksouls\" class=\"u-url mention\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>darksouls</span></a></span>, <span class=\"h-card\"><a href=\"https://botsin.space/@nierautomata\" class=\"u-url mention\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>nierautomata</span></a></span>, <span class=\"h-card\"><a href=\"https://mastodon.social/@fedi\" class=\"u-url mention\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>fedi</span></a></span>, code for <span class=\"h-card\"><a href=\"https://botsin.space/@awoobot\" class=\"u-url mention\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>awoobot</span></a></span>",
      "verified_at": null
    },
    {
      "name": "Website",
      "value": "<a href=\"http://shork.xyz\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">http://</span><span class=\"\">shork.xyz</span><span class=\"invisible\"></span></a>",
      "verified_at": "2019-11-10T10:31:10.744+00:00"
    }
  ],
  "feature_approval": {
    "automatic": [ "public" ],
    "manual": [],
    "current_user": "automatic"
  }
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 계정 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
0.1.0 - 추가

### `username` {#username}

**설명:** 도메인을 제외한 계정 사용자명입니다.\
**유형:** 문자열\
**버전 이력:**\
0.1.0 - 추가

### `acct` {#acct}

**설명:** WebFinger 계정 URI입니다. 로컬 사용자는 `username`, 원격 사용자는 `username@domain`과 같습니다.\
**유형:** 문자열\
**버전 이력:**\
0.1.0 - 추가

### `url` {#url}

**설명:** 사용자 프로필 페이지의 위치입니다(웹 인터페이스 URL).\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
0.1.0 - 추가

### `uri` {#uri}

**설명:** 사용자의 ActivityPub 행위자 식별자입니다(연합에 사용).\
**유형:** 문자열 (URL)\
**버전 이력:**\
4.2.0 - 추가

### `display_name` {#display_name}

**설명:** 프로필의 표시 이름입니다.\
**유형:** 문자열\
**버전 이력:**\
0.1.0 - 추가

### `note` {#note}

**설명:** 프로필의 소개 또는 설명입니다.\
**유형:** 문자열 (HTML)\
**버전 이력:**\
0.1.0 - 추가

### `avatar` {#avatar}

**설명:** 게시물 옆과 프로필에 표시하는 아이콘 이미지입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
0.1.0 - 추가

### `avatar_static` {#avatar_static}

**설명:** 아바타의 정적 버전입니다. `avatar`가 정적 이미지이면 같은 값이며, `avatar`가 애니메이션 GIF이면 다른 값입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
1.1.2 - 추가

### `avatar_description` {#avatar_description}

**설명:** 아바타 이미지의 텍스트 설명입니다.\
**유형:** 문자열\
**버전 이력:**\
4.6.0 - 추가

### `header` {#header}

**설명:** 프로필 위와 프로필 카드에 표시하는 배너 이미지입니다. 사용자가 헤더 이미지를 설정하지 않으면 `/headers/original/missing.png`로 끝납니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
0.1.0 - 추가

### `header_static` {#header_static}

**설명:** 헤더의 정적 버전입니다. `header`가 정적 이미지이면 같은 값이며, `header`가 애니메이션 GIF이면 다른 값입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
1.1.2 - 추가

### `header_description` {#header_description}

**설명:** 헤더 이미지의 텍스트 설명입니다.\
**유형:** 문자열\
**버전 이력:**\
4.6.0 - 추가

### `locked` {#locked}

**설명:** 계정이 팔로우 요청을 수동으로 승인하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
0.1.0 - 추가

### `fields` {#fields}

**설명:** 이름-값 쌍으로 프로필에 첨부한 추가 메타데이터입니다.\
**유형:** 배열: [Field](#Field)\
**버전 이력:**\
2.4.0 - 추가

### `emojis` {#emojis}

**설명:** 프로필을 렌더링할 때 사용할 사용자 지정 이모지 엔터티입니다.\
**유형:** 배열: [CustomEmoji]({{< relref "entities/CustomEmoji" >}})\
**버전 이력:**\
2.4.0 - 추가

### `bot` {#bot}

**설명:** 계정이 자동 동작을 수행하거나, 관리되지 않거나, 로봇임을 나타냅니다. 계정의 `actor_type`이 'Application' 또는 'Service'로 설정되어 있는지에 따라 결정합니다.\
**유형:** 불리언\
**버전 이력:**\
2.4.0 - 추가

### `group` {#group}

**설명:** 계정이 Group 행위자를 나타내는지 표시합니다.\
**유형:** 불리언\
**버전 이력:**\
3.1.0 - 추가

### `discoverable` {#discoverable}

**설명:** 계정이 프로필 디렉터리 같은 발견 기능에 참여하는지 나타냅니다.\
**유형:** {{<nullable>}} 불리언\
**버전 이력:**\
3.1.0 - 추가

### `indexable` {#indexable}

**설명:** 계정이 검색 엔진의 색인 생성을 허용하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.3.0 - 추가

### `noindex` {{%optional%}} {#noindex}

**설명:** 로컬 사용자가 검색 엔진의 색인 생성을 거부했는지 나타냅니다.\
**유형:** {{<nullable>}} 불리언\
**버전 이력:**\
4.0.0 - 추가

### `moved` {{%optional%}} {#moved}

**설명:** 프로필이 현재 비활성 상태이며 사용자가 새 계정으로 이주했음을 나타냅니다.\
**유형:** {{<nullable>}} [Account]({{< relref "entities/Account" >}}), 프로필이 이전하지 않았거나 정지되었으면 null\
**버전 이력:**\
2.1.0 - 추가

### `memorial` {{%optional%}} {#memorial}

**설명:** 계정을 추모 계정으로 지정했을 때만 반환하는 추가 속성입니다(`memorial`이 true인 경우).\
**유형:** 불리언\
**버전 이력:**\
4.2.0 - 추가

### `suspended` {{%optional%}} {#suspended}

**설명:** 계정이 정지되었을 때만 반환하는 추가 속성입니다.\
**유형:** 불리언\
**버전 이력:**\
3.3.0 - 추가

### `limited` {{%optional%}} {#limited}

**설명:** 계정이 제한(숨김)되었을 때만 반환하는 추가 속성입니다. true이면 경고 화면 뒤에 계정을 숨겨야 함을 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
3.5.3 - 추가

### `created_at` {#created_at}

**설명:** 계정 생성 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
0.1.0 - 추가\
3.4.0 - 이제 정확한 시각 대신 자정으로 표시

### `last_status_at` {#last_status_at}

**설명:** 가장 최근 게시물을 올린 시각입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜](/api/datetime-format#date)), 게시물이 없으면 null\
**버전 이력:**\
3.0.0 - 추가\
3.1.0 - 이제 시각 없이 날짜만 반환

### `statuses_count` {#statuses_count}

**설명:** 계정의 게시물 수입니다.\
**유형:** 정수\
**버전 이력:**\
0.1.0 - 추가

### `followers_count` {#followers_count}

**설명:** 이 프로필의 보고된 팔로워 수입니다.\
**유형:** 정수\
**버전 이력:**\
0.1.0 - 추가

### `following_count` {#following_count}

**설명:** 이 프로필의 보고된 팔로잉 수입니다.\
**유형:** 정수\
**버전 이력:**\
0.1.0 - 추가

### `hide_collections` {#hide_collections}

**설명:** 사용자가 팔로잉 및 팔로워 컬렉션의 내용을 숨기는지 나타냅니다.\
**유형:** {{<nullable>}} 불리언\
**버전 이력:**\
4.3.0 - 추가

### `show_media` {#show_media}

**설명:** 계정이 프로필에 미디어 첨부 파일을 담은 “미디어” 탭을 표시하기 원하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.6.0 - 추가

### `show_media_replies` {#show_media_replies}

**설명:** 계정이 프로필의 “미디어” 탭에 답글을 표시하기 원하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.6.0 - 추가

### `show_featured` {#show_featured}

**설명:** 계정이 프로필에 “소개” 탭을 표시하기 원하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.6.0 - 추가

### `roles` {#roles}

**설명:** 로컬 계정인 경우 사용자에게 할당된 공개 역할의 배열입니다(강조된 역할만). 강조된 역할이 없으면 빈 배열이고, 원격 계정이면 null입니다.\
**유형:** {{<nullable>}} 배열: [AccountRole](#AccountRole)\
**버전 이력:**\
4.1.0 - 추가

### `feature_approval` {#feature_approval}

**설명:** [Collection]({{< relref "entities/Collection" >}})에 소개되는 것에 관한 계정 정책과 요청 사용자에게 적용되는 방식을 요약합니다.\
**유형:** [FeatureApproval]({{< relref "entities/FeatureApproval" >}})
**버전 이력:**\
4.6.0 - 추가

### `invalid_handle` {{%optional%}} {#invalid_handle}

**설명**: 계정의 핸들이 잘못되었는지 나타냅니다. 핸들이 잘못된 계정도 서버 내에서 고유한 `acct`와 함께 반환되지만, 이 서버 외부에서 확인할 수 있거나 계정이 선택한 사용자명 또는 소속 서버를 반영한다고 가정하면 안 됩니다. 핸들을 확인할 수 없는 계정의 자리 표시자이며, 드물고 일시적인 예외 상황이어야 합니다.\
**유형:** 불리언\
4.7.0 - 추가

---

## CredentialAccount 엔터티 속성 {#CredentialAccount}

```json
{
  "id": "14715",
  "username": "trwnh",
  "acct": "trwnh",
  "display_name": "infinite love ⴳ",
  // ...
  "note": "<p>i have approximate knowledge of many things. perpetual student. (nb/ace/they)</p><p>xmpp/email: a@trwnh.com<br /><a href=\"https://trwnh.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer\"><span class=\"invisible\">https://</span><span class=\"\">trwnh.com</span><span class=\"invisible\"></span></a><br />help me live: <a href=\"https://liberapay.com/trwnh\" target=\"_blank\" rel=\"nofollow noopener noreferrer\"><span class=\"invisible\">https://</span><span class=\"\">liberapay.com/trwnh</span><span class=\"invisible\"></span></a> or paypal</p><p>- my triggers are moths and glitter<br />- i have all notifs except mentions turned off, so please interact if you wanna be friends! i literally will not notice otherwise<br />- dm me if i did something wrong, so i can improve<br />- purest person on fedi, do not lewd in my presence</p>",
  // ...
  "indexable": true,
  "roles": [],
  "source": {
    "attribution_domains": ["example.com", "example.net"],
    "privacy": "public",
    "sensitive": false,
    "spoiler_field": false,
    "language": "",
    "note": "i have approximate knowledge of many things. perpetual student. (nb/ace/they)\r\n\r\nxmpp/email: a@trwnh.com\r\nhttps://trwnh.com\r\nhelp me live: https://liberapay.com/trwnh or paypal\r\n\r\n- my triggers are moths and glitter\r\n- i have all notifs except mentions turned off, so please interact if you wanna be friends! i literally will not notice otherwise\r\n- dm me if i did something wrong, so i can improve\r\n- purest person on fedi, do not lewd in my presence",
    "fields": [
      {
        "name": "Website",
        "value": "https://trwnh.com",
        "verified_at": "2019-08-29T04:14:55.571+00:00"
      },
      {
        "name": "Portfolio",
        "value": "https://abdullahtarawneh.com",
        "verified_at": "2021-02-11T20:34:13.574+00:00"
      },
      {
        "name": "Fan of:",
        "value": "Punk-rock and post-hardcore (Circa Survive, letlive., La Dispute, THE FEVER 333)Manga (Yu-Gi-Oh!, One Piece, JoJo's Bizarre Adventure, Death Note, Shaman King)Platformers and RPGs (Banjo-Kazooie, Boktai, Final Fantasy Crystal Chronicles)",
        "verified_at": null
      },
      {
        "name": "What to expect:",
        "value": "talking about various things i find interesting, and otherwise being a genuine and decent wholesome poster. i'm just here to hang out and talk to cool people! and to spill my thoughts.",
        "verified_at": null
      }
    ],
    "follow_requests_count": 5,
    "hide_collections": false,
    "discoverable": false,
    "indexable": true
  },
  // ...
  "fields": [
    {
      "name": "Website",
      "value": "<a href=\"https://trwnh.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">trwnh.com</span><span class=\"invisible\"></span></a>",
      "verified_at": "2019-08-29T04:14:55.571+00:00"
    },
    {
      "name": "Portfolio",
      "value": "<a href=\"https://abdullahtarawneh.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">abdullahtarawneh.com</span><span class=\"invisible\"></span></a>",
      "verified_at": "2021-02-11T20:34:13.574+00:00"
    },
    {
      "name": "Fan of:",
      "value": "Punk-rock and post-hardcore (Circa Survive, letlive., La Dispute, THE FEVER 333)Manga (Yu-Gi-Oh!, One Piece, JoJo&#39;s Bizarre Adventure, Death Note, Shaman King)Platformers and RPGs (Banjo-Kazooie, Boktai, Final Fantasy Crystal Chronicles)",
      "verified_at": null
    },
    {
      "name": "What to expect:",
      "value": "talking about various things i find interesting, and otherwise being a genuine and decent wholesome poster. i&#39;m just here to hang out and talk to cool people! and to spill my thoughts.",
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

### `source` {#source}

**설명:** [자격 증명 확인]({{< relref "methods/accounts#verify_credentials" >}}) 및 [자격 증명 갱신]({{< relref "methods/accounts#update_credentials" >}}) API 메서드에 사용할 원본 값을 포함하는 추가 속성입니다.\
**유형:** 해시\
**버전 이력:**\
2.4.0 - 추가

### `source[attribution_domains]` {#source-attribution_domains}

**설명:** 이 계정을 저자로 표시할 수 있는 웹사이트 도메인입니다.\
**유형:** 배열: 문자열\
**버전 이력:**\
4.4.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 3) - 추가

#### `source[note]` {#source-note}

**설명:** HTML 대신 일반 텍스트로 된 프로필 소개입니다.\
**유형:** 문자열\
**버전 이력:**\
1.5.0 - 추가

#### `source[fields]` {#source-fields}

**설명:** 계정에 관한 메타데이터입니다.\
**유형:** 배열: [Field](#Field)\
**버전 이력:**\
2.4.0 - 추가

#### `source[privacy]` {#source-privacy}

**설명:** 새 게시물에 사용할 기본 공개 범위입니다.\
**유형:** 문자열 (열거형, 다음 중 하나)\
`public` = 공개 게시물\
`unlisted` = 조용한 공개 게시물\
`private` = 팔로워 전용 게시물\
`direct` = 개인 멘션 게시물\
**버전 이력:**\
1.5.0 - 추가

#### `source[sensitive]` {#source-sensitive}

**설명:** 새 게시물에 기본적으로 민감함 표시를 할지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
1.5.0 - 추가

#### `source[spoiler_field]` {#source-spoiler-field}

**설명:** 새 게시물에 기본적으로 콘텐츠 경고를 지정할지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
5.0.0 - 추가

#### `source[language]` {#source-language}

**설명:** 새 게시물의 기본 작성 언어입니다.\
**유형:** 문자열 (ISO 639-1 두 글자 언어 코드 또는 빈 문자열)\
**버전 이력:**\
2.4.2 - 추가

#### `source[follow_requests_count]` {#follow_requests_count}

**설명:** 대기 중인 팔로우 요청 수입니다.\
**유형:** 정수\
**버전 이력:**\
3.0.0 - 추가

#### `source[hide_collections]` {#source-hide_collections}

**설명:** 사용자가 팔로잉 및 팔로워 컬렉션의 내용을 숨기는지 나타냅니다.\
**유형:** {{<nullable>}} 불리언\
**버전 이력:**\
4.1.0 - 추가

#### `source[discoverable]` {#source-discoverable}

**설명:** 계정이 프로필 디렉터리 같은 발견 기능에 참여하는지 나타냅니다.\
**유형:** {{<nullable>}} 불리언\
**버전 이력:**\
3.1.0 - 추가

#### `source[indexable]` {#source-indexable}

**설명:** 공개 게시물을 누구나 검색할 수 있게 할지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.3.0 - 추가

#### `source[quote_policy]` {#source-quote_policy}

**설명:** 새 게시물에 사용할 기본 인용 정책입니다.\
**유형:** 문자열 (열거형, 다음 중 하나)\
`public` = 차단된 계정을 제외한 누구나 인용할 수 있습니다.\
`followers` = 팔로워와 작성자만 인용할 수 있습니다.\
`nobody` = 작성자만 인용할 수 있습니다.\
**버전 이력:**\
4.5.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 7) - `posting:default:quoted_policy` 추가

### `role` {#role}

**설명:** 권한과 강조 상태를 포함하여 현재 인증된 사용자에게 할당된 전체 역할입니다.\
**유형:** [Role]({{< relref "entities/Role" >}})\
**버전 이력:**\
4.0.0 - 추가

### `state` {#state}

**설명:** 현재 계정의 상태입니다.\
**유형:** [AccountState](#AccountState)\
**버전 이력:**\
5.0.0 - 추가

---

## MutedAccount 엔터티 속성 {#MutedAccount}

### `mute_expires_at` {#mute_expires_at}

**설명:** 해당하는 경우, 기간을 정한 뮤트의 만료 시각입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜와 시각](/api/datetime-format#datetime)), 무기한 뮤트이면 null\
**버전 이력:**\
3.3.0 - 추가

---

## `PartialAccountWithAvatar` entity {#PartialAccountWithAvatar}

아바타 목록을 표시하는 데 필요한 정보와 몇 가지 유용한 속성만 포함하는 축약된 [Account]({{< relref "entities/Account" >}}) 버전입니다. 비용이 큰 서버 직렬화 작업과 [알림 그룹]({{< relref "methods/grouped_notifications" >}}) 등의 네트워크 전송량을 줄이기 위한 것입니다.

### 속성 {#attributes-1}

#### `id` {#id-1}

**설명:** 계정 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.3.0 - 추가

#### `acct` {#acct-1}

**설명:** WebFinger 계정 URI입니다. 로컬 사용자는 `username`, 원격 사용자는 `username@domain`과 같습니다.\
**유형:** 문자열\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `url` {#url-1}

**설명:** 사용자 프로필 페이지의 위치입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `avatar` {#avatar-1}

**설명:** 게시물 옆과 프로필에 표시하는 아이콘 이미지입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `avatar_static` {#avatar_static-1}

**설명:** 아바타의 정적 버전입니다. `avatar`가 정적 이미지이면 같은 값이며, `avatar`가 애니메이션 GIF이면 다른 값입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

### `avatar_description` {#avatar_description-1}

**설명:** 아바타 이미지의 텍스트 설명입니다.\
**유형:** 문자열\
**버전 이력:**\
4.6.0 - 추가

#### `locked` {#locked-1}

**설명:** 계정이 팔로우 요청을 수동으로 승인하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `bot` {#bot-1}

**설명:** 계정이 자동 동작을 수행하거나, 관리되지 않거나, 로봇임을 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

### 예시 {#example-1}

```json
{
  "id": "23634",
  "acct": "noiob@awoo.space",
  "locked": false,
  "bot": false,
  "url": "https://awoo.space/@noiob",
  "avatar": "https://files.mastodon.social/accounts/avatars/000/023/634/original/6ca8804dc46800ad.png",
  "avatar_static": "https://files.mastodon.social/accounts/avatars/000/023/634/original/6ca8804dc46800ad.png",
  "avatar_description": "a shark"
}
```

---

## AccountRole 엔터티 속성 {#AccountRole}

Account의 `roles` 배열에 반환하는 간소화된 역할 엔터티로, 공개 역할 정보만 포함합니다.

### `id` {#accountrole-id}

**설명:** 데이터베이스의 Role ID입니다.\
**유형:** 문자열\
**버전 이력:**\
4.1.0 - 추가

### `name` {#accountrole-name}

**설명:** 역할 이름입니다.\
**유형:** 문자열\
**버전 이력:**\
4.1.0 - 추가

### `color` {#accountrole-color}

**설명:** 이 역할에 할당된 16진수 색상 코드입니다. 코드가 할당되지 않으면 빈 문자열입니다.\
**유형:** 문자열\
**버전 이력:**\
4.1.0 - 추가

---

## Field 엔터티 속성 {#Field}

### `name` {#name}

**설명:** 주어진 필드의 키-값 쌍에서 키입니다.\
**유형:** 문자열\
**버전 이력:**\
2.4.0 - 추가

### `value` {#value}

**설명:** `name` 키에 연결된 값입니다.\
**유형:** 문자열 (HTML)\
**버전 이력:**\
2.4.0 - 추가

### `verified_at` {#verified_at}

**설명:** 서버가 rel="me" 링크의 URL 값을 확인한 시각의 타임스탬프입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜와 시각](/api/datetime-format#datetime)) (`value`가 검증된 URL인 경우). 그렇지 않으면 null입니다.\
**버전 이력:**\
2.6.0 - 추가

---

## AccountState 엔터티 속성 {#AccountState}

계정 상태입니다.

### `functional` {#accountstate-functional}

**설명:** 현재 계정을 완전히 사용할 수 있는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
5.0.0 - 추가

### `confirmed` {#accountstate-confirmed}

**설명:** 현재 계정이 이메일 주소를 확인했는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
5.0.0 - 추가

### `approved` {#accountstate-approved}

**설명:** 중재자가 현재 계정을 승인했는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
5.0.0 - 추가


### `error` {#accountstate-error}

**설명:** 해당하는 경우, 계정을 사용할 수 없는 이유를 설명하는 현지화된 문자열입니다.\
**유형:** {{<nullable>}} 문자열\
**버전 이력:**\
5.0.0 - 추가

### `error_code` {#accountstate-error_code}

**설명:** 해당하는 경우, 계정을 사용할 수 없는 이유입니다. 코드로 표현합니다. 향후 추가 사유가 생길 수 있습니다.\
**유형:** {{<nullable>}} 문자열 (열거형, 다음 중 하나 `pending_confirmation`, `pending_approval`, `account_deleted`, `account_suspended`, `memorial`, `login_disabled`, `2fa_required`)\
**버전 이력:**\
5.0.0 - 추가

---

## 함께 보기 {#see-also}

{{< page-relref ref="methods/accounts" caption="accounts API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/account_serializer.rb" caption="app/serializers/rest/account_serializer.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/credential_account_serializer.rb" caption="app/serializers/rest/credential_account_serializer.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/muted_account_serializer.rb" caption="app/serializers/rest/muted_account_serializer.rb" >}}
