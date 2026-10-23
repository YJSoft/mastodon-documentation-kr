---
title: 미리보기 카드 작성자 (PreviewCardAuthor)
description: 풍부한 미리보기 카드의 작성자를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/PreviewCardAuthor",
]
---

## 속성 {#attributes}

### `name` {#name}

**설명:** 원본 리소스 작성자의 이름입니다. 미리보기 카드의 폐기 예정 속성 `author_name`을 대체합니다.\
**유형:** 문자열\
**버전 이력:**\
4.3.0 - 추가

### `url` {#url}

**설명:** 원본 리소스 작성자 링크입니다. 미리보기 카드의 폐기 예정 속성 `author_url`을 대체합니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
4.3.0 - 추가

### `account` {{%nullable%}} {#account}

**설명:** 작성자의 연합우주 계정입니다.\
**유형:** [Account]({{< relref "entities/Account">}})\
**버전 이력:**\
4.3.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="entities/PreviewCard#authors" caption="PreviewCard (`authors` 속성)" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/preview_card_serializer.rb" caption="app/serializers/rest/preview_card_serializer.rb" >}}
