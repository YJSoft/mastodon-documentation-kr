---
title: 타임라인 API 메서드
description: 게시물 타임라인을 읽고 조회합니다.
menu:
  docs:
    name: 타임라인
    parent: methods
    identifier: methods-timelines
aliases: [
  "/methods/timelines",
  "/api/methods/timelines",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 공개 타임라인 조회 {#public}

```http
GET /api/v1/timelines/public HTTP/1.1
```

공개 게시물을 조회합니다.

**반환:** 배열: [Status]({{<relref "entities/status">}})\
**OAuth:** 공개. 서버에서 공개 미리보기를 비활성화했다면 앱 토큰 + `read:statuses` 필요.\
**버전 이력:**\
0.0.0 - 추가\
2.3.0 - `only_media` 추가\
2.6.0 - `min_id` 추가\
3.0.0 - 공개 미리보기가 비활성화되면 인증 필요\
3.1.4 - `remote` 추가\
3.3.0 - 이제 `min_id`와 `max_id` 동시 사용 가능\
4.5.0 - [접근 제어 설정]({{<relref "entities/Instance/#timelines_access-live_feeds">}}) 추가

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters}

local
: 불리언. 로컬 게시물만 표시할지 여부입니다. 기본값은 false입니다.

remote
: 불리언. 원격 게시물만 표시할지 여부입니다. 기본값은 false입니다.

only_media
: 불리언. 미디어가 첨부된 게시물만 표시할지 여부입니다. 기본값은 false입니다.

max_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 작습니다. 결과의 상한을 설정합니다.

since_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 큽니다. 결과의 하한을 설정합니다.

min_id
: 문자열. 이 ID보다 바로 다음으로 새로운 결과를 반환합니다. 이 ID에 커서를 설정하고 앞으로 페이지를 이동합니다.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 게시물 20개이며 최대 40개입니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

limit=2인 API 호출 예입니다.

```json
[
  {
    "id": "103206804533200177",
    "created_at": "2019-11-26T23:27:31.000Z",
    // ...
    "visibility": "public",
    // ...
  },
  {
    "id": "103206804086086361",
    "created_at": "2019-11-26T23:27:32.000Z",
    // ...
    "visibility": "public",
    // ...
  }
]
```

참고: 피드가 비활성화되면 반환 배열이 비어 있을 수 있습니다. [서버 구성 속성]({{<relref "entities/Instance/#timelines_access-live_feeds" >}})을 참고하세요.

##### 401: 인증되지 않음 {#401-unauthorized}

서버가 공개 타임라인에 대한 인증 없는 접근을 비활성화하도록 설정되었는데 Authorization 헤더가 없거나 유효하지 않은 경우입니다. 이 타임라인의 원격 게시물에 대한 인증 없는 접근이 비활성화되면 `local`이 true가 아닌 한 이 엔드포인트에 대한 인증되지 않은 요청은 401로 실패합니다. 로컬 게시물에 대한 인증 없는 접근과 `remote` 매개변수도 같은 방식으로 적용됩니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 해시태그 타임라인 조회 {#tag}

```http
GET /api/v1/timelines/tag/:hashtag HTTP/1.1
```

지정한 해시태그를 포함하는 공개 게시물을 조회합니다.

**반환:** 배열: [Status]({{<relref "entities/status">}})\
**OAuth:** 공개. 서버에서 공개 미리보기를 비활성화했다면 앱 토큰 + `read:statuses` 필요.\
**버전 이력:**\
0.0.0 - 추가\
2.3.0 - `only_media` 추가\
2.6.0 - `min_id` 추가\
2.7.0 - 추가 태그를 위한 `any[]`, `all[]`, `none[]` 추가\
3.0.0 - 공개 미리보기가 비활성화되면 인증 필요\
3.3.0 - 이제 `min_id`와 `max_id` 동시 사용 가능. `remote` 추가\
4.5.0 - [접근 제어 설정]({{<relref "entities/Instance/#timelines_access-hashtag_feeds">}}) 추가

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters}

:hashtag
: {{<required>}} 문자열. 해시태그 이름입니다(# 기호 제외).

##### 헤더 {#headers-1}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-1}

{{< hint style="info" >}}
각 쿼리 매개변수에서 적용할 태그 수에는 제한이 있습니다(기본값은 총 4개 태그). `any`, `all`, `none` 매개변수를 사용할 때 참고하세요.
{{</ hint >}}

any[]
: 문자열 배열. 이 추가 태그 중 하나라도 포함하는 게시물을 반환합니다.

all[]
: 문자열 배열. 이 추가 태그를 모두 포함하는 게시물을 반환합니다.

none[]
: 문자열 배열. 이 추가 태그를 하나도 포함하지 않는 게시물을 반환합니다.

local
: 불리언. 로컬 게시물만 반환할지 여부입니다. 기본값은 false입니다.

remote
: 불리언. 원격 게시물만 반환할지 여부입니다. 기본값은 false입니다.

only_media
: 불리언. 미디어 첨부 파일이 있는 게시물만 반환할지 여부입니다. 기본값은 false입니다.

max_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 작습니다. 결과의 상한을 설정합니다.

since_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 큽니다. 결과의 하한을 설정합니다.

min_id
: 문자열. 이 ID보다 바로 다음으로 새로운 결과를 반환합니다. 이 ID에 커서를 설정하고 앞으로 페이지를 이동합니다.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 게시물 20개이며 최대 40개입니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

해시태그 #cats와 limit=2를 사용한 타임라인 예입니다.

```json
[
  {
    "id": "103206185588894565",
    "created_at": "2019-11-26T20:50:15.866Z",
    // ...
    "visibility": "public",
    // ...
    "content": "<p><a href=\"https://mastodon.social/tags/cats\" class=\"mention hashtag\" rel=\"tag\">#<span>cats</span></a></p>",
    // ...
    "tags": [
      {
        "name": "cats",
        "url": "https://mastodon.social/tags/cats"
      }
    ],
    // ...
  },
  {
    "id": "103203659567597966",
    "created_at": "2019-11-26T10:07:49.000Z",
    // ...
    "visibility": "public",
    // ...
    "content": "<p>Caught on the hop. 😺 </p><p><a href=\"https://chaos.social/tags/Qualit%C3%A4tskatzen\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>Qualitätskatzen</span></a> <a href=\"https://chaos.social/tags/cats\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>cats</span></a> <a href=\"https://chaos.social/tags/mastocats\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>mastocats</span></a> <a href=\"https://chaos.social/tags/catsofmastodon\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>catsofmastodon</span></a> <a href=\"https://chaos.social/tags/Greece\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>Greece</span></a> <a href=\"https://chaos.social/tags/Agistri\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>Agistri</span></a><br>(photo: <span class=\"h-card\"><a href=\"https://chaos.social/@kernpanik\" class=\"u-url mention\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>kernpanik</span></a></span> | license: CC BY-NC-SA 4.0)</p>",
    // ...
    "tags": [
      {
        "name": "qualitätskatzen",
        "url": "https://mastodon.social/tags/qualit%C3%A4tskatzen"
      },
      {
        "name": "cats",
        "url": "https://mastodon.social/tags/cats"
      },
      {
        "name": "mastocats",
        "url": "https://mastodon.social/tags/mastocats"
      },
      {
        "name": "catsofmastodon",
        "url": "https://mastodon.social/tags/catsofmastodon"
      },
      {
        "name": "greece",
        "url": "https://mastodon.social/tags/greece"
      },
      {
        "name": "agistri",
        "url": "https://mastodon.social/tags/agistri"
      }
    ],
    // ...
  }
]
```

참고: 일치하는 태그가 없거나 피드가 비활성화되면 반환 배열이 비어 있을 수 있습니다. [서버 구성 속성]({{<relref "entities/Instance/#timelines_access-hashtag_feeds" >}})을 참고하세요.

##### 401: 인증되지 않음 {#401-unauthorized-1}

서버가 해시태그 타임라인에 대한 인증 없는 접근을 비활성화하도록 설정되었는데 Authorization 헤더가 없거나 유효하지 않은 경우입니다.

```json
{
  "error": "The access token is invalid"
}
```

## 홈 타임라인 조회 {#home}

```http
GET /api/v1/timelines/home HTTP/1.1
```

팔로우하는 사용자와 해시태그의 게시물을 조회합니다.

**반환:** 배열: [Status]({{<relref "entities/status">}})\
**OAuth:** 사용자 + `read:statuses`\
**버전 이력:**\
0.0.0 - 추가\
2.6.0 - `min_id` 추가\
3.3.0 - 이제 `min_id`와 `max_id` 동시 사용 가능\
4.0.0 - 이제 사용자가 해시태그를 팔로우할 수 있으므로 팔로우하지 않는 사용자의 게시물도 타임라인에 표시될 수 있음\
5.0.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 12) - `exclude_direct`, `exclude_reblogs`, `exclude_quotes` 및 `exclude_replies` 매개변수 추가\

#### 요청 {#request-2}

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-2}

