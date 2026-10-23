---
title: 오류 해결하기
menu:
  docs:
    weight: 120
    parent: admin
    identifier: admin-troubleshooting
---

## **IPv4/IPv6 충돌** {#ipv4ipv6-conflicts}

DNS에 IPv6가 있지만 올바른 IP나 방화벽 설정이 적용되지 않으면 시간 초과 같은 성능 문제나 연합우주 관련 작업 실패가 발생할 수 있습니다. DNS 영역에 'AAAA' 레코드가 있다면 듀얼 스택이 완전히 작동하는지 확인합니다.

## **문제가 발생했다는 오류 페이지가 보입니다. 원인을 어떻게 찾나요?** {#i-see-an-error-page-that-says-something-went-wrong-how-do-i-find-out-whats-wrong}

스택 추적이 포함된 모든 오류 메시지는 시스템 로그에 기록됩니다. systemd를 사용한다면 `journalctl -u mastodon-web`으로 각 systemd 서비스의 로그를 볼 수 있습니다. 올바른 서비스 이름으로 바꿉니다. Docker도 비슷하게 `docker logs mastodon_web_1`을 사용하며 올바른 컨테이너 이름으로 바꿉니다.

서버 측 오류의 자세한 내용은 공개적으로 _절대_ 표시하지 않습니다. 내부 구성 모습을 드러내 공격자가 침입하거나 시스템을 더 효과적으로 악용할 단서를 줄 수 있기 때문입니다.

마스토돈 웹 서버의 각 응답에는 고유한 요청 ID 헤더가 있으며 로그에도 같은 ID가 기록됩니다. 오류 페이지의 헤더를 조사하면 로그에서 해당 스택 추적을 쉽게 찾을 수 있습니다.

## **로그에 정보가 별로 없습니다. 추가 로그나 디버깅 정보를 어떻게 활성화하나요?** {#i}

마스토돈은 12요소 애플리케이션으로서 일반적인 Rails의 `#{Rails.root}/log/#{Rails.env}.log`가 아닌 `stdout`에 로그를 남깁니다. 콘솔을 확인하세요!

기본 로그 수준은 `info`입니다. 더 많은 디버깅 메시지를 보려면 `.env.production` 파일에서 해당 서비스의 로그 수준을 높일 수 있습니다.

- **웹/Sidekiq:** `RAILS_LOG_LEVEL`을 `debug`로 설정한 다음 문제를 조사하는 서비스를 재시작합니다.
- **스트리밍:** `LOG_LEVEL`을 `silly`로 설정한 다음 문제를 조사하는 서비스를 재시작합니다.

