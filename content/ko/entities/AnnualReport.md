---
title: 연간 보고서 (AnnualReport)
description: 주어진 연도에 이루어진 사용자 활동의 요약을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/annual_report",
  "/entities/AnnualReport",
  "/entities/wrapped_annual_reports",
  "/entities/WrappedAnnualReports",
  "/api/entities/AnnualReport",
  "/api/entities/WrappedAnnualReports",
]
---

## 예시 {#example}

```json
{
    "year": 2025,
    "data": {
    "archetype": "oracle",
    "time_series": [
        {
        "month": 12,
        "statuses": 7123,
        "followers": 48
        }
    ],
    "top_hashtags": [
        {
        "name": "Mastodon",
        "count": 12
        }
    ],
    "top_statuses": {
        "by_reblogs": "114348347829110933",
        "by_replies": null,
        "by_favourites": null
    }
    },
    "schema_version": 2,
    "share_url": "https://example.com/@Foobar/wrapstodon/2025/7fa0231c0f206390",
    "account_id": "55911"
}
```

## 속성 {#attributes}

### `year` {#year}

**설명:** 이 보고서의 연도입니다.\
**유형:** 정수\
**버전 이력:**\
4.3.0 - 추가

### `data` {#data}

**설명:** 보고서에 포함된 원시 데이터입니다. 데이터 스키마는 `schema_version` 값에 따라 달라집니다.\
**유형:** 해시\
**버전 이력:**\
4.3.0 - 추가\
4.6.0 - 스키마 버전 2 추가

#### `data[archetype]` {#data-archetype}

**설명:** 사용자에 해당하는 유형입니다. 한 해 동안의 게시 습관을 재미있고 대략적으로 보여 주기 위한 것입니다.\
**유형:** 문자열 (열거형, 다음 중 하나)\
`lurker` = 작성 예정\
`booster` = 작성 예정\
`pollster` = 작성 예정\
`replier` = 작성 예정\
`oracle` = 작성 예정\
**버전 이력:**\
4.3.0 - 추가

#### `data[type_distribution]` {#date-type_distribution}

**설명:** 한 해 동안의 사용자 게시물 통계 내역을 제공합니다. 스키마 버전 1에서만 사용할 수 있습니다.\
**유형:** 해시\
**버전 이력:**\
4.3.0 - 추가\
4.6.0 - 스키마 버전 2에서 제거

#### `data[top_statuses]` {#data-top_statuses}

**설명:** 한 해 동안 상호작용이 가장 많았던 게시물을 상호작용 유형(부스트, 좋아요, 답글)별로 제공합니다.\
**유형:** 해시\
**버전 이력:**\
4.3.0 - 추가\
4.6.0 - 스키마 버전 2에서 `by_reblogs`만 포함하고 조용한 공개 게시물도 표시할 수 있도록 변경

#### `data[most_used_apps] {#data-most_used_apps}

**설명:** 한 해 동안 사용자가 게시물을 올리는 데 가장 많이 사용한 앱 내역을 제공합니다. 스키마 버전 1에서만 사용할 수 있습니다.\
**유형:** 배열: 해시\
**버전 이력:**\
4.3.0 - 추가\
4.6.0 - 스키마 버전 2에서 제거

#### `data[commonly_interacted_with_accounts] {#data-commonly_interacted_with_accounts}

**설명:** 한 해 동안 사용자가 가장 자주 답글을 단 계정 내역을 제공합니다. 스키마 버전 1에서만 사용할 수 있습니다.\
**유형:** 배열: 해시\
**버전 이력:**\
4.3.0 - 추가\
4.6.0 - 스키마 버전 2에서 제거

#### `data[time_series] {#data-time_series}

**설명:** 월별 새 게시물, 팔로우, 팔로워 내역을 제공합니다.\
**유형:** 배열: 해시\
**버전 이력:**\
4.3.0 - 추가\
4.6.0 - 스키마 버전 2에서 `following`을 제거하도록 변경

#### `data[top_hashtags] {#data-top_hashtags}

**설명:** 한 해 동안 사용자가 가장 자주 사용한 해시태그 내역을 제공합니다.\
**유형:** 배열: 해시\
**버전 이력:**\
4.3.0 - 추가\
4.6.0 - 스키마 버전 2에서 해시태그 하나로 제한하도록 변경

#### `data[most_reblogged_accounts] {#data-most_reblogged_accounts}

**설명:** 한 해 동안 사용자가 가장 많이 부스트한 계정 내역을 제공합니다. 스키마 버전 1에서만 사용할 수 있습니다.\
**유형:** 배열: 해시\
**버전 이력:**\
4.3.0 - 추가\
4.6.0 - 스키마 버전 2에서 제거

#### `data[percentiles] {#data-percentiles}

**설명:** 동일 서버에서 게시물을 가장 많이 올린 사용자 중 해당 사용자가 속한 백분위입니다. 스키마 버전 1에서만 사용할 수 있습니다.\
**유형:** 실수\
**버전 이력:**\
4.3.0 - 추가\
4.6.0 - 스키마 버전 2에서 제거

### `schema_version` {#schema_version}

**설명:** 보고서의 스키마 버전으로, `data`를 해석하는 방법을 정의합니다.\
**유형:** 정수\
**버전 이력:**\
4.3.0 - 추가\
4.6.0 - 스키마 버전 2 추가

### `share_url` {#share_url}

**설명:** 보고서의 공유용 버전에 대한 선택적 링크입니다.\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
4.6.0 - 추가

### `account_id` {#account_id}

**설명:** 보고서 대상 계정 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.6.0 - 추가

## WrappedAnnualReports 엔터티 {#WrappedAnnualReports}

하나 이상의 [AnnualReport]({{< relref "entities/AnnualReport" >}})를 관련 [Account]({{< relref "entities/Account" >}}) 및 [Status]({{< relref "entities/Status" >}}) 엔터티와 함께 객체로 감쌉니다.

### 예시 {#example-1}

```json
{
  "annual_reports": [
    {
      "year": 2025,
      "data": {
        "archetype": "oracle",
        "time_series": [
          {
            "month": 12,
            "statuses": 7123,
            "followers": 48
          }
        ],
        "top_hashtags": [
          {
            "name": "Mastodon",
            "count": 12
          }
        ],
        "top_statuses": {
          "by_reblogs": "114348347829110933",
          "by_replies": null,
          "by_favourites": null
        }
      },
      "schema_version": 2,
      "share_url": "https://example.com/@Foobar/wrapstodon/2025/7fa0231c0f206390",
      "account_id": "55911"
    }
  ],
  "accounts": [
    /* Relevant Account entities */
  ],
  "statuses": [
    /* Relevant Status entities */
  ]
}
```

### `annual_reports` {#annual_reports}

**설명:** 보고서의 전체 AnnualReport 엔터티입니다.\
**유형:** 배열: [AnnualReport]({{< relref "entities/AnnualReport" >}})\
**버전 이력:**\
4.3.0 - 추가

### `accounts` {#accounts}

**설명:** 보고서에서 언급한 계정의 전체 Account 엔터티입니다.\
**유형:** 배열: [Account]({{< relref "entities/Account" >}})\
**버전 이력:**\
4.3.0 - 추가

### `statuses` {#statuses}

**설명:** 보고서에서 언급한 게시물의 전체 Status 엔터티입니다.\
**유형:** 배열: [Status]({{< relref "entities/Status" >}})\
**버전 이력:**\
4.3.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/annual_reports" caption="연간 보고서 API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/annual_report_serializer.rb" caption="app/serializers/rest/annual_report_serializer.rb" >}}
