---
title: 프로필 (Profile)
description: 편집 가능한 모든 필드의 원본 값을 포함한 현재 사용자 프로필을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/profile",
  "/entities/Profile",
  "/api/entities/profile",
  "/api/entities/Profile",
]
---

## 예시 {#example}

```json
{
  "id": "116222600881276277",
  "display_name": "Documentation user",
  "note": "I'm only here as an example for documentation",
  "fields": [
    {
      "name": "pronouns",
      "value": "it/its",
      "verified_at": null
    }
  ],
  "avatar": null,
  "avatar_static": null,
  "avatar_description": "",
  "header": null,
  "header_static": null,
  "header_description": "",
  "locked": false,
  "bot": false,
  "hide_collections": null,
  "discoverable": true,
  "indexable": true,
  "show_media": true,
  "show_media_replies": true,
  "show_featured": true,
  "attribution_domains": [
    "articles.example.com"
  ],
  "featured_tags": [
    {
      "id": "1",
      "name": "foo",
      "url": "https://example.com/@darrel_metz0/tagged/foo",
      "statuses_count": "0",
      "last_status_at": null
    }
  ]
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 계정 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.6.0 - 추가

### `display_name` {#display_name}

**설명:** 프로필의 표시 이름입니다.\
**유형:** 문자열\
**버전 이력:**\
4.6.0 - 추가

### `note` {#note}

**설명:** 프로필의 소개 또는 설명입니다. [Account]({{< relref "entities/Account">}})와 달리 렌더링된 HTML이 아닌 처리 전 원시 텍스트입니다.\
**유형:** 문자열 (원시 텍스트)\
**버전 이력:**\
4.6.0 - 추가

### `fields` {#fields}

**설명:** 계정에 관한 메타데이터입니다. 처리 전 원시 이름과 값을 포함합니다.\
**유형:** 배열: [Field](#Field)\
**버전 이력:**\
4.6.0 - 추가

### `avatar` {#avatar}

**설명:** 게시물 옆과 프로필에 표시하는 아이콘 이미지입니다. [Account]({{< relref "entities/Account">}})와 달리 null을 허용하며, 아바타를 설정하지 않으면 null입니다.\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
4.6.0 - 추가

### `avatar_static` {#avatar_static}

**설명:** 아바타의 정적 버전입니다. [Account]({{< relref "entities/Account">}})와 달리 null을 허용하며, 아바타를 설정하지 않으면 null입니다.\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
4.6.0 - 추가

### `avatar_description` {#avatar_description}

**설명:** 시각 장애가 있거나 아바타가 로드되지 않을 때 사용할 아바타의 텍스트 설명입니다.\
**유형:** 문자열\
**버전 이력:**\
4.6.0 - 추가

### `header` {#header}

**설명:** 프로필 위와 프로필 카드에 표시하는 배너 이미지입니다. [Account]({{< relref "entities/Account">}})와 달리 null을 허용하며, 헤더를 설정하지 않으면 null입니다.\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
4.6.0 - 추가

### `header_static` {#header_static}

**설명:** 헤더의 정적 버전입니다. [Account]({{< relref "entities/Account">}})와 달리 null을 허용하며, 헤더를 설정하지 않으면 null입니다.\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
4.6.0 - 추가

### `header_description` {#header_description}

**설명:** 시각 장애가 있거나 아바타가 로드되지 않을 때 사용할 프로필 헤더의 텍스트 설명입니다.\
**유형:** 문자열\
**버전 이력:**\
4.6.0 - 추가

### `locked` {#locked}

**설명:** 계정이 팔로우 요청을 수동으로 승인하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.6.0 - 추가

### `bot` {#bot}

**설명:** 계정이 자동 동작을 수행하거나, 관리되지 않거나, 로봇임을 나타냅니다. 계정의 `actor_type`이 'Application' 또는 'Service'로 설정되어 있는지에 따라 결정합니다.\
**유형:** 불리언\
**버전 이력:**\
4.6.0 - 추가

### `hide_collections` {#hide_collections}

**설명:** 사용자가 팔로잉 및 팔로워 컬렉션의 내용을 숨기는지 나타냅니다.\
**유형:** {{<nullable>}} 불리언\
**버전 이력:**\
4.6.0 - 추가

### `discoverable` {#discoverable}

**설명:** 계정이 프로필 디렉터리 같은 발견 기능에 참여하는지 나타냅니다.\
**유형:** {{<nullable>}} 불리언\
**버전 이력:**\
4.6.0 - 추가

### `indexable` {#indexable}

**설명:** 계정이 검색 엔진의 색인 생성을 허용하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.6.0 - 추가

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

### `attribution_domains` {#attribution_domains}

**설명:** 이 계정을 저자로 표시할 수 있는 웹사이트 도메인입니다.\
**유형:** 배열: 문자열\
**버전 이력:**\
4.6.0 - 추가

## Field 엔터티 속성 {#Field}

### `name` {#name}

**설명:** 주어진 필드의 키-값 쌍에서 키에 해당합니다. HTML이 아닌 처리 전 원시 문자열입니다.\
**유형:** 문자열\
**버전 이력:**\
4.6.0 - 추가

### `value` {#value}

**설명:** `name` 키에 연결된 값입니다. HTML이 아닌 처리 전 원시 문자열입니다.\
**유형:** 문자열\
**버전 이력:**\
4.6.0 - 추가

### `verified_at` {#verified_at}

**설명:** 서버가 rel="me" 링크의 URL 값을 확인한 시각의 타임스탬프입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜와 시각](/api/datetime-format#datetime)) (`value`가 검증된 URL인 경우). 그렇지 않으면 null입니다.\
**버전 이력:**\
4.6.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/profile#get-current-user-profile" caption="GET /api/v1/profile" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/profile_serializer.rb" caption="app/serializers/rest/profile_serializer.rb" >}}