이 옵션에서 사용할 다른 로그 수준은 [환경 설정](https://docs.joinmastodon.org/admin/config) 페이지에서 확인할 수 있습니다.

`debug`와 `silly` 수준은 매우 많은 로그를 남길 수 있으므로 문제 해결을 마치면 더 낮은 수준으로 되돌려야 합니다.

## **새 버전으로 업그레이드한 뒤 일부 페이지의 요소에 스타일이 없는 것처럼 이상하게 보입니다. 왜 그런가요?** {#after-an-upgrade-to-a-newer-version-some-pages-look-weird-like-they-have-unstyled-elements-why}

오래된 스타일시트와 스크립트를 제공하는 것 같으므로 업그레이드 후 `RAILS_ENV=production bin/rails assets:precompile`을 실행하고 마스토돈 웹 프로세스를 재시작했는지 확인합니다. 사전 컴파일이 실패하면 다른 컴퓨터에서 에셋을 사전 컴파일하고 `public/packs` 디렉터리를 복사할 수 있습니다.

## **새 버전으로 업그레이드한 뒤 일부 요청이 실패하며 로그에 열이나 테이블이 없다는 오류가 보입니다. 왜 그런가요?** {#after-an-upgrade-to-a-newer-version-some-requests-fail-and-the-logs-show-error-messages-about-missing-columns-or-tables-why}

마스토돈 코드가 더 새롭거나 오래된 데이터베이스 스키마에 접근하는 것 같으므로 업그레이드 후 `RAILS_ENV=production bin/rails db:migrate`를 실행했는지 확인합니다. PgBouncer를 사용한다면 이 명령만큼은 PostgreSQL에 직접 연결해야 합니다. PgBouncer는 마이그레이션에 사용되는 종류의 테이블 잠금을 지원하지 않습니다.

## **`tootctl`이나 `rake`/`rails` 명령을 실행하면 초기화되지 않은 상수 오류만 나옵니다. 무엇이 문제인가요?** {#i-am-trying-to-run-a}

명령 앞에 `RAILS_ENV=production`으로 올바른 환경을 지정했는지 확인합니다. 기본값은 개발 환경이므로 코드가 개발 관련 gem을 불러오려고 합니다. 하지만 운영 환경에서는 이 gem들을 설치하지 않기 때문에 오류가 발생합니다.

## **`RAILS_ENV=production bundle exec rails assets:precompile` 실행 중 컴파일 오류가 발생했지만 추가 정보가 없습니다. 어떻게 해결하나요?** {#i-encountered-a-compilation-error-while-executing}

대개 에셋 컴파일 중 서버 메모리가 부족해졌기 때문입니다. 스왑 파일을 사용하거나 스왑 공간을 늘려 메모리 용량을 늘립니다. `RAILS_ENV=production bundle exec rake tmp:cache:clear`로 캐시를 지운 다음 `RAILS_ENV=production bundle exec rails assets:precompile`로 다시 컴파일합니다. 컴파일 오류 후 캐시를 지우지 않으면 “Everything's OK”라고 표시하면서 에셋은 그대로 남을 수 있습니다.

## **`Read-only file system @ dir_s_mkdir` 오류가 발생합니다. 왜 그런가요?** {#i-am-getting-this-error}

기본적으로 마스토돈은 [systemd의 샌드박스 기능](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#Sandboxing)으로 `/home/mastodon` 밖에 쓰지 못하도록 합니다. 다른 위치에 설치했다면 `mastodon-sidekiq`와 `mastodon-web`이 사용자 정의 디렉터리에 쓰도록 허용해야 할 수 있습니다.
1. `/etc/systemd/system/mastodon-sidekiq.service`와 `/etc/systemd/system/mastodon-web.service` 파일에 `ReadWritePaths` 매개변수를 추가합니다. 예: `ReadWritePaths=/example/mastodon/live`
2. `systemctl stop mastodon-sidekiq mastodon-web`을 실행합니다.
3. `systemctl daemon-reload`를 실행합니다.
4. `systemctl start mastodon-sidekiq mastodon-web`을 실행합니다.


## 마스토돈 웹 UI에는 오류 페이지만 보이지만 API는 작동합니다 {#the-mastodon-webui-just-displays-an-error-page-but-the-api-works}

예를 들어 다음 명령을 실행할 때

```bash
RAILS_ENV=production bundle exec rails assets:precompile
```

유효하게 작동하는 NodeJS 환경이 없으면 이런 일이 생깁니다. 경우에 따라 `yarn install --immutable`을 아직 실행하지 않아 웹 파일이 올바른 디렉터리에 설치되지 않은 상태일 수 있습니다. `assets::precompile`을 다시 실행하는 것만으로는 해결되지 않을 수 있습니다. 다음과 같이 해결합니다.

```bash
cd live
yarn install --immutable
RAILS_ENV=production bundle exec rake tmp:cache:clear
RAILS_ENV=production bundle exec rails assets:precompile
```

그런 다음 `mastodon-web` 서비스를 재시작합니다.

```bash
sudo systemctl restart mastodon-web.service
```


## 마스토돈 업데이트 중 Postgres 데이터베이스 마이그레이션이 실패합니다 {#postgres-database-migrations-fail-during-a-mastodon-update}

다음과 같은 오류 메시지가 발생한다면,

```text
WARNING:  you don't own a lock of type ExclusiveLock                                           
bin/rails aborted!                                                                             
ActiveRecord::ConcurrentMigrationError:  (ActiveRecord::ConcurrentMigrationError)              
                                                                                                                                                                                               
Failed to release advisory lock 
```

PostgreSQL 앞에 pg_bouncer를 실행하면서 기본 pg_bouncer 포트 대신 PostgreSQL 포트를 수동으로 지정하는 것을 잊었을 가능성이 높습니다. 마이그레이션 명령이 작동하도록 `DB_PORT`를 추가합니다. 예:

```bash
RAILS_ENV=production DB_PORT=5432 bundle exec rails db:migrate
```

배포 전 마이그레이션과 배포 후 마이그레이션 모두에 적용해야 합니다. [마스토돈 확장 - pg_bouncer 절](https://docs.joinmastodon.org/admin/scaling/)도 확인합니다.
