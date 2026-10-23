---
title: 관리자 CLI 사용하기
description: 명령줄에서 실행할 수 있는 tootctl 명령어입니다.
menu:
  docs:
    weight: 60
    parent: admin
---

마스토돈의 명령줄 인터페이스는 마스토돈 루트 디렉터리의 `bin` 안에 있는 `tootctl` 실행 파일입니다. 실행할 때마다 `RAILS_ENV` 환경 변수로 사용할 환경을 지정해야 합니다. 로컬 컴퓨터에서 작업하는 개발자가 아니라면 `RAILS_ENV=production`을 사용해야 합니다. 개발, 테스트, 스테이징 등 다른 환경이 필요 없다고 확신한다면 다음과 같이 `.bashrc`에 추가해 편리하게 사용할 수 있습니다.

```bash
echo "export RAILS_ENV=production" >> ~/.bashrc
```

이렇게 설정하면 매번 명령 앞에 지정할 필요가 없습니다. 그렇지 않다면 마스토돈 코드가 `/home/mastodon/live`에 있다고 가정할 때 보통 다음과 같이 `tootctl`을 호출합니다.

```bash
cd /home/mastodon/live
RAILS_ENV=production bin/tootctl help
```

## 기본 CLI {#base-cli}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/lib/mastodon/cli/base.rb" caption="lib/mastodon/cli/base.rb" >}}


---


### `tootctl self-destruct` {#self-destruct}

알려진 모든 다른 서버에 계정의 `Delete` 활동을 전송하여 이 서버를 연합에서 제거합니다. 다른 서버에 캐시를 거의 남기지 않아 마스토돈 서버 운영을 깔끔하게 종료할 수 있습니다. 이 명령은 항상 대화식으로 실행되며 두 번 확인해야 합니다.

마스토돈 4.3.0 이전에는 이 명령을 실행하면 삭제 작업이 즉시 대기열에 추가됩니다. 4.3.0부터는 `Delete` 활동을 보내는 자체 폐쇄 모드로 전환하는 방법을 출력합니다. 자체 폐쇄 모드에서는 사용자가 로그인하여 데이터를 내려받을 수 있지만 다른 작업은 할 수 없습니다. 이 모드에서 `tootctl self-destruct`를 다시 실행하면 폐쇄 작업의 진행 상황을 출력합니다.

데이터베이스를 비우거나 VPS 전체를 삭제하는 편이 더 빠르므로 로컬 데이터를 실제로 삭제하지는 않습니다. 명령을 실행한 뒤에도 서버를 계속 운영하면 상태 불일치로 오류나 연합 문제가 발생할 수 있습니다.

{{< hint style="danger" >}}
**이 명령의 영향을 정확히 이해한 뒤 실행하세요.** 되돌릴 수 없으며 오래 걸릴 수 있습니다. 명령이 끝나면 서버는 정상적으로 운영할 수 없는 상태가 됩니다. Sidekiq 프로세스가 실행 중이어야 하므로 모든 대기열이 완전히 비워질 때까지 서버를 종료하지 마세요.
{{< /hint >}}

`--dry-run` {{%removed%}}
: 실제 작업 없이 예상 결과만 출력합니다. 4.3.0에서 제거되었습니다.

**버전 이력:**\
2.8.0 - 추가\
4.3.0 - `--dry-run` 제거, 자체 폐쇄 모드 도입


---


### `tootctl --version` {#version}

현재 실행 중인 마스토돈 서버의 버전을 표시합니다.

**버전 이력:**\
2.7.0 - 추가


---


## 계정 CLI {#accounts}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/lib/mastodon/cli/accounts.rb" caption="lib/mastodon/cli/accounts.rb" >}}


---


### `tootctl accounts rotate` {#accounts-rotate}

보안 유지보수의 일환으로 새 RSA 키를 생성하고 전파합니다.

`USERNAME`
: 계정의 로컬 사용자명입니다.

`--all`
: `USERNAME` 대신 지정하여 모든 로컬 계정의 키를 교체할 수 있습니다.

**버전 이력:**\
2.5.0 - 추가


---


### `tootctl accounts create` {#accounts-create}

