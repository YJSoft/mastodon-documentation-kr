---
title: ActivityPub
description: ActivityStreams 2.0 데이터 형식과 JSON-LD를 기반으로 하는 분산 소셜 네트워킹 프로토콜입니다.
menu:
  docs:
    weight: 10
    parent: spec
---

## 게시물 연합 {#status}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/activitypub/activity.rb" caption="app/lib/activitypub/activity.rb" >}}

### 게시물에서 지원하는 활동 {#supported-activities-for-statuses}

Create
: 게시물로 변환하여 데이터베이스에 저장합니다.

Delete
: 데이터베이스에서 게시물을 제거합니다.

Like
: 게시물의 좋아요로 변환합니다.

Announce
: 게시물의 부스트로 변환합니다.

Update
: 투표의 득표수를 갱신합니다. 마스토돈 3.5.0부터는 `updated` 타임스탬프가 있으면 게시물을 수정합니다.

Undo
: 이전 Like 또는 Announce를 취소합니다.

Flag
: 중재팀에 보내는 신고로 변환합니다. 자세한 내용은 [신고](#Flag) 확장을 참고하세요.

QuoteRequest
: 인용 게시물의 승인을 요청합니다. 자세한 내용은 [인용 게시물](#Quote) 확장을 참고하세요.

### 페이로드 {#payloads}

마스토돈이 기본적으로 지원하는 Object 유형은 `Note`와 `Question`입니다.

- Note는 일반 게시물로 변환합니다.
- Question은 투표 게시물로 변환합니다. 자세한 내용은 [투표](#Question) 확장을 참고하세요.

일부 다른 Object 유형도 가능한 범위에서 변환합니다.

- Article
- Page
- Image
- Audio
- Video
- Event

변환기는 게시물 텍스트를 생성할 때 `content`가 있으면 사용하고, 없으면 `name`을 사용합니다. `url`을 덧붙입니다. `summary` 속성은 콘텐츠 경고 텍스트로, `icon`은 썸네일로 사용합니다.

### HTML 정리 {#sanitization}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/lib/sanitize_ext/sanitize_config.rb" caption="lib/sanitize_ext/sanitize_config.rb" >}}

마스토돈은 API 클라이언트 개발자의 전제를 깨뜨리지 않도록 수신한 HTML을 정리합니다. 지원하는 요소는 그대로 유지하고, 지원하지 않는 요소는 변환하거나 제거합니다. 지원하는 속성은 유지하고 다른 모든 속성은 제거합니다. 다음 요소와 속성을 지원합니다.
 
- `<p>`
- `<span>` (`class`)
- `<br>`
- `<a>` (`href`, `rel`, `class`)
- 목록은 `<p>`로 변환하고 목록 항목은 `<br>`로 구분합니다.

마스토돈 v4.2부터 다음 요소와 속성을 지원합니다.

- `<p>`
- `<span>` (`class`)
- `<br>`
- `<a>` (`href`, `rel`, `class`)
- `<del>`
- `<pre>`
- `<code>`
- `<em>`
- `<strong>`
- `<b>`
- `<i>`
- `<u>`
- `<ul>`
- `<ol>` (`start`, `reversed`)
- `<li>` (`value`)
- `<blockquote>`
- 제목은 `<strong>`으로 변환한 뒤 `<p>`로 감쌉니다.
 
정리 과정에서 마이크로포맷 접두사로 시작하거나 의미를 나타내는 클래스는 유지합니다.

- h-*
- p-*
- u-*
- dt-*
- e-*
- mention
- hashtag
- ellipsis
- invisible

지원하는 프로토콜을 사용하는 링크는 유지하고, 그렇지 않으면 텍스트로 변환합니다. 다음 링크 프로토콜을 지원합니다.

- http
- https
- dat
- dweb
- ipfs
- ipns
- ssb
- gopher
- xmpp
- magnet
- gemini

### 사용하는 속성 {#properties-used}

content
: 게시물 텍스트로 사용합니다.

name
: 변환한 Object 유형에 `content`가 없으면 게시물 텍스트로 사용합니다.

summary
: 콘텐츠 경고 텍스트로 사용합니다.

sensitive
: 게시물 미디어나 텍스트를 기본적으로 숨길지 결정하는 데 사용합니다. `as:sensitive`에 관한 자세한 내용은 [민감한 콘텐츠](#sensitive) 확장 절을 참고하세요.

inReplyTo
: 게시물을 다른 게시물에 대한 답글로 글타래에 연결하는 데 사용합니다.

published
: 게시물 날짜로 사용합니다.

url
: 게시물 고유 링크로 사용하며, 변환한 Object의 게시물 텍스트에도 덧붙입니다.

attributedTo
: 게시물 작성 프로필을 결정하는 데 사용합니다.

to/cc
: 멘션과 함께 게시물의 공개 대상과 공개 범위를 결정하는 데 사용합니다. [주소 지정 및 알림용 멘션](#Mention)을 참고하세요.

tag
: 멘션과 해시태그를 마크업하는 데 사용합니다.

tag[].type
: 현재 `Mention`, `Hashtag`, `Emoji`를 지원합니다. 자세한 내용은 [해시태그](#Hashtag)와 [사용자 지정 이모지](#Emoji) 확장 절을 참고하세요.

tag[].name
: 프로필 Mention의 일반 텍스트 WebFinger 주소(`@user` 또는 `@user@domain`), 일반 텍스트 Hashtag(`#tag`), 사용자 지정 Emoji 단축 코드(`:thounking:`)입니다.

tag[].href
: 행위자 또는 태그의 URL입니다.

attachment
: 첨부 이미지, 동영상, 오디오를 포함하는 데 사용합니다.

attachment[].url
: 미디어 첨부 파일을 가져오는 데 사용합니다.

attachment[].summary
: 미디어 설명으로 사용합니다.

attachment[].blurhash
: 이미지의 색상에 맞는 흐린 미리보기 이미지를 생성하는 데 사용합니다. 자세한 내용은 [Blurhash](#blurhash)를 참고하세요.

replies
: 현재 게시물의 답글인 게시물 Collection입니다. 원격 게시물을 발견할 때 글타래를 더 완전하게 확인하기 위해 같은 서버의 답글을 최대 5개 가져옵니다. 마스토돈에서는 첫 페이지에 자기 답글을 포함하고, 이후 페이지에는 다른 사람의 답글을 포함합니다.

likes
: 이 게시물이 받은 `Like` 활동을 나타내는 Collection입니다. 현재 마스토돈은 실제 활동을 공개하지 않습니다.

likes.totalItems
: 이 게시물이 받은 좋아요 수입니다.

shares
: 이 게시물이 받은 `Announce` 활동을 나타내는 Collection입니다. 현재 마스토돈은 실제 활동을 공개하지 않습니다.

shares.totalItems
: 이 게시물이 받은 `Announce` 활동 수입니다.

#### 투표 전용 속성 {#poll-specific-properties}

endTime
: 투표가 종료될 시각의 타임스탬프입니다.

closed
: 투표가 종료된 시각의 타임스탬프입니다. `endTime` 타임스탬프와 같을 가능성이 높습니다. 이 속성이 있으면 투표가 종료된 것으로 간주합니다.

votersCount
: 투표에 참여한 사람 수입니다. 복수 선택 투표에서는 제출된 표 수와 다릅니다.

oneOf
: 단일 선택 투표의 선택지입니다.

anyOf
: 복수 선택 투표의 선택지입니다.

oneOf/anyOf[].name
: 투표 선택지의 텍스트입니다.

oneOf/anyOf[].replies.totalItems
: 투표 선택지의 득표수입니다.

## 프로필 연합 {#profile}

### 프로필에서 지원하는 활동 {#supported-activities-for-profiles}

Follow
: 프로필의 게시물 갱신을 받고 싶다는 의사를 나타냅니다.

Accept/Reject
: Follow 활동을 승인하거나 거절하는 데 사용합니다. 잠기지 않은 계정은 자동으로 Accept로 응답하며, 잠긴 계정은 팔로우 요청을 승인할지 거절할지 수동으로 선택할 수 있습니다.

Add/Remove
: 고정 게시물과 추천 컬렉션을 관리합니다.

Update
: 계정 세부 정보를 갱신합니다.

Delete
: 데이터베이스에서 계정과 해당 계정의 모든 게시물을 제거합니다.

Undo
: 이전 Follow, Accept Follow 또는 Block을 취소합니다.

Block
: 원격 서버에 해당 사용자에게 내 프로필을 숨기도록 신호를 보냅니다. 보장되지는 않습니다. 자세한 내용은 [원격 차단](#Block)을 참고하세요.

Flag
: 해당 중재팀에 사용자를 신고합니다. 자세한 내용은 [신고](#Flag) 확장을 참고하세요.

Move
: 한 계정의 팔로워를 다른 계정으로 이전합니다. 새 계정에 이전 계정을 가리키는 `alsoKnownAs`가 설정되어 있어야 합니다.

### 사용하는 속성 {#properties-used-1}

preferredUsername
: WebFinger 조회에 사용합니다. 도메인 내에서 고유해야 하며 WebFinger `acct:` URI에 대응해야 합니다.

name
: 프로필 표시 이름으로 사용합니다.

summary
: 프로필 소개로 사용합니다.

type
: Person으로 간주합니다. 유형이 Application 또는 Service이면 봇 플래그로 해석합니다.

url
: 프로필 링크로 사용합니다.

icon
: 프로필 아바타로 사용합니다.

image
: 프로필 헤더로 사용합니다.

manuallyApprovesFollowers
: 잠긴 계정으로 표시합니다.

discoverable
: 프로필 디렉터리에 표시합니다. [발견 가능 플래그](#discoverable)를 참고하세요.

indexable
: 이 계정의 게시물을 전문 검색용으로 색인할 수 있습니다. [색인 가능 플래그](#indexable)를 참고하세요.

publicKey
: 서명에 필요합니다. [공개 키](#publicKey)를 참고하세요.

featured
: 고정 게시물입니다. [추천 컬렉션](#featured)을 참고하세요.

attachment
: 프로필 필드에 사용합니다. [프로필 메타데이터](#PropertyValue)와 [신원 증명](#IdentityProof)을 참고하세요.

alsoKnownAs
: Move 활동에 필요합니다.

published
: 프로필 생성 시각입니다.

memorial
: 계정이 추모 계정인지 나타냅니다.

suspended
: 계정이 현재 정지되었는지 나타냅니다.

attributionDomains
: 게시된 기사에서 이 행위자를 위한 `fediverse:creator`를 사용할 수 있는 도메인입니다.

showFeatured
: 이 계정 프로필에 “소개” 탭을 표시할지 나타냅니다.

showMedia
: 이 계정 프로필에 “미디어” 탭을 표시할지 나타냅니다.

showRepliesInMedia
: 이 계정 프로필의 “미디어” 탭에 답글을 포함할지 나타냅니다.

## JSON-LD 컨텍스트와 확장 {#contexts}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/activitypub/adapter.rb" caption="app/lib/activitypub/adapter.rb" >}}

### 마스토돈 확장 (`toot:`) {#toot}

기본 URI: `http://joinmastodon.org/ns#`

마스토돈 기능에서 사용하는 용어를 포함합니다.

- toot:Emoji (`http://joinmastodon.org/ns#Emoji`)
- toot:IdentityProof (`http://joinmastodon.org/ns#IdentityProof`)
- toot:attributionDomains (`http://joinmastodon.org/ns#attributionDomains`)
- toot:blurhash (`http://joinmastodon.org/ns#blurhash`)
- toot:discoverable (`http://joinmastodon.org/ns#discoverable`)
- toot:featured (`http://joinmastodon.org/ns#featured`)
- toot:featuredTags (`http://joinmastodon.org/ns#featuredTags`)
- toot:focalPoint (`http://joinmastodon.org/ns#focalPoint`)
- toot:indexable (`http://joinmastodon.org/ns#indexable`)
- toot:memorial (`http://joinmastodon.org/ns#memorial`)
- toot:suspended (`http://joinmastodon.org/ns#suspended`)
- toot:votersCount (`http://joinmastodon.org/ns#votersCount`)

### ActivityStreams 확장 (`as:`) {#as}

기본 URI: `https://www.w3.org/ns/activitystreams#`

제안되었지만 아직 공식 채택되지 않은 ActivityStreams 확장 속성을 포함합니다. 현재는 [ActivityPub 기타 용어](https://swicg.github.io/miscellany/) 문서에 기술되어 있습니다.

- as:Hashtag (`https://www.w3.org/ns/activitystreams#Hashtag`)
- as:manuallyApprovesFollowers (`https://www.w3.org/ns/activitystreams#manuallyApprovesFollowers`)
- as:movedTo (`https://www.w3.org/ns/activitystreams#movedTo`)
- as:sensitive (`https://www.w3.org/ns/activitystreams#sensitive`)

### Schema.org 확장 (`schema:`) {#schema}

프로필 메타데이터에 사용하는 속성을 포함합니다.

기본 URI: `http://schema.org#` (잘못된 값이며 `https://schema.org/`여야 합니다)

- [schema:PropertyValue (`http://schema.org#PropertyValue`, 올바른 값은 `https://schema.org/PropertyValue`)](https://schema.org/PropertyValue)
- [schema:value (`http://schema.org#value`, 올바른 값은 `https://schema.org/value`)](https://schema.org/value)

### W3ID 보안 어휘 (`sec:`) {#sec}

컨텍스트: [`https://w3id.org/security/v1`](https://w3id.org/security/v1)

HTTPS 서명에 사용합니다. 신원 증명에도 사용합니다. 자세한 내용은 [보안]({{< relref "spec/security" >}})을 참고하세요.

- [sec:publicKey (`https://w3id.org/security#publicKey`)](https://w3id.org/security#publicKey)
- [sec:publicKeyPem (`https://w3id.org/security#publicKeyPem`)](https://w3id.org/security#publicKeyPem)
- [sec:owner (`https://w3id.org/security#owner`)](https://w3id.org/security#owner)
- [sec:signature (`https://w3id.org/security#signature`)](https://w3id.org/security#signature)
- [sec:signatureValue (`https://w3id.org/security#signatureValue`)](https://w3id.org/security#signatureValue)

#### W3ID 신원 {#w3id-identity}

컨텍스트: [`https://w3id.org/identity/v1`](https://w3id.org/identity/v1) (오프라인)

연결 데이터 서명에 사용합니다. 자세한 내용은 [보안 > 연결 데이터 서명]({{< relref "spec/security#ld" >}})을 참고하세요.

- [dc:creator (`http://purl.org/dc/terms/creator`)](http://purl.org/dc/terms/creator)
- [dc:created (`http://purl.org/dc/terms/created`)](http://purl.org/dc/terms/created)
- [sec:signature (`https://w3id.org/security#signature`)](https://w3id.org/security#signature)
- [sec:signatureValue (`https://w3id.org/security#signatureValue`)](https://w3id.org/security#signatureValue)

## ActivityStreams 어휘를 사용하여 정의한 확장 {#extensions-defined-using-activitystreams-vocabulary}

Activity Vocabulary는 다양한 유형과 용어를 정의하지만 ActivityPub은 그중 일부에 대해서만 부수 효과를 정의합니다. 다음 활동 유형을 마스토돈 수신함에서 받으면 아래의 부수 효과가 발생합니다.

### 원격 차단 (`Block`) {#Block}

ActivityPub은 클라이언트-서버(C2S) 용도로 `Block` 활동을 정의하지만 서버-서버(S2S) 용도로는 정의하지 않으며, 서버가 Block 활동을 `object`에 전달하지 않는 것이 좋다고 권고합니다(SHOULD NOT). 하지만 마스토돈은 로컬 사용자가 원격 사용자를 차단할 때 이 활동을 보냅니다. 마스토돈이 로컬 도메인의 행위자를 `object`로 하는 `Block` 활동을 받으면, 해당 로컬 사용자에게 그 행위자의 프로필과 게시물을 숨기고 그 로컬 사용자의 해당 행위자 멘션도 금지하라는 신호로 해석합니다.

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://mastodon.example/bd06bb61-01e0-447a-9dc8-95915db9aec8",
  "type": "Block",
  "actor": "https://mastodon.example/users/alice",
  "object": "https://example.com/~mallory",
  "to": "https://example.com/~mallory"
}
```

### 프로필과 게시물 신고 (`Flag`) {#Flag}

원격 서버의 프로필 및/또는 게시물을 신고하려면 마스토돈이 서버 행위자로부터 `Flag` 활동을 보냅니다. 이 활동의 `object`에는 신고 대상 사용자와 신고에 첨부된 게시물이 포함됩니다. 신고에 의견을 첨부했다면 활동의 `content`로 사용합니다.

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://mastodon.example/ccb4f39a-506a-490e-9a8c-71831c7713a4",
  "type": "Flag",
  "actor": "https://mastodon.example/actor",
  "content": "Please take a look at this user and their posts",
  "object": [
    "https://example.com/users/1",
    "https://example.com/posts/380590",
    "https://example.com/posts/380591"
  ],
  "to": "https://example.com/users/1"
}
```

### 계정 이전 (`Move`) {#Move}

마스토돈은 계정이 다른 계정으로 이전했음을 알리기 위해 Move 활동을 사용합니다. 이전이 유효한 것으로 간주되려면 새 계정이 `alsoKnownAs` 속성을 통해 이전 계정을 가리키는 별칭을 정의했는지 확인합니다.

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://mastodon.example/users/alice#moves/1",
  "actor": "https://mastodon.example/users/alice",
  "type": "Move",
  "object": "https://mastodon.example/users/alice",
  "target": "https://alice.com/users/109835986274379",
  "to": "https://mastodon.example/users/alice/followers"
}
```

### 투표 {#Question}

{{< caption-link url="https://www.w3.org/TR/activitystreams-vocabulary/#questions" caption="Activity Vocabulary §5.4 - 질문 표현" >}}

ActivityStreams Vocabulary 사양은 질문을 표현하는 방법을 느슨하게(비규범적으로) 설명합니다. 마스토돈의 투표 구현은 이 절에서 어느 정도 영감을 받았습니다. 다음 구현 세부 사항을 확인할 수 있습니다.

- `Question`은 `IntransitiveActivity` 대신 `Object` 유형으로 사용합니다. 직접 보내는 대신 다른 게시물과 마찬가지로 `Create`로 감쌉니다.
- 투표 선택지는 `oneOf` 또는 `anyOf`를 사용하여 배열로 직렬화합니다.
  - 배열의 각 항목에는 `id`가 없고, `type`은 `Note`이며, `name`은 투표 선택지의 텍스트입니다.
  - 배열의 각 항목에는 해당 선택지의 응답을 나타내는 `replies` 속성도 있습니다. 이 노드에는 `id`가 없고, `type`은 `Collection`이며, 선택지의 총 득표수를 나타내는 `totalItems` 속성이 있습니다.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    {
      "votersCount": "http://joinmastodon.org/ns#votersCount"
    }
  ],
  "id": "https://mastodon.example/users/alice/statuses/1009947848598745",
  "type": "Question",
  "content": "What should I eat for breakfast today?",
  "published": "2023-03-05T07:40:13Z",
  "endTime": "2023-03-06T07:40:13Z",
  "votersCount": 7,
  "anyOf": [
    {
      "type": "Note",
      "name": "apple",
      "replies": {
        "type": "Collection",
        "totalItems": 3
      }
    },
    {
      "type": "Note",
      "name": "orange",
      "replies": {
        "type": "Collection",
        "totalItems": 7
      }
    },
    {
      "type": "Note",
      "name": "banana",
      "replies": {
        "type": "Collection",
        "totalItems": 6
      }
    }
  ]
}
```

- 투표는 `Create` 활동으로 직렬화하며, `object`는 `name`이 투표 선택지의 `name`과 정확히 일치하는 `Note`입니다. `Note.inReplyTo`는 `Question` 객체의 URI를 가리킵니다.
  - 복수 선택 투표에서는 여러 활동을 보낼 수 있습니다. 이전에 해당 선택지에 투표하지 않았다면 표가 집계됩니다.

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://mastodon.example/users/bob#votes/827163/activity",
  "to": "https://mastodon.example/users/alice",
  "actor": "https://mastodon.example/users/bob",
  "type": "Create",
  "object": {
    "id": "https://mastodon.example/users/bob#votes/827163",
    "type": "Note",
    "name": "orange",
    "attributedTo": "https://mastodon.example/users/bob",
    "to": "https://mastodon.example/users/alice",
    "inReplyTo": "https://mastodon.example/users/alice/statuses/1009947848598745"
  }
}
```
```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://mastodon.example/users/bob#votes/827164/activity",
  "to": "https://mastodon.example/users/alice",
  "actor": "https://mastodon.example/users/bob",
  "type": "Create",
  "object": {
    "id": "https://mastodon.example/users/bob#votes/827164",
    "type": "Note",
    "name": "banana",
    "attributedTo": "https://mastodon.example/users/bob",
    "to": "https://mastodon.example/users/alice",
    "inReplyTo": "https://mastodon.example/users/alice/statuses/1009947848598745"
  }
}
```

### 주소 지정 및 알림용 멘션 {#Mention}

{{< caption-link url="https://www.w3.org/TR/activitystreams-vocabulary/#microsyntaxes" caption="Activity Vocabulary §5.6 - 멘션, 태그 및 기타 일반적인 소셜 마이크로구문" >}}

ActivityStreams Vocabulary에서 `Mention`은 @멘션 마이크로구문을 표현하기 위한 `Link`의 하위 유형입니다. `tag` 속성은 다른 Object나 Link에 대한 참조를 추가하기 위한 것입니다. Link 태그에서 Link의 `name`은 해당 객체의 자연어 속성(`name`, `summary`, `content`)의 부분 문자열이어야 합니다. 이 부분 문자열을 찾은 곳에서 `href`를 참조하는 하이퍼링크로 변환할 수 있습니다.

하지만 마스토돈은 일부 경우 `Mention` 태그를 주소 지정에도 사용합니다. Mention 태그의 포함 여부를 `to`와 `cc`에 명시된 대상과 비교하여 게시물 공개 범위를 계산합니다. 또한 마스토돈에서 알림을 생성하려면 Mention 태그가 필요합니다(멘션된 행위자가 게시물을 받으려면 여전히 `to` 또는 `cc`에 명시적으로 포함되어야 합니다).

- `public`: 공개 게시물은 `to`에 `as:Public` 특수 컬렉션을 포함합니다.
- `unlisted`: 조용한 공개 게시물은 `cc`에 `as:Public` 특수 컬렉션을 포함합니다.
- `private`: 팔로워 전용 게시물은 `to` 또는 `cc`에 행위자의 팔로워 컬렉션을 포함하지만 `as:Public` 특수 컬렉션은 포함하지 않습니다.
- `limited`: 제한된 대상에게 공개하는 게시물은 `to` 또는 `cc`에 행위자를 포함하며, 그중 적어도 하나는 `tag`에서 `Mention`되지 않습니다.
- `direct`: 멘션 전용 게시물은 `to` 또는 `cc`에 행위자를 포함하며, 모두 `tag`에서 `Mention`됩니다.

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/activitypub/activity/create.rb" caption="app/lib/activitypub/activity/create.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/activitypub/parser/status_parser.rb" caption="app/lib/activitypub/parser/status_parser.rb" >}}

## ActivityStreams가 정의하지 않은 확장 {#extensions-not-defined-by-activitystreams}

다음 기능은 ActivityStreams에서 정의하지 않은 속성과 유형을 사용하여 정의합니다.

### 공개 키 {#publicKey}

공개 키는 HTTP 서명과 연결 데이터 서명에 사용합니다. 행위자 객체의 추가 속성 `publicKey`로 구현합니다. 자세한 내용은 [보안]({{< relref "spec/security" >}})을 참고하세요.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1"
  ],
  "id": "https://mastodon.social/users/Gargron",
  "type": "Person",
  "publicKey": {
    "id": "https://mastodon.social/users/Gargron#main-key",
    "owner": "https://mastodon.social/users/Gargron",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvXc4vkECU2/CeuSo1wtn\nFoim94Ne1jBMYxTZ9wm2YTdJq1oiZKif06I2fOqDzY/4q/S9uccrE9Bkajv1dnkO\nVm31QjWlhVpSKynVxEWjVBO5Ienue8gND0xvHIuXf87o61poqjEoepvsQFElA5ym\novljWGSA/jpj7ozygUZhCXtaS2W5AD5tnBQUpcO0lhItYPYTjnmzcc4y2NbJV8hz\n2s2G8qKv8fyimE23gY1XrPJg+cRF+g4PqFXujjlJ7MihD9oqtLGxbu7o1cifTn3x\nBfIdPythWu5b4cujNsB3m3awJjVmx+MHQ9SugkSIYXV0Ina77cTNS0M2PYiH1PFR\nTwIDAQAB\n-----END PUBLIC KEY-----\n"
  }
}
```

### 추천 컬렉션 {#featured}

마스토돈에서 “고정 게시물”로 알려진, 프로필 상단에 항상 표시하는 게시물은 객체의 `Collection`을 가리키는 행위자 객체의 추가 속성 `featured`로 구현합니다.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    {
      "featured": {
        "@id": "http://joinmastodon.org/ns#featured",
        "@type": "@id"
      }
    }
  ],

  "id": "https://example.com/@alice",
  "type": "Person",
  "featured": "https://example.com/@alice/collections/featured"
}
```

### 추천 태그 {#featuredTags}

마스토돈은 발견 기능으로 사용자가 프로필에 특정 해시태그를 소개하여 쉽게 찾아볼 수 있게 합니다. `Hashtag` 객체의 `Collection`을 가리키는 행위자 객체의 추가 속성 `featuredTags`로 구현합니다.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    {
      "featuredTags": {
        "@id": "http://joinmastodon.org/ns#featuredTags",
        "@type": "@id"
      }
    }
  ],

  "id": "https://example.com/@alice",
  "type": "Person",
  "featuredTags": "https://example.com/@alice/collections/tags"
}
```

### 프로필 메타데이터 {#PropertyValue}

마스토돈은 이름-값 쌍을 담은 임의의 프로필 필드를 지원합니다. 행위자 객체의 `attachment` 속성을 사용하여 구현하며, 배열의 객체는 schema.org 네임스페이스의 `PropertyValue` 유형과 `value` 속성을 가집니다.

{{<hint style="warning">}}
위의 [schema.org @context 확장](#schema) 목록에서 설명했듯이, 마스토돈은 현재 잘못된 기본 URI인 `http://schema.org#`를 예상하고 `schema` 용어를 여기에 매핑하며 올바른 `https://schema.org/`를 사용하지 않습니다. 따라서 올바른 컨텍스트 정의를 사용하는 JSON-LD 처리기는 프로필 필드를 올바르게 처리하지 못합니다.
{{</hint>}}

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    {
      "schema": "http://schema.org#",
      "PropertyValue": "schema:PropertyValue",
      "value": "schema:value"
    }
  ],
  "id": "https://mastodon.social/users/Gargron",
  "type": "Person",
  "attachment": [
    {
      "type": "PropertyValue",
      "name": "Patreon",
      "value": "<a href=\"https://www.patreon.com/mastodon\" rel=\"me nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://www.</span><span class=\"\">patreon.com/mastodon</span><span class=\"invisible\"></span></a>"
    },
    {
      "type": "PropertyValue",
      "name": "Homepage",
      "value": "<a href=\"https://zeonfederated.com\" rel=\"me nofollow noopener noreferrer\" target=\"_blank\"><span class=\"invisible\">https://</span><span class=\"\">zeonfederated.com</span><span class=\"invisible\"></span></a>"
    }
  ]
}
```

### 신원 증명 {{%deprecated%}} {#IdentityProof}

{{< hint style="warning" >}}
마스토돈 3.5에서 Keybase 지원이 제거되어 현재 이 속성은 사용하지 않으며 폐기 예정입니다: <https://github.com/mastodon/mastodon/pull/17045>
{{</hint>}}

마스토돈은 프로필이 특정 신원에 연결되어 있음을 증명하기 위한 신원 제공자 연동을 지원합니다. 행위자 객체의 `attachment` 속성으로 구현하며 배열의 객체는 마스토돈 네임스페이스의 `IdentityProof` 유형입니다. 이 객체에는 W3ID 보안 어휘 네임스페이스의 `signatureAlgorithm`과 `signatureValue`도 포함됩니다.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {
      "IdentityProof": "http://joinmastodon.org/ns#IdentityProof"
    }
  ],
  "id": "https://mastodon.social/users/Gargron",
  "type": "Person",
  "attachment": [
    {
      "type": "IdentityProof",
      "name": "gargron",
      "signatureAlgorithm": "keybase",
      "signatureValue": "5cfc20c7018f2beefb42a68836da59a792e55daa4d118498c9b1898de7e845690f"
    }
  ]
}
```

### 발견 가능 플래그 {#discoverable}

마스토돈에서는 사용자가 프로필 디렉터리 같은 발견 기능에 참여하거나 참여하지 않을 수 있습니다. 이 플래그는 외부 발견 서비스에 포함되는 것에 대한 사용자 선호도 나타낼 수 있습니다. 이러한 도구를 구현한다면 속성이 있을 때 이를 존중하는 것이 좋습니다. 프로필에 매핑되는 객체의 추가 속성 `discoverable`로 구현합니다.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    {
      "discoverable": "http://joinmastodon.org/ns#discoverable"
    }
  ],
  "id": "https://mastodon.social/users/Gargron",
  "type": "Person",
  "discoverable": true
}
```

### 색인 가능 플래그 {#indexable}

마스토돈에서는 사용자가 공개 게시물 전문 검색 같은 색인 기능에 참여하거나 참여하지 않을 수 있습니다. 이러한 도구를 구현한다면 속성이 있을 때 이를 존중하는 것이 좋습니다. 프로필에 매핑되는 객체의 추가 속성 `indexable`로 구현합니다.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    {
      "indexable": "http://joinmastodon.org/ns#indexable"
    }
  ],
  "id": "https://mastodon.social/users/Gargron",
  "type": "Person",
  "indexable": true
}
```

### 정지 플래그 {#suspended}

마스토돈은 계정을 더 잘 처리할 수 있도록 사용자가 로컬에서 정지되었는지 알립니다. 마스토돈의 정지된 계정은 빈 데이터를 반환합니다. 원격 계정이 정지된 것으로 표시되면 로컬에서 정지를 해제할 수 없습니다. 정지된 계정은 Update, Undo, Reject, Delete 같은 활동의 대상이 될 수 있습니다. 객체의 추가 속성 `suspended`로 구현합니다.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    {
      "suspended": "http://joinmastodon.org/ns#suspended"
    }
  ],
  "id": "https://example.com/@eve",
  "type": "Person",
  "suspended": true
}
```

### 추모 플래그 {#memorial}

마스토돈은 계정을 더 잘 처리할 수 있도록 사용자 프로필이 추모 계정으로 지정되었는지 알립니다. 추모 계정은 일반 데이터를 반환하지만 추모 계정임을 나타내는 헤더와 함께 표시됩니다. 객체의 추가 속성 `memorial`로 구현합니다.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    {
      "memorial": "http://joinmastodon.org/ns#memorial"
    }
  ],
  "id": "https://example.com/@alice",
  "type": "Person",
  "memorial": true
}
```

### 해시태그 {#Hashtag}

ActivityStreams에 이미 정의된 Link 하위 유형 `Mention`과 비슷하게, 마스토돈은 문자열 키로 식별되는 공통 주제를 참조하는 게시물을 표시하기 위해 Link의 하위 유형으로 `Hashtag`를 사용합니다. Hashtag의 `name`에는 #해시태그 마이크로구문, 즉 `#` 뒤에 주제를 나타내는 문자열이 포함됩니다. 이는 `@` 뒤에 리소스를 나타내는 문자열이 오는 @멘션 마이크로구문과 비슷합니다(마스토돈에서는 해당 리소스가 계정일 것으로 예상합니다). 또한 마스토돈은 ASCII 변환을 수행하고 잘못된 문자를 제거하여 해시태그를 대소문자를 구분하지 않는 소문자 문자열로 정규화합니다.

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/hashtag_normalizer.rb" caption="app/lib/hashtag_normalizer.rb" >}}

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    {
      "Hashtag": "https://www.w3.org/ns/activitystreams#Hashtag"
    }
  ],
  "id": "https://example.com/some-post",
  "type": "Note",
  "attributedTo": "https://example.com",
  "content": "I love #cats",
  "tag": [
    {
      "type": "Hashtag",
      "name": "#cats",
      "href": "https://example.com/tagged/cats"
    }
  ]
}
```

### 사용자 지정 이모지 {#Emoji}

마스토돈은 `Emoji` 유형의 `tag`를 포함하여 임의의 이모지를 지원합니다. 사용자 지정 이모지 처리는 멘션 및 해시태그 처리와 비슷하며, 태그된 엔터티의 `name`을 자연어 속성(`name`, `summary`, `content`)의 부분 문자열로 찾은 뒤 특정 리소스나 주제의 로컬 표현에 연결합니다. 이모지 단축 코드의 경우 `name`을 `icon` 속성이 나타내는 인라인 이미지 HTML로 바꿉니다(`icon.url`은 이미지 리소스에 연결됩니다).

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    {
      "Emoji": "http://joinmastodon.org/ns#Emoji",
    }
  ],

  "id": "https://example.com/@alice/hello-world",
  "type": "Note",
  "content": "Hello world :kappa:",
  "tag": [
    {
      "id": "https://example.com/emoji/123",
      "type": "Emoji",
      "name": ":kappa:",
      "icon": {
        "type": "Image",
        "mediaType": "image/png",
        "url": "https://example.com/files/kappa.png"
      }
    }
  ]
}
```

### 초점 {#focalPoint}

마스토돈은 업로드한 이미지에 초점을 설정하여 이미지가 어디에 표시되든 초점이 보이게 할 수 있습니다. `Image` 객체의 추가 속성 `focalPoint`로 구현합니다. 이 속성은 -1.0과 1.0 사이의 부동소수점 수 두 개로 된 배열이며, 0,0은 이미지 중앙입니다. 첫 값은 x(-1.0은 왼쪽 끝, +1.0은 오른쪽 끝), 두 번째 값은 y(-1.0은 아래쪽 끝, +1.0은 위쪽 끝)입니다. 자세한 내용은 [API 지침 > 초점]({{< relref "api/guidelines#focal-points" >}})을 참고하세요.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    {
      "focalPoint": {
        "@container": "@list",
        "@id": "http://joinmastodon.org/ns#focalPoint"
      }
    }
  ],

  "id": "https://example.com/@alice/hello-world",
  "type": "Note",
  "content": "A picture attached!",
  "attachment": [
    {
      "type": "Image",
      "mediaType": "image/png",
      "url": "https://example.com/files/cats.png",
      "focalPoint": [
        -0.55,
        0.43
      ]
    }
  ]
}
```

{{< figure src="/assets/focal-points.jpg" caption="다양한 초점과 해당 좌표의 예시입니다." >}}

위 예시의 초점 (-0.55, 0.43)은 중앙에서 왼쪽으로 55%, 위쪽으로 43%인 지점에 해당합니다. 이미지를 잘라 썸네일을 만들더라도 이 초점은 보여야 합니다.

### Blurhash {#blurhash}

마스토돈은 첨부 파일용으로 색상이 있는 미리보기 썸네일을 생성합니다. `Image` 객체의 추가 속성 `blurhash`로 구현합니다. 이 속성은 [BlurHash 알고리즘](https://blurha.sh)으로 생성한 문자열입니다.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    {
      "blurhash": "http://joinmastodon.org/ns#blurhash"
    }
  ],

  "id": "https://example.com/@alice/hello-world",
  "type": "Note",
  "content": "A picture attached!",
  "attachment": [
    {
      "type": "Image",
      "mediaType": "image/png",
      "url": "https://example.com/files/cats.png",
      "blurhash": "UBL_:rOpGG-oBUNG,qRj2so|=eE1w^n4S5NH"
    }
  ]
}
```

### 민감한 콘텐츠 {#sensitive}

마스토돈은 `as:sensitive` 확장 속성으로 특정 게시물을 민감함으로 표시합니다. 민감함으로 표시된 게시물에 첨부한 미디어는 기본적으로 숨기며, `summary`가 있으면 게시물 `content`를 이 요약 뒤에 접어 둡니다. 마스토돈에서는 이를 **콘텐츠 경고**라고 합니다.

### 인용 게시물과 인용 제어 {#Quote}

마스토돈은 [FEP-044f](https://codeberg.org/fediverse/fep/src/branch/main/fep/044f/fep-044f.md)에 따라 원격 인용 게시물 처리를 지원합니다. 호환성을 위해 `quoteUri`, `quoteUrl`, `_misskey_quote`도 이해합니다.

게시물에 인용이 여러 개 있으면 마스토돈은 첫 번째 인용만 허용합니다.

또한 마스토돈은 모든 상호작용 정책을 처리하는 대신 허용된 팔로워를 “공개”, “팔로워”, “팔로잉”, “아무도 없음”의 조합으로 변환하며, 기본값은 “아무도 없음”입니다.

v4.5부터 마스토돈은 같은 사양에 따른 인용 작성과 인용 승인을 제공합니다.

## 기타 기능 {#other-functionality}

### 보안 모드 {#secure-mode}

마스토돈 서버가 보안 모드로 실행될 때는 서버 간의 모든 HTTP 요청에 서명이 필요합니다(즉, 공개 리소스에 대한 `GET` 요청도 포함). 이를 통해 마스토돈 서버는 차단한 서버의 요청을 거절하고 공개 정보의 “유출”을 피할 수 있습니다. 마스토돈 자체는 전용 시스템 행위자로 이러한 HTTP 요청에 서명합니다. HTTP 서명의 자세한 내용은 [보안]({{< relref "spec/security" >}})을 참고하세요.

보안 모드는 “제한된 연합 모드”의 기반입니다. 제한된 연합 모드의 마스토돈 서버는 관리자가 명시적으로 허용한 서버와만 연합하며 다른 모든 요청을 거절합니다.

### 팔로워 동기화 메커니즘 {#follower-synchronization-mechanism}

마스토돈에는 “팔로워 전용” 게시물이라는 개념이 있지만 현재 팔로워 컬렉션의 확장은 출발지가 아닌 목적지에서 처리합니다(즉, 명시적인 주소 지정으로 처리하지 않습니다). 따라서 동기화 문제를 감지하고 수정할 메커니즘이 필요합니다. 이 메커니즘은 전체 컬렉션(공개 정보가 아닐 수 있음)이 아닌 부분 팔로워 컬렉션에서 작동해야 합니다. 특정 서버의 팔로워만 포함한다는 점에서 부분 컬렉션이지만, 해당 팔로워는 모두 포함해야 합니다(MUST). 컬렉션에서 팔로워가 누락되면 해당 팔로우 관계가 단절됩니다.

원격 사용자에게 메시지를 전달할 때 `Signature` 헤더와 같은 구문으로 다음 속성을 갖는 선택적 `Collection-Synchronization` HTTP 헤더를 첨부합니다.

- `collectionId` = 발신자의 `followers` 컬렉션이어야 합니다(MUST).
- `url` = 수신자 서버에 있는 발신자의 모든 팔로워 식별자를 포함한 부분 컬렉션의 URL입니다. 행위자 자체와 같은 도메인에 있어야 하며(MUST), 수신자 서버의 서명된 조회로만 접근할 수 있는 것이 좋습니다(SHOULD).
- `digest` = 부분 컬렉션의 각 식별자 SHA256 다이제스트를 XOR한 값의 16진수 표현입니다.

#### 다이제스트 계산 {#digest-calculation}

다이제스트는 다음과 같이 계산합니다.

1. 각 팔로워 식별자(UTF-8 인코딩 문자열)의 SHA256 해시를 계산합니다.
2. 생성된 모든 다이제스트 바이트를 서로 XOR합니다.
3. 최종 결과를 16진수 표현으로 변환합니다.

팔로워가 여러 명이면 각 SHA256 다이제스트를 다른 다이제스트와 XOR합니다. 예를 들어 팔로워 A와 B의 경우 `digest = SHA256(A) XOR SHA256(B)`입니다.

예시:

```http
POST https://mastodon.social/users/foo/inbox HTTP/1.1
Collection-Synchronization:
  collectionId="https://social.sitedethib.com/users/Thib/followers",
  url="https://social.sitedethib.com/users/Thib/followers_synchronization",
  digest="b08ab6951c7d6cc2b91e17ebd9557da7fae02489728e9332fcb3a97748244d50"
```

원격 사용자가 부분 컬렉션 `url`을 GET하려 할 때 이 요청에는 HTTP 서명이 필요합니다. 예시:

```http
GET https://social.sitedethib.com/users/Thib/followers_synchronization HTTP/1.1
Signature: ... # a signature from an account on mastodon.social

{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://social.sitedethib.com/users/Thib/followers?domain=mastodon.social",
  "type": "OrderedCollection",
  "orderedItems": [
    "https://mastodon.social/users/Gargron"
  ]
}
```
