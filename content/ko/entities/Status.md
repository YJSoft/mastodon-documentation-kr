---
title: 게시물 (Status)
description: 계정이 올린 게시물을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/mention",
  "/entities/Mention",
  "/entities/status",
  "/entities/Status",
  "/api/entities/mention",
  "/api/entities/Mention",
  "/api/entities/status",
  "/api/entities/Status",
]
---

## 예시 {#example}

```json
{
  "id": "103270115826048975",
  "created_at": "2019-12-08T03:48:33.901Z",
  "in_reply_to_id": null,
  "in_reply_to_account_id": null,
  "sensitive": false,
  "spoiler_text": "",
  "visibility": "public",
  "language": "en",
  "uri": "https://mastodon.social/users/Gargron/statuses/103270115826048975",
  "url": "https://mastodon.social/@Gargron/103270115826048975",
  "replies_count": 5,
  "reblogs_count": 6,
  "favourites_count": 11,
  "quotes_count": 2,
  "favourited": false,
  "reblogged": false,
  "muted": false,
  "bookmarked": false,
  "content": "<p>&quot;I lost my inheritance with one wrong digit on my sort code&quot;</p><p><a href=\"https://www.theguardian.com/money/2019/dec/07/i-lost-my-193000-inheritance-with-one-wrong-digit-on-my-sort-code\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://www.</span><span class=\"ellipsis\">theguardian.com/money/2019/dec</span><span class=\"invisible\">/07/i-lost-my-193000-inheritance-with-one-wrong-digit-on-my-sort-code</span></a></p>",
  "reblog": null,
  "application": {
    "name": "Web",
    "website": null
  },
  "account": {
    "id": "1",
    "username": "Gargron",
    "acct": "Gargron",
    "display_name": "Eugen",
    "locked": false,
    "bot": false,
    "discoverable": true,
    "group": false,
    "created_at": "2016-03-16T14:34:26.392Z",
    "note": "<p>Developer of Mastodon and administrator of mastodon.social. I post service announcements, development updates, and personal stuff.</p>",
    "url": "https://mastodon.social/@Gargron",
    "avatar": "https://files.mastodon.social/accounts/avatars/000/000/001/original/d96d39a0abb45b92.jpg",
    "avatar_static": "https://files.mastodon.social/accounts/avatars/000/000/001/original/d96d39a0abb45b92.jpg",
    "header": "https://files.mastodon.social/accounts/headers/000/000/001/original/c91b871f294ea63e.png",
    "header_static": "https://files.mastodon.social/accounts/headers/000/000/001/original/c91b871f294ea63e.png",
    "followers_count": 322930,
    "following_count": 459,
    "statuses_count": 61323,
    "last_status_at": "2019-12-10T08:14:44.811Z",
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
  "quote": null,
  "card": {
    "url": "https://www.theguardian.com/money/2019/dec/07/i-lost-my-193000-inheritance-with-one-wrong-digit-on-my-sort-code",
    "title": "‘I lost my £193,000 inheritance – with one wrong digit on my sort code’",
    "description": "When Peter Teich’s money went to another Barclays customer, the bank offered £25 as a token gesture",
    "type": "link",
    "author_name": "",
    "author_url": "",
    "provider_name": "",
    "provider_url": "",
    "html": "",
    "width": 0,
    "height": 0,
    "image": null,
    "embed_url": ""
  },
  "poll": null,
  "quote_approval": {
    "automatic": [],
    "manual": [],
    "current_user": "automatic"
  }
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 게시물 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
0.1.0 - 추가

### `uri` {#uri}

**설명:** 연합에 사용하는 게시물 URI입니다.\
**유형:** 문자열\
**버전 이력:**\
0.1.0 - 추가

### `created_at` {#created_at}

**설명:** 게시물 생성 날짜입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
0.1.0 - 추가

### `account` {#account}

**설명:** 게시물을 작성한 계정입니다.\
**유형:** [Account]({{< relref "entities/Account" >}})\
**버전 이력:**\
0.1.0 - 추가

### `content` {#content}

**설명:** HTML로 인코딩한 게시물 콘텐츠입니다.\
**유형:** 문자열 (HTML)\
**버전 이력:**\
0.1.0 - 추가

### `visibility` {#visibility}

**설명:** 게시물의 공개 범위입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`public` = 누구나 볼 수 있으며 공개 타임라인에 표시합니다.\
`unlisted` = 공개적으로 볼 수 있지만 공개 타임라인에는 포함하지 않습니다.\
`private` = 팔로워와 멘션된 사용자만 볼 수 있습니다.\
`direct` = 멘션된 사용자만 볼 수 있습니다.\
**버전 이력:**\
0.9.9 - 추가

### `sensitive` {#sensitive}

**설명:** 게시물에 민감한 콘텐츠 표시가 되어 있는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
0.9.9 - 추가

### `spoiler_text` {#spoiler_text}

**설명:** 게시물의 제목 또는 요약문입니다. 펼치기 전까지 그 아래의 게시물 콘텐츠를 접어 둡니다.\
**유형:** 문자열\
**버전 이력:**\
1.0.0 - 추가

### `media_attachments` {#media_attachments}

**설명:** 게시물에 첨부한 미디어입니다.\
**유형:** 배열: [MediaAttachment]({{< relref "entities/MediaAttachment" >}})\
**버전 이력:**\
0.6.0 - 추가

### `application` {{%optional%}} {#application}

**설명:** 게시물을 올리는 데 사용한 애플리케이션입니다.\
**유형:** 해시\
**버전 이력:**\
0.9.9 - 추가

#### `application[name]` {#application-name}

**설명:** 게시물을 올린 애플리케이션의 이름입니다.\
**유형:** 문자열\
**버전 이력:**\
0.9.9 - 추가

#### `application[website]` {#application-website}

**설명:** 게시물을 올린 애플리케이션에 연결된 웹사이트입니다.\
**유형:** {{<nullable>}} 문자열 (URL) 또는 null\
**버전 이력:**\
0.9.9 - 추가\
3.5.1 - 이제 이 속성에 null 허용

### `mentions` {#mentions}

**설명:** 게시물 콘텐츠 내의 사용자 멘션입니다.\
**유형:** 배열: [Status::Mention](#Mention)\
**버전 이력:**\
0.6.0 - 추가

### `tags` {#tags}

**설명:** 게시물 콘텐츠에서 사용한 해시태그입니다.\
**유형:** 배열: [Status::Tag](#Tag)\
**버전 이력:**\
0.6.0 - 추가

### `emojis` {#emojis}

**설명:** 게시물 콘텐츠를 렌더링할 때 사용할 사용자 지정 이모지입니다.\
**유형:** 배열: [CustomEmoji]({{< relref "entities/CustomEmoji" >}})\
**버전 이력:**\
2.0.0 - 추가

### `reblogs_count` {#reblogs_count}

**설명:** 게시물이 받은 부스트 수입니다.\
**유형:** 정수\
**버전 이력:**\
0.1.0 - 추가

### `favourites_count` {#favorites_count}

**설명:** 게시물이 받은 좋아요 수입니다.\
**유형:** 정수\
**버전 이력:**\
0.1.0 - 추가

### `quotes_count` {#quotes_count}

**설명:** 게시물의 승인된 인용 수입니다.\
**유형:** 정수\
**버전 이력:**\
4.5.0 - 추가

### `replies_count` {#replies_count}

**설명:** 게시물이 받은 답글 수입니다.\
**유형:** 정수\
**버전 이력:**\
2.5.0 - 추가

### `url` {#url}

**설명:** 게시물의 HTML 표현 링크입니다.\
**유형:** {{<nullable>}} 문자열 (URL) 또는 null\
**버전 이력:**\
0.1.0 - 추가

### `in_reply_to_id` {#in_reply_to_id}

**설명:** 답글 대상 게시물의 ID입니다.\
**유형:** {{<nullable>}} 문자열 (정수에서 변환하지만 숫자라는 보장은 없음) 또는 null\
**버전 이력:**\
0.1.0 - 추가

### `in_reply_to_account_id` {#in_reply_to_account_id}

**설명:** 답글 대상 게시물 작성 계정의 ID일 수 있습니다. 자기 자신에게 단 답글을 건너뛰는 경우가 있습니다. 계정 1이 게시물 A를 올리고 계정 2가 A에 대한 답글로 B, C, D를 연달아 올렸다면 B, C, D 모두 `in_reply_to_account_id` = 1입니다(C와 D에서 `in_reply_to_account_id` = 2가 되지 않습니다). 하지만 계정 1이 게시물 A를 올리고 계정 1이 A에 직접 답글로 B를 올렸다면 B의 `in_reply_to_account_id` = 1입니다(null이 아닙니다).\
**유형:** {{<nullable>}} 문자열 (정수에서 변환하지만 숫자라는 보장은 없음) 또는 null\
**버전 이력:**\
0.1.0 - 추가

### `reblog` {#reblog}

**설명:** 부스트한 게시물입니다.\
**유형:** {{<nullable>}} [Status]({{< relref "entities/status" >}}) 또는 null\
**버전 이력:**\
0.1.0 - 추가

### `poll` {#poll}

**설명:** 게시물에 첨부된 투표입니다.\
**유형:** {{<nullable>}} [Poll]({{< relref "entities/Poll" >}}) 또는 null\
**버전 이력:**\
2.8.0 - 추가

### `card` {#card}

**설명:** 게시물 콘텐츠에 포함된 링크의 미리보기 카드입니다.\
**유형:** {{<nullable>}} [PreviewCard]({{< relref "entities/PreviewCard" >}}) 또는 null\
**버전 이력:**\
2.6.0 - 추가

### `language` {#language}

**설명:** 게시물의 기본 언어입니다.\
**유형:** {{<nullable>}} 문자열 (ISO 639-1 두 글자 언어 코드) 또는 null\
**버전 이력:**\
1.4.0 - 추가

### `text` {#text}

**설명:** 게시물의 일반 텍스트 원본입니다. 게시물을 삭제할 때 `content` 대신 반환하여 클라이언트가 HTML 콘텐츠에서 원문을 역으로 추출하지 않고도 사용자가 원문을 바탕으로 다시 작성할 수 있게 합니다.\
**유형:** {{<nullable>}} 문자열 또는 null\
**버전 이력:**\
2.9.0 - 추가

### `edited_at` {#edited_at}

**설명:** 게시물의 마지막 수정 시각을 나타내는 타임스탬프입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
3.5.0 - 추가

### `quote` {#quote}

**설명:** 인용한 게시물이 있는 경우 해당 게시물의 정보입니다.\
**유형:** {{<nullable>}} [Quote]({{< relref "entities/quote" >}}), [ShallowQuote]({{< relref "entities/ShallowQuote" >}}) 또는 null\
**버전 이력:**\
4.4.0 - 추가

### `quote_approval` {#quote_approval}

**설명:** 게시물 인용 승인 정책과 요청 사용자에게 적용되는 방식의 요약입니다. 즉, 사용자가 해당 게시물을 인용할 수 있을 것으로 예상되는지 나타냅니다.\
**유형:** [QuoteApproval]({{< relref "entities/QuoteApproval" >}})
**버전 이력:**\
4.5.0 - 추가

### `favourited` {{%optional%}} {#favourited}

**설명:** 현재 토큰에 인증된 사용자가 있는 경우, 이 게시물에 좋아요를 눌렀는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
0.1.0 - 추가

### `reblogged` {{%optional%}} {#reblogged}

**설명:** 현재 토큰에 인증된 사용자가 있는 경우, 이 게시물을 부스트했는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
0.1.0 - 추가

### `muted` {{%optional%}} {#muted}

**설명:** 현재 토큰에 인증된 사용자가 있는 경우, 이 게시물의 대화 알림을 뮤트했는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
1.4.0 - 추가

### `bookmarked` {{%optional%}} {#bookmarked}

**설명:** 현재 토큰에 인증된 사용자가 있는 경우, 이 게시물을 북마크했는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
3.1.0 - 추가

### `pinned` {{%optional%}} {#pinned}

**설명:** 현재 토큰에 인증된 사용자가 있는 경우, 이 게시물을 고정했는지 나타냅니다. 고정할 수 있는 게시물에만 표시됩니다.\
**유형:** 불리언\
**버전 이력:**\
1.6.0 - 추가

### `filtered` {{%optional%}} {#filtered}

**설명:** 현재 토큰에 인증된 사용자가 있는 경우, 이 게시물과 일치한 필터와 키워드입니다.\
**유형:** 배열: [FilterResult]({{< relref "entities/FilterResult" >}})\
**버전 이력:**\
4.0.0 - 추가

### `tagged_collections` {#tagged_collections}

**설명:** `content`에 서버가 인식한 컬렉션 링크가 포함되어 있으면 실제 컬렉션을 포함합니다.\
**유형:** 배열: [Collection]({{< relref "entities/Collection" >}})\
**버전 이력:**\
4.6.0 - 추가

## Status::Mention 속성 {#Mention}

### `id` {#Mention-id}

**설명:** 멘션된 사용자의 계정 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
0.6.0 - 추가

### `username` {#Mention-username}

**설명:** 멘션된 사용자의 사용자명입니다.\
**유형:** 문자열\
**버전 이력:**\
0.6.0 - 추가

### `url` {#Mention-url}

**설명:** 멘션된 사용자의 프로필 위치입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
0.6.0 - 추가

### `acct` {#Mention-acct}

**설명:** 멘션된 사용자의 WebFinger acct: URI입니다. 로컬 사용자는 `username`, 원격 사용자는 `username@domain`과 같습니다.\
**유형:** 문자열\
**버전 이력:**\
0.6.0 - 추가

## Status::Tag 속성 {#Tag}

### `name` {#Tag-name}

**설명:** # 기호 뒤의 해시태그 값입니다.\
**유형:** 문자열\
**버전 이력:**\
0.9.0 - 추가

### `url` {#Tag-url}

**설명:** 서버의 해시태그 링크입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
0.9.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/accounts#statuses" caption="GET /api/v1/accounts/:id/statuses" >}}

{{< page-relref ref="methods/search#v2" caption="POST /api/v2/search/" >}}

{{< page-relref ref="methods/statuses" caption="statuses 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/status_serializer.rb" caption="app/serializers/rest/status_serializer.rb" >}}
