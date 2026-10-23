---
title: API 시작하기
description: 'REST API, HTTP 요청과 응답, 매개변수의 기초를 소개합니다.'
menu:
  docs:
    weight: 10
    parent: client
---

## REST 소개 {#rest}

마스토돈은 REST API를 통해 데이터에 접근할 수 있게 합니다. REST는 REpresentational State Transfer의 약자이지만, 여기서는 요청에 따라 다양한 리소스의 정보를 보내고 받는 방식이라고 생각하면 됩니다. 마스토돈 REST API는 요청에 HTTP를, 페이로드에 JSON을 사용합니다.

## HTTP 요청과 응답 이해하기 {#http}

REST API 엔드포인트는 특정 HTTP 메서드로 호출할 수 있으며, 같은 엔드포인트에서 여러 메서드를 사용할 수도 있습니다. 마스토돈 API는 일반적으로 다음 HTTP 메서드를 사용합니다.

* **GET**: 리소스를 읽거나 봅니다.
* **POST**: 서버에 정보를 보냅니다.
* **PUT** \| **PATCH**: 리소스를 업데이트합니다.
* **DELETE**: 리소스를 삭제합니다.

선호하는 프로그래밍 언어에는 아마 HTTP 요청을 만드는 유틸리티나 라이브러리가 있을 것입니다. 이 절의 예제에서는 여러 운영 체제에 기본적으로 포함되어 있는 명령줄 유틸리티 cURL(`curl`)을 사용합니다.

cURL의 기본 HTTP 메서드는 GET이지만 `--request` 또는 `-X` 플래그로 요청 유형을 지정할 수 있습니다. 예를 들어 `curl -X POST`는 GET 대신 POST 요청을 보냅니다. 필요하다면 `-i` 플래그를 사용하여 응답의 일부로 반환되는 추가 HTTP 헤더도 포함할 수 있습니다.

## 매개변수 제공하기 {#parameters}

HTTP 요청에는 여러 방식으로 추가 매개변수를 포함할 수 있습니다. 특히 마스토돈 API는 쿼리 문자열, 폼 데이터, JSON을 이해합니다.

{{< hint style="info" >}}
API는 쿼리 문자열, 폼 데이터, POST 본문으로 제출한 JSON을 모두 동일하게 처리합니다. GET 요청에는 쿼리 문자열을, 나머지 요청에는 폼 데이터나 JSON을 사용하는 것이 일반적입니다.
{{< /hint >}}

### 쿼리 문자열 {#query-strings}

URL 끝에 쿼리 문자열을 추가하여 요청합니다. 먼저 ?를 입력한 다음 parameter=value 형태로 추가합니다. 여러 쿼리 문자열은 &로 구분하여 추가할 수 있습니다. 예:

```bash
curl https://mastodon.example/endpoint?q=test&n=0
```

### 폼 데이터 {#form-data}

쿼리 문자열로 URL을 변경하는 대신 데이터를 별도로 보낼 수 있습니다. cURL에서는 `--data` 또는 `-d` 플래그로 데이터를 전달합니다. 쿼리 문자열처럼 한꺼번에 보내거나, 여러 데이터 플래그를 사용하여 키와 값 쌍을 따로 보낼 수도 있습니다. 키와 값 쌍에 `--form` 또는 `-F` 플래그를 사용할 수도 있으며, 이를 통해 파일 등의 멀티파트 데이터도 보낼 수 있습니다. 예:

```bash
# send raw data as query strings
curl -X POST \
     -d 'q=test&n=0' \
     https://mastodon.example/endpoint
# send raw data separately
curl -X POST \
     -d 'q=test' \
     -d 'n=0' \
     https://mastodon.example/endpoint
# explicit form-encoded; allows for multipart data
curl -X POST \
     -F 'q=test' \
     -F 'n=0' \
     -F 'file=@filename.jpg' \
     https://mastodon.example/endpoint
```

### JSON {#json}

ECMA-404에 정의된 *JavaScript Object Notation*입니다. 간단한 한 페이지 개요: https://www.json.org/

폼 데이터를 보내는 방식과 비슷하지만 데이터가 JSON 형식임을 지정하는 헤더가 추가됩니다. cURL로 JSON 요청을 보내려면 헤더에 JSON 콘텐츠 유형을 지정한 다음 JSON 데이터를 폼 데이터로 보냅니다.

```bash
curl -X POST \
     -H 'Content-Type: application/json' \
     -d '{"parameter": "value"}' \
     https://mastodon.example/endpoint
```

## 데이터 유형 {#types}

### 여러 값(배열) {#array}

배열 매개변수는 대괄호 표기법으로 인코딩해야 합니다. 예를 들어 `array[]=foo&array[]=bar`는 다음과 같이 변환됩니다.

```ruby
array = [
  'foo',
  'bar',
]
```

JSON에서는 배열을 다음과 같이 표현합니다.

```json
{
  "array": ["foo", "bar"]
}
```

### 중첩 매개변수(해시) {#hash}

일부 매개변수는 중첩해야 합니다. 이때도 대괄호 표기법을 사용해야 합니다. 예를 들어 `source[privacy]=public&source[language]=en`은 다음과 같이 변환됩니다.

```ruby
source = {
  privacy: 'public',
  language: 'en',
}
```

JSON에서는 해시를 다음과 같이 표현합니다.

```json
{
  "source": {
    "privacy": "public",
    "language": "en"
  }
}
```

### 참 또는 거짓(불리언) {#boolean}

불리언 값은 `0`, `f`, `F`, `false`, `FALSE`, `off`, `OFF`이면 거짓으로, 빈 문자열이면 제공되지 않은 것으로, 나머지 모든 값은 참으로 간주합니다. JSON 데이터를 사용할 때는 대신 리터럴 `true`, `false`, `null`을 사용합니다.

### 파일 {#file}

파일 업로드는 `multipart/form-data`로 인코딩해야 합니다.

배열과 조합할 수도 있습니다.

## API 응답 데이터 사용 방법 {#responses}

마스토돈 REST API는 응답 텍스트로 JSON을 반환합니다. 또한 응답 처리에 유용할 수 있는 HTTP 헤더와 서버가 요청을 어떻게 처리했는지 알려 주는 HTTP 상태 코드를 반환합니다. 다음 HTTP 상태 코드가 예상됩니다.

- 200 = OK. 요청을 성공적으로 처리했습니다.
- 4xx = 클라이언트 오류입니다. 요청이 올바르지 않습니다. 일반적으로 401 Unauthorized, 404 Not Found, 410 Gone, 422 Unprocessable Content 또는 [429 Too Many Requests]({{< relref "api/rate-limits" >}})를 볼 수 있습니다.
- 5xx = 서버 오류입니다. 요청을 처리하는 중 문제가 발생했습니다. 일반적으로 503 Unavailable을 볼 수 있습니다.
