---
title: 태그 API 메서드
description: 해시태그 정보를 조회하거나 팔로우 및 팔로우 해제합니다.
menu:
  docs:
    name: 태그
    parent: methods-accounts
    identifier: methods-tags
aliases: [
  "/methods/tags",
  "/api/methods/tags",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 태그 하나의 정보 조회 {#get}

```http
GET /api/v1/tags/:name HTTP/1.1
```

해시태그와 관련 정보를 표시합니다.

**반환:** [Tag]({{< relref "entities/Tag" >}})\
**OAuth:** 공개, 또는 사용자 토큰\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request}

##### 경로 매개변수 {#path-parameters}

:name
: {{<required>}} 문자열. 해시태그 이름이며 대소문자를 구분하지 않습니다.

##### 헤더 {#headers}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

```json
{
  "id": "802",
  "name": "Caturday",
  "url": "http://mastodon.example/tags/caturday",
  "history": [
    {
      "day": "1668556800",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668470400",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668384000",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668297600",
      "accounts": "1",
      "uses": "1"
    },
    {
      "day": "1668211200",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668124800",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668038400",
      "accounts": "0",
      "uses": "0"
    }
  ],
  "following": false,
  "featured": false
}
```

---

## 해시태그 팔로우 {#follow}

```http
POST /api/v1/tags/:name/follow HTTP/1.1
```

해시태그를 팔로우합니다. 팔로우한 해시태그를 포함하는 게시물이 홈 타임라인에 추가됩니다.

**반환:** [Tag]({{< relref "entities/Tag" >}})\
**OAuth:** 사용자 토큰 + `write:follows`\
**버전 이력:**\
4.0.0 - 추가\
4.1.0 - 이제 이 작업은 멱등적임

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters-1}

:name
: {{<required>}} 문자열. 해시태그 이름이며 대소문자를 구분하지 않습니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

태그를 팔로우했습니다.

```json
{
  "id": "802",
  "name": "Caturday",
  "url": "http://mastodon.example/tags/caturday",
  "history": [
    {
      "day": "1668556800",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668470400",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668384000",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668297600",
      "accounts": "1",
      "uses": "1"
    },
    {
      "day": "1668211200",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668124800",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668038400",
      "accounts": "0",
      "uses": "0"
    }
  ],
  "following": true,
  "featured": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

4.1.0 이전: 태그를 이미 팔로우하고 있습니다.

```json
{
  "error": "Duplicate record"
}
```

---

## 해시태그 팔로우 해제 {#unfollow}

```http
POST /api/v1/tags/:name/unfollow HTTP/1.1
```

해시태그의 팔로우를 해제합니다. 이 해시태그를 포함하는 게시물이 더 이상 홈 타임라인에 추가되지 않습니다.

**반환:** [Tag]({{< relref "entities/Tag" >}})\
**OAuth:** 사용자 토큰 + `write:follows`\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-2}

##### 경로 매개변수 {#path-parameters-2}

:name
: {{<required>}} 문자열. 해시태그 이름이며 대소문자를 구분하지 않습니다.

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

태그의 팔로우를 해제했거나 이미 팔로우하지 않은 상태입니다.

```json
{
  "id": "802",
  "name": "Caturday",
  "url": "http://mastodon.example/tags/caturday",
  "history": [
    {
      "day": "1668556800",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668470400",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668384000",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668297600",
      "accounts": "1",
      "uses": "1"
    },
    {
      "day": "1668211200",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668124800",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668038400",
      "accounts": "0",
      "uses": "0"
    }
  ],
  "following": false,
  "featured": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-1}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 해시태그 추천 {#feature}

```http
POST /api/v1/tags/:id/feature HTTP/1.1
```

프로필에서 해시태그를 추천합니다.

**반환:** [Tag]({{< relref "entities/Tag" >}})\
**OAuth:** 사용자 토큰 + `write:accounts`\
**버전 이력:**\
4.4.0 - 추가

#### 요청 {#request-3}

##### 경로 매개변수 {#path-parameters-3}

:id
: {{<required>}} 문자열. 해시태그 이름입니다.

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-3}
##### 200: 성공 {#200-ok-3}

태그를 추천했거나 이미 추천한 상태입니다.

```json
{
  "name": "Test",
  "url": "http://mastodon.example/tags/test",
  "history": [
    {
      "day": "1668556800",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668470400",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668384000",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668297600",
      "accounts": "1",
      "uses": "1"
    },
    {
      "day": "1668211200",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668124800",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668038400",
      "accounts": "0",
      "uses": "0"
    }
  ],
  "following": false,
  "featured": true
}
```

##### 401: 인증되지 않음 {#401-unauthorized-2}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 해시태그 추천 해제 {#unfeature}

```http
POST /api/v1/tags/:id/unfeature HTTP/1.1
```

프로필에서 해시태그 추천을 중단합니다.

**반환:** [Tag]({{< relref "entities/Tag" >}})\
**OAuth:** 사용자 토큰 + `write:accounts`\
**버전 이력:**\
4.4.0 - 추가

#### 요청 {#request-4}

##### 경로 매개변수 {#path-parameters-4}

:id
: {{<required>}} 문자열. 해시태그 이름입니다.

##### 헤더 {#headers-4}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-4}
##### 200: 성공 {#200-ok-4}

태그 추천을 해제했습니다.

```json
{
  "name": "Test",
  "url": "http://mastodon.example/tags/test",
  "history": [
    {
      "day": "1668556800",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668470400",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668384000",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668297600",
      "accounts": "1",
      "uses": "1"
    },
    {
      "day": "1668211200",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668124800",
      "accounts": "0",
      "uses": "0"
    },
    {
      "day": "1668038400",
      "accounts": "0",
      "uses": "0"
    }
  ],
  "following": false,
  "featured": false
}
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

{{< page-relref ref="methods/followed_tags#get" caption="GET /api/v1/followed_tags" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/tags_controller.rb" caption="app/controllers/api/v1/tags_controller.rb" >}}

