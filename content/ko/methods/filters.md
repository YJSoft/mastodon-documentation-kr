---
title: 필터 API 메서드
description: 필터를 생성하고 관리합니다.
menu:
  docs:
    name: 필터
    parent: methods-accounts
    identifier: methods-filters
aliases: [
  "/methods/filters",
  "/api/methods/filters",
  "/methods/accounts/filters",
]
---

## 서버 측(v2) 메서드 {#v2}

마스토돈 4.0부터 필터는 여러 키워드를 포함할 수 있으며 서버 측에서 일치 여부를 확인합니다. 클라이언트는 [게시물의 `filtered` 속성]({{< relref "entities/Status#filtered" >}})에 따라 필터 동작을 적용합니다.

---

### 모든 필터 조회 {#get}

```http
GET /api/v2/filters HTTP/1.1
```

현재 사용자의 모든 필터 그룹 목록을 가져옵니다.

**반환:** 배열: [Filter]({{< relref "entities/Filter" >}})\
**OAuth:** 사용자 토큰 + `read:filters`\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

```json
[
  {
    "id": "20060",
    "title": "Remove Twitter crossposts from public timeline",
    "context": [
      "public"
    ],
    "expires_at": null,
    "filter_action": "hide",
    "keywords": [
        {
          "id": "1311",
          "keyword": "from birdsite",
          "whole_word": true
        },
        {
          "id": "1324",
          "keyword": "@twitter.com",
          "whole_word": false
        },
        {
          "id": "1325",
          "keyword": "https://t.co/",
          "whole_word": false
        }
    ],
    "statuses": []
  },
  // ...
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

### 특정 필터 조회 {#get-one}

```http
GET /api/v2/filters/:id HTTP/1.1
```

현재 사용자가 소유한 필터 그룹 하나를 가져옵니다.

**반환:** [Filter]({{< relref "entities/Filter" >}})\
**OAuth:** 사용자 토큰 + `read:filters`\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 데이터베이스의 Filter ID입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

```json
{
  "id": "20060",
  "title": "Remove Twitter crossposts from public timeline",
  "context": [
    "public"
  ],
  "expires_at": null,
  "filter_action": "hide",
  "keywords": [
    {
      "id": "1311",
      "keyword": "from birdsite",
      "whole_word": true
    },
    {
      "id": "1324",
      "keyword": "@twitter.com",
      "whole_word": false
    },
    {
      "id": "1325",
      "keyword": "https://t.co/",
      "whole_word": false
    }
  ],
  "statuses": []
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

Filter가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

### 필터 생성 {#create}

```http
POST /api/v2/filters HTTP/1.1
```

지정한 매개변수로 필터 그룹을 생성합니다.

**반환:** [Filter]({{< relref "entities/Filter" >}})\
**OAuth:** 사용자 토큰 + `write:filters`\
**버전 이력:**\
4.0.0 - 추가\
4.4.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 5) - `filter_action` 속성에 `blur` 값 추가

#### 요청 {#request-2}

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

title
: {{<required>}} 문자열. 필터 그룹 이름입니다.

context[]
: {{<required>}} 문자열 배열. 필터를 적용할 위치입니다. `home`, `notifications`, `public`, `thread`, `account` 중 하나 이상을 지정하세요.

filter_action
: 문자열. 필터가 일치하면 적용할 정책입니다. `warn`, `hide`, `blur` 중 하나를 지정하세요.

expires_in
: 정수. 지금부터 필터가 만료될 때까지의 초 단위 시간입니다. 기본값은 만료되지 않음입니다.

keywords_attributes[][keyword]
: 문자열. 새로 생성한 필터 그룹에 추가할 키워드입니다.

keywords_attributes[][whole_word]
: 불리언. 키워드에 단어 경계를 고려할지 여부입니다.

<!-- TODO: Remove when https://github.com/mastodon/mastodon/issues/21727 is fixed
keywords_attributes[][id]
: 문자열. 제공하면 404 오류가 발생합니다.

keywords_attributes[][_destroy]
: 불리언. 제공하면 키워드가 연결되지 않습니다.
-->

#### 응답 {#response-2}

##### 200: 성공 {#200-ok-2}

호출로 생성한 Filter의 예입니다.

