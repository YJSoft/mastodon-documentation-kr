---
title: 디렉터리 API 메서드
description: 이 웹사이트가 알고 있는 프로필의 디렉터리입니다.
menu:
  docs:
    name: 디렉터리
    parent: methods-instance
    identifier: methods-directory
aliases: [
  "/methods/directory",
  "/api/methods/directory",
  "/methods/instance/directory",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 프로필 디렉터리 조회 {#get}

```http
GET /api/v1/directory HTTP/1.1
```

디렉터리에 표시되는 계정을 나열합니다.

**반환:** 배열: [Account]({{< relref "entities/account" >}})\
**OAuth:** 공개\
**버전 이력:**\
3.0.0 - 추가

#### 요청 {#request}

##### 쿼리 매개변수 {#query-parameters}

offset
: 숫자. 처음 n개 결과를 건너뜁니다.

limit
: 숫자. 가져올 계정 수입니다. 기본값은 계정 40개이며 최대 80개입니다.

order
: 문자열. 최근 게시물 작성 순서(기본값)로 정렬하려면 `active`, 최근 프로필 생성 순서로 정렬하려면 `new`를 사용합니다.

local
: 불리언. true이면 로컬 계정만 반환합니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

limit=2인 결과 예입니다.

```json
[
  {
    "id": "796927",
    "username": "eternalNo3",
    "acct": "eternalNo3@best-friends.chat",
    "display_name": "ESD＠┓（谷）┏",
    // ...
  },
  {
    "id": "787648",
    "username": "ariel",
    "acct": "ariel@best-friends.chat",
    "display_name": "あやっしー🧜🏻‍♀️",
    // ...
  }
]
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/directories_controller.rb" caption="app/controllers/api/v1/directories_controller.rb" >}}
