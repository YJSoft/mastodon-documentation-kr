---
title: 개발 환경 설정하기
description: 마스토돈 개발을 시작하는 방법을 안내합니다.
menu:
  docs:
    weight: 20
    parent: dev
---

## Vagrant로 빠르게 시작하기 {#vagrant}

마스토돈 저장소에는 수동 구성 없이 개발 환경을 빠르게 설정할 수 있는 Vagrantfile이 포함되어 있습니다. 이 개발 환경을 사용하려면 실행 가능한 바이너리나 패키지 관리자를 통해 [Vagrant](https://vagrantup.com)를 설치합니다.

Vagrant를 설치한 다음에는 편의를 위해 컴퓨터의 hosts 파일을 자동으로 갱신하는 플러그인을 설치하는 것을 권장합니다. 그러면 hosts 파일을 직접 편집하지 않고도 `http://mastodon.local`에서 개발 환경에 접속할 수 있습니다. 다음 명령을 실행합니다.

```sh
vagrant plugin install vagrant-hostsupdater
```

이제 가상 머신을 시작할 수 있습니다.

```sh
vagrant up
```

가상 머신이 시작되면 `dev` 작업 실행기를 실행하여 마스토돈의 여러 프로세스를 시작할 수 있습니다.

```sh
vagrant ssh -c "cd /vagrant && bin/dev"
```

마스토돈 프로세스가 모두 시작되면 브라우저에서 `http://mastodon.local`을 열어 VM 안의 마스토돈 서버에 접속할 수 있습니다. 사용자명 `admin@mastodon.local`, 비밀번호 `mastodonadmin`으로 기본 관리자 계정에 로그인할 수 있습니다.

소스 코드 변경 사항은 파일을 저장하면 반영됩니다.

VM을 초기 상태로 되돌리려면 삭제한 다음 다시 시작합니다.

```sh
vagrant destroy
vagrant up
```

## 소스에서 수동으로 설치하기 {#manual}

[운영 환경 안내서의 사전 준비 지침]({{<relref "admin/install">}})을 따라도 되지만, `mastodon` 사용자는 만들지 않습니다. 개발 환경에는 자체 웹 서버가 있으므로 `nginx`, `certbot`, `python-certbot-nginx`도 설치할 필요가 없습니다. Windows에서는 WSL2에서도 개발 환경을 설정하고 실행할 수 있음이 확인되었습니다.

### 설정 {#setup}

프로젝트 디렉터리에서 다음 명령을 실행합니다.

```sh
bundle install
yarn install
```

개발 환경에서 마스토돈은 `ident` 방식으로 현재 로그인한 Linux 사용자로 PostgreSQL을 사용합니다. 현재 로그인한 사용자를 위한 PostgreSQL 사용자와 데이터베이스를 만들어 두어야 합니다.

```sh
sudo -u postgres createuser $YOUR_USERNAME_HERE --createdb
```

이제 `mastodon_development`와 `mastodon_test` 데이터베이스를 만들고 스키마를 불러온 다음, `db/seeds/`에 정의된 초기 데이터를 `mastodon_development`에 생성할 수 있습니다.

```sh
RAILS_ENV=development bin/rails db:setup
```

이제 브라우저에서 `http://localhost:3000`을 열고 기본 관리자 계정(`admin@localhost` / `mastodonadmin`)으로 로그인할 수 있습니다.

{{<hint style="warning">}}
마스토돈은 기본적으로 3000번 포트에서 실행됩니다. 다른 포트를 설정하면 생성되는 관리자 계정에도 그 번호가 사용됩니다.
{{</hint>}}

### 실행 {#running}

마스토돈의 모든 기능을 사용하려면 여러 프로세스를 실행해야 합니다. 필요에 따라 일부는 생략할 수도 있습니다. 명령 하나로 모두 실행하려면 Foreman을 설치하여 사용합니다.

```sh
gem install foreman --no-document
bin/dev
```

이 명령은 `Procfile.dev`에 정의된 프로세스, 즉 Rails 웹 서버, 에셋용 Vite 서버, 스트리밍 API 서버, 백그라운드 작업용 Sidekiq를 시작합니다. 물론 필요에 따라 각각 따로 실행할 수도 있습니다.

## 개발 중 이메일 다루기 {#working-with-emails-in-development}

개발 모드에서 마스토돈은 [Letter Opener](https://github.com/ryanb/letter_opener)라는 gem으로 이메일을 “전송”합니다. 이를 통해 실제로 SMTP 서버에서 이메일을 보내지 않고도 브라우저에서 이메일을 디버깅할 수 있습니다.

이메일을 다루려면 Sidekiq, Redis, PostgreSQL을 실행해야 합니다. 그런 다음 `http://localhost:3000/letter_opener/`에서 이메일을 확인할 수 있습니다.

Docker에서 개발한다면 `REMOTE_DEV=true` 환경 변수를 설정해야 합니다.

## 테스트 실행 준비 {#preparing-to-run-tests}

테스트 데이터베이스를 설정합니다.

```sh
RAILS_ENV=test bin/rails db:setup
```

테스트 모드에서 사용할 사전 컴파일 에셋을 생성합니다.

```sh
RAILS_ENV=test bin/rails assets:precompile
```

## 테스트에 유용한 명령 {#testing}

`RAILS_ENV=test bin/rspec`
: Ruby 테스트 모음을 실행합니다.

`yarn run test`
: JavaScript 테스트 모음을 실행합니다.

`bin/rubocop`
: Ruby 코드가 프로젝트 코드 스타일을 따르는지 검사합니다.

## 개발 서버 업데이트하기 {#update}

`bundle install`
: Ruby gem을 업데이트하고 새 의존성을 설치합니다.

`yarn install`
: JavaScript 패키지를 업데이트하고 새 의존성을 설치합니다.

`RAILS_ENV=development bin/rails db:migrate`
: 개발 서버의 데이터베이스에 새 데이터베이스 마이그레이션을 실행합니다.
