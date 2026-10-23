---
title: 새 컴퓨터로 이전하기
description: 아무것도 잃지 않고 마스토돈 설치 환경을 새 서버로 복사합니다.
menu:
  docs:
    weight: 90
    parent: admin
---

때로는 여러 이유로 마스토돈 서버를 다른 컴퓨터로 이전하고 싶을 수 있습니다. 다행히 어렵지는 않지만 일정 시간 중단될 수 있습니다.

{{< hint style="info" >}}
이 안내서는 Ubuntu Server를 기준으로 작성되었으며 다른 구성에서는 차이가 있을 수 있습니다.
{{< /hint >}}

## 기본 단계 {#basic-steps}

1. [운영 환경 안내]({{< relref "install" >}})에 따라 새 마스토돈 서버를 설정합니다. 다만 `mastodon:setup`은 실행하지 않고 PostgreSQL 서비스만 실행한 상태로 둡니다.
2. 이전 서버에서 마스토돈을 중지합니다. 예: `systemctl stop 'mastodon-*.service'`
3. 아래 지침에 따라 PostgreSQL 데이터베이스를 덤프하고 불러옵니다.
4. 아래 지침에 따라 `system/` 파일을 복사합니다. S3를 사용한다면 이 단계는 생략할 수 있습니다.
5. `.env.production` 파일을 복사합니다.
6. Redis 데이터베이스를 저장하고 이전 컴퓨터와 새 컴퓨터 양쪽에서 Redis 서비스를 중지한 다음 `/var/lib/redis/`의 Redis 데이터베이스를 새 서버에 복사합니다.
7. `RAILS_ENV=production bundle exec rails assets:precompile`을 실행하여 마스토돈을 컴파일합니다.
8. 새 서버에서 마스토돈과 Redis를 시작합니다.
9. `RAILS_ENV=production ./bin/tootctl feeds build`를 실행하여 각 사용자의 홈 타임라인을 다시 만듭니다.
10. `RAILS_ENV=production ./bin/tootctl search deploy`를 실행하여 Elasticsearch 인덱스를 다시 만듭니다. Elasticsearch를 사용하지 않는다면 생략할 수 있습니다.
11. DNS 설정이 새 서버를 가리키도록 업데이트합니다.
12. Nginx 설정을 업데이트하거나 복사하고 필요에 따라 LetsEncrypt를 다시 실행합니다.
13. 새 서버를 즐겨 보세요!

## 상세 단계 {#detailed-steps}

### 마스토돈 서비스 중지 {#stop-the-mastodon-services}

```bash
systemctl stop 'mastodon-*.service'
```

### 이전해야 할 데이터 {#what-data-needs-to-be-migrated}

크게 보면 다음 항목을 복사해야 합니다.

