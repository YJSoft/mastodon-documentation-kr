---
title: 게시물 수정 이력 (StatusEdit)
description: 수정된 게시물의 리비전을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/statusedit",
	"/entities/StatusEdit",
	"/api/entities/statusedit",
	"/api/entities/StatusEdit",
]
---

## 예시 {#example}

```json
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
```

## 속성 {#attributes}

### `content` {#content}

**설명:** 이 리비전에서의 게시물 콘텐츠입니다.\
**유형:** 문자열 (HTML)\
**버전 이력:**\
3.5.0 - 추가

### `spoiler_text` {#spoiler_text}

**설명:** 이 리비전에서의 제목 또는 콘텐츠 경고 내용입니다.\
**유형:** 문자열 (HTML)\
**버전 이력:**\
3.5.0 - 추가

### `sensitive` {#sensitive}

**설명:** 이 리비전에서 게시물이 민감함으로 표시되었는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
3.5.0 - 추가

### `created_at` {#created_at}

**설명:** 이 리비전이 게시된 시각의 타임스탬프입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
3.5.0 - 추가

### `account` {#account}

**설명:** 이 리비전을 게시한 계정입니다.\
**유형:** [Account]({{<relref "entities/Account">}})\
**버전 이력:**\
3.5.0 - 추가

### `poll` {{%optional%}} {#poll}

**설명:** 이 리비전에서의 투표 선택지 상태입니다. 투표 선택지를 변경하면 투표가 초기화되므로, 선택지를 변경하는 수정은 하나의 수정으로 합쳐집니다.\
**유형:** 해시\
**버전 이력:**\
3.5.0 - 추가

#### `poll.options[]` {#poll-options}

**설명:** 이 리비전에서의 투표 선택지입니다.\
**유형:** 배열: 해시\
**버전 이력:**\
3.5.0 - 추가

#### `poll.options[].title` {#poll-options-title}

**설명:** 투표 선택지의 텍스트입니다.\
**유형:** 문자열\
**버전 이력:**\
3.5.0 - 추가

### `media_attachments` {#media_attachments}

**설명:** 이 리비전에서의 미디어 첨부 파일 상태입니다.\
**유형:** 배열: [MediaAttachment]({{<relref "entities/MediaAttachment">}})\
**버전 이력:**\
3.5.0 - 추가

### `emojis` {#emojis}

**설명:** 현재 리비전에서 사용한 사용자 지정 이모지입니다.\
**유형:** 배열: [CustomEmoji]({{<relref "entities/CustomEmoji">}})\
**버전 이력:**\
3.5.0 - 추가

### `quote` {{%optional%}} {#quote}

**설명:** 인용한 게시물이 있는 경우 해당 게시물의 정보입니다.\
**유형:** {{<nullable>}} [Quote]({{< relref "entities/quote" >}}) 또는 [ShallowQuote]({{< relref "entities/ShallowQuote" >}})\
**버전 이력:**\
4.4.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/statuses#history" caption="GET /api/v1/statuses/:id/history" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/status_edit_serializer.rb" caption="app/serializers/rest/status_edit_serializer.rb" >}}

