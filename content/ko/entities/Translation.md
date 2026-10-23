---
title: 번역 (Translation)
description: 게시물 콘텐츠를 기계 번역한 결과를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/api/entities/Translation",
  "/api/entities/translation",
]
---

## 예시 {#examples}

콘텐츠 경고와 미디어가 있는 게시물의 번역

```json
{
  "content": "<p>Hello world</p>",
  "spoiler_text": "Greatings ahead",
  "language": "en",
  "media_attachments": [
    {
      "id": "22345792",
      "description": "Status author waving at the camera"
    }
  ],
  "poll": null,
  "detected_source_language": "es",
  "provider": "DeepL.com"
}
```

투표가 있는 게시물의 번역:
```json
{
  "content": "<p>Should I stay or should I go?</p>",
  "spoiler_text": "",
  "language": "en",
  "media_attachments": [],
  "poll": {
    "id": "34858",
    "options": [
      {
        "title": "Stay"
      },
      {
        "title": "Go"
      }
    ]
  },
  "detected_source_language": "ja",
  "provider": "DeepL.com"
}
```


## 속성 {#attributes}

### `content` {#content}

**설명:** HTML로 인코딩된 게시물 콘텐츠의 번역입니다.\
**유형:** 문자열 (HTML)\
**버전 이력:**\
4.0.0 - 추가

### `spoiler_text` {#spoiler_text}

**설명:** 게시물의 스포일러 경고 번역입니다.\
**유형:** 문자열\
**버전 이력:**\
4.2.0 - 추가

### `language` {#language}

**설명:** 텍스트가 번역된 결과 언어입니다.\
**유형:** 문자열\
**버전 이력:**\
4.0.0 - 추가

### `poll` {{%optional%}} {#poll}

**설명:** 게시물 투표의 번역입니다.\
**유형:** [Translation::Poll](#Poll)\
**버전 이력:**\
4.2.0 - 추가

### `media_attachments` {#media_attachments}

**설명:** 게시물 미디어 설명의 번역입니다.\
**유형:** 배열: [Translation::Attachment](#Attachment)\
**버전 이력:**\
4.2.0 - 추가

### `detected_source_language` {#detected_source_language}

**설명:** 기계 번역 제공자가 자동으로 감지한 원문 언어입니다.\
**유형:** 문자열 (ISO 639-1 언어 코드)\
**버전 이력:**\
4.0.0 - 추가

### `provider` {#provider}

**설명:** 기계 번역을 제공한 서비스입니다.\
**유형:** 문자열\
**버전 이력:**\
4.0.0 - 추가

## Translation::Poll 속성 {#Poll}

### `id` {#Poll-id}

**설명:** 투표 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.2.0 - 추가

### `options` {#Poll-options}

**설명:** 번역된 투표 선택지입니다.\
**유형:** 배열: [Translation::Poll::Option](#Option)\
**버전 이력:**\
4.2.0 - 추가

## Translation::Poll::Option 속성 {#Option}

### `title` {#Option-title}

**설명:** 번역된 투표 선택지 제목입니다.\
**유형:** 문자열\
**버전 이력:**\
4.2.0 - 추가

## Translation::Attachment 속성 {#Attachment}

### `id` {#Attachment-id}

**설명:** 첨부 파일 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.2.0 - 추가

### `description` {#Attachment-description}

**설명:** 번역된 첨부 파일 설명입니다.\
**유형:** 문자열\
**버전 이력:**\
4.2.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/statuses#translate" caption="POST /api/v1/statuses/:id/translate" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/translation_serializer.rb" caption="app/serializers/rest/translation_serializer.rb" >}}
