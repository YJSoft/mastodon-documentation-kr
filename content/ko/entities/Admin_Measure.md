---
title: 관리자용 측정값 (Admin::Measure)
description: 서버에 대한 정량 데이터를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/admin-measure",
  "/entities/Admin-Measure",
  "/entities/admin_measure",
  "/entities/Admin_Measure",
  "/api/entities/admin-measure",
  "/api/entities/Admin-Measure",
  "/api/entities/admin_measure",
  "/api/entities/Admin_Measure",
]
---

## 속성 {#attributes}

### `key` {#key}

**설명:** 요청한 측정값의 고유 키 문자열입니다.\
**유형:** 문자열\
**버전 이력:**\
3.5.0 - 추가

### `unit` {#unit}

**설명:** 해당하는 경우, 이 데이터 항목 값의 단위입니다.\
**유형:** {{<nullable>}} 문자열 또는 null\
**버전 이력:**\
3.5.0 - 추가

### `total` {#total}

**설명:** 요청한 측정값의 수치 합계입니다.\
**유형:** 문자열 (정수에서 변환)\
**버전 이력:**\
3.5.0 - 추가

### `human_value` {{%optional%}} {#data-human_value}

**설명:** 사람이 읽기 쉽게 서식화한 데이터 항목 값입니다.\
**유형:** 문자열\
**버전 이력:**\
3.5.0 - 추가

### `previous_total` {{%optional%}} {#previous_total}

**설명:** 이전 기간의 요청한 측정값 수치 합계입니다. 이전 기간은 start_at과 end_at 날짜의 차이를 계산한 뒤 시작일과 종료일을 모두 해당 기간 길이만큼 과거로 이동하여 계산합니다.\
**유형:** 문자열 (정수에서 변환)\
**버전 이력:**\
3.5.0 - 추가

### `data` {#data}

**설명:** 요청한 측정값에 사용할 수 있는 데이터를 일별 버킷으로 나눈 값입니다.\
**유형:** 배열: 해시\
**버전 이력:**\
3.5.0 - 추가

#### `data[][date]` {#data-date}

