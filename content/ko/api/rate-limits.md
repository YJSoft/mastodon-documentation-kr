---
title: 요청 빈도 제한
description: REST API를 얼마나 자주 호출할 수 있는지 정의합니다.
menu:
  docs:
    weight: 30
    parent: api
---

## 헤더 {#headers}

요청 빈도 제한 정보는 응답 헤더에 반환됩니다.

`X-RateLimit-Limit`
: 기간당 허용되는 요청 수

`X-RateLimit-Remaining`
: 아직 보낼 수 있는 요청 수

`X-RateLimit-Reset`
: 요청 빈도 제한이 초기화될 시각의 타임스탬프

{{< hint style="info" >}}
하나의 API 메서드에 여러 요청 빈도 제한이 중첩 적용될 수 있습니다. 헤더는 그중 초과에 가장 가까운 제한의 정보를 반환합니다.
{{</ hint >}}

## 제한 {#limits}

기본적으로 다음 제한이 하드코딩되어 있습니다.

### 계정별 {#per-account}

모든 엔드포인트와 메서드는 5분 동안 300번 호출할 수 있습니다.

#### 미디어 업로드 {#uploading-media}

`POST /api/v1/media`는 30분 동안 30번 호출할 수 있습니다.

#### 게시물 삭제 {#deleting-statuses}

`DELETE /api/v1/statuses/:id` 또는 `POST /api/v1/statuses/:id/unreblog`는 30분 동안 30번 호출할 수 있습니다.

### IP별 {#per-ip}

모든 엔드포인트와 메서드는 5분 동안 300번 호출할 수 있습니다.

#### 계정 생성 {#creating-accounts}

`POST /api/v1/accounts`는 30분 동안 5번 호출할 수 있습니다.
