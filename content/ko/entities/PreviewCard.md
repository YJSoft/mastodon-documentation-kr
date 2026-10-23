---
title: 미리보기 카드 (PreviewCard)
description: URL의 OpenGraph 태그로 생성한 풍부한 미리보기 카드를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/card",
  "/entities/Card",
  "/entities/previewcard",
  "/entities/PreviewCard",
  "/api/entities/card",
  "/api/entities/Card",
  "/api/entities/previewcard",
  "/api/entities/PreviewCard",
]
---

## 예시 {#examples}

### 동영상 {#video}

```json
{
  "url": "https://www.youtube.com/watch?v=OMv_EPMED8Y",
  "title": "♪ Brand New Friend (Christmas Song!)",
  "description": "",
  "type": "video",
  "author_name": "YOGSCAST Lewis & Simon",
  "author_url": "https://www.youtube.com/user/BlueXephos",
  "provider_name": "YouTube",
  "provider_url": "https://www.youtube.com/",
  "html": "<iframe width=\"480\" height=\"270\" src=\"https://www.youtube.com/embed/OMv_EPMED8Y?feature=oembed\" frameborder=\"0\" allowfullscreen=\"\"></iframe>",
  "width": 480,
  "height": 270,
  "image": "https://files.mastodon.social/preview_cards/images/014/179/145/original/9cf4b7cf5567b569.jpeg",
  "embed_url": "",
  "blurhash": "UvK0HNkV,:s9xBR%njog0fo2W=WBS5ozofV@"
}
```

### 사진 {#photo}

```json
{
  "url": "https://www.flickr.com/photos/tomfenskephotography/49088768431/",
  "title": "Oregon",
  "description": "",
  "type": "photo",
  "author_name": "Tom Fenske Photography",
  "author_url": "https://www.flickr.com/photos/tomfenskephotography/",
  "provider_name": "Flickr",
  "provider_url": "https://www.flickr.com/",
  "html": "",
  "width": 1024,
  "height": 427,
  "image": "https://files.mastodon.social/preview_cards/images/014/287/139/original/651b1c6976817824.jpeg",
  "embed_url": "https://live.staticflickr.com/65535/49088768431_6a4322b3bb_b.jpg",
  "blurhash": "UnE{@jt6M_oIAhjYs+ayT2WBf9ayRkkDXAj["
}
```

### 링크 {#link}

```json
{
  "url": "https://www.theguardian.com/money/2019/dec/07/i-lost-my-193000-inheritance-with-one-wrong-digit-on-my-sort-code",
  "title": "‘I lost my £193,000 inheritance – with one wrong digit on my sort code’",
  "description": "When Peter Teich’s money went to another Barclays customer, the bank offered £25 as a token gesture",
  "type": "link",
  "authors": [],
  "author_name": "",
  "author_url": "",
  "provider_name": "",
  "provider_url": "",
  "html": "",
  "width": 0,
  "height": 0,
  "image": null,
  "embed_url": "",
  "blurhash": null,
  "published_at": "1661472000"
}
```

## 속성 {#attributes}

### `url` {#url}

**설명:** 링크된 리소스의 위치입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
1.0.0 - 추가

### `title` {#title}

**설명:** 링크된 리소스의 제목입니다.\
**유형:** 문자열\
**버전 이력:**\
1.0.0 - 추가

### `description` {#description}

**설명:** 미리보기 설명입니다.\
**유형:** 문자열\
**버전 이력:**\
1.0.0 - 추가

### `type` {#type}

**설명:** 미리보기 카드 유형입니다.\
**유형:** 문자열 (열거형, 다음 중 하나)\
`link` = 링크 OEmbed\
`photo` = 사진 OEmbed\
`video` = 동영상 OEmbed\
`rich` = iframe OEmbed. 현재 허용하지 않으므로 실제로 표시되지 않습니다.\
**버전 이력:**\
1.3.0 - 추가

### `authors` {#authors}

**설명:** 원본 리소스 작성자들의 연합우주 계정입니다.\
**유형:** 배열: [PreviewCardAuthor]({{< relref "entities/PreviewCardAuthor">}})\
**버전 이력:**\
4.3.0 - 추가

