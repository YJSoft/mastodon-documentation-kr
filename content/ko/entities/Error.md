---
title: 오류 (Error)
description: 오류 메시지를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/error",
	"/entities/Error",
  "/api/entities/error",
	"/api/entities/Error",
]
---

## 예시 {#example}

```json
{
  "error": "invalid_grant",
  "error_description": "The provided authorization grant is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client."
}
```

{{< hint style="info" >}}
**오류 응답에서 가장 중요한 부분은 HTTP 상태 코드입니다.** 표준 의미를 따릅니다. 오류 본문은 사용 가능한 추가 정보를 포함하는 JSON 객체입니다.
{{< /hint >}}

## 속성 {#attributes}

### `error` {#error}

**설명:** 오류 메시지입니다.\
**유형:** 문자열\
**버전 이력:**\
0.6.0 - 추가

### `error_description` {{%optional%}} {#error_description}

**설명:** 오류의 자세한 설명으로, 주로 OAuth API에서 제공합니다.\
**유형:** 문자열\
**버전 이력:**\
0.6.0 - 추가

## 가능한 원인 {#reasons}

### 400 - 잘못된 요청 {#400---bad-request}

#### ParameterMissing {#parameter-missing}

오류: {문자열}. API 호출에 필수 매개변수가 없을 때 나타납니다.

### 401 - 인증되지 않음 {#401}

#### require_authenticated_user! {#auth}

오류: 이 API는 인증된 사용자가 필요합니다. 서버가 API 메서드의 모든 공개 사용을 막는 보안 모드일 때 나타납니다.

### 403 - 금지됨 {#403}

#### NotPermitted {#not-permitted}

오류: 이 동작은 허용되지 않습니다. 관리자나 운영진 메서드처럼 권한이 없는 메서드를 호출하거나, 나를 차단한 사용자를 팔로우하는 등 허용되지 않은 동작을 수행하려 할 때 나타납니다.

#### current_user.disabled? {#disabled}

오류: 현재 로그인이 비활성화되어 있습니다. 중재자가 OAuth 토큰으로 인증된 사용자의 계정을 비활성화했을 때 나타납니다.

#### !current_user.confirmed? {#unconfirmed}

오류: 로그인 계정에 확인된 이메일 주소가 없습니다. OAuth 토큰으로 인증된 사용자 계정의 이메일 주소가 아직 확인되지 않았을 때 나타납니다.

#### !current_user.approved? {#unapproved}

오류: 현재 로그인 계정은 승인 대기 중입니다. OAuth 토큰으로 인증된 사용자가 가입 승인이 필요한 서버에 가입했으며 중재자가 아직 계정을 승인하지 않았을 때 나타납니다.

### 404 - 찾을 수 없음 {#404}

#### RecordNotFound {#not-found}

오류: 레코드를 찾을 수 없습니다. 엔터티 레코드가 없거나 인증된 사용자가 비공개 엔터티의 공개 대상에 속하지 않을 때 나타납니다.

### 422 - 처리할 수 없는 엔터티 {#422}

#### RecordInvalid {#invalid}

오류: {문자열}. 엔터티 생성에 실패했을 때 나타날 수 있습니다.

#### RecordNotUnique {#not-unique}

오류: 중복 레코드입니다. 이미 고정된 계정이나 게시물을 고정하려 할 때 나타납니다.

#### !current_user {#user-required}

오류: 이 메서드는 인증된 사용자가 필요합니다. 사용자 인증이 필요한 API 메서드를 인증된 사용자가 없는 OAuth 토큰으로 호출하거나 토큰 없이 호출하려 할 때 나타납니다.

### 429 - 요청이 너무 많음 {#429}

오류: {번역된 문자열}. 요청 빈도 제한을 초과했을 때 나타납니다. 자세한 내용은 [요청 빈도 제한]({{< relref "api/rate-limits" >}})을 참고하세요.

### 503 - 원격 서비스를 사용할 수 없음 {#503}

#### UnexpectedResponseError {#unexpected-response}

오류: 원격 데이터를 가져올 수 없습니다. 마스토돈이 다른 서버의 WebFinger 같은 원격 서비스를 호출했으나 오류가 반환될 때 나타납니다.

#### SSLError {#ssl}

오류: 원격 SSL 인증서를 확인할 수 없습니다. 호출한 원격 서비스의 SSL 인증서가 유효하지 않을 때 나타납니다.

#### NetworkingError {#networking-error}

오류: 요청을 처리하는 중 일시적인 문제가 발생했습니다. 다시 시도하세요. S3 스토리지 서버 호출에 실패했을 때 나타납니다.

#### RaceConditionError {#race-condition}

오류: 요청을 처리하는 중 일시적인 문제가 발생했습니다. 다시 시도하세요. 서버 코드의 경쟁 상태로 인해 오류가 발생했을 때 나타납니다.

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/base_controller.rb" caption="app/controllers/api/base_controller.rb" >}}





