---
title: 공지 (Announcement)
description: 관리자가 설정한 공지를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/announcement",
	"/entities/Announcement",
  "/api/entities/announcement",
	"/api/entities/Announcement",
]
---

## 예시 {#example}
```json
{
  "id": "8",
  "content": "<p>Looks like there was an issue processing audio attachments without embedded art since yesterday due to an experimental new feature. That issue has now been fixed, so you may see older posts with audio from other servers pop up in your feeds now as they are being finally properly processed. Sorry!</p>",
  "starts_at": null,
  "ends_at": null,
  "all_day": false,
  "published_at": "2020-07-03T01:27:38.726Z",
  "updated_at": "2020-07-03T01:27:38.752Z",
  "read": true,
  "mentions": [],
  "statuses": [],
  "tags": [],
  "emojis": [],
  "reactions": [
    {
      "name": "bongoCat",
      "count": 9,
      "me": false,
      "url": "https://files.mastodon.social/custom_emojis/images/000/067/715/original/fdba57dff7576d53.png",
      "static_url": "https://files.mastodon.social/custom_emojis/images/000/067/715/static/fdba57dff7576d53.png"
    },
    {
      "name": "thonking",
      "count": 1,
      "me": false,
      "url": "https://files.mastodon.social/custom_emojis/images/000/098/690/original/a8d36edc4a7032e8.png",
      "static_url": "https://files.mastodon.social/custom_emojis/images/000/098/690/static/a8d36edc4a7032e8.png"
    },
    {
      "name": "AAAAAA",
      "count": 1,
      "me": false,
      "url": "https://files.mastodon.social/custom_emojis/images/000/071/387/original/AAAAAA.png",
      "static_url": "https://files.mastodon.social/custom_emojis/images/000/071/387/static/AAAAAA.png"
    },
    {
      "name": "🤔",
      "count": 1,
      "me": true
    }
  ],
  "reactions_allowed": true
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 공지 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
3.1.0 - 추가

### `content` {#content}

**설명:** 공지 내용입니다.\
**유형:** 문자열 (HTML)\
**버전 이력:**\
3.1.0 - 추가

### `starts_at` {#starts_at}

**설명:** 공지 시작 시각입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜와 시각](/api/datetime-format#datetime)) 또는 null\
**버전 이력:**\
3.1.0 - 추가

### `ends_at` {#ends_at}

**설명:** 공지 종료 시각입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜와 시각](/api/datetime-format#datetime)) 또는 null\
**버전 이력:**\
3.1.0 - 추가

### `all_day` {#all_day}

**설명:** 공지를 날짜와 시각 대신 날짜만으로 시작하고 종료할지 나타냅니다. `starts_at` 또는 `ends_at` 시각이 없으면 false입니다.\
**유형:** 불리언\
**버전 이력:**\
3.1.0 - 추가

### `published_at` {#created_at}

**설명:** 공지가 게시된 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
3.1.0 - 추가

### `updated_at` {#updated_at}

**설명:** 공지의 마지막 갱신 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
3.1.0 - 추가

### `read` {{%optional%}} {#read}

**설명:** 현재 사용자가 공지를 읽었는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
3.1.0 - 추가

### `mentions` {#mentions}

**설명:** 공지 본문에서 멘션한 계정입니다.\
**유형:** 배열: [Announcement::Account](#Account)\
**버전 이력:**\
3.1.0 - 추가

### `statuses` {#statuses}

**설명:** 공지 본문에 링크된 게시물입니다.\
**유형:** 배열: [Announcement::Status](#Status)\
**버전 이력:**\
3.1.0 - 추가

### `tags` {#tags}

**설명:** 공지 본문에 링크된 태그입니다.\
**유형:** 배열: [Status::Tag]({{< relref "entities/Status#Tag" >}})\
**버전 이력:**\
3.1.0 - 추가

### `emojis` {#emojis}

**설명:** 공지 본문에서 사용한 사용자 지정 이모지입니다.\
**유형:** 배열: [CustomEmoji]({{< relref "entities/CustomEmoji" >}})\
**버전 이력:**\
3.1.0 - 추가

### `reactions` {#reactions}

**설명:** 공지에 달린 이모지 반응입니다.\
**유형:** 배열: [Reaction]({{< relref "entities/Reaction" >}})\
**버전 이력:**\
3.1.0 - 추가

### `reactions_allowed` {#reactions_allowed}

**설명:** 이 공지에서 이모지 반응을 허용하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
5.0.0 - 추가

## Announcement::Account 속성 {#Account}

### `id` {#Account-id}

**설명:** 멘션된 사용자의 계정 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
3.1.0 - 추가

### `username` {#Account-username}

**설명:** 멘션된 사용자의 사용자명입니다.\
**유형:** 문자열\
**버전 이력:**\
3.1.0 - 추가

### `url` {#Account-url}

**설명:** 멘션된 사용자의 프로필 위치입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
3.1.0 - 추가

### `acct` {#Account-acct}

**설명:** 멘션된 사용자의 WebFinger acct: URI입니다. 로컬 사용자는 `username`, 원격 사용자는 `username@domain`과 같습니다.\
**유형:** 문자열\
**버전 이력:**\
3.1.0 - 추가

## Announcement::Status 속성 {#Status}

### `id` {#Status-id}

**설명:** 데이터베이스의 첨부된 Status ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
3.1.0 - 추가

### `url` {#Status-url}

**설명:** 첨부된 Status의 URL입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
3.1.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/announcements" caption="announcements API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/announcement_serializer.rb" caption="app/serializers/rest/announcement_serializer.rb" >}}
