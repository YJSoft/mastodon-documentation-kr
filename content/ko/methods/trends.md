---
title: 인기 항목 API 메서드
description: 활동이 증가한 태그, 게시물, 링크 목록입니다.
menu:
  docs:
    name: 인기 항목
    parent: methods-instance
    identifier: methods-trends
aliases: [
  "/methods/trends",
  "/api/methods/trends",
  "/methods/instance/trends",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 개요 {#summary}

이 엔드포인트는 태그, 게시물,
링크 각각의 관련 인기 결과를 반환합니다. 결과는 내부 인기 점수에 따라 반환하며,
시간순이나 사전순 정렬을 보장하지 않습니다. 인기 점수는
주기적으로 다시 계산합니다.

## 인기 태그 조회 {#tags}

```http
GET /api/v1/trends/tags HTTP/1.1
```

지난 일주일간 더 자주 사용된 태그입니다.

**반환:** 배열: [Tag]({{< relref "entities/Tag" >}})\
**OAuth:** 공개\
**버전 이력:**\
3.0.0 - 추가\
3.5.0 - 메서드 시그니처를 `GET /api/v1/trends`에서 `GET /api/v1/trends/tags`로 변경. 전자는 향후 제거될 수 있는 사용 중단 예정 별칭입니다.

#### 요청 {#request}

##### 쿼리 매개변수 {#query-parameters}

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 태그 10개이며 최대 20개입니다.

offset
: 정수. 처음 n개 결과를 건너뜁니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

```json
[
  {
    "id": "201",
    "name": "hola",
    "url": "https://mastodon.social/tags/hola",
    "history": [
      {
        "day": "1574726400",
        "uses": "13",
        "accounts": "10"
      },
      // ...
    ]
  },
  {
    "id": "695",
    "name": "SaveDotOrg",
    "url": "https://mastodon.social/tags/SaveDotOrg",
    "history": [
      {
        "day": "1574726400",
        "uses": "9",
        "accounts": "9"
      },
      // ...
    ]
  },
  {
    "id": "415",
    "name": "introduction",
    "url": "https://mastodon.social/tags/introduction",
    "history": [
      {
        "day": "1574726400",
        "uses": "15",
        "accounts": "14"
      },
      // ...
    ]
  },
  // ...
]
```

---

## 인기 게시물 조회 {#statuses}

```http
GET /api/v1/trends/statuses HTTP/1.1
```

다른 게시물보다 상호작용이 많은 게시물입니다.

**반환:** 배열: [Status]({{< relref "entities/Status" >}})\
**OAuth:** 공개\
**버전 이력:**\
3.5.0 - 추가

#### 요청 {#request-1}
##### 쿼리 매개변수 {#query-parameters-1}

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 게시물 20개이며 최대 40개입니다.

offset
: 정수. 처음 n개 결과를 건너뜁니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

```json
[
  {
    "id": "108910940413327534",
    "created_at": "2022-08-30T08:44:26.366Z",
    "in_reply_to_id": null,
    "in_reply_to_account_id": null,
    "sensitive": false,
    // ...
    "content": "<p>In order to prevent such incidents from happening in the future, we are implementing a fixed set of internal guidelines which must be met before any media content can be shared on our social media platforms. The distribution of material which promotes a message of racism or sexism is unacceptable. We can do better and in the future we will do better.</p><p>We apologize again for this incident and can assure you that it will not happen again.</p><p>Your Tutanota Team</p>",
    // ...
  },
  // ...
]
```

---

## 인기 링크 조회 {#links}

```http
GET /api/v1/trends/links HTTP/1.1
```

다른 링크보다 많이 공유된 링크입니다.

**반환:** 배열: [Trends::Link]({{< relref "entities/PreviewCard#trends-link" >}})\
**OAuth:** 공개\
**버전 이력:**\
3.5.0 - 추가

#### 요청 {#request-2}
##### 쿼리 매개변수 {#query-parameters-2}

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 링크 10개이며 최대 20개입니다.

offset
: 정수. 처음 n개 결과를 건너뜁니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

```json
[
  {
    "url": "https://www.nbcnews.com/specials/plan-your-vote-2022-elections/index.html",
    "title": "Plan Your Vote: 2022 Elections",
    "description": "Everything you need to know about the voting rules where you live, including registration, mail-in voting, changes since 2020, and more.",
    "type": "link",
    "author_name": "NBC News",
    "author_url": "",
    "provider_name": "NBC News",
    "provider_url": "",
    "html": "",
    "width": 400,
    "height": 225,
    "image": "https://files.mastodon.social/cache/preview_cards/images/045/027/478/original/0783d5e91a14fd49.jpeg",
    "embed_url": "",
    "blurhash": "UcQmF#ay~qofj[WBj[j[~qof9Fayofofayay",
    "history": [
      {
        "day": "1661817600",
        "accounts": "7",
        "uses": "7"
      },
      {
        "day": "1661731200",
        "accounts": "23",
        "uses": "23"
      },
      {
        "day": "1661644800",
        "accounts": "0",
        "uses": "0"
      },
      {
        "day": "1661558400",
        "accounts": "0",
        "uses": "0"
      },
      {
        "day": "1661472000",
        "accounts": "0",
        "uses": "0"
      },
      {
        "day": "1661385600",
        "accounts": "0",
        "uses": "0"
      },
      {
        "day": "1661299200",
        "accounts": "0",
        "uses": "0"
      }
    ]
  },
  // ...
]
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/trends/links_controller.rb" caption="app/controllers/api/v1/trends/links_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/trends/statuses_controller.rb" caption="app/controllers/api/v1/trends/statuses_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/trends/tags_controller.rb" caption="app/controllers/api/v1/trends/tags_controller.rb" >}}
