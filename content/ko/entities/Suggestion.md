---
title: 추천 (Suggestion)
description: 팔로우 추천 계정과 추천 사유를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/suggestion",
  "/entities/Suggestion",
  "/api/entities/suggestion",
  "/api/entities/Suggestion",
]
---

## 예시 {#example}

```json
{
  "source": "staff",
  "account": {
    "id": "109031732217496096",
    "username": "alice",
    "acct": "alice",
    // ...
  }
}
```

## 속성 {#attributes}

### `source` {#source}

**설명:** 이 계정이 추천되는 사유입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`staff` = 관리팀이 이 계정을 수동으로 추천했습니다.\
`past_interactions` = 인증된 계정이 이전에 이 계정과 상호작용했습니다.\
`global` = 지난 30일 동안 이 계정에 많은 부스트, 좋아요, 활동 중인 로컬 팔로워가 있습니다.\
**버전 이력:**\
3.4.0 - 추가\
4.3.0 - 폐기 예정. 대신 `sources` 사용

### `sources` {#sources}

**설명:** 이 계정이 추천되는 사유 목록입니다. `source`를 대체합니다.\
**유형:** 배열: 문자열 (열거형 다음 중 하나)\
`featured` = 관리팀이 이 계정을 수동으로 추천했습니다. `source`의 `staff` 값과 같습니다.\
`most_followed` = 이 계정에 활동 중인 로컬 팔로워가 많습니다.\
`most_interactions` = 지난 30일 동안 이 계정이 많은 부스트와 좋아요를 받았습니다.\
`similar_to_recently_followed` = 이 계정의 프로필이 인증된 계정이 가장 최근에 팔로우한 계정들과 비슷합니다.\
`friends_of_friends` = 인증된 계정이 팔로우하는 사람들이 이 계정을 팔로우합니다.\
**버전 이력:**\
4.3.0 - 추가

### `account` {#account}

**설명:** 팔로우를 추천하는 계정입니다.\
**유형:** [Account]({{< relref "entities/Account" >}})\
**버전 이력:**\
3.4.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/suggestions#v2" caption="GET /api/v2/suggestions" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/suggestion_serializer.rb" caption="app/serializers/rest/suggestion_serializer.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/models/account_suggestions.rb" caption="app/models/account_suggestions.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/models/account_suggestions/" caption="app/models/account_suggestions/" >}}
