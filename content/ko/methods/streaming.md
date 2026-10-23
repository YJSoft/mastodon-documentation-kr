---
title: 스트리밍 API 메서드
description: >-
  오래 유지되는 HTTP 연결이나 WebSocket을 통해 서버 전송 이벤트를 구독하여 실시간 갱신을 받습니다.
menu:
  docs:
    name: 스트리밍
    parent: methods-timelines
    identifier: methods-streaming
aliases: [
  "/methods/streaming",
  "/api/methods/streaming",
  "/methods/timelines/streaming",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 호스트명 탐색 {#hostname-discovery}

서버 구성에 따라 스트리밍 API는 REST API의 다른 부분과 다른 호스트명에서 제공될 수 있습니다. 여기에 설명된 모든 경로는 그 호스트명 값을 기준으로 합니다. 클라이언트는 다음 방법 중 하나로 먼저 호스트명을 얻어야 합니다.

- [서버 엔드포인트](../instance)에서 `configuration.urls.streaming` 값을 추출합니다.
- 일반 호스트의 `api/v1/streaming` 엔드포인트에 REST API 요청을 합니다. 스트리밍 서버 URL이 설정되어 있으면 해당 URL로 리디렉션하고, 같은 호스트를 사용해야 하면 Not Found를 반환합니다.

## 이벤트 유형과 페이로드 {#events}

`update`
: 새 Status가 나타났습니다. 페이로드에는 문자열로 변환한 [Status]({{< relref "entities/Status" >}})가 포함됩니다. v1.0.0부터 사용할 수 있습니다.

`delete`
: 게시물이 삭제되었습니다. 페이로드에는 삭제된 Status의 문자열 ID가 포함됩니다. v1.0.0부터 사용할 수 있습니다.

`notification`
: 새 알림이 나타났습니다. 페이로드에는 문자열로 변환한 [Notification]({{< relref "entities/Notification" >}})이 포함됩니다. v1.4.2부터 사용할 수 있습니다.

`filters_changed`
: 키워드 필터가 변경되었습니다. 페이로드가 없거나(WebSocket 연결) 정의되지 않은 페이로드가 포함됩니다(HTTP 연결). v2.4.3부터 사용할 수 있습니다.

`conversation`
: 개인 대화가 수정되었습니다. 페이로드에는 문자열로 변환한 [Conversation]({{< relref "entities/Conversation" >}})이 포함됩니다. v2.6.0부터 사용할 수 있습니다.

`announcement`
: 공지가 게시되었습니다. 페이로드에는 문자열로 변환한 [Announcement]({{< relref "entities/Announcement" >}})가 포함됩니다. v3.1.0부터 사용할 수 있습니다.

`announcement.reaction`
: 공지에 이모지 반응이 추가되었습니다. 페이로드에는 문자열로 변환한 해시(`name`, `count`, `announcement_id` 포함)가 포함됩니다. v3.1.0부터 사용할 수 있습니다.

`announcement.delete`
: 공지가 삭제되었습니다. 페이로드에는 삭제된 Announcement의 문자열 ID가 포함됩니다. v3.1.0부터 사용할 수 있습니다.

`status.update`
: Status가 편집되었습니다. 페이로드에는 문자열로 변환한 [Status]({{< relref "entities/Status" >}})가 포함됩니다. v3.5.0부터 사용할 수 있습니다.

`notifications_merged`
: 수락한 알림 요청의 병합이 끝났으므로 알림 목록을 새로고침해야 합니다. 페이로드는 무시할 수 있습니다. v4.3.0부터 사용할 수 있습니다.

## 타임라인/분류 스트리밍 {#streams}

`public`
: 서버가 알고 있는 모든 공개 게시물입니다. 연합 타임라인과 비슷합니다. v1.0.0부터 사용할 수 있습니다.

`public:media`
: 서버가 알고 있는 모든 공개 게시물 중 미디어 첨부 파일이 있는 게시물입니다. "미디어만"을 활성화한 연합 타임라인과 비슷합니다. v2.4.0부터 사용할 수 있습니다.

`public:local`
: 이 서버에서 비롯된 모든 공개 게시물입니다. 로컬 타임라인과 비슷합니다. v1.1부터 사용할 수 있습니다.

`public:local:media`
: 이 서버에서 비롯된 모든 공개 게시물 중 미디어 첨부 파일이 있는 게시물입니다. "미디어만"을 활성화한 로컬 타임라인과 비슷합니다. v2.4.0부터 사용할 수 있습니다.

`public:remote`
: 다른 서버에서 비롯된 모든 공개 게시물입니다. v3.1.4부터 사용할 수 있습니다.

`public:remote:media`
: 다른 서버에서 비롯된 모든 공개 게시물 중 미디어 첨부 파일이 있는 게시물입니다. v3.1.4부터 사용할 수 있습니다.

`hashtag`
: 특정 해시태그를 사용하는 모든 공개 게시물입니다. v1.0.0부터 사용할 수 있습니다.

`hashtag:local`
: 이 서버에서 비롯된 특정 해시태그를 사용하는 모든 공개 게시물입니다. v1.1부터 사용할 수 있습니다.

`user`
: 홈 피드 갱신과 알림 등 현재 사용자와 관련된 이벤트입니다. v1.0.0부터 사용할 수 있습니다.

`user:notification`
: 현재 사용자의 알림입니다. v1.4.2부터 사용할 수 있습니다.

`list`
: 특정 리스트의 갱신입니다. v2.1.0부터 사용할 수 있습니다.

`direct`
: 개인 대화의 갱신입니다. v2.4.0부터 사용할 수 있습니다.

---

## HTTP 서버 전송 이벤트 소개 {#http}

애플리케이션은 [서버 전송 이벤트](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) 엔드포인트를 사용하여 실시간 갱신을 받을 수 있습니다. 서버 전송 이벤트는 청크 인코딩 전송에만 의존하는 매우 간단한 전송 방식입니다. 즉 HTTP 연결을 열어 둔 채 주기적으로 새 데이터를 받습니다.

스트림에는 이벤트와 하트비트 주석이 포함됩니다. 파서는 콜론(`:`)으로 시작하는 줄을 무시할 수 있습니다. 예를 들어 하트비트 주석으로 연결을 유지할 수 있습니다.

```text
:thump
```

일반적으로 이벤트는 다음 구조를 갖습니다.

```text
event: <name>
data: <payload>
```

---

## 서버 작동 여부 확인 {#health}

```http
GET /api/v1/streaming/health HTTP/1.1
```

연결하기 전에 스트리밍 서비스가 작동하는지 확인합니다.

**반환:** 문자열\
**OAuth:** 공개\
**버전 이력:**\
2.5.0 - 추가

#### 응답 {#response}
##### 200: 성공 {#200-ok}

스트리밍 서비스가 작동 중입니다.

```text
OK
```

---

## 홈 타임라인과 알림 구독 {#user}

```http
GET /api/v1/streaming/user HTTP/1.1
```

인증된 사용자와 관련된 이벤트, 즉 홈 타임라인과 알림을 반환합니다.

**반환:** `update`, `delete`, `notification`, `filters_changed`, `announcement`, `announcement.reaction`, `announcement.delete`, `status.update`\
**OAuth:** 사용자 토큰 + `read:statuses` + `read:notifications`\
**버전 이력:**\
1.0.0 - 추가\
1.4.2 - 이제 `notification` 반환\
2.4.3 - 이제 `filters_changed` 반환\
3.1.0 - 이제 `announcement`, `announcement.reaction`, `announcement.delete` 반환\
3.5.0 - 이제 `status.update` 반환


#### 요청 {#request}
##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 이벤트 {#events-1}

홈 타임라인 갱신 예:

```text
event: update
data: {"id":"108914327388663283","created_at":"2022-08-30T23:05:46.839Z","in_reply_to_id":"108914298452377720","in_reply_to_account_id":"107946650784398271","sensitive":false,"spoiler_text":"","visibility":"unlisted","language":null,"uri":"https://letsalllovela.in/objects/e9cebb0c-7c75-414f-9608-20b5628e52d7","url":"https://letsalllovela.in/objects/e9cebb0c-7c75-414f-9608-20b5628e52d7","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":null,"favourited":false,"reblogged":false,"muted":false,"bookmarked":false,"content":"<span class=\"h-card\"><a class=\"u-url mention\" href=\"https://pl.nulled.red/users/disarray\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>disarray</span></a></span> glad i was able to help","filtered":[],"reblog":null,"account":{"id":"464472","username":"freon","acct":"freon@letsalllovela.in","display_name":"freon","locked":false,"bot":false,"discoverable":true,"group":false,"created_at":"2018-08-18T00:00:00.000Z","note":"tech archaeologist, unix weenie<br><a class=\"hashtag\" href=\"https://letsalllovela.in/tag/nobot\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#nobot</a>","url":"https://letsalllovela.in/users/freon","avatar":"https://files.mastodon.social/cache/accounts/avatars/000/464/472/original/bfc518d70cf6f13a.png","avatar_static":"https://files.mastodon.social/cache/accounts/avatars/000/464/472/original/bfc518d70cf6f13a.png","header":"https://files.mastodon.social/cache/accounts/headers/000/464/472/original/2e94bd33745f86a6.gif","header_static":"https://files.mastodon.social/cache/accounts/headers/000/464/472/static/2e94bd33745f86a6.png","followers_count":37,"following_count":41,"statuses_count":18442,"last_status_at":"2022-08-30","emojis":[],"fields":[{"name":"pronouns","value":"emacs/xemacs (or he/they)","verified_at":null},{"name":"age","value":"23.66667","verified_at":null}]},"media_attachments":[],"mentions":[{"id":"107946650784398271","username":"disarray","url":"https://pl.nulled.red/users/disarray","acct":"disarray@pl.nulled.red"}],"tags":[],"emojis":[],"card":null,"poll":null}
```

알림 예:

```text
event: notification
data: {"id":"68739215","type":"mention","created_at":"2022-08-30T23:09:54.070Z","account":{"id":"108892712797543112","username":"a","acct":"a@pl.nulled.red","display_name":"a","locked":false,"bot":true,"discoverable":false,"group":false,"created_at":"2022-08-27T00:00:00.000Z","note":"a (pleroma edition)","url":"https://pl.nulled.red/users/a","avatar":"https://files.mastodon.social/cache/accounts/avatars/108/892/712/797/543/112/original/5396d516ae170bb0.png","avatar_static":"https://files.mastodon.social/cache/accounts/avatars/108/892/712/797/543/112/original/5396d516ae170bb0.png","header":"https://files.mastodon.social/cache/accounts/headers/108/892/712/797/543/112/original/f61d0382356caa0e.png","header_static":"https://files.mastodon.social/cache/accounts/headers/108/892/712/797/543/112/original/f61d0382356caa0e.png","followers_count":0,"following_count":0,"statuses_count":12,"last_status_at":"2022-08-30","emojis":[],"fields":[{"name":"mastodon","value":"<a href=\"https://mastodon.social/@trwnh\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@trwnh@mastodon.social</a>","verified_at":null}]},"status":{"id":"108914343542683797","created_at":"2022-08-30T23:09:52.359Z","in_reply_to_id":null,"in_reply_to_account_id":null,"sensitive":false,"spoiler_text":"","visibility":"unlisted","language":null,"uri":"https://pl.nulled.red/objects/64b196c6-3bc5-44d5-8ffb-f760235ee6ca","url":"https://pl.nulled.red/objects/64b196c6-3bc5-44d5-8ffb-f760235ee6ca","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":null,"favourited":false,"reblogged":false,"muted":false,"bookmarked":false,"content":"<span class=\"h-card\"><a class=\"u-url mention\" href=\"https://mastodon.social/@trwnh\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>trwnh</span></a></span> test","filtered":[],"reblog":null,"account":{"id":"108892712797543112","username":"a","acct":"a@pl.nulled.red","display_name":"a","locked":false,"bot":true,"discoverable":false,"group":false,"created_at":"2022-08-27T00:00:00.000Z","note":"a (pleroma edition)","url":"https://pl.nulled.red/users/a","avatar":"https://files.mastodon.social/cache/accounts/avatars/108/892/712/797/543/112/original/5396d516ae170bb0.png","avatar_static":"https://files.mastodon.social/cache/accounts/avatars/108/892/712/797/543/112/original/5396d516ae170bb0.png","header":"https://files.mastodon.social/cache/accounts/headers/108/892/712/797/543/112/original/f61d0382356caa0e.png","header_static":"https://files.mastodon.social/cache/accounts/headers/108/892/712/797/543/112/original/f61d0382356caa0e.png","followers_count":0,"following_count":0,"statuses_count":12,"last_status_at":"2022-08-30","emojis":[],"fields":[{"name":"mastodon","value":"<a href=\"https://mastodon.social/@trwnh\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@trwnh@mastodon.social</a>","verified_at":null}]},"media_attachments":[],"mentions":[{"id":"14715","username":"trwnh","url":"https://mastodon.social/@trwnh","acct":"trwnh"}],"tags":[],"emojis":[],"card":null,"poll":null}}
```

필터 변경 예:

```text
event: filters_changed
data: undefined
```

공지 예:

```text
event: announcement
data: {"id":"1","content":"<p>test</p>","starts_at":null,"ends_at":null,"all_day":true,"published_at":"2022-11-15T15:55:22.452Z","updated_at":"2022-11-15T15:55:22.528Z","mentions":[],"statuses":[],"tags":[],"emojis":[],"reactions":[]}
```

공지 반응 예:

```text
event: announcement.reaction
data: {"name":"🤔","count":1,"announcement_id":"1"}
```

공지 삭제 예:

```text
event: announcement.delete
data: 1
```

게시물 편집 예:

```text
event: status.update
data: {"id":"109348677773283527","created_at":"2022-11-15T16:06:48.410Z","in_reply_to_id":null,"in_reply_to_account_id":null,"sensitive":false,"spoiler_text":"","visibility":"public","language":"en","uri":"http://mastodon.local/users/admin/statuses/109348677773283527","url":"http://mastodon.local/@admin/109348677773283527","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":"2022-11-15T16:07:29.023Z","content":"<p>edited</p>","reblog":null,"application":{"name":"Web","website":null},"account":{"id":"109334860508022726","username":"admin","acct":"admin","display_name":"","locked":false,"bot":false,"discoverable":null,"group":false,"created_at":"2022-11-13T00:00:00.000Z","note":"","url":"http://mastodon.local/@admin","avatar":"http://mastodon.local/avatars/original/missing.png","avatar_static":"http://mastodon.local/avatars/original/missing.png","header":"http://mastodon.local/headers/original/missing.png","header_static":"http://mastodon.local/headers/original/missing.png","followers_count":0,"following_count":0,"statuses_count":4,"last_status_at":"2022-11-15","noindex":false,"emojis":[],"fields":[]},"media_attachments":[],"mentions":[],"tags":[],"emojis":[],"card":null,"poll":null,"favourited":false,"reblogged":false,"muted":false,"bookmarked":false,"pinned":false,"filtered":[]}
```

---

## 알림 구독 {#notification}

```http
GET /api/v1/streaming/user/notification HTTP/1.1
```

수신한 알림의 이벤트를 반환합니다.

**반환:** `notification`\
**OAuth:** 사용자 토큰 + `read:statuses` + `read:notifications`\
**버전 이력:**\
1.4.2 - 추가

#### 요청 {#request-1}
##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 이벤트 {#events-2}

알림 예:

```text
event: notification
data: {"id":"68739215","type":"mention","created_at":"2022-08-30T23:09:54.070Z","account":{"id":"108892712797543112","username":"a","acct":"a@pl.nulled.red","display_name":"a","locked":false,"bot":true,"discoverable":false,"group":false,"created_at":"2022-08-27T00:00:00.000Z","note":"a (pleroma edition)","url":"https://pl.nulled.red/users/a","avatar":"https://files.mastodon.social/cache/accounts/avatars/108/892/712/797/543/112/original/5396d516ae170bb0.png","avatar_static":"https://files.mastodon.social/cache/accounts/avatars/108/892/712/797/543/112/original/5396d516ae170bb0.png","header":"https://files.mastodon.social/cache/accounts/headers/108/892/712/797/543/112/original/f61d0382356caa0e.png","header_static":"https://files.mastodon.social/cache/accounts/headers/108/892/712/797/543/112/original/f61d0382356caa0e.png","followers_count":0,"following_count":0,"statuses_count":12,"last_status_at":"2022-08-30","emojis":[],"fields":[{"name":"mastodon","value":"<a href=\"https://mastodon.social/@trwnh\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@trwnh@mastodon.social</a>","verified_at":null}]},"status":{"id":"108914343542683797","created_at":"2022-08-30T23:09:52.359Z","in_reply_to_id":null,"in_reply_to_account_id":null,"sensitive":false,"spoiler_text":"","visibility":"unlisted","language":null,"uri":"https://pl.nulled.red/objects/64b196c6-3bc5-44d5-8ffb-f760235ee6ca","url":"https://pl.nulled.red/objects/64b196c6-3bc5-44d5-8ffb-f760235ee6ca","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":null,"favourited":false,"reblogged":false,"muted":false,"bookmarked":false,"content":"<span class=\"h-card\"><a class=\"u-url mention\" href=\"https://mastodon.social/@trwnh\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>trwnh</span></a></span> test","filtered":[],"reblog":null,"account":{"id":"108892712797543112","username":"a","acct":"a@pl.nulled.red","display_name":"a","locked":false,"bot":true,"discoverable":false,"group":false,"created_at":"2022-08-27T00:00:00.000Z","note":"a (pleroma edition)","url":"https://pl.nulled.red/users/a","avatar":"https://files.mastodon.social/cache/accounts/avatars/108/892/712/797/543/112/original/5396d516ae170bb0.png","avatar_static":"https://files.mastodon.social/cache/accounts/avatars/108/892/712/797/543/112/original/5396d516ae170bb0.png","header":"https://files.mastodon.social/cache/accounts/headers/108/892/712/797/543/112/original/f61d0382356caa0e.png","header_static":"https://files.mastodon.social/cache/accounts/headers/108/892/712/797/543/112/original/f61d0382356caa0e.png","followers_count":0,"following_count":0,"statuses_count":12,"last_status_at":"2022-08-30","emojis":[],"fields":[{"name":"mastodon","value":"<a href=\"https://mastodon.social/@trwnh\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@trwnh@mastodon.social</a>","verified_at":null}]},"media_attachments":[],"mentions":[{"id":"14715","username":"trwnh","url":"https://mastodon.social/@trwnh","acct":"trwnh"}],"tags":[],"emojis":[],"card":null,"poll":null}}
```

---

## 연합 타임라인 구독 {#public}

```http
GET /api/v1/streaming/public HTTP/1.1
```

모든 공개 게시물을 반환합니다.

**반환:** `update`, `delete`, `status.update`\
**OAuth:** 사용자 토큰 + `read:statuses`\
**버전 이력:**\
1.0.0 - 추가\
2.4.0 - `only_media` 매개변수 추가\
3.5.0 - 이제 `status.update` 반환\
4.2.0 - 사용자 토큰이 필수가 되어 공개 및 앱 토큰 접근 제거 [#23989](https://github.com/mastodon/mastodon/pull/23989)

#### 요청 {#request-2}
##### 헤더 {#headers-2}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters}

only_media
: 불리언. true이면 미디어 첨부 파일이 있는 게시물만 반환합니다.

#### 이벤트 {#events-3}

연합 타임라인 갱신 예:

```text
event: update
data: {"id":"108914354907984653","created_at":"2022-08-30T23:12:47.000Z","in_reply_to_id":null,"in_reply_to_account_id":null,"sensitive":false,"spoiler_text":"","visibility":"public","language":"en","uri":"https://mstdn.jp/users/aiueohisama/statuses/108914354891945610","url":"https://mstdn.jp/@aiueohisama/108914354891945610","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":null,"content":"<p>処女の子が「処女だからキモい絡み方しちゃうかもだけど許して🥺」なんて言ってるのわたしは見たことない、童貞の甘えだよそれは 嫌われたくないなら最低限のマナーくらい身につけた方がいい</p>","reblog":null,"account":{"id":"272619","username":"aiueohisama","acct":"aiueohisama@mstdn.jp","display_name":"💎🌻陽菜💙💛","locked":false,"bot":false,"discoverable":false,"group":false,"created_at":"2017-04-15T00:00:00.000Z","note":"<p>とっても素直で真面目なOLでし！</p>","url":"https://mstdn.jp/@aiueohisama","avatar":"https://files.mastodon.social/cache/accounts/avatars/000/272/619/original/573669a325c87b8b.jpeg","avatar_static":"https://files.mastodon.social/cache/accounts/avatars/000/272/619/original/573669a325c87b8b.jpeg","header":"https://files.mastodon.social/cache/accounts/headers/000/272/619/original/5d5dad59a9fd1531.jpeg","header_static":"https://files.mastodon.social/cache/accounts/headers/000/272/619/original/5d5dad59a9fd1531.jpeg","followers_count":182,"following_count":20,"statuses_count":1128,"last_status_at":"2022-08-30","emojis":[],"fields":[]},"media_attachments":[],"mentions":[],"tags":[],"emojis":[],"card":null,"poll":null,"filter_results":[]}
```

삭제 예:

```text
event: delete
data: 107214471804101576
```

게시물 편집 예:

```text
event: status.update
data: {"id":"109348684737626801","created_at":"2022-11-15T16:08:30.000Z","in_reply_to_id":null,"in_reply_to_account_id":null,"sensitive":false,"spoiler_text":"","visibility":"public","language":"en","uri":"https://ruby.social/users/chrismo/statuses/109348684454557541","url":"https://ruby.social/@chrismo/109348684454557541","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":"2022-11-15T16:10:43.000Z","content":"<p><a href=\"https://ruby.social/tags/musicTuesday\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>musicTuesday</span></a> </p><p>Here's a solo <a href=\"https://ruby.social/tags/piano\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>piano</span></a> track of mine called Gravity Assist</p><p><a href=\"https://ruby.social/tags/neoclassical\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>neoclassical</span></a> (<a href=\"https://ruby.social/tags/jazz\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>jazz</span></a> ish)</p><p><a href=\"https://cstudios.bandcamp.com/track/celestia-gravity-assist-no-19-var-2\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"ellipsis\">cstudios.bandcamp.com/track/ce</span><span class=\"invisible\">lestia-gravity-assist-no-19-var-2</span></a></p>","reblog":null,"account":{"id":"795442","username":"chrismo","acct":"chrismo@ruby.social","display_name":"chrismo","locked":false,"bot":false,"discoverable":true,"group":false,"created_at":"2019-04-25T00:00:00.000Z","note":"<p>i mash keys</p>","url":"https://ruby.social/@chrismo","avatar":"https://files.mastodon.social/cache/accounts/avatars/000/795/442/original/12084217a7eb7513.png","avatar_static":"https://files.mastodon.social/cache/accounts/avatars/000/795/442/original/12084217a7eb7513.png","header":"https://static-cdn.mastodon.social/headers/original/missing.png","header_static":"https://static-cdn.mastodon.social/headers/original/missing.png","followers_count":40,"following_count":62,"statuses_count":42,"last_status_at":"2022-11-15","emojis":[],"fields":[{"name":"web","value":"clabs.org","verified_at":null},{"name":"github","value":"github.com/chrismo","verified_at":null},{"name":"twitter","value":"twitter.com/the_chrismo","verified_at":null},{"name":"bandcamp","value":"cstudios.bandcamp.com","verified_at":null}]},"media_attachments":[],"mentions":[],"tags":[{"name":"MUSICTUESDAY","url":"https://mastodon.social/tags/MUSICTUESDAY"},{"name":"piano","url":"https://mastodon.social/tags/piano"},{"name":"neoclassical","url":"https://mastodon.social/tags/neoclassical"},{"name":"jazz","url":"https://mastodon.social/tags/jazz"}],"emojis":[],"card":null,"poll":null}
```

---

## 로컬 타임라인 구독 {#public-local}

```http
GET /api/v1/streaming/public/local HTTP/1.1
```

모든 로컬 공개 게시물을 반환합니다.

**반환:** `update`, `delete`, `status.update`\
**OAuth:** 사용자 토큰 + `read:statuses`\
**버전 이력:**\
1.1.0 - 추가\
2.4.0 - `only_media` 매개변수 추가\
3.5.0 - 이제 `status.update` 반환\
4.2.0 - 사용자 토큰이 필수가 되어 공개 및 앱 토큰 접근 제거 [#23989](https://github.com/mastodon/mastodon/pull/23989)

#### 요청 {#request-3}
##### 헤더 {#headers-3}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-1}

only_media
: 불리언. true이면 미디어 첨부 파일이 있는 게시물만 반환합니다.

#### 이벤트 {#events-4}

로컬 타임라인 갱신 예:

```text
event: update
data: {"id":"108914398911648589","created_at":"2022-08-30T23:23:58.863Z","in_reply_to_id":null,"in_reply_to_account_id":null,"sensitive":false,"spoiler_text":"","visibility":"public","language":"en","uri":"https://mastodon.social/users/trwnh/statuses/108914398911648589","url":"https://mastodon.social/@trwnh/108914398911648589","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":null,"content":"<p>test</p>","reblog":null,"application":{"name":"Web","website":null},"account":{"id":"14715","username":"trwnh","acct":"trwnh","display_name":"infinite love ⴳ","locked":false,"bot":false,"discoverable":true,"group":false,"created_at":"2016-11-24T00:00:00.000Z","note":"<p>i have approximate knowledge of many things. perpetual student. (nb/ace/they)</p><p>xmpp/email: a@trwnh.com<br /><a href=\"https://trwnh.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer\"><span class=\"invisible\">https://</span><span class=\"\">trwnh.com</span><span class=\"invisible\"></span></a><br />help me live: <a href=\"https://liberapay.com/trwnh\" target=\"_blank\" rel=\"nofollow noopener noreferrer\"><span class=\"invisible\">https://</span><span class=\"\">liberapay.com/trwnh</span><span class=\"invisible\"></span></a> or paypal</p><p>- my triggers are moths and glitter<br />- i have all notifs except mentions turned off, so please interact if you wanna be friends! i literally will not notice otherwise<br />- dm me if i did something wrong, so i can improve<br />- purest person on fedi, do not lewd in my presence</p>","url":"https://mastodon.social/@trwnh","avatar":"https://files.mastodon.social/accounts/avatars/000/014/715/original/e430cc93d56f5ac2.png","avatar_static":"https://files.mastodon.social/accounts/avatars/000/014/715/original/e430cc93d56f5ac2.png","header":"https://files.mastodon.social/accounts/headers/000/014/715/original/5c6fc24edb3bb873.jpg","header_static":"https://files.mastodon.social/accounts/headers/000/014/715/original/5c6fc24edb3bb873.jpg","followers_count":2520,"following_count":266,"statuses_count":59817,"last_status_at":"2022-08-30","emojis":[],"fields":[{"name":"Website","value":"<a href=\"https://trwnh.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">trwnh.com</span><span class=\"invisible\"></span></a>","verified_at":"2019-08-29T04:14:55.571+00:00"},{"name":"Portfolio","value":"<a href=\"https://abdullahtarawneh.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">abdullahtarawneh.com</span><span class=\"invisible\"></span></a>","verified_at":"2021-02-11T20:34:13.574+00:00"},{"name":"Fan of:","value":"Punk-rock and post-hardcore (Circa Survive, letlive., La Dispute, THE FEVER 333)Manga (Yu-Gi-Oh!, One Piece, JoJo&#39;s Bizarre Adventure, Death Note, Shaman King)Platformers and RPGs (Banjo-Kazooie, Boktai, Final Fantasy Crystal Chronicles)","verified_at":null},{"name":"What to expect:","value":"talking about various things i find interesting, and otherwise being a genuine and decent wholesome poster. i&#39;m just here to hang out and talk to cool people! and to spill my thoughts.","verified_at":null}]},"media_attachments":[],"mentions":[],"tags":[],"emojis":[],"card":null,"poll":null}
```

삭제 예:

```text
event: delete
data: 108914398911648589
```

게시물 편집 예:

```
event: status.update
data: {"id":"109348699525106378","created_at":"2022-11-15T16:12:20.310Z","in_reply_to_id":"109348674754176227","in_reply_to_account_id":"30437","sensitive":false,"spoiler_text":"","visibility":"public","language":"en","uri":"https://mastodon.social/users/gregpak/statuses/109348699525106378","url":"https://mastodon.social/@gregpak/109348699525106378","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":"2022-11-15T16:12:41.694Z","content":"<p>By default, in Feedly it just shows a thumbnail of the images in a post, though. And NetNewsWire doesn&#39;t show any image, boo! Gotta find an RSS reader that&#39;ll show a full sized image automatically without requiring a clickthrough... any suggestions would be very welcome, thanks!</p>","reblog":null,"account":{"id":"30437","username":"gregpak","acct":"gregpak","display_name":"Greg Pak","locked":false,"bot":false,"discoverable":false,"group":false,"created_at":"2017-04-02T00:00:00.000Z","note":"<p>Comic book writer &amp; filmmaker. Mech Cadet Yu, Planet Hulk, Darth Vader, Ronin Island, Princess Who Saved. Get vaxxed, get out the vote. He/Him.<br /><a href=\"https://mastodon.social/tags/Comics\" class=\"mention hashtag\" rel=\"tag\">#<span>Comics</span></a> <a href=\"https://mastodon.social/tags/ComicBooks\" class=\"mention hashtag\" rel=\"tag\">#<span>ComicBooks</span></a> <a href=\"https://mastodon.social/tags/writing\" class=\"mention hashtag\" rel=\"tag\">#<span>writing</span></a> <a href=\"https://mastodon.social/tags/AmWriting\" class=\"mention hashtag\" rel=\"tag\">#<span>AmWriting</span></a> <a href=\"https://mastodon.social/tags/photography\" class=\"mention hashtag\" rel=\"tag\">#<span>photography</span></a>  <a href=\"https://mastodon.social/tags/BelieveInFilm\" class=\"mention hashtag\" rel=\"tag\">#<span>BelieveInFilm</span></a></p>","url":"https://mastodon.social/@gregpak","avatar":"https://files.mastodon.social/accounts/avatars/000/030/437/original/9a71f06d6e285f32.jpg","avatar_static":"https://files.mastodon.social/accounts/avatars/000/030/437/original/9a71f06d6e285f32.jpg","header":"https://files.mastodon.social/accounts/headers/000/030/437/original/1f589d01e13340bc.jpg","header_static":"https://files.mastodon.social/accounts/headers/000/030/437/original/1f589d01e13340bc.jpg","followers_count":2307,"following_count":279,"statuses_count":818,"last_status_at":"2022-11-15","noindex":false,"emojis":[],"fields":[{"name":"Website/Blog","value":"<a href=\"https://gregpak.com/\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">gregpak.com/</span><span class=\"invisible\"></span></a>","verified_at":"2022-11-04T19:59:52.817+00:00"},{"name":"Newsletter","value":"<a href=\"https://gregpak.com/newsletter\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">gregpak.com/newsletter</span><span class=\"invisible\"></span></a>","verified_at":"2022-11-04T19:59:58.287+00:00"},{"name":"Shop","value":"<a href=\"https://gregpakshop.com/pages/about-us\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">gregpakshop.com/pages/about-us</span><span class=\"invisible\"></span></a>","verified_at":"2022-11-07T05:50:02.310+00:00"}]},"media_attachments":[],"mentions":[],"tags":[],"emojis":[],"card":null,"poll":null}
```

---

## 원격 게시물 구독 {#public-remote}

```http
GET /api/v1/streaming/public/remote HTTP/1.1
```

원격 서버의 모든 공개 게시물을 반환합니다.

**반환:** `update`, `delete`, `status.update`\
**OAuth:** 사용자 토큰 + `read:statuses`\
**버전 이력:**\
3.1.4 - 추가\
3.5.0 - 이제 `status.update` 반환\
4.2.0 - 사용자 토큰이 필수가 되어 공개 및 앱 토큰 접근 제거 [#23989](https://github.com/mastodon/mastodon/pull/23989)

#### 요청 {#request-4}
##### 헤더 {#headers-4}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-2}

only_media
: 불리언. true이면 미디어 첨부 파일이 있는 게시물만 반환합니다.

#### 이벤트 {#events-5}

갱신 예:

```text
event: update
data: {"id":"108914354907984653","created_at":"2022-08-30T23:12:47.000Z","in_reply_to_id":null,"in_reply_to_account_id":null,"sensitive":false,"spoiler_text":"","visibility":"public","language":"en","uri":"https://mstdn.jp/users/aiueohisama/statuses/108914354891945610","url":"https://mstdn.jp/@aiueohisama/108914354891945610","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":null,"content":"<p>処女の子が「処女だからキモい絡み方しちゃうかもだけど許して🥺」なんて言ってるのわたしは見たことない、童貞の甘えだよそれは 嫌われたくないなら最低限のマナーくらい身につけた方がいい</p>","reblog":null,"account":{"id":"272619","username":"aiueohisama","acct":"aiueohisama@mstdn.jp","display_name":"💎🌻陽菜💙💛","locked":false,"bot":false,"discoverable":false,"group":false,"created_at":"2017-04-15T00:00:00.000Z","note":"<p>とっても素直で真面目なOLでし！</p>","url":"https://mstdn.jp/@aiueohisama","avatar":"https://files.mastodon.social/cache/accounts/avatars/000/272/619/original/573669a325c87b8b.jpeg","avatar_static":"https://files.mastodon.social/cache/accounts/avatars/000/272/619/original/573669a325c87b8b.jpeg","header":"https://files.mastodon.social/cache/accounts/headers/000/272/619/original/5d5dad59a9fd1531.jpeg","header_static":"https://files.mastodon.social/cache/accounts/headers/000/272/619/original/5d5dad59a9fd1531.jpeg","followers_count":182,"following_count":20,"statuses_count":1128,"last_status_at":"2022-08-30","emojis":[],"fields":[]},"media_attachments":[],"mentions":[],"tags":[],"emojis":[],"card":null,"poll":null,"filter_results":[]}
```

삭제 예:

```text
event: delete
data: 107214471804101576
```

게시물 편집 예:

```text
event: status.update
data: {"id":"109348684737626801","created_at":"2022-11-15T16:08:30.000Z","in_reply_to_id":null,"in_reply_to_account_id":null,"sensitive":false,"spoiler_text":"","visibility":"public","language":"en","uri":"https://ruby.social/users/chrismo/statuses/109348684454557541","url":"https://ruby.social/@chrismo/109348684454557541","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":"2022-11-15T16:10:43.000Z","content":"<p><a href=\"https://ruby.social/tags/musicTuesday\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>musicTuesday</span></a> </p><p>Here's a solo <a href=\"https://ruby.social/tags/piano\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>piano</span></a> track of mine called Gravity Assist</p><p><a href=\"https://ruby.social/tags/neoclassical\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>neoclassical</span></a> (<a href=\"https://ruby.social/tags/jazz\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>jazz</span></a> ish)</p><p><a href=\"https://cstudios.bandcamp.com/track/celestia-gravity-assist-no-19-var-2\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"ellipsis\">cstudios.bandcamp.com/track/ce</span><span class=\"invisible\">lestia-gravity-assist-no-19-var-2</span></a></p>","reblog":null,"account":{"id":"795442","username":"chrismo","acct":"chrismo@ruby.social","display_name":"chrismo","locked":false,"bot":false,"discoverable":true,"group":false,"created_at":"2019-04-25T00:00:00.000Z","note":"<p>i mash keys</p>","url":"https://ruby.social/@chrismo","avatar":"https://files.mastodon.social/cache/accounts/avatars/000/795/442/original/12084217a7eb7513.png","avatar_static":"https://files.mastodon.social/cache/accounts/avatars/000/795/442/original/12084217a7eb7513.png","header":"https://static-cdn.mastodon.social/headers/original/missing.png","header_static":"https://static-cdn.mastodon.social/headers/original/missing.png","followers_count":40,"following_count":62,"statuses_count":42,"last_status_at":"2022-11-15","emojis":[],"fields":[{"name":"web","value":"clabs.org","verified_at":null},{"name":"github","value":"github.com/chrismo","verified_at":null},{"name":"twitter","value":"twitter.com/the_chrismo","verified_at":null},{"name":"bandcamp","value":"cstudios.bandcamp.com","verified_at":null}]},"media_attachments":[],"mentions":[],"tags":[{"name":"MUSICTUESDAY","url":"https://mastodon.social/tags/MUSICTUESDAY"},{"name":"piano","url":"https://mastodon.social/tags/piano"},{"name":"neoclassical","url":"https://mastodon.social/tags/neoclassical"},{"name":"jazz","url":"https://mastodon.social/tags/jazz"}],"emojis":[],"card":null,"poll":null}
```

---

## 해시태그의 공개 타임라인 구독 {#hashtag}

```http
GET /api/v1/streaming/hashtag HTTP/1.1
```

특정 해시태그의 모든 공개 게시물을 반환합니다.

**반환:** `update`, `delete`, `status.update`\
**OAuth:** 사용자 토큰 + `read:statuses`\
**버전 이력:**\
1.0.0 - 추가\
3.5.0 - 이제 `status.update` 반환\
4.2.0 - 사용자 토큰이 필수가 되어 공개 및 앱 토큰 접근 제거 [#23989](https://github.com/mastodon/mastodon/pull/23989)

#### 요청 {#request-5}
##### 헤더 {#headers-5}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-3}

tag
: {{<required>}} 문자열. 구독할 해시태그 이름입니다.

#### 이벤트 {#events-6}

해시태그 타임라인 갱신 예:

```text
event: update
data: {"id":"108914430312582020","created_at":"2022-08-30T23:31:58.006Z","in_reply_to_id":null,"in_reply_to_account_id":null,"sensitive":false,"spoiler_text":"","visibility":"public","language":"en","uri":"https://mastodon.social/users/trwnh/statuses/108914430312582020","url":"https://mastodon.social/@trwnh/108914430312582020","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":null,"content":"<p><a href=\"https://mastodon.social/tags/test\" class=\"mention hashtag\" rel=\"tag\">#<span>test</span></a></p>","reblog":null,"application":{"name":"Web","website":null},"account":{"id":"14715","username":"trwnh","acct":"trwnh","display_name":"infinite love ⴳ","locked":false,"bot":false,"discoverable":true,"group":false,"created_at":"2016-11-24T00:00:00.000Z","note":"<p>i have approximate knowledge of many things. perpetual student. (nb/ace/they)</p><p>xmpp/email: a@trwnh.com<br /><a href=\"https://trwnh.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer\"><span class=\"invisible\">https://</span><span class=\"\">trwnh.com</span><span class=\"invisible\"></span></a><br />help me live: <a href=\"https://liberapay.com/trwnh\" target=\"_blank\" rel=\"nofollow noopener noreferrer\"><span class=\"invisible\">https://</span><span class=\"\">liberapay.com/trwnh</span><span class=\"invisible\"></span></a> or paypal</p><p>- my triggers are moths and glitter<br />- i have all notifs except mentions turned off, so please interact if you wanna be friends! i literally will not notice otherwise<br />- dm me if i did something wrong, so i can improve<br />- purest person on fedi, do not lewd in my presence</p>","url":"https://mastodon.social/@trwnh","avatar":"https://files.mastodon.social/accounts/avatars/000/014/715/original/e430cc93d56f5ac2.png","avatar_static":"https://files.mastodon.social/accounts/avatars/000/014/715/original/e430cc93d56f5ac2.png","header":"https://files.mastodon.social/accounts/headers/000/014/715/original/5c6fc24edb3bb873.jpg","header_static":"https://files.mastodon.social/accounts/headers/000/014/715/original/5c6fc24edb3bb873.jpg","followers_count":2520,"following_count":266,"statuses_count":59817,"last_status_at":"2022-08-30","emojis":[],"fields":[{"name":"Website","value":"<a href=\"https://trwnh.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">trwnh.com</span><span class=\"invisible\"></span></a>","verified_at":"2019-08-29T04:14:55.571+00:00"},{"name":"Portfolio","value":"<a href=\"https://abdullahtarawneh.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">abdullahtarawneh.com</span><span class=\"invisible\"></span></a>","verified_at":"2021-02-11T20:34:13.574+00:00"},{"name":"Fan of:","value":"Punk-rock and post-hardcore (Circa Survive, letlive., La Dispute, THE FEVER 333)Manga (Yu-Gi-Oh!, One Piece, JoJo&#39;s Bizarre Adventure, Death Note, Shaman King)Platformers and RPGs (Banjo-Kazooie, Boktai, Final Fantasy Crystal Chronicles)","verified_at":null},{"name":"What to expect:","value":"talking about various things i find interesting, and otherwise being a genuine and decent wholesome poster. i&#39;m just here to hang out and talk to cool people! and to spill my thoughts.","verified_at":null}]},"media_attachments":[],"mentions":[],"tags":[{"name":"test","url":"https://mastodon.social/tags/test"}],"emojis":[],"card":null,"poll":null}
```

삭제 예:

```text
event: delete
data: 108914430312582020
```

게시물 편집 예:

```text
event: status.update
data: {"id":"109348684737626801","created_at":"2022-11-15T16:08:30.000Z","in_reply_to_id":null,"in_reply_to_account_id":null,"sensitive":false,"spoiler_text":"","visibility":"public","language":"en","uri":"https://ruby.social/users/chrismo/statuses/109348684454557541","url":"https://ruby.social/@chrismo/109348684454557541","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":"2022-11-15T16:10:43.000Z","content":"<p><a href=\"https://ruby.social/tags/musicTuesday\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>musicTuesday</span></a> </p><p>Here's a solo <a href=\"https://ruby.social/tags/piano\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>piano</span></a> track of mine called Gravity Assist</p><p><a href=\"https://ruby.social/tags/neoclassical\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>neoclassical</span></a> (<a href=\"https://ruby.social/tags/jazz\" class=\"mention hashtag\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#<span>jazz</span></a> ish)</p><p><a href=\"https://cstudios.bandcamp.com/track/celestia-gravity-assist-no-19-var-2\" rel=\"nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"ellipsis\">cstudios.bandcamp.com/track/ce</span><span class=\"invisible\">lestia-gravity-assist-no-19-var-2</span></a></p>","reblog":null,"account":{"id":"795442","username":"chrismo","acct":"chrismo@ruby.social","display_name":"chrismo","locked":false,"bot":false,"discoverable":true,"group":false,"created_at":"2019-04-25T00:00:00.000Z","note":"<p>i mash keys</p>","url":"https://ruby.social/@chrismo","avatar":"https://files.mastodon.social/cache/accounts/avatars/000/795/442/original/12084217a7eb7513.png","avatar_static":"https://files.mastodon.social/cache/accounts/avatars/000/795/442/original/12084217a7eb7513.png","header":"https://static-cdn.mastodon.social/headers/original/missing.png","header_static":"https://static-cdn.mastodon.social/headers/original/missing.png","followers_count":40,"following_count":62,"statuses_count":42,"last_status_at":"2022-11-15","emojis":[],"fields":[{"name":"web","value":"clabs.org","verified_at":null},{"name":"github","value":"github.com/chrismo","verified_at":null},{"name":"twitter","value":"twitter.com/the_chrismo","verified_at":null},{"name":"bandcamp","value":"cstudios.bandcamp.com","verified_at":null}]},"media_attachments":[],"mentions":[],"tags":[{"name":"MUSICTUESDAY","url":"https://mastodon.social/tags/MUSICTUESDAY"},{"name":"piano","url":"https://mastodon.social/tags/piano"},{"name":"neoclassical","url":"https://mastodon.social/tags/neoclassical"},{"name":"jazz","url":"https://mastodon.social/tags/jazz"}],"emojis":[],"card":null,"poll":null}
```

---

## 해시태그의 로컬 타임라인 구독 {#hashtag-local}

```http
GET /api/v1/streaming/hashtag/local HTTP/1.1
```

특정 해시태그의 모든 로컬 공개 게시물을 반환합니다.

**반환:** `update`, `delete`, `status.update`\
**OAuth:** 사용자 토큰 + `read:statuses`\
**버전 이력:**\
1.1.0 - 추가\
3.5.0 - 이제 `status.update` 반환\
4.2.0 - 사용자 토큰이 필수가 되어 공개 및 앱 토큰 접근 제거 [#23989](https://github.com/mastodon/mastodon/pull/23989)

#### 요청 {#request-6}
##### 헤더 {#headers-6}

Authorization
: 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-4}

tag
: {{<required>}} 문자열. 구독할 해시태그 이름입니다.

#### 이벤트 {#events-7}

로컬 해시태그 타임라인 갱신 예:

```text
event: update
data: {"id":"108914430312582020","created_at":"2022-08-30T23:31:58.006Z","in_reply_to_id":null,"in_reply_to_account_id":null,"sensitive":false,"spoiler_text":"","visibility":"public","language":"en","uri":"https://mastodon.social/users/trwnh/statuses/108914430312582020","url":"https://mastodon.social/@trwnh/108914430312582020","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":null,"content":"<p><a href=\"https://mastodon.social/tags/test\" class=\"mention hashtag\" rel=\"tag\">#<span>test</span></a></p>","reblog":null,"application":{"name":"Web","website":null},"account":{"id":"14715","username":"trwnh","acct":"trwnh","display_name":"infinite love ⴳ","locked":false,"bot":false,"discoverable":true,"group":false,"created_at":"2016-11-24T00:00:00.000Z","note":"<p>i have approximate knowledge of many things. perpetual student. (nb/ace/they)</p><p>xmpp/email: a@trwnh.com<br /><a href=\"https://trwnh.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer\"><span class=\"invisible\">https://</span><span class=\"\">trwnh.com</span><span class=\"invisible\"></span></a><br />help me live: <a href=\"https://liberapay.com/trwnh\" target=\"_blank\" rel=\"nofollow noopener noreferrer\"><span class=\"invisible\">https://</span><span class=\"\">liberapay.com/trwnh</span><span class=\"invisible\"></span></a> or paypal</p><p>- my triggers are moths and glitter<br />- i have all notifs except mentions turned off, so please interact if you wanna be friends! i literally will not notice otherwise<br />- dm me if i did something wrong, so i can improve<br />- purest person on fedi, do not lewd in my presence</p>","url":"https://mastodon.social/@trwnh","avatar":"https://files.mastodon.social/accounts/avatars/000/014/715/original/e430cc93d56f5ac2.png","avatar_static":"https://files.mastodon.social/accounts/avatars/000/014/715/original/e430cc93d56f5ac2.png","header":"https://files.mastodon.social/accounts/headers/000/014/715/original/5c6fc24edb3bb873.jpg","header_static":"https://files.mastodon.social/accounts/headers/000/014/715/original/5c6fc24edb3bb873.jpg","followers_count":2520,"following_count":266,"statuses_count":59817,"last_status_at":"2022-08-30","emojis":[],"fields":[{"name":"Website","value":"<a href=\"https://trwnh.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">trwnh.com</span><span class=\"invisible\"></span></a>","verified_at":"2019-08-29T04:14:55.571+00:00"},{"name":"Portfolio","value":"<a href=\"https://abdullahtarawneh.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">abdullahtarawneh.com</span><span class=\"invisible\"></span></a>","verified_at":"2021-02-11T20:34:13.574+00:00"},{"name":"Fan of:","value":"Punk-rock and post-hardcore (Circa Survive, letlive., La Dispute, THE FEVER 333)Manga (Yu-Gi-Oh!, One Piece, JoJo&#39;s Bizarre Adventure, Death Note, Shaman King)Platformers and RPGs (Banjo-Kazooie, Boktai, Final Fantasy Crystal Chronicles)","verified_at":null},{"name":"What to expect:","value":"talking about various things i find interesting, and otherwise being a genuine and decent wholesome poster. i&#39;m just here to hang out and talk to cool people! and to spill my thoughts.","verified_at":null}]},"media_attachments":[],"mentions":[],"tags":[{"name":"test","url":"https://mastodon.social/tags/test"}],"emojis":[],"card":null,"poll":null}
```

삭제 예:

```text
event: delete
data: 108914430312582020
```

게시물 편집 예:

```text
event: status.update
data: {"id":"108914430312582020","created_at":"2022-08-30T23:32:12.006Z","in_reply_to_id":null,"in_reply_to_account_id":null,"sensitive":false,"spoiler_text":"","visibility":"public","language":"en","uri":"https://mastodon.social/users/trwnh/statuses/108914430312582020","url":"https://mastodon.social/@trwnh/108914430312582020","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":null,"content":"<p><a href=\"https://mastodon.social/tags/test\" class=\"mention hashtag\" rel=\"tag\">#<span>test</span></a> but edited</p>","reblog":null,"application":{"name":"Web","website":null},"account":{"id":"14715","username":"trwnh","acct":"trwnh","display_name":"infinite love ⴳ","locked":false,"bot":false,"discoverable":true,"group":false,"created_at":"2016-11-24T00:00:00.000Z","note":"<p>i have approximate knowledge of many things. perpetual student. (nb/ace/they)</p><p>xmpp/email: a@trwnh.com<br /><a href=\"https://trwnh.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer\"><span class=\"invisible\">https://</span><span class=\"\">trwnh.com</span><span class=\"invisible\"></span></a><br />help me live: <a href=\"https://liberapay.com/trwnh\" target=\"_blank\" rel=\"nofollow noopener noreferrer\"><span class=\"invisible\">https://</span><span class=\"\">liberapay.com/trwnh</span><span class=\"invisible\"></span></a> or paypal</p><p>- my triggers are moths and glitter<br />- i have all notifs except mentions turned off, so please interact if you wanna be friends! i literally will not notice otherwise<br />- dm me if i did something wrong, so i can improve<br />- purest person on fedi, do not lewd in my presence</p>","url":"https://mastodon.social/@trwnh","avatar":"https://files.mastodon.social/accounts/avatars/000/014/715/original/e430cc93d56f5ac2.png","avatar_static":"https://files.mastodon.social/accounts/avatars/000/014/715/original/e430cc93d56f5ac2.png","header":"https://files.mastodon.social/accounts/headers/000/014/715/original/5c6fc24edb3bb873.jpg","header_static":"https://files.mastodon.social/accounts/headers/000/014/715/original/5c6fc24edb3bb873.jpg","followers_count":2520,"following_count":266,"statuses_count":59817,"last_status_at":"2022-08-30","emojis":[],"fields":[{"name":"Website","value":"<a href=\"https://trwnh.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">trwnh.com</span><span class=\"invisible\"></span></a>","verified_at":"2019-08-29T04:14:55.571+00:00"},{"name":"Portfolio","value":"<a href=\"https://abdullahtarawneh.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer me\"><span class=\"invisible\">https://</span><span class=\"\">abdullahtarawneh.com</span><span class=\"invisible\"></span></a>","verified_at":"2021-02-11T20:34:13.574+00:00"},{"name":"Fan of:","value":"Punk-rock and post-hardcore (Circa Survive, letlive., La Dispute, THE FEVER 333)Manga (Yu-Gi-Oh!, One Piece, JoJo&#39;s Bizarre Adventure, Death Note, Shaman King)Platformers and RPGs (Banjo-Kazooie, Boktai, Final Fantasy Crystal Chronicles)","verified_at":null},{"name":"What to expect:","value":"talking about various things i find interesting, and otherwise being a genuine and decent wholesome poster. i&#39;m just here to hang out and talk to cool people! and to spill my thoughts.","verified_at":null}]},"media_attachments":[],"mentions":[],"tags":[{"name":"test","url":"https://mastodon.social/tags/test"}],"emojis":[],"card":null,"poll":null}
```

---

## 리스트 갱신 구독 {#list}

```http
GET /api/v1/streaming/list HTTP/1.1
```

리스트의 게시물을 반환합니다.

**반환:** `update`, `delete`, `status.update`\
**OAuth:** 사용자 토큰 + `read:statuses`\
**버전 이력:**\
2.1.0 - 추가\
3.5.0 - 이제 `status.update` 반환\
4.2.0 - 사용자 토큰이 필수가 되어 공개 및 앱 토큰 접근 제거 [#23989](https://github.com/mastodon/mastodon/pull/23989)

#### 요청 {#request-7}
##### 헤더 {#headers-7}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-5}

list
: {{<required>}} 문자열. 구독할 리스트 ID입니다.

#### 이벤트 {#events-8}

리스트 타임라인 갱신 예:

```text
event: update
data: {"id":"108914327388663283","created_at":"2022-08-30T23:05:46.839Z","in_reply_to_id":"108914298452377720","in_reply_to_account_id":"107946650784398271","sensitive":false,"spoiler_text":"","visibility":"unlisted","language":null,"uri":"https://letsalllovela.in/objects/e9cebb0c-7c75-414f-9608-20b5628e52d7","url":"https://letsalllovela.in/objects/e9cebb0c-7c75-414f-9608-20b5628e52d7","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":null,"favourited":false,"reblogged":false,"muted":false,"bookmarked":false,"content":"<span class=\"h-card\"><a class=\"u-url mention\" href=\"https://pl.nulled.red/users/disarray\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>disarray</span></a></span> glad i was able to help","filtered":[],"reblog":null,"account":{"id":"464472","username":"freon","acct":"freon@letsalllovela.in","display_name":"freon","locked":false,"bot":false,"discoverable":true,"group":false,"created_at":"2018-08-18T00:00:00.000Z","note":"tech archaeologist, unix weenie<br><a class=\"hashtag\" href=\"https://letsalllovela.in/tag/nobot\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#nobot</a>","url":"https://letsalllovela.in/users/freon","avatar":"https://files.mastodon.social/cache/accounts/avatars/000/464/472/original/bfc518d70cf6f13a.png","avatar_static":"https://files.mastodon.social/cache/accounts/avatars/000/464/472/original/bfc518d70cf6f13a.png","header":"https://files.mastodon.social/cache/accounts/headers/000/464/472/original/2e94bd33745f86a6.gif","header_static":"https://files.mastodon.social/cache/accounts/headers/000/464/472/static/2e94bd33745f86a6.png","followers_count":37,"following_count":41,"statuses_count":18442,"last_status_at":"2022-08-30","emojis":[],"fields":[{"name":"pronouns","value":"emacs/xemacs (or he/they)","verified_at":null},{"name":"age","value":"23.66667","verified_at":null}]},"media_attachments":[],"mentions":[{"id":"107946650784398271","username":"disarray","url":"https://pl.nulled.red/users/disarray","acct":"disarray@pl.nulled.red"}],"tags":[],"emojis":[],"card":null,"poll":null}
```

삭제 예:

```text
event: delete
data: 108914398911648589
```

게시물 편집 예:

```text
event: status.update
data: {"id":"108914327388663283","created_at":"2022-08-30T23:05:53.839Z","in_reply_to_id":"108914298452377720","in_reply_to_account_id":"107946650784398271","sensitive":false,"spoiler_text":"","visibility":"unlisted","language":null,"uri":"https://letsalllovela.in/objects/e9cebb0c-7c75-414f-9608-20b5628e52d7","url":"https://letsalllovela.in/objects/e9cebb0c-7c75-414f-9608-20b5628e52d7","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":null,"favourited":false,"reblogged":false,"muted":false,"bookmarked":false,"content":"<span class=\"h-card\"><a class=\"u-url mention\" href=\"https://pl.nulled.red/users/disarray\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>disarray</span></a></span> glad i was able to help","filtered":[],"reblog":null,"account":{"id":"464472","username":"freon","acct":"freon@letsalllovela.in","display_name":"freon","locked":false,"bot":false,"discoverable":true,"group":false,"created_at":"2018-08-18T00:00:00.000Z","note":"tech archaeologist, unix weenie<br><a class=\"hashtag\" href=\"https://letsalllovela.in/tag/nobot\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">#nobot</a>","url":"https://letsalllovela.in/users/freon","avatar":"https://files.mastodon.social/cache/accounts/avatars/000/464/472/original/bfc518d70cf6f13a.png","avatar_static":"https://files.mastodon.social/cache/accounts/avatars/000/464/472/original/bfc518d70cf6f13a.png","header":"https://files.mastodon.social/cache/accounts/headers/000/464/472/original/2e94bd33745f86a6.gif","header_static":"https://files.mastodon.social/cache/accounts/headers/000/464/472/static/2e94bd33745f86a6.png","followers_count":37,"following_count":41,"statuses_count":18442,"last_status_at":"2022-08-30","emojis":[],"fields":[{"name":"pronouns","value":"emacs/xemacs (or he/they)","verified_at":null},{"name":"age","value":"23.66667","verified_at":null}]},"media_attachments":[],"mentions":[{"id":"107946650784398271","username":"disarray","url":"https://pl.nulled.red/users/disarray","acct":"disarray@pl.nulled.red"}],"tags":[],"emojis":[],"card":null,"poll":null}
```

---

## 개인 멘션 구독 {#direct}

```http
GET /api/v1/streaming/direct HTTP/1.1
```

수신한 개인 멘션의 이벤트를 반환합니다.

**반환:** `conversation`\
**OAuth:** 사용자 토큰 + `read:statuses`\
**버전 이력:**\
2.4.0 - 추가\
2.6.0 - `update` 대신 `conversation` 반환

#### 요청 {#request-8}
##### 헤더 {#headers-8}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 이벤트 {#events-9}

#### 이벤트 {#events-10}

대화 갱신 예:

```text
event: conversation
data: {"id":"819516","unread":true,"accounts":[{"id":"108892712797543112","username":"a","acct":"a@pl.nulled.red","display_name":"a","locked":false,"bot":true,"discoverable":false,"group":false,"created_at":"2022-08-27T00:00:00.000Z","note":"a (pleroma edition)","url":"https://pl.nulled.red/users/a","avatar":"https://files.mastodon.social/cache/accounts/avatars/108/892/712/797/543/112/original/975674b2caa61034.png","avatar_static":"https://files.mastodon.social/cache/accounts/avatars/108/892/712/797/543/112/original/975674b2caa61034.png","header":"https://files.mastodon.social/cache/accounts/headers/108/892/712/797/543/112/original/f61d0382356caa0e.png","header_static":"https://files.mastodon.social/cache/accounts/headers/108/892/712/797/543/112/original/f61d0382356caa0e.png","followers_count":0,"following_count":0,"statuses_count":362,"last_status_at":"2022-11-13","emojis":[],"fields":[]}],"last_status":{"id":"109346889330629417","created_at":"2022-11-15T08:31:57.476Z","in_reply_to_id":null,"in_reply_to_account_id":null,"sensitive":false,"spoiler_text":"","visibility":"direct","language":null,"uri":"https://pl.nulled.red/objects/c869c5be-c184-4706-a45d-3459d9aa711c","url":"https://pl.nulled.red/objects/c869c5be-c184-4706-a45d-3459d9aa711c","replies_count":0,"reblogs_count":0,"favourites_count":0,"edited_at":null,"favourited":false,"reblogged":false,"muted":false,"bookmarked":false,"content":"test <span class=\"h-card\"><a class=\"u-url mention\" href=\"https://mastodon.social/@trwnh\" rel=\"nofollow noopener noreferrer\" target=\"_blank\">@<span>trwnh</span></a></span>","filtered":[],"reblog":null,"account":{"id":"108892712797543112","username":"a","acct":"a@pl.nulled.red","display_name":"a","locked":false,"bot":true,"discoverable":false,"group":false,"created_at":"2022-08-27T00:00:00.000Z","note":"a (pleroma edition)","url":"https://pl.nulled.red/users/a","avatar":"https://files.mastodon.social/cache/accounts/avatars/108/892/712/797/543/112/original/975674b2caa61034.png","avatar_static":"https://files.mastodon.social/cache/accounts/avatars/108/892/712/797/543/112/original/975674b2caa61034.png","header":"https://files.mastodon.social/cache/accounts/headers/108/892/712/797/543/112/original/f61d0382356caa0e.png","header_static":"https://files.mastodon.social/cache/accounts/headers/108/892/712/797/543/112/original/f61d0382356caa0e.png","followers_count":0,"following_count":0,"statuses_count":362,"last_status_at":"2022-11-13","emojis":[],"fields":[]},"media_attachments":[],"mentions":[{"id":"14715","username":"trwnh","url":"https://mastodon.social/@trwnh","acct":"trwnh"}],"tags":[],"emojis":[],"card":null,"poll":null}}
```

---

## WebSocket 연결 설정 {#websocket}

```http
wss://mastodon.example/api/v1/streaming
```

**반환:** [이벤트](#events) 스트림\
**OAuth:** 사용자 토큰 + `read`(또는 `read:statuses` 및/또는 `read:notifications`)\
**버전 이력:**\
3.3.0 - 추가\
4.2.0 - 사용자 토큰이 필수가 되어 공개 및 앱 토큰 접근 제거 [#23989](https://github.com/mastodon/mastodon/pull/23989)

이벤트를 받으려면 다중화된 WebSocket 연결을 여세요. WebSocket 명세는 텍스트와 바이너리 데이터 프레임을 모두 허용하지만 작은 텍스트 조각만 처리하므로 스트리밍 서버는 텍스트 프레임만 사용합니다. 필요하면 클라이언트도 이에 맞게 설정해야 합니다.

### 인가 방식 {#authorization}

여기서 설명한 스트리밍 엔드포인트 중 인가가 필요한 것은 `Authorization` HTTP 헤더에 `Bearer <user_token>` 값을 사용하는 방식을 제안합니다. 선호하고 권장하는 방식이며 많은 REST API 엔드포인트의 요구사항과 일치합니다. 대안으로 같은 사용자 토큰을 `Sec-Websocket-Protocol` 헤더 또는 `access_token` 쿼리 매개변수로 보내도 작동합니다.

{{< hint style="warning" >}}
쿼리 매개변수는 접근 로그에 수집되는 경우가 있으므로 새 클라이언트에는 `access_token` 쿼리 매개변수 인가를 권장하지 않습니다. 레거시 지원용입니다.
{{</hint>}}

#### 요청 {#request-9}
##### 헤더 {#headers-9}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 매개변수 {#parameters}

{{< hint style="info" >}}
단일 목적 연결에는 쿼리 매개변수를 권장하지만, WebSocket 연결로 `type` 매개변수가 있는 JSON 인코딩 페이로드를 보내 매개변수를 제공할 수도 있습니다.

해시태그 `#foo`를 포함하는 로컬 게시물 구독 예:

```json
{ "type": "subscribe", "stream": "hashtag:local", "tag": "foo" }
```

사용자 갱신 구독 해제 예:

```json
{ "type": "unsubscribe", "stream": "user" }
```
{{</hint>}}

access_token
: {{%optional%}} 문자열. 사용자가 인가한 OAuth 토큰입니다. 위에서 [설명한](#authorization) `Authorization` 헤더의 레거시 대안으로 제공합니다.

stream
: {{<required>}} 문자열. 단일 스트림의 이벤트를 구독하려는 경우입니다. 가능한 값은 [스트림](#streams)을 참고하세요.
: {{%optional%}} 문자열. 특정 구독 대상 없이 일반 연결을 시작하는 경우입니다.

list
: 문자열. `stream`이 `list`이면 이 매개변수로 리스트 ID를 지정합니다.

tag
: 문자열. `stream`이 `hashtag` 또는 `hashtag:local`이면 이 매개변수로 태그 이름을 지정합니다.

type
: 문자열. 서버로 보내는 JSON 인코딩 페이로드에서 수신할 이벤트를 관리하려면 `subscribe` 또는 `unsubscribe`를 지정합니다.


##### 이벤트 {#events-11}

이벤트는 JSON으로 인코딩됩니다. 유효하지 않은 액세스 토큰을 제공하면 즉시 연결을 닫습니다. 서버에서 제한적 연합 모드 또는 인증된 가져오기 모드를 활성화했다면 이벤트를 받으려면 액세스 토큰을 제공해야 합니다.

공개 타임라인 갱신 예:

```json
{
  "stream": [
    "public"
  ],
  "event": "update",
  "payload": "{\"id\":\"108913983692647032\",\"created_at\":\"2022-08-30T21:38:22.000Z\",\"in_reply_to_id\":\"108913981098896721\",\"in_reply_to_account_id\":\"1081104\",\"sensitive\":false,\"spoiler_text\":\"\",\"visibility\":\"public\",\"language\":\"en\",\"uri\":\"https://fosstodon.org/users/tobtobxx/statuses/108913983628474640\",\"url\":\"https://fosstodon.org/@tobtobxx/108913983628474640\",\"replies_count\":0,\"reblogs_count\":0,\"favourites_count\":0,\"edited_at\":null,\"content\":\"<p>And now I can't exit the inner nvim because I mapped escape to the parent vim instance 😂</p>\",\"reblog\":null,\"account\":{\"id\":\"1081104\",\"username\":\"tobtobxx\",\"acct\":\"tobtobxx@fosstodon.org\",\"display_name\":\"TobTobXX\",\"locked\":false,\"bot\":false,\"discoverable\":true,\"group\":false,\"created_at\":\"2020-01-10T00:00:00.000Z\",\"note\":\"<p>Young tech enthusiast. Likes software (and also general, just not work-) minimalsim. Constantly trying to escape big-tech software.<br>Other hobbies include making music, stargazing, math and recently chess, but there's a lot that piques my interest and a lot left to learn out there.</p><p>„Of course, every house is constructed by someone, but the one who constructed all things is God.“ (Hebrews 3:4 [nwt18])</p>\",\"url\":\"https://fosstodon.org/@tobtobxx\",\"avatar\":\"https://files.mastodon.social/cache/accounts/avatars/001/081/104/original/230a8d0fb54e249b.png\",\"avatar_static\":\"https://files.mastodon.social/cache/accounts/avatars/001/081/104/original/230a8d0fb54e249b.png\",\"header\":\"https://static-cdn.mastodon.social/headers/original/missing.png\",\"header_static\":\"https://static-cdn.mastodon.social/headers/original/missing.png\",\"followers_count\":150,\"following_count\":216,\"statuses_count\":2447,\"last_status_at\":\"2022-08-30\",\"emojis\":[],\"fields\":[{\"name\":\"📍 Lives in:\",\"value\":\"Switzerland (CET: UTC+1 or CEST: UTC+2)\",\"verified_at\":null},{\"name\":\"🔑 GPG  key:\",\"value\":\"EA23 42C5 3EBF 2A2D 985C  416A 12AC 3D47 52E2 FA2E\",\"verified_at\":null}]},\"media_attachments\":[],\"mentions\":[],\"tags\":[],\"emojis\":[],\"card\":null,\"poll\":null}"
}
```

{{< hint style="warning" >}}
이벤트는 JSON으로 인코딩되지만 `payload`는 문자열로 인코딩되고 이스케이프되므로 해당 문자열을 JSON으로 해석하여 로드해야 합니다. 다만 `delete`와 `announcements.delete` 이벤트의 페이로드는 JSON 값이 아니라 식별자를 나타내는 문자열입니다.
{{</hint>}}

공개 타임라인의 삭제 이벤트 예:

```json
{
  "stream": [
    "public"
  ],
  "event": "delete",
  "payload": "106692867363994015"
}
```

사용자의 필터 변경 예:

```json
{
  "stream": [
    "user"
  ],
  "event": "filters_changed"
}
```

{{< hint style="warning" >}}
`filters_changed` 이벤트에는 `payload` 속성이 없습니다. `delete`와 `announcements.delete`의 페이로드는 객체가 아닌 문자열입니다.
{{</hint>}}

## 오류 응답 {#error-responses}

존재하지 않는 스트리밍 엔드포인트에 HTTP 요청을 보내면 스트리밍 서버는 HTTP 400과 오류를 설명하는 JSON 본문으로 응답합니다.

```json
{
  "error": "Unknown channel requested"
}
```

WebSocket 내에서 유효하지 않은 요청(예: 잘못된 스트림 이름)을 하면 서버는 오류 JSON으로 응답합니다.

```json
{
  "error": "Unknown stream type",
  "status":400
}
```

## 함께 보기 {#see-also}

### 스트리밍 서버 {#streaming-server}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/streaming/index.js" caption="streaming/index.js" >}}

### 백엔드 이벤트 발행 {#backend-event-publishing}

스트리밍 타임라인은 Redis에서 유지하며 `redis.publish()`를 통해 Redis에 발행합니다.

#### 게시물 이벤트 {#status-events}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/services/fan_out_on_write_service.rb" caption="app/services/fan_out_on_write_service.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/services/remove_status_service.rb" caption="app/services/remove_status_service.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/services/batched_remove_status_service.rb" caption="app/services/batched_remove_status_service.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/workers/push_conversation_worker.rb" caption="app/workers/push_conversation_worker.rb" >}}

#### 사용자 이벤트 {#user-events}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/feed_manager.rb" caption="app/lib/feed_manager.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/workers/push_update_worker.rb" caption="app/workers/push_update_worker.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/services/notify_service.rb" caption="app/services/notify_service.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/models/custom_filter.rb" caption="app/models/custom_filter.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/workers/publish_scheduled_announcement_worker.rb" caption="app/workers/publish_scheduled_announcement_worker.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/workers/publish_announcement_reaction_worker.rb" caption="app/workers/publish_announcement_reaction_worker.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/workers/unpublish_announcement_worker.rb" caption="app/workers/unpublish_announcement_worker.rb" >}}

### 스트리밍 클라이언트 {#streaming-client}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/javascript/mastodon/stream.js" caption="app/javascript/mastodon/stream.js" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/javascript/mastodon/actions/streaming.js" caption="app/javascript/mastodon/actions/streaming.js" >}}