```text
POST https://mastodon.example/api/v2/filters
?title=test
&context[]=public
&keywords_attributes[][keyword]=foo
&keywords_attributes[][whole_word]=false
&keywords_attributes[][keyword]=bar
&keywords_attributes[][whole_word]=true
```

```json
{
  "id": "25933",
  "title": "test",
  "context": [
    "public"
  ],
  "expires_at": null,
  "filter_action": "warn",
  "keywords": [
    {
      "id": "34978",
      "keyword": "foo",
      "whole_word": false
    },
    {
      "id": "34979",
      "keyword": "bar",
      "whole_word": true
    }
  ],
  "statuses": []
}
```

##### 401: 인증되지 않음 {#401-unauthorized-2}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-1}

필터 키워드 ID가 지정되었습니다.

```json
{
  "error": "Record not found"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

```json
{
  "error": "Validation failed: Title can't be blank, Context can't be blank, Context None or invalid context supplied"
}
```

---

### 필터 수정 {#update}

```http
PUT /api/v2/filters/:id HTTP/1.1
```

지정한 매개변수로 필터 그룹을 수정합니다.

**반환:** [Filter]({{< relref "entities/Filter" >}})\
**OAuth:** 사용자 토큰 + `write:filters`\
**버전 이력:**\
4.0.0 - 추가\
4.4.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 5) - `filter_action` 속성에 `blur` 값 추가

#### 요청 {#request-3}

##### 경로 매개변수 {#path-parameters-1}

:id
: {{<required>}} 문자열. 데이터베이스의 Filter ID입니다.

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-1}

title
: 문자열. 필터 그룹 이름입니다.

context[]
: 문자열 배열. 필터를 적용할 위치입니다. `home`, `notifications`, `public`, `thread`, `account` 중 하나 이상을 지정하세요.

filter_action
: 문자열. 필터가 일치하면 적용할 정책입니다. `warn`, `hide`, `blur` 중 하나를 지정하세요.

expires_in
: 정수. 지금부터 필터가 만료될 때까지의 초 단위 시간입니다.

keywords_attributes[][keyword]
: 문자열. 새로 생성한 필터 그룹에 추가할 키워드입니다.

keywords_attributes[][whole_word]
: 불리언. 키워드에 단어 경계를 고려할지 여부입니다.

keywords_attributes[][id]
: 문자열. 새 키워드를 생성하는 대신 기존 키워드를 수정하려면 해당 ID를 제공하세요.

keywords_attributes[][_destroy]
: 불리언. true이면 지정한 ID의 키워드를 제거합니다.

#### 응답 {#response-3}
##### 200: 성공 {#200-ok-3}

호출 예:

```
PUT /api/v2/filters/25933
?keywords_attributes[][id]=34978
&keywords_attributes[][_destroy]=true
&keywords_attributes[][id]=34979
&keywords_attributes[][keyword]=baz
```

키워드 34978("foo")을 제거하고 키워드 34979("bar")를 새 키워드("baz")로 바꿉니다.

```json
{
  "id": "25933",
  "title": "test",
  "context": [
    "public"
  ],
  "expires_at": null,
  "filter_action": "warn",
  "keywords": [
    {
      "id": "34979",
      "keyword": "baz",
      "whole_word": true
    }
  ],
  "statuses": []
}
```

##### 401: 인증되지 않음 {#401-unauthorized-3}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-2}

Filter가 내 소유가 아니거나 존재하지 않습니다. 또는 `keywords_attributes[][id]`를 제공했지만 이 Filter에 해당 ID의 키워드가 없습니다.

```json
{
  "error": "Record not found"
}
```

---

### 필터 삭제 {#delete}

```http
DELETE /api/v2/filters/:id HTTP/1.1
```

지정한 ID의 필터 그룹을 삭제합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:filters`\
**버전 이력:**\
4.0.0 - 추가

##### 경로 매개변수 {#path-parameters-2}

:id
: {{<required>}} 문자열. 데이터베이스의 Filter ID입니다.

##### 헤더 {#headers-4}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-4}
##### 200: 성공 {#200-ok-4}

Filter를 삭제했습니다.

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-4}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-3}

Filter가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

### 필터에 추가된 키워드 조회 {#keywords-get}

```http
GET /api/v2/filters/:filter_id/keywords HTTP/1.1
```

