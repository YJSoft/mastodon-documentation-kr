---
title: 인용 게시물 구현하기
description: '인용 게시물 API와 UX 지침의 개요'
menu:
  docs:
    weight: 70
    parent: client
---

## 인용 게시물을 위한 API 추가 사항 {#api-additions-for-quote-posts}

아래의 새 API는 `mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 7부터 사용할 수 있습니다.

### 기존 엔터티의 새 속성 {#new-attributes-to-existing-entities}

- [Status]({{< relref "entities/status" >}}) 엔터티에는 [QuoteApproval]({{< relref "entities/QuoteApproval" >}}) 엔터티를 담는 새 `quote_approval` 속성이 있습니다.
- [Status]({{< relref "entities/status" >}}) 엔터티에는 수락된 인용 수를 세는 `quotes_count` 속성도 추가되었습니다.
- [CredentialAccount]({{< relref "entities/Account#CredentialAccount">}}) 엔터티에는 사용자의 기본 인용 정책을 담는 `source[quote_policy]` 속성이 추가되었습니다. 값은 `public`, `followers`, `nobody` 중 하나입니다.
- [ScheduledStatus]({{< relref "entities/scheduledstatus" >}}) 엔터티에는 인용 대상 게시물의 ID를 담는 새 `params[quoted_status_id]` 속성이 있습니다.
- [ScheduledStatus]({{< relref "entities/scheduledstatus" >}}) 엔터티에는 게시물의 인용 정책을 담는 새 `params[quote_approval_policy]` 속성도 있습니다. 값은 `public`, `followers`, `nobody` 중 하나입니다.
- [`GET /api/v1/preferences`]({{< relref "methods/preferences#get" >}}) 응답에는 사용자의 기본 인용 정책을 담는 새 속성 `posting:default:quote_policy`가 있습니다. 값은 `public`, `followers`, `nobody` 중 하나입니다.

### 새 알림 유형 {#new-notification-types}

마스토돈 4.5에서는 두 가지 알림 유형이 새로 도입되었습니다.
- `quote`: 누군가 내 게시물을 인용했습니다. 이는 마스토돈이 인용 게시물을 자동 수락했다는 뜻입니다. 마스토돈은 사용자에게 수동 승인을 제공하지 않습니다. 인용 게시물은 `status` 속성에 있습니다.
- `quoted_update`: 내가 인용한 게시물이 수정되었습니다. `update`와 비슷하지만 `status`에는 인용 대상 게시물이 아닌 내가 작성한 인용 게시물이 담깁니다. 현재는 나를 인용한 게시물의 수정에 대한 알림은 없습니다.

이 두 알림 유형은 [`/api/v1/push`]({{< relref "methods/push" >}}) 엔드포인트 요청에서도 새 `alerts` 키로 사용됩니다.

### 기존 엔드포인트의 새 매개변수 {#new-parameters-to-existing-endpoints}

다음 엔드포인트에 새 매개변수가 추가되었습니다.
- [`POST /api/v1/statuses`]({{< relref "methods/statuses#create" >}})에는 두 가지 선택적 매개변수가 새로 추가되었습니다.
  - `quoted_status_id`: 인용할 게시물의 식별자입니다.
    현재 사용자가 해당 게시물에 접근할 수 없거나 정책에서 인용을 허용하지 않는다는 사실을 마스토돈이 확실히 알면 오류가 발생합니다.\
    인용 대상 게시물이 같은 서버에 있지 않다면 인용은 명시적으로 수락될 때까지 [대기 상태]({{< relref "entities/Quote#state" >}})가 됩니다. 비공개 게시물은 비공개 인용으로만 인용할 수 있습니다.\
    개인 멘션은 인용할 수 없습니다.\
    개인 멘션에서 인용 작성자를 명시적으로 멘션하지 않으면 마스토돈은 해당 개인 멘션으로 인용을 보내는 것을 허용하지 않습니다.\
    게시물 본문에 인용 대상 게시물 링크가 아직 없다면 하위 호환성을 위해 서버가 본문 앞에 `<p class="quote-inline">RE: <a href="…">…</a></p>` 링크를 추가합니다. 이 추가된 문단은 마스토돈 웹 UI에서 숨겨집니다.
  - `quote_approval_policy`: `public`, `followers`, `nobody` 중 하나인 문자열입니다. 생략하면 사용자 기본 설정을 사용합니다. 게시물 공개 범위가 `private` 또는 `direct`라면 이 매개변수는 무시하고 정책을 `nobody`로 설정합니다.
- [`PUT /api/v1/statuses/:id`]({{< relref "methods/statuses#edit" >}})에는 새 매개변수 하나가 추가되었습니다.
  - `quote_approval_policy`: `public`, `followers`, `nobody` 중 하나인 문자열입니다. 생략하면 사용자 기본 설정을 사용합니다. 게시물 공개 범위가 `private` 또는 `direct`라면 이 매개변수는 무시하고 정책을 `nobody`로 설정합니다.
- [`PATCH /api/v1/accounts/update_credentials`]({{< relref "methods/accounts#update_credentials" >}})에는 새 매개변수 하나가 추가되었습니다.
  - `source[quote_policy]`: `public`, `followers`, `nobody` 중 하나인 문자열로 새 게시물을 작성할 때의 기본 인용 정책을 설정합니다.

### 새 엔드포인트 {#new-endpoints}

- [`GET /api/v1/statuses/:id/quotes`]({{< relref "methods/statuses#quotes" >}}): `id`로 지정한 게시물을 인용한 게시물 목록을 반환합니다. 로그인한 사용자가 필요합니다.
- [`POST /api/v1/statuses/:id/quotes/:quoting_status_id/revoke`]({{< relref "methods/statuses#revoke_quote" >}}): 게시물 `quoting_status_id`의 인용 인가를 철회합니다. `id`가 가리키는 게시물의 소유자가 현재 사용자여야 합니다.
- [`PUT /api/v1/statuses/:id/interaction_policy`]({{< relref "methods/statuses#edit_interaction_policy" >}}): 전체 수정 과정을 거치지 않고 `quote_approval_policy` 매개변수로 게시물의 인용 정책을 업데이트합니다.

## 클라이언트를 위한 일반 권장 사항 {#general-recommendations-for-clients}

인용 게시물 관련 기능의 대략적인 구현 우선순위는 다음과 같습니다.
- 인용 게시물 표시: 이를 구현하지 않으면 인용을 의도한 게시물을 표시할 때 의미가 손실될 수 있습니다.
- 인용 알림 처리와 인용 철회 제공: 기본 게시 설정을 바꾸지 않은 사용자의 게시물은 다른 사람이 인용할 수 있기 때문입니다.
- 새 게시물과 기존 게시물의 인용 정책 변경 처리
- 인용 게시물 작성 처리

### 인용 게시물 표시 {#displaying-quote-posts}

[Quote]{{< relref "entities/Quote" >}} 및 [ShallowQuote]({{< relref "entities/ShallowQuote" >}}) 엔터티에 이미 전처리된 모든 정보가 포함되어 있어 인용 게시물 표시는 비교적 간단합니다.

인용 대상 게시물에도 필터를 적용해야 합니다. 맥락 유형은 인용하는 게시물에서 상속됩니다. 예를 들어 홈 타임라인에 있다면 홈 타임라인 필터를 적용해야 합니다. 마스토돈 웹 UI에서는 인용 대상 게시물이 `hide` 동작 필터와 일치하더라도 인용하는 게시물이 일치하지 않으면 인용하는 게시물을 계속 표시하기로 했습니다. 이 경우 인용 대상 게시물은 “필터 중 하나로 인해 숨겨졌습니다”라는 문구와 함께 숨깁니다.

인용은 1단계보다 깊게 표시하지 않고 대신 자리 표시자를 사용하는 것을 권장합니다.
<img width="383" height="412" alt="인용 게시물 표시 예시" src="https://github.com/user-attachments/assets/5dc484b9-cb5c-4ac4-b653-6f238d35dc13" />

더 깊은 인용을 처리하기로 한다면 무한 재귀 가능성에 주의합니다.

또한 게시물에 `quote`가 있다면 콘텐츠에서 `quote-inline` CSS 클래스가 있는 요소를 제거하거나 숨겨야 합니다. 이 요소는 대체 표시용으로 사용되며 그렇지 않으면 중복됩니다.

### 인용 정책 해석 {#interpreting-quote-policies}

현재 마스토돈에서는 자동 승인만 가능한 `public`, `followers`, `nobody`라는 매우 단순한 인용 정책만 설정할 수 있지만, 기반 프로토콜은 자동 승인과 수동 승인 정책을 모두 허용하며 각 정책에 임의의 계정 목록을 지정할 수 있습니다. 마스토돈은 구현 복잡성과 데이터베이스 저장 공간 때문에 그 일부만 지원하기로 했지만, 설정할 수 있는 것보다 세분화된 정책을 노출합니다.

특히 자동 정책과 수동 정책의 구분을 지원하고, 하위 정책이 너무 복잡하여 마스토돈에서 정확히 표현할 수 없는 경우도 기록합니다. 이는 해당 하위 정책의 `unsupported_policy` 값으로 나타납니다.

위에서 설명한 `current_user` 속성을 통해 마스토돈은 API 사용자에게 게시물 인용이 `denied`인지, 승인이 `automatic`인지, 인용 승인이 `manual`인지, 마스토돈이 알 수 없는 `unknown`인지 알려 줍니다. 마지막 경우는 거절될 가능성이 높더라도 최대한 정확한 표현과 인용 작성을 원하는 “고급 사용자”를 대상으로 하지 않는 한 `denied`로 취급하는 것이 좋습니다.

`automatic` 및 `manual` 목록으로 사용자에게 정책을 최대한 정확하게 전달할 수 있습니다.

참고로 마스토돈 웹 UI는 `current_user`, `automatic`, `manual` 값을 다음과 같이 사용합니다.
- `current_user`가 `automatic`이면 인용을 허용하고 버튼에 “인용”이라고 표시합니다.
- `current_user`가 `manual`이면 인용을 허용하고 버튼에 “인용 요청” / “작성자가 직접 검토합니다”라고 표시합니다.
- `current_user`가 `unknown` 또는 `denied`이면 인용을 허용하지 않고, 정책에 `followers`가 있는지에 따라 “팔로워만 이 게시물을 인용할 수 있습니다” 또는 “이 게시물을 인용할 수 없습니다”를 표시합니다.

### 인용 정책 설정 {#setting-quote-policies}

앞서 설명했듯 기반 프로토콜은 더 복잡한 정책을 허용하지만, 마스토돈에서는 미리 정의된 몇 가지 정책만 설정할 수 있습니다.
- `public`(“누구나 인용 가능”): 차단된 사용자를 제외한 누구나 인용할 수 있습니다.
- `followers`(“팔로워만 인용 가능”): 팔로워와 작성자만 인용할 수 있습니다.
- `nobody`(“나만”): 작성자만 인용할 수 있습니다.

작성자는 개인 멘션을 제외하고 언제나 자신의 게시물을 인용할 수 있으며, 차단된 사용자는 절대 인용할 수 없습니다. 마스토돈은 차단된 사용자의 인용을 자동으로 거절합니다. 승인은 마스토돈이 자동 처리하므로 클라이언트의 수동 인가는 없지만 사후 인용 제거는 가능합니다.

마스토돈은 항상 `private`(“팔로워 전용”)와 `direct`(“개인 멘션”) 게시물의 정책을 `nobody`(“나만”)로 설정합니다. 사용자 혼란을 피하도록 UI에서도 이 제한을 고려해야 합니다.

### 인용 게시물 작성 {#authoring-quote-posts}

마스토돈 4.5는 정책이 허용하면 게시물을 인용할 수 있게 합니다. 인용과 함께 투표나 미디어 첨부를 추가할 수 없으므로 클라이언트에서도 이를 고려해야 합니다. 게시물을 수정하여 인용을 제거하거나 바꿀 수는 없습니다.
