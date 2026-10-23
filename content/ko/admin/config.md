---
title: 환경 설정하기
description: 마스토돈 설치 환경의 환경 변수 설정
menu:
  docs:
    weight: 30
    parent: admin
---

마스토돈은 환경 변수를 설정으로 사용합니다.

편의를 위해 마스토돈 디렉터리의 `.env.production`이라는 일반 파일(“dotenv” 파일)에서 읽을 수 있지만, 특정 프로세스에서 언제든 덮어쓸 수 있습니다. 예를 들어 systemd 서비스 파일은 `EnvironmentFile`이나 `Environment` 인라인 정의에서 환경 변수를 읽을 수 있으므로 특정 서비스마다 다른 설정 매개변수를 둘 수 있습니다. 명령줄에서 마스토돈을 호출할 때 지정할 수도 있습니다.

## 기본 {#basic}

### 연합과 표시 {#federation}

#### `LOCAL_DOMAIN` {#local_domain}

네트워크에서 서버를 식별하는 고유 식별자입니다. 변경하면 원격 서버가 기존 계정을 완전히 새로운 계정으로 혼동하므로 나중에 안전하게 변경할 수 없습니다. 서버를 운영하는 도메인 이름이어야 하며 프로토콜 부분은 제외합니다. 예를 들어 `example.com`만 사용합니다.

#### `WEB_DOMAIN` {#web_domain}

`WEB_DOMAIN`은 마스토돈을 한 도메인에 설치하면서 사용자 주소에는 다른 도메인을 사용하게 하는 선택적 환경 변수입니다. 예를 들어 사용자 주소는 `@alice@example.com`이지만 마스토돈 접속은 `mastodon.example.com`으로 할 수 있습니다. 도메인 이름을 이미 다른 웹사이트에 사용하지만 더 보기 좋거나 짧아서 마스토돈 식별자로도 쓰고 싶을 때 유용합니다.

`LOCAL_DOMAIN`과 마찬가지로 `WEB_DOMAIN`도 일단 설정하면 안전하게 변경할 수 없습니다. 이전 설정을 아는 원격 서버가 혼동하여 통신이 끊기거나 불안정해질 수 있기 때문입니다. 문제는 원격 서버가 계정을 이해하는 방식에 있으므로 마스토돈을 처음부터 다시 설치해도 해결되지 않습니다. 따라서 `LOCAL_DOMAIN`과 `WEB_DOMAIN` 설정 시 매우 신중해야 합니다.

`mastodon.example.com`에 마스토돈을 설치하면서 `@alice@example.com`을 제공하려면 `LOCAL_DOMAIN`을 `example.com`으로, `WEB_DOMAIN`을 `mastodon.example.com`으로 설정합니다. 또한 `example.com` 호스팅 서버에서 `https://example.com/.well-known/webfinger` 요청을 `https://mastodon.example.com/.well-known/webfinger`로 리디렉션하도록 추가 설정해야 합니다. 예를 들어 nginx 설정은 다음과 같습니다.

```nginx
location /.well-known/webfinger {
  add_header Access-Control-Allow-Origin '*';
  return 301 https://mastodon.example.com$request_uri;
}
```

{{< hint style="info" >}}
리디렉션에는 CORS 헤더가 있어야 합니다. 그렇지 않으면 마스토돈 웹 UI의 일부 기능이 작동하지 않습니다. 예: `Access-Control-Allow-Origin: *`
{{</ hint >}}

#### `ALTERNATE_DOMAINS` {#alternate_domains}

여러 도메인이 마스토돈 서버를 가리킨다면 이 설정으로 다른 도메인을 사용하는 사용자 주소에서도 서버가 자기 자신을 인식하게 합니다. 도메인은 `foo.com,bar.com`처럼 쉼표로 구분합니다.

#### `ALLOWED_PRIVATE_ADDRESSES` {#allowed_private_addresses}