지정한 `USERNAME`과 `--email`로 새 사용자 계정을 만듭니다.

`USERNAME`
: 새 계정의 로컬 사용자명입니다. {{<required>}}

`--email EMAIL`
: 사용자에게 연결할 이메일 주소입니다. {{<required>}}

`--confirmed`
: 확인 이메일을 보내지 않고 계정을 즉시 활성화합니다.

`--role ROLE`
: [Role]({{< relref "entities/Role" >}})의 `name`을 지정하여 새 계정의 사용자 지정 역할을 설정합니다. 기본 역할은 `Owner`, `Admin`, `Moderator`이며 대소문자를 구분합니다.

`--reattach`
: 계정이 삭제된 뒤 이전 USERNAME을 다시 사용합니다.

`--force`
: 이 `USERNAME`을 가진 기존 계정을 강제로 삭제하고, 방금 삭제한 계정 대신 새 계정을 연결합니다.

**버전 이력:**\
2.6.0 - 추가\
3.5.1 - `--skip-sign-in-token` 제거\
4.0.0 - `--role`은 더 이상 고정된 `user`, `moderator`, `admin` 역할을 받지 않습니다. 대신 사용자 지정 역할의 이름을 지정하며 대소문자를 구분합니다.


---


### `tootctl accounts modify` {#accounts-modify}

사용자 계정의 역할, 이메일, 활성 상태, 승인 상태 또는 2단계 인증 요구 사항을 변경합니다.

`USERNAME`
: 해당 계정의 로컬 사용자명입니다. {{<required>}}

`--role ROLE`
: [Role]({{< relref "entities/Role" >}})의 `name`을 지정하여 기존 계정의 사용자 지정 역할을 설정합니다. 기본 역할은 `Owner`, `Admin`, `Moderator`이며 대소문자를 구분합니다.

`--remove-role`
: 사용자의 현재 역할을 제거합니다.

`--email EMAIL`
: 사용자의 이메일 주소를 `EMAIL`로 변경합니다.

`--confirm`
: `--email`과 함께 사용하면 확인 이메일을 보내지 않습니다.

`--disable`
: `USERNAME`이 계정에 접근하지 못하도록 잠급니다.

`--enable`
: `USERNAME`의 계정이 비활성화되어 있으면 잠금을 해제합니다.

`--approve`
: 현재 또는 이전에 승인제 가입을 사용했다면 `USERNAME`의 계정을 승인합니다.

`--disable-2fa`
: 추가 인증 수단을 제거하고 비밀번호로 로그인하도록 허용합니다.

`--reset-password`
: 지정한 계정의 비밀번호를 재설정합니다.

**버전 이력:**\
2.6.0 - 추가\
3.1.2 - 추가 `--reset-password`\
3.5.1 - `--skip-sign-in-token` 제거\
4.0.0 - `--role`은 더 이상 고정된 `user`, `moderator`, `admin` 역할을 받지 않습니다. 대신 사용자 지정 역할의 이름을 지정하며 대소문자를 구분합니다. 현재 역할은 `--remove-role`로 제거합니다.


---


### `tootctl accounts delete` {#accounts-delete}

지정한 USERNAME의 사용자 계정을 삭제합니다.

`USERNAME`
: 삭제할 계정의 로컬 사용자명입니다. {{<required>}}

**버전 이력:**\
2.6.0 - 추가


---


### `tootctl accounts backup` {#accounts-backup}

지정한 USERNAME의 계정 백업을 요청합니다. Sidekiq가 비동기적으로 백업을 만들며, 완료되면 사용자에게 다운로드 링크를 이메일로 보냅니다.

`USERNAME`
: 백업할 계정의 로컬 사용자명입니다. {{<required>}}

**버전 이력:**\
2.6.0 - 추가


---


### `tootctl accounts cull` {#accounts-cull}

더 이상 존재하지 않는 원격 계정을 제거합니다. 데이터베이스의 모든 원격 계정이 원래 서버에 아직 있는지 하나씩 확인하고, 없다면 데이터베이스에서 제거합니다. 최근 일주일 안에 활동이 확인된 계정은 검사에서 제외합니다. 검사할 때 계정의 도메인에 접근할 수 없다면 계정을 제거하지 않고 스크립트 종료 시 해당 도메인을 보고합니다.

