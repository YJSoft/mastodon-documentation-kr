---
title: 신고 API 메서드
description: 문제 있는 사용자를 중재자에게 신고합니다.
menu:
  docs:
    name: 신고
    parent: methods-accounts
    identifier: methods-reports
aliases: [
  "/methods/reports",
  "/api/methods/reports",
  "/methods/accounts/reports",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 신고 제출 {#post}

```http
POST /api/v1/reports HTTP/1.1
```

문제 있는 계정과 콘텐츠를 중재자에게 신고합니다.

**반환:** [Report]({{< relref "entities/report" >}})\
**OAuth:** 사용자 토큰 + `write:reports`\
**버전 이력:**\
1.1 - 추가\
2.3.0 - `forward` 매개변수 추가\
3.5.0 - `category` 및 `rule_ids` 매개변수 추가\
4.0.0 - `rule_ids`를 제공하면 `category`는 선택 사항\
4.2.0 - `legal` 분류 추가\
4.6.0 - `collection_ids` 매개변수 추가

#### 요청 {#request}
##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

account_id
: {{<required>}} 문자열. 신고할 계정 ID입니다.

status_ids[]
: 문자열 배열. 추가 맥락을 제공하도록 신고에 게시물을 첨부할 수 있습니다.

collection_ids[]
: 문자열 배열. 추가 맥락을 제공하도록 신고에 컬렉션을 첨부할 수 있습니다.

comment
: 문자열. 신고 사유입니다. 기본 최대 길이는 1000자입니다.

forward
: 불리언. 원격 계정인 경우 원격 관리자에게 신고를 전달할지 여부입니다. 기본값은 false입니다.

category
: 문자열. 신고 사유가 `spam`, `legal`(불법 콘텐츠), 명시된 서버 규칙의 `violation`, `other` 중 무엇인지 지정합니다. 기본값은 `other`입니다. `rule_ids[]`를 제공하면 지정한 분류 값에 관계없이 `violation`으로 설정됩니다.

rule_ids[]
: 문자열 배열. `violation` 분류 신고에는 위반한 규칙의 정확한 ID를 지정합니다. 규칙과 ID는 [GET /api/v1/instance/rules]({{< relref "methods/instance#rules" >}})와 [GET /api/v1/instance]({{< relref "methods/instance#v1" >}})에서 확인할 수 있습니다. 자세한 내용은 [ID 처리 및 정렬]({{< relref "api/guidelines/#id" >}})을 참고하세요.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

게시물 ID 하나와 설명, `spam` 분류를 제공한 호출 예입니다.

```json
{
  "id": "48914",
  "action_taken": false,
  "action_taken_at": null,
  "category": "spam",
  "comment": "Spam account",
  "forwarded": false,
  "created_at": "2022-08-25T09:56:16.763Z",
  "status_ids": [
    "108882889550545820"
  ],
  "rule_ids": null,
  "target_account": {
    "id": "108366849347798387",
    "username": "Baluke",
    "acct": "Baluke",
    "display_name": "Baluke Dental Studios",
    "locked": false,
    "bot": false,
    "discoverable": false,
    "group": false,
    "created_at": "2022-05-26T00:00:00.000Z",
    "note": "<p>Baluke Dental Studios is a full service dental lab offering fabrication, staining, and digital services. Advanced technologies and a meticulous process ensure reduced chair time, lower costs, and better patient outcomes with beautiful smiles. Talk to a representative today.</p><p><a href=\"https://baluke.com/\" target=\"_blank\" rel=\"nofollow noopener noreferrer\"><span class=\"invisible\">https://</span><span class=\"\">baluke.com/</span><span class=\"invisible\"></span></a></p>",
    "url": "https://mastodon.social/@Baluke",
    "avatar": "https://files.mastodon.social/accounts/avatars/108/366/849/347/798/387/original/dbcfe99ed5def0f4.png",
    "avatar_static": "https://files.mastodon.social/accounts/avatars/108/366/849/347/798/387/original/dbcfe99ed5def0f4.png",
    "header": "https://static-cdn.mastodon.social/headers/original/missing.png",
    "header_static": "https://static-cdn.mastodon.social/headers/original/missing.png",
    "followers_count": 0,
    "following_count": 0,
    "statuses_count": 38,
    "last_status_at": "2022-08-25",
    "emojis": [],
    "fields": []
  }
}
```

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found}

신고가 제출되지 않았습니다.

```json
{
  "error": "Record not found"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

토큰에 인증된 사용자가 없습니다.

```json
{
  "error": "This method requires an authenticated user"
}
```

또는 `category`를 `violation`으로 설정했지만 `rule_ids`가 없거나 유효하지 않습니다.

```json
{
  "error": "Validation failed: Rule ids does not reference valid rules"
}
```

또는 (마스토돈 3.5에서) `category`를 `violation` 이외의 값으로 설정했지만 `rule_ids`를 제공했습니다.

```json
{
  "error": "Validation failed: Rule ids must be blank"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/reports_controller.rb" caption="app/controllers/api/v1/reports_controller.rb" >}}