현재 필터 그룹에 연결된 모든 키워드를 나열합니다.

**반환:** 배열: [FilterKeyword]({{< relref "entities/FilterKeyword" >}})\
**OAuth:** 사용자 토큰 + `read:filters`\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-4}

##### 경로 매개변수 {#path-parameters-3}

:filter_id
: {{<required>}} 문자열. 데이터베이스의 Filter ID입니다.

##### 헤더 {#headers-5}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-5}
##### 200: 성공 {#200-ok-5}

```json
[
  {
    "id": "34979",
    "keyword": "baz",
    "whole_word": true
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

##### 404: 찾을 수 없음 {#404-not-found-4}

Filter가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

### 필터에 키워드 추가 {#keywords-create}

```http
POST /api/v2/filters/:filter_id/keywords HTTP/1.1
```

지정한 필터 그룹에 지정한 키워드를 추가합니다.

**반환:** [FilterKeyword]({{< relref "entities/FilterKeyword" >}})\
**OAuth:** 사용자 토큰 + `write:filters`\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-5}

##### 경로 매개변수 {#path-parameters-4}

:filter_id
: {{<required>}} 문자열. 데이터베이스의 Filter ID입니다.

##### 헤더 {#headers-6}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-2}

keyword
: {{<required>}} 문자열. 필터 그룹에 추가할 키워드입니다.

whole_word
: 불리언. 키워드에 단어 경계를 고려할지 여부입니다.

#### 응답 {#response-6}
##### 200: 성공 {#200-ok-6}

```json
{
  "id": "35583",
  "keyword": "some",
  "whole_word": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-6}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-5}

Filter가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-1}

키워드가 제공되지 않았습니다.

```json
{
  "error": "Validation failed: Keyword can't be blank"
}
```

---

### 키워드 하나 조회 {#keywords-get-one}

```http
GET /api/v2/filters/keywords/:id HTTP/1.1
```

지정한 ID의 필터 키워드 하나를 가져옵니다.

**반환:** [FilterKeyword]({{< relref "entities/FilterKeyword" >}})\
**OAuth:** 사용자 토큰 + `read:filters`\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-6}

##### 경로 매개변수 {#path-parameters-5}

:id
: {{<required>}} 문자열. 데이터베이스의 FilterKeyword ID입니다.

##### 헤더 {#headers-7}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-7}
##### 200: 성공 {#200-ok-7}

```json
{
  "id": "34979",
  "keyword": "baz",
  "whole_word": true
}
```

##### 401: 인증되지 않음 {#401-unauthorized-7}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-6}

Filter가 내 소유가 아니거나, 필터 또는 필터 키워드가 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

### 필터의 키워드 편집 {#keywords-update}

```http
PUT /api/v2/filters/keywords/:id HTTP/1.1
```

지정한 필터 키워드를 수정합니다.

**반환:** [FilterKeyword]({{< relref "entities/FilterKeyword" >}})\
**OAuth:** 사용자 토큰 + `write:filters`\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-7}

##### 경로 매개변수 {#path-parameters-6}

:id
: {{<required>}} 문자열. 데이터베이스의 FilterKeyword ID입니다.

##### 헤더 {#headers-8}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-3}

keyword
: {{<required>}} 문자열. 필터 그룹에 추가할 키워드입니다.

whole_word
: 불리언. 키워드에 단어 경계를 고려할지 여부입니다.

#### 응답 {#response-8}
##### 200: 성공 {#200-ok-8}

키워드 "some"을 "other"로 수정했습니다.

```json
{
  "id": "35583",
  "keyword": "other",
  "whole_word": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-8}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-7}

FilterKeyword가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-2}

키워드가 제공되지 않았습니다.

```json
{
  "error": "Validation failed: Keyword can't be blank"
}
```

---

### 필터에서 키워드 제거 {#keywords-delete}

```http
DELETE /api/v2/filters/keywords/:id HTTP/1.1
```

지정한 필터 키워드를 삭제합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:filters`\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-8}

##### 경로 매개변수 {#path-parameters-7}

:id
: {{<required>}} 문자열. 데이터베이스의 FilterKeyword ID입니다.

##### 헤더 {#headers-9}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-9}
##### 200: 성공 {#200-ok-9}