`DOMAIN[...]`
: 정리할 특정 도메인을 선택적으로 지정합니다.

`--concurrency N`
: 이 작업에 사용할 작업자 수입니다. 기본값은 N=5입니다.

`--dry-run`
: 실제 작업 없이 예상 결과만 출력합니다.

**버전 이력:**\
2.6.0 - 추가\
2.8.0 - 추가: `--dry-run`\
3.5.0 - 특정 도메인을 지정하는 기능 추가


---


### `tootctl accounts refresh` {#accounts-refresh}

하나 이상의 원격 계정에서 사용자 데이터와 파일을 다시 가져옵니다.

`USERNAME`
: 원격 계정의 username@domain 주소입니다.

`--all`
: `USERNAME` 대신 지정하여 모든 원격 계정을 갱신할 수 있습니다.

`--domain DOMAIN`
: `USERNAME` 대신 지정할 수 있습니다. 이 `DOMAIN`에 속한 원격 계정만 처리합니다.

`--concurrency N`
: 이 작업에 사용할 작업자 수입니다. 기본값은 N=5입니다.

`--verbose`
: 작업을 처리하는 동안 추가 정보를 출력합니다.

`--dry-run`
: 실제 작업 없이 예상 결과만 출력합니다.

**버전 이력:**\
2.6.0 - 추가


---


### `tootctl accounts merge` {#accounts-merge}

두 원격 계정을 하나로 합칩니다. 주로 다른 서버의 도메인 변경으로 생긴 중복 계정을 정리하기 위한 기능입니다. 기본적으로 공개 키가 같아야 하지만 이 검사를 무시할 수 있습니다.

`FROM`
: 제거할 원격 계정의 username@domain 주소입니다. {{<required>}}

`TO`
: 유지할 원격 계정의 username@domain 주소입니다. {{<required>}}

`--force`
: 공개 키 검사를 무시합니다.

**버전 이력:**\
3.3.0 - 추가


---


### `tootctl accounts follow` {#accounts-follow}

모든 로컬 계정이 사용자명으로 지정한 로컬 계정을 강제로 팔로우하게 합니다.

`USERNAME`
: 로컬 사용자명입니다. {{<required>}}

`--concurrency N`
: 이 작업에 사용할 작업자 수입니다. 기본값은 N=5입니다.

`--verbose`
: 작업을 처리하는 동안 추가 정보를 출력합니다.

**버전 이력:**\
2.7.0 - 추가\
3.0.0 - `ACCT` 대신 `USERNAME` 사용


---


### `tootctl accounts unfollow` {#accounts-unfollow}

모든 로컬 계정이 주소로 지정한 계정의 팔로우를 강제로 취소하게 합니다.

`ACCT`
: `username@domain` 주소입니다. {{<required>}}

`--concurrency N`
: 이 작업에 사용할 작업자 수입니다. 기본값은 N=5입니다.

`--verbose`
: 작업을 처리하는 동안 추가 정보를 출력합니다.

**버전 이력:**\
2.7.0 - 추가


---


### `tootctl accounts reset-relationships` {#accounts-reset-relationships}

로컬 계정의 팔로잉 또는 팔로워 관계 전체를 재설정합니다.

`USERNAME`
: 로컬 사용자명입니다.

`--follows`
: `USERNAME`이 모든 팔로우를 강제로 취소한 뒤 다시 팔로우하게 합니다.

`--followers`
: `USERNAME`의 팔로워를 모두 제거합니다.

**버전 이력:**\
2.8.0 - 추가


---


### `tootctl accounts approve` {#accounts-approve}

서버가 승인제 가입 모드일 때 새 가입을 승인합니다.

`USERNAME`
: 로컬 사용자명입니다.

`--number N`
: 가장 오래 기다린 가입 요청 N개를 승인합니다.

`--all`
: 대기 중인 가입 요청을 모두 승인합니다.

**버전 이력:**\
2.8.0 - 추가


---


