---
title: 도메인 차단 API 메서드
description: 사용자가 차단한 도메인을 관리합니다.
menu:
  docs:
    name: 도메인 차단
    parent: methods-accounts
    identifier: methods-domain_blocks
aliases: [
  "/methods/domain_blocks",
  "/api/methods/domain_blocks",
  "/methods/accounts/domain_blocks"]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 도메인 차단 가져오기 {#get}

```http
GET /api/v1/domain_blocks HTTP/1.1
```

사용자가 차단한 도메인을 조회합니다.

**반환:** 문자열 배열\
**OAuth:** 사용자 토큰 + `read:blocks` 또는 `follow`\
**버전:**\
1.4.0 - 추가\
3.3.0 - 이제 `min_id`와 `max_id` 동시 사용 가능

#### 요청 {#request}
##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters}

max_id 
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

since_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

min_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 도메인 차단 100개이며 최대 200개입니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

limit=2인 호출 예입니다.

```json
["nsfw.social","artalley.social"]
```

AccountDomainBlock ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <https://mastodon.example/api/v1/domain_blocks?limit=2&max_id=16194>; rel="next", <https://mastodon.example/api/v1/domain_blocks?limit=2&since_id=16337>; rel="prev"
```

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 도메인 차단 {#block}

```http
POST /api/v1/domain_blocks HTTP/1.1
```

도메인을 차단하여 해당 도메인의 서버와의 상호작용을 변경합니다.

- 모든 공개 게시물 숨기기
- 모든 알림 숨기기
- 모든 팔로워 제거
- 새 사용자 팔로우 방지(기존 팔로우는 제거하지 않음)
- 공개 게시물을 가져오지 못하게 하기(`AUTHORIZED_FETCH`가 활성화된 경우)

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:blocks` 또는 `follow`\
**버전:**\
1.4.0 - 추가

#### 요청 {#request-1}

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

domain
: {{<required>}} 문자열. 차단할 도메인입니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

호출이 성공하면 빈 객체를 반환합니다. 도메인이 이미 차단되었거나, 존재하지 않거나, 도메인이 아닌 경우에도 호출이 성공합니다.

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-1}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

`domain`을 제공하지 않으면 요청이 실패합니다.

```json
{
  "error": "Validation failed: Domain can't be blank"
}
```

`domain`에 공백이 포함되면 요청이 실패합니다.

```json
{
  "error": "Validation failed: Domain is not a valid domain name"
}
```

---

## 도메인 차단 해제 {#unblock}

```http
DELETE /api/v1/domain_blocks HTTP/1.1
```

사용자의 차단 도메인 배열에 해당 도메인 차단이 있으면 제거합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:blocks` 또는 `follow`\
**버전 이력:**\
1.4.0 - 추가

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-1}

domain
: {{<required>}} 문자열. 차단을 해제할 도메인입니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

호출이 성공하면 빈 객체를 반환합니다. 도메인이 이전에 차단되지 않았더라도 호출이 성공합니다.

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

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-1}

`domain`을 제공하지 않으면 요청이 실패합니다.

```json
{
  "error": "Validation failed: Domain can't be blank"
}
```

`domain`에 공백이 포함되면 요청이 실패합니다.

```json
{
  "error": "Validation failed: Domain is not a valid domain name"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/domain_blocks_controller.rb" caption="app/controllers/api/v1/domain_blocks_controller.rb" >}}
