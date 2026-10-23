---
title: "WebFinger"
description: "`user@domain` 멘션을 행위자 프로필 URI로 변환합니다."
menu:
  docs:
    weight: 20
    parent: spec
---

## WebFinger란 무엇이며 왜 사용하나요? {#intro}

마스토돈의 사용자 프로필은 내 웹사이트와 같은 곳에 로컬로 호스팅되거나 완전히 다른 웹사이트에 원격으로 호스팅될 수 있습니다. 같은 사용자명을 다른 도메인에서 사용할 수 있습니다. 따라서 마스토돈 사용자의 전체 멘션은 `@username@domain` 형식으로 사용자명과 도메인을 모두 포함합니다. 실제로 `@user@example.com`은 `@user@example.org`와 다릅니다. 도메인이 없으면 마스토돈은 `@username`이라는 로컬 사용자를 찾으려 합니다. 하지만 ActivityPub으로 누군가에게 전달할 때는 `@username@domain` 멘션만으로 충분하지 않습니다. 원격 행위자의 수신함과 발신함을 찾을 수 있도록 **먼저 멘션을 HTTPS URI로 변환해야 합니다**.

여기서 WebFinger를 사용합니다. [RFC 7033](https://tools.ietf.org/html/rfc7033)의 WebFinger는 특정 서버의 URI만으로 **리소스에 대한 링크를 확인하는 방법**을 정의하는 사양입니다. 예를 들어 이메일이나 전화번호를 통해 정확한 위치를 미리 알지 못해도 누구나 리소스 위치를 조회할 수 있습니다. 조회는 `/.well-known/webfinger` 엔드포인트로 보내며 `resource` 쿼리 매개변수를 함께 전달합니다. 마스토돈에서 사용하는 리소스 URI는 [RFC 7565](https://tools.ietf.org/html/rfc7565)의 `acct:` URI로, 특정 도메인에서 호스팅하는 프로필의 사용자명을 포함합니다.

{{< hint style="danger" >}}
**마스토돈은 다른 프로필의 주소를 지정할 때 멘션에 크게 의존하므로 완전히 상호 운용하려면 WebFinger가 필요합니다.** 보통 사용자는 직접 HTTPS URI를 알고 있다면 해당 URI 또는 `username@domain` 주소를 검색하여 프로필을 로드할 수 있지만, 마스토돈 내부 로직은 거의 전적으로 `acct`: URI나 `username@domain` 표현에 의존합니다. WebFinger가 없는 ActivityPub 구현의 객체나 프로필을 검색하면 작성자를 로컬 데이터베이스의 사용자로 변환할 수 없어 실패합니다.
{{< /hint >}}

## WebFinger 흐름 예시 {#example}

`mastodon.social` 웹사이트에 있는 사용자 `@Gargron`을 조회한다고 가정하겠습니다.

해당 도메인의 `/.well-known/webfinger` 엔드포인트로 요청을 보내고 `resource` 쿼리 매개변수를 `acct:` URI로 설정하면 됩니다.

{{< code title="https://mastodon.social/.well-known/webfinger?resource=acct:gargron@mastodon.social" >}}
```json
{
  "subject": "acct:Gargron@mastodon.social",
  "aliases": [
    "https://mastodon.social/@Gargron",
    "https://mastodon.social/users/Gargron"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://mastodon.social/@Gargron"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://mastodon.social/users/Gargron"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://mastodon.social/authorize_interaction?uri={uri}"
    }
  ]
}
```
{{< /code >}}

이 JSON 응답을 분석하여 원하는 유형의 링크를 찾을 수 있습니다. ActivityPub `id`를 찾으려면 특히 `application/activity+json`에 주목합니다.

이렇게 `@Gargron@mastodon.social`을 `https://mastodon.social/users/Gargron`으로 변환했으며, 이제 필요한 곳에서 이 URI를 `id`로 참조하여 ActivityPub으로 상호작용할 수 있습니다.

{{< code title="활동 예시" >}}
```json
{
"id": "https://social.example/activities/1",
"type": "Create",
"actor": "https://social.example/actors/1",
"object": {
    "id": "https://social.example/objects/1",
    "type": "Note",
    "content": "Hello, Gargron!"
},
"to": "https://mastodon.social/users/Gargron"
}
```
{{< /code >}}

위 예시에서 `social.example`은 마스토돈과 다른 URI 구조를 사용합니다. 따라서 사용자명과 도메인만으로 행위자 `id`를 추측할 수 없습니다. 하지만 `social.example`이 WebFinger를 지원하면 `https://social.example/.well-known/webfinger?resource=acct:username@social.example`을 요청하고 응답에서 `application/ld+json; profile="https://www.w3.org/ns/activitystreams"` 또는 `application/activity+json` 유형의 링크를 찾아 이 `id`를 얻을 수 있습니다. 이 링크에는 `rel="self"` 링크 관계도 있어야 합니다.

## 마스토돈의 WebFinger 요구 사항 {#mastodons-requirements-for-webfinger}

`username@domain` 또는 `@username@domain` 형식의 계정이 주어지면 마스토돈은 다음을 수행합니다.

- 해당 사용자명과 도메인으로 `acct:` URI를 구성합니다.
- 해당 `resource`에 대한 WebFinger 요청을 보냅니다.

마스토돈은 WebFinger 응답으로 다음을 확인합니다.

- `subject`가 존재합니다.
- `links` 배열에 `rel`이 `self`이고 `type`이 `application/ld+json; profile="https://www.w3.org/ns/activitystreams"` 또는 `application/activity+json`인 링크가 있습니다.
  - 이 링크의 `href`가 ActivityPub 행위자로 확인됩니다.

예를 들어 최소한의 유효한 WebFinger 응답은 다음과 같습니다.

```json
{
  "subject": "acct:username@host.example",
  "links": [
    {
      "href": "https://host.example/accounts/username",
      "rel": "self",
      "type": "application/activity+json"
    }
  ]
}
```

마스토돈은 해당 ActivityPub 행위자 표현(최초 WebFinger 요청 없이 직접 제공될 수도 있음)으로 다음을 수행합니다.

- `preferredUsername`과 행위자 서버의 호스트명을 가져옵니다.
- 해당 사용자명과 도메인으로 `acct:` URI를 구성합니다.
- 해당 `resource`에 대한 WebFinger 요청을 보냅니다.

`subject`가 `resource`와 일치하면 여기서 절차를 끝냅니다. 그렇지 않고 `subject`에 다른 정규 계정 URI가 포함되어 있으면, 마스토돈은 해당 정규 계정 URI에 대해 WebFinger 요청을 추가로 보내 동일한 기준으로 새 `resource`가 같은 ActivityPub 행위자에 연결되는지 확인합니다.

즉, 다음 경우가 유효합니다.

- `example.com`에 `acct:alice@example.com` 리소스를 요청하면 `preferredUsername`이 `alice`이고 도메인이 `example.com`인 행위자의 링크를 얻으며, `subject`는 요청한 리소스 `acct:alice@example.com`과 일치합니다.
- `example.com`에 `acct:alice@example.com` 리소스를 요청하면 `preferredUsername`이 `alice`이고 도메인이 `ap.example.com`인 행위자의 링크를 얻습니다.
  - ...그런 다음 `ap.example.com`에 `acct:alice@ap.example.com` 리소스를 요청하면 `subject`로 `acct:alice@example.com`을, 그리고 동일한 행위자의 링크를 얻습니다.

## FEP-2c59 {#FEP-2c59}

버전 4.6.0부터 마스토돈은 행위자가 WebFinger 핸들을 명시할 수 있게 하는 [FEP-2c59](https://codeberg.org/fediverse/fep/src/branch/main/fep/2c59/fep-2c59.md)도 지원합니다. 위 흐름보다 우선하며, `webfinger` 속성이 없거나 잘못된 형식일 때만 `preferredUsername`을 사용합니다.

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/services/activitypub/fetch_remote_actor_service.rb" caption="app/services/activitypub/fetch_remote_actor_service.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/services/resolve_account_service.rb" caption="app/services/resolve_account_service.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/webfinger.rb" caption="app/lib/webfinger.rb" >}}