### `tootctl accounts prune` {#accounts-prune}

로컬 사용자와 한 번도 상호작용하지 않은 원격 계정을 정리합니다.

`--concurrency N`
: 이 작업에 사용할 작업자 수입니다. 기본값은 N=5입니다.

`--dry-run`
: 실제 작업 없이 예상 결과만 출력합니다.

**버전 이력:**\
2.8.0 - 추가


---


## 캐시 CLI {#cache}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/lib/mastodon/cli/cache.rb" caption="lib/mastodon/cli/cache.rb" >}}


---


### `tootctl cache clear` {#cache-clear}

캐시 저장소를 비웁니다.

**버전 이력:**\
2.8.1 - 추가


---


### `tootctl cache recount` {#cache-recount}

참조되는 레코드를 처음부터 다시 세어 TYPE의 저장된 카운터를 갱신합니다. 데이터베이스 크기에 따라 매우 오래 걸릴 수 있습니다. 계정은 팔로워, 팔로잉, 게시물 수를 갱신하고, 게시물은 답글, 부스트, 좋아요 수를 갱신합니다.

`TYPE`
: `accounts` 또는 `statuses`입니다. {{<required>}}

`--concurrency N`
: 이 작업에 사용할 작업자 수입니다. 기본값은 N=5입니다.

`--verbose`
: 작업을 처리하는 동안 추가 정보를 출력합니다.

**버전 이력:**\
3.0.0 - 추가


---


## 도메인 CLI {#domains}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/lib/mastodon/cli/domains.rb" caption="lib/mastodon/cli/domains.rb" >}}


---


### `tootctl domains purge` {#domains-purge}

지정한 DOMAIN의 모든 계정을 기록을 남기지 않고 제거합니다. 정지와 달리 DOMAIN이 계속 운영 중이면 나중에 계정 정보를 다시 조회할 때 계정이 다시 나타날 수 있습니다.

`DOMAIN[...]`
: 제거할 도메인을 공백으로 구분하여 지정합니다.

`--by-uri`
: WebFinger 주소 대신 액터 URI의 도메인을 기준으로 일치 여부를 판단합니다.

`--limited-federation-mode`
: DOMAIN 대신 지정할 수 있습니다. 하나의 도메인만 제거하는 대신 허용 목록에 없는 모든 도메인의 계정을 데이터베이스에서 제거합니다. 제한된 연합 모드를 활성화하고 허용 목록을 설정한 뒤 사용하세요.

`--concurrency N`
: 이 작업에 사용할 작업자 수입니다. 기본값은 5입니다.

`--verbose`
: 작업을 처리하는 동안 추가 정보를 출력합니다.

`--dry-run`
: 실제 작업 없이 예상 결과만 출력합니다.

**버전 이력:**\
2.6.0 - 추가\
2.8.0 - 추가: `--whitelist-mode`\
2.9.0 - 커스텀 이모지도 제거\
3.0.0 - 여러 도메인 지정 지원\
3.2.0 - `--whitelist-mode`를 `--limited-federation-mode`로 이름 변경\
3.5.0 - 추가: `--by-uri`


---


### `tootctl domains crawl` {#domains-crawl}

알려진 모든 연결 서버를 공개하는 마스토돈 REST API 엔드포인트를 사용하여 연합우주를 탐색하고 통계를 수집합니다. 연결 서버가 해당 API를 지원해야 합니다. START를 지정하지 않으면 자체 데이터베이스의 알려진 서버 목록에서 탐색을 시작합니다. 서버 총수, 등록 사용자 총수, 지난주 활성 사용자 총수와 지난주 가입 사용자 총수를 반환합니다.

`START`
: 다른 도메인에서 탐색을 시작하도록 선택적으로 지정합니다.

`--exclude-suspended`
: 정지한 서버를 결과에서 제외합니다. 해당 서버의 하위 도메인도 제외합니다.

`--concurrency N`
: 이 작업에 사용할 작업자 수입니다. 기본값은 N=50입니다.

`--format FORMAT`
: 결과 출력 형식을 지정합니다. `summary`는 요약을 출력하고, `domains`는 발견한 모든 연결 서버를 줄바꿈으로 구분하여 출력합니다. `json`은 집계한 원시 데이터를 출력합니다. 기본값은 `summary`입니다.

