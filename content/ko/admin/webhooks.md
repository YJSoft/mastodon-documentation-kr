---
title: 웹훅
description: 애플리케이션 이벤트에 대한 실시간 알림
menu:
  docs:
    weight: 120
    parent: admin
---

## 웹훅 관리 {#managing-webhooks}

관리 UI의 **관리 > 웹훅** 영역에서 웹훅을 관리합니다.

엔드포인트를 추가하려면 웹훅을 보낼 URL과
알림을 받을 관련 이벤트를 제공하며, 선택적으로 생성하여 전송할
JSON을 제어하는 페이로드 템플릿을 지정합니다. 기본적으로 JSON은
웹훅 전송을 유발한 레코드를 직렬화한 것입니다.

## 웹훅 수신 {#receiving-webhooks}

관련 이벤트가 생성되면 등록한 URL로 웹훅 페이로드를 `POST`로
전송합니다.

[WebSub 명세][WebSub spec]에서 채택한 `X-Hub-Signature` 헤더가 포함되며,
페이로드의 진위 여부를 검증하는 데 사용할 수 있습니다.

## 이벤트 {#events}

이벤트 이름은 이를 발생시키는 시스템 이벤트를 따릅니다.

지원하는 이벤트는 다음과 같습니다.

* `account.approved`
* `account.created`
* `account.updated`
* `report.created`
* `report.updated`
* `status.created`
* `status.updated`

## 페이로드 예제 {#example-payload}

