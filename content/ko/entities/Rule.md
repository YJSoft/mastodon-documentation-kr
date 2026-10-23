---
title: 규칙 (Rule)
description: 서버 사용자가 따라야 하는 규칙을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/rule",
	"/entities/Rule",
	"/api/entities/rule",
	"/api/entities/Rule",
]
---

## 예시 {#example}

```json
{
	"id": "2",
	"text": "No racism, sexism, homophobia, transphobia, ableism, xenophobia, or casteism.",
	"hint": "Transphobic behavior such as intentional misgendering and deadnaming is strictly prohibited. Promotion of \"conversion therapy\" is strictly prohibited. Criticism of governments and religions is permissible unless being used as a proxy for discrimination.",
	"translations": {
		"fr": {
			"text": "Pas de racisme, sexisme, homophobie, transphobie, validisme, xénophobie ou casteisme.",
			"hint": "Les comportements transhobes tels que le deadnaming intentionel sont formellement interdits. La promotion des « thérapies de conversion » est formellement interdite. La critique des gouvernements et des religions est permise à moins qu'elle ne soit utilisée comme excuse pour de la discrimination."
		}
	}
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 규칙의 식별자입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
3.4.0 - 추가

### `text` {#text}

**설명:** 따라야 하는 규칙입니다.\
**유형:** 문자열 \
**버전 이력:**\
3.4.0 - 추가

### `hint` {#hint}

**설명:** 규칙의 자세한 설명입니다.\
**유형:** 문자열 \
**버전 이력:**\
4.3.0 - 추가

### `translations` {#translations}

**설명:** 이 규칙의 `text`와 `hint`에 제공되는 번역입니다. 키가 로캘 코드이고 값이 `text`와 `hint` 키를 갖는 해시인 해시로 표현합니다.\
**유형:** 해시\
**버전 이력:**\
4.4.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/instance#rules" caption="GET /api/v1/instance/rules" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/models/rule.rb" caption="app/models/rule.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/rule_serializer.rb" caption="app/serializers/rest/rule_serializer.rb" >}}