FilterKeyword를 삭제했습니다.

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-9}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-8}

FilterKeyword가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

### 모든 게시물 필터 조회 {#statuses-get}

```http
GET /api/v2/filters/:filter_id/statuses HTTP/1.1
```

이 필터 그룹에 속한 모든 게시물 필터 목록을 가져옵니다.

**반환:** 배열: [FilterStatus]({{< relref "entities/FilterStatus" >}})\
**OAuth:** 사용자 토큰 + `read:filters`\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-9}

##### 경로 매개변수 {#path-parameters-8}

:filter_id
: {{<required>}} 문자열. 데이터베이스의 Filter ID입니다.

##### 헤더 {#headers-10}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-10}
##### 200: 성공 {#200-ok-10}

```json
[
  {
    "id": "897",
    "status_id": "109416512469928632"
  },
  // ...
]
```

##### 401: 인증되지 않음 {#401-unauthorized-10}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-9}

Filter가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

### 필터 그룹에 게시물 추가 {#statuses-add}

```http
POST /api/v2/filters/:filter_id/statuses HTTP/1.1
```

현재 필터 그룹에 게시물 필터를 추가합니다.

**반환:** [FilterStatus]({{< relref "entities/FilterStatus" >}})\
**OAuth:** 사용자 토큰 + `write:filters`\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-10}

##### 경로 매개변수 {#path-parameters-9}

:filter_id
: {{<required>}} 문자열. 데이터베이스의 Filter ID입니다.

##### 헤더 {#headers-11}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-4}

status_id
: {{<required>}} 문자열. 필터 그룹에 추가할 게시물 ID입니다.

#### 응답 {#response-11}
##### 200: 성공 {#200-ok-11}

현재 Filter 안에 FilterStatus를 생성했습니다.

```json
{
  "id": "897",
  "status_id": "109416512469928632"
}
```

##### 401: 인증되지 않음 {#401-unauthorized-11}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-10}

Filter가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

### 게시물 필터 하나 조회 {#statuses-get-one}

```http
GET /api/v2/filters/statuses/:id HTTP/1.1
```

게시물 필터 하나를 가져옵니다.

**반환:** [FilterStatus]({{< relref "entities/FilterStatus" >}})\
**OAuth:** 사용자 토큰 + `read:filters`\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-11}

##### 경로 매개변수 {#path-parameters-10}

:id
: {{<required>}} 문자열. 데이터베이스의 FilterStatus ID입니다.

##### 헤더 {#headers-12}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-12}
##### 200: 성공 {#200-ok-12}

```json
{
  "id": "897",
  "status_id": "109416512469928632"
}
```

##### 401: 인증되지 않음 {#401-unauthorized-12}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-11}

FilterStatus가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

### 필터 그룹에서 게시물 제거 {#statuses-remove}

```http
DELETE /api/v2/filters/statuses/:id HTTP/1.1
```

현재 필터 그룹에서 게시물 필터를 제거합니다.

**반환:** [FilterStatus]({{< relref "entities/FilterStatus" >}})\
**OAuth:** 사용자 토큰 + `write:filters`\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-12}

##### 경로 매개변수 {#path-parameters-11}

:id
: {{<required>}} 문자열. 데이터베이스의 FilterStatus ID입니다.

##### 헤더 {#headers-13}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-13}
##### 200: 성공 {#200-ok-13}

FilterStatus를 삭제했습니다.

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-13}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-12}

FilterStatus가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

## 클라이언트 측(v1) 메서드 {#v1}

마스토돈 4.0 이전에는 클라이언트 측에서 필터 일치 여부를 확인했으며 필터는 필터링할 문구 하나만 포함할 수 있었습니다.

---

### 내 필터 조회 {{%deprecated%}} {#get-v1}

```http
GET /api/v1/filters HTTP/1.1
```

**반환:** 목록: [V1::Filter]({{< relref "entities/V1_Filter" >}})\
**OAuth:** 사용자 토큰 + `read:filters`\
**버전 이력:**\
2.4.3 - 추가\
4.0.0 - 사용 중단 예정. 호환성을 위해 각 V1::Filter가 하나의 FilterKeyword를 나타내는 V1::Filter 목록을 반환하도록 변경(`keyword`를 `phrase` 속성에 표시)