**버전 이력:**\
2.7.0 - 추가\
3.0.0 - 추가: `--exclude-suspended`


---


## 이메일 도메인 차단 CLI {#email-domain-blocks}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/lib/mastodon/cli/email_domain_blocks.rb" caption="lib/mastodon/cli/email_domain_blocks.rb" >}}


---


### `tootctl email-domain-blocks list` {#email-domain-blocks-list}

현재 차단된 이메일 도메인을 모두 나열합니다.

**버전 이력:**\
3.2.0 - 추가


---


### `tootctl email-domain-blocks add` {#email-domain-blocks-add}

이메일 도메인 차단 목록에 항목을 추가합니다.

`DOMAIN[...]`
: 차단할 이메일 도메인을 공백으로 구분하여 지정합니다. {{<required>}}

`--with-dns-records`
: 지정하면 A, AAAA, MX 레코드도 조회하여 함께 차단합니다.

**버전 이력:**\
3.2.0 - 추가


---


### `tootctl email-domain-blocks remove` {#email-domain-blocks-remove}

이메일 도메인 차단 목록에서 항목을 제거합니다.

`DOMAIN[...]`
: 차단을 해제할 이메일 도메인을 공백으로 구분하여 지정합니다. {{<required>}}

**버전 이력:**\
3.2.0 - 추가


---


## 이모지 CLI {#emoji}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/lib/mastodon/cli/emoji.rb" caption="lib/mastodon/cli/emoji.rb" >}}


---


### `tootctl emoji export` {#emoji-export}

커스텀 이모지를 PATH의 `export.tar.gz`로 내보냅니다.

`PATH`
: 이미지를 담은 .tar.gz 보관 파일을 만들 경로입니다. {{<required>}}

`--overwrite`
: `PATH`에 기존 보관 파일이 있으면 덮어씁니다.

`--category CATEGORY`
: 지정한 `CATEGORY`만 내보냅니다. 생략하면 모든 이모지를 내보냅니다.

**버전 이력:**\
3.1.4 - 추가


---


### `tootctl emoji import` {#emoji-import}

지정한 경로의 .tar.gz 보관 파일에서 커스텀 이모지를 가져옵니다. 보관 파일에는 50KB 이하의 PNG 또는 GIF 파일이 들어 있어야 합니다. 단축 코드는 확장자를 뺀 파일명으로 설정되며, 선택적으로 접두사나 접미사를 붙일 수 있습니다.

`PATH`
: 이미지를 담은 .tar.gz 보관 파일을 만들 경로입니다. {{<required>}}

`--prefix PREFIX`
: 생성되는 단축 코드 앞에 PREFIX를 붙입니다.

`--suffix SUFFIX`
: 생성되는 단축 코드 뒤에 SUFFIX를 붙입니다.

`--overwrite`
: 기존 이모지를 건너뛰지 않고, 같은 단축 코드의 이모지가 발견되면 새 이모지로 대체합니다.

`--category CATEGORY`
: 처리한 이모지를 선택창의 CATEGORY 분류에 묶습니다.

`--unlisted`
: 처리한 이모지는 이모지 선택창에 표시되지 않으며 단축 코드를 직접 입력해야만 사용할 수 있습니다.

**버전 이력:**\
2.5.0 - 추가


---


### `tootctl emoji purge` {#emoji-purge}

모든 커스텀 이모지를 제거합니다.

`--remote-only`
: 지정하면 원격 도메인의 이모지만 제거합니다.

**버전 이력:**\
2.8.0 - 추가\
3.1.0 - 추가: `--remote-only`


---


## 피드 CLI {#feeds}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/lib/mastodon/cli/feeds.rb" caption="lib/mastodon/cli/feeds.rb" >}}


---


### `tootctl feeds build` {#feeds-build}

한 명 또는 모든 사용자의 홈 피드와 리스트 피드를 생성합니다. 데이터베이스에서 피드를 구성하여 Redis 메모리에 캐시합니다. 활성 사용자의 홈 피드는 마스토돈이 자동으로 관리합니다.

