---
title: 투표 API 메서드
description: >-
  게시물에 첨부된 투표를 조회하고 참여합니다. 투표 ID를 찾으려면 먼저 Status를 GET한 다음 `poll` 속성을 확인해야 합니다.
menu:
  docs:
    name: 투표
    parent: methods-statuses
    identifier: methods-polls
aliases: [
  "/methods/polls",
  "/api/methods/polls",
  "/methods/statuses/polls",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 투표 조회 {#get}

```http
GET /api/v1/polls/:id HTTP/1.1
```

게시물에 첨부된 투표를 조회합니다.

**반환:** [Poll]({{< relref "entities/poll" >}})\
**OAuth:** 상위 게시물이 공개이면 공개. 상위 게시물이 비공개이면 사용자 토큰 + `read:statuses`.\
**버전 이력:**\
2.8.0 - 추가

#### 요청 {#request}

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 데이터베이스의 Poll ID입니다.

##### 헤더 {#headers}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

```json
{
  "id": "34830",
  "expires_at": "2019-12-05T04:05:08.302Z",
  "expired": true,
  "multiple": false,
  "votes_count": 10,
  "voters_count": null,
  "voted": true,
  "own_votes": [
    1
  ],
  "options": [
    {
      "title": "accept",
      "votes_count": 6
    },
    {
      "title": "deny",
      "votes_count": 4
    }
  ],
  "emojis": []
}
```

##### 404: 찾을 수 없음 {#404-not-found}

투표가 없거나 상위 게시물이 비공개입니다.

```json
{
  "error": "Record not found"
}
```

---

## 투표 참여 {#vote}

```http
POST /api/v1/polls/:id/votes HTTP/1.1
```

게시물에 첨부된 투표에 참여합니다.

**반환:** [Poll]({{< relref "entities/poll" >}})\
**OAuth:** 사용자 토큰 + `write:statuses`\
**버전 이력:**\
2.8.0 - 추가

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters-1}

:id
: {{<required>}} 문자열. 데이터베이스의 Poll ID입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

choices[]
: {{<required>}} 정수 배열. 각 선택지의 인덱스(0부터 시작)로 내 투표를 제공합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

투표에 참여했습니다.

```json
{
  "id": "34873",
  "expires_at": "2019-12-05T11:16:17.426Z",
  "expired": false,
  "multiple": true,
  "votes_count": 5,
  "voters_count": null,
  "voted": true,
  "own_votes": [
    0,
    2,
    4,
    9,
    6
  ],
  "options": [
    {
      "title": "option 0",
      "votes_count": 1
    },
    {
      "title": "option 1",
      "votes_count": 0
    },
    {
      "title": "option 2",
      "votes_count": 1
    },
    {
      "title": "option 3",
      "votes_count": 0
    },
    {
      "title": "option 4",
      "votes_count": 1
    },
    {
      "title": "option 5",
      "votes_count": 0
    },
    {
      "title": "option 6",
      "votes_count": 1
    },
    {
      "title": "option 7",
      "votes_count": 0
    },
    {
      "title": "option 8",
      "votes_count": 0
    },
    {
      "title": "option 9",
      "votes_count": 1
    }
  ],
  "emojis": []
}
```

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-1}

투표가 없거나 상위 게시물이 비공개입니다.

```json
{
  "error": "Record not found"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

투표가 만료되었습니다.

```json
{
  "error": "Validation failed: The poll has already ended"
}
```

또는 이미 투표했습니다.

```json
{
  "error": "Validation failed: You have already voted on this poll"
}
```

---

## 함께 보기 {#see-also}

{{< page-relref ref="methods/statuses#create" caption="POST /api/v1/statuses (`poll` parameter)" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/polls_controller.rb" caption="app/controllers/api/v1/polls_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/polls/votes_controller.rb" caption="app/controllers/api/v1/polls/votes_controller.rb" >}}
