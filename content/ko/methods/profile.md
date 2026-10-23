---
title: 프로필 API 메서드
description: 프로필에 관한 메서드입니다.
menu:
  docs:
    name: 프로필
    parent: methods
    identifier: methods-profile
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 현재 사용자 프로필 가져오기 {#get-current-user-profile}

```http
GET /api/v1/profile HTTP/1.1
```

**반환:** [Profile]({{< relref "entities/Profile">}})\
**OAuth:** 사용자 토큰 + `profile` 또는 `read:accounts`\
**버전 이력:**
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 8) - 추가\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 9) - `avatar_description` 및 `header_description` 추가

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response}

##### 200: 성공 {#200-ok}

현재 사용자 프로필을 반환합니다.

```json
{
  "id": "116222600881276277",
  "display_name": "Documentation user",
  "note": "I'm only here as an example for documentation",
  "fields": [
    {
      "name": "pronouns",
      "value": "it/its",
      "verified_at": null
    }
  ],
  "avatar": null,
  "avatar_static": null,
  "avatar_description": "",
  "header": null,
  "header_static": null,
  "header_description": "",
  "locked": false,
  "bot": false,
  "hide_collections": null,
  "discoverable": true,
  "indexable": true,
  "show_media": true,
  "show_media_replies": true,
  "show_featured": true,
  "attribution_domains": [
    "articles.example.com"
  ],
  "featured_tags": [
    {
      "id": "1",
      "name": "foo",
      "url": "https://example.com/@darrel_metz0/tagged/foo",
      "statuses_count": "0",
      "last_status_at": null
    }
  ]
}
```

### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
	"error": "The access token is invalid"
}
```

---

## 현재 사용자 프로필 수정 {#update-current-user-profile}

```http
PATCH /api/v1/profile
```

현재 사용자 프로필을 수정합니다.

**반환:** [Profile]({{< relref "entities/Profile">}})\
**OAuth:** 사용자 토큰 + `write:accounts`\
**버전 이력:**
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 8) - 추가

#### 요청 {#request-1}

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

display_name
: 문자열. 프로필에 사용할 표시 이름입니다.

note
: 문자열. 계정 소개입니다.

avatar
: `multipart/form-data`로 인코딩한 아바타 이미지입니다.

avatar_description
: 문자열. 접근성을 위한 아바타의 일반 텍스트 설명입니다.

header
: `multipart/form-data`로 인코딩한 헤더 이미지입니다.

header_description
: 문자열. 접근성을 위한 헤더의 일반 텍스트 설명입니다.

locked
: 불리언. 팔로우 요청에 수동 승인이 필요한지 여부입니다.

bot
: 불리언. 계정에 봇 표시가 있는지 여부입니다.

discoverable
: 불리언. 프로필 디렉터리에 계정을 표시하고 컬렉션에 포함되는 등 다른 탐색 기능에서도 검색 가능하게 할지 여부입니다.

hide_collections
: 불리언. 팔로워와 팔로잉 계정을 숨길지 여부입니다. 이 필드는 컬렉션 기능보다 먼저 도입되었으며 이름과 달리 컬렉션과 관련이 없습니다.

indexable
: 불리언. 누구나 공개 게시물을 검색할 수 있게 할지 여부입니다.

show_media
: 불리언. 이 프로필에 미디어 첨부 파일을 포함하는 “미디어” 탭을 표시할지 여부입니다.

show_media_replies
: 불리언. 답글의 미디어 첨부 파일을 이 프로필의 “미디어” 탭에 표시할지 여부입니다.

show_featured
: 불리언. 이 프로필에 “추천” 탭을 표시할지 여부입니다.

attribution_domains[]
: 문자열 배열. 이 계정을 작성자로 표시하도록 허용할 웹사이트 도메인입니다. 최대 10개입니다.

fields_attributes
: 해시 배열. 설정할 프로필 필드입니다. 각 해시는 `name`과 `value`를 포함합니다. 기본적으로 최대 4개 필드입니다([Instance#max_profile_fields]({{< relref "entities/Instance#max_profile_fields" >}})에 명시).

fields_attributes[:index][name]
: 문자열. 프로필 필드 이름입니다. 기본적으로 최대 255자입니다([Instance#profile_field_name_limit]({{< relref "entities/Instance#profile_field_name_limit" >}})에 명시).

fields_attributes[:index][value]
: 문자열. 프로필 필드 값입니다. 기본적으로 최대 255자입니다([Instance#profile_field_value_limit]({{< relref "entities/Instance#profile_field_value_limit" >}})에 명시).

#### 응답 {#response-1}

##### 200: 성공 {#200-ok-1}

수정된 프로필을 반환합니다.

##### 401: 인증되지 않음 {#401-unauthorized-1}

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

---

## 프로필 아바타 삭제 {#delete-profile-avatar}

```http
DELETE /api/v1/profile/avatar HTTP/1.1
```

**반환:** [CredentialAccount]({{< relref "entities/Account#CredentialAccount">}})\
**OAuth:** 사용자 토큰 + `write:accounts`\
**버전 이력:**\
4.2.0 - 추가

사용자 프로필에 연결된 아바타를 삭제합니다.

#### 요청 {#request-2}

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 경로 매개변수 {#path-parameters}

#### 응답 {#response-2}

##### 200: 성공 {#200-ok-2}

사용자 프로필에서 아바타를 삭제했습니다. 프로필에 연결된 아바타가 없어도 응답은 삭제 성공을 나타냅니다.

```json
{
  "id": "110357222516183152",
  "username": "rob",
  "acct": "rob",
  "display_name": "",
  "locked": false,
  "bot": false,
  "discoverable": false,
  "group": false,
  "created_at": "2023-05-12T00:00:00.000Z",
  "note": "",
  "url": "http://localhost:3000/@rob",
  "uri": "http://localhost:3000/users/rob",
  "avatar": "http://localhost:3000/avatars/original/missing.png",
  "avatar_static": "http://localhost:3000/avatars/original/missing.png",
  "header": "http://localhost:3000/system/accounts/headers/110/357/222/516/183/152/original/0cd99648c23005ed.png",
  "header_static": "http://localhost:3000/system/accounts/headers/110/357/222/516/183/152/original/0cd99648c23005ed.png",
  "followers_count": 14,
  "following_count": 2,
  "statuses_count": 10,
  "last_status_at": "2023-06-26",
  "noindex": false,
  "source": {
    "privacy": "public",
    "sensitive": false,
    "language": null,
    "note": "",
    "fields": [],
    "follow_requests_count": 0
  },
  "emojis": [],
  "roles": [],
  "fields": [],
  "role": {
    "id": "-99",
    "name": "",
    "permissions": "65536",
    "color": "",
    "highlighted": false
  }
}
```

### 401: 인증되지 않음 {#401-unauthorized-2}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
	"error": "The access token is invalid"
}
```

