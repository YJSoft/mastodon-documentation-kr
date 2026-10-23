---
title: 미디어 첨부 파일 (MediaAttachment)
description: 게시물에 추가할 수 있는 파일 또는 미디어 첨부 파일을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/attachment",
  "/entities/Attachment",
  "/entities/mediaattachment",
  "/entities/MediaAttachment",
  "/api/entities/attachment",
  "/api/entities/Attachment",
  "/api/entities/mediaattachment",
  "/api/entities/MediaAttachment",
]
---

## 예시 {#example}

### 이미지 {#image}

```json
{
  "id": "22345792",
  "type": "image",
  "url": "https://files.mastodon.social/media_attachments/files/022/345/792/original/57859aede991da25.jpeg",
  "preview_url": "https://files.mastodon.social/media_attachments/files/022/345/792/small/57859aede991da25.jpeg",
  "remote_url": null,
  "text_url": "https://mastodon.social/media/2N4uvkuUtPVrkZGysms",
  "meta": {
    "original": {
      "width": 640,
      "height": 480,
      "size": "640x480",
      "aspect": 1.3333333333333333
    },
    "small": {
      "width": 461,
      "height": 346,
      "size": "461x346",
      "aspect": 1.3323699421965318
    },
    "focus": {
      "x": -0.27,
      "y": 0.51
    }
  },
  "description": "test media description",
  "blurhash": "UFBWY:8_0Jxv4mx]t8t64.%M-:IUWGWAt6M}"
}
```

### 동영상 {#video}

```json
{
  "id": "22546306",
  "type": "video",
  "url": "https://files.mastodon.social/media_attachments/files/022/546/306/original/dab9a597f68b9745.mp4",
  "preview_url": "https://files.mastodon.social/media_attachments/files/022/546/306/small/dab9a597f68b9745.png",
  "remote_url": null,
  "text_url": "https://mastodon.social/media/wWd1HJIBmH1MZGDfg50",
  "meta": {
    "length": "0:01:28.65",
    "duration": 88.65,
    "fps": 24,
    "size": "1280x720",
    "width": 1280,
    "height": 720,
    "aspect": 1.7777777777777777,
    "audio_encode": "aac (LC) (mp4a / 0x6134706D)",
    "audio_bitrate": "44100 Hz",
    "audio_channels": "stereo",
    "original": {
      "width": 1280,
      "height": 720,
      "frame_rate": "6159375/249269",
      "duration": 88.654,
      "bitrate": 862056
    },
    "small": {
      "width": 400,
      "height": 225,
      "size": "400x225",
      "aspect": 1.7777777777777777
    }
  },
  "description": null,
  "blurhash": "U58E0g8_0M.94T?bIr00?bD%NGoM?bD%oLt7"
}
```

### GIFV {#gifv}

```json
{
  "id": "21130559",
  "type": "gifv",
  "url": "https://files.mastodon.social/media_attachments/files/021/130/559/original/bc84838f77991326.mp4",
  "preview_url": "https://files.mastodon.social/media_attachments/files/021/130/559/small/bc84838f77991326.png",
  "remote_url": null,
  "text_url": "https://mastodon.social/media/2ICiasGyjezmi7cQYM8",
  "meta": {
    "length": "0:00:01.11",
    "duration": 1.11,
    "fps": 33,
    "size": "600x332",
    "width": 600,
    "height": 332,
    "aspect": 1.8072289156626506,
    "original": {
      "width": 600,
      "height": 332,
      "frame_rate": "100/3",
      "duration": 1.11,
      "bitrate": 1627639
    },
    "small": {
      "width": 400,
      "height": 221,
      "size": "400x221",
      "aspect": 1.8099547511312217
    }
  },
  "description": null,
  "blurhash": "URHT%Jm,2a1d%MRO%LozkrNH$*n*oMn$Rjt7"
}
```

### 오디오 {#audio}