#### 요청 {#request-13}
##### 헤더 {#headers-14}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-14}
##### 200: 성공 {#200-ok-14}

서로 다른 적용 위치에 있는 여러 필터의 발췌입니다.

```json
[
  {
    "id": "6191",
    "phrase": ":eurovision2019:",
    "context": [
      "home"
    ],
    "whole_word": true,
    "expires_at": "2019-05-21T13:47:31.333Z",
    "irreversible": false
  },
  // ...
  {
    "id": "5580",
    "phrase": "@twitter.com",
    "context": [
      "home",
      "notifications",
      "public",
      "thread"
    ],
    "whole_word": false,
    "expires_at": null,
    "irreversible": true
  },
  // ...
]
```

##### 401: 인증되지 않음 {#401-unauthorized-14}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

### 필터 하나 조회 {{%deprecated%}} {#get-one-v1}

```http
GET /api/v1/filters/:id HTTP/1.1
```

**반환:** [V1::Filter]({{< relref "entities/V1_Filter" >}})\
**OAuth:** 사용자 토큰 + `read:filters`\
**버전 이력:**\
2.4.3 - 추가\
4.0.0 - 사용 중단 예정. 호환성을 위해 하나의 FilterKeyword를 나타내는 V1::Filter를 반환하도록 변경(`keyword`를 `phrase` 속성에 표시)

#### 요청 {#request-14}

##### 경로 매개변수 {#path-parameters-12}

:id
: {{<required>}} 문자열. 데이터베이스의 FilterKeyword ID입니다.

##### 헤더 {#headers-15}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-15}
##### 200: 성공 {#200-ok-15}

```json
{
  "id": "8449",
  "phrase": "test",
  "context": [
    "home",
    "notifications",
    "public",
    "thread"
  ],
  "whole_word": false,
  "expires_at": "2019-11-26T09:08:06.254Z",
  "irreversible": true
}
```

##### 401: 인증되지 않음 {#401-unauthorized-15}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-13}

Filter ID가 존재하지 않거나 내 소유가 아닙니다.

```json
{
  "error": "Record not found"
}
```

---

### 필터 생성 {{%deprecated%}} {#create-v1}

```http
POST /api/v1/filters HTTP/1.1
```

**반환:** [V1::Filter]({{< relref "entities/V1_Filter" >}})\
**OAuth:** 사용자 토큰 + `write:filters`\
**버전 이력:**\
2.4.3 - 추가\
3.1.0 - 프로필 보기를 필터링할 `account` 적용 위치 추가\
4.0.0 - 사용 중단 예정. 호환성을 위해 하나의 FilterKeyword를 나타내는 V1::Filter를 반환하도록 변경(`keyword`를 `phrase` 속성에 표시). 이 메서드는 FilterKeyword 하나만 포함하는 Filter를 생성합니다. Filter의 `title`과 FilterKeyword의 `keyword`는 제공한 `phrase`와 같은 값으로 설정됩니다.

#### 요청 {#request-15}
##### 헤더 {#headers-16}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-5}

phrase
: {{<required>}} 문자열. 필터링할 텍스트입니다.

context[]
: {{<required>}} 문자열 배열. 필터를 적용할 위치입니다. `home`, `notifications`, `public`, `thread`, `account` 중 하나 이상을 지정하세요.

irreversible
: 불리언. 서버가 일치하는 엔터티를 홈과 알림에서 되돌릴 수 없게 제거할지 여부입니다. 기본값은 false입니다.

whole_word
: 불리언. 이 키워드를 필터링할 때 단어 경계를 고려할지 여부입니다. 기본값은 false입니다.

expires_in
: 정수. 지금부터 필터가 만료될 때까지의 초 단위 시간입니다. 만료되지 않는 필터는 `null`입니다.

#### 응답 {#response-16}
##### 200: 성공 {#200-ok-16}

새로 생성한 필터를 반환합니다.

```json
{
  "id": "8449",
  "phrase": "test",
  "context": [
    "home",
    "notifications",
    "public",
    "thread"
  ],
  "whole_word": false,
  "expires_at": "2019-11-26T09:08:06.254Z",
  "irreversible": true
}
```

##### 401: 인증되지 않음 {#401-unauthorized-16}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-3}

phrase가 올바르게 제공되지 않은 경우:

