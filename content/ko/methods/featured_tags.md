---
title: 추천 태그 API 메서드
description: 자주 사용하는 태그를 프로필에서 추천합니다.
menu:
  docs:
    name: 추천 태그
    parent: methods-accounts
    identifier: methods-featured_tags
aliases: [
  "/methods/featured_tags",
  "/api/methods/featured_tags",
  "/methods/accounts/featured_tags",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 추천 태그 조회 {#get}

```http
GET /api/v1/featured_tags HTTP/1.1
```

프로필에서 추천하는 모든 해시태그를 나열합니다.

**반환:** 배열: [FeaturedTag]({{< relref "entities/featuredtag" >}})\
**OAuth:** 사용자 토큰 + `read:accounts`\
**버전 이력:**\
3.0.0 - 추가

#### 요청 {#request}
##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

{{< hint style="info" >}}
이 응답 항목의 `id` 속성은 [FeaturedTag]({{< relref "entities/featuredtag" >}}) 엔터티를 가리키며 [Tag]({{< relref "entities/tag" >}}) 엔터티의 `id`가 아닙니다.
{{< /hint >}}

```json
[
  {
    "id": "627",
    "name": "nowplaying",
    "url": "https://mastodon.social/@trwnh/tagged/nowplaying",
    "statuses_count": 70,
    "last_status_at": "2022-08-29T12:03:35.061Z"
  }
]
```

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 태그 추천 {#feature}

```http
POST /api/v1/featured_tags HTTP/1.1
```

프로필에서 해시태그를 추천합니다.

**반환:** [FeaturedTag]({{< relref "entities/featuredtag" >}})\
**OAuth:** 사용자 토큰 + `write:accounts`\
**버전 이력:**\
3.0.0 - 추가

#### 요청 {#request-1}
##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

name
: {{<required>}} 문자열. 추천할 해시태그이며 해시 기호는 제외합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

지정한 `name`으로 FeaturedTag를 생성합니다.

```json
{
  "id": "13174",
  "name": "circasurvive",
  "url": "https://mastodon.social/@trwnh/tagged/circasurvive",
  "statuses_count": 23,
  "last_status_at": "2021-10-22T14:47:35.357Z"
}
```

##### 401: 인증되지 않음 {#401-unauthorized-1}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

`name`이 유효한 해시태그가 아닌 경우입니다. 예를 들어 허용되지 않는 문자가 있거나 숫자로만 이루어진 경우입니다.

```json
{
  "error": "Validation failed: Tag is invalid"
}
```

---

## 태그 추천 해제 {#unfeature}

```http
DELETE /api/v1/featured_tags/:id HTTP/1.1
```

프로필에서 해시태그 추천을 중단합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:accounts`\
**버전 이력:**\
3.0.0 - 추가

#### 요청 {#request-2}

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 데이터베이스의 FeaturedTag ID입니다.

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

태그 추천을 해제했습니다.

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-2}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found}

FeaturedTag가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

## 추천할 만한 태그 조회 {#suggestions}

```http
GET /api/v1/featured_tags/suggestions HTTP/1.1
```

최근에 사용한 태그를 최대 10개 표시합니다.

**반환:** 배열: [Tag]({{< relref "entities/Tag" >}})\
**OAuth:** 사용자 토큰 + `read:accounts`\
**버전 이력:**\
3.0.0 - 추가

#### 요청 {#request-3}
##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-3}
##### 200: 성공 {#200-ok-3}

첫 번째와 마지막 태그만 남긴 결과입니다.

```json
[
  {
    "id": "4325",
    "name": "nowplaying",
    "url": "https://mastodon.social/tags/nowplaying",
    "history": [
      {
        "day": "1574553600",
        "uses": "200",
        "accounts": "31"
      },
      {
        "day": "1574467200",
        "uses": "272",
        "accounts": "39"
      },
      {
        "day": "1574380800",
        "uses": "345",
        "accounts": "40"
      },
      {
        "day": "1574294400",
        "uses": "366",
        "accounts": "46"
      },
      {
        "day": "1574208000",
        "uses": "226",
        "accounts": "32"
      },
      {
        "day": "1574121600",
        "uses": "217",
        "accounts": "42"
      },
      {
        "day": "1574035200",
        "uses": "214",
        "accounts": "34"
      }
    ]
  },
  // ...
  {
    "id": "1684",
    "name": "mastothemes",
    "url": "https://mastodon.social/tags/mastothemes",
    "history": [
      {
        "day": "1574553600",
        "uses": "0",
        "accounts": "0"
      },
      {
        "day": "1574467200",
        "uses": "0",
        "accounts": "0"
      },
      {
        "day": "1574380800",
        "uses": "0",
        "accounts": "0"
      },
      {
        "day": "1574294400",
        "uses": "0",
        "accounts": "0"
      },
      {
        "day": "1574208000",
        "uses": "0",
        "accounts": "0"
      },
      {
        "day": "1574121600",
        "uses": "0",
        "accounts": "0"
      },
      {
        "day": "1574035200",
        "uses": "0",
        "accounts": "0"
      }
    ]
  }
]
```

##### 401: 인증되지 않음 {#401-unauthorized-3}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/featured_tags_controller.rb" caption="app/controllers/api/v1/featured_tags_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/featured_tags/suggestions_controller.rb" caption="app/controllers/api/v1/featured_tags/suggestions_controller.rb" >}}
