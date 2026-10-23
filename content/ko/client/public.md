---
title: 공개 데이터 다뤄 보기
description: 엔드포인트와 엔터티에 익숙해지기
menu:
  docs:
    weight: 20
    parent: client
---

이제 cURL이나 선호하는 프로그래밍 언어의 HTTP 유틸리티 또는 라이브러리로 HTTP 요청을 만드는 방법을 알았으니, 엔드포인트와 응답을 알아볼 차례입니다.

## 엔드포인트 설명 {#endpoints}

모든 HTTP 요청은 대상 URL로 보냅니다. 웹사이트에서 데이터를 요청하거나 웹사이트로 데이터를 보낼 때는 특정 URL을 사용합니다. HTTP 서버는 URL에 따라 요청을 해석하고 적절한 응답을 반환합니다.

예제에서는 `https://mastodon.example`에서 호스팅되는 가상의 마스토돈 웹사이트 mastodon.example을 사용합니다. 이 웹사이트의 루트는 `/`이며, 특정 하위 디렉터리와 경로를 엔드포인트라고 합니다. 마스토돈 API 엔드포인트는 `/api` 네임스페이스 아래에 있으며, 현재 대부분의 메서드의 엔드포인트는 `/api/v1` 아래에 있습니다. 요청은 HTTP 메서드와 엔드포인트로 표기합니다. 예를 들어 GET /api/v1/endpoint는 해당 도메인의 해당 엔드포인트, 즉 `https://mastodon.example/api/v1/endpoint`로 보내는 GET 요청을 뜻합니다.

## 공개 타임라인 가져오기 {#timelines}

마스토돈 공개 데이터의 가장 기본적인 사용 사례 중 하나인 공개 타임라인을 살펴봅니다.

다음과 같이 [GET /api/v1/timelines/public]({{< relref "methods/timelines" >}})을 요청할 수 있습니다.

```bash
curl https://mastodon.example/api/v1/timelines/public
```

응답 텍스트가 상당히 많습니다! 공개 타임라인은 기본적으로 게시물 20개를 반환합니다.

{{< hint style="danger" >}}
일부 마스토돈 서버는 관리자 설정에서 타임라인의 공개 접근을 비활성화할 수 있습니다. 해당 서버가 그렇다면 오류 응답을 받게 됩니다.
{{</ hint >}}

`limit` 매개변수로 더 적게 요청할 수 있습니다. 이번에는 같은 엔드포인트에 제한을 2로 설정하여 요청해 봅니다.

```bash
curl https://mastodon.example/api/v1/timelines/public?limit=2
```

이번 응답은 다루기 더 쉬울 것입니다. 원하는 유틸리티로 JSON을 파싱하거나 보기 좋게 정리하면 다음과 비슷한 응답이 보입니다.

```json
[
  {
    "id": "103206804533200177",
    "created_at": "2019-11-26T23:27:31.000Z",
    // ...
    "visibility": "public",
    // ...
  },
  {
    "id": "103206804086086361",
    "created_at": "2019-11-26T23:27:32.000Z",
    // ...
    "visibility": "public",
    // ...
  }
]
```

[GET /api/v1/timelines/tag/:hashtag]({{< relref "methods/timelines#tag" >}})를 호출하면 해시태그도 비슷하게 처리할 수 있습니다. 여기서 콜론은 엔드포인트의 해당 부분이 경로 매개변수임을 뜻합니다. :hashtag에는 해시태그 이름을 넣습니다. 이번에도 제한을 2로 설정합니다.

```bash
curl https://mastodon.example/api/v1/timelines/tag/cats?limit=2
```

다시 게시물 2개가 [Status]({{< relref "entities/status" >}}) 엔터티의 JSON 배열로 반환됩니다. JSON을 배열로 파싱한 다음 객체로 파싱할 수 있습니다. Python을 사용한다면 코드는 다음과 비슷합니다.

