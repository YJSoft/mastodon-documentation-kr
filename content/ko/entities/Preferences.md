---
title: 환경 설정 (Preferences)
description: 사용자의 환경 설정을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/preferences",
  "/entities/Preferences",
  "/api/entities/preferences",
  "/api/entities/Preferences",
]
---

## 예시 {#example}

```json
{
  "posting:default:visibility": "public",
  "posting:default:sensitive": false,
  "posting:default:language": null,
  "reading:expand:media": "default",
  "reading:expand:spoilers": false
}
```

## 속성 {#attributes}

### `posting:default:visibility` {#posting-default-visibility}

**설명:** 새 게시물의 기본 공개 범위입니다. [CredentialAccount#source\[privacy\]]({{< relref "entities/Account#source-privacy" >}})와 같습니다.\
**유형:** 문자열 (열거형, 다음 중 하나)\
`public` = 공개 게시물\
`unlisted` = 조용한 공개 게시물\
`private` = 팔로워 전용 게시물\
`direct` = 개인 멘션 게시물\
**버전 이력:**\
2.8.0 - 추가

### `posting:default:sensitive` {#posting-default-sensitive}

**설명:** 새 게시물의 기본 민감함 플래그입니다. [CredentialAccount#source\[sensitive\]]({{< relref "entities/Account#source-sensitive" >}})와 같습니다.\
**유형:** 불리언\
**버전 이력:**\
2.8.0 - 추가

### `posting:default:language` {#posting-default-language}

**설명:** 새 게시물의 기본 언어입니다. [CredentialAccount#source\[language\]]({{< relref "entities/Account#source-language" >}})와 같습니다.\
**유형:** {{<nullable>}} 문자열 (ISO 639-1 두 글자 언어 코드), 또는 null\
**버전 이력:**\
2.8.0 - 추가

### `posting:default:spoiler_field` {#posting-default-spoiler-field}

**설명:** 새 게시물에 콘텐츠 경고를 추가할지에 대한 기본값입니다. [CredentialAccount#source\[spoiler_field\]]({{< relref "entities/Account#source-spoiler-field" >}})와 같습니다.\
**유형:** 불리언\
**버전 이력:**\
5.0.0 - 추가

### `reading:expand:media` {#reading-expand-media}

**설명:** 미디어 첨부 파일을 자동으로 표시할지, 흐리게 하거나 숨길지 나타냅니다.\
**유형:** 문자열 (열거형, 다음 중 하나)\
`default` = 민감함으로 표시된 미디어를 숨깁니다.\
`show_all` = 민감함 여부와 관계없이 기본적으로 모든 미디어를 항상 표시합니다.\
`hide_all` = 민감함 여부와 관계없이 기본적으로 모든 미디어를 항상 숨깁니다.\
**버전 이력:**\
2.8.0 - 추가

### `reading:expand:spoilers` {#reading-expand-spoilers}

**설명:** 콘텐츠 경고를 기본적으로 펼칠지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.8.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/preferences" caption="preferences API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/preferences_serializer.rb" caption="app/serializers/rest/preferences_serializer.rb" >}}