max_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 작습니다. 결과의 상한을 설정합니다.

since_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 큽니다. 결과의 하한을 설정합니다.

min_id
: 문자열. 이 ID보다 바로 다음으로 새로운 결과를 반환합니다. 이 ID에 커서를 설정하고 앞으로 페이지를 이동합니다.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 게시물 20개이며 최대 40개입니다.

exclude_direct
: 불리언. 응답에서 개인 멘션을 제외할지 여부입니다.

exclude_reblogs
: 불리언. 응답에서 부스트를 제외할지 여부입니다.

exclude_quotes
: 불리언. 응답에서 인용 게시물을 제외할지 여부입니다.

exclude_replies
: 불리언. 응답에서 답글을 제외할지 여부입니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

홈 타임라인의 게시물을 반환합니다.

```json
[
  {
    "id": "103206791453397862",
    "created_at": "2019-11-26T23:24:13.113Z",
    // ...
  },
  // ...
]
```

##### 206: 부분 콘텐츠 {#206-partial-content}

홈 피드를 다시 생성 중입니다.

##### 401: 인증되지 않음 {#401-unauthorized-2}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 링크 타임라인 조회 {#link}

```http
GET /api/v1/timelines/link?url=:url HTTP/1.1
```

지정한 현재 인기 기사의 링크를 포함하는 공개 게시물을 조회합니다. 검색 및 탐색 기능에 동의한 사람의 게시물만 나열합니다.

