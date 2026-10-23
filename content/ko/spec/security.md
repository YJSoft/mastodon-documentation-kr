---
title: 보안
description: 공개 키 암호 방식과 HTTP 및 JSON-LD에서 지원하는 서명 체계입니다.
menu:
  docs:
    weight: 30
    parent: spec
---

## 서명된 HTTP 요청 {#http}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/request.rb" caption="app/lib/request.rb" >}}

HTTP 서명 헤더는 HTTP 메시지에 암호학적으로 서명하는 방법입니다. 마스토돈은 수신한 활동이 이를 생성한 행위자가 작성했는지 검증하기 위해 HTTP 서명을 요구합니다. 보안 모드가 활성화되면 모든 GET 요청에도 HTTP 서명이 필요합니다.

### HTTP 서명 {#http-signatures}

{{< hint style="warning" >}}
이 버전의 HTTP 서명은 이전 마스토돈 버전(아직 지원되는 4.4.0 포함) 및 다른 연합우주 구현과의 호환성을 위해 여전히 필요합니다. 하지만 장차 이 초기 초안에서 벗어날 예정이므로, 구현자는 검증부터 시작하여 최신 HTTP 메시지 서명(RFC9421) 사양도 구현할 것을 강력히 권장합니다.
{{< /hint >}}

