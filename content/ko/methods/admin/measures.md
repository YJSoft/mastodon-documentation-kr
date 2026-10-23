---
title: 측정값 API 메서드
description: 서버에 대한 정량적 지표를 가져옵니다.
menu:
  docs:
    name: 측정값
    parent: methods-admin
    identifier: methods-admin-measures
aliases: [
  "/methods/admin/measures",
  "/api/methods/admin/measures",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 측정 데이터 가져오기 {#get}

```http
POST /api/v1/admin/measures HTTP/1.1
```

서버의 통계 측정값을 가져옵니다.

**반환:** 배열: [Admin::Measure]({{< relref "entities/Admin_Measure" >}})\
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

keys[]
: {{<required>}} 문자열 배열. 키 문자열로 특정 측정값을 요청합니다. 지원하는 측정값은 다음과 같습니다.
- `active_users` = 해당 기간 서버의 전체 활성 사용자 수
- `new_users` = 해당 기간 서버에 가입한 사용자 수
- `interactions` = 해당 기간 로컬 게시물의 총 상호작용 수(좋아요, 부스트, 답글)
- `opened_reports` = 해당 기간 제출된 총 신고 수
- `resolved_reports` = 해당 기간 해결된 총 신고 수
- `tag_accounts` = 해당 기간 하나 이상의 게시물에서 태그를 사용한 총 계정 수
- `tag_uses` = 해당 기간 태그를 사용한 총 게시물 수
- `tag_servers` = 해당 기간 태그를 사용한 게시물의 원본 원격 서버 총수
- `instance_accounts` = 해당 기간 원격 도메인에서 비롯된 총 계정 수
- `instance_media_attachments` = 해당 기간 원격 도메인의 미디어 첨부 파일이 사용한 총 공간
- `instance_reports` = 해당 기간 원격 도메인 계정에 대해 제출된 총 신고 수
- `instance_statuses` = 해당 기간 원격 도메인에서 비롯된 총 게시물 수
- `instance_follows` = 해당 기간 로컬 사용자가 팔로우한 원격 도메인 계정 총수
- `instance_followers` = 해당 기간 원격 도메인 계정이 팔로우한 로컬 계정 총수

start_at
: {{<required>}} 문자열([날짜와 시간](/api/datetime-format#datetime)). 기간의 시작일입니다. 시간을 제공해도 무시됩니다.

end_at
: {{<required>}} 문자열([날짜와 시간](/api/datetime-format#datetime)). 기간의 종료일입니다. 시간을 제공해도 무시됩니다.

tag_accounts[id]
: 문자열. 요청한 키에 `tag_accounts`가 있으면 지정한 기간에 하나 이상의 게시물에서 해당 해시태그를 사용한 계정 수를 측정하기 위해 태그 ID를 제공해야 합니다.

tag_uses[id]
: 문자열. 요청한 키에 `tag_uses`가 있으면 지정한 기간에 해당 해시태그를 사용한 게시물 수를 측정하기 위해 태그 ID를 제공해야 합니다.

tag_servers[id]
: 문자열. 요청한 키에 `tag_servers`가 있으면 지정한 기간에 하나 이상의 게시물에서 해당 해시태그를 사용한 서버 수를 측정하기 위해 태그 ID를 제공해야 합니다.

instance_accounts[domain]
: 문자열. 요청한 키에 `instance_accounts`가 있으면 지정한 기간에 해당 서버에서 발견된 계정 수를 측정하기 위해 원격 도메인을 제공해야 합니다.

instance_media_attachments[domain]
: 문자열. 요청한 키에 `instance_media_attachments`가 있으면 지정한 기간에 해당 서버의 미디어 첨부 파일이 사용하는 공간을 측정하기 위해 원격 도메인을 제공해야 합니다.

instance_reports[domain]
: 문자열. 요청한 키에 `instance_reports`가 있으면 지정한 기간에 해당 서버의 계정에 대해 제출된 신고 수를 측정하기 위해 원격 도메인을 제공해야 합니다.

instance_statuses[domain]
: 문자열. 요청한 키에 `instance_statuses`가 있으면 지정한 기간에 해당 서버에서 비롯된 게시물 수를 측정하기 위해 원격 도메인을 제공해야 합니다.

instance_follows[domain]
: 문자열. 요청한 키에 `instance_follows`가 있으면 지정한 기간에 로컬 계정이 해당 서버 계정에 수행한 팔로우 수를 측정하기 위해 원격 도메인을 제공해야 합니다.

instance_followers[domain]
: 문자열. 요청한 키에 `instance_followers`가 있으면 지정한 기간에 해당 서버 계정이 로컬 계정에 수행한 팔로우 수를 측정하기 위해 원격 도메인을 제공해야 합니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

각 측정값에 대해 전체 집계와 데이터 버킷별 정량적 데이터를 반환합니다.

```json
[
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
      // ...
    ]
  },
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
      // ...
    ]
  },
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
      // ...
    ]
  },
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
      // ...
    ]
  },
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
      // ...
    ]
  },
  {
    "key": "tag_accounts",
    "unit": null,
    "total": "1",
    "previous_total": "0",
    "data": [
      {
        "date": "2022-09-14T00:00:00Z",
        "value": "0"
      },
      // ...
    ]
  },
  {
    "key": "tag_uses",
    "unit": null,
    "total": "2",
    "previous_total": "0",
    "data": [
      {
        "date": "2022-09-14T00:00:00Z",
        "value": "0"
      },
      // ...
    ]
  },
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
      // ...
    ]
  },
  {
    "key": "instance_accounts",
    "unit": null,
    "total": "0",
    "data": [
      {
        "date": "2022-09-14T00:00:00.000+00:00",
        "value": "0"
      },
      // ...
    ]
  },
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
      // ...
    ]
  },
  {
    "key": "instance_reports",
    "unit": null,
    "total": "0",
    "data": [
      {
        "date": "2022-09-14T00:00:00.000+00:00",
        "value": "0"
      },
      // ...
    ]
  },
  {
    "key": "instance_statuses",
    "unit": null,
    "total": "0",
    "data": [
      {
        "date": "2022-09-14T00:00:00.000+00:00",
        "value": "0"
      },
      // ...
    ]
  },
  {
    "key": "instance_follows",
    "unit": null,
    "total": "0",
    "data": [
      {
        "date": "2022-09-14T00:00:00.000+00:00",
        "value": "0"
      },
      // ...
    ]
  },
  {
    "key": "instance_followers",
    "unit": null,
    "total": "0",
    "data": [
      {
        "date": "2022-09-14T00:00:00.000+00:00",
        "value": "0"
      },
      // ...
    ]
  }
]
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

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/admin/measures_controller.rb" caption="app/controllers/api/v1/admin/measures_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/admin/metrics/measure.rb" caption="app/lib/admin/metrics/measure.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/admin/metrics/measure/" caption="app/lib/admin/metrics/measure/" >}}