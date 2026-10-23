---
title: nginx를 통해 객체 스토리지 프록시하기
description: 마스토돈의 사용자 업로드 파일을 자신의 도메인에서 제공하기
---

## 개요 {#summary}

Amazon S3, Wasabi, Google Cloud 등의 객체 스토리지와 마스토돈을 함께 사용하면 기본적으로 파일 URL은 스토리지 제공자를 거칩니다. 여기에는 다음 단점이 있습니다.

- 대역폭은 보통 사용량에 따라 과금되며 매우 비쌉니다.
- 나중에 제공자를 바꾸면 URL이 깨집니다.

## 프록시 {#proxying}

자신의 도메인에서 파일을 제공하면서 캐싱을 적용할 수 있습니다. 마스토돈에서는 새 파일이 스트리밍 API로 새 게시물에 표시되거나 연합으로 공유될 때 여러 클라이언트가 동시에 접근하는 경우가 많고, 오래된 콘텐츠는 접근 빈도가 낮습니다. 따라서 캐싱만으로는 프록시가 실제 객체 스토리지에서 사용하는 대역폭을 크게 줄이지 못합니다. 이를 해결하려면 한 번에 하나의 프록시 요청만 이루어지도록 캐시 잠금 메커니즘을 구현할 수 있습니다.

다음은 이를 구현하는 nginx 설정 예제입니다.

```nginx
server {
  listen 443 ssl http2;
  listen [::]:443 ssl http2;
  server_name files.example.com;
  root /var/www/html;

  ssl_certificate     /etc/ssl/certs/ssl-cert-snakeoil.pem;
  ssl_certificate_key /etc/ssl/private/ssl-cert-snakeoil.key;

  keepalive_timeout 30;

  location = / {
    index index.html;
  }

  location / {
    try_files $uri @s3;
  }

  set $s3_backend 'https://YOUR_BUCKET_NAME.YOUR_S3_HOSTNAME';

  location @s3 {
    limit_except GET {
      deny all;
    }

    resolver 8.8.8.8;
    proxy_set_header Host YOUR_BUCKET_NAME.YOUR_S3_HOSTNAME;
    proxy_set_header Connection '';
    proxy_set_header Authorization '';
    proxy_hide_header Set-Cookie;
    proxy_hide_header 'Access-Control-Allow-Origin';
    proxy_hide_header 'Access-Control-Allow-Methods';
    proxy_hide_header 'Access-Control-Allow-Headers';
    proxy_hide_header x-amz-id-2;
    proxy_hide_header x-amz-request-id;
    proxy_hide_header x-amz-meta-server-side-encryption;
    proxy_hide_header x-amz-server-side-encryption;
    proxy_hide_header x-amz-bucket-region;
    proxy_hide_header x-amzn-requestid;
    proxy_ignore_headers Set-Cookie;
    proxy_pass $s3_backend$uri;
    proxy_intercept_errors off;

    proxy_cache CACHE;
    proxy_cache_valid 200 48h;
    proxy_cache_use_stale error timeout updating http_500 http_502 http_503 http_504;
    proxy_cache_lock on;

    expires 1y;
    add_header Cache-Control public;
    add_header 'Access-Control-Allow-Origin' '*';
    add_header X-Cache-Status $upstream_cache_status;
    add_header X-Content-Type-Options nosniff;
    add_header Content-Security-Policy "default-src 'none'; form-action 'none'";
  }
}
```

{{< hint style="info" >}}
객체 스토리지 제공자의 IP가 항상 같지는 않을 수 있으므로 nginx가 값에 대해 DNS 조회를 수행하도록 `$s3_backend` 변수를 사용합니다.
실제로 제공자마다 패턴도 다를 수 있습니다.
예를 들어 DigitalOcean의 패턴은 https://YOUR_BUCKET_NAME.YOUR_S3_HOSTNAME/YOUR_BUCKET_NAME 입니다.
{{</ hint >}}

이 설정은 다음 작업을 수행합니다.

- 객체 스토리지 제공자에 대한 GET 외 모든 요청을 차단합니다.
- 객체 스토리지 제공자에 인증된 요청이 전달되지 않게 합니다.
- 객체 스토리지 제공자가 쿠키를 설정하지 못하게 합니다.
- 객체 스토리지 제공자가 반환하는 불필요한 헤더를 제거합니다.
- 유효한 파일을 최대 48시간 캐시합니다.
- 객체 스토리지를 사용할 수 없으면 오래된 캐시를 허용합니다.
- 캐시 잠금으로 객체 스토리지에 대한 동시 요청을 방지합니다.
- 반환되는 모든 파일을 브라우저에서 최대 1년간 캐시할 수 있게 합니다.
- 마스토돈 웹 UI에 필요한 CORS 헤더를 추가합니다.
- 요청의 캐시 적중 여부를 알려 주는 특별한 헤더를 추가합니다.

다음 값을 바꿔야 합니다.

- `files.example.com`
- `YOUR_BUCKET_NAME`
- `YOUR_S3_HOSTNAME`

실제 값으로 바꿉니다. 설정을 `/etc/nginx/sites-available/files.example.com`에 저장하고 다음과 같이 활성화합니다.

```bash
ln -s /etc/nginx/sites-available/files.example.com /etc/nginx/sites-enabled/
systemctl reload nginx
```

SSL 인증서도 받아야 합니다.

```bash
certbot --nginx -d files.example.com
systemctl reload nginx
```

마지막으로 마스토돈이 새 프록시를 사용하여 파일 URL을 생성하게 합니다. 마스토돈의 `.env.production`에 다음을 추가합니다.

```bash
S3_ALIAS_HOST=files.example.com
```

선택 사항: S3_ALIAS_HOST가 301 리디렉션 등을 사용한다면 최종 위치를 EXTRA_MEDIA_HOSTS에 추가합니다.

```bash
EXTRA_MEDIA_HOSTS=https://data.example1.com,https://data.example2.com
```

그리고 마스토돈을 재시작합니다.

```bash
systemctl restart mastodon-sidekiq
systemctl reload mastodon-web
```

{{< hint style="success" >}}
**이제 브라우저에서 마스토돈에 접속하여 모든 항목이 올바르게 불러와지는지 확인할 수 있습니다.**
{{< /hint >}}

## 이전 {#migration}

이전에 로컬에서 파일을 제공하다가 프록시 방식으로 이전했다면, “이전” 미디어 URL이 여전히 유통되어 한동안 서버에 해당 요청이 계속 들어온다는 점을 기억합니다. `nginx.conf`의 `location ^~ /system/` 절에 `rewrite`나 `redirect` 규칙을 추가하여 해당 트래픽을 새 위치로 보내는 것이 좋습니다.