---

## 프로필 헤더 삭제 {#delete-profile-header}

```http
DELETE /api/v1/profile/header HTTP/1.1
```

**반환:** [CredentialAccount]({{< relref "entities/Account#CredentialAccount">}})\
**OAuth:** 사용자 토큰 + `write:accounts`\
**버전 이력:**\
4.2.0 - 추가

사용자 프로필에 연결된 헤더 이미지를 삭제합니다.

#### 요청 {#request-3}

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 경로 매개변수 {#path-parameters-1}

#### 응답 {#response-3}

##### 200: 성공 {#200-ok-3}

사용자 프로필에서 헤더를 삭제했습니다. 프로필에 연결된 헤더가 없어도 응답은 삭제 성공을 나타냅니다.

```json
{
  "id": "110357222516183152",
  "username": "rob",
  "acct": "rob",
  "display_name": "",
  "locked": false,
  "bot": false,
  "discoverable": false,
  "group": false,
  "created_at": "2023-05-12T00:00:00.000Z",
  "note": "",
  "url": "http://localhost:3000/@rob",
  "uri": "http://localhost:3000/users/rob",
  "avatar": "http://localhost:3000/avatars/original/missing.png",
  "avatar_static": "http://localhost:3000/avatars/original/missing.png",
  "header": "http://localhost:3000/headers/original/missing.png",
  "header_static": "http://localhost:3000/headers/original/missing.png",
  "followers_count": 14,
  "following_count": 2,
  "statuses_count": 10,
  "last_status_at": "2023-06-26",
  "noindex": false,
  "source": {
    "privacy": "public",
    "sensitive": false,
    "language": null,
    "note": "",
    "fields": [],
    "follow_requests_count": 0
  },
  "emojis": [],
  "roles": [],
  "fields": [],
  "role": {
    "id": "-99",
    "name": "",
    "permissions": "65536",
    "color": "",
    "highlighted": false
  }
}
```

### 401: 인증되지 않음 {#401-unauthorized-3}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
	"error": "The access token is invalid"
}
```