### `author_name` {#author_name}

**설명:** 원본 리소스의 작성자입니다. 4.3.0부터 폐기 예정이므로 클라이언트는 대신 `authors`를 사용해야 합니다.\
**유형:** 문자열\
**버전 이력:**\
1.3.0 - 추가\
4.3.0 - 폐기 예정

### `author_url` {#author_url}

**설명:** 원본 리소스 작성자 링크입니다. 4.3.0부터 폐기 예정이므로 클라이언트는 대신 `authors`를 사용해야 합니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
1.3.0 - 추가\
4.3.0 - 폐기 예정

### `provider_name` {#provider_name}

**설명:** 원본 리소스 제공자입니다.\
**유형:** 문자열\
**버전 이력:**\
1.3.0 - 추가

### `provider_url` {#provider_url}

**설명:** 원본 리소스 제공자 링크입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
1.3.0 - 추가

### `html` {#html}

**설명:** 미리보기 카드를 생성할 때 사용할 HTML입니다.\
**유형:** 문자열 (HTML)\
**버전 이력:**\
1.3.0 - 추가

### `width` {#height}

**설명:** 미리보기 너비(픽셀)입니다.\
**유형:** 정수\
**버전 이력:**\
1.3.0 - 추가

### `height` {#height}

**설명:** 미리보기 높이(픽셀)입니다.\
**유형:** 정수\
**버전 이력:**\
1.3.0 - 추가

### `image` {#image}

**설명:** 미리보기 썸네일입니다.\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
1.0.0 - 추가

### `embed_url` {#embed_url}

**설명:** 사진 임베드에 사용자 지정 `html` 대신 사용합니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
2.1.0 - 추가

### `blurhash` {#blurhash}

**설명:** 미디어를 아직 다운로드하지 않았을 때 색상이 있는 미리보기 썸네일을 생성하기 위해 [BlurHash 알고리즘](https://github.com/woltapp/blurhash)으로 계산한 해시입니다.\
**유형:** {{<nullable>}} 문자열\
**버전 이력:**\
3.2.0 - 추가

### `missing_attribution` {#missing_attribution}

**설명:** 링크된 기사가 현재 사용자가 작성했다고 주장하지만 사용자의 [`attribution_domains`]({{< relref "entities/Account#source-attribution_domains" >}}))에 해당 기사 도메인이 없으면 true입니다. 사용자에게 도메인을 검토하고 추가하도록 안내하는 데 사용합니다.\
**유형:** {{<nullable>}} 불리언\
**버전 이력:**\
4.6.0 - 추가

#### `published_at` {#published-at}

**설명:** 게시 날짜의 UNIX 타임스탬프입니다.\
**유형:** {{<nullable>}} 문자열 (UNIX 타임스탬프)

## Trends::Link 엔터티 속성 {#trends-link}
사용 이력이 추가된 것을 제외하면 `Link` 유형의 `PreviewCard`와 같습니다.

```json
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
}
```

### `history` {#history}

**설명:** 주어진 날짜들(보통 지난 일주일)의 사용 통계입니다.\
**유형:** 배열: 해시\
**버전 이력:**\
3.5.0 - 추가

#### `history[][day]` {#history-day}

**설명:** 해당 날짜 자정의 UNIX 타임스탬프입니다.\
**유형:** 문자열 (UNIX 타임스탬프)\
**버전 이력:**\
3.5.0 - 추가

#### `history[][accounts]` {#history-accounts}

**설명:** 해당 날짜에 링크를 사용한 계정 수입니다.\
**유형:** 문자열 (정수에서 변환)\
**버전 이력:**\
3.5.0 - 추가

#### `history[][uses]` {#history-uses}

**설명:** 해당 날짜에 링크를 사용한 게시물 수입니다.\
**유형:** 문자열 (정수에서 변환)\
**버전 이력:**\
3.5.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="entities/Status#card" caption="Status (`card` 속성)" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/preview_card_serializer.rb" caption="app/serializers/rest/preview_card_serializer.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/trends/link_serializer.rb" caption="app/serializers/rest/trends/link_serializer.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/models/trends/links.rb" caption="app/models/trends/links.rb" >}}