`USERNAME`
: 피드를 다시 생성할 로컬 사용자명입니다.

`--all`
: `USERNAME` 대신 지정하여 모든 원격 계정을 갱신할 수 있습니다.

`--concurrency N`
: 이 작업에 사용할 작업자 수입니다. 기본값은 N=5입니다.

`--verbose`
: 작업을 처리하는 동안 추가 정보를 출력합니다.

`--dry-run`
: 실제 작업 없이 예상 결과만 출력합니다.

**버전 이력:**\
2.6.0 - 추가


---


### `tootctl feeds clear` {#feeds-clear}

Redis에서 모든 홈 피드와 리스트 피드를 제거합니다.

**버전 이력:**\
2.6.0 - 추가


---


## 유지보수 CLI {#maintenance}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/lib/mastodon/cli/maintenance.rb" caption="lib/mastodon/cli/maintenance.rb" >}}


---


### `tootctl maintenance fix-duplicates` {#maintenance-fix-duplicates}

정렬 규칙 변경으로 손상되었을 수 있는 데이터베이스 색인을 복구합니다. 중복된 계정, 게시물, 이모지 등을 삭제하거나 병합합니다. 실행 전에 마스토돈을 중지해야 하며, 오래 걸리고 데이터 손실을 일으킬 수 있습니다. <https://wiki.postgresql.org/wiki/Locale_data_changes>와 같은 문제로 데이터베이스 색인이 손상된 경우에 유용합니다.

**버전 이력:**\
3.3.0 - 추가


---


## 미디어 CLI {#media}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/lib/mastodon/cli/media.rb" caption="lib/mastodon/cli/media.rb" >}}


---


### `tootctl media remove` {#media-remove}

다른 서버의 미디어 첨부, 아바타 또는 프로필 헤더 중 로컬에 캐시된 사본을 제거합니다. 기본적으로 미디어 첨부만 제거합니다.

`--days N`
: 미디어 첨부를 제거할 기준 경과 일수입니다. 아바타와 헤더는 해당 사용자의 마지막 WebFinger 요청 및 갱신 이후의 경과 일수를 기준으로 합니다. 기본값은 7입니다.

`--concurrency N`
: 이 작업에 사용할 작업자 수입니다. 기본값은 N=5입니다.

`--prune-profiles`
: 미디어 첨부 대신 다른 서버의 아바타와 헤더 중 로컬 캐시 사본을 제거합니다. `--remove-headers`와 함께 사용할 수 없습니다.

`--remove-headers`
: 미디어 첨부 대신 다른 서버의 헤더 중 로컬 캐시 사본을 제거합니다. `--prune-profiles`와 함께 사용할 수 없습니다.

`--include-follows`
: `--prune-profiles`와 `--remove-headers`의 기본 동작을 변경하여 팔로우 관계와 무관하게 다른 서버의 아바타 및 헤더 캐시를 제거합니다. 기본적으로는 로컬 사용자와 어느 방향으로도 팔로우 관계가 없는 계정만 제거 대상입니다. `--prune-profiles` 또는 `--remove-headers`와 함께 사용해야 합니다.

`--verbose`
: 작업을 처리하는 동안 추가 정보를 출력합니다.

`--dry-run`
: 실제 작업 없이 예상 결과만 출력합니다.

**버전 이력:**\
2.5.0 - 추가\
2.6.2 - 확보한 디스크 공간 표시\
4.1.0 - --prune-profiles, --remove-headers, --include-follows 추가


---


### `tootctl media remove-orphans` {#media-remove-orphans}

기존 미디어 첨부에 속하지 않는 파일을 찾아 제거합니다. 일부 스토리지 제공자는 오브젝트 목록 조회에 필요한 API 요청에 비용을 청구합니다. 또한 모든 파일을 하나씩 확인해야 하므로 느리게 처리됩니다.

`--start-after`
: 순회를 시작할 Paperclip 첨부 키입니다. 이전에 명령이 중단되었다면 이 옵션을 사용하세요.

`--dry-run`
: 실제 작업 없이 예상 결과만 출력합니다.

