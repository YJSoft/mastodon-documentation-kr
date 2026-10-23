---
title: 컬렉션 구현하기
description: '컬렉션 API와 UX 지침의 개요'
menu:
  docs:
    weight: 80
    parent: client
---

## 개요 {#overview}

컬렉션은 사용자가 다른 사람에게 팔로우하도록 추천하는 계정의 모음입니다. 사용자는 컬렉션을 만들고 공유할 수 있으며, 다른 사용자의 컬렉션에 자신이 소개될지 여부를 제어할 수 있습니다.

컬렉션과 아래의 새 API는 `mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10부터 사용할 수 있습니다.

## 컬렉션 관리 {#managing-collections}

컬렉션을 위해 추가된 모든 새 API 메서드의 개요는 [컬렉션 메서드]({{< relref "methods/collections" >}})를 확인합니다. 여기에는 기본적인 CRUD(생성/읽기/업데이트/삭제) 작업 메서드가 포함됩니다.

### 새 컬렉션 만들기 {#creating-a-new-collection}

[`POST /api/v1/collections`]({{< relref "methods/collections#create" >}})으로 새 컬렉션을 만듭니다. 새 컬렉션은 비어 있어도 되지만 바로 소개할 계정 ID 목록을 제공할 수도 있습니다.

### 컬렉션 읽기 {#reading-collections}

[`GET /api/v1/:account_id/collections`]({{< relref "methods/collections#get_collections" >}})로 특정 계정의 모든 컬렉션을 가져올 수 있습니다.

마찬가지로 [`GET /api/v1/:account_id/in_collections`]({{< relref "methods/collections#in_collections" >}})로 특정 계정이 소개된 모든 컬렉션을 가져올 수 있습니다.

ID를 알고 있다면 [`GET /api/v1/collections/:id`]({{< relref "methods/collections#get_collection" >}})로 컬렉션 하나를 가져올 수 있습니다.


### 컬렉션 업데이트 {#updating-collections}

[`PATCH /api/v1/collections/:id`]({{< relref "methods/collections#update_collection" >}})로 이름이나 설명 등 컬렉션의 메타데이터를 업데이트합니다. 이 엔드포인트로는 컬렉션에서 소개하는 계정을 변경할 수 없습니다. 대신 다음 엔드포인트를 사용합니다.

[`POST /api/v1/collections/:collection_id/items`]({{< relref "methods/collections#add_account" >}})로 기존 컬렉션에 계정을 추가할 수 있습니다. 추가할 수 있는 계정의 조건은 [컬렉션 소개에 동의하기]({{< relref "client/collections#consent" >}})를 확인합니다.

마찬가지로 [`DELETE /api/v1/collections/:collection_id/items/:id`]({{< relref "methods/collections#remove_account" >}})로 컬렉션의 항목을 제거할 수 있습니다.

### 컬렉션 삭제 {#deleting-a-collection}

[`DELETE /api/v1/collections/:id`]({{< relref "methods/collections#delete_collection" >}})를 호출하면 컬렉션을 영구적으로 삭제합니다.

## 제한 사항 {#limitations}

* 컬렉션 하나에 최대 **25**개 계정을 추가할 수 있습니다. 마스토돈 이외의 다른 서버에서 온 컬렉션에는 최대 150개 항목이 포함될 수 있습니다.
* 사용자 한 명이 만들 수 있는 컬렉션 수에는 제한이 있으며 사용자 역할에 따라 결정됩니다. [`collection_limit`]({{< relref "entities/Role#collection_limit" >}})를 확인합니다. 기본값은 10이지만 관리자 사용자가 변경할 수 있습니다.
* 컬렉션에서 소개되는 데 동의한 사용자만 추가할 수 있습니다. 자세한 내용은 [다음 절]({{< relref "client/collections#consent" >}})을 확인합니다.
* 컬렉션은 연합되지만 게시물과 프로필 데이터처럼 마스토돈 서버가 로컬 캐시 사본을 보관합니다. 따라서 다른 서버의 컬렉션에 대해 로컬 서버에서 가져온 정보는 원격 서버의 현재 상태를 즉시 반영하지 않을 수 있습니다.

## 컬렉션 소개에 동의하기 {#consent}

원격 계정을 포함한 계정은 컬렉션에 소개되는 것을 허용하는지, 소개 요청을 자동 또는 수동으로 승인할지 나타낼 수 있습니다.

클라이언트 개발자는 계정을 컬렉션에 추가할 수 있는지 확인하려면 새 [`feature_approval`]({{< relref "entities/Account#feature_approval"  >}}) 속성을 검사해야 합니다. 이 속성은 게시물의 [`quote_approval`]({{< relref "entities/Status#quote_approval" >}})을 밀접하게 본떠 설계되었습니다.

동의하지 않았거나 환경설정을 알 수 없는 계정은 컬렉션에 추가할 수 없습니다.

따라서 이전 버전의 마스토돈을 포함하여 이 기능을 지원하지 않는 소프트웨어를 실행하는 서버의 계정도 컬렉션에 추가할 수 없습니다.

마스토돈은 수동 승인을 지원하지 않지만 다른 소프트웨어는 지원할 수 있습니다. 또한 마스토돈에는 아직 이를 위한 전용 설정이 없습니다. 대신 계정의 기존 `discoverable` 설정과 연결되어 있습니다. 앱이 계정이나 프로필 설정에서 `discoverable`을 변경할 수 있게 한다면 설명을 이에 맞게 조정해야 합니다.

컬렉션에 소개된 후에도 언제든지 동의를 철회할 수 있으며, 그러면 해당 컬렉션에서 계정이 자동으로 제거됩니다.

현재 사용자가 컬렉션에 소개되는 것에 대한 동의를 철회하려면 [POST /api/v1/collections/:collection_id/items/:id/revoke]({{< relref "methods/collections#revoke_item" >}}) 요청을 수행할 수 있습니다.

## 컬렉션 공유 {#sharing-collections}

컬렉션의 [`url`]({{< relref "entities/Collection" >}})과 정확히 일치하는 URL이 포함된 게시물을 만들면 마스토돈은 컬렉션 링크의 공유임을 감지합니다.

이러한 게시물을 API로 가져오면 멘션과 비슷하게 해당 컬렉션을 포함하는 새 [`tagged_collections`]({{< relref "entities/Status#tagged_collections" >}}) 속성이 있습니다.

이 정보를 활용하여 컬렉션의 풍부한 미리 보기를 렌더링하거나 링크에 표시를 더해 컬렉션으로 연결됨을 쉽게 알릴 수 있습니다. 사용자가 이러한 링크를 클릭하면 연결된 컬렉션이 앱 안에서 열려야 합니다.

## 컬렉션 신고 {#reporting-collections}

다른 사용자 생성 콘텐츠와 마찬가지로 컬렉션에도 설명 등에 원치 않는 콘텐츠가 포함될 수 있습니다. 앱은 사용자가 신고할 방법을 제공해야 합니다. 이를 지원하도록 기존 [신고 생성 엔드포인트]({{< relref "methods/reports#post" >}})를 확장하여 `collection_ids` 배열을 추가할 수 있게 했습니다. 게시물을 첨부하듯 신고에 컬렉션을 첨부할 수 있습니다.

## 기타 {#miscellaneous}

* [검색 API]({{< relref "methods/search" >}})는 아직 컬렉션 내용 검색을 지원하도록 확장되지 않았습니다. 다만 `resolve` 매개변수로 컬렉션 URL을 검색하는 것은 작동합니다.
* 컬렉션을 “목록에 표시하지 않음”으로 설정할 수 있습니다(`discoverable` 속성을 `false`로 설정). 이는 소유자의 프로필에 표시하지 않는다는 뜻입니다. 앞으로는 검색 결과와 기타 탐색 수단에도 표시되지 않게 됩니다. 목록에 표시하지 않는 컬렉션도 URL로 직접 접근할 수 있으므로 이를 통해 공유할 수 있습니다.
* 컬렉션을 위한 [Notification]({{< relref "entities/Notification" >}}) 유형 두 가지가 추가되었습니다. `added_to_collection`은 누군가 나를 컬렉션에 추가했음을 나타내며, `collection_update`는 내가 소개된 컬렉션을 소유자가 업데이트했을 때 전송됩니다.
