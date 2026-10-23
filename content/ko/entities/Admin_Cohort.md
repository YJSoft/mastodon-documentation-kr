---
title: 관리자용 코호트 (Admin::Cohort)
description: 유지율 지표를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/admin-cohort",
  "/entities/Admin-Cohort",
  "/entities/admin_cohort",
  "/entities/Admin_Cohort",
  "/api/entities/admin-cohort",
  "/api/entities/Admin-Cohort",
  "/api/entities/admin_cohort",
  "/api/entities/Admin_Cohort",
]
---

## 예시 {#example}

2022-09에 사용자 2명이 가입하여 해당 월에 한 번 이상 활동했다고 가정할 때의 2022-09 월간 유지율 데이터입니다.

```json
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
```

2022-09-08에 사용자 2명이 가입하고 그중 1명이 2022-09-09 이후 활동을 중단했다고 가정할 때, 2022-09-08부터 2022-09-14까지의 주간 일별 유지율 데이터입니다.

```json
{
	"period": "2022-09-08T00:00:00+00:00",
	"frequency": "day",
	"data": [
		{
			"date": "2022-09-08T00:00:00+00:00",
			"rate": 1.0,
			"value": "2"
		},
		{
			"date": "2022-09-09T00:00:00+00:00",
			"rate": 1.0,
			"value": "2"
		},
		{
			"date": "2022-09-10T00:00:00+00:00",
			"rate": 0.5,
			"value": "1"
		},
		{
			"date": "2022-09-11T00:00:00+00:00",
			"rate": 0.5,
			"value": "1"
		},
		{
			"date": "2022-09-12T00:00:00+00:00",
			"rate": 0.5,
			"value": "1"
		},
		{
			"date": "2022-09-13T00:00:00+00:00",
			"rate": 0.5,
			"value": "1"
		},
		{
			"date": "2022-09-14T00:00:00+00:00",
			"rate": 0.5,
			"value": "1"
		}
	]
}
```

## 속성 {#attributes}

### `period` {#period}

**설명:** 기간 시작일 자정의 타임스탬프입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
3.5.0 - 추가

### `frequency` {#frequency}

**설명:** 반환한 데이터의 버킷 크기입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`day` = 일별 버킷\
`month` = 월별 버킷\
**버전 이력:**\
3.5.0 - 추가

### `data` {#data}

**설명:** 주어진 기간에 가입한 사용자의 유지율 데이터입니다.\
**유형:** 배열: [CohortData](#CohortData)\
**버전 이력:**\
3.5.0 - 추가

## CohortData 엔터티 속성 {#CohortData}

### `date` {#date}

**설명:** 버킷 시작일 자정의 타임스탬프입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
3.5.0 - 추가

### `rate` {#rate}

**설명:** 지정한 `period`에 가입하고 주어진 `date` 버킷에 활동한 사용자의 비율(백분율)입니다.\
**유형:** 숫자\
**버전 이력:**\
3.5.0 - 추가

### `value` {#value}

**설명:** 지정한 `period`에 가입하고 주어진 `date` 버킷에 활동한 사용자 수입니다.\
**유형:** 문자열 (정수에서 변환)\
**버전 이력:**\
3.5.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/admin/retention" caption="admin/retention API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/admin/cohort_serializer.rb" caption="app/serializers/rest/admin/cohort_serializer.rb" >}}