**반환:** 배열: [Status]({{<relref "entities/status">}})\
**OAuth:** 공개. 서버에서 공개 미리보기를 비활성화했다면 앱 토큰 + `read:statuses` 필요.\
**버전 이력:**\
4.3.0 - 추가\
4.5.0 - [접근 제어 설정]({{<relref "entities/Instance/#timelines_access-trending_link_feeds">}}) 추가

#### 요청 {#request-3}

##### 헤더 {#headers-3}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-3}

url
: {{<required>}} 문자열. 인기 기사의 URL입니다.

max_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 작습니다. 결과의 상한을 설정합니다.

since_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 큽니다. 결과의 하한을 설정합니다.

min_id
: 문자열. 이 ID보다 바로 다음으로 새로운 결과를 반환합니다. 이 ID에 커서를 설정하고 앞으로 페이지를 이동합니다.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 게시물 20개이며 최대 40개입니다.

#### 응답 {#response-3}

##### 200: 성공 {#200-ok-3}

limit=2인 API 호출 예입니다.

```json
[
  {
    "id": "103206804533200177",
    "created_at": "2019-11-26T23:27:31.000Z",
    // ...
    "visibility": "public",
    // ...
  },
  {
    "id": "103206804086086361",
    "created_at": "2019-11-26T23:27:32.000Z",
    // ...
    "visibility": "public",
    // ...
  }
]

```
참고: 피드가 비활성화되면 반환 배열이 비어 있을 수 있습니다. [서버 구성 속성]({{<relref "entities/Instance/#timelines_access-trending_link_feeds" >}})을 참고하세요.