```json
{
  "error": "Validation failed: Phrase can't be blank"
}
```

context가 올바르게 제공되지 않은 경우:

```json
{
  "error": "Validation failed: Context can't be blank, Context None or invalid context supplied"
}
```

---

### 필터 수정 {{%deprecated%}} {#update-v1}

```http
PUT /api/v1/filters/:id HTTP/1.1
```

필터의 매개변수를 제자리에서 교체합니다.

**반환:** [V1::Filter]({{< relref "entities/V1_Filter" >}})\
**OAuth:** 사용자 토큰 + `write:filters`\
**버전 이력:**\
2.4.3 - 추가\
3.1.0 - 프로필 보기를 필터링할 `account` 적용 위치 추가\
4.0.0 - 사용 중단 예정. 호환성을 위해 하나의 FilterKeyword를 나타내는 V1::Filter를 반환하도록 변경(`keyword`를 `phrase` 속성에 표시). 여러 키워드가 있는 필터의 `expires_in`, `irreversible`, `context`를 변경하려고 하면 오류를 반환합니다. `phrase`와 `whole_word`는 언제든 안전하게 변경할 수 있습니다.

#### 요청 {#request-16}

##### 경로 매개변수 {#path-parameters-13}

:id
: {{<required>}} 문자열. 데이터베이스의 FilterKeyword ID입니다.

##### 헤더 {#headers-17}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-6}

phrase
: {{<required>}} 문자열. 필터링할 텍스트입니다.

context[]
: {{<required>}} 문자열 배열. `home`, `notifications`, `public`, `thread`, `account` 중 하나 이상을 지정하세요.

irreversible
: 불리언. 서버가 일치하는 엔터티를 홈과 알림에서 되돌릴 수 없게 제거할지 여부입니다. 기본값은 false입니다.

whole_word
: 불리언. 필터가 단어 경계를 고려할지 여부입니다. 기본값은 false입니다.

expires_in
: 정수. 지금부터 필터가 만료될 때까지의 초 단위 시간입니다. 만료되지 않는 필터는 `null`입니다.

#### 응답 {#response-17}
##### 200: 성공 {#200-ok-17}

필터를 수정했습니다.

```json
{
  "id": "8449",
  "phrase": "test",
  "context": [
    "home",
    "notifications",
    "public",
    "thread"
  ],
  "whole_word": false,
  "expires_at": null,
  "irreversible": true
}
```

##### 401: 인증되지 않음 {#401-unauthorized-17}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-14}

Filter가 존재하지 않거나 내 소유가 아닙니다.

```json
{
  "error": "Record not found"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-4}

phrase가 올바르게 제공되지 않은 경우:

```json
{
  "error": "Validation failed: Phrase can't be blank"
}
```

context가 올바르게 제공되지 않은 경우:

```json
{
  "error": "Validation failed: Context can't be blank, Context None or invalid context supplied"
}
```

---

### 필터 제거 {{%deprecated%}} {#delete-v1}

```http
DELETE /api/v1/filters/:id HTTP/1.1
```

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:filters`\
**버전 이력:**\
2.4.3 - 추가\
4.0.0 - 사용 중단 예정. 이 메서드는 상위 Filter에서 FilterKeyword만 삭제합니다. 상위 Filter를 삭제하려면 v2 필터 API를 사용해야 합니다.

#### 요청 {#request-17}

##### 경로 매개변수 {#path-parameters-14}

:id
: {{<required>}} 문자열. 데이터베이스의 Filter ID입니다.

##### 헤더 {#headers-18}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-18}
##### 200: 성공 {#200-ok-18}

필터를 삭제했으므로 빈 객체를 반환합니다.

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-18}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-15}

Filter가 존재하지 않거나 내 소유가 아닙니다.

```json
{
  "error": "Record not found"
}
```

---

## 함께 보기 {#see-also}

{{< page-relref ref="api/guidelines#filters" caption="필터 구현 지침" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v2/filters_controller.rb" caption="app/controllers/api/v2/filters_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/filters/keywords_controller.rb" caption="app/controllers/api/v1/filters/keywords_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/filters/statuses_controller.rb" caption="app/controllers/api/v1/filters/statuses_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/filters_controller.rb" caption="app/controllers/api/v1/filters_controller.rb" >}}