* 사용자 업로드 이미지와 동영상이 들어 있는 `~/live/public/system` 디렉터리(S3를 사용한다면 필요 없음)
* PostgreSQL 데이터베이스([pg_dump](https://www.postgresql.org/docs/9.1/static/backup-dump.html) 사용)
* 서버 설정과 비밀 정보가 들어 있는 `~/live/.env.production` 파일
* 처리되지 않은 Sidekiq 작업이 들어 있는 `/var/lib/redis/` 디렉터리의 Redis 데이터베이스

필수는 아니지만 편의를 위해 다음 항목도 복사하는 것이 좋습니다.

* nginx 설정(`/etc/nginx/sites-available/mastodon`)
* 도메인의 SSL 인증서(LetsEncrypt를 사용한다면 `/etc/letsencrypt/live/`)
* 서버 조정 및 사용자 정의가 들어 있을 수 있는 systemd 설정 파일(`/etc/systemd/system/mastodon-*.service`)
* `/etc/pgbouncer`의 PgBouncer 설정(사용하는 경우)

### PostgreSQL 덤프와 불러오기 {#dump-and-load-postgresql}

{{< hint style="info" >}}
시작하기 전에 `pg_dump`와 `pg_restore` 모두 오래 걸릴 수 있다는 점에 유의합니다. 약 15GB 백업 파일에 몇 시간이 걸리기도 합니다. 덤프와 복원 작업만을 위해 [Postgres 성능을 일시적으로 조정](https://stackoverflow.com/a/2095283)할 수 있습니다.
{{< /hint >}}

`mastodon:setup` 대신 `template0` 데이터베이스로 빈 PostgreSQL 데이터베이스를 만듭니다. 이는 [pg_dump 문서의 설명](https://www.postgresql.org/docs/9.1/static/backup-dump.html#BACKUP-DUMP-RESTORE)처럼 PostgreSQL 덤프를 복원할 때 유용합니다.

PostgreSQL 사용자에 비밀번호를 사용한다면 편의를 위해 새 시스템의 `mastodon` 사용자도 이전 시스템과 같은 비밀번호를 사용하도록 설정할 수 있습니다.

```bash
sudo -u postgres psql  
ALTER USER mastodon WITH PASSWORD 'YOUR_PASSWORD';  
\q
```

이전 시스템에서 `mastodon` 사용자로 다음을 실행합니다.

```bash
pg_dump -Fc mastodon_production -f backup.dump
```

`rsync`나 `scp`로 `backup.dump` 파일을 복사합니다. 그런 다음 새 시스템에서 `mastodon` 사용자로 빈 데이터베이스를 만듭니다.

```bash
createdb -T template0 mastodon_production
```

이제 가져옵니다. 복원 성능을 높이려면 -j#의 #을 시스템 CPU 수로 바꿉니다.

```bash
pg_restore -Fc -j# -U mastodon -n public --no-owner --role=mastodon \
  -d mastodon_production backup.dump
```
{{< hint style="info" >}}
새 서버의 사용자명이 `mastodon`이 아니라면 위의 `-U`와 `--role` 값을 모두 변경해야 합니다. 두 서버의 사용자명은 달라도 됩니다.
{{< /hint >}}

### 파일 복사 {#copy-files}

시간이 걸릴 수 있으며 불필요한 재복사를 피하는 것이 좋으므로 `rsync`를 권장합니다. 이전 컴퓨터에서 `mastodon` 사용자로 실행합니다.

```bash
rsync -avz ~/live/public/system/ mastodon@example.com:~/live/public/system/
```

이전 서버의 파일이 바뀌면 다시 실행해야 합니다.

비밀 정보가 포함된 `.env.production` 파일도 복사해야 합니다.

새 컴퓨터에서 Redis가 실행 중이지 않은지 확인합니다. 그렇지 않으면 복원할 덤프 파일을 덮어쓸 수 있습니다. `root` 사용자로 실행합니다.

```bash
systemctl stop redis-server.service
```

이제 Redis 데이터베이스를 복사합니다. 필요하면 데이터베이스 위치를 조정합니다. 이전 컴퓨터에서 `root` 사용자로 실행합니다.

```bash
redis-cli SAVE
systemctl stop redis-server.service
rsync -avz /var/lib/redis/ root@example.com:/var/lib/redis
```

원한다면 nginx, systemd, PgBouncer 설정 파일을 복사하거나 처음부터 다시 작성합니다.

### Certbot {#certbot}

Nginx 설정 파일을 복사하는 것만으로는 letsencrypt를 다시 실행하기에 충분하지 않습니다.

대신 `/etc/nginx/sites-available/mastodon`의 `ssl_certificate`와 `ssl_certificate_key`가 참조하는 인증서 파일을 새 컴퓨터에 복사하고 새 컴퓨터의 nginx 설정에서 경로를 업데이트합니다. letsencrypt 자체의 `live` 폴더를 사용하면 인증서를 다시 생성할 때 오류를 표시하므로 사용하지 않습니다. letsencrypt를 다시 실행하면 어차피 설정을 덮어쓰므로 임시 디렉터리를 사용하면 됩니다.

### 이전 중 {#during-migration}

기존 사용자에게 이전 중임을 알리는 보기 좋은 오류 메시지를 표시하려면 이전 컴퓨터의 `~/live/public/500.html` 페이지를 편집할 수 있습니다.

새 IP 주소를 가리키도록 바꾼 후 DNS가 빨리 전파되도록 하루 정도 전에 DNS TTL을 30~60분처럼 짧게 설정하는 것도 좋습니다.

### 이전 후 {#after-migrating}

mastodon 사용자로 다음 명령을 실행합니다.

```bash
RAILS_ENV=production bundle exec rails assets:precompile  
```

이제 root 사용자로 다음 명령을 실행합니다.

```bash
systemctl daemon-reload
systemctl start redis-server  
systemctl enable --now mastodon-web mastodon-sidekiq mastodon-streaming  
systemctl restart nginx
```

서버가 다시 온라인 상태가 되면 사용자의 홈 피드를 다시 만들 수 있습니다. 사용자 수에 따라 오래 걸릴 수 있습니다.

```bash
RAILS_ENV=production ./bin/tootctl feeds build
```

Elasticsearch를 사용한다면 다음 명령으로 인덱스를 다시 만듭니다. 게시물 수에 따라 오래 걸릴 수 있습니다.

```bash
RAILS_ENV=production ./bin/tootctl search deploy
```

[whatsmydns.net](https://whatsmydns.net/)에서 DNS 전파 진행 상황을 확인할 수 있습니다. 먼저 새 서버를 사용해 보려면 자신의 `/etc/hosts` 파일이 새 서버를 가리키도록 편집하면 됩니다.
