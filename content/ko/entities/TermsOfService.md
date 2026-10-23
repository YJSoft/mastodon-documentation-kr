---
title: 이용약관 (TermsOfService)
description: 서버 이용약관을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/termsofservice",
  "/entities/TermsOfService",
  "/api/entities/termsofservice",
  "/api/entities/TermsOfService",
]
---

## 예시 {#example}

```json
{
  "effective_date": "2025-04-15",
  "effective": true,
  "content": "<p>Foo bar newer</p>\n",
  "succeeded_by": null
}
```

## 속성 {#attributes}

### `effective_date` {#effective_date}

**설명:** 이 이용약관이 시행되거나 시행될 날짜입니다.\
**유형:** 문자열 ([날짜](/api/datetime-format#date))\
**버전 이력:**\
4.4.0 - 추가

### `effective` {#effective}

**설명:** 이 이용약관이 현재 유효한지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.4.0 - 추가

### `content` {#content}

**설명:** 렌더링된 HTML 형식의 이용약관 내용입니다.\
**유형:** 문자열 (HTML)\
**버전 이력:**\
4.4.0 - 추가

### `succeeded_by` {#succeeded_by}

**설명:** 더 새로운 이용약관이 있는 경우 그 시행일입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜](/api/datetime-format#date))\
**버전 이력:**\
4.4.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/instance#terms_of_service" caption="GET /api/v1/instance/terms_of_service" >}}

{{< page-relref ref="methods/instance#terms_of_service_date" caption="GET /api/v1/instance/terms_of_service/:date" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/terms_of_service_serializer.rb" caption="app/serializers/rest/terms_of_service_serializer.rb" >}}
