---
title: 서버 규모 확장하기
descriptions: Optimizations that can be done to serve more users.
menu:
  docs:
    weight: 100
    parent: admin
---

## 동시성 관리 {#concurrency}

마스토돈에는 세 가지 유형의 프로세스가 있습니다.

- 웹(Puma)
- 스트리밍 API
- 백그라운드 처리(Sidekiq)

### 웹(Puma) {#web}

웹 프로세스는 애플리케이션 대부분의 짧은 HTTP 요청을 처리합니다. 다음 환경 변수로 제어합니다.

- `WEB_CONCURRENCY`는 작업자 프로세스 수를 제어합니다.
- `MAX_THREADS`는 프로세스당 스레드 수를 제어합니다.

스레드는 부모 프로세스의 메모리를 공유합니다. 서로 다른 프로세스는 쓰기 시 복사로 일부 메모리를 공유하지만 자체 메모리를 할당합니다. 스레드를 많이 늘리면 CPU가 먼저 한계에 도달하고, 프로세스를 많이 늘리면 RAM이 먼저 한계에 도달합니다.

이 값은 동시에 처리할 수 있는 HTTP 요청 수에 영향을 줍니다.

처리량 측면에서는 스레드보다 프로세스를 늘리는 편이 좋습니다.

### 스트리밍 API {#streaming}

스트리밍 API는 클라이언트가 실시간 업데이트를 받는 오래 지속되는 HTTP 및 WebSocket 연결을 처리합니다. 다음 환경 변수로 제어합니다.

