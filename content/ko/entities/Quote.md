---
title: 인용 (Quote)
description: 현재 승인 상태가 포함된 인용 또는 인용 자리 표시자를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/quote",
]
---

## 예시 {#example}

```json
{
  "state": "accepted",
  "quoted_status": {
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
      "fields": []
    },
    "media_attachments": [],
    "mentions": [],
    "tags": [],
    "emojis": [],
    "card": null,
    "poll": null
  }
}
```

## 속성 {#attributes}

### `state` {#state}

**설명:** 인용 상태입니다. 알 수 없는 값은 `unauthorized`로 처리해야 합니다.\
**유형:** 문자열 (열거형, 다음 중 하나)\
`pending` = 인용된 계정이 아직 인용을 확인하지 않았으며, 표시하려면 승인이 필요합니다.\
`accepted` = 인용이 승인되어 표시할 수 있습니다. `quoted_status`는 null이 아닙니다.\
`rejected` = 인용된 계정이 인용을 명시적으로 거절하여 표시할 수 없습니다.\
`revoked` = 이전에 승인된 인용의 승인이 취소되어 표시할 수 없습니다.\
`deleted` = 인용은 승인되었지만 인용된 게시물 자체가 삭제되었습니다.\
`unauthorized` = 인용은 승인되었지만 사용자에게 이를 볼 권한이 없어 표시할 수 없습니다.\
`blocked_account` = 인용은 승인되었지만 사용자가 인용된 계정을 차단했으므로 표시하면 안 됩니다. `quoted_status`는 null이 아닙니다.\
`blocked_domain` = 인용은 승인되었지만 사용자가 인용된 계정의 도메인을 차단했으므로 표시하면 안 됩니다. `quoted_status`는 null이 아닙니다.\
`muted_account` = 인용은 승인되었지만 사용자가 인용된 계정을 뮤트했으므로 표시하면 안 됩니다. `quoted_status`는 null이 아닙니다.
**버전 이력:**\
4.4.0 - 추가\
4.5.0 - `blocked_account`, `blocked_domain`, `muted_account` 추가

### `quoted_status` {#quoted_status}

**설명:** 인용이 승인된 경우 인용된 게시물입니다. `state` 속성이 `accepted`, `blocked_account`, `blocked_domain`, `muted_account` 중 하나이거나, 이를 감싸는 [Status]({{< relref "entities/status" >}}) 엔터티를 `DELETE /api/v1/statuses/:id` 호출로 얻은 경우가 아니면 `null`입니다.\
**유형:** {{<nullable>}} [Status]({{< relref "entities/status" >}}) 또는 null\
**버전 이력:**\
4.4.0 - 추가\
4.5.7 - 게시물 삭제 응답의 일부로 엔터티를 반환할 때는 `state`와 관계없이 `quoted_status`를 인용된 게시물로 설정합니다.

## 함께 보기 {#see-also}

{{< page-relref ref="entities/ShallowQuote" caption="ShallowQuote" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/quote_serializer.rb" caption="app/serializers/rest/quote_serializer.rb" >}}