**설명:** 기간 내 요청한 날짜 또는 요청한 날짜의 자정입니다.\
**유형:** 문자열 ([날짜](/api/datetime-format#date) 또는 [날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
3.5.0 - 추가

#### `data[][value]` {#data-value}

**설명:** 요청한 측정값의 수치입니다.\
**유형:** 문자열 (정수에서 변환)\
**버전 이력:**\
3.5.0 - 추가

## 예시 {#examples}

### `active_users` {#active_users}

2022-09-14부터 2022-09-22까지 서버의 총 활성 사용자 수

```json
{
  "key": "active_users",
  "unit": null,
  "total": "2",
  "previous_total": "0",
  "data": [
    {
      "date": "2022-09-14T00:00:00Z",
      "value": "0"
    },
    {
      "date": "2022-09-15T00:00:00Z",
      "value": "0"
    },
    {
      "date": "2022-09-16T00:00:00Z",
      "value": "0"
    },
    {
      "date": "2022-09-17T00:00:00Z",
      "value": "1"
    },
    {
      "date": "2022-09-18T00:00:00Z",
      "value": "1"
    },
    {
      "date": "2022-09-19T00:00:00Z",
      "value": "1"
    },
    {
      "date": "2022-09-20T00:00:00Z",
      "value": "2"
    },
    {
      "date": "2022-09-21T00:00:00Z",
      "value": "1"
    }
  ]
}
```

### `new_users` {#new_users}

2022-09-14부터 2022-09-22까지 서버에 가입한 사용자 수

```json
{
  "key": "new_users",
  "unit": null,
  "total": "2",
  "previous_total": "0",
  "data": [
    {
      "date": "2022-09-14T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-15T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-16T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-17T00:00:00.000+00:00",
      "value": "1"
    },
    {
      "date": "2022-09-18T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-19T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-20T00:00:00.000+00:00",
      "value": "1"
    },
    {
      "date": "2022-09-21T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-22T00:00:00.000+00:00",
      "value": "0"
    }
  ]
}
```

### `interactions` {#interactions}

2022-09-14부터 2022-09-22까지 로컬 게시물의 총 상호작용 수(좋아요, 부스트, 답글)

```json
{
  "key": "interactions",
  "unit": null,
  "total": "0",
  "previous_total": "0",
  "data": [
    {
      "date": "2022-09-14T00:00:00Z",
      "value": "0"
    },
    {
      "date": "2022-09-15T00:00:00Z",
      "value": "0"
    },
    {
      "date": "2022-09-16T00:00:00Z",
      "value": "0"
    },
    {
      "date": "2022-09-17T00:00:00Z",
      "value": "0"
    },
    {
      "date": "2022-09-18T00:00:00Z",
      "value": "0"
    },
    {
      "date": "2022-09-19T00:00:00Z",
      "value": "0"
    },
    {
      "date": "2022-09-20T00:00:00Z",
      "value": "0"
    },
    {
      "date": "2022-09-21T00:00:00Z",
      "value": "0"
    }
  ]
}
```

### `opened_reports` {#opened_reports}

2022-09-14부터 2022-09-22까지 접수된 총 신고 수

```json
{
        "key": "opened_reports",
        "unit": null,
        "total": "0",
        "previous_total": "0",
        "data": [
            {
                "date": "2022-09-14T00:00:00.000+00:00",
                "value": "0"
            },
            {
                "date": "2022-09-15T00:00:00.000+00:00",
                "value": "0"
            },
            {
                "date": "2022-09-16T00:00:00.000+00:00",
                "value": "0"
            },
            {
                "date": "2022-09-17T00:00:00.000+00:00",
                "value": "0"
            },
            {
                "date": "2022-09-18T00:00:00.000+00:00",
                "value": "0"
            },
            {
                "date": "2022-09-19T00:00:00.000+00:00",
                "value": "0"
            },
            {
                "date": "2022-09-20T00:00:00.000+00:00",
                "value": "0"
            },
            {
                "date": "2022-09-21T00:00:00.000+00:00",
                "value": "0"
            },
            {
                "date": "2022-09-22T00:00:00.000+00:00",
                "value": "0"
            }
        ]
    }
```

### `resolved_reports` {#resolved_reports}

2022-09-14부터 2022-09-22까지 처리된 총 신고 수

```json
{
  "key": "resolved_reports",
  "unit": null,
  "total": "0",
  "previous_total": "0",
  "data": [
    {
      "date": "2022-09-14T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-15T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-16T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-17T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-18T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-19T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-20T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-21T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-22T00:00:00.000+00:00",
      "value": "0"
    }
  ]
}
```

### `tag_accounts` {#tag_accounts}

2022-09-14부터 2022-09-22까지 하나 이상의 게시물에서 태그를 사용한 총 계정 수

```json
{
  "key": "tag_accounts",
  "unit": null,
  "total": "1",
  "previous_total": "0",
  "data": [
    {
      "date": "2022-09-14T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-15T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-16T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-17T00:00:00.000+00:00",
      "value": "1"
    },
    {
      "date": "2022-09-18T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-19T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-20T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-21T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-22T00:00:00.000+00:00",
      "value": "0"
    }
  ]
}
```

### `tag_uses` {#tag_uses}

2022-09-14부터 2022-09-22까지 태그를 사용한 총 게시물 수

```json
{
  "key": "tag_uses",
  "unit": null,
  "total": "2",
  "previous_total": "0",
  "data": [
    {
      "date": "2022-09-14T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-15T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-16T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-17T00:00:00.000+00:00",
      "value": "1"
    },
    {
      "date": "2022-09-18T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-19T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-20T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-21T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-22T00:00:00.000+00:00",
      "value": "1"
    }
  ]
}
```

### `tag_servers` {#tag_servers}

2022-09-14부터 2022-09-22까지 태그를 사용한 게시물의 원본 원격 서버 총수

```json
{
  "key": "tag_servers",
  "unit": null,
  "total": "0",
  "previous_total": "0",
  "data": [
    {
      "date": "2022-09-14T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-15T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-16T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-17T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-18T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-19T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-20T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-21T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-22T00:00:00.000+00:00",
      "value": "0"
    }
  ]
}
```

### `instance_accounts` {#instance_accounts}

2022-09-14부터 2022-09-22까지 원격 도메인에 속한 총 계정 수

```json
{
  "key": "instance_accounts",
  "unit": null,
  "total": "0",
  "data": [
    {
      "date": "2022-09-14T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-15T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-16T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-17T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-18T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-19T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-20T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-21T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-22T00:00:00.000+00:00",
      "value": "0"
    }
  ]
}
```

### `instance_media_attachments` {#instance_media_attachments}

2022-09-14부터 2022-09-22까지 원격 도메인의 미디어 첨부 파일이 사용한 총 공간

```json
{
  "key": "instance_media_attachments",
  "unit": "bytes",
  "total": "0",
  "human_value": "0 Bytes",
  "data": [
    {
      "date": "2022-09-14T00:00:00.000+00:00",
      "value": ""
    },
    {
      "date": "2022-09-15T00:00:00.000+00:00",
      "value": ""
    },
    {
      "date": "2022-09-16T00:00:00.000+00:00",
      "value": ""
    },
    {
      "date": "2022-09-17T00:00:00.000+00:00",
      "value": ""
    },
    {
      "date": "2022-09-18T00:00:00.000+00:00",
      "value": ""
    },
    {
      "date": "2022-09-19T00:00:00.000+00:00",
      "value": ""
    },
    {
      "date": "2022-09-20T00:00:00.000+00:00",
      "value": ""
    },
    {
      "date": "2022-09-21T00:00:00.000+00:00",
      "value": ""
    },
    {
      "date": "2022-09-22T00:00:00.000+00:00",
      "value": ""
    }
  ]
}
```

### `instance_reports` {#instance_reports}
2022-09-14부터 2022-09-22까지 원격 도메인 계정에 대해 접수된 총 신고 수

```json
{
  "key": "instance_reports",
  "unit": null,
  "total": "0",
  "data": [
    {
      "date": "2022-09-14T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-15T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-16T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-17T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-18T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-19T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-20T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-21T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-22T00:00:00.000+00:00",
      "value": "0"
    }
  ]
}
```

### `instance_statuses` {#instance_statuses}

2022-09-14부터 2022-09-22까지 원격 도메인에 속한 총 게시물 수

```json
{
  "key": "instance_statuses",
  "unit": null,
  "total": "0",
  "data": [
    {
      "date": "2022-09-14T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-15T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-16T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-17T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-18T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-19T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-20T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-21T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-22T00:00:00.000+00:00",
      "value": "0"
    }
  ]
}
```

### `instance_follows` {#instance_follows}

2022-09-14부터 2022-09-22까지 로컬 사용자가 팔로우한 원격 도메인의 총 계정 수

```json
{
  "key": "instance_follows",
  "unit": null,
  "total": "0",
  "data": [
    {
      "date": "2022-09-14T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-15T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-16T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-17T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-18T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-19T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-20T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-21T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-22T00:00:00.000+00:00",
      "value": "0"
    }
  ]
}
```

### `instance_followers` {#instance_followers}

2022-09-14부터 2022-09-22까지 원격 도메인 계정이 팔로우한 총 로컬 계정 수

```json
{
  "key": "instance_followers",
  "unit": null,
  "total": "0",
  "data": [
    {
      "date": "2022-09-14T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-15T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-16T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-17T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-18T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-19T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-20T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-21T00:00:00.000+00:00",
      "value": "0"
    },
    {
      "date": "2022-09-22T00:00:00.000+00:00",
      "value": "0"
    }
  ]
}
```

## 함께 보기 {#see-also}

{{< page-relref ref="methods/admin/dimensions" caption="admin/dimensions API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/admin/measure_serializer.rb" caption="app/serializers/rest/admin/measure_serializer.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/admin/metrics/measure.rb" caption="app/lib/admin/metrics/measure.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/admin/metrics/measure/" caption="app/lib/admin/metrics/measure/" >}}
