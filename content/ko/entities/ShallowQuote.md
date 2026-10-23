---
title: 간략한 인용 (ShallowQuote)
description: 현재 승인 상태가 포함된 인용 또는 인용 자리 표시자를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/shallow_quote",
]
---

## 예시 {#example}

```json
{
  "state": "accepted",
  "quoted_status_id": "103270115826048975"
}
```

## 속성 {#attributes}

### `state` {#state}

**설명:** 인용 상태입니다. 알 수 없는 값은 `unauthorized`로 처리해야 합니다.\
**유형:** 문자열 (열거형, 다음 중 하나)\
`pending` = 인용된 계정이 아직 인용을 확인하지 않았으며, 표시하려면 승인이 필요합니다.\
`accepted` = 인용이 승인되어 표시할 수 있습니다. `quoted_status_id`가 null이 아닌 몇 안 되는 경우 중 하나입니다.\
`rejected` = 인용된 계정이 인용을 명시적으로 거절하여 표시할 수 없습니다.\
`revoked` = 이전에 승인된 인용의 승인이 취소되어 표시할 수 없습니다.\
`deleted` = 인용은 승인되었지만 인용된 게시물 자체가 삭제되었습니다.\
`unauthorized` = 인용은 승인되었지만 사용자에게 이를 볼 권한이 없어 표시할 수 없습니다.\
`blocked_account` = 인용은 승인되었지만 사용자가 인용된 계정을 차단했으므로 표시하면 안 됩니다. `quoted_status_id`가 null이 아닌 몇 안 되는 경우 중 하나입니다.\
`blocked_domain` = 인용은 승인되었지만 사용자가 인용된 계정의 도메인을 차단했으므로 표시하면 안 됩니다. `quoted_status_id`가 null이 아닌 몇 안 되는 경우 중 하나입니다.\
`muted_account` = 인용은 승인되었지만 사용자가 인용된 계정을 뮤트했으므로 표시하면 안 됩니다. `quoted_status_id`가 null이 아닌 몇 안 되는 경우 중 하나입니다.
**버전 이력:**\
4.4.0 - 추가\
4.5.0 - `blocked_account`, `blocked_domain`, `muted_account` 추가

### `quoted_status_id` {#quoted_status_id}

**설명:** 인용된 게시물의 식별자입니다. `state` 속성이 `accepted`, `blocked_account`, `blocked_domain`, `muted_account` 중 하나이거나, 이를 감싸는 [Status]({{< relref "entities/status" >}}) 엔터티를 `DELETE /api/v1/statuses/:id` 호출로 얻은 경우가 아니면 `null`입니다.\
**유형:** {{<nullable>}} 문자열 (정수에서 변환하지만 숫자라는 보장은 없음) 또는 null\
**버전 이력:**\
4.4.0 - 추가\
4.5.7 - 게시물 삭제 응답의 일부로 엔터티를 반환할 때는 `state`와 관계없이 `quoted_status_id`를 게시물 ID로 설정

## 함께 보기 {#see-also}

{{< page-relref ref="entities/quote" caption="Quote" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/shallow_quote_serializer.rb" caption="app/serializers/rest/shallow_quote_serializer.rb" >}}
