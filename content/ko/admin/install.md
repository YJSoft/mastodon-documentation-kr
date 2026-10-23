---
title: 소스에서 설치하기
description: 마스토돈으로 운영되는 나만의 웹사이트를 만드는 안내서
menu:
  docs:
    weight: 20
    parent: admin
---

## 사전 준비 {#pre-requisites}

* root 권한으로 접근할 수 있는 **Ubuntu 24.04** 또는 **Debian 13** 실행 컴퓨터
* 마스토돈 서버용 **도메인 이름** 또는 하위 도메인(예: `example.com`)
* 이메일 배달 서비스 또는 기타 **SMTP 서버**

다음 예제에서는 도메인으로 `example.com`을 사용합니다. 명령을 실행하기 전에 자신의 도메인으로 바꾸세요.

명령은 root로 실행합니다. 아직 root가 아니라면 `sudo -i`로 전환합니다.

### 시스템 저장소 {#system-repositories}

먼저 curl, wget, gnupg, lsb-release, ca-certificates가 설치되어 있는지 확인합니다.

```bash
apt install -y curl wget gnupg lsb-release ca-certificates
```

#### Node.js {#node-js}

```bash
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_24.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list
```

#### PostgreSQL {#postgresql}

```bash
wget -O /usr/share/keyrings/postgresql.asc https://www.postgresql.org/media/keys/ACCC4CF8.asc
echo "deb [signed-by=/usr/share/keyrings/postgresql.asc] http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/postgresql.list
```

### 시스템 패키지 {#system-packages}

```bash
apt update
apt install -y \
  imagemagick ffmpeg libvips-tools libpq-dev libxslt1-dev file git \
  protobuf-compiler pkg-config autoconf bison build-essential \
  libssl-dev libyaml-dev libreadline-dev zlib1g-dev libffi-dev \
  libgdbm-dev nginx nodejs redis-server postgresql certbot \
  python3-certbot-nginx libidn-dev libicu-dev libjemalloc-dev
```

#### Yarn {#yarn}

올바른 버전의 `yarn`을 자동으로 설치할 수 있도록 `corepack`을 활성화합니다.

```bash
corepack enable
```

### `mastodon` 사용자 만들기 {#creating-the-mastodon-user}

마스토돈은 이 사용자 계정으로 실행됩니다.

```bash
adduser --disabled-password mastodon
```

## 설정 {#setup}

### PostgreSQL 설정 {#setting-up-postgresql}

#### 성능 설정(선택 사항) {#performance-configuration-optional}