마스토돈은 전통적으로 [HTTP 서명](https://datatracker.ietf.org/doc/html/draft-cavage-http-signatures)이라는 제안 초안 표준을 사용합니다. HTTP 요청에 `Signature:` 헤더를 사용하여 HTTP 메시지에 서명하는 사양입니다.

마스토돈으로 들어오는 모든 HTTP 요청에는 Signature 헤더를 첨부해야 합니다.

```http
Signature: keyId="https://my.example.com/actor#main-key",headers="(request-target) host date",signature="Y2FiYW...IxNGRiZDk4ZA=="
```

`Signature:` 헤더의 세 부분은 다음과 같이 나눌 수 있습니다.

```http
Signature:
  keyId="https://my.example.com/actor#main-key",
  headers="(request-target) host date",
  signature="Y2FiYW...IxNGRiZDk4ZA=="
```

`keyId`는 `signature` 생성에 사용하는 행위자와 키에 대응해야 합니다. 서명 값은 `headers`의 모든 매개변수를 이어 붙여 해당 키로 서명한 뒤 Base64로 인코딩한 값입니다. 행위자 키에 관한 자세한 내용은 [ActivityPub > 공개 키]({{< relref "activitypub#publicKey" >}})를 참고하세요. 키 예시는 다음과 같습니다.

```json
"publicKey": {
    "id": "https://my.example.com/actor#main-key",
    "owner": "https://my.example.com/actor",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvXc4vkECU2/CeuSo1wtn\nFoim94Ne1jBMYxTZ9wm2YTdJq1oiZKif06I2fOqDzY/4q/S9uccrE9Bkajv1dnkO\nVm31QjWlhVpSKynVxEWjVBO5Ienue8gND0xvHIuXf87o61poqjEoepvsQFElA5ym\novljWGSA/jpj7ozygUZhCXtaS2W5AD5tnBQUpcO0lhItYPYTjnmzcc4y2NbJV8hz\n2s2G8qKv8fyimE23gY1XrPJg+cRF+g4PqFXujjlJ7MihD9oqtLGxbu7o1cifTn3x\nBfIdPythWu5b4cujNsB3m3awJjVmx+MHQ9SugkSIYXV0Ina77cTNS0M2PYiH1PFR\nTwIDAQAB\n-----END PUBLIC KEY-----\n"
 },
```

함께 보기: [https://blog.joinmastodon.org/2018/07/how-to-make-friends-and-verify-requests/](https://blog.joinmastodon.org/2018/07/how-to-make-friends-and-verify-requests/)

#### HTTP 서명 생성 {#http-sign}

HTTP 서명을 생성하려면 해시와 서명에 포함할 헤더를 정의해야 합니다. 예를 들어 다음 GET 요청을 살펴보세요.

```http
GET /users/username/outbox HTTP/1.1
Host: mastodon.example
Date: 18 Dec 2019 10:08:46 GMT
Accept: application/ld+json; profile="https://www.w3.org/ns/activitystreams"
```

서명 문자열은 `headers`에 정의한 HTTP 헤더 값을 줄바꿈으로 연결하여 구성합니다. 보통 요청 대상, 호스트, 날짜를 포함하는 것이 좋습니다. 헤더가 제공되지 않으면 마스토돈은 `Date:` 헤더를 가정합니다. 위 GET 요청에서 `headers="(request-target) host date"`인 `Signature:`를 생성하려면 다음 문자열을 생성합니다.

```text
(request-target): get /users/username/outbox
host: mastodon.example
date: 18 Dec 2019 10:08:46 GMT
```

`Accept:` 헤더는 `headers`에 지정하지 않으므로 고려하지 않습니다.

그런 다음 서명 문자열을 RSA-SHA256(SHA-256을 사용하는 RSASSA-PKCS1-v1_5)으로 해시하고 행위자의 개인 키로 서명합니다. 결과 값을 `Signature:` 헤더의 `signature`에 첨부합니다. 최종 요청은 다음과 같습니다.

```http
GET /users/username/inbox HTTP/1.1
Host: mastodon.example
Date: 18 Dec 2019 10:08:46 GMT
Accept: application/ld+json; profile="https://www.w3.org/ns/activitystreams"
Signature: keyId="https://my.example.com/actor#main-key",headers="(request-target) host date",signature="Y2FiYW...IxNGRiZDk4ZA=="
```

이 요청은 기능상 `https://my.example.com/actor`가 `https://mastodon.example/users/username/inbox`를 요청하고, `keyId`에 연결된 개인 키로 `(request-target)`, `Host:`, `Date:`에 서명하여 제공된 `signature`를 생성함으로써 자신이 요청을 보냈음을 증명하는 것과 같습니다.

##### POST 요청 서명과 Digest 헤더 {#digest}

마스토돈에 POST 요청을 보낼 때는 요청 본문의 RSA-SHA256 다이제스트 해시를 계산하고 이 해시를 Base64로 인코딩하여 `Digest:` 헤더에 포함해야 합니다. `Digest:` 헤더는 `Signature:` 헤더의 `headers` 매개변수에도 포함해야 합니다. 예시:

```http
POST /users/username/inbox HTTP/1.1
HOST: mastodon.example
Date: 18 Dec 2019 10:08:46 GMT
Digest: sha-256=hcK0GZB1BM4R0eenYrj9clYBuyXs/lemt5iWRYmIX0A=
Signature: keyId="https://my.example.com/actor#main-key",headers="(request-target) host date digest",signature="Y2FiYW...IxNGRiZDk4ZA=="
Content-Type: application/ld+json; profile="https://www.w3.org/ns/activitystreams"

{
  "@context": "https://www.w3.org/ns/activitystreams",
  "actor": "https://my.example.com/actor",
  "type": "Create",
  "object": {
    "type": "Note",
    "content": "Hello!"
  },
  "to": "https://mastodon.example/users/username"
}
```

#### HTTP 서명 검증 {#http-verify}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/concerns/signature_verification.rb" caption="app/controllers/concerns/signature_verification.rb" >}}

다음 요청을 살펴보세요.

```http
POST /users/username/inbox HTTP/1.1
Host: mastodon.example
Date: 18 Dec 2019 10:08:46 GMT
Digest: e37e179c75071a291f90a5fd4f848da87b491f1282f7bb8509ef2115b81ee0f4
Signature: keyId="https://my.example.com/actor#main-key",headers="(request-target) host date digest",signature="Y2FiYW...IxNGRiZDk4ZA=="
Content-Type: application/ld+json; profile="https://www.w3.org/ns/activitystreams"

{
  "@context": "https://www.w3.org/ns/activitystreams",
  "actor": "https://my.example.com/actor",
  "type": "Create",
  "object": {
    "type": "Note",
    "content": "Hello!"
  }
  "to": "https://mastodon.example/users/username"
}
```

마스토돈은 다음 알고리즘으로 서명을 검증합니다.

* `Signature:`를 개별 매개변수로 분리합니다.
* `headers` 값으로 서명 문자열을 구성합니다.
* `keyId`[^keyId]를 가져와 행위자의 `publicKey`를 확인합니다.
* 서명 문자열을 RSA-SHA256으로 해시하고, Base64로 디코딩한 뒤 `publicKey[publicKeyPem]`으로 복호화한 `signature`와 비교합니다.
* `Date:` 헤더로 서명된 요청이 지난 12시간 이내에 생성되었는지 확인합니다.

### HTTP 메시지 서명 (RFC9421) {#http-message-signatures}

**버전 이력:**\
4.4.0 - `rsa-v1_5-sha256` 서명 검증 지원 추가. 기본적으로 활성화되지는 않음\
4.5.0 - `rsa-v1_5-sha256` 서명 검증 지원을 기본적으로 활성화\
4.7.0 (미출시) - `ed25519` 서명 검증 지원 추가. cavage 초안 서명으로 보낸 요청이 400 또는 401로 실패할 경우 대체 수단으로 RFC9421을 사용하여 발신 요청에 서명하는 기능 추가

마스토돈이 HTTP 서명을 구현한 이후 이 초안 사양은 대폭 개정되어 [RFC9421](https://www.rfc-editor.org/rfc/rfc9421.html)로 발표되었으며 “HTTP 메시지 서명”으로 이름이 바뀌었습니다.

마스토돈 4.4.0은 수신 HTTP 요청의 RFC9421 호환 서명을 지원했지만 `http_message_signatures` 기능 플래그를 켜야 했습니다. 마스토돈 4.5.0에서는 기능 플래그를 제거하고 이 지원을 기본적으로 활성화합니다.

위에서 설명한 HTTP 서명 표준과 가장 큰 차이는 HTTP 메시지 서명이 `Signature`와 `Signature-Input`이라는 *두 개의* 별도 HTTP 헤더를 사용한다는 점입니다.

```http
Signature-Input: sig1=("@method" "@target-uri" "content-digest");created=1748341414;keyid="https://my.example.com/actor#main-key" 
Signature: sig1=:Y2FiYW...IxNGRiZDk4ZA==:
```

`Signature-Input`에는 `keyid`, `created` 타임스탬프 같은 매개변수와 서명해야 하는 여러 구성 요소가 포함됩니다. 구성 요소는 HTTP 헤더일 수도 있고, 요청에 사용된 HTTP 메서드(`@method`)나 URL(`@target-uri`) 같은 “파생 구성 요소”일 수도 있습니다.

`Signature`에는 실제 서명만 포함됩니다.

마스토돈의 RFC9421 호환 서명 요구 사항은 다음과 같습니다.

* 서명은 하나만 지원합니다.
* `created` 매개변수가 반드시 있어야 합니다(MUST).
* “파생 구성 요소”인 `@method`와 `@target-uri`에 반드시 서명해야 합니다(MUST).
* `Content-Digest` 헤더([RFC9530](https://datatracker.ietf.org/doc/html/rfc9530))가 반드시 존재하고 서명되어야 합니다(MUST).
* 여전히 유일하게 지원하는 알고리즘은 [SHA-256을 사용하는 RSASSA-PKCS1-v1_5](https://www.rfc-editor.org/rfc/rfc9421.html#name-rsassa-pkcs1-v1_5-using-sha)입니다.

HTTP 메시지 서명에 관한 자세한 내용은 다음을 참고하세요.

* 모든 세부 사항: [RFC9421](https://www.rfc-editor.org/rfc/rfc9421.html)
* 대화형 실습 환경과 RFC9421 구현 라이브러리 목록: [HTTP 메시지 서명 샌드박스](https://httpsig.org/)

## 내장 서명 {#embedded-signatures}

서명된 HTTP 요청과 달리 내장 서명은 ActivityPub 문서의 일부이므로 저자 증명과 함께 문서를 중계할 수 있습니다.
이는 작성자 서버에 추가 요청을 보내지 않고 수신함 전달 등의 작업을 하는 데 유용합니다.

### 연결 데이터 서명 {#ld}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/activitypub/linked_data_signature.rb" caption="app/lib/activitypub/linked_data_signature.rb" >}}

{{< hint style="warning" >}}
마스토돈의 현재 LD 서명 구현은 사양 초안 작성 단계와 확정 단계 사이에 JSON-LD `@context`가 변경되어 구식이 되었습니다. 마스토돈은 `type`으로 `RsaSignature2017`을 기대하지만 이후 초안은 `https://w3id.org/security/v2` 네임스페이스를 통해 `RsaSignature2018`을 정의합니다. 또한 LD 서명 사양 전체는 이전 LD 서명 사양과 대체로 호환되지 않는 [검증 가능한 자격 증명 데이터 무결성 1.0](https://w3c.github.io/vc-data-integrity/) 사양으로 대체되었습니다. 따라서 LD 서명 지원 구현은 권장하지 않습니다.
{{< /hint >}}

[연결 데이터 서명 1.0](https://web.archive.org/web/20170923124140/https://w3c-dvcg.github.io/ld-signatures/)은 JSON-LD 문서에 암호학적 서명을 첨부하는 초안 사양이었습니다. LD 서명은 마스토돈에서 널리 사용되지는 않지만 다음 상황에서 사용합니다.

- 알려진 모든 피어에게 Delete 활동을 보내는 [자체 파괴]({{< relref "admin/tootctl#self-destruct" >}}) 절차를 실행할 때는 HTTP 서명을 사용할 수 없으므로 페이로드에 LD 서명을 사용합니다. HTTP 서버가 더 이상 이전 행위자 정보를 호스팅하지 않으므로 수신 서버는 로컬에 캐시된 행위자 키로 서명을 검증하여 처리합니다.
- 릴레이의 활동을 수신할 때 사용합니다. 공개 활동을 선택적으로 LD 서명과 함께 릴레이에 보낼 수 있으며, 릴레이를 구독하는 서버는 원본에서 활동을 직접 다시 가져올 필요가 없습니다. 이는 잠재적으로 무한한 수의 서버가 내 서버에서 게시물을 로드하려 하는 것을 막습니다.

#### LD 서명 생성 {#ld-sign}

서명을 생성할 때 마스토돈은 `https://mastodon.example/users/username#main-key`의 행위자에 연결된 키 쌍을 사용합니다. 그런 다음 문서의 RSA-SHA256 해시를 생성하고 해당 키 쌍으로 서명한 뒤 결과를 엄격한 Base64로 인코딩하여 `signatureValue`를 얻습니다. 다음 해시를 JSON-LD 문서에 병합합니다.

```json
"signature": {
    "type": "RsaSignature2017",
    "creator": "https://mastodon.example/users/username#main-key",
    "created": "2019-12-08T03:48:33.901Z",
    "signatureValue": "s69F3mfddd99dGjmvjdjjs81e12jn121Gkm1"
}
```

#### LD 서명 검증 {#ld-verify}

마스토돈은 다음 알고리즘으로 서명을 검증합니다.

* `signature`가 존재하며 해시인지 확인합니다.
* `signature[type]`이 `RsaSignature2017`인지 확인합니다.
* `signature[creator]` URI를 가져옵니다. 생성자가 존재하는지 확인합니다.
* `signature`에서 `type`, `id`, `signatureValue`를 제거하여 `signature[creator]`와 `signature[created]`만 남깁니다.
* `signatureValue`를 Base64로 디코딩하고 `signature[creator]`의 공개 키로 검증합니다.

[^keyId]: `keyId`는 `publicKeyPem` 속성(키 자료)을 참조하지 않습니다. 행위자에 연결된 `publicKey` 객체의 URI입니다. 이 공개 키 객체의 owner 속성은 키를 소유한 행위자의 URI여야 합니다. 추출된 `keyId` 값은 다음과 같이 처리합니다.

    * `keyId`가 행위자와 프래그먼트(`actor#key`)이면 owner는 동일한 문서(행위자)를 다시 가리킵니다.
    * `keyId`가 키(`/key`)이면 owner는 어떤 행위자를 다시 가리키고, 그 행위자는 동일한 키를 다시 가리켜야 합니다(양방향 주장 수립).

### 객체 무결성 증명 (FEP-8b32) {#fep-8b32}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/lib/activitypub/object_integrity_proof.rb" caption="app/lib/activitypub/object_integrity_proof.rb" >}}

**버전 이력:**\
4.7.0 (미출시) - `eddsa-jcs-2022` 또는 `mldsa44-jcs-2024` 암호 스위트를 사용하는 FEP-8b32 객체 무결성 증명 검증 지원 추가

앞 절에서 설명했듯이 연결 데이터 서명은 새 어휘를 사용하고 *암호 스위트*를 추상화하는 프레임워크를 제공하는 [검증 가능한 자격 증명 데이터 무결성 1.0](https://w3c.github.io/vc-data-integrity/) 사양으로 대체되었습니다. [FEP-8b32: 객체 무결성 증명](https://codeberg.org/fediverse/fep/src/branch/main/fep/8b32/fep-8b32.md)은 ActivityPub에서 `eddsa-jcs-2022` 암호 스위트로 이 사양을 사용하는 방법을 지정합니다.
마스토돈 4.7.0(미출시)에 수신 객체 무결성 증명 지원이 추가되었습니다.

어휘 변경 외에도 이 FEP가 권장하는 암호 스위트는 마스토돈이 연결 데이터 서명에 사용하는 `RsaSignature2017`과 두 가지 중요한 차이가 있습니다.
- RSA 대신 EdDSA를 사용합니다.
- [RDF 데이터셋 정규화](https://www.w3.org/TR/rdf-canon/) 대신 [JSON 정규화 방식](https://datatracker.ietf.org/doc/html/rfc8785)을 사용합니다. 훨씬 간단하고 자원 사용량이 적지만 JSON-LD 확장, 압축, 프레이밍 과정에서 보존되지 않습니다.

마스토돈은 `mldsa44-jcs-2024` 암호 스위트로 생성한 증명의 검증도 구현하여 이 지원을 확장합니다.

### 객체 신원 증명 검증 {#verifying-object-identity-proofs}

증명 검증은 [FEP-8b32](https://codeberg.org/fediverse/fep/src/branch/main/fep/8b32/fep-8b32.md#proof-verification)에 설명되어 있습니다.

마스토돈은 현재 연결 데이터 서명을 우선하며, 연결 데이터 서명이 없거나 검증할 수 없을 때만 객체 무결성 증명 검증을 시도합니다. 객체 신원 증명을 검증할 때는 다음 알고리즘을 사용합니다.

* 수신한 JSON에서 `signature`를 제거합니다(https://codeberg.org/fediverse/fep/src/branch/main/fep/8b32/fep-8b32.md#backward-compatibility 참고).
* `proof`가 존재하며 객체인지 확인합니다.
* `proof[type]`이 `DataIntegrityProof`이고, `proof[proofPurpose]`가 `assertionMethod`이며, `proof[verificationMethod]`가 존재하는지 확인합니다.
* `proof[expires]`가 있다면 미래로 설정되어 있는지 확인합니다.
* `proof[cryptosuite]`가 지원하는 암호 스위트 중 하나인지 확인합니다(현재 `eddsa-jcs-2022` 또는 `mldsa44-jcs-2024`).
* [FEP-521a](https://codeberg.org/fediverse/fep/src/branch/main/fep/521a/fep-521a.md)를 사용하여 `proof[verificationMethod]` URI가 지정한 키를 가져옵니다.
* 이전 단계에서 가져온 키로 암호 스위트 사양에 따라 서명을 검증합니다.
  * `eddsa-jcs-2022`의 경우 [데이터 무결성 EdDSA 암호 스위트 v1.0 사양](https://www.w3.org/TR/vc-di-eddsa/#verify-proof-eddsa-jcs-2022)에 지정되어 있습니다.
  * `mldsa44-jcs-2024`의 경우 [양자 내성 암호 스위트 v1.0 사양](https://www.w3.org/TR/2026/WD-vc-di-quantum-resistant-1.0-20260616/#verify-proof-ml-dsa)에 지정되어 있습니다.
