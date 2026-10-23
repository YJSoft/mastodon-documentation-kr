---
title: 차원 API 메서드
description: 서버에 대한 정성적 지표를 가져옵니다.
menu:
  docs:
    name: 차원
    parent: methods-admin
    identifier: methods-admin-dimensions
aliases: [
  "/methods/admin/dimensions",
  "/api/methods/admin/dimensions",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 차원 데이터 가져오기 {#get}

```http
POST /api/v1/admin/dimensions HTTP/1.1
```

특정 계정, 서버, 언어 등의 인기도에 대한 정보를 가져옵니다.

**반환:** 배열: [Admin::Dimension]({{< relref "entities/Admin_Dimension" >}})\
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
: {{<required>}} 문자열 배열. 키 문자열로 특정 차원을 요청합니다. 지원하는 차원은 다음과 같습니다.
- `languages` = 이 서버에서 가장 많이 사용하는 언어
- `sources` = 이 서버에서 가장 많이 사용하는 클라이언트 앱
- `servers` = 게시물이 가장 많은 원격 서버
- `space_usage` = 소프트웨어 스택이 사용하는 공간
- `software_versions` = 소프트웨어 스택의 버전 번호
- `tag_servers` = 인기 태그를 포함하는 게시물이 가장 많은 서버
- `tag_languages` = 인기 태그를 포함하는 게시물에서 가장 많이 사용하는 언어
- `instance_accounts` = 원격 서버에서 팔로워가 가장 많은 계정
- `instance_languages` = 원격 서버에서 가장 많이 사용하는 언어

start_at
: 문자열([날짜와 시간](/api/datetime-format#datetime)). 기간의 시작일입니다. 시간을 제공해도 무시됩니다.

end_at
: 문자열([날짜와 시간](/api/datetime-format#datetime)). 기간의 종료일입니다. 시간을 제공해도 무시됩니다.

limit
: 정수. 출처, 서버, 언어, 태그 또는 서버 차원에 대해 반환할 최대 결과 수입니다.

tag_servers[id]
: 문자열. 요청한 키에 `tag_servers`가 있으면 어떤 서버에서 해당 태그를 게시하는지 알아보기 위해 인기 태그 ID를 제공해야 합니다.

tag_languages[id]
: 문자열. 요청한 키에 `tag_languages`가 있으면 어떤 언어로 해당 태그를 게시하는지 알아보기 위해 인기 태그 ID를 제공해야 합니다.

instance_accounts[domain]
: 문자열. 요청한 키에 `instance_accounts`가 있으면 해당 서버의 인기 계정 정보를 얻기 위해 도메인을 제공해야 합니다.

instance_languages[domain]
: 문자열. 요청한 키에 `instance_accounts`가 있으면 해당 서버의 인기 언어 정보를 얻기 위해 도메인을 제공해야 합니다.

#### 응답 {#response}

##### 200: 성공 {#200-ok}

mastodon.social과 지정한 인기 태그에 대한 데이터를 결과 수 제한 2개로 요청합니다.

```json
[
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
      }
    ]
  },
  {
    "key": "sources",
    "data": [
      {
        "key": "web",
        "human_key": "Website",
        "value": "3"
      }
    ]
  },
  {
    "key": "servers",
    "data": [
      {
        "key": "botsin.space",
        "human_key": "botsin.space",
        "value": "13738"
      },
      {
        "key": "monads.online",
        "human_key": "monads.online",
        "value": "8928"
      }
    ]
  },
  {
    "key": "space_usage",
    "data": [
      {
        "key": "postgresql",
        "human_key": "PostgreSQL",
        "value": "49581359907",
        "unit": "bytes",
        "human_value": "46.2 GB"
      },
      {
        "key": "redis",
        "human_key": "Redis",
        "value": "100765744",
        "unit": "bytes",
        "human_value": "96.1 MB"
      },
      {
        "key": "media",
        "human_key": "Media storage",
        "value": "837837315424",
        "unit": "bytes",
        "human_value": "780 GB"
      }
    ]
  },
  {
    "key": "software_versions",
    "data": [
      {
        "key": "mastodon",
        "human_key": "Mastodon",
        "value": "3.5.1+chitter",
        "human_value": "3.5.1+chitter"
      },
      {
        "key": "ruby",
        "human_key": "Ruby",
        "value": "3.0.3p157",
        "human_value": "3.0.3p157"
      },
      {
        "key": "postgresql",
        "human_key": "PostgreSQL",
        "value": "14.3",
        "human_value": "14.3"
      },
      {
        "key": "redis",
        "human_key": "Redis",
        "value": "6.2.7",
        "human_value": "6.2.7"
      }
    ]
  },
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
      }
    ]
  },
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
      }
    ]
  },
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
  },
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
      }
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

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/admin/dimensions_controller.rb" caption="app/controllers/api/v1/admin/dimensions_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/admin/metrics/dimension.rb" caption="app/lib/admin/metrics/dimension.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/admin/metrics/dimension/" caption="app/lib/admin/metrics/dimension/" >}}