##### 404: 찾을 수 없음 {#404-not-found}

제공한 URL은 현재 인기 링크가 아닙니다.

```json
{
  "error": "Record not found"
}
```

##### 401: 인증되지 않음 {#401-unauthorized-3}

서버가 링크 타임라인에 대한 인증 없는 접근을 비활성화하도록 설정되었는데 Authorization 헤더가 없거나 유효하지 않은 경우입니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 리스트 타임라인 조회 {#list}

```http
GET /api/v1/timelines/list/:list_id HTTP/1.1
```

지정한 리스트 타임라인의 게시물을 조회합니다.

**반환:** 배열: [Status]({{<relref "entities/status">}})\
**OAuth:** 사용자 토큰 + `read:lists`\
**버전 이력:**\
2.1.0 - 추가\
2.6.0 - `min_id` 추가\
3.3.0 - 이제 `min_id`와 `max_id` 동시 사용 가능

#### 요청 {#request-4}

##### 경로 매개변수 {#path-parameters-1}

:list_id
: {{<required>}} 문자열. 데이터베이스의 List 로컬 ID입니다.

##### 헤더 {#headers-4}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-4}

max_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 작습니다. 결과의 상한을 설정합니다.

since_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 큽니다. 결과의 하한을 설정합니다.

min_id
: 문자열. 이 ID보다 바로 다음으로 새로운 결과를 반환합니다. 이 ID에 커서를 설정하고 앞으로 페이지를 이동합니다.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 게시물 20개이며 최대 40개입니다.

#### 응답 {#response-4}
##### 200: 성공 {#200-ok-4}

이 리스트의 게시물을 반환합니다.

```json
[
  {
    "id": "103206791453397862",
    "created_at": "2019-11-26T23:24:13.113Z",
    // ...
  },
  // ...
]
```

##### 401: 인증되지 않음 {#401-unauthorized-4}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-1}

리스트가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

## 개인 멘션 타임라인 조회 {{%deprecated%}} {#direct}

```http
GET /api/v1/timelines/direct HTTP/1.1
```

내 계정 또는 내 알림에 있는 "direct" 공개 범위의 게시물을 조회합니다.

**반환:** 배열: [Status]({{<relref "entities/status">}})\
**OAuth:** 사용자 토큰 + `read:statuses`\
**버전 이력:**\
x.x.x - 추가\
2.6.0 - `min_id` 추가. [대화 API]({{<relref "methods/conversations">}})를 권장하며 사용 중단 예정\
3.0.0 - 제거

#### 요청 {#request-5}
##### 헤더 {#headers-5}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-5}

max_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 작습니다. 결과의 상한을 설정합니다.

since_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 큽니다. 결과의 하한을 설정합니다.

min_id
: 문자열. 이 ID보다 바로 다음으로 새로운 결과를 반환합니다. 이 ID에 커서를 설정하고 앞으로 페이지를 이동합니다.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 게시물 20개이며 최대 40개입니다.

#### 응답 {#response-5}
##### 200: 성공 {#200-ok-5}

내가 작성했거나 나를 멘션한 direct 공개 범위의 게시물입니다. 대화별로 그룹화하지 않고 시간순으로 반환합니다.

```json
[
  {
    "id": "103206185588894565",
    "created_at": "2019-11-26T20:50:15.866Z",
    // ...
    "visibility": "direct",
    // ...
  },
  // ...
]
```

##### 401: 인증되지 않음 {#401-unauthorized-5}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 함께 보기 {#see-also}

{{< page-relref ref="entities/Instance/#timelines_access" caption="Instance#configuration[timeline_access]" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/timelines/home_controller.rb" caption="app/controllers/api/v1/timelines/home_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/timelines/list_controller.rb" caption="app/controllers/api/v1/timelines/list_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/timelines/public_controller.rb" caption="app/controllers/api/v1/timelines/public_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/timelines/tag_controller.rb" caption="app/controllers/api/v1/timelines/tag_controller.rb" >}}