`--prefix`
: 파일 저장소에서 지정한 접두사의 파일만 순회합니다.

`--fix-permissions`
: 환경 변수에 따른 기본값으로 S3 ACL을 설정합니다.

**버전 이력:**\
3.1.0 - 추가\
3.1.3 - 추가 `--prefix`\
3.3.0 - 추가 `--fix-permissions`


---


### `tootctl media refresh` {#media-refresh}

다른 서버에서 원격 미디어 첨부를 다시 가져옵니다. `--status`, `--account`, `--domain`, `--days` 중 하나로 대상을 지정해야 합니다. 데이터베이스에 첨부가 이미 있다면 `--force`를 사용하지 않는 한 덮어쓰지 않습니다.

`--account ACCT`
: 계정의 `username@domain` 주소 문자열입니다.

`--domain DOMAIN`
: FQDN 문자열입니다.

`--status ID`
: 데이터베이스에서 게시물의 로컬 숫자 ID입니다.

`--days N`
: 작업 대상을 제한할 일수입니다.

`--concurrency N`
: 이 작업에 사용할 작업자 수입니다. 기본값은 5입니다.

`--verbose`
: 작업을 처리하는 동안 추가 정보를 출력합니다.

`--dry-run`
: 실제 작업 없이 예상 결과만 출력합니다.

`--force`
: 원격 리소스를 강제로 다시 내려받고 로컬 첨부를 덮어씁니다.

**버전 이력:**\
3.0.0 - 추가\
3.0.1 - `--force` 추가, 기본적으로 이미 내려받은 첨부는 건너뜀\
4.0.0 - 추가: `--days`


---


### `tootctl media usage` {#media-usage}

마스토돈이 사용하는 디스크 공간을 계산합니다.

**버전 이력:**\
3.0.1 - 추가


---


### `tootctl media lookup` {#media-lookup}

미디어 URL을 입력받고 해당 미디어가 표시되는 게시물을 찾습니다.

**버전 이력:**\
3.1.0 - 추가


---


## 미리보기 카드 CLI {#preview_cards}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/lib/mastodon/cli/preview_cards.rb" caption="lib/mastodon/cli/preview_cards.rb" >}}


---


### `tootctl preview_cards remove` {#preview_cards-remove}

미리보기 카드의 로컬 썸네일을 제거합니다.

`--days N`
: 미디어 첨부를 제거할 기준 경과 일수입니다. 기본값은 180입니다. 참고: 미리보기 카드는 마지막 게시 후 2주가 지난 뒤 링크가 다시 게시되어야 다시 가져오므로, 최근 14일 이내의 카드는 삭제하지 않는 것이 좋습니다.

`--concurrency N`
: 이 작업에 사용할 작업자 수입니다. 기본값은 N=5입니다.

`--verbose`
: 작업을 처리하는 동안 추가 정보를 출력합니다.

`--dry-run`
: 실제 작업 없이 예상 결과만 출력합니다.

`--link`
: 링크 유형의 미리보기 카드만 삭제하고 동영상 및 사진 카드는 유지합니다.

**버전 이력:**\
3.0.0 - 추가


---


## 검색 CLI {#search}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/lib/mastodon/cli/search.rb" caption="lib/mastodon/cli/search.rb" >}}


---


### `tootctl search deploy` {#search-deploy}

Elasticsearch 색인을 만들거나 갱신하고 데이터를 채웁니다. Elasticsearch가 비어 있으면 필요한 색인을 만든 뒤 데이터베이스의 데이터를 가져옵니다. 마지막 실행 이후 기반 스키마가 바뀌었다면 색인도 업그레이드합니다.

`--batch-size`
: 기본값은 100입니다. 배치 크기를 늘리면 PostgreSQL 데이터베이스의 부하를 줄이면서 Elasticsearch가 레코드를 더 빠르게 처리할 수 있지만, 색인 생성 중 Elasticsearch 노드의 메모리 부담이 커질 수 있습니다.

`--only INDEX`
: 색인 이름 [`instances`, `accounts`, `tags`, `statuses`, `public_statuses`]을 지정하여 해당 색인만 만들거나 갱신합니다.

