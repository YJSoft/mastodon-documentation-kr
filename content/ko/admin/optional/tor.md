---
title: Onion 서비스
description: Tor onion 서비스를 통해 마스토돈 제공하기
menu:
  docs:
    weight: 20
    parent: admin-optional
---

마스토돈을 Tor의 onion 서비스로 제공할 수 있습니다. 그러면 Tor 네트워크에 연결했을 때만 사용할 수 있는 `*.onion` 주소가 생깁니다.

## Tor 설치 {#install}

먼저 Tor의 Debian 아카이브를 apt에 추가해야 합니다.

```text
deb https://deb.torproject.org/torproject.org stretch main
deb-src https://deb.torproject.org/torproject.org stretch main
```

그런 다음 gpg 키를 추가합니다.

```bash
curl https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | gpg --import
gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add -
```

마지막으로 필요한 패키지를 설치합니다.

```bash
apt install tor deb.torproject.org-keyring
```

다음과 같은 오류가 발생하면,

```text
E: The repository 'https://deb.torproject.org/torproject.org stretch Release' does not have a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```


저장소 설치에 관한 [Tor 프로젝트 지침](https://support.torproject.org/apt/tor-deb-repo/)을 따릅니다.

## Tor 설정 {#configure}

`/etc/tor/torrc` 파일을 편집하고 다음 설정을 추가합니다.

```text
HiddenServiceDir /var/lib/tor/onion_service/
HiddenServiceVersion 3
HiddenServicePort 80 127.0.0.1:80
```

Tor를 재시작합니다.

```bash
sudo service tor restart
```

이제 `/var/lib/tor/onion_service/hostname`에서 Tor 호스트명을 찾을 수 있습니다.

## 마스토돈 설정 옮기기 {#nginx}

Nginx에 마스토돈 설정을 두 번 알려 주어야 합니다. [중복을 피하기](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) 위해 마스토돈 설정을 나중에 참조할 수 있는 별도 파일로 옮겨야 합니다.

`/etc/nginx/snippets/mastodon.conf`에 새 파일을 만듭니다. `listen`, `server_name`, `include` 지시문과 모든 SSL 옵션을 제외한 마스토돈 설정 매개변수를 모두 복사합니다. 지원하는 브라우저가 이 서비스를 Tor로도 이용할 수 있음을 알도록 `Onion-Location` 헤더를 포함합니다. 새 파일은 대략 다음과 같습니다.

```nginx
add_header Referrer-Policy "same-origin";
add_header Onion-Location mastodon.qKnFwnNH2oH4QhQ7CoRf7HYj8wCwpDwsa8ohJmcPG9JodMZvVA6psKq7qKnFwnNH2oH4QhQ7CoRf7HYj8wCwpDwsa8ohJmcPG9JodMZvVA6psKq7.onion$request_uri;

keepalive_timeout    70;
sendfile             on;
client_max_body_size 80m;

root /home/mastodon/live/public;

# …

error_page 500 501 502 503 504 /500.html;

access_log /var/log/nginx/mastodon_access.log;
error_log /var/log/nginx/mastodon_error.log warn;
```

새 설정 파일에서 기존 마스토돈 설정이 있던 자리에 include 지시문을 추가합니다.

이제 Nginx 설정 파일은 대략 다음과 같습니다.

```nginx
server {
  listen 80;
  server_name mastodon.example.com;
  return 301 https://$server_name$request_uri;
}

map $http_upgrade $connection_upgrade {
  default upgrade;
  ''      close;
}

server {
  listen 443 ssl http2;
  list [::]:443 ssl http2;
  server_name mastodon.example.com;
  include /etc/nginx/snippets/mastodon.conf;

  ssl_certificate /etc/letsencrypt/live/mastodon.example.com/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/mastodon.example.com/privkey.pem;
}
```

## HTTP로 Tor 서비스 제공 {#http}

이 절에서는 서버를 Tor와 공개 인터넷에 *동시에* 노출하려는 것으로 가정합니다.

Tor 버전의 마스토돈도 HTTPS로 제공하고 싶겠지만 항상 이상적인 것은 아닙니다. 이는 주로 회사 정보로 자체 인증서를 발급받을 수 있는 대기업에 유용합니다. 이를 [무료로](https://community.torproject.org/onion-services/advanced/https/) 제공하는 인증 기관(CA)은 없으며, [Tor 프로젝트 블로그 글](https://blog.torproject.org/facebook-hidden-services-and-https-certs)에서는 HTTPS 인증서가 보안에 실질적인 이점이 없는 이유를 설명합니다. 반면 마스토돈에는 사이트의 HTTPS 버전으로 향하는 리디렉션이 많아, 유효한 인증서가 있으면 사용자가 URL에서 `https://` 접두사를 수동으로 지우지 않고도 Tor에서 서버를 사용하기 쉬울 수 있습니다.

이 절에서는 **Tor에서만** HTTP로 마스토돈을 제공하는 방법을 설명합니다. 기존 Nginx 설정 앞에 추가 설정을 넣으면 됩니다.

```nginx
server {
  listen 80;
  server_name mastodon.qKnFwnNH2oH4QhQ7CoRf7HYj8wCwpDwsa8ohJmcPG9JodMZvVA6psKq7qKnFwnNH2oH4QhQ7CoRf7HYj8wCwpDwsa8ohJmcPG9JodMZvVA6psKq7.onion;
  include /etc/nginx/snippets/mastodon.conf;
}

server {
  listen 80;
  server_name mastodon.example.com;
  return 301 https://$server_name$request_uri;
}

map $http_upgrade $connection_upgrade {
  default upgrade;
  ''      close;
}

server {
  listen 443 ssl http2;
  list [::]:443 ssl http2;
  server_name mastodon.example.com;
  include /etc/nginx/snippets/mastodon.conf;

  ssl_certificate /etc/letsencrypt/live/mastodon.example.com/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/mastodon.example.com/privkey.pem;
}
```

`.env.production`도 업데이트합니다.

```text
ALTERNATE_DOMAINS=mastodon.qKnFwnNH2oH4QhQ7CoRf7HYj8wCwpDwsa8ohJmcPG9JodMZvVA6psKq7qKnFwnNH2oH4QhQ7CoRf7HYj8wCwpDwsa8ohJmcPG9JodMZvVA6psKq7.onion
```

여기에 제시된 긴 해시를 `/var/lib/tor/onion_service/hostname` 파일의 Tor 도메인으로 바꿉니다. 스니펫 파일의 `Onion-Location` 헤더에도 반영해야 합니다.

onion 호스트명 앞에 “mastodon.”이 붙어 있다는 점에 주목합니다. Tor 주소는 와일드카드 도메인처럼 동작합니다. 모든 하위 도메인이 라우팅되며 원하는 하위 도메인에 응답하도록 Nginx를 설정할 수 있습니다. Tor 주소에서 다른 서비스를 호스팅할 생각이 없다면 하위 도메인을 생략하거나 다른 하위 도메인을 선택해도 됩니다.

마스토돈 설정을 별도 파일로 옮긴 이점이 여기서 드러납니다. 그렇지 않았다면 모든 설정을 두 위치에 복사하고, 설정을 바꿀 때마다 양쪽을 모두 수정해야 합니다.

웹 서버를 재시작합니다.

```bash
service nginx restart
```

웹 서버를 재시작할 때 다음 문제가 발생할 수 있습니다.

```text
systemctl status nginx.service
...
[...] could not build server_names_hash, you should increase server_names_hash_bucket_size: 64
...
```

그렇다면 nginx.conf에서 다음 줄의 주석을 해제할 수 있습니다.

```nginx
# server_names_hash_bucket_size 64;
```

그래도 문제가 있다면 크기를 128까지 늘려 봅니다.

### 대체 서비스 {#alt-svc}

[Alt-Svc 헤더][Alt-Svc Header]로 onion 서비스의 존재를 알릴 수 있습니다. 이는 클라이언트에게 Tor로 서비스에 접근할 수 있음을 알리며, 이를 지원하는 일부 클라이언트는 이 헤더를 보면 해당 방식으로 연결합니다. nginx 설정 예제는 다음과 같습니다.

```nginx
add_header Alt-Svc 'h2="qKnF…sKq7.onion:443"; ma=86400; persist=1';
```

설정 시 유의할 사항:

- 축약된 onion 이름을 자신의 이름으로 바꿉니다.
- 예제에서는 443번 포트를 사용하지만 필수는 아니며 다르게 설정할 수 있습니다.
- TLS 연결이 onion 서비스에서 종료되는 것이 아니므로 HTTPS에는 일반적인 비 onion TLS 인증서를 사용할 수 있습니다.

[Alt-Svc Header]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Alt-Svc

## 주의 사항 {#gotchas}

다음 사항을 알아 두어야 합니다.

- 앞서 설명했듯 마스토돈 프런트엔드의 일부 URL은 사용자를 HTTPS URL로 강제 이동시킵니다. 계속하려면 URL을 수동으로 HTTP로 바꿔야 합니다.
- 이미지 등 여러 리소스는 **여전히** 일반 공개 인터넷 도메인으로 제공됩니다. 사용자가 얼마나 신중해야 하거나 신중하고 싶은지에 따라 문제가 될 수 있습니다.
