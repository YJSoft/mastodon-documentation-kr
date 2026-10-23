---
title: 컬렉션 API 메서드
description: 다른 사람에게 추천할 계정 컬렉션을 관리합니다.
menu:
  docs:
    name: 컬렉션
    parent: methods
    identifier: methods-collections
aliases: ["/methods/collections", "/api/methods/collections"]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 컬렉션 생성 {#create}

```http
POST /api/v1/collections HTTP/1.1
```

새 컬렉션을 생성합니다.

**반환:** [WrappedCollection]({{< relref "entities/Collection#WrappedCollection" >}})\
**OAuth:** 사용자 토큰 + `write:collections`\
**버전 이력:**\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - 추가

#### 요청 {#create-request-example}

요청 예:

```http
POST /api/v1/collections HTTP/1.1
Content-Type: application/json

{
  "name": "Nice accounts",
  "description": "These accounts are very nice",
  "language": "en",
  "tag_name": "#accounts",
  "sensitive": false,
  "discoverable": true,
  "account_ids": ["112658193342215767", "117628196343117789"]
}
```

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

name
: {{<required>}} 문자열. 컬렉션 이름이며 최대 40자입니다. 문자열을 "있는 그대로" 사용하므로 현재 URL과 해시태그를 특별하게 처리하지 않으며 사용자 지정 이모지도 지원하지 않습니다.

description
: 문자열. 컬렉션의 상세 설명이며 최대 100자입니다. 문자열을 "있는 그대로" 사용하므로 현재 URL과
해시태그를 특별하게 처리하지 않으며 사용자 지정 이모지도 지원하지 않습니다.

language
: 문자열. 마스토돈이 지원하는 언어 코드 중 하나입니다(두 글자 ISO 639-1 코드 및 예외).

tag_name
: 문자열. 컬렉션을 설명하는 해시태그 하나입니다.

sensitive
: 불리언. 이 컬렉션을 민감한 콘텐츠로 표시할지 여부입니다.

discoverable
: 불리언. 이 컬렉션을 사용자 프로필, 검색 결과, 기타 탐색 수단에 표시할지 여부입니다.

account_ids[]
: 문자열 배열. 이 컬렉션에서 추천할 계정의 ID입니다.

#### 응답 {#response}

##### 200: 성공 {#200-ok}

```json
{
  "collection": {
    "id": "116131056935959117",
    "account_id": "113668893442515793",
    "uri": "https://example.com/ap/113668893442515793/collections/116131056935959117",
    "url": "https://example.com/collections/116131056935959117",
    "name": "Nice accounts",
    "description": "These accounts are very nice",
    "language": "en",
    "local": true,
    "sensitive": false,
    "discoverable": true,
    "tag": {
      "name": "accounts",
      "url": "https://example.com/tags/accounts"
    },
    "item_count": 2,
    "items": [
      // ...
    ],
    "created_at": "2026-02-25T11:35:01.394Z",
    "updated_at": "2026-02-25T11:35:01.394Z"
  }
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

유효성 검사 오류가 있으면 HTTP 상태 `422`를 반환합니다. 응답에는 일반 오류 메시지와 속성별 세부 정보를 담은 JSON 객체가 포함됩니다.

Example:

```json
{
  "error": {
    "error": "Validation failed: Name is too long (maximum is 40 characters)",
    "details": {
      "name": [
        {
          "error": "ERR_TOO_LONG",
          "description": "is too long (maximum is 40 characters)"
        }
      ]
    }
  }
}
```

오류 코드 목록은 [계정 등록]({{< relref "methods/accounts#create" >}})을 참고하세요.

---

## 컬렉션 하나 가져오기 {#get_collection}

```http
GET /api/v1/collections/:id HTTP/1.1
```

**반환:** [CollectionWithAccounts]({{< relref "entities/CollectionWithAccounts" >}})\
**OAuth:** 공개 또는 인증된 접근을 위한 사용자 토큰 + `read:collections`\
**버전 이력:**\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - 추가

#### 요청 {#request}

##### 헤더 {#headers-1}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}

##### 200: 성공 {#200-ok-1}

실제 컬렉션과 컬렉션의 모든 계정 및 소유자를 포함하는 Account 객체 목록이 담긴 객체를 반환합니다.

인증된 요청에서는 요청 사용자를 기준으로 컬렉션 항목을 조정합니다. 즉 사용자가 차단한 항목은 포함하지 않으며, 사용자가 소유한 컬렉션을 요청하면 `pending` 상태의 항목도 포함합니다.

다른 사용자의 컬렉션을 요청하거나 익명으로 요청하면 `accepted` 상태의 항목만 반환합니다.

```json
{
  "accounts": [
    // ...
  ],
  "collection": {
    "id": "116131056935959117",
    "account_id": "113668893442515793",
    "uri": "https://example.com/ap/113668893442515793/collections/116131056935959117",
    "url": "https://example.com/collections/116131056935959117",
    "name": "Nice accounts",
    "description": "These accounts are very nice",
    "language": "en",
    "local": true,
    "sensitive": false,
    "discoverable": true,
    "tag": {
      "name": "accounts",
      "url": "https://example.com/tags/accounts"
    },
    "item_count": 2,
    "items": [
      // ...
    ],
    "created_at": "2026-02-25T11:35:01.394Z",
    "updated_at": "2026-02-25T11:35:01.394Z"
  }
}
```

## 지정한 계정의 모든 컬렉션 가져오기 {#get_collections}

```http
GET /api/v1/accounts/:account_id/collections HTTP/1.1
```

**반환:** [Collections]({{< relref "entities/Collection#Collections" >}})\
**OAuth:** 공개 또는 인증된 접근을 위한 사용자 토큰 + `read:collections`\
**버전 이력:**\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - 추가

#### 요청 {#request-1}

##### 헤더 {#headers-2}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters}

limit
: 정수. 최대 결과 수입니다. 기본값은 컬렉션 40개이며 최대 80개입니다.

offset
: 정수. 처음 n개 결과를 건너뜁니다. 기본값은 0입니다.

#### 응답 {#response-2}

##### 200: 성공 {#200-ok-2}

컬렉션 목록이 담긴 객체를 반환합니다. `:account_id`가 요청한 계정의 ID인 경우를 제외하면 [`discoverable`]({{< relref "entities/Collection#discoverable" >}})이 `true`인 컬렉션만 포함합니다.

인증된 요청에서는 요청 사용자를 기준으로 컬렉션 항목을 조정합니다. 자세한 내용은 위의 ["컬렉션 하나 가져오기"](#get_collection)를 참고하세요.

결과가 여러 페이지이면 다음 또는 이전 결과 페이지를 참조하는 `Link` 헤더가 포함됩니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```json
{
  "collections:": [
    {
      "id": "116131056935959117",
      "account_id": "113668893442515793",
      "uri": "https://example.com/ap/113668893442515793/collections/116131056935959117",
      "url": "https://example.com/collections/116131056935959117",
      "name": "Nice accounts",
      "description": "These accounts are very nice",
      "language": "en",
      "local": true,
      "sensitive": false,
      "discoverable": true,
      "tag": {
        "name": "accounts",
        "url": "https://example.com/tags/accounts"
      },
      "item_count": 2,
      "items": [
        // ...
      ],
      "created_at": "2026-02-25T11:35:01.394Z",
      "updated_at": "2026-02-25T11:35:01.394Z"
    },
    // ...
  ]
}
```

---

## 현재 계정이 추천된 모든 컬렉션 가져오기 {#in_collections}

```http
GET /api/v1/accounts/:account_id/in_collections HTTP/1.1
```

**반환:** [Collections]({{< relref "entities/Collection#Collections" >}})\
**OAuth:** 사용자 토큰 + `read:collections`\
**버전 이력:**\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - 추가

#### 요청 {#request-2}

##### 헤더 {#headers-3}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-1}

limit
: 정수. 최대 결과 수입니다. 기본값은 컬렉션 40개이며 최대 80개입니다.

offset
: 정수. 처음 n개 결과를 건너뜁니다. 기본값은 0입니다.

#### 응답 {#response-3}

##### 200: 성공 {#200-ok-3}

컬렉션 목록이 담긴 객체를 반환합니다.

요청 사용자를 기준으로 컬렉션 항목을 조정합니다. 자세한 내용은 위의 ["컬렉션 하나 가져오기"](#get_collection)를 참고하세요.

결과가 여러 페이지이면 다음 또는 이전 결과 페이지를 참조하는 `Link` 헤더가 포함됩니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```json
{
  "collections:": [
    {
      "id": "116131056935959117",
      "account_id": "113668893442515793",
      "uri": "https://example.com/ap/113668893442515793/collections/116131056935959117",
      "url": "https://example.com/collections/116131056935959117",
      "name": "Nice accounts",
      "description": "These accounts are very nice",
      "language": "en",
      "local": true,
      "sensitive": false,
      "discoverable": true,
      "tag": {
        "name": "accounts",
        "url": "https://example.com/tags/accounts"
      },
      "item_count": 2,
      "items": [
        // ...
      ],
      "created_at": "2026-02-25T11:35:01.394Z",
      "updated_at": "2026-02-25T11:35:01.394Z"
    },
    // ...
  ]
}
```

---

## 컬렉션 수정 {#update_collection}

```http
PATCH /api/v1/collections/:id HTTP/1.1
```

기존 컬렉션을 수정합니다.

**반환:** [WrappedCollection]({{< relref "entities/Collection#WrappedCollection" >}})\
**OAuth:** 사용자 토큰 + `write:collections`\
**버전 이력:**\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - 추가

#### 요청 {#request-3}

요청 예:

```http
PATCH /api/v1/collections/116131056935959117 HTTP/1.1
Content-Type: application/json

{
  "name": "Nice accounts",
  "description": "These accounts are very nice",
  "language": "en",
  "tag_name": "#accounts",
  "sensitive": false,
  "discoverable": true
}
```

##### 헤더 {#headers-4}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-1}

name
: 문자열. 컬렉션 이름이며 최대 40자입니다.

description
: 문자열. 컬렉션의 상세 설명이며 최대 100자입니다.

language
: 문자열. 마스토돈이 지원하는 언어 코드 중 하나입니다(두 글자 ISO 639-1 코드 및 예외).

tag_name
: 문자열. 컬렉션을 설명하는 해시태그 하나입니다.

sensitive
: 불리언. 이 컬렉션을 민감한 콘텐츠로 표시할지 여부입니다.

discoverable
: 불리언. 이 컬렉션을 검색 결과와 기타 탐색 수단에 표시할지 여부입니다.

#### 응답 {#response-4}

##### 200: 성공 {#200-ok-4}

```json
{
  "collection": {
    "id": "116131056935959117",
    "account_id": "113668893442515793",
    "uri": "https://example.com/ap/113668893442515793/collections/116131056935959117",
    "url": "https://example.com/collections/116131056935959117",
    "name": "Nice accounts",
    "description": "These accounts are very nice",
    "language": "en",
    "local": true,
    "sensitive": false,
    "discoverable": true,
    "tag": {
      "name": "accounts",
      "url": "https://example.com/tags/accounts"
    },
    "item_count": 2,
    "items": [
      // ...
    ],
    "created_at": "2026-02-25T11:35:01.394Z",
    "updated_at": "2026-02-25T11:35:01.394Z"
  }
}
```

##### 401: 인증되지 않음 {#401-unauthorized-1}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 403: 금지됨 {#403-forbidden}

다른 사용자 소유의 컬렉션을 수정하려는 경우입니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-1}

유효성 검사 오류가 있으면 HTTP 상태 `422`를 반환합니다. 응답에는 일반 오류 메시지와 속성별 세부 정보를 담은 JSON 객체가 포함됩니다.

Example:

```json
{
  "error": {
    "error": "Validation failed: Name is too long (maximum is 40 characters)",
    "details": {
      "name": [
        {
          "error": "ERR_TOO_LONG",
          "description": "is too long (maximum is 40 characters)"
        }
      ]
    }
  }
}
```

오류 코드 목록은 [계정 등록]({{< relref "methods/accounts#create" >}})을 참고하세요.


---

## 컬렉션 삭제 {#delete_collection}

```http
DELETE /api/v1/collections/:id HTTP/1.1
```

컬렉션을 삭제합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:collections`\
**버전 이력:**\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - 추가

#### 요청 {#request-4}

요청 예:

```http
DELETE /api/v1/collections/116131056935959117 HTTP/1.1
```

##### 헤더 {#headers-5}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-5}

##### 200: 성공 {#200-ok-5}

컬렉션을 삭제했습니다.

##### 401: 인증되지 않음 {#401-unauthorized-2}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 403: 금지됨 {#403-forbidden-1}

다른 사용자 소유의 컬렉션을 삭제하려는 경우입니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 컬렉션에 계정 추가 {#add_account}

```http
POST /api/v1/collections/:collection_id/items HTTP/1.1
```

컬렉션에 계정을 추가합니다.

**반환:** [WrappedCollectionItem]({{< relref "entities/CollectionItem#WrappedCollectionItem" >}})\
**OAuth:** 사용자 토큰 + `write:collections`\
**버전 이력:**\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - 추가

#### 요청 {#request-5}

요청 예:

```http
POST /api/v1/collections/116131056935959117/items HTTP/1.1
Content-Type: application/json

{
  "account_id": "112658193342215767"
}
```

##### 헤더 {#headers-6}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-2}

account_id
: 문자열. 이 컬렉션에 추가할 계정의 ID입니다.

#### 응답 {#response-6}

##### 200: 성공 {#200-ok-6}

```json
{
  "collection_item": {
    "id": "116151066915353115",
    "account_id": "112658193342215767",
    "state": "accepted",
    "created_at": "2026-02-25T11:35:01.394Z",
  }
}
```

##### 401: 인증되지 않음 {#401-unauthorized-3}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 403: 금지됨 {#403-forbidden-2}

다른 사용자 소유의 컬렉션에 추가하려는 경우입니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-2}

유효성 검사 오류, 즉 지정한 계정을 추가할 수 없거나 지정한 ID를 알 수 없는 경우 HTTP 상태 `422`를 반환합니다. 응답에는 일반 오류 메시지가 담긴 JSON 객체가 포함됩니다.

Example:

```json
{
  "error": "`account_id` parameter is missing"
}
```

---

## 컬렉션에서 계정 제거 {#remove_account}

```http
DELETE /api/v1/collections/:collection_id/items/:id HTTP/1.1
```

컬렉션에서 계정을 제거합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:collections`\
**버전 이력:**\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - 추가

#### 요청 {#request-6}

요청 예:

```http
DELETE /api/v1/collections/116131056935959117/items/116151066915353115 HTTP/1.1
```

##### 헤더 {#headers-7}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-7}

##### 200: 성공 {#200-ok-7}

계정을 제거했습니다.

##### 401: 인증되지 않음 {#401-unauthorized-4}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 403: 금지됨 {#403-forbidden-3}

다른 사용자 소유의 컬렉션에서 항목을 제거하려는 경우입니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 컬렉션 포함 철회 {#revoke_item}

```http
POST /api/v1/collections/:collection_id/items/:id/revoke HTTP/1.1
```

다른 사용자가 생성한 컬렉션에서 현재 사용자를 제거합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:collections`\
**버전 이력:**\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - 추가

#### 요청 {#request-7}

요청 예:

```http
POST /api/v1/collections/116131056935959117/items/116151066915353115/revoke HTTP/1.1
```

##### 헤더 {#headers-8}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-8}

##### 200: 성공 {#200-ok-8}

계정을 제거했습니다.

##### 401: 인증되지 않음 {#401-unauthorized-5}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 403: 금지됨 {#403-forbidden-4}

현재 사용자를 포함하지 않는 컬렉션에서 항목을 제거하려는 경우입니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/collections_controller.rb" caption="app/controllers/api/v1/collections_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/collection_items_controller.rb" caption="app/controllers/api/v1/collection_items_controller.rb" >}}