```json
{
  "id": "21165404",
  "type": "audio",
  "url": "https://files.mastodon.social/media_attachments/files/021/165/404/original/a31a4a46cd713cd2.mp3",
  "preview_url": "https://files.mastodon.social/media_attachments/files/021/165/404/small/a31a4a46cd713cd2.mp3",
  "remote_url": null,
  "text_url": "https://mastodon.social/media/5O4uILClVqBWx0NNgvo",
  "meta": {
    "length": "0:06:42.86",
    "duration": 402.86,
    "audio_encode": "mp3",
    "audio_bitrate": "44100 Hz",
    "audio_channels": "stereo",
    "original": {
      "duration": 402.860408,
      "bitrate": 166290
    }
  },
  "description": null,
  "blurhash": null
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 첨부 파일 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
0.6.0 - 추가

### `type` {#type}

**설명:** 첨부 파일 유형입니다.\
**유형:** 문자열 (열거형, 다음 중 하나)\
`unknown` = 지원하지 않거나 인식할 수 없는 파일 유형\
`image` = 정적 이미지\
`gifv` = 반복 재생되는 무음 애니메이션\
`video` = 동영상 클립\
`audio` = 오디오 트랙\
**버전 이력:**\
0.6.0 - 추가\
2.9.1 - `audio` 추가

### `url` {#url}

**설명:** 원본 전체 크기 첨부 파일의 위치입니다. 파일을 처리 중이면 URL이 null일 수 있습니다. [`POST /api/v2/media`]({{< relref "methods/media" >}}#v2)를 참고하세요.\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
0.6.0 - 추가

### `preview_url` {#preview_url}

**설명:** 축소한 첨부 파일 미리보기의 위치입니다.\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
0.6.0 - 추가

### `remote_url` {#remote_url}

**설명:** 원격 웹사이트에 있는 전체 크기 원본 첨부 파일의 위치입니다.\
**유형:** {{<nullable>}} 문자열 (URL), 로컬 첨부 파일이면 null\
**버전 이력:**\
0.6.0 - 추가

### `meta` {#meta}

**설명:** Paperclip이 반환한 메타데이터입니다.\
**유형:** {{<nullable>}} 해시 또는 null\
**버전 이력:**\
1.5.0 - 추가

`small` 및 `original` 하위 트리와 여러 다른 최상위 속성을 포함할 수 있습니다.

### `meta[focus]` {{%optional%}} {#meta-focus}

**설명:** 스마트 썸네일 자르기에 사용할 수 있는 좌표입니다. 자세한 내용은 [잘린 미디어 썸네일의 초점]({{< relref "api/guidelines#focal-points" >}})을 참고하세요.\
**유형:** {{<nullable>}} 해시 또는 null\
**버전 이력:**\
2.3.0 - `meta.focus` 추가

### `meta[focus][x]` {#meta-focus-x}

**설명:** 가로 초점\
**유형:** {{<nullable>}} 실수 또는 null

### `meta[focus][y]` {#meta-focus-y}

**설명:** 세로 초점\
**유형:** {{<nullable>}} 실수 또는 null

### `description` {#description}

**설명:** 시각 장애가 있거나 미디어 첨부 파일이 로드되지 않을 때 사용할, 미디어 첨부 파일 내용을 설명하는 대체 텍스트입니다.\
**유형:** {{<nullable>}} 문자열, 미디어 첨부 파일의 대체 텍스트가 제공되지 않았으면 null\
**버전 이력:**\
2.0.0 - 추가

### `blurhash` {#blurhash}

**설명:** 미디어를 아직 다운로드하지 않았을 때 색상이 있는 미리보기 썸네일을 생성하기 위해 [BlurHash 알고리즘](https://github.com/woltapp/blurhash)으로 계산한 해시입니다.\
**유형:** {{<nullable>}} 문자열 (Blurhash)\
**버전 이력:**\
2.8.1 - 추가

### `text_url` {{%removed%}} {#text_url}

**설명:** 첨부 파일의 짧은 URL입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
0.6.0 - 추가\
3.5.0 - 제거

## 함께 보기 {#see-also}

{{< page-relref ref="entities/Status#media_attachments" caption="Status (`media_attachments` 속성)" >}}

{{< page-relref ref="methods/media" caption="media API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/media_attachment_serializer.rb" caption="app/serializers/rest/media_attachment_serializer.rb" >}}
