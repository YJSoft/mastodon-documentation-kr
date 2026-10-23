---
title: 필터 키워드 (FilterKeyword)
description: 일치할 경우 필터 동작을 실행해야 하는 키워드를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/filterkeyword",
	"/entities/FilterKeyword",
	"/api/entities/filterkeyword",
	"/api/entities/FilterKeyword",
]
---

## 예시 {#example}

```json
{
	"id": "1197",
	"keyword": "bad word",
	"whole_word": false
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 FilterKeyword ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.0.0 - 추가

### `keyword` {#keyword}

**설명:** 일치 여부를 검사할 구문입니다.\
**유형:** 문자열\
**버전 이력:**\
4.0.0 - 추가

### `whole_word` {#whole_word}

**설명:** 필터가 단어 경계를 고려해야 하는지 나타냅니다. [필터 구현 지침]({{< relref "api/guidelines#filters" >}})을 참고하세요.\
**유형:** 불리언\
**버전 이력:**\
4.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="api/guidelines#filters" caption="필터 구현 지침" >}}

{{< page-relref ref="methods/filters" caption="/api/v2/filters 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/filter_keyword_serializer.rb" caption="app/serializers/rest/filter_keyword_serializer.rb" >}}