---
title: 라우트
description: HTTP 메서드가 컨트롤러와 액션에 매핑되는 방식
menu:
  docs:
    weight: 40
    parent: dev
---

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/config/routes.rb" caption="config/routes.rb" >}}

## 라우트 설명 {#routes}

마스토돈은 Ruby on Rails를 사용하며 라우터 설정은 config/routes.rb에 정의되어 있습니다. 자세한 내용은 [Ruby on Rails 라우팅 안내](https://guides.rubyonrails.org/routing.html)를 참고할 수 있으며, 이 페이지에서는 마스토돈의 기본 라우팅 처리 방식을 설명합니다.

### 라우트 구성 방식 {#router}

`namespace`는 특정 컨트롤러 디렉터리에 매핑된 라우트의 접두사입니다. `resources`는 해당 네임스페이스 디렉터리 안의 컨트롤러에 매핑됩니다. `scope`는 `module`의 컨트롤러로 전달합니다. 예를 들어 다음과 같이 축약된 코드를 살펴봅니다.

{{< code title="config/routes.rb 발췌" >}}
```ruby
namespace :api do
    namespace :v1 do
        resources :statuses, only [:create, :show, :destroy] do
            scope module: :statuses do
                resource :favourite, only: :create
                resource :unfavourite, to: 'favourites#destroy'
                member do
                    get :context
                end
            end
        end
    end
end
```
{{< /code >}}

첫 번째 리소스는 :api와 :v1 네임스페이스 아래에 중첩된 :statuses입니다. 따라서 HTTP 라우트는 /api/v1/statuses가 됩니다. `only`는 허용할 메서드를 지정하며, 이 메서드는 `app/controllers/api/v1/statuses_controller.rb`의 컨트롤러에서 정의합니다.

/api/v1/statuses 안에는 :statuses 모듈의 범위가 있으며 추가 리소스가 정의됩니다. 해당 리소스의 컨트롤러는 `app/controllers/api/v1/statuses/`에 있습니다. 예를 들어 :favourite는 `app/controllers/api/v1/statuses/favourites_controller.rb`의 #create 액션으로 처리하고, :unfavourite는 같은 컨트롤러의 #destroy 액션으로 처리합니다.

이 범위의 모든 `member`, 즉 `app/controllers/api/v1/statuses_controller.rb`에서 제어하는 모든 게시물에 대한 사용자 정의 메서드도 있습니다. 이 메서드는 GET /api/v1/statuses/:id/context에 매핑되며 해당 컨트롤러에 정의된 :context 액션으로 처리됩니다.

### 사용 가능한 메서드 {#methods}

#### :index {#index}

목록을 위한 HTTP GET에 매핑됩니다. 컨트롤러의 #index 액션으로 처리합니다.

#### :show {#show}

단일 항목 보기를 위한 HTTP GET에 매핑됩니다. 컨트롤러의 #show 액션으로 처리합니다.

#### :create {#create}

HTTP POST에 매핑됩니다. 컨트롤러의 #create 액션으로 처리합니다.

#### :update {#update}

HTTP PUT에 매핑됩니다. 컨트롤러의 #update 액션으로 처리합니다.

#### :destroy {#destroy}

HTTP DELETE에 매핑됩니다. 컨트롤러의 #destroy 액션으로 처리합니다.

## .well-known {#well-known}

### /.well-known/host-meta {#host-meta}

확장 가능한 리소스 설명자(XRD)입니다. WebFinger의 존재를 알립니다.

### /.well-known/nodeinfo {#nodeinfo}

`/nodeinfo/2.0`의 NodeInfo 2.0 엔드포인트에 매핑되며 소프트웨어 이름과 버전, 프로토콜, 사용 통계, 가입 허용 여부를 알립니다.

### /.well-known/webfinger {#webfinger}

ActivityPub 행위자 ID를 찾는 데 사용합니다. 자세한 내용은 [명세 준수 &gt; WebFinger]({{< relref "spec/webfinger" >}})를 확인합니다.

### /.well-known/change-password {#change-password}

계정 설정 페이지에 매핑됩니다.

### /.well-known/keybase-proof-config {#keybase}

Keybase 통합에 사용하며 허용되는 사용자명과 증명을 확인할 위치를 정의합니다.

{{< hint style="warning" >}}
아래 절은 작성 중입니다.
{{< /hint >}}

## 공개 URI {#public}

* `/users/username` = 사용자 URI
* `/users/username/remote_follow` = 원격 팔로우 대화 상자
* `/users/username/statuses/id` = 게시물 URI
* `/@username` = “게시물” 탭
* `/@username/with_replies` = “게시물과 답글” 탭
* `/@username/media` = “미디어” 탭
* `/@username/tagged/:hashtag` = 사용자의 해당 태그가 붙은 게시물
* `/@username/:status_id` = 게시물 고유 링크
* `/@username/:status_id/embed` = 임베드 가능한 버전
* `/interact/:status_id` = 원격 상호작용 대화 상자
* `/explore` = 프로필 디렉터리
* `/explore/:hashtag` = 자기소개에 이 해시태그가 있는 프로필
* `/public` = 공개 타임라인 미리 보기
* `/about` = 첫 화면
* `/about/more` = 상세 설명
* `/terms` = 이용약관

## API {#api}

* /api/oembed
* /api/proofs
* /api/v1
  * [게시물]({{< relref "methods/statuses" >}}) [create, show, destroy]
    * reblogged_by [index]
    * favourited_by [index]
    * reblog [create]
    * unreblog [POST reblog#destroy]
    * favourite [create]
    * unfavourite [POST favourites#destroy]
    * bookmark [create]
    * unbookmark [POST bookmarks#destroy]
    * mute [create]
    * unmute [POST mutes#destroy]
    * pin [create]
    * unpin [POST pins#destroy]
    * context [GET]
  * [타임라인]({{< relref "methods/timelines" >}})
    * home [show]
    * public [show]
    * tag [show]
    * list [show]
  * [스트리밍]({{< relref "methods/streaming" >}}) [index]
  * [사용자 정의 에모지]({{< relref "methods/custom_emojis" >}}) [index]
  * [추천]({{< relref "methods/suggestions" >}}) [index, destroy]
  * [예약 게시물]({{< relref "methods/scheduled_statuses" >}}) [index, show, update, destroy]
  * [환경설정]({{< relref "methods/preferences" >}}) [index]
  * [대화]({{< relref "methods/conversations" >}}) [index, destroy]
    * read [POST]
  * [미디어]({{< relref "methods/media" >}}) [create, update]
  * [차단]({{< relref "methods/blocks" >}}) [index]
  * [뮤트]({{< relref "methods/mutes" >}}) [index]
  * [좋아요]({{< relref "methods/favourites" >}}) [index]
  * [북마크]({{< relref "methods/bookmarks" >}}) [index]
  * [신고]({{< relref "methods/reports" >}}) [create]
  * [트렌드]({{< relref "methods/trends" >}}) [index]
  * [필터]({{< relref "methods/filters" >}}) [index, create, show, update, destroy]
  * [추천 계정]({{< relref "methods/endorsements" >}}) [index]
  * [읽은 위치]({{< relref "methods/markers" >}}) [index, create]
  * [앱]({{< relref "methods/apps" >}}) [create]
    * verify_credentials [credentials#show]
  * [서버]({{< relref "methods/instance" >}}) [show]
    * peers [index]
    * activity [show]
  * [도메인 차단]({{< relref "methods/domain_blocks" >}}) [show, create, destroy]
  * [디렉터리]({{< relref "methods/directory" >}}) [show]
  * [팔로우 요청]({{< relref "methods/follow_requests" >}}) [index]
    * authorize [POST]
    * reject [POST]
  * [알림]({{< relref "methods/notifications" >}}) [index, show]
    * clear [POST]
    * dismiss [POST]
  * [계정]({{< relref "methods/accounts" >}})
    * verify_credentials [GET credentials#show]
    * update_credentials [PATCH credentials#update]
    * search [show (search#index)]
    * relationships [index]
  * [계정]({{< relref "methods/accounts" >}}) [create, show]
    * statuses [index accounts/statuses]
    * followers [index accounts/follower_accounts]
    * following [index accounts/following_accounts]
    * lists [index accounts/lists]
    * identity_proofs [index accounts/identity_proofs]
    * follow [POST]
    * unfollow [POST]
    * block [POST]
    * unblock [POST]
    * mute [POST]
    * unmute [POST]
    * pin [POST]
    * unpin [POST]
  * [리스트]({{< relref "methods/lists" >}}) [index, create, show, update, destroy]
    * accounts [POST accounts/pins#destroy]
  * [추천 태그]({{< relref "methods/featured_tags" >}}) [index, create, destroy]
    * suggestions [GET suggestions#index]
  * [투표]({{< relref "methods/polls" >}}) [create, show]
    * votes [create polls/votes]
  * [푸시]({{< relref "methods/push" >}})
    * subscription [create, show, update, destroy]
  * [관리]({{< relref "methods/admin" >}})
    * accounts [index, show]
      * enable [POST]
      * unsilence [POST]
      * unsuspend [POST]
      * approve [POST]
      * reject [POST]
      * action [create account_actions]
    * reports [index, show]
      * assign_to_self [POST]
      * unassign [POST]
      * reopen [POST]
      * resolve [POST]
* /api/v2
  * [검색]({{< relref "methods/search" >}}) [GET search#index]

