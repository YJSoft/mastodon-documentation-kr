---
title: 대화 API 메서드
description: >-
  다른 참여자와의 개인 대화입니다. (현재는 "direct" 공개 범위의 게시물을 포함한 글타래입니다.)
menu:
  docs:
    name: 대화
    parent: methods-timelines
    identifier: methods-conversations
aliases: [
  "/methods/conversations",
  "/api/methods/conversations",
  "/methods/timelines/conversations",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 모든 대화 조회 {#get}

```http
GET /api/v1/conversations HTTP/1.1
```

**반환:** 배열: [Conversation]({{< relref "entities/conversation" >}})\
**OAuth:** 사용자 토큰 + `read:statuses`\
**버전 이력:**\
2.6.0 - 추가\
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
: 정수. 반환할 최대 결과 수입니다. 기본값은 대화 20개이며 최대 40개입니다.

#### 응답 {#response}

##### 200: 성공 {#200-ok}

limit=2인 API 호출 결과의 일부입니다.

```json
[
  {
    "id": "418450",
    "unread": true,
    "accounts": [
      {
        "id": "482403",
        "username": "amic",
        "acct": "amic@nulled.red",
        // ...
      }
    ],
    "last_status": {
      "id": "103196583826321184",
      "created_at": "2019-11-25T04:08:24.000Z",
      "in_reply_to_id": "103196540587943467",
      "in_reply_to_account_id": "14715",
      // ...
    }
  },
  {
    "id": "418374",
    "unread": false,
    "accounts": [
      {
        "id": "464472",
        "username": "freon",
        "acct": "freon@letsalllovela.in",
        // ...
      }
    ],
    "last_status": {
      "id": "103195253010396431",
      "created_at": "2019-11-24T22:29:56.331Z",
      "in_reply_to_id": "103195239650546339",
      "in_reply_to_account_id": "14715",
      // ...
    }
  }
]
```

AccountConversation ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <https://mastodon.example/api/v1/conversations?limit=2&max_id=108835003356700379>; rel="next", <https://mastodon.example/api/v1/conversations?limit=2&min_id=108888782724768580>; rel="prev"
```

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 대화 제거 {#delete}

```http
DELETE /api/v1/conversations/:id HTTP/1.1
```

대화 목록에서 대화를 제거합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:conversations`\
**버전 이력:**\
2.6.0 - 추가

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 데이터베이스의 Conversation ID입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

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

##### 404: 찾을 수 없음 {#404-not-found}

대화가 없거나 내 소유가 아닙니다.

```json
{
  "error": "Record not found"
}
```

---

## 대화를 읽음으로 표시 {#read}

```http
POST /api/v1/conversations/:id/read HTTP/1.1
```

**반환:** [Conversation]({{< relref "entities/conversation" >}})\
**OAuth:** 사용자 토큰 + `write:conversations`\
**버전 이력:**\
2.6.0 - 추가

#### 요청 {#request-2}

##### 경로 매개변수 {#path-parameters-1}

:id
: {{<required>}} 문자열. 데이터베이스의 Conversation ID입니다.

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

`unread` 값이 false로 변경되었습니다.

```json
{
  "id": "418450",
  "unread": false,
  "accounts": [
    {
      "id": "482403",
      // ...
    }
  ],
  "last_status": {
    "id": "103196583826321184",
    // ...
  }
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

대화가 없거나 내 소유가 아닙니다.

```json
{
  "error": "Record not found"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/conversations_controller.rb" caption="app/controllers/api/v1/conversations_controller.rb" >}}