```json
{
  "event": "report.created",
  "created_at": "2023-10-26T13:34:00.351Z",
  "object": {
    "id": "8437",
    "action_taken": false,
    "action_taken_at": null,
    "category": "violation",
    "comment": "",
    "forwarded": true,
    "created_at": "2023-10-26T13:34:00.348Z",
    "updated_at": "2023-10-26T13:34:00.348Z",
    "account": {
      "id": "123456789",
      "username": "bobisaburger",
      "domain": null,
      "created_at": "2023-07-13T04:39:22.493Z",
      "email": "bobisaburger@emailservice.com",
      "ip": "12.34.56.78",
      "confirmed": true,
      "suspended": false,
      "silenced": false,
      "sensitized": false,
      "disabled": false,
      "approved": true,
      "locale": "en",
      "invite_request": "I would love to be a member of your instance!",
      "ips": [
        {
          "ip": "12.34.56.78",
          "used_at": "2023-07-13T04:45:31.835Z"
        },
        {
          "ip": "98.76.54.32",
          "used_at": "2023-07-13T04:39:22.722Z"
        }
      ],
      "account": {
        "id": "123456789",
        "username": "bobisaburger",
        "acct": "bobisaburger",
        "display_name": "bobisaburger",
        "locked": false,
        "bot": false,
        "discoverable": null,
        "group": false,
        "created_at": "2023-07-13T00:00:00.000Z",
        "note": "",
        "url": "https://mastodonwebsite/@bobisaburger",
        "uri": "https://mastodonwebsite/users/bobisaburger",
        "avatar": "https://locationofavatar.com/image.jpg",
        "avatar_static": "https://locationofavatar.com/image.jpg",
        "header": "locationofheader.com/image.jpg",
        "header_static": "locationofheader.com/image.jpg",
        "followers_count": 100,
        "following_count": 200,
        "statuses_count": 9,
        "last_status_at": "2023-08-05",
        "noindex": true,
        "emojis": [],
        "roles": [],
        "fields": []
      },
      "role": {
        "id": "-99",
        "name": "",
        "permissions": "65536",
        "color": "",
        "highlighted": false
      }
    },
    "target_account": {
      "id": "123454321",
      "username": "cheeseperson",
      "domain": "someothermastodonsite.com",
      "created_at": "2023-08-20T00:00:00.000Z",
      "email": null,
      "ip": null,
      "confirmed": null,
      "suspended": false,
      "silenced": false,
      "sensitized": false,
      "disabled": null,
      "approved": null,
      "locale": null,
      "invite_request": null,
      "ips": null,
      "account": {
        "id": "123454321",
        "username": "cheeseperson",
        "acct": "cheeseperson@someothermastodonsite.com",
        "display_name": "cheeseperson",
        "locked": false,
        "bot": false,
        "discoverable": false,
        "group": false,
        "created_at": "2023-08-20T00:00:00.000Z",
        "note": "",
        "url": "https://someothermastodonsite.com/@cheeseperson",
        "uri": "https://someothermastodonsite.com/users/cheeseperson",
        "avatar": "https://someothermastadonsite.com/avatars/original/missing.png",
        "avatar_static": "https://someothermastadonsite.com/avatars/original/missing.png",
        "header": "locationofheader.com/image.jpg",
        "header_static": "locationofheader.com/image.jpg",
        "followers_count": 2,
        "following_count": 2,
        "statuses_count": 95,
        "last_status_at": "2023-10-26",
        "emojis": [],
        "fields": []
      },
      "role": null
    },
    "assigned_account": null,
    "action_taken_by_account": null,
    "statuses": [
      {
        "id": "12345678987654321",
        "created_at": "2023-10-26T11:29:13.000Z",
        "in_reply_to_id": "1918282746465",
        "in_reply_to_account_id": "101010101010",
        "sensitive": false,
        "spoiler_text": "",
        "visibility": "public",
        "language": "de",
        "uri": "https://someothermastodonsite.com/users/cheeseperson/statuses/111301083360371621",
        "url": "https://someothermastodonsite.com/@cheeseperson/111301083360371621",
        "replies_count": 0,
        "reblogs_count": 0,
        "favourites_count": 0,
        "edited_at": "2023-10-26T11:30:31.000Z",
        "content": "<p>Here is some content</p>",
        "reblog": null,
        "account": {
          "id": "123454321",
          "username": "cheeseperson",
          "acct": "cheeseperson@someothermastodonsite.com",
          "display_name": "cheeseperson",
          "locked": false,
          "bot": false,
          "discoverable": false,
          "group": false,
          "created_at": "2023-08-20T00:00:00.000Z",
          "note": "",
          "url": "https://someothermastodonsite.com/@cheeseperson",
          "uri": "https://someothermastodonsite.com/users/cheeseperson",
          "avatar": "https://someothermastadonsite.com/avatars/original/missing.png",
          "avatar_static": "https://someothermastadonsite.com/avatars/original/missing.png",
          "header": "locationofheader.com/image.jpg",
          "header_static": "locationofheader.com/image.jpg",
          "followers_count": 2,
          "following_count": 2,
          "statuses_count": 95,
          "last_status_at": "2023-10-26",
          "emojis": [],
          "fields": []
        },
        "media_attachments": [],
        "mentions": [
          {
            "id": "101010101010",
            "username": "thirdperson",
            "url": "https://thirdpersonsinstance.com/@thirdperson",
            "acct": "thirdperson@emailwebsite.com"
          }
        ],
        "tags": [],
        "emojis": [],
        "card": null,
        "poll": null
      }
    ],
    "rules": [
      {
        "id": "2",
        "text": "Don't be a meanie!"
      }
    ]
  }
}
```

### 사용자 정의 템플릿 {#custom-templates}

기본 JSON 대신 사용자 정의 템플릿으로 웹훅
페이로드를 생성할 수 있습니다. 템플릿에서는 이중 중괄호 보간 구문으로
기본 페이로드의 값에 접근할 수 있습니다. 예를 들어 간단한 사용자 정의 템플릿은
다음과 같습니다.

```json
{ "content": "Hello {{object.username}}" }
```

이 예제의 `{{object.username}}`은 보간을 통해
원본 이벤트 페이로드의 해당 값으로 바뀝니다.

[WebSub spec]: https://www.w3.org/TR/websub/