```python
import requests
import json

response = requests.get("https://mastodon.example/api/v1/timelines/tag/cats?limit=2")
statuses = json.loads(response.text) # this converts the json to a python list of dictionary
assert statuses[0]["visibility"] == "public" # we are reading a public timeline
print(statuses[0]["content"]) # this prints the status text
```

{{< hint style="info" >}}
JSON을 파싱하여 프로그램에서 사용하는 방법은 선택한 프로그래밍 언어와 프로그램 설계에 따라 다르므로 이 안내의 범위를 벗어납니다. 선택한 프로그래밍 언어에서 JSON을 다루는 다른 안내를 찾아보세요.
{{< /hint >}}

## 공개 계정과 게시물 가져오기 {#posts}

이제 요청을 만들고 응답을 처리하는 방법에 익숙해졌으니 더 많은 공개 데이터로 실험할 수 있습니다. 다음 메서드가 유용할 수 있습니다.

* 계정 ID를 알면 [GET /api/v1/accounts/:id]({{< relref "methods/accounts" >}})로 [Account]({{< relref "entities/account" >}}) 엔터티를 볼 수 있습니다.
  * 해당 계정이 작성한 공개 게시물을 보려면 [GET /api/v1/accounts/:id/statuses]({{< relref "methods/statuses" >}})를 사용하고 결과로 나온 [Status]({{< relref "entities/status" >}}) 엔터티 배열을 파싱합니다.
* 게시물 ID를 알면 [GET /api/v1/statuses/:id]({{< relref "methods/statuses#get" >}})로 Status 엔터티를 볼 수 있습니다.
  * [GET /api/v1/statuses/:id/reblogged_by]({{< relref "methods/statuses#reblogged_by" >}})로 해당 게시물을 부스트한 사람을 볼 수도 있고,
  * [GET /api/v1/statuses/:id/favourited_by]({{< relref "methods/statuses#favourited_by" >}})로 해당 게시물에 좋아요를 누른 사람을 볼 수도 있습니다.
  * [GET /api/v1/statuses/:id/context]({{< relref "methods/statuses#context" >}})를 요청하면 대화 스레드 트리에서 해당 게시물의 상위 및 하위 게시물을 볼 수 있습니다.
  * 게시물에 투표가 첨부되어 있다면 [GET /api/v1/polls/:id]({{< relref "methods/polls" >}})로 투표를 따로 볼 수 있습니다.

계정과 게시물의 ID는 마스토돈 웹사이트의 데이터베이스에 한정되며 마스토돈 웹사이트마다 다릅니다.

## 공개 서버 데이터 가져오기 {#instance}

익명 요청으로 마지막으로 할 수 있는 일은 마스토돈 웹사이트 정보를 보는 것입니다.

* [GET /api/v1/instance]({{< relref "methods/instance#v1" >}})로 일반 정보를 볼 수 있고,
  * [GET /api/v1/instance/peers]({{< relref "methods/instance#peers" >}})로 연결된 서버를 보거나,
  * [GET /api/v1/instance/activity]({{< relref "methods/instance#activity" >}})로 주간 활동을 볼 수 있으며,
  * [GET /api/v1/custom_emojis]({{< relref "methods/custom_emojis" >}})로 사용 가능한 모든 사용자 정의 에모지를 나열할 수 있습니다.
* 사용 가능한 모든 프로필의 디렉터리는 [GET /api/v1/directory]({{< relref "methods/directory" >}})를 확인합니다.
* 현재 인기 있는 해시태그는 [GET /api/v1/trends]({{< relref "methods/trends" >}})를 확인합니다.

{{< hint style="info" >}}
서버 데이터만으로 할 수 있는 실제 사례로 [emojos.in](https://emojos.in/)을 살펴보세요. 특정 서버의 모든 사용자 정의 에모지를 미리 볼 수 있습니다.
{{< /hint >}}