- `STREAMING_API_BASE_URL`은 스트리밍 API의 기본 URL을 제어합니다.
- `PORT`는 스트리밍 서버가 수신할 포트를 제어하며 기본값은 4000입니다. `BIND`와 `SOCKET` 환경 변수도 사용할 수 있습니다.
- 추가로 공통 [데이터베이스](/admin/config#postgresql) 및 [Redis](/admin/config#redis) 환경 변수를 사용합니다.

원한다면 `STREAMING_API_BASE_URL`을 설정하여 스트리밍 API에 다른 하위 도메인을 사용할 수 있습니다. 그러면 스트리밍용 로드 밸런서와 웹/API 요청용 로드 밸런서를 따로 둘 수 있습니다. 다만 애플리케이션도 웹 API와 같은 호스트에서 제공된다고 가정하지 말고 [서버 엔드포인트](/methods/instance/#v2)에서 스트리밍 URL을 올바르게 요청해야 합니다.

스트리밍 서버 프로세스 하나로 상당한 연결 수와 처리량을 감당할 수 있지만, 하나로 서버 부하를 감당하지 못한다면 각 프로세스의 `PORT`를 다르게 하여 여러 프로세스를 실행하고 nginx로 트래픽을 분산할 수 있습니다. 예를 들어 계정 약 50,000개와 월간 활성 계정 10,000~20,000개인 커뮤니티에서는 평균적으로 약 800~1,200개의 스트리밍 연결이 동시에 이루어집니다.

스트리밍 서버는 현재 부하를 파악하는 데 도움이 되는 여러 지표를 제공하는 [Prometheus](https://prometheus.io/) 엔드포인트도 `/metrics`에 노출합니다. 주요 지표는 다음과 같습니다.

- `mastodon_streaming_connected_clients`: 연결된 클라이언트 수이며 클라이언트 유형(websocket 또는 eventsource) 태그가 붙습니다.
- `mastodon_streaming_connected_channels`: 현재 구독 중인 “채널” 수입니다. 현재 내부 “시스템” 채널의 동작 방식 때문에 연결된 클라이언트 수보다 훨씬 큽니다.
- `mastodon_streaming_messages_sent_total`: 마지막 재시작 이후 클라이언트에게 보낸 총 메시지 수입니다.
- `mastodon_streaming_redis_messages_received_total`: Redis pubsub에서 받은 메시지 수이며 [Redis 직접 모니터링](https://sysdig.com/blog/redis-prometheus/)을 보완하기 위한 지표입니다.

Prometheus로 모니터링할 때는 nginx 엔드포인트 대신 개별 스트리밍 서버를 각각 모니터링해야 합니다. nginx 요청은 임의의 스트리밍 서버로 라우팅되어 개별 서버 추적보다 지표의 유용성이 낮아지기 때문입니다.

{{< hint style="info" >}}
스트리밍 서버 프로세스를 많이 실행할수록 PostgreSQL 데이터베이스 연결도 많이 소비하므로 아래에 설명한 PgBouncer를 사용하는 것이 좋습니다.
{{< /hint >}}

`PORT` 4000, 4001, 4002의 서로 다른 세 프로세스로 트래픽을 라우팅하는 nginx 설정 예제는 다음과 같습니다.

```nginx
upstream streaming {
    least_conn;
    server 127.0.0.1:4000 fail_timeout=0;
    server 127.0.0.1:4001 fail_timeout=0;
    server 127.0.0.1:4002 fail_timeout=0;
}
```

배포된 systemd 파일을 사용한다면 다음 명령으로 여러 스트리밍 서버를 시작할 수 있습니다.

```bash
$ sudo systemctl start mastodon-streaming@4000.service
$ sudo systemctl start mastodon-streaming@4001.service
$ sudo systemctl start mastodon-streaming@4002.service
```

기본적으로 `sudo systemctl start mastodon-streaming`은 4000번 포트의 프로세스 하나만 시작하며, `sudo systemctl start mastodon-streaming@4000.service`와 같습니다.

{{< hint style="warning" >}}
이전 마스토돈 버전에는 스트리밍 서버가 여러 작업자 프로세스를 시작하고 Node.js로 부하를 분산하는 클러스터링을 사용하게 하는 `STREAMING_CLUSTER_NUM` 환경 변수가 있었습니다.

이 변수는 다른 설정과 상호작용하여 특히 데이터베이스 연결과 CPU 자원의 용량 계획을 어렵게 했습니다. 기본적으로 스트리밍 서버가 모든 CPU의 자원을 소비하여 같은 서버의 다른 소프트웨어와 자원 경합이 생길 수 있었습니다. 또 클러스터 작업자 프로세스마다 연결 풀을 열기 때문에 `STREAMING_CLUSTER_NUM`을 잘못 설정하면 데이터베이스 연결이 소진되는 문제도 흔했습니다. 예를 들어 `STREAMING_CLUSTER_NUM`이 `5`이고 `DB_POOL`이 `10`이면 최대 50개의 데이터베이스 연결을 소비할 수 있었습니다.

이제 단일 스트리밍 서버 프로세스는 최대 `DB_POOL`개의 PostgreSQL 연결만 사용하며 스트리밍 서버를 더 실행하여 확장합니다.
{{< /hint >}}

### 백그라운드 처리(Sidekiq) {#sidekiq}

마스토돈의 많은 작업은 HTTP 요청을 빠르게 유지하고 요청 중단이 작업 실행에 영향을 주지 않도록 백그라운드 처리에 위임됩니다. Sidekiq는 스레드 수를 설정할 수 있는 단일 프로세스입니다.

#### 스레드 수 {#sidekiq-threads}

웹 프로세스의 스레드 수는 최종 사용자에 대한 마스토돈 서버의 응답성에 영향을 주지만, 백그라운드 처리에 할당된 스레드 수는 게시물이 작성자로부터 다른 사람에게 전달되는 속도와 이메일 전송 시점 등에 영향을 줍니다.

스레드 수는 환경 변수가 아니라 Sidekiq 실행 시 명령줄 인수로 조절합니다. 예:

```bash
bundle exec sidekiq -c 15
```

이 명령은 스레드 15개로 Sidekiq를 시작합니다. 각 스레드는 데이터베이스 연결 하나가 필요하므로 큰 데이터베이스 풀이 필요합니다. 풀 크기는 `DB_POOL` 환경 변수로 관리하며 최소한 스레드 수 이상으로 설정해야 합니다.

#### 큐 {#sidekiq-queues}

Sidekiq는 중요도가 다른 작업에 서로 다른 큐를 사용합니다. 중요도는 해당 큐가 작동하지 않을 때 서버의 로컬 사용자 경험에 미치는 영향으로 정의합니다. 중요도가 높은 순서로 나열하면 다음과 같습니다.

`default`
: 로컬 사용자에게 영향을 주는 모든 작업입니다.

`push`
: 다른 서버로 페이로드를 전달합니다.

`ingress`
: 들어오는 원격 활동입니다. 서버 부하가 높아도 로컬 사용자가 자신의 게시물을 볼 수 있도록 기본 큐보다 우선순위가 낮습니다.

`mailers`
: 이메일을 배달합니다.

`pull`
: 가져오기, 백업, 스레드 조회, 사용자 삭제, 답글 전달 등 우선순위가 낮은 작업입니다.

`scheduler`
: 인기 해시태그 갱신과 로그 정리 같은 주기적 작업을 처리합니다.

`fasp`
: 외부 서비스를 제공하는 서버와의 <abbr title="연합우주 보조 서비스 제공자">FASP</abbr> 상호작용을 관리합니다.

기본 큐와 우선순위는 [config/sidekiq.yml](https://github.com/mastodon/mastodon/blob/main/config/sidekiq.yml)에 저장되지만 Sidekiq의 명령줄 실행으로 덮어쓸 수 있습니다. 예:

```bash
bundle exec sidekiq -q default
```

이 명령은 `default` 큐만 실행합니다.

Sidekiq는 첫 큐에 작업이 있는지 먼저 확인하고 없으면 다음 큐를 확인합니다. 따라서 첫 큐가 가득 차면 다른 큐의 작업이 지연될 수 있습니다.

각 큐에 서로 다른 Sidekiq 프로세스를 시작하면 실제 병렬 실행을 보장할 수 있습니다. 예를 들어 인수가 다른 여러 Sidekiq systemd 서비스를 만들 수 있습니다.

{{< hint style="warning" >}}
작업을 효율적으로 처리하는 데 필요한 만큼 Sidekiq 프로세스와 스레드를 실행할 수 있지만, `scheduler` 큐는 동시에 둘 이상의 Sidekiq 프로세스에서 실행해서는 안 됩니다.
{{< /hint >}}

## PgBouncer를 사용한 트랜잭션 풀링 {#pgbouncer}

### PgBouncer가 필요한 이유 {#pgbouncer-why}

가용 PostgreSQL 연결(기본값 100개)이 부족해지기 시작한다면 PgBouncer가 좋은 해결책일 수 있습니다. 이 문서는 흔한 함정과 마스토돈에 적합한 기본 설정을 설명합니다.

마스토돈에서 `DevOps` 권한이 있는 역할은 관리 화면의 PgHero 링크를 통해 PostgreSQL 연결의 현재 사용량을 모니터링할 수 있습니다. 보통 열린 연결 수는 Puma, Sidekiq, 스트리밍 API의 전체 스레드 수를 합친 것과 같습니다.

PgHero의 “Query Stats”를 활성화하려면 [쿼리 통계 안내](https://github.com/ankane/pghero/blob/master/guides/Query-Stats.md)를 검토하고 PostgreSQL에 올바른 권한과 확장이 구성되었는지 확인합니다.

### PgBouncer 설치 {#pgbouncer-install}

Debian과 Ubuntu에서는 다음과 같습니다.

```bash
sudo apt install pgbouncer
```

### PgBouncer 설정 {#pgbouncer-config}

#### 비밀번호 설정 {#pgbouncer-password}

먼저 PostgreSQL의 `mastodon` 사용자가 비밀번호 없이 설정되어 있다면 비밀번호를 설정해야 합니다.

다음과 같이 비밀번호를 재설정할 수 있습니다.

```bash
psql -p 5432 -U mastodon mastodon_production -w
```

그런 다음 다음을 실행합니다. 당연히 “password” 대신 다른 비밀번호를 사용해야 합니다.

```sql
ALTER USER mastodon WITH PASSWORD 'password';
```

그런 다음 `\q`로 종료합니다.

#### userlist.txt 설정 {#pgbouncer-userlist}

`/etc/pgbouncer/userlist.txt`를 편집합니다.

나중에 `pgbouncer.ini`에 사용자와 비밀번호를 지정한다면 `userlist.txt`의 값은 실제 PostgreSQL 역할과 일치할 필요가 _없습니다_. 사용자와 비밀번호를 임의로 정의할 수 있지만 단순하게 실제 자격 증명을 재사용할 수 있습니다. `userlist.txt`에 `mastodon` 사용자를 추가합니다.

```text
"mastodon" "md5d75bb2be2d7086c6148944261a00f605"
```

여기서는 md5 방식을 사용합니다. md5 비밀번호는 `password + username`의 md5sum 앞에 `md5` 문자열을 붙인 것입니다. 예를 들어 비밀번호가 `password`인 사용자 `mastodon`의 해시를 구하려면 다음과 같습니다.

```bash
# ubuntu, debian, etc.
echo -n "passwordmastodon" | md5sum
# macOS, openBSD, etc.
md5 -s "passwordmastodon"
```

그런 다음 결과 앞에 `md5`만 붙입니다.

PgBouncer 관리 데이터베이스에 로그인할 `pgbouncer` 관리자 사용자도 만드는 것이 좋습니다. 다음은 `userlist.txt` 예제입니다.

```text
"mastodon" "md5d75bb2be2d7086c6148944261a00f605"
"pgbouncer" "md5a45753afaca0db833a6f7c7b2864b9d9"
```

두 경우 모두 비밀번호는 `password`입니다.

#### pgbouncer.ini 설정 {#pgbouncer-ini}

`/etc/pgbouncer/pgbouncer.ini`를 편집합니다.

`[databases]` 아래에 연결할 PostgreSQL 데이터베이스를 나열하는 줄을 추가합니다. 여기서는 PgBouncer가 같은 사용자명, 비밀번호, 데이터베이스 이름으로 실제 PostgreSQL 데이터베이스에 연결하게 합니다.

```ini
[databases]
mastodon_production = host=127.0.0.1 port=5432 dbname=mastodon_production user=mastodon password=password
```

`listen_addr`와 `listen_port`는 PgBouncer가 연결을 수락할 주소와 포트를 지정합니다. 기본값이면 충분합니다.

```ini
listen_addr = 127.0.0.1
listen_port = 6432
```

`userlist.txt`에서 md5 형식을 사용한다면 `auth_type`을 `md5`로 설정합니다.

```ini
auth_type = md5
```

`pgbouncer` 사용자가 관리자인지 확인합니다.

```ini
admin_users = pgbouncer
```

마스토돈에는 기본 세션 방식과 다른 풀링 모드가 필요합니다. 구체적으로 트랜잭션 기반 풀링이 필요하며, 트랜잭션 시작 시 PostgreSQL 연결을 설정하고 완료 시 종료합니다. 따라서 `pool_mode`를 `session`에서 `transaction`으로 바꿔야 합니다.

```ini
pool_mode = transaction
```

다음으로 `max_client_conn`은 PgBouncer 자체가 수락할 연결 수를 정의하고, `default_pool_size`는 내부적으로 열 PostgreSQL 연결 수를 제한합니다. PgHero는 PgBouncer를 모르므로 보고되는 연결 수는 `default_pool_size`에 해당합니다.

처음에는 기본값이면 충분하며 나중에 언제든 늘릴 수 있습니다.

```ini
max_client_conn = 100
default_pool_size = 20
```

변경 후 PgBouncer를 다시 불러오거나 재시작하는 것을 잊지 않습니다.

```bash
sudo systemctl reload pgbouncer
```

#### 작동 여부 디버깅 {#pgbouncer-debug}

PostgreSQL에 연결하듯 PgBouncer에도 연결할 수 있어야 합니다.

```bash
psql -p 6432 -U mastodon mastodon_production
```

그런 다음 비밀번호로 로그인합니다.

PgBouncer 로그도 다음과 같이 확인할 수 있습니다.

```bash
tail -f /var/log/postgresql/pgbouncer.log
```

#### 마스토돈이 PgBouncer와 통신하도록 설정 {#pgbouncer-mastodon}

먼저 `.env.production` 파일에서 다음이 설정되어 있는지 확인합니다.

```bash
PREPARED_STATEMENTS=false
```

트랜잭션 기반 풀링을 사용하므로 준비된 구문을 사용할 수 없습니다.

다음으로 마스토돈이 5432(PostgreSQL) 대신 6432(PgBouncer) 포트를 사용하도록 설정하면 준비가 끝납니다.

```bash
DB_HOST=localhost
DB_USER=mastodon
DB_NAME=mastodon_production
DB_PASS=password
DB_PORT=6432
```

{{< hint style="warning" >}}
`db:migrate` 작업에는 PgBouncer를 사용할 수 없지만 쉽게 우회할 수 있습니다. PostgreSQL과 PgBouncer가 같은 호스트에 있다면 작업 호출 시 `RAILS_ENV=production`과 함께 `DB_PORT=5432`를 정의하면 됩니다. 예: `RAILS_ENV=production DB_PORT=5432 bundle exec rails db:migrate`. 호스트도 다르다면 `DB_HOST` 등을 지정할 수 있습니다.
{{< /hint >}}

#### PgBouncer 관리 {#pgbouncer-admin}

재시작하는 가장 쉬운 방법은 다음과 같습니다.

```bash
sudo systemctl restart pgbouncer
```

하지만 PgBouncer 관리자 사용자를 설정했다면 관리자로 연결할 수도 있습니다.

```bash
psql -p 6432 -U pgbouncer pgbouncer
```

그런 다음 다음을 실행합니다.

```sql
RELOAD;
```

이후 `\q`로 종료합니다.

## 캐시용 Redis 분리 {#redis}

Redis는 애플리케이션 전반에서 널리 사용되지만 용도마다 중요도가 다릅니다. 홈 피드, 리스트 피드, Sidekiq 큐, 스트리밍 API는 Redis를 사용하며 잃고 싶지 않은 중요한 데이터입니다. 손실을 감당할 수는 있지만 PostgreSQL 데이터베이스는 그렇지 않으므로 절대 잃지 마세요!

Redis는 휘발성 캐싱에도 사용됩니다. 규모가 커지면서 부하 처리 용량이 걱정된다면 캐싱 전용 Redis 데이터베이스를 따로 할당할 수 있습니다. 환경에 `CACHE_REDIS_URL`을 설정하거나 `CACHE_REDIS_HOST`, `CACHE_REDIS_PORT` 등의 개별 요소를 정의합니다.

지정하지 않은 요소는 캐시 접두사 없는 변수의 값이 기본값이 됩니다.

캐싱용 Redis에서는 재시작 시 데이터 손실이 치명적이지 않으므로 백그라운드 디스크 저장을 끄면 디스크 I/O를 줄일 수 있습니다. 또한 최대 메모리 한도와 키 제거 정책 설정을 고려합니다. 자세한 내용은 [Redis를 LRU 캐시로 사용하기](https://redis.io/topics/lru-cache)를 참고합니다.

## Sidekiq용 Redis 분리 {#redis-sidekiq}

Sidekiq는 Redis로 잠금과 큐를 추적합니다. 일반적으로 성능 향상이 크지는 않지만 일부 서버에서는 Sidekiq용 Redis를 분리하는 것이 도움이 될 수 있습니다.

환경 파일에 `SIDEKIQ_REDIS_URL`이나 `SIDEKIQ_REDIS_HOST`, `SIDEKIQ_REDIS_PORT` 등의 개별 요소를 지정할 수 있습니다. 지정하지 않은 요소는 `SIDEKIQ_` 접두사 없는 변수와 같은 값으로 대체됩니다.

Sidekiq용 Redis를 따로 만드는 것은 비교적 간단합니다.

먼저 기본 redis systemd 서비스를 복사합니다.

```bash
cp /etc/systemd/system/redis.service /etc/systemd/system/redis-sidekiq.service
```

`redis-sidekiq.service` 파일에서 다음 값을 바꿉니다.

```bash
ExecStart=/usr/bin/redis-server /etc/redis/redis-sidekiq.conf --supervised systemd --daemonize no
PIDFile=/run/redis/redis-server-sidekiq.pid
ReadWritePaths=-/var/lib/redis-sidekiq
Alias=redis-sidekiq.service
```

새 Sidekiq Redis를 위해 Redis 설정 파일을 복사합니다.

```bash
cp /etc/redis/redis.conf /etc/redis/redis-sidekiq.conf
```

`redis-sidekiq.conf` 파일에서 다음 값을 바꿉니다.

```bash
port 6479
pidfile /var/run/redis/redis-server-sidekiq.pid
logfile /var/log/redis/redis-server-sidekiq.log
dir /var/lib/redis-sidekiq
```

새 Redis를 시작하기 전에 데이터 디렉터리를 만듭니다.

```bash
mkdir /var/lib/redis-sidekiq
chown redis /var/lib/redis-sidekiq
```

새 Redis를 시작합니다.

```bash
systemctl enable --now redis-sidekiq
```

환경을 업데이트하여 다음 줄을 추가합니다.

```bash
SIDEKIQ_REDIS_URL=redis://127.0.0.1:6479/
```

새 Redis를 사용하도록 마스토돈을 재시작합니다. 웹과 Sidekiq를 모두 재시작해야 합니다. 그렇지 않으면 한쪽이 계속 잘못된 Redis를 사용합니다.

```bash
systemctl restart mastodon-web.service
systemctl restart redis-sidekiq.service
```

## 고가용성을 위한 Redis Sentinel {#redis-sentinel}

앞서 말했듯 Redis는 마스토돈 운영의 핵심 요소입니다. 기본 배포는 Redis 하나를 사용하며 캐시를 설정했다면 여러 개를 사용합니다. 하지만 Redis가 중단되면 마스토돈 서버 전체가 중단될 수도 있습니다. 이를 완화하려면 Redis Sentinel로 Redis를 추적하고 장애 시 클라이언트를 새 주 노드로 자동 연결할 수 있습니다. `REDIS_SENTINELS`에는 현재 마스터 Redis 노드를 확인하기 위해 마스토돈이 통신할 Sentinel의 IP:포트 조합을 쉼표로 구분하여 지정합니다. 연결할 마스터 이름도 `REDIS_SENTINEL_MASTER`에 지정해야 합니다. 기본적으로 Sentinel은 현재 마스터에 1분간 접근할 수 없으면 중단으로 판단하고 새 마스터를 선택하지만 구성에 맞게 조정할 수 있습니다.

Redis를 여러 개 사용한다면 모든 Sentinel 관련 변수에 `CACHE_`와 `SIDEKIQ_` 접두사를 붙인 형태도 사용할 수 있습니다.

Redis Sentinel 자세히 알아보기: https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/

## 읽기 복제본 {#read-replicas}

PostgreSQL 서버의 부하를 줄이려면 핫 스트리밍 복제(읽기 복제본)를 구성할 수 있습니다. [이 안내에서 예제를 확인합니다](https://cloud.google.com/community/tutorials/setting-up-postgres-hot-standby).

### 마스토돈 >= 4.2 {#mastodon--42}

마스토돈은 4.2부터 복제본을 기본 지원합니다. Sidekiq를 포함한 모든 서비스에 같은 설정을 사용할 수 있으며, Rails의 내장 복제본 지원으로 가능한 일부 쿼리를 읽기 전용 복제본에 전달합니다. 복제본이 몇 초 이상 뒤처지면 따라잡을 때까지 쿼리 전송을 중단합니다.

다음 환경 변수로 설정합니다.

```text
REPLICA_DB_HOST
REPLICA_DB_PORT
REPLICA_DB_NAME
REPLICA_DB_USER
REPLICA_DB_PASS
REPLICA_PREPARED_STATEMENTS
REPLICA_DB_TASKS
```

하나의 변수로 모두 설정하려면 `REPLICA_DATABASE_URL`을 사용할 수도 있습니다.

`REPLICA_DB_TASKS=false`는 스키마 관리, 마이그레이션, 초기 데이터 등의 데이터베이스 관리 작업 없이 복제본에 연결합니다. 기본값은 true입니다.

`REPLICA_PREPARED_STATEMENTS`로 선택적으로 `PREPARED_STATEMENTS` 값을 덮어쓸 수 있습니다. `PREPARED_STATEMENTS`가 설정되지 않았다면 기본값은 true입니다.

이제 완료되었습니다. 복제본 서버에 요청이 들어오기 시작할 것입니다!

### 마스토돈 <= 4.1 {#mastodon--41}

4.2 이전 버전에서는 다음 방법으로 복제본을 사용할 수 있습니다.

- 스트리밍 API 서버는 쓰기 작업을 전혀 하지 않으므로 복제본에 직접 연결할 수 있습니다. 다만 원래 데이터베이스 쿼리가 잦지 않아 효과는 작습니다.
- 웹과 Sidekiq 프로세스에서 Makara 드라이버를 사용하여 쓰기는 마스터 데이터베이스로, 읽기는 복제본으로 보냅니다. 아래에서 설명합니다.

{{< hint style="warning" >}}
현재 Sidekiq 프로세스에서는 읽기 복제본을 지원하지 않으며 사용하면 작업 실패와 데이터 손실이 발생합니다.
{{< /hint >}}

웹 프로세스에는 별도의 `config/database.yml` 파일을 사용하고 `production` 절을 다음과 같이 바꿔야 합니다.

```yaml
production:
  <<: *default
  adapter: postgresql_makara
  prepared_statements: false
  makara:
    id: postgres
    sticky: true
    connections:
      - role: master
        blacklist_duration: 0
        url: postgresql://db_user:db_password@db_host:db_port/db_name
      - role: slave
        url: postgresql://db_user:db_password@db_host:db_port/db_name
```

URL이 올바른 PostgreSQL 서버 위치를 가리키는지 확인합니다. 복제본을 여러 개 추가할 수 있습니다. 로컬 PgBouncer가 데이터베이스 이름에 따라 두 서버로 연결하도록 구성할 수도 있습니다. 예를 들어 “mastodon”은 주 서버로, “mastodon_replica”는 복제본으로 보내면 위 파일의 두 URL은 사용자, 비밀번호, 호스트, 포트는 같고 데이터베이스 이름만 다른 로컬 PgBouncer를 가리킵니다. 구성 방법은 다양합니다. Makara의 자세한 내용은 [문서](https://github.com/taskrabbit/makara#databaseyml)를 확인합니다.

{{< hint style="warning" >}}
작업 실패와 데이터 손실을 피하려면 Sidekiq 프로세스를 반드시 원래의 `config/database.yml`로 실행합니다!
{{< /hint >}}

## 웹 로드 밸런서 사용 {#using-a-web-load-balancer}

DigitalOcean, AWS, Hetzner 등의 클라우드 제공자는 하나의 공개 IP 주소로 여러 서버에 네트워크 트래픽을 분산하는 가상 로드 밸런서를 제공합니다.

이런 가상 로드 밸런서 뒤에 여러 웹/Puma 서버를 두도록 확장하면 단일 서버에 사용자 트래픽이 몰릴 위험을 줄여 더 일관된 성능을 제공하고, 유지 관리나 업그레이드 시 중단 시간도 줄일 수 있습니다. 설정 방법은 제공자 문서를 참고하되, 응답하지 않는 서비스로 트래픽이 전달되지 않도록 로드 밸런서가 백엔드 웹/Puma 노드의 상태를 모니터링하게 설정해야 합니다.

이를 위해 다음 엔드포인트를 모니터링할 수 있습니다.

- **웹/Puma:** `/health`
- **스트리밍 API:** `/api/v1/streaming/health`

두 엔드포인트 모두 HTTP 상태 코드 200과 텍스트 `OK`를 반환해야 합니다.

{{< hint style="info" >}}
외부 모니터링 및 알림 유틸리티의 상태 검사에도 이 엔드포인트를 사용할 수 있습니다.
{{< /hint >}}

## 사용자 생성 콘텐츠 보관 {#user-generated-content-retention}

저장 에셋이 무한정 늘지 않도록 **관리** > **콘텐츠 보관** 설정을 검토하고 서버와 사용자에 맞는 값을 설정합니다. 정리 작업은 백그라운드 작업 스케줄러로 실행되며 수동 실행이나 cron 설정이 필요 없습니다.

- 미디어 캐시 보관 설정은 원격 사용자의 미디어를 서버에 캐시할 기간을 제어합니다.
- 사용자 아카이브 보관 기간은 사용자가 생성한 백업을 유지할 기간을 제어합니다.
