---
title: 상태 확인 API 메서드
description: 서버 웹 프로세스의 상태를 확인합니다.
menu:
  docs:
    name: 상태 확인
    parent: methods
    identifier: methods-health
aliases: [
  "/methods/health"
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 기본 상태를 JSON으로 가져오기 {#get}

마스토돈 서버 웹 프로세스의 상태를 확인합니다. 간단한 모니터링에 유용합니다. 이 엔드포인트는 웹 프로세스가 요청에 응답하는지 확인합니다. 데이터베이스와 캐시에 성공적으로 연결할 수 있는지도 확인합니다.

HTTP 200 이외의 응답은 웹 프로세스의 일부 요소가 정상적이지 않다는 뜻으로 해석해야 합니다.

```http
GET /health HTTP/1.1
```

**반환:** 상태 정보\
**OAuth:** 공개\
**버전 이력:**\
3.0.0 - 추가

#### 요청 {#request}

##### 쿼리 매개변수 {#query-parameters}

none

#### 응답 {#response}

##### 200: 성공 {#200-ok}

```json
{
  "status": "UP"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/health_controller.rb" caption="app/controllers/health_controller.rb" >}}
