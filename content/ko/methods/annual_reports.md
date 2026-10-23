---
title: 연간 보고서(Wrapstodon) API
description: Wrapstodon 보고서를 생성하고 가져옵니다.
menu:
  docs:
    name: 연간 보고서
    parent: methods
    identifier: methods-annual-reports
aliases: [
  "/methods/annual_reports",
  "/api/methods/annual_reports",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

이 페이지는 사용자 인터페이스에서 “Wrapstodon”이라고도 부르는 연간 보고서에 관한 설명입니다.
서버 관리자가 활성화하면 사용자는 현재 저장되어 있는 연간 활동을 공유 가능한 보고서로 모을 수 있습니다. 선택적 기능입니다.
이 기능은 매년 12월 10일부터 31일까지 충분한 활동이 있는 사용자에게 제공됩니다.

## 모든 연간 보고서 가져오기 {#index}

```http
GET /api/v1/annual_reports HTTP/1.1
```

현재 사용자가 생성한 연간 보고서가 있으면 모두 반환합니다.

**반환:** [WrappedAnnualReports]({{< relref "entities/AnnualReport#WrappedAnnualReports" >}})\
**OAuth:** 사용자 토큰 + `read:accounts`\
**버전 이력:**\
4.3.0 - 추가

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

#### 응답 {#response}

##### 200: 성공 {#200-ok}

현재 사용자가 생성한 모든 보고서가 담긴 [WrappedAnnualReports]({{< relref "entities/AnnualReport#WrappedAnnualReports" >}})입니다.

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
    },
    {
      "year": 2026,
      "data": {
        "archetype": "oracle",
        "time_series": [
          {
            "month": 12,
            "statuses": 6241,
            "followers": 42
          }
        ],
        "top_hashtags": [
          {
            "name": "Cats",
            "count": 13
          }
        ],
        "top_statuses": {
          "by_reblogs": "116680004222523313",
          "by_replies": null,
          "by_favourites": null
        }
      },
      "schema_version": 2,
      "share_url": "https://example.com/@Foobar/wrapstodon/2026/dd6a5b58ec0e3c12",
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

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

## 연간 보고서 하나 가져오기 {#get}

```http
GET /api/v1/annual_reports/:year HTTP/1.1
```

지정한 연도에 대해 현재 사용자가 생성한 연간 보고서가 있으면 반환합니다.

**반환:** [WrappedAnnualReports]({{< relref "entities/AnnualReport#WrappedAnnualReports" >}})\
**OAuth:** 사용자 토큰 + `read:accounts`\
**버전 이력:**\
4.4.0 - 추가

#### 요청 {#request-1}

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

##### 경로 매개변수 {#path-parameters}

:year
: {{<required>}} 문자열. 연간 보고서의 연도입니다.

#### 응답 {#response-1}

##### 200: 성공 {#200-ok-1}

요청한 연도의 보고서 하나가 담긴 [WrappedAnnualReports]({{< relref "entities/AnnualReport#WrappedAnnualReports" >}})입니다.

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

##### 401: 인증되지 않음 {#401-unauthorized-1}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found}

현재 사용자는 요청한 연도에 대해 생성된 보고서가 없습니다.

## 연간 보고서 상태 가져오기 {#get-state}

```http
GET /api/v1/annual_reports/:year/state HTTP/1.1
```

현재 사용자와 지정한 연도의 연간 보고서 상태를 반환합니다.

**반환:** `state` 키 하나가 있고 값은 문자열(열거형, `available`, `generating`, `eligible`, `ineligible` 중 하나)인 해시\
**OAuth:** 사용자 토큰 + `read:accounts`\
**버전 이력:**\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 8) - 추가

#### 요청 {#request-2}

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

##### 경로 매개변수 {#path-parameters-1}

:year
: {{<required>}} 문자열. 연간 보고서의 연도입니다.

#### 응답 {#response-2}

##### 200: 성공 {#200-ok-2}

요청한 연도의 보고서 하나가 담긴 [WrappedAnnualReports]({{< relref "entities/AnnualReport#WrappedAnnualReports" >}})입니다.

```json
{
  "state": "available"
}
```

##### 401: 인증되지 않음 {#401-unauthorized-2}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

## 연간 보고서를 읽음으로 표시 {#read}

```http
POST /api/v1/annual_reports/:year/read HTTP/1.1
```

지정한 연도에 대해 사용자가 생성한 연간 보고서를 읽음으로 표시합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:accounts`\
**버전 이력:**\
4.3.0 - 추가

#### 요청 {#request-3}

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

##### 경로 매개변수 {#path-parameters-2}

:year
: {{<required>}} 문자열. 연간 보고서의 연도입니다.

#### 응답 {#response-3}

##### 200: 성공 {#200-ok-3}

연간 보고서를 읽음으로 표시했습니다.

##### 401: 인증되지 않음 {#401-unauthorized-3}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-1}

현재 사용자는 지정한 연도에 대해 생성된 보고서가 없습니다.

## 새 연간 보고서 생성 {generate} {#generate-a-new-annual-report-generate}

```http
POST /api/v1/annual_reports/:year/generate HTTP/1.1
```

지정한 연도에 대한 사용자의 연간 보고서를 생성합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:accounts`\
**버전 이력:**\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 8) - 추가

#### 요청 {#request-4}

##### 헤더 {#headers-4}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

##### 경로 매개변수 {#path-parameters-3}

:year
: {{<required>}} 문자열. 연간 보고서의 연도입니다.

#### 응답 {#response-4}

##### 200: 성공 {#200-ok-4}

요청한 연간 보고서가 이미 생성되었거나 생성 대상이 아닙니다.

##### 202: 접수됨 {#202-accepted}

요청한 연간 보고서를 생성 중입니다.

##### 401: 인증되지 않음 {#401-unauthorized-4}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/annual_reports_controller.rb" caption="app/controllers/api/v1/annual_reports_controller.rb" >}}
