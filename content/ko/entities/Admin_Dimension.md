---
title: 관리자용 차원 (Admin::Dimension)
description: 서버에 대한 정성 데이터를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/admin-dimension",
  "/entities/Admin-Dimension",
  "/entities/admin_dimension",
  "/entities/Admin_Dimension",
  "/api/entities/admin-dimension",
  "/api/entities/Admin-Dimension",
  "/api/entities/admin_dimension",
  "/api/entities/Admin_Dimension",
]
---

## 속성 {#attributes}

### `key` {#key}

**설명:** 요청한 차원의 고유 키 문자열입니다.\
**유형:** 문자열\
**버전 이력:**\
3.5.0 - 추가

### `data` {#data}

**설명:** 요청한 차원에 사용할 수 있는 데이터입니다.\
**유형:** 배열: 해시\
**버전 이력:**\
3.5.0 - 추가

## Data 속성 {#data-attributes}

### `key` {#data-key}

**설명:** 이 데이터 항목의 고유 키 문자열입니다.\
**유형:** 문자열\
**버전 이력:**\
3.5.0 - 추가

### `human_key` {#data-human_key}

**설명:** 사람이 읽기 쉬운 데이터 항목의 키입니다.\
**유형:** 문자열\
**버전 이력:**\
3.5.0 - 추가

### `value` {#data-value}

**설명:** 이 데이터 항목의 값입니다.\
**유형:** 문자열\
**버전 이력:**\
3.5.0 - 추가

### `unit` {{%optional%}} {#data-unit}

**설명:** 해당하는 경우, 이 데이터 항목 값의 단위입니다.\
**유형:** 문자열\
**버전 이력:**\
3.5.0 - 추가

### `human_value` {{%optional%}} {#data-human_value}

**설명:** 사람이 읽기 쉽게 서식화한 데이터 항목 값입니다.\
**유형:** 문자열\
**버전 이력:**\
3.5.0 - 추가

## 예시 {#examples}

### `languages` {#languages}

언어별 로컬 게시물 수를 집계한 뒤 각 언어의 인기도에 대한 차원 데이터를 표시합니다.

```json
{
	"key": "languages",
	"data": [
		{
			"key": "en",
			"human_key": "English",
			"value": "10"
		},
		{
			"key": "es",
			"human_key": "Spanish",
			"value": "1"
		},
		// ...
	]
}
```

### `sources` {#sources}

주어진 클라이언트로 작성한 로컬 게시물 수를 집계한 뒤 각 클라이언트의 인기도에 대한 차원 데이터를 표시합니다.

```json
{
	"key": "sources",
	"data": [
		{
			"key": "web",
			"human_key": "Website",
			"value": "2"
		},
		// ...
	]
}
```

### `servers` {#servers}

주어진 도메인에서 게시한 게시물 수를 집계한 뒤 가장 인기 있는 원격 서버에 대한 차원 데이터를 표시합니다.

```json
{
    "key": "servers",
    "data": [
      {
        "key": "botsin.space",
        "human_key": "botsin.space",
        "value": "13738"
      },
      {
        "key": "mastodon.social",
        "human_key": "mastodon.social",
        "value": "8928"
      },
		// ...
    ]
  }
```

### `space_usage` {#space_usage}

서버 스택의 각 소프트웨어가 사용하는 공간에 대한 차원 데이터를 표시합니다.

```json
{
	"key": "space_usage",
	"data": [
		{
			"key": "postgresql",
			"human_key": "PostgreSQL",
			"value": "14924935",
			"unit": "bytes",
			"human_value": "14.2 MB"
		},
		{
			"key": "redis",
			"human_key": "Redis",
			"value": "1972544",
			"unit": "bytes",
			"human_value": "1.88 MB"
		},
		{
			"key": "media",
			"human_key": "Media storage",
			"value": "0",
			"unit": "bytes",
			"human_value": "0 Bytes"
		}
	]
}
```

### `software_versions` {#software_versions}

서버 스택에서 사용 중인 소프트웨어 버전에 대한 차원 데이터를 표시합니다.

```json
{
	"key": "software_versions",
	"data": [
		{
			"key": "mastodon",
			"human_key": "Mastodon",
			"value": "3.5.3",
			"human_value": "3.5.3"
		},
		{
			"key": "ruby",
			"human_key": "Ruby",
			"value": "3.0.4p208",
			"human_value": "3.0.4p208"
		},
		{
			"key": "postgresql",
			"human_key": "PostgreSQL",
			"value": "10.22",
			"human_value": "10.22"
		},
		{
			"key": "redis",
			"human_key": "Redis",
			"value": "4.0.9",
			"human_value": "4.0.9"
		}
	]
}
```

### `tag_servers` {#tag_servers}

주어진 `id`의 유행 태그를 포함한 게시물 수를 집계한 뒤 해당 태그를 사용하는 가장 인기 있는 서버에 대한 차원 데이터를 표시합니다.

```json
{
	"key": "tag_servers",
	"data": [
		{
			"key": "live.hatnix.net",
			"human_key": "live.hatnix.net",
			"value": "6"
		},
		{
			"key": "linuxrocks.online",
			"human_key": "linuxrocks.online",
			"value": "4"
		}
	]
}
```

### `tag_languages` {#tag_languages}

주어진 `id`의 유행 태그를 포함한 게시물 수를 집계한 뒤 해당 게시물에서 가장 인기 있는 언어에 대한 차원 데이터를 표시합니다.

```json
{
    "key": "tag_languages",
    "data": [
      {
        "key": "und",
        "human_key": "und",
        "value": "8"
      },
      {
        "key": "en",
        "human_key": "English",
        "value": "7"
      },
		// ...
    ]
  }
```

### `instance_accounts` {#instance_accounts}

주어진 `domain`의 각 계정이 가진 팔로워 수를 집계한 뒤 해당 원격 서버에서 가장 인기 있는 계정에 대한 차원 데이터를 표시합니다.

```json
{
	"key": "instance_accounts",
	"data": [
		{
			"key": "fribbledom",
			"human_key": "fribbledom",
			"value": "33"
		},
		{
			"key": "ShugoWah",
			"human_key": "ShugoWah",
			"value": "26"
		},
		// ...
	]
}
```

### `instance_languages` {#instance_languages}

주어진 `domain`의 언어별 게시물 수를 집계한 뒤 해당 원격 서버에서 각 언어의 인기도에 대한 차원 데이터를 표시합니다.

```json
{
	"key": "instance_languages",
	"data": [
		{
			"key": "en",
			"human_key": "English",
			"value": "5848"
		},
		{
			"key": "de",
			"human_key": "German",
			"value": "155"
		},
		// ...
	]
}
```

## 함께 보기 {#see-also}

{{< page-relref ref="methods/admin/dimensions" caption="admin/dimensions API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/admin/dimension_serializer.rb" caption="app/serializers/rest/admin/dimension_serializer.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/admin/metrics/dimension.rb" caption="app/lib/admin/metrics/dimension.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/admin/metrics/dimension/" caption="app/lib/admin/metrics/dimension/" >}}