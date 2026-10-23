---
title: 유지율 API 메서드
description: 시간에 따른 유지율 데이터를 표시합니다.
menu:
  docs:
    name: 유지율
    parent: methods-admin
    identifier: methods-admin-retention
aliases: [
  "/methods/admin/retention",
  "/api/methods/admin/retention",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 유지율 데이터 계산 {#create}

```http
POST /api/v1/admin/retention HTTP/1.1
```

지정한 기간과 버킷에 대한 유지율 데이터 보고서를 생성합니다.

**반환:** 배열: [Admin::Cohort]({{< relref "entities/Admin_Cohort" >}})\
**OAuth:** 사용자 토큰 + `admin:read`\
**권한:** 대시보드 조회\
**버전 이력:**\
3.5.0 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

start_at
: {{<required>}} 문자열([날짜와 시간](/api/datetime-format#datetime)). 기간의 시작일입니다. 시간을 제공해도 무시됩니다.

end_at
: {{<required>}} 문자열([날짜와 시간](/api/datetime-format#datetime)). 기간의 종료일입니다. 시간을 제공해도 무시됩니다.

frequency
: {{<required>}} 문자열(열거형 중 하나). 집계 단위를 `day` 또는 `month`로 지정합니다. 다른 값을 제공하면 기본값인 `day`를 사용합니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

2022-09에 사용자 2명이 가입했고 해당 월에 한 번 이상 활동한 경우의 2022-09 월별 유지율 데이터입니다.

```json
[
	{
		"period": "2022-09-01T00:00:00+00:00",
		"frequency": "month",
		"data": [
			{
					"date": "2022-09-01T00:00:00+00:00",
					"rate": 1.0,
					"value": "2"
			}
		]
	}
]
```

2022-09-08에 사용자 2명이 가입했고 그중 1명이 2022-09-09 이후 활동을 중단한 경우의 2022-09-08부터 2022-09-14까지 일주일간 일별 유지율 데이터입니다.

```json
[
  {
    "period": "2022-09-08T00:00:00+00:00",
    "frequency": "day",
    "data": [
      {
        "date": "2022-09-08T00:00:00+00:00",
        "rate": 1,
        "value": "2"
      },
      {
        "date": "2022-09-09T00:00:00+00:00",
        "rate": 1,
        "value": "2"
      },
      {
        "date": "2022-09-10T00:00:00+00:00",
        "rate": 0.5,
        "value": "1"
      },
      // ...
      {
        "date": "2022-09-14T00:00:00+00:00",
        "rate": 0.5,
        "value": "1"
      }
    ]
  },
  {
    "period": "2022-09-09T00:00:00+00:00",
    "frequency": "day",
    "data": [
      {
        "date": "2022-09-09T00:00:00+00:00",
        "rate": 0,
        "value": "0"
      },
		// ...
      {
        "date": "2022-09-14T00:00:00+00:00",
        "rate": 0,
        "value": "0"
      }
    ]
  },
  {
    "period": "2022-09-10T00:00:00+00:00",
    "frequency": "day",
    "data": [
      {
        "date": "2022-09-10T00:00:00+00:00",
        "rate": 0,
        "value": "0"
      },
		// ...
      {
        "date": "2022-09-14T00:00:00+00:00",
        "rate": 0,
        "value": "0"
      }
    ]
  },
  // ...
  {
    "period": "2022-09-14T00:00:00+00:00",
    "frequency": "day",
    "data": [
      {
        "date": "2022-09-14T00:00:00+00:00",
        "rate": 0,
        "value": "0"
      }
    ]
  }
]
```

매개변수가 하나라도 누락되면 코호트 계산이 실패하고 빈 배열을 반환합니다.

```json
[]
```

##### 403: 금지됨 {#403-forbidden}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/admin/retention_controller.rb" caption="app/controllers/api/v1/admin/retention_controller.rb" >}}