최적의 성능을 위해 [pgTune](https://pgtune.leopard.in.ua/#/)으로 적절한 설정을 생성할 수 있습니다.

* 적절한 PG 버전과 운영 체제 유형을 선택합니다.
* DB Type으로 "Web application"을 선택합니다.
* 다른 값은 서버에 맞게 입력합니다.

생성된 설정에 따라 `/etc/postgresql/18/main/postgresql.conf`의 값을 편집한 다음 `systemctl restart postgresql`로 PostgreSQL을 재시작합니다.

#### 사용자 만들기 {#creating-a-user}

마스토돈이 사용할 PostgreSQL 사용자를 만들어야 합니다. 간단한 구성에서는 PostgreSQL 사용자에 별도 비밀번호를 두지 않고 같은 사용자명의 Linux 사용자가 사용할 수 있는 “ident” 인증이 가장 쉽습니다.

프롬프트를 엽니다.

```bash
sudo -u postgres psql
```

프롬프트에서 다음을 실행합니다.

```sql
CREATE USER mastodon CREATEDB;
\q
```

완료되었습니다!

### 마스토돈 설정 {#setting-up-mastodon}

이제 마스토돈 코드를 다운로드합니다. mastodon 사용자로 전환합니다.

```bash
su - mastodon
```

#### 코드 체크아웃 {#checking-out-the-code}

git으로 마스토돈의 최신 안정 릴리스를 다운로드합니다.

```bash
git clone https://github.com/mastodon/mastodon.git live && cd live
git checkout $(git tag -l | grep '^v[0-9.]*$' | sort -V | tail -n 1)
```

#### Ruby 설치 {#installing-ruby}

올바른 버전을 구하고 새 릴리스가 나오면 업데이트하기 쉽도록 rbenv로 Ruby 버전을 관리합니다.
rbenv와 ruby-build를 설치합니다.

```bash
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
source ~/.bashrc
git clone https://github.com/rbenv/ruby-build.git "$(rbenv root)"/plugins/ruby-build
```

이 작업을 마치면 올바른 Ruby 버전을 설치할 수 있습니다.

```bash
RUBY_CONFIGURE_OPTS=--with-jemalloc rbenv install
```

#### 나머지 의존성 설치 {#installing-the-last-dependencies}

이제 Ruby 및 JavaScript 의존성을 설치합니다.

```bash
bundle config deployment 'true'
bundle config without 'development test'
bundle install
yarn install
```

{{< hint style="info" >}}
두 `bundle config` 명령은 처음 의존성을 설치할 때만 필요합니다. 이후 의존성을 업데이트하거나 다시 설치할 때는 `bundle install`만으로 충분합니다.
{{< /hint >}}

#### 설정 생성 {#generating-a-configuration}

대화형 설정 마법사를 실행합니다.

```bash
RAILS_ENV=production bin/rails mastodon:setup
```

이 명령은 다음을 수행합니다.

* 설정 파일 생성
* 에셋 사전 컴파일 실행
* 데이터베이스 스키마 생성

설정 파일은 `.env.production`으로 저장됩니다. 검토하고 원하는 대로 편집할 수 있습니다. [설정 문서]({{< relref "config" >}})를 참고합니다.

일단 mastodon 사용자로 할 일은 마쳤으므로 root로 돌아갑니다.

```bash
exit
```

### SSL 인증서 받기 {#acquiring-a-ssl-certificate}

Let’s Encrypt로 무료 SSL 인증서를 받습니다.

```bash
certbot certonly --nginx -d example.com
```

이 명령은 인증서를 받아 `/etc/letsencrypt/live/example.com/` 디렉터리에 저장합니다.

### nginx 설정 {#setting-up-nginx}

마스토돈 디렉터리에서 nginx 설정 템플릿을 복사합니다.

```bash
cp /home/mastodon/live/dist/nginx.conf /etc/nginx/sites-available/mastodon
ln -s /etc/nginx/sites-available/mastodon /etc/nginx/sites-enabled/mastodon
rm /etc/nginx/sites-enabled/default
```

그런 다음 `/etc/nginx/sites-available/mastodon`을 편집합니다.

1. `example.com`을 자신의 도메인 이름으로 바꿉니다.
2. `ssl_certificate`와 `ssl_certificate_key`의 주석을 해제합니다. 자체 인증서를 사용한다면 이 단계는 생략합니다.

    ```nginx
    ssl_certificate     /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;;
    ```

3. 그 밖에 필요한 조정을 합니다.

nginx의 `www-data` 사용자가 에셋 파일에 접근할 수 있도록 다른 사용자가 mastodon 사용자의 홈 디렉터리를 통과하도록 허용합니다.

```bash
chmod o+x /home/mastodon
```

변경 사항이 적용되도록 nginx를 재시작합니다.

```bash
systemctl restart nginx
```

이제 브라우저에서 도메인에 접속하면 코끼리가 컴퓨터 화면을 두드리는 오류 페이지가 보일 것입니다. 아직 마스토돈 프로세스를 시작하지 않았기 때문입니다.

### systemd 서비스 설정 {#setting-up-systemd-services}

마스토돈 디렉터리에서 systemd 서비스 템플릿을 복사합니다.

```sh
cp /home/mastodon/live/dist/mastodon-*.service /etc/systemd/system/
```

어느 단계에서든 기본값과 다르게 설정했다면 사용자명과 경로가 올바른지 확인합니다.

```sh
$EDITOR /etc/systemd/system/mastodon-*.service
```

마지막으로 새 systemd 서비스를 시작하고 활성화합니다.

```sh
systemctl daemon-reload
systemctl enable --now mastodon-web mastodon-sidekiq mastodon-streaming
```

이제 부팅할 때 자동으로 시작됩니다.

{{< hint style="success" >}}
**완료되었습니다! 이제 브라우저에서 자신의 도메인에 접속할 수 있습니다!**
{{< /hint >}}