`--concurrency N`
: 여러 스레드에서 명령을 병렬 실행합니다. 기본값은 5입니다.

`--import`
: 데이터베이스의 데이터를 색인으로 가져옵니다.

`--clean`
: 색인에서 오래된 문서를 제거합니다.

`--reset-chewy`
: Chewy 내부 색인을 초기화합니다.

**버전 이력:**\
2.8.0 - 추가\
3.0.0 - 병렬 처리를 위한 `--processes` 추가\
3.3.0 - 옵션 변경\
3.5.0 - 추가: `--batch-size`\
3.5.3 - `--batch-size` 기본값을 1000에서 100으로, `--concurrency` 기본값을 2에서 5로 변경하고 `--import`, `--clean` 추가\
4.2.0 - `--only`에 `instances`와 `public_statuses` 선택지 추가, `--reset-chewy` 추가


---


## 설정 CLI {#settings}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/lib/mastodon/cli/settings.rb" caption="lib/mastodon/cli/settings.rb" >}}


---


### `tootctl settings registrations open` {#settings-registrations-open}

가입을 허용합니다.

**버전 이력:**\
2.6.0 - 추가


---


### `tootctl settings registrations close` {#settings-registrations-close}

가입을 닫습니다.

**버전 이력:**\
2.6.0 - 추가


---


### `tootctl settings registrations approved` {#settings-registrations-approved}

가입 시 승인이 필요하도록 설정합니다.

**버전 이력:**\
3.5.2 - 추가

`--require_reason`
: true이면 가입할 때 이유를 입력해야 합니다.


---


## 게시물 CLI {#statuses}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/lib/mastodon/cli/statuses.rb" caption="lib/mastodon/cli/statuses.rb" >}}


---


### `tootctl statuses remove` {#statuses-remove}

릴레이에서 들어왔거나 로컬 계정이 더 이상 팔로우하지 않는 사용자의 게시물 중 답글이나 다른 상호작용이 없는 것처럼, 참조되지 않는 게시물을 데이터베이스에서 제거합니다.

처리 전에 추가 데이터베이스 색인을 만들고 완료 후 제거하는, 계산 부하가 큰 작업입니다.

`--days N`
: 게시물을 제거할 기준 경과 일수입니다. 기본값은 90입니다.

`--batch_size N`
: 배치마다 처리할 레코드 수입니다. 기본값은 1000입니다.

`--continue`
: 제거가 완료되지 않았다면 이전에 중단된 지점부터 계속합니다.

`--clean_followed`
: 로컬 계정이 팔로우하는 원격 계정의 게시물도 제거 후보에 포함합니다.

`--skip_status_remove`
: 게시물 제거를 건너뛰고 정리 작업만 실행합니다.

`--skip-media-remove`
: S3 오류가 발생할 때 미디어 제거를 건너뜁니다. 기본값은 false입니다.

`--compress_database`
: 데이터베이스를 압축하고 통계를 갱신합니다. 테이블을 오랫동안 잠그므로 서비스를 중지한 상태에서 실행하세요.


**버전 이력:**\
2.8.0 - 추가\
3.1.3 - 추가 `--skip-media-remove`\
3.5.0 - 고아 레코드를 제거하고 추가 정리 작업 수행


---


## 업그레이드 CLI {#upgrade}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/lib/mastodon/cli/upgrade.rb" caption="lib/mastodon/cli/upgrade.rb" >}}


---


### `tootctl upgrade storage-schema` {#upgrade-storage-schema}

스토리지 스키마를 업그레이드하여 모든 비로컬 미디어 리소스를 최상위 캐시 디렉터리에 저장합니다. 경고: 선택 사항이며 v3.1.4 이전에 배포한 서버에만 해당합니다. 테라바이트 규모의 데이터를 이동할 수 있어 오브젝트 스토리지 비용이 매우 크게 발생할 수 있습니다.

`--verbose`
: 작업을 처리하는 동안 추가 정보를 출력합니다.

`--dry-run`
: 실제 작업 없이 예상 결과만 출력합니다.

**버전 이력:**\
3.1.4 - 추가
