---
title: 필터 (Filter)
description: 사용자에게 표시하지 않을 게시물을 결정하는 사용자 정의 필터를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/filter",
	"/entities/Filter",
	"/api/entities/filter",
	"/api/entities/Filter",
]
---

## 예시 {#example}

```json
{
	"id": "19972",
	"title": "Test filter",
	"context": [
		"home"
	],
	"expires_at": "2022-09-20T17:27:39.296Z",
	"filter_action": "warn",
	"keywords": [
		{
			"id": "1197",
			"keyword": "bad word",
			"whole_word": false
		}
	],
	"statuses": [
		{
			"id": "1",
			"status_id": "109031743575371913"
		}
    ]
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 Filter ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.0.0 - 추가

### `title` {#title}

**설명:** 사용자가 필터에 붙인 제목입니다.\
**유형:** 문자열\
**버전 이력:**\
4.0.0 - 추가

### `context` {#context}

**설명:** 필터를 적용할 문맥입니다.\
**유형:** 배열: 문자열 (열거형, 하나 이상)\
`home` = 홈 타임라인과 리스트\
`notifications` = 알림 타임라인\
`public` = 공개 타임라인\
`thread` = 게시물 상세 화면에서 펼친 글타래\
`account` = 프로필을 볼 때\
**버전 이력:**\
4.0.0 - 추가

### `expires_at` {#expires_at}

**설명:** 필터 적용이 종료되는 시각입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜와 시각](/api/datetime-format#datetime)), 만료되지 않는 필터는 null\
**버전 이력:**\
4.0.0 - 추가

### `filter_action` {#filter_action}

**설명:** 게시물이 이 필터와 일치할 때 수행할 동작입니다.\
**유형:** 문자열 (열거형, 다음 중 하나)\
`warn` = 일치한 필터의 `title`을 보여 주는 경고를 표시하고, 사용자가 필터링된 게시물을 펼칠 수 있게 합니다. 기본값입니다(알 수 없는 값도 `warn`과 동일하게 처리해야 합니다).\
`hide` = 이 게시물을 받으면 표시하지 않습니다.\
`blur` = 일치한 필터의 `title`을 보여 주는 경고와 함께 미디어 첨부 파일을 숨기거나 흐리게 표시합니다.\
**버전 이력:**\
4.0.0 - 추가\
4.4.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 5) - `filter_action` 속성에 `blur` 값 추가

### `keywords` {{%optional%}} {#keywords}

**설명:** 이 필터에 속한 키워드입니다. [FilterResult]({{< relref "entities/FilterResult" >}})의 일부일 때는 생략합니다.\
**유형:** 배열: [FilterKeyword]({{< relref "entities/FilterKeyword" >}})\
**버전 이력:**\
4.0.0 - 추가

### `statuses` {{%optional%}} {#statuses}

**설명:** 이 필터에 속한 게시물입니다. [FilterResult]({{< relref "entities/FilterResult" >}})의 일부일 때는 생략합니다.\
**유형:** 배열: [FilterStatus]({{< relref "entities/FilterStatus" >}})\
**버전 이력:**\
4.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="api/guidelines#filters" caption="필터 구현 지침" >}}

{{< page-relref ref="entities/V1_Filter" caption="V1::Filter (마스토돈 3.5 이하)" >}}

{{< page-relref ref="methods/filters" caption="/api/v2/filters 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/filter_serializer.rb" caption="app/serializers/rest/filter_serializer.rb" >}}
