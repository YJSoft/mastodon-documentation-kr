---
title: 실험적 비동기 새로고침 API 메서드
description: 비동기 새로고침에 관한 메서드입니다.
menu:
  docs:
    name: 비동기 새로고침
    parent: methods
    identifier: methods-async-refreshes
aliases: [
  "/methods/async_refreshes",
  "/api/methods/async_refreshes"
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

{{< hint style="warning" >}}
이 페이지는 아직 확정되지 않은 API 엔드포인트를 설명합니다. 여러 용도로 사용할 예정이지만 지금까지는 한 가지만 구현했습니다. 모바일 앱에서도 아직 사용하지 않습니다. 따라서 요구사항이 바뀔 수 있습니다. 서드파티 개발자의 의견도 환영합니다.
이 API가 안정화되었다고 선언하고 위치를 옮긴 뒤에도 사용자가 안정 엔드포인트로 이전할 시간을 가질 수 있도록 한 버전 동안 이 엔드포인트를 추가로 유지합니다.
{{</ hint >}}

## 비동기 새로고침 상태 가져오기 {#show}

```http
GET /api/v1_alpha/async_refreshes/:id HTTP/1.1
```

결과를 생성하거나 다시 생성하는 백그라운드 작업이 이미 실행 중이거나, 요청이 결과를 생성 또는 가져오는 백그라운드 작업을 시작하기 때문에 API 요청이 예상한 결과나 가능한 모든 결과를 반환하지 못할 때가 있습니다.

예를 들어 다시 생성해야 하는 타임라인(시간이 걸립니다), 백그라운드에서 원격 서버로부터 추가 결과를 가져오도록 하는 검색 등의 요청이 있습니다.

이 모든 경우에 API 응답은 추가 헤더를 포함할 수 있습니다(MAY).

```http
Mastodon-Async-Refresh: id="<string>", retry=<int>, result_count=<int>
```

`retry` 키는 같은 엔드포인트를 다시 시도하거나 이 엔드포인트를 조회하기 전에 클라이언트가 최소한 기다려야 하는(SHOULD) 초 단위 시간입니다.

`result_count` 키는 선택 사항입니다. 있으면 진행 중인 비동기 새로고침의 일부로 이미 가져온 결과의 수를 포함합니다.

클라이언트는 `id`를 사용해 이 엔드포인트에서 비동기 새로고침의 현재 상태를 조회할 수 있습니다.

비동기 새로고침의 `status`는 `running` 또는 `finished`입니다. 타임라인 재생성과 같은 일부 비동기 새로고침에서는 이 정보만으로 더 기다릴지 타임라인을 새로고침할지 결정할 수 있습니다. 다른 종류는 이미 생성되거나 가져온 새 결과 수를 담은 `result_count` 키를 선택적으로 포함할 수 있습니다. 클라이언트는 이 수에 따라 리소스를 다시 가져오거나, 더 기다리거나, 아무 작업도 하지 않을 수 있습니다. 즉 `result_count`가 `0`인 `finished` 작업은 완료되었지만 새 결과가 없다는 의미입니다. 이 경우 새로고침할 필요가 없습니다.

백그라운드 작업의 비동기적 특성으로 경쟁 상태가 발생할 수 있습니다. 또한 일부 비동기 새로고침은 사용자와 무관하지만 가져온 데이터는 그렇지 않으므로, 새 데이터를 가져와도 현재 사용자에게 적합하지 않을 수 있습니다. 예를 들어 게시물의 새 답글을 가져오는 백그라운드 작업이 시작될 수 있습니다. 새 답글이 있어도 현재 사용자가 그 작성자를 차단했을 수 있습니다.

이러한 이유로 `AsyncRefresh`는 클라이언트가 언제 새 데이터를 요청할 가치가 있을지 알려주는 지표 역할만 할 수 있습니다. 일반적으로 새 데이터가 제공된다는 보장은 없습니다.

**반환:** `async_refresh` 키 하나가 있고 값은 [AsyncRefresh]({{< relref "entities/AsyncRefresh" >}})인 해시\
**OAuth:** 사용자 토큰 + `read`\
**버전 이력:**\
4.4.0 - 추가

### 요청 {#request}

#### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

### 응답 {#response}

#### 200: 성공 {#200-ok}

```json
{
  "async_refresh": {
    "id": "ImNvbnRleHQ6MTEzNjQwNTczMzAzNzg1MTc4OnJlZnJlc2gi--c526259eb4a1f3ef0d4b91cf8c99bf501330a815",
    "status": "running",
    "result_count": 2
  }
}
```

#### 404: 찾을 수 없음 {#404-not-found}

```json
{
  "error": "Not Found"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1_alpha/async_refreshes_controller.rb" caption="app/controllers/api/v1_alpha/async_refreshes_controller.rb" >}}