나가는 HTTP 요청에서 허용할 사설 IP 주소와 서브넷을 쉼표로 구분한 목록입니다. 마스토돈은 [서버 측 요청 위조](https://en.wikipedia.org/wiki/Server-side_request_forgery)를 막기 위해 `127.0.0.1`, `192.168.1.1/16` 같은 사설 IP 범위 호스트로 보내는 HTTP 요청을 차단합니다. 이 설정은 지정한 IP 주소와 서브넷을 차단 대상에서 제외합니다.

#### `AUTHORIZED_FETCH` {#authorized_fetch}

“보안 모드”라고도 합니다. `true`로 설정하면 다음과 같이 바뀝니다.

- 마스토돈은 공개 게시물에 연결 데이터 서명을 생성하지 않습니다. 이로써 효율적이지만 정확한 통제 없이 재배포되는 것을 막습니다. 서명된 연결 데이터 객체는 그 자체로 완전하므로 원본 서버에 추가 요청을 보내지 않고도 전달할 수 있기 때문입니다.
- 마스토돈은 보통 인증 없이 제공되는 공개 게시물과 프로필의 ActivityPub 표현에도 HTTP 서명 인증을 요구합니다. 인증하지 않으면 프로필은 최소한의 기술 정보만 반환합니다.
- v4.0.0 이전: 보통 일부 API 엔드포인트는 인증 없이 사용할 수 있지만, 모든 REST/스트리밍 API 접근에 사용자 맥락, 즉 활성 사용자로 OAuth 인가 화면을 거친 상태를 요구합니다.

그 결과 인증을 요구하고 자신의 서버를 거치지 않는 재배포 방식을 사용하지 않음으로써, 공개 콘텐츠를 가져갈 수 있는 대상까지 통제할 수 있습니다. 예를 들어 도메인을 차단한 서버가 공개 콘텐츠를 가져가지 못하게 할 수 있습니다.

{{< hint style="warning" >}}
안타깝게도 보안 모드에는 단점이 있어 기본적으로 켜져 있지 않습니다. 연합우주의 모든 소프트웨어가 완전히 지원하지는 않으며 특히 3.0 이전 마스토돈 서버에서는 일부 기능이 작동하지 않습니다. 연결 데이터 서명은 공개 대화 스레드를 더 완전하게 만드는 데 쓰이므로 최신 서버 사이에서도 일부 유용한 기능을 잃습니다. 또한 공개 콘텐츠에 인증을 요구하면 캐싱이 불가능해져 연산 비용이 늘어납니다.
{{</ hint >}}

{{< hint style="warning" >}}
보안 모드는 공개 게시물과 프로필의 HTML 표현을 숨기지 않습니다. HTML은 기본 ActivityPub 표현이나 REST API보다 정보 손실이 큰 형식이지만 여전히 콘텐츠 수집 경로가 될 수 있습니다.
{{</ hint >}}

#### `LIMITED_FEDERATION_MODE` {#limited_federation_mode}

`true`로 설정하면 마스토돈은 수동 승인한 서버와만 연합하며 모든 공개 페이지와 일부 REST API를 비활성화합니다. 제한된 연합 모드는 보안 모드(`AUTHORIZED_FETCH`)를 바탕으로 합니다.

이 기능이 다른 기능에 미치는 영향을 고려합니다.

- 제한된 연합 모드를 활성화하면 도메인 차단은 무시하고 도메인 허용을 활성화합니다. 기존 서버를 제한된 연합 모드로 전환할 때는 다음 명령으로 허용하지 않은 도메인의 기존 데이터를 제거해야 합니다.

    ```bash
    tootctl domain purge --limited-federation-mode
    ```

- 제한된 연합 모드를 비활성화하면 도메인 허용은 무시하고 도메인 차단을 활성화합니다. 이 모드를 꺼서 더 넓은 네트워크에 참여할 때는 커뮤니티가 악의적인 행위자에게 우연히 노출될 가능성을 줄이도록 먼저 도메인 차단 목록을 가져오는 것이 좋습니다.

{{< hint style="warning" >}}
이 모드는 사실상 데이터를 고립시키므로 탈중앙화라는 마스토돈의 사명에 어긋납니다. 따라서 교육 기관이나 회사 내부망 같은 비공개 용도로만 사용하도록 의도되었습니다.
{{</ hint >}}

{{< hint style="info" >}}
3.1.5 이전에는 이 설정을 `WHITELIST_MODE`라고 불렀습니다.
{{</ hint >}}

#### `DISALLOW_UNAUTHENTICATED_API_ACCESS` {#disallow_unauthenticated_api_access}

마스토돈 v4.0.0부터는 로그아웃한 방문자를 포함한 모든 요청을 웹 앱으로 렌더링합니다. 이를 위해 웹 앱은 공개 API 요청으로 계정과 게시물을 가져옵니다. 이를 금지하려면 이 변수를 `true`로 설정합니다. 인증되지 않은 API 접근을 금지하면 로그아웃한 사용자의 프로필과 게시물 고유 링크가 오류를 반환하므로, 사실상 로컬 로그인이나 ActivityPub 가져오기로만 콘텐츠를 볼 수 있습니다.

#### `SINGLE_USER_MODE` {#single_user_mode}

`true`로 설정하면 서버 첫 화면은 항상 데이터베이스의 첫 번째 프로필로 리디렉션되고 가입은 비활성화됩니다.

#### `DISABLE_AUTOMATIC_SWITCHING_TO_APPROVED_REGISTRATIONS` {#disable_automatic_switching_to_approved_registrations}

방치된 마스토돈 서버가 스팸, 괴롭힘 및 기타 악의적인 활동에 악용되지 않도록, 가입이 열린 채 신고에 접근할 권한이 있는 로그인 사용자의 활동이 일주일 내내 감지되지 않으면 신규 가입을 중재자 승인이 필요한 방식으로 자동 전환합니다. 활동에는 앱에서 수행하는 중재 이외의 작업도 포함됩니다. 이때 서버 설정을 변경할 권한이 있는 사용자에게 이메일 알림을 보냅니다.

`DISABLE_AUTOMATIC_SWITCHING_TO_APPROVED_REGISTRATIONS=true`로 설정하면 이 동작을 비활성화합니다.

**버전 이력:**\
4.2.8 - 추가됨

#### `DEFAULT_LOCALE` {#default_locale}

기본적으로 마스토돈은 브라우저 헤더에서 방문자의 언어를 자동 감지하고 지원한다면 해당 언어로 인터페이스를 표시하며, 그렇지 않으면 영어로 표시합니다.
특정 언어나 지역을 위한 서버를 운영한다면 이 동작 때문에 해당 언어를 하지 못하는 방문자가 오해하여 가입할 수 있습니다. 따라서 이 변수를 특정 언어로 설정하는 것이 좋을 수 있습니다.

마스토돈 4.4.0부터는 이 환경 변수가 방문자의 브라우저 언어를 덮어쓰지 않습니다. 덮어쓰려면 `FORCE_DEFAULT_LOCALE=true`도 설정합니다.

**버전 이력:**\
4.4.0 - 대체 언어와 기본 언어에만 영향을 주도록 변경됨

예시 값: `de`

[지원 언어 목록](https://github.com/mastodon/mastodon/blob/main/config/initializers/i18n.rb)은 버전별로 바뀔 수 있으므로 실행 중인 버전이 원하는 로캘을 지원하는지 확인합니다.

지원하는 전체 로캘 목록을 보려면 다음을 실행합니다.

```bash
bin/rails runner 'puts Rails.application.config.i18n.available_locales.sort'
```

#### `FORCE_DEFAULT_LOCALE` {#force_default_locale}

`true`로 설정하면 방문자의 브라우저 언어 감지를 건너뛰고 `DEFAULT_LOCALE` 또는 영어를 사용합니다. 마스토돈 4.4.0 이전의 `DEFAULT_LOCALE` 동작에 해당합니다.

**버전 이력:**\
4.4.0 - 추가됨

### 비밀 정보 {#secrets}

#### `SECRET_KEY_BASE` {#secret_key_base}

`rails secret`으로 생성합니다. 변경하면 모든 활성 브라우저 세션이 무효화됩니다.

#### `OTP_SECRET` {#otp_secret}

`rails secret`으로 생성합니다. 변경하면 2단계 인증이 작동하지 않습니다.

#### `VAPID_PRIVATE_KEY` {#vapid_private_key}

`rake mastodon:webpush:generate_vapid_key`로 생성합니다. 변경하면 푸시 알림이 작동하지 않습니다.

#### `VAPID_PUBLIC_KEY` {#vapid_public_key}

`rake mastodon:webpush:generate_vapid_key`로 생성합니다. 변경하면 푸시 알림이 작동하지 않습니다.

### 배포 {#deployment}

#### `RAILS_ENV` {#rails_env}

실행 환경입니다. `production`, `development`, `test` 중 하나입니다. 개인 컴퓨터에서 개발 목적으로 실행한다면 기본값이기도 한 `development`를 사용합니다. 온라인으로 마스토돈을 운영한다면 `production`을 사용합니다. 환경에 따라 서로 다른 기본 설정을 불러옵니다.

{{< hint style="warning" >}}
이 변수는 dotenv(`.env`) 파일을 불러오기 전에 사용하므로 해당 파일에서 정의할 수 없습니다.
{{</ hint >}}

#### `RAILS_SERVE_STATIC_FILES` {#rails_serve_static_files}

true로 설정하면 마스토돈이 `public` 디렉터리 파일 요청에 응답합니다. 컨테이너 환경처럼 리버스 프록시(예: nginx)가 `public` 디렉터리 파일 시스템에 직접 접근할 수 없다면 필요할 수 있습니다. 하지만 파일 시스템에서 정적 파일을 직접 제공하는 것이 Ruby on Rails 프로세스로 제공하는 것보다 항상 훨씬 빠르므로 최적의 설정은 아닙니다.

#### `RAILS_LOG_LEVEL` {#rails_log_level}

웹 및 Sidekiq 프로세스에서 생성하는 로그 양을 결정합니다. 기본값 `info`는 처리하는 모든 요청과 백그라운드 작업마다 로그를 생성합니다. 유용할 수 있지만 트래픽이나 활동이 많으면 매우 많은 로그가 발생하여 컴퓨터의 I/O에 부담을 줄 수 있습니다. 이때는 문제가 생긴 정보만 출력하고 나머지 경우에는 조용한 `warn`을 권장합니다. 가능한 값은 `debug`, `info`, `warn`, `error`, `fatal`, `unknown`입니다.

#### `LOG_LEVEL` {#log_level}

스트리밍 프로세스에서 생성하는 로그 양을 결정합니다. 기본값은 `info`입니다. 가능한 값은 `debug`와 `info`입니다.

#### `TRUSTED_PROXY_IP` {#trusted_proxy_ip}

마스토돈 웹 및 스트리밍 프로세스에 신뢰할 리버스 프록시(예: nginx, Cloudflare)의 IP를 알려 줍니다. 중요한 요청 빈도 제한과 보안 기능에 쓰이는 각 요청의 원본 IP 판단에 영향을 줍니다. 잘못 설정하면 실제 원본 대신 리버스 프록시의 IP를 사용할 수 있습니다.

기본적으로 루프백과 사설 네트워크 주소 범위를 신뢰합니다. 구체적으로 다음과 같습니다.

- `127.0.0.1/8`
- `::1/128`
- `10.0.0.0/8`
- `172.16.0.0/12`
- `192.168.0.0/16`
- `fc00::/7`

리버스 프록시 하나가 마스토돈 웹 및 스트리밍 프로세스와 같은 컴퓨터나 사설 네트워크에서 실행된다면 대부분 기본 설정을 그대로 사용할 수 있습니다. 여러 프록시 모두가 같은 사설 네트워크에 있는 경우도 같습니다. 하지만 Cloudflare 같은 프록시가 공개 IP 주소로 웹 및 스트리밍 서버에 접근한다면 이 변수를 설정해야 합니다. 사용하는 모든 리버스 프록시의 IP나 [CIDR 표기법](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation) IP 범위를 쉼표로 구분하여 지정합니다. 이 변수를 설정하면 위의 기본 범위는 더 이상 신뢰하지 않으므로, 외부 프록시와 localhost 프록시를 _모두_ 사용한다면 양쪽 IP 또는 IP 범위를 모두 넣어야 합니다.

관리자와 중재자는 설정 > 중재 > 계정 탭에서 마스토돈이 각 사용자의 원본으로 인식하는 IP를 확인할 수 있습니다. [IPInfo](https://ipinfo.io) 같은 도구로 해당 IP가 최종 사용자의 ISP인지 프록시 호스팅 서버인지 판단할 수 있습니다.

#### `SOCKET` {#socket}

`127.0.0.1` 같은 IP 주소 대신 Unix 소켓에 바인딩할 수 있습니다. 이 변수는 프로세스별이므로 각 프로세스에 다른 값이 필요하며 웹(Puma) 프로세스와 스트리밍 API(Node.js) 프로세스 모두에 적용됩니다.

{{< hint style="warning" >}}
이 변수는 dotenv(`.env`) 파일을 불러오기 전에 사용하므로 해당 파일에서 정의할 수 없습니다.
{{</ hint >}}

#### `PORT` {#port}

Unix 소켓을 사용하지 않는다면 프로세스가 수신할 포트를 정의합니다. 이 변수는 프로세스별이므로 각 프로세스에 다른 값이 필요하며 웹(Puma)과 스트리밍 API(Node.js) 모두에 적용됩니다. 기본적으로 웹은 `3000`, 스트리밍 API는 `4000`에서 수신합니다.

{{< hint style="warning" >}}
이 변수는 dotenv(`.env`) 파일을 불러오기 전에 사용하므로 해당 파일에서 정의할 수 없습니다.
{{</ hint >}}

#### `NODE_ENV` {#node_env}

스트리밍 API(Node.js)에서 사용하는 `RAILS_ENV`에 해당합니다.

{{< hint style="warning" >}}
이 변수는 dotenv(`.env`) 파일을 불러오기 전에 사용하므로 해당 파일에서 정의할 수 없습니다.
{{</ hint >}}

#### `BIND` {#bind}

Unix 소켓을 사용하지 않는다면 프로세스가 바인딩할 IP를 정의합니다. 서로 다른 포트에서 수신한다면 여러 프로세스가 같은 IP에 바인딩할 수 있습니다. 기본값은 `127.0.0.1`입니다.

{{< hint style="warning" >}}
이 변수는 dotenv(`.env`) 파일을 불러오기 전에 사용하므로 해당 파일에서 정의할 수 없습니다.
{{</ hint >}}

#### `MASTODON_USE_LIBVIPS` {#mastodon_use_libvips}

기본적으로 마스토돈은 게시물 이미지를 ImageMagick으로 처리합니다. 대안으로 성능이 더 좋고 자원 사용량이 적은 [libvips](https://www.libvips.org) 8.13 이상을 사용할 수 있습니다.

소스에서 설치할 때 기본값은 `false`이며 활성화하려면 `true`로 설정합니다.

마스토돈 프로젝트의 컨테이너 이미지를 배포하면 `true`로 고정되며 덮어쓰면 안 됩니다.

**버전 이력:**\
4.3.0 - 추가됨

### 규모 확장 옵션 {#scaling}

{{< page-ref page="admin/scaling" >}}

#### `SIDEKIQ_CONCURRENCY` {#sidekiq_concurrency}

4.1에서 추가되었습니다. Sidekiq 전용 변수로, Sidekiq가 분기할 프로세스 수를 결정합니다. 기본값은 `5`입니다.

#### `WEB_CONCURRENCY` {#web_concurrency}

Puma 전용 변수로, Puma가 분기할 프로세스 수를 결정합니다. 기본값은 `2`입니다.

#### `MAX_THREADS` {#max_threads}

Puma 전용 변수로, 각 Puma 프로세스가 유지할 스레드 수를 결정합니다. 기본값은 `5`입니다.

#### `PERSISTENT_TIMEOUT` {#persistent_timeout}

Puma 전용 변수로, 연결을 닫기 전에 기다릴 시간을 결정합니다. 기본값은 `20`입니다.

#### `PREPARED_STATEMENTS` {#prepared_statements}

기본적으로 마스토돈은 성능상 이점이 있는 PostgreSQL의 준비된 구문 기능을 사용합니다. 트랜잭션 간 연결을 공유하는 연결 풀에서는 사용할 수 없으므로 `false`로 설정해야 합니다. 규모를 확장할 때는 트랜잭션 기반 연결 풀의 이점이 준비된 구문의 이점보다 큽니다.

#### `STREAMING_API_BASE_URL` {#streaming_api_base_url}

스트리밍 API를 다른 도메인이나 하위 도메인에 배포할 수 있습니다. 기본 구성에서는 오래 지속되는 스트리밍 요청을 nginx가 프록시하지만, 별도 도메인에서 제공하면 nginx를 완전히 거치지 않을 수 있어 성능이 개선될 수 있습니다.

예시 값: `wss://streaming.example.com`

#### `STREAMING_CLUSTER_NUM` {{%removed%}} {#streaming_cluster_num}

{{< hint style="danger" >}}
**제거됨:**\
스트리밍 서버 프로세스는 이제 단일 Node.js 프로세스만 사용합니다. 더 확장하려면 [규모 확장 안내](/admin/scaling#streaming)를 따라야 합니다.
{{< /hint >}}

스트리밍 API 전용 변수로, API가 분기할 프로세스 수를 결정합니다. 기본값은 CPU 코어 수에서 하나를 뺀 값입니다.

## 백엔드 {#backend}

### PostgreSQL {#postgresql}

#### `DB_HOST` {#db_host}

기본값은 `localhost`입니다.

#### `DB_USER` {#db_user}

기본값은 `mastodon`입니다.

#### `DB_NAME` {#db_name}

기본값은 `mastodon_production`입니다.

#### `DB_PASS` {#db_pass}

기본값은 없습니다.

#### `DB_PORT` {#db_port}

기본값은 `5432`입니다.

#### `DB_POOL` {#db_pool}

프로세스에 풀링할 데이터베이스 연결 수를 정의합니다. 프로세스의 모든 스레드를 감당해야 하므로 기본값은 `MAX_THREADS` 값입니다.

#### `DB_SSLMODE` {#db_sslmode}

PostgreSQL [SSL 모드](https://www.postgresql.org/docs/10/libpq-ssl.html)입니다. 기본값은 `prefer`입니다.

#### `DATABASE_URL` {#database_url}

제공하면 `DB_HOST`, `DB_USER`, `DB_NAME`, `DB_PASS`, `DB_PORT`보다 우선합니다.

예시 값: `postgresql://user:password@localhost:5432`

#### `QUERY_LOG_TAGS_ENABLED` {#query_log_tags_enabled}

`true`로 설정하면 ActiveRecord가 모든 SQL 구문 끝에 주석을 넣어 애플리케이션 성능 분석에 도움을 줍니다.

주석은 SqlCommenter 형식이며 다음 속성을 사용합니다.
- `namespaced_controller`: 이 SQL 구문을 생성한 HTTP 요청 컨트롤러의 전체 이름입니다.
- `action`: 이 SQL 구문을 생성한 HTTP 요청 액션의 이름입니다.
- `sidekiq_job_class`: 이 SQL 구문을 생성한 Sidekiq 작업의 클래스 이름입니다.

{{< hint style="warning" >}}
이 옵션을 활성화하면 준비된 구문을 비활성화합니다.
{{</ hint >}}

기본값은 `false`입니다.

**버전 이력:**\
4.4.0 - 추가됨

### PostgreSQL(읽기 전용 복제본) {#postgresql-replica}

{{< hint style="info" >}}
읽기 전용 데이터베이스 복제본을 사용하려면 [이 페이지](../scaling/#read-replicas)에서 자세한 내용을 확인할 수 있습니다.
{{</ hint >}}

#### `REPLICA_DB_HOST` {#replica_db_host}

기본값은 없습니다.

#### `REPLICA_DB_PORT` {#replica_db_port}

기본값은 없습니다.

#### `REPLICA_DB_NAME` {#replica_db_name}

기본값은 없습니다.

#### `REPLICA_DB_USER` {#replica_db_user}

기본값은 없습니다.

#### `REPLICA_DB_PASS` {#replica_db_pass}

기본값은 없습니다.

#### `REPLICA_DATABASE_URL` {#replica_database_url}

제공하면 `REPLICA_DB_HOST`, `REPLICA_DB_PORT`, `REPLICA_DB_NAME`, `REPLICA_DB_USER`, `REPLICA_DB_PASS`보다 우선합니다.

기본값은 없습니다.

### Redis {#redis}

마스토돈은 Redis를 세 가지 방식으로 사용합니다.

* 웹 애플리케이션 자체가 데이터를 저장하고 스트리밍 서버와 통신하는 데 사용합니다.
* Rails의 내장 캐싱 기능의 캐시 백엔드로 사용합니다.
* 백그라운드 작업을 처리하는 Sidekiq가 작업 데이터를 저장합니다.

세 가지 용도에 Redis 하나를 사용할 수 있습니다. 아래의 적절한 `REDIS_*` 변수를 사용하면 됩니다. 하지만
`CACHE_` 및 `SIDEKIQ_` 접두사가 붙은 변수로 둘 또는 세 개의 서로 다른 Redis를 사용할 수도 있습니다.

{{< hint style="info" >}}
휘발성 캐시에는 별도 Redis 서버 사용을 권장합니다. 단일 Redis 서버가 과부하되기 시작하면 분리하는 것이 좋습니다.
{{</ hint >}}

#### `REDIS_HOST` {#redis_host}

기본값은 `localhost`입니다.

#### `REDIS_PORT` {#redis_port}

기본값은 `6379`입니다.

#### `REDIS_USER` {#redis_user}

선택 사항입니다. Redis 연결에 사용할 사용자명입니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `REDIS_PASSWORD` {#redis_password}

선택 사항입니다. Redis 연결에 사용할 비밀번호입니다.

#### `REDIS_URL` {#redis_url}

제공하면 `REDIS_HOST`, `REDIS_PORT`, `REDIS_USER`, `REDIS_PASSWORD` 및 Sentinel 설정보다 우선합니다.

예시 값: `redis://user:password@localhost:6379`

Redis 서버에 TLS로 연결하려면 프로토콜 스키마 `rediss://`를 사용하는 `REDIS_URL`을 지정하고 아래 설명대로 `REDIS_DRIVER`를 설정해야 합니다.

#### `REDIS_DRIVER` {#redis_driver}

제공하면 Redis 연결 드라이버를 마스토돈 기본 hiredis 드라이버에서 표준 Ruby 드라이버로 바꿉니다. Redis에 TLS로 연결하려면 Ruby 드라이버가 필요합니다. 일부 환경에서는 Ruby 드라이버 사용이 Redis 성능에 영향을 줄 수 있습니다.

기본값은 `hiredis`이며 `hiredis` 또는 `ruby`를 사용할 수 있습니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `REDIS_NAMESPACE` {#redis_namespace}

제공하면 모든 Redis 키에 네임스페이스를 지정합니다. 서로 다른 프로젝트나 마스토돈 서버가 같은 Redis 데이터베이스를 공유할 수 있습니다.

{{< hint style="warning" >}}
이 옵션은 더 이상 권장하지 않습니다. Sidekiq 7은 네임스페이스 지원을 제거하며 향후 마스토돈 버전도 제거할 예정입니다. 그때까지 명확한 이전 방법을 문서화할 계획입니다. 새 서버를 설정한다면 이 옵션은 사용하지 않을 것을 강력히 권장합니다.
{{</ hint >}}

**버전 이력:**\
4.3.0 - 사용 중단 예정

#### `REDIS_SENTINELS` {#redis_sentinels}

Redis Sentinel의 HOST:PORT를 쉼표로 구분한 목록입니다. 포트는 선택 사항이며 생략하면 `REDIS_SENTINEL_PORT` 값 또는 기본값 `26379`를 사용합니다.

Redis Sentinel을 사용하려면 `REDIS_SENTINEL_MASTER`도 지정해야 합니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `REDIS_SENTINEL_MASTER` {#redis_sentinel_master}

연결할 Redis Sentinel 마스터의 이름입니다.

Redis Sentinel을 사용하려면 `REDIS_SENTINELS`도 지정해야 합니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `REDIS_SENTINEL_PORT` {#redis_sentinel_port}

`REDIS_SENTINELS`에 지정된 Sentinel의 기본 포트입니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `REDIS_SENTINEL_USERNAME` {#redis_sentinel_username}

Sentinel 인증에 사용할 사용자명입니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `REDIS_SENTINEL_PASSWORD` {#redis_sentinel_password}

Sentinel 인증에 사용할 비밀번호입니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `CACHE_REDIS_HOST` {#cache_redis_host}

기본값은 `REDIS_HOST` 값입니다.

#### `CACHE_REDIS_PORT` {#cache_redis_port}

기본값은 `REDIS_PORT` 값입니다.

#### `CACHE_REDIS_USER` {#cache_redis_user}

선택 사항입니다. Redis 연결에 사용할 사용자명입니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `CACHE_REDIS_PASSWORD` {#cache_redis_password}

선택 사항입니다. Redis 연결에 사용할 비밀번호입니다.

#### `CACHE_REDIS_URL` {#cache_redis_url}

제공하면 `CACHE_REDIS_HOST`와 `CACHE_REDIS_PORT`보다 우선합니다. 기본값은 `REDIS_URL` 값입니다.

#### `CACHE_REDIS_NAMESPACE` {#cache_redis_namespace}

기본값은 `REDIS_NAMESPACE` 값입니다.

#### `CACHE_REDIS_SENTINELS` {#cache_redis_sentinels}

Redis Sentinel의 HOST:PORT를 쉼표로 구분한 목록입니다. 포트는 선택 사항이며 생략하면 기본값 `26379`를 사용합니다.

Redis Sentinel을 사용하려면 `CACHE_REDIS_SENTINEL_MASTER`도 지정해야 합니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `CACHE_REDIS_SENTINEL_MASTER` {#cache_redis_sentinel_master}

연결할 Redis Sentinel 마스터의 이름입니다.

Redis Sentinel을 사용하려면 `CACHE_REDIS_SENTINELS`도 지정해야 합니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `CACHE_REDIS_SENTINEL_PORT` {#cache_redis_sentinel_port}

`CACHE_REDIS_SENTINELS`에 지정된 Sentinel의 기본 포트입니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `CACHE_REDIS_SENTINEL_USERNAME` {#cache_redis_sentinel_username}

Sentinel 인증에 사용할 사용자명입니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `CACHE_REDIS_SENTINEL_PASSWORD` {#cache_redis_sentinel_password}

Sentinel 인증에 사용할 비밀번호입니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `SIDEKIQ_REDIS_HOST` {#sidekiq_redis_host}

기본값은 `REDIS_HOST` 값입니다.

#### `SIDEKIQ_REDIS_PORT` {#sidekiq_redis_port}

기본값은 `REDIS_PORT` 값입니다.

#### `SIDEKIQ_REDIS_USER` {#sidekiq_redis_user}

선택 사항입니다. Redis 연결에 사용할 사용자명입니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `SIDEKIQ_REDIS_PASSWORD` {#sidekiq_redis_password}

선택 사항입니다. Redis 연결에 사용할 비밀번호입니다.

#### `SIDEKIQ_REDIS_URL` {#sidekiq_redis_url}

제공하면 `SIDEKIQ_REDIS_HOST`와 `SIDEKIQ_REDIS_PORT`보다 우선합니다. 기본값은 `REDIS_URL` 값입니다.

#### `SIDEKIQ_REDIS_NAMESPACE` {#sidekiq_redis_namespace}

기본값은 `REDIS_NAMESPACE` 값입니다.

#### `SIDEKIQ_REDIS_SENTINELS` {#sidekiq_redis_sentinels}

Redis Sentinel의 HOST:PORT를 쉼표로 구분한 목록입니다. 포트는 선택 사항이며 생략하면 기본값 `26379`를 사용합니다.

Redis Sentinel을 사용하려면 `SIDEKIQ_REDIS_SENTINEL_MASTER`도 지정해야 합니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `SIDEKIQ_REDIS_SENTINEL_MASTER` {#sidekiq_redis_sentinel_master}

연결할 Redis Sentinel 마스터의 이름입니다.

Redis Sentinel을 사용하려면 `SIDEKIQ_REDIS_SENTINELS`도 지정해야 합니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `SIDEKIQ_REDIS_SENTINEL_PORT` {#sidekiq_redis_sentinel_port}

`SIDEKIQ_REDIS_SENTINELS`에 지정된 Sentinel의 기본 포트입니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `SIDEKIQ_REDIS_SENTINEL_USERNAME` {#sidekiq_redis_sentinel_username}

Sentinel 인증에 사용할 사용자명입니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `SIDEKIQ_REDIS_SENTINEL_PASSWORD` {#sidekiq_redis_sentinel_password}

Sentinel 인증에 사용할 비밀번호입니다.

**버전 이력:**\
4.3.0 - 추가됨

### Elasticsearch {#elasticsearch}

{{< page-ref page="admin/elasticsearch" >}}

#### `ES_ENABLED` {#es_enabled}

`true`로 설정하면 마스토돈은 검색 기능에 Elasticsearch를 사용합니다.

#### `ES_PRESET` {#es_preset}

Elasticsearch 인덱스 구성(샤드와 복제본 수)을 제어합니다.

가능한 값은 다음과 같습니다.

- `single_node_cluster` (기본값)
- `small_cluster`
- `large_cluster`

[Elasticsearch 설정 페이지에서 각 설정의 자세한 내용](../elasticsearch#choosing-the-correct-preset)을 확인합니다.

#### `ES_HOST` {#es_host}

Elasticsearch 서버의 호스트입니다. 기본값은 `localhost`입니다. TLS를 사용하면 호스트명 앞에 `https://`를 붙입니다. 예: `https://elastic.example.com`

#### `ES_PORT` {#es_port}

Elasticsearch 서버의 포트입니다. 기본값은 `9200`입니다.

#### `ES_USER` {#es_user}

선택적으로 Elasticsearch 인증에 사용합니다.

#### `ES_PASS` {#es_pass}

선택적으로 Elasticsearch 인증에 사용합니다.

#### `ES_PREFIX` {#es_prefix}

여러 프로젝트나 서로 다른 마스토돈 서버가 Elasticsearch를 공유할 때 유용합니다. 기본값은 `REDIS_NAMESPACE` 값입니다.

#### `ES_CA_FILE` {#es_ca_file}

사용할 인증 기관 번들 파일을 덮어씁니다. 자체 서명 인증서를 사용할 때 유용합니다.

**버전 이력:**\
4.3.0 - 추가됨

### SMTP 이메일 배달 {#smtp}

#### `SMTP_SERVER` {#smtp_server}

#### `SMTP_PORT` {#smtp_port}

#### `SMTP_LOGIN` {#smtp_login}

#### `SMTP_PASSWORD` {#smtp_password}

#### `SMTP_FROM_ADDRESS` {#smtp_from_address}

#### `SMTP_DOMAIN` {#smtp_domain}

#### `SMTP_DELIVERY_METHOD` {#smtp_delivery_method}

#### `SMTP_AUTH_METHOD` {#smtp_auth_method}

#### `SMTP_CA_FILE` {#smtp_ca_file}

#### `SMTP_OPENSSL_VERIFY_MODE` {#smtp_openssl_verify_mode}

#### `SMTP_ENABLE_STARTTLS_AUTO` {#smtp_enable_starttls_auto}

#### `SMTP_ENABLE_STARTTLS` {#smtp_enable_starttls}

`auto`(기본값), `always`, `never` 중 하나로 설정합니다.

**버전 이력:**\
4.0.0 - 추가됨

#### `SMTP_TLS` {#smtp_tls}

#### `SMTP_SSL` {#smtp_ssl}

이메일 설정은 마스토돈이 사용하는 *Ruby on Rails* 프레임워크의 *action_mailer* 컴포넌트를 바탕으로 합니다. action_mailer의 전체 문서는 [여기](https://guides.rubyonrails.org/action_mailer_basics.html#action-mailer-configuration)에 있습니다. 클라이언트는 SMTP 또는 파생 방식인 StartTLS + SMTP나 SMTPS(TLS를 통한 SMTP)를 사용합니다.

### 기본 설정 {#basic}

* `SMTP_SERVER`: 사용할 서버를 지정합니다. 예: `sub.domain.tld`
* `SMTP_PORT`: 기본값은 일반 SMTP 포트인 `25`입니다. StartTLS를 감지하면 587번 포트로 전환할 수 있습니다.
* `SMTP_DOMAIN`: HELO 도메인이 필요할 때만 필수입니다. 기본적으로 `SMTP_SERVER` 도메인으로 설정됩니다.
* `SMTP_FROM_ADDRESS`: 발신자 주소를 지정합니다.
* `SMTP_DELIVERY_METHOD`: 기본값은 `smtp`이며 `sendmail`도 가능합니다.

### SMTP 서버 인증 {#smtpauthentication}

* `SMTP_LOGIN`: SMTP 사용자 로그인입니다.
* `SMTP_PASSWORD`: SMTP 사용자 비밀번호입니다.
* `SMTP_AUTH_METHOD`: `plain`(기본값, 비밀번호를 평문 전송), `login`(비밀번호를 base64 인코딩), `cram_md5` 중 하나입니다.

### 보안 SMTP {#secured-smtp}
기본적으로 지정한 SMTP 서버에 StartTLS 연결을 시도합니다.

* `SMTP_ENABLE_STARTTLS_AUTO`: 기본값은 `true`입니다.
* `SMTP_CA_FILE`: 값을 지정할 수 있지만 많은 Linux 배포판(예: Debian 계열)에서는 `/etc/ssl/certs/ca-certificates.crt`입니다.
* `SMTP_OPENSSL_VERIFY_MODE`: `none` 또는 `peer`입니다. TLS를 사용할 때 자체 서명 인증서 연결을 수락하는 데 유용할 수 있습니다.
* `SMTP_TLS`: `true` 또는 `false`이며 기본값은 `false`입니다.
* `SMTP_SSL`: `true` 또는 `false`이며 기본값은 `false`입니다.

현재 안전한 것으로 간주되는 SSL/TLS 프로토콜은 `TLSv1.3`과 `TLSv1.2`뿐입니다.

### 선택적 대량 이메일 설정 {#optional-bulk-email-settings}

일부 트랜잭션 이메일 제공자는 트랜잭션 성격이 아닌 이메일을 보낼 때 별도의 SMTP 자격 증명을 사용하도록 요구합니다. 마스토돈에서는 서버 사용자에게 많은 이메일을 보낼 수 있는 서버 공지와 이용약관 변경이 이에 해당합니다.

이를 위한 두 번째 SMTP 환경 변수 모음이 있습니다. 모두 `BULK_` 접두사가 붙으므로 `BULK_SMTP_SERVER`, `BULK_SMTP_PORT` 등이 있습니다. 위에서 설명한 접두사 없는 변수와 똑같이 동작합니다.

대량 이메일 설정은 전적으로 선택 사항입니다. 설정하지 않으면 모든 발신 이메일에 같은 SMTP 설정을 사용합니다.

**버전 이력:**\
4.4.0 - 선택적 대량 이메일 설정 지원 추가

### Prometheus 지표 {#prometheus}

마스토돈은 선택적으로 일부 지표를 Prometheus 형식으로 노출할 수 있습니다.

Ruby 프로세스에서는 [`prometheus_exporter` gem](https://github.com/discourse/prometheus_exporter)을 사용합니다. 자세한 내용은 해당 문서를 참고합니다.

기본적으로 `./bin/prometheus_exporter`로 `prometheus_exporter` 서버를 실행하여 지표를 수집하고 수집기가 가져갈 수 있도록 노출해야 합니다. 이 동작을 바꾸려면 `MASTODON_PROMETHEUS_EXPORTER_LOCAL`을 확인합니다.

스트리밍 서버에서는 Prometheus 형식의 지표가 항상 활성화되어 있으며 `http://streaming-server-host:port/metrics`에서 접근할 수 있습니다.

**버전 이력:**\
4.4.0 - Ruby 프로세스 지원 추가

#### `MASTODON_PROMETHEUS_EXPORTER_ENABLED` {#mastodon_prometheus_exporter_enabled}

`true`로 설정하면 마스토돈의 Ruby 프로세스(웹 및 Sidekiq)에서 Prometheus 계측을 활성화합니다.

#### `MASTODON_PROMETHEUS_EXPORTER_WEB_DETAILED_METRICS` {#mastodon_prometheus_exporter_web_detailed_metrics}

`true`로 설정하면 모든 웹 요청에 대해 컨트롤러와 액션별 지표를 수집하고 노출합니다. 추가 자원 부담이 생길 수 있습니다.

#### `MASTODON_PROMETHEUS_EXPORTER_SIDEKIQ_DETAILED_METRICS` {#mastodon_prometheus_exporter_sidekiq_detailed_metrics}

`true`로 설정하면 모든 Sidekiq 작업에 대해 작업별 지표를 수집하고 노출합니다. 추가 자원 부담이 생길 수 있습니다.

#### `MASTODON_PROMETHEUS_EXPORTER_LOCAL` {#mastodon_prometheus_exporter_local}

`true`로 설정하면 외부 `prometheus_exporter` 서버에 전송하는 대신 프로세스 내부 서버를 시작하여 지표를 노출합니다. 컨테이너 환경에서 Sidekiq를 실행할 때 외부 내보내기의 부담을 피하는 데 유용합니다. 지표는 `http://host:port/metrics`에 노출됩니다.

중요: Puma 같은 다중 프로세스 서버에서는 모든 프로세스가 같은 포트에서 수신하려 하여 실패하므로 작동하지 않습니다.

#### `PROMETHEUS_EXPORTER_HOST` {#prometheus_exporter_host}

프로세스 내부 서버가 활성화되지 않았다면 이 호스트로 지표를 보냅니다. 해당 호스트에는 `prometheus_exporter` 서버가 실행 중이어야 합니다. 기본값은 `localhost`입니다.

#### `PROMETHEUS_EXPORTER_PORT` {#prometheus_exporter_port}

프로세스 내부 서버가 활성화되지 않았다면 이 호스트로 지표를 보냅니다. 해당 호스트에는 `prometheus_exporter` 서버가 실행 중이어야 합니다. 기본값은 `9394`입니다.

#### `MASTODON_PROMETHEUS_EXPORTER_HOST` {#mastodon_prometheus_exporter_host}

프로세스 내부 서버를 활성화하면 내부 내보내기가 이 호스트에서 수신합니다. 기본값은 `localhost`입니다.

#### `MASTODON_PROMETHEUS_EXPORTER_PORT` {#mastodon_prometheus_exporter_port}

프로세스 내부 서버를 활성화하면 내부 내보내기가 이 포트에서 수신합니다. 기본값은 `9394`입니다.

### OpenTelemetry {#otel}

마스토돈은 OpenTelemetry 프로토콜로 추적 데이터를 내보낼 수 있습니다. 표준 OTEL Ruby SDK로 계측하며 `OTEL_SERVICE_NAME`을 제외한 [표준 OTEL 환경 설정 변수](https://opentelemetry.io/docs/languages/sdk-configuration/general/)를 지원합니다. OTEL_SERVICE_NAME 대신 아래의 `OTEL_SERVICE_NAME_PREFIX`를 확인합니다. 현재 마스토돈에는 OLTP 내보내기만 포함되어 있습니다.

**버전 이력:**\
4.3.0 - Ruby 백엔드 지원 추가

#### `OTEL_SERVICE_NAME_PREFIX` {#otel_service_name_prefix}

OTEL 서비스 이름의 접두사입니다. 서비스 이름은 `$prefix/web`와 `$prefix/sidekiq`가 됩니다. 기본값은 `mastodon`입니다.

#### `OTEL_SERVICE_NAME_SEPARATOR` {#otel_service_name_separator}

서로 다른 서비스를 구분하는 서비스 이름의 문자입니다. 기본값은 `/`이며 예를 들어 `mastodon/web`이 됩니다.

#### `OTEL_EXPORTER_OTLP_ENDPOINT` {#otel_exporter_otlp_endpoint}

추적을 보낼 OLTP 서버 URL입니다. 이 변수를 설정하지 않으면 OpenTelemetry 계측이 비활성화됩니다. 기본값은 없으며 빈 값입니다.

### 번역 서비스 {#translation}

마스토돈은 [DeepL] 및 [LibreTranslate]를 백엔드 언어 번역 엔진으로 통합할 수 있습니다. 두 서비스 모두 별도로 준비하고 환경 변수로 마스토돈에 사용 방법을 설정해야 합니다.

- DeepL에는 `DEEPL_API_KEY`와 `DEEPL_PLAN`(기본값 "free")이 필요합니다.
- LibreTranslate에는 `LIBRE_TRANSLATE_ENDPOINT`가 필요합니다. 자체 호스팅에서는 `LIBRE_TRANSLATE_API_KEY`가 선택 사항이지만 libretranslate.com처럼 API 키로 구성된 서버에서는 필수입니다.

[DeepL]: https://www.deepl.com
[LibreTranslate]: https://libretranslate.com

## 파일 스토리지 {#files}

### CDN {#cdn}

#### `CDN_HOST` {#cdn_host}

CDN(Content Delivery Network) 같은 별도 호스트에서 로고, 에모지, CSS, JS 등의 정적 에셋을 제공하면 사용자의 로딩 시간을 줄일 수 있습니다.

예시 값: `https://assets.example.com`

{{< hint style="info" >}}
파일에는 CORS 헤더가 있어야 합니다. 그렇지 않으면 마스토돈 웹 UI의 일부 기능이 작동하지 않습니다. 예: `Access-Control-Allow-Origin: *`
{{</ hint >}}

### 로컬 파일 스토리지 {#paperclip}

#### `PAPERCLIP_ROOT_PATH` {#paperclip_root_path}

#### `PAPERCLIP_ROOT_URL` {#paperclip_root_url}

### AWS S3 및 호환 스토리지 {#s3}

{{< page-ref page="admin/optional/object-storage" >}}

버킷은 접근 제어 목록(ACL)을 지원해야 합니다. AWS S3에서는 "Object Ownership"을 "ACLs enabled"로, Google Cloud Storage에서는 "Access control"을 "Fine-grained"로 설정합니다.

#### `S3_ENABLED` {#s3_enabled}

#### `S3_REGION` {#s3_region}

#### `S3_ENDPOINT` {#s3_endpoint}

#### `S3_BUCKET` {#s3_bucket}

#### `AWS_ACCESS_KEY_ID` {#aws_access_key_id}

#### `AWS_SECRET_ACCESS_KEY` {#aws_secret_access_key}

#### `S3_SIGNATURE_VERSION` {#s3_signature_version}

#### `S3_OVERRIDE_PATH_STYLE` {#s3_override_path_style}

#### `S3_PROTOCOL` {#s3_protocol}

#### `S3_HOSTNAME` {#s3_hostname}

#### `S3_ALIAS_HOST` {#s3_alias_host}

#### `EXTRA_MEDIA_HOSTS` {#extra_media_hosts}

**버전 이력:**\
4.4.0 - 추가됨

#### `S3_OPEN_TIMEOUT` {#s3_open_timeout}

#### `S3_READ_TIMEOUT` {#s3_read_timeout}

#### `S3_RETRY_LIMIT` {#s3_retry_limit}

#### `S3_FORCE_SINGLE_REQUEST` {#s3_force_single_request}

#### `S3_ENABLE_CHECKSUM_MODE` {#s3_enable_checksum_mode}

#### `S3_STORAGE_CLASS` {#s3_storage_class}

#### `S3_MULTIPART_THRESHOLD` {#s3_multipart_threshold}

#### `S3_PERMISSION` {#s3_permission}

#### `S3_BATCH_DELETE_LIMIT` {#s3_batch_delete_limit}

#### `S3_BATCH_DELETE_RETRY` {#s3_batch_delete_retry}

### Swift {#swift}

#### `SWIFT_ENABLED` {#swift_enabled}

#### `SWIFT_USERNAME` {#swift_username}

#### `SWIFT_TENANT` {#swift_tenant}

#### `SWIFT_PASSWORD` {#swift_password}

#### `SWIFT_PROJECT_ID` {#swift_project_id}

#### `SWIFT_AUTH_URL` {#swift_auth_url}

#### `SWIFT_CONTAINER` {#swift_container}

#### `SWIFT_OBJECT_URL` {#swift_object_url}

#### `SWIFT_REGION` {#swift_region}

#### `SWIFT_DOMAIN_NAME` {#swift_domain_name}

#### `SWIFT_CACHE_TTL` {#swift_cache_ttl}

### HTTP 캐시 무효화 {#http-cache-buster}

캐시 무효화 기능을 설정하면 미디어 파일이 원본에서 삭제되거나 접근 불가 상태가 될 때 캐시 무효화 요청을 보냅니다. 이를 통해 캐싱 계층이나 CDN에서도 마스토돈에서 제거된 콘텐츠를 지울 수 있습니다.

{{< hint style="info" >}}
구현 방법은 프록시나 CDN 제공자에 따라 크게 다르며 설정이 필요합니다. nginx를 HTTP 캐시에 사용한다면 `proxy_cache_purge` 설정 지시문을 확인합니다.
{{</ hint >}}

#### `CACHE_BUSTER_ENABLED` {#cache_buster_enabled}

`true`로 설정하면 파일 삭제 시 미디어 URL에 캐시 무효화 요청을 보내 캐시에서 파일을 제거할 수 있게 합니다.

기본값은 `false`입니다.

#### `CACHE_BUSTER_HTTP_METHOD` {#cache_buster_http_method}

기본값은 `GET`입니다.

#### `CACHE_BUSTER_SECRET_HEADER` {#cache_buster_secret_header}

`CACHE_BUSTER_SECRET`에 정의된 비밀 값을 담을 헤더의 이름입니다.

기본값은 빈 값이며 헤더를 추가하지 않습니다.

#### `CACHE_BUSTER_SECRET` {#cache_buster_secret}

위에서 구성한 `CACHE_BUSTER_SECRET_HEADER` 헤더의 값입니다.

## 외부 인증 {#external-authentication}

### OmniAuth {#omniauth}

#### `ALLOW_UNSAFE_AUTH_PROVIDER_REATTACH` {#allow_unsafe_auth_provider_reattach}
기존 사용자가 같은 이메일 주소를 사용하는 경우 이전에 사용하지 않은 외부 인증 제공자로 로그인하도록 허용합니다. 외부 제공자 간 이전을 제공하려는 경우 유용하지만 잠재적인 보안 위험이 있습니다. 공격자가 구성된 제공자 중 하나에서 대상 사용자의 이메일 주소로 새 신원을 만들면 계정을 탈취할 수 있기 때문입니다.

**버전 이력:**\
4.2.6 - 추가됨

#### `OMNIAUTH_ONLY` {#omniauth_only}

#### `ONE_CLICK_SSO_LOGIN` {#one_click_sso_login}
`Login or Register` 버튼을 활성화합니다.
모든 인증을 단일 외부 제공자(CAS, SAML, OIDC)로 처리하는
서버에서 유용합니다.

활성화하면 익명 세션의 캐싱을 막습니다.
또한 OIDC 검색을 사용할 때는 마스토돈이 시작되기 전에
신원 제공자를 사용할 수 있어야 합니다.

### LDAP {#ldap}

#### `LDAP_ENABLED` {#ldap_enabled}

#### `LDAP_HOST` {#ldap_host}

#### `LDAP_PORT` {#ldap_port}

#### `LDAP_METHOD` {#ldap_method}

#### `LDAP_BASE` {#ldap_base}

#### `LDAP_BIND_DN` {#ldap_bind_dn}

#### `LDAP_PASSWORD` {#ldap_password}

#### `LDAP_UID` {#ldap_uid}

#### `LDAP_SEARCH_FILTER` {#ldap_search_filter}

#### `LDAP_MAIL` {#ldap_mail}

#### `LDAP_UID_CONVERSION_ENABLED` {#ldap_uid_conversion_enabled}

### PAM {#pam}

#### `PAM_ENABLED` {#pam_enabled}

#### `PAM_EMAIL_DOMAIN` {#pam_email_domain}

#### `PAM_DEFAULT_SERVICE` {#pam_default_service}

#### `PAM_CONTROLLED_SERVICE` {#pam_controlled_service}

### CAS {#cas}

#### `CAS_ENABLED` {#cas_enabled}

#### `CAS_DISPLAY_NAME` {#cas_display_name}

#### `CAS_URL` {#cas_url}

#### `CAS_HOST` {#cas_host}

#### `CAS_PORT` {#cas_port}

#### `CAS_SSL` {#cas_ssl}

#### `CAS_VALIDATE_URL` {#cas_validate_url}

#### `CAS_CALLBACK_URL` {#cas_callback_url}

#### `CAS_LOGOUT_URL` {#cas_logout_url}

#### `CAS_LOGIN_URL` {#cas_login_url}

#### `CAS_UID_FIELD` {#cas_uid_field}

#### `CAS_CA_PATH` {#cas_ca_path}

#### `CAS_DISABLE_SSL_VERIFICATION` {#cas_disable_ssl_verification}

#### `CAS_UID_KEY` {#cas_uid_key}
계정 사용자명으로 사용할 키입니다.
생성되는 계정은 `@uid@domain.tld`입니다.

#### `CAS_NAME_KEY` {#cas_name_key}

#### `CAS_EMAIL_KEY` {#cas_email_key}

#### `CAS_NICKNAME_KEY` {#cas_nickname_key}

#### `CAS_FIRST_NAME_KEY` {#cas_first_name_key}

#### `CAS_LAST_NAME_KEY` {#cas_last_name_key}

#### `CAS_LOCATION_KEY` {#cas_location_key}

#### `CAS_IMAGE_KEY` {#cas_image_key}
계정 아바타로 사용할 이미지의 키입니다.
이 키의 값은 이미지 파일의 URL이어야 합니다.
지원되는 파일 형식인 JPEG나 PNG를 사용해야 하며 SVG는 사용할 수 없습니다.

#### `CAS_PHONE_KEY` {#cas_phone_key}

#### `CAS_SECURITY_ASSUME_EMAIL_IS_VERIFIED` {#cas_security_assume_email_is_verified}

### SAML {#saml}

#### `SAML_ENABLED` {#saml_enabled}

#### `SAML_ACS_URL` {#saml_acs_url}

#### `SAML_ISSUER` {#saml_issuer}

#### `SAML_IDP_SSO_TARGET_URL` {#saml_idp_sso_target_url}

#### `SAML_IDP_CERT` {#saml_idp_cert}

#### `SAML_IDP_CERT_FINGERPRINT` {#saml_idp_cert_fingerprint}

#### `SAML_NAME_IDENTIFIER_FORMAT` {#saml_name_identifier_format}

#### `SAML_CERT` {#saml_cert}

#### `SAML_PRIVATE_KEY` {#saml_private_key}

#### `SAML_SECURITY_WANT_ASSERTION_SIGNED` {#saml_security_want_assertion_signed}

#### `SAML_SECURITY_WANT_ASSERTION_ENCRYPTED` {#saml_security_want_assertion_encrypted}

#### `SAML_SECURITY_ASSUME_EMAIL_IS_VERIFIED` {#saml_security_assume_email_is_verified}

#### `SAML_ATTRIBUTES_STATEMENTS_UID` {#saml_attributes_statements_uid}

#### `SAML_ATTRIBUTES_STATEMENTS_EMAIL` {#saml_attributes_statements_email}

#### `SAML_ATTRIBUTES_STATEMENTS_FULL_NAME` {#saml_attributes_statements_full_name}

#### `SAML_ATTRIBUTES_STATEMENTS_FIRST_NAME` {#saml_attributes_statements_first_name}

#### `SAML_ATTRIBUTES_STATEMENTS_LAST_NAME` {#saml_attributes_statements_last_name}

#### `SAML_UID_ATTRIBUTE` {#saml_uid_attribute}

#### `SAML_ATTRIBUTES_STATEMENTS_VERIFIED` {#saml_attributes_statements_verified}

#### `SAML_ATTRIBUTES_STATEMENTS_VERIFIED_EMAIL` {#saml_attributes_statements_verified_email}

## 숨김 서비스 {#hidden-services}

### TOR {#tor}

{{< page-ref page="admin/optional/tor" >}}

#### `http_proxy` {#http_proxy}

#### `http_hidden_proxy` {#http_hidden_proxy}

#### `ALLOW_ACCESS_TO_HIDDEN_SERVICE` {#allow_access_to_hidden_service}

## 제한 {#limits}

### 스팸 및 악용 방지 {#anti-spam--abuse}

#### `HCAPTCHA_SITE_KEY` {#hcaptcha_site_key}
#### `HCAPTCHA_SECRET_KEY` {#hcaptcha_secret_key}

설정하면 가입 확인 페이지에 CAPTCHA가 표시됩니다. [CAPTCHA](https://docs.joinmastodon.org/admin/optional/captcha/)를 확인합니다.

### 이메일 도메인 {#email-domains}

#### `EMAIL_DOMAIN_ALLOWLIST` {#email_domain_allowlist}

설정하면 지정한 도메인의 이메일 **이외에는** 가입할 수 없습니다. `foo.com|bar.com`처럼 파이프로 구분합니다.

#### `EMAIL_DOMAIN_DENYLIST` {{%deprecated%}} {#email_domain_denylist-deprecated}

설정하면 지정한 도메인의 이메일로 가입할 수 없습니다. `foo.com|bar.com`처럼 파이프로 구분합니다.

{{< hint style="warning" >}}
이 옵션은 더 이상 권장하지 않습니다. 관리 인터페이스나 `tootctl` 명령줄에서 이메일 도메인을 동적으로 차단할 수 있습니다.
{{</ hint >}}

### 세션 {#sessions}

#### `MAX_SESSION_ACTIVATIONS` {#max_session_activations}

사용자당 허용할 최대 브라우저 세션 수이며 기본값은 10입니다. 새 세션 생성으로 한도를 초과하면 가장 오래된 세션을 삭제하여 해당 세션에서 로그아웃됩니다.

### 홈 피드 {#home-feeds}

#### `USER_ACTIVE_DAYS` {#user_active_days}

마스토돈은 홈 피드를 RAM, 구체적으로 Redis 데이터베이스에 저장합니다. 접근과 갱신이 매우 빠르지만 사용하지 않는 피드를 계속 보관하거나 접근하지 않을 피드에 새 항목을 넣는 데 자원을 쓰는 것은 바람직하지 않습니다. 따라서 한동안 접속하지 않은 사용자의 홈 피드를 주기적으로 지우고 다시 접속하면 데이터베이스에서 재생성합니다. 기본적으로 최근 `7`일 이내에 접속한 사용자를 활성 사용자로 간주합니다.

홈 피드 재생성에는 연산 비용이 많이 듭니다. 사용자는 3일마다 접속하는데 `USER_ACTIVE_DAYS`가 2라서 Sidekiq가 계속 재생성한다면 값을 늘리는 것이 좋습니다.

{{< hint style="info" >}}
이 설정은 월간 활성 사용자 수 같은 통계에서 활성 사용자를 판단하는 기준과는 관계가 없습니다.
{{</ hint >}}

### 모든 답글 가져오기 {#fetch-all-replies}

**버전 이력:**\
4.4.0 - 추가됨\
4.5.0 - 제거됨

{{< hint style="danger" >}}
4.5에서는 모든 답글 가져오기가 무조건 활성화되었습니다. 따라서 관련 설정 변수는 제거되었습니다.
{{< /hint >}}

모든 답글 가져오기는 각 게시물의 [답글 컬렉션](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-replies)을 재귀적으로 요청한 뒤 게시물 자체를 요청하여 펼쳐진 게시물 아래의 답글 트리를 가져옵니다. 게시물의 `context` 요청으로 실행되므로 웹 인터페이스와 외부 앱 모두에서 실행됩니다.

구체적으로 다음 조건에서 게시물을 가져옵니다.
- 원격 서버가 [페이지네이션](https://www.w3.org/TR/activitystreams-core/#paging)을 포함한 [ActivityPub/ActivityStreams 컬렉션](https://www.w3.org/TR/activitypub/#collections)을 올바르게 구현합니다.
- 원격 서버가 기본 서버 행위자에서 답글 컬렉션을 요청하도록 허용합니다.
- 다음 중 하나입니다.
  - 일치하는 URI의 게시물이 데이터베이스에 없거나,
  - `FETCH_REPLIES_COOLDOWN_MINUTES` 동안 게시물을 가져오지 않았으며,
  - 게시물이 생성된 지 `FETCH_REPLIES_INITIAL_WAIT_MINUTES`보다 오래 지났습니다.

모든 공개 범위 체계는 그대로 적용됩니다. 가져오는 서버가 올바르게 동작한다면 게시물 작성자에게 차단된 계정 등에는 가져온 답글이 보이지 않습니다.

가져올 때 로컬 팔로워가 없는 계정의 게시물은 상위 게시물의 `replies` 컬렉션에 없더라도 다시 가져옵니다. 로컬 팔로워가 없으면 가져오는 서버가 `Delete` 활동을 받지 못했을 것이므로, 재조회 시 원격 서버가 `404`를 반환하면 이전에 가져온 게시물을 제거합니다.

서버 규모에 따라 답글 가져오기의 필요성과 비용이 크게 달라질 수 있으므로, 관리자는 이 설정으로 자원 사용량을 조정할 수 있습니다. 작은 서버는 한도를 높이고 큰 서버는 낮추거나 재시도 대기 간격을 늘리는 것이 좋을 수 있습니다.

#### `FETCH_REPLIES_ENABLED` {{%removed%}} {#fetch_replies_enabled-removed}

**기본값:** `false`

게시물 상세 보기를 펼칠 때 추가 답글 가져오기를 켜거나 끕니다.

#### `FETCH_REPLIES_COOLDOWN_MINUTES` {{%removed%}} {#fetch_replies_cooldown_minutes-removed}

**기본값:** `15`

게시물과 답글을 마지막으로 가져온 후 다시 가져오기까지 기다릴 시간입니다.

이는 게시물별로 적용됩니다. 상위 게시물 가져오기를 실행한 뒤 답글 트리의 하위 게시물에서도 실행하더라도 같은 게시물을 두 번 가져오지 않습니다.

#### `FETCH_REPLIES_INITIAL_WAIT_MINUTES` {{%removed%}} {#fetch_replies_initial_wait_minutes-removed}

**기본값:** `5`

게시물 생성 후 답글을 가져올 수 있을 때까지 기다릴 시간입니다.

#### `FETCH_REPLIES_MAX_GLOBAL` {{%removed%}} {#fetch_replies_max_global-removed}

**기본값:** `1000`

한 번의 가져오기에서 전체 답글 트리를 재귀적으로 탐색하며 가져올 최대 답글 수입니다.

#### `FETCH_REPLIES_MAX_SINGLE` {{%removed%}} {#fetch_replies_max_single-removed}

**기본값:** `500`

답글 트리 안에서 단일 게시물에 대해 가져올 최대 답글 수입니다.

#### `FETCH_REPLIES_MAX_PAGES` {{%removed%}} {#fetch_replies_max_pages-removed}

**기본값:** `500`

한 번의 가져오기에서 전체 답글 트리로부터 가져올 ActivityPub `Collection` 페이지의 총수입니다.


## 기타 {#other}

### 데이터베이스 마이그레이션 {#migrations}

#### `SKIP_POST_DEPLOYMENT_MIGRATIONS` {#skip_post_deployment_migrations}

이 변수는 `rake db:migrate` 실행 시에만 효과가 있으며 마스토돈 업그레이드 과정에 매우 특화되어 있습니다. 데이터베이스 마이그레이션에는 새 코드를 배포하여 실행하기 전의 작업과 그 이후의 작업 두 종류가 있습니다. 기본적으로 모두 실행합니다. 마이그레이션 전에 모든 마스토돈 프로세스를 종료한다면 차이가 없습니다. 이 변수는 중단 없는 업그레이드에 의미가 있습니다. 특정 버전의 업그레이드 지침에서 사용 여부를 확인할 수 있습니다.

### 데이터베이스 암호화 지원 {#db-encryption-support}

다음 세 환경 변수를 설정해야 마스토돈이 일부 데이터베이스 속성을
암호화하고 복호화하는 데 사용하는 Rails의 Active Record
Encryption 기능을 활성화할 수 있습니다.

이 변수의 값을 생성하려면 다음을 실행합니다.
`bundle exec rake db:encryption:init`

- `ACTIVE_RECORD_ENCRYPTION_PRIMARY_KEY`
- `ACTIVE_RECORD_ENCRYPTION_DETERMINISTIC_KEY`
- `ACTIVE_RECORD_ENCRYPTION_KEY_DERIVATION_SALT`

**버전 이력:**\
4.3.0 - 추가됨

### StatsD(4.3.0에서 제거됨) {#statsd}

{{< hint style="danger" >}}
StatsD 지원은 마스토돈 4.2.0에서 사용 중단 예정으로 지정되었고 4.3.0에서 완전히 제거되었습니다.
{{< /hint >}}

#### `STATSD_ADDR` {#statsd_addr}

설정하면 호스트명과 포트로 식별되는 StatsD에 일부 이벤트와 지표를 기록합니다.

예시 값: `localhost:8125`

#### `STATSD_NAMESPACE` {#statsd_namespace}

설정하면 모든 StatsD 키 앞에 이 값을 붙입니다. 기본값은 `RAILS_ENV`가 `production`이면 `Mastodon.production`, `development`이면 `Mastodon.development` 등입니다.

#### `STATSD_SIDEKIQ` {#statsd_sidekiq}

`true`로 설정하면 일부 Sidekiq 지표를 StatsD에 기록합니다. 기본값은 `false`입니다.

### 미분류 또는 미정렬 {#uncategorized-or-unsorted}

#### `BUNDLE_GEMFILE` {#bundle_gemfile}

bundler(Ruby 패키지 관리자)에 애플리케이션 빌드 방법을 지시합니다.

#### `DEEPL_API_KEY` {#deepl_api_key}

DeepL을 사용할 때 번역 서비스 접근에 사용하는 API 키입니다.

#### `DEEPL_PLAN` {#deepl_plan}

DeepL을 사용할 때 구성된 요금제 이름입니다.

**버전 이력:**\
4.2.6 - 추가됨

#### `LIBRE_TRANSLATE_ENDPOINT` {#libre_translate_endpoint}

Libre Translate 서비스가 실행 중인 엔드포인트 URL입니다. /translate 경로는 포함하지 않습니다.

예시 값: `http://127.0.0.1:5544`

#### `LIBRE_TRANSLATE_API_KEY` {#libre_translate_api_key}

Libre Translate를 사용할 때 번역 서비스 접근에 사용하는 API 키입니다.

#### `GITHUB_REPOSITORY` {#github_repository}

애플리케이션 코드가 있는 소스 저장소입니다. 기본값은 `mastodon/mastodon`입니다.

#### `SOURCE_BASE_URL` {#source_base_url}

기본값은 `https://github.com/$GITHUB_REPOSITORY`입니다.

#### `FFMPEG_BINARY` {#ffmpeg_binary}

기본값은 빈 값이며 활성화되지 않습니다.

#### `LOCAL_HTTPS` {#local_https}

운영 환경에서는 HTTPS가 항상 활성화됩니다. 다른 환경에서는 이 설정값이 `true`이면 HTTPS를 활성화합니다.

#### `PATH` {#path}

#### `MAX_FOLLOWS_THRESHOLD` {#max_follows_threshold}

계정의 인가되지 않은 팔로우 또는 팔로우 요청 수를 제한합니다. 기본값은 `7500`입니다.

#### `MAX_FOLLOWS_RATIO` {#max_follows_ratio}

인가된 팔로우 수가 `MAX_FOLLOWS_THRESHOLD`를 초과하는 계정의 새 인가되지 않은 팔로우를 팔로워 수에 이 비율을 곱한 값으로 제한합니다. 기본값은 `1.1`입니다.

#### `IP_RETENTION_PERIOD` {#ip_retention_period}

사용자 레코드와 연결된 IP 주소 데이터를 데이터베이스에 보관할 기간입니다. 기본값은 `31536000`(1년)입니다.

#### `SESSION_RETENTION_PERIOD` {#session_retention_period}

활동 없이 인증 세션의 유효성을 유지할 기간입니다. 기본값은 `31536000`(1년)입니다.

#### `BACKTRACE` {#backtrace}

Rails 프레임워크 코드까지 역추적하려면 `1`로 설정합니다.

#### `EMAIL_DOMAIN_LISTS_APPLY_AFTER_CONFIRMATION` {#email_domain_lists_apply_after_confirmation}

`true`로 설정하면 확인 후 사용자 이메일 주소를 차단 목록과 대조합니다. 기본적으로는 확인 전에만 수행합니다.

#### `DISABLE_FOLLOWERS_SYNCHRONIZATION` {#disable_followers_synchronization}

`true`로 설정하면 일부 이벤트 후 실행되는 팔로워 동기화를 비활성화합니다.

#### `MAX_REQUEST_POOL_SIZE` {#max_request_pool_size}

다른 서버와 상호작용하는 HTTP 요청 풀의 최대 크기를 제한합니다. 기본값은 `512`입니다.

#### `GITHUB_API_TOKEN` {#github_api_token}

GitHub 커밋 내역에서 AUTHORS.md를 생성하는 rake 작업에 사용합니다.
