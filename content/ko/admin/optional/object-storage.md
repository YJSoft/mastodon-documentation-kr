---
title: 객체 스토리지
description: 외부 객체 스토리지로 마스토돈 사용자 업로드 파일 제공하기
menu:
  docs:
    weight: 15
    parent: admin-optional
---

사용자 업로드 파일은 주 서버의 파일 시스템이나 외부 객체 스토리지 서버에 저장할 수 있으며, 규모 확장을 위해 외부 스토리지가 필요할 수 있습니다.

## 파일 시스템 사용 {#FS}

사용자 업로드를 저장하는 가장 간단한 방법은 서버의 파일 시스템을 사용하는 것입니다. 기본 동작이며 소규모 서버에 적합합니다.

기본적으로 마스토돈은 설치 디렉터리의 `public/system` 아래에 업로드 파일을 저장하지만 `PAPERCLIP_ROOT_PATH` 환경 변수로 바꿀 수 있습니다.

{{< hint style="info" >}}
`PAPERCLIP_ROOT_PATH`가 `/home/mastodon/live` 아래에 있지 않다면 `mastodon-sidekiq.service`와 `mastodon-web.service`를 편집하여 `ReadWritePaths=/home/mastodon/live`를 `ReadWritePaths=/home/mastodon <PAPERCLIP_ROOT_PATH>`로 바꿔야 합니다.
{{</ hint >}}

기본적으로 파일은 `https://your-domain/system`에서 제공되며 `PAPERCLIP_ROOT_URL`과 `CDN_HOST`로 바꿀 수 있습니다.

{{< hint style="info" >}}
서버의 파일 시스템은 소규모 서버에서 충분히 쓸 만하지만 외부 객체 스토리지를 사용하면 더 쉽게 확장할 수 있습니다.
{{</ hint >}}

{{< hint style="danger" >}}
웹 서버는 파일을 제공하되 목록 조회는 허용하지 않도록 구성해야 합니다. 즉 `https://your-domain/system/`에서 파일 목록을 반환해서는 안 됩니다. 마스토돈과 함께 배포되는 설정 파일을 사용하면 이렇게 되어 있겠지만 다시 확인하는 것이 좋습니다.
{{</ hint >}}

## S3 호환 객체 스토리지 백엔드 {#S3}

마스토돈은 S3 호환 객체 스토리지 백엔드를 사용할 수 있습니다. ACL을 지원하면 일시 정지된 사용자의 콘텐츠를 빠르게 접근 불가 상태로 만들고 비공개 데이터의 보안을 조금 개선할 수 있으므로 권장합니다.

마스토돈은 S3 API(`S3_REGION`, `S3_ENDPOINT`, `S3_BUCKET`,
`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `S3_SIGNATURE_VERSION`,
`S3_OVERRIDE_PATH_STYLE`)를 모든 쓰기, 삭제,
권한 변경 작업에 사용합니다. 여기에는 웹 인터페이스,
마스토돈 API 클라이언트 및 ActivityPub 서버에서의 미디어 업로드,
게시물 수정 또는 삭제 시의 미디어 삭제,
계정 정지 시의 미디어 접근 차단이 포함됩니다.

마스토돈은 모든 '읽기' 작업에 대해 웹 인터페이스, 마스토돈 API 클라이언트,
ActivityPub 서버에 URL을 보냅니다. 따라서 이러한
작업은 익명이며 인증이나 인가가 필요 없고,
일반 HTTP GET 메서드를 사용하므로
리버스 프록시와 CDN을 통해 라우팅하고 캐시할 수 있습니다. 또한
원한다면 URL에 S3 스토리지 제공자 자체와 완전히 다른
호스트명이나 도메인 이름을 포함할 수도 있습니다. URL 구성 방식과
관련 환경 변수는
아래의 자세한 문서를 확인합니다.

S3 스토리지를 활성화하려면 `S3_ENABLED` 환경 변수를 `true`로 설정합니다.

### S3 API 접근용 환경 변수 {#environment-variables-for-s3-api-access}

- `S3_REGION` (기본값은 'us-east-1'이며 AWS S3를 사용하면 필수입니다.
  다른 스토리지 제공자는 필요하지 않을 수 있습니다.)
- `S3_ENDPOINT` (기본값은 'https://s3.<S3_REGION>.amazonaws.com'이며,
  AWS S3 이외의 제공자를 사용하면 필수입니다.)
- `S3_BUCKET=mastodata` (`mastodata`를 자신의
  버킷 이름으로 바꿉니다.)
- `AWS_ACCESS_KEY_ID`와 `AWS_SECRET_ACCESS_KEY`는
  자신의 자격 증명으로 설정해야 합니다.
- `S3_SIGNATURE_VERSION` (기본값은 'v4'이며
  대부분의 스토리지 제공자와 호환됩니다.)
- `S3_OVERRIDE_PATH_STYLE` (`S3_ENDPOINT`가 구성된 경우에만 사용하며,
  스토리지 제공자가 API 작업을 '<S3_BUCKET>.<S3_ENDPOINT>`로
  보내도록 요구하면 `true`로 설정합니다. 도메인 방식입니다.)

### 클라이언트의 미디어 객체 접근용 환경 변수 {#environment-variables-for-client-access-to-media-objects}

- `S3_PROTOCOL` (기본값은 `https`입니다.)
- `S3_HOSTNAME` (기본값은 's3-<S3_REGION>.amazonaws.com'이며,
  AWS S3를 사용하지 않고 `S3_ALIAS_HOST`도 설정하지 않았다면 필수입니다.)
- `S3_ALIAS_HOST` (미디어 URL에 `S3_BUCKET`을 포함하지 않으려면
  `S3_HOSTNAME` 대신 사용할 수 있습니다. 스토리지 제공자 앞에
  리버스 프록시나 CDN이
  준비되어 있어야 합니다.)

앞서 설명했듯 클라이언트가 스토리지 제공자의 미디어 객체에
접근해야 하면 마스토돈은 URL을 보냅니다.
URL은 다음과 같이 구성됩니다.

- `S3_ALIAS_HOST`가 설정되지 않았다면 URL은 다음과 같습니다.
  '<S3_PROTOCOL>://<S3_HOSTNAME>/<S3_BUCKET>/\<object path\>'

- `S3_ALIAS_HOST`가 설정되었다면 URL은 다음과 같습니다.
  '<S3_PROTOCOL>://<S3_ALIAS_HOST>/\<object path\>'

`S3_ALIAS_HOST`를 설정하면 생성되는 URL에 버킷
이름이 포함되지 **않습니다**. 따라서 버킷
이름을 `S3_ALIAS_HOST`에 포함하거나(이른바
'도메인 방식' 객체 접근), `S3_ALIAS_HOST`가
스토리지 제공자에게 요청을 전달할 때 사용하는 URL에 버킷 이름을
포함할 수 있는 리버스 프록시나 CDN을 가리켜야 합니다. 이런
설정을 사용하면 서버의 클라이언트에게 스토리지 제공자 사용을
'숨길' 수 있으므로 최종 URL을 바꾸지 않고
스토리지 제공자를 변경할 수 있습니다.

스토리지 제공자 사용을 숨기는 것 외에도, 제공자에게서 가져온
미디어를 캐시하여
스토리지 제공자의 송신 대역폭 비용을
줄일 수 있습니다. 자체 리버스 프록시나
CDN에서 구현할 수 있습니다.

`EXTRA_MEDIA_HOSTS`로 서버의 미디어를 제공하도록 허용하는
호스트 목록을 추가할 수 있습니다. 사용자 정의 CSS나
소개 페이지에 외부 미디어를 포함하거나,
데이터 스토리지 제공자가 다른 도메인으로 리디렉션한다면 유용합니다.
`EXTRA_MEDIA_HOSTS=https://data.example1.com,https://data.example2.com`

{{< page-ref page="admin/optional/object-storage-proxy.md" >}}

{{< hint style="info" >}}
파일을 제공할 때는 CORS 헤더가 있어야 합니다. 그렇지 않으면 마스토돈 웹 UI의 일부 기능이 작동하지 않습니다. 예: `Access-Control-Allow-Origin: *`
{{</ hint >}}

{{< hint style="info" >}}
파일을 호스팅하는 도메인 이름을 바꾼다면(예: 로컬에서 객체 스토리지로, 또는 객체 스토리지 호스트 간 이전), 변경 최소 1주일 전에 서버의 `Content-Security-Policy` 헤더에 새 도메인을 추가해야 합니다. 마스토돈 서비스 워커가 값을 최대 1주일 캐시하기 때문입니다. 그렇지 않으면 사용자에게 깨진 이미지가 표시됩니다.
{{</ hint >}}

### 선택적 환경 변수 {#optional-environment-variables}

#### `S3_OPEN_TIMEOUT` {#s3_open_timeout}

기본값: 5초

새 HTTP 세션을 열려고 시도할 때 HTTP 처리기가 시간 초과로 처리하기까지의 초 단위 시간입니다.

#### `S3_READ_TIMEOUT` {#s3_read_timeout}

기본값: 5초

HTTP 응답을 기다릴 때 HTTP 처리기가 시간 초과로 처리하기까지의 초 단위 시간입니다.

#### `S3_RETRY_LIMIT` {#s3_retry_limit}

일부 S3 제공자는 특히 마스토돈 서버와 S3 스토리지 사이에 연결 문제가 있을 때 조정이 필요할 수 있습니다. 다른 서버의 게시물에서 미디어가 누락되는 현상으로 나타날 수 있습니다.

기본값은 `0`입니다. 작업자를 필요 이상으로 오래 점유하므로 `3`보다 크게 늘리지 않는 것을 권장합니다.

**버전 이력:**\
4.3.0 - 추가됨

#### `S3_FORCE_SINGLE_REQUEST` {#s3_force_single_request}

기본값: false

큰 파일 처리에 문제가 있다면 `true`로 설정합니다.

#### `S3_ENABLE_CHECKSUM_MODE` {#s3_enable_checksum_mode}

기본값: false

마스토돈이 스토리지 제공자에게서 객체를 가져올 때
객체 체크섬 검증을 활성화합니다. AWS S3에서는
사용할 수 있지만 다른 S3 호환 구현에서는 지원하지 않을 수 있습니다.

#### `S3_STORAGE_CLASS` {#s3_storage_class}

기본값: 없음

AWS S3를 사용한다면 이 변수를 [스토리지
클래스](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
중 하나로 설정할 수 있습니다. 이는 업로드한 객체에 사용할 스토리지와
그에 따른 접근 시간 및 비용에 영향을 줍니다. 클래스를 지정하지 않으면
AWS S3는 `STANDARD` 클래스를 사용하며, 다른 옵션으로는
`REDUCED_REDUNDANCY`, `GLACIER` 등이 있습니다.

#### `S3_MULTIPART_THRESHOLD` {#s3_multipart_threshold}

기본값: 15MB

이 크기 이하의 객체는 한 번의 작업으로
업로드하지만 더 큰 객체는 멀티파트
분할 방식으로 업로드하여 전송 속도와 안정성을 높일 수 있습니다.

#### `S3_PERMISSION` {#s3_permission}

기본값: `public-read`

새 파일 업로드 시 S3 객체 ACL을 정의합니다.
[S3 퍼블릭 액세스
차단](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)
에서 `BlockPublicAcls`를 켜면 `public-read` ACL로 객체를
업로드할 때 실패(403)하므로 주의합니다. 이 경우 `S3_PERMISSION`을
`private`으로 설정합니다.

{{< hint style="danger" >}}
ACL 구성과 관계없이 S3 버킷의
모든 객체를 공개적으로 읽을 수는 있지만
쓰거나 나열할 수는 없도록 설정해야 합니다. 동시에 마스토돈
자체에는 버킷 쓰기 권한이 있어야 합니다. 이 구성은
일반적으로 모든 S3 제공자에서 비슷하며,
흔한 제공자의 설정을 아래에 소개합니다.
{{</ hint >}}

#### `S3_BATCH_DELETE_LIMIT` {#s3_batch_delete_limit}

기본값: `1000`

공식 [Amazon S3
API](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html)
는 한 번의 배치 작업으로 객체 1,000개를 삭제할 수 있지만, 일부 제공자는
단일 요청에서 이렇게 많은 객체를 처리하기 어렵거나 더 낮은
한도를 제공합니다.

#### `S3_BATCH_DELETE_RETRY` {#s3_batch_delete_retry}

기본값: 3

배치 삭제 중 S3 제공자가 간헐적으로 실패하거나
삭제 요청 처리 중 시간 초과될 수 있습니다. 마스토돈은 잠시 기다린 다음
이 최대 횟수만큼 요청을 재시도합니다.

### MinIO {#minio}

MinIO는 S3 객체 제공자의 오픈 소스 구현입니다. 이 절에서는 설치 방법이 아니라 마스토돈용 버킷 구성 방법을 설명합니다.

버킷 안의 객체에 읽기 전용 접근은 허용하되 목록 조회는 허용하지 않는 익명 접근 정책을 설정해야 합니다.

이를 위해 사용자 정의 정책을 설정합니다. `mastodata`를 실제 S3 버킷 이름으로 바꿉니다.
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "*"
                ]
            },
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::mastodata/*"
            ]
        }
    ]
}
```

마스토돈 자체는 버킷에 쓸 수 있어야 하므로 관리자 MinIO 계정(권장하지 않음)이나 마스토돈 전용 계정(권장)에 다음 정책을 연결하여 사용합니다. `mastodata`를 실제 S3 버킷 이름으로 바꿉니다.
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::mastodata/*"
        }
    ]
}
```

MinIO Console 웹 인터페이스나 명령줄 클라이언트(`mcli` / `mc`)에서 이 정책을 설정할 수 있습니다.

#### MinIO Console 사용 {#using-the-minio-console}

MinIO Console 웹 인터페이스에 연결하고 새 버킷을 만들거나 기존 버킷으로 이동합니다.
![MinIO 버킷](/assets/object-storage/minio-bucket.png)

그런 다음 “Access Policy”를 사용자 정의로 설정하여 쓰기와 객체 목록 조회 없이 읽기(`s3:GetObject`)만 허용합니다. 위 내용을 참고합니다.
![MinIO 접근 정책](/assets/object-storage/minio-access-policy.png)

{{< hint style="info" >}}
MinIO Console에서 “Custom” 정책을 설정할 수 없다면 MinIO를 업데이트해야 할 수 있습니다. *standalone* 또는 *filesystem* 모드라면 [`RELEASE.2022-10-24T18-35-07Z`](https://github.com/minio/minio/releases/tag/RELEASE.2022-10-24T18-35-07Z)는 [복잡한 이전 절차](https://min.io/docs/minio/linux/operations/install-deploy-manage/migrate-fs-gateway.html#migrate-from-gateway-or-filesystem-mode) 없이 안전하게 업데이트할 수 있는 버전입니다.
{{< /hint >}}

새 `mastodon-readwrite` 정책을 만듭니다. 위 내용을 참고합니다.
![MinIO 읽기 및 쓰기 정책](/assets/object-storage/minio-mastodon-readwrite.png)

마지막으로 `mastodon-readwrite` 정책을 가진 새 `mastodon` 사용자를 만듭니다.
![MinIO 마스토돈 사용자](/assets/object-storage/minio-mastodon-user.png)

#### 명령줄 유틸리티 사용 {#using-the-command-line-utility}

[MinIO Client](https://min.io/docs/minio/linux/reference/minio-mc.html) 명령줄 유틸리티로도 같은 작업을 수행할 수 있습니다. 설치 출처에 따라 `mc` 또는 `mcli`라는 이름일 수 있습니다.

새 버킷을 만듭니다.
`mc mb myminio/mastodata`

위의 익명 접근 정책은 `anonymous-readonly-policy.json`으로, 마스토돈 사용자 접근 정책은 `mastodon-readwrite.json`으로 저장합니다. `mastodata`를 새 버킷 이름으로 바꿔야 합니다.

버킷의 익명 접근 정책을 설정합니다.
`mc anonymous set-json anonymous-readonly-policy.json myminio/mastodata`

`mastodon-readwrite` 정책을 추가합니다.
`mc admin policy add myminio mastodon-readwrite mastodon-readwrite.json`

`mastodon` 사용자를 추가합니다. 비밀번호를 바꿉니다.
`mc admin user add myminio mastodon SECRET_PASSWORD`

`mastodon` 사용자에게 `mastodon-readwrite` 정책을 적용합니다.
`mc admin policy set myminio mastodon-readwrite user=mastodon`

### Wasabi Object Storage {#wasabi-object-storage}

새 버킷을 만들고 객체를 익명으로 읽을 수는 있지만 나열할 수는 없도록 정책을 정의합니다.
```json
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Effect": "Allow",
         "Principal": {
           "AWS": "*"
         },
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::mastodata/*"
      }
   ]
}
```

![Wasabi 접근 정책](/assets/object-storage/wasabi-access-policy.png)

{{< hint style="info" >}}
기존 버킷을 사용한다면 Wasabi의 이전 Access Control 설정에서 “Everyone”에 객체 읽기 권한을 부여하지 않았는지 확인합니다. 이 설정은 목록 조회를 허용하며 위에서 정의한 IAM 정책보다 우선합니다.

![Wasabi 접근 제어](/assets/object-storage/wasabi-access-control.png)
{{< /hint >}}

그런 다음 버킷의 읽기와 쓰기 권한을 부여하는 `mastodon-readwrite` 정책을 만듭니다.
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::mastodata/*"
        }
    ]
}
```

![Wasabi 읽기 및 쓰기 정책](/assets/object-storage/wasabi-mastodon-readwrite.png)

마지막으로 새 `mastodon` 사용자를 만들고 `mastodon-readwrite` 정책을 활성화합니다.
![Wasabi 마스토돈 사용자](/assets/object-storage/wasabi-mastodon-user.png)

마스토돈에서는 큰 업로드를 올바르게 처리하도록 `S3_FORCE_SINGLE_REQUEST=true`를 설정해야 합니다.

### DigitalOcean Spaces {#digitalocean-spaces}

DigitalOcean Spaces 버킷에서 “File Listing”이 액세스 키가 있는 사용자로 “Restricted”되어 있는지 확인합니다.

![DigitalOcean Spaces 설정](/assets/object-storage/do-spaces.png)

### Scaleway {#scaleway}

Scaleway Object Storage를 사용하려면 마스토돈 서버 에셋 전용 Scaleway 프로젝트를 만들고 사용자 정의 IAM 정책을 사용할 것을 강력히 권장합니다.

먼저 새 Scaleway 프로젝트와 그 안에 객체 스토리지 버킷을 만듭니다. 객체를 나열할 수 없도록 버킷 공개 범위를 "Private"으로 설정해야 합니다.

![Scaleway 버킷](/assets/object-storage/scaleway-bucket.png)

버킷을 만들었으므로 마스토돈 서버 설정에 사용할 API 키를 만들어야 합니다.

화면 오른쪽 위의 조직 메뉴에서 IAM 설정으로 이동하고 새 IAM 정책(예: `mastodon-media-access`)을 만듭니다.

![Scaleway 정책](/assets/object-storage/scaleway-policy.jpg)

이 정책에는 위에서 만든 Scaleway 프로젝트를 범위로 하여 객체 읽기, 쓰기, 삭제를 허용하는 규칙 하나가 있어야 합니다.

![Scaleway 정책 규칙](/assets/object-storage/scaleway-policy-rules.jpg)

그런 다음 IAM Applications 페이지에서 새 애플리케이션(예: `my-mastodon-instance`)을 만들고 위의 정책을 선택합니다.

마지막으로 방금 만든 애플리케이션을 클릭하고 "API Keys"에서 서버 설정에 사용할 새 API 키를 만듭니다. "Yes, set up preferred Project"를 사용하고 위에서 만든 프로젝트를 이 키의 기본 프로젝트로 선택합니다.

![Scaleway API 키](/assets/object-storage/scaleway-api-key.png)

Access Key ID와 Secret을 복사하여 마스토돈 설정 변수 `AWS_ACCESS_KEY_ID`와 `AWS_SECRET_ACCESS_KEY`에 사용합니다.

### Exoscale {#exoscale}

Exoscale 버킷에는 읽기 ACL이 없어야 합니다. 마스토돈이 객체 자체에 적절한 ACL을 설정합니다.

마스토돈 앱용 API 키를 만들되 Object Storage(`sos`) 서비스와 해당 버킷으로 제한하고 작업에는 제한을 두지 않습니다.

![Exoscale 설정](/assets/object-storage/exoscale.png)

마스토돈에서는 큰 업로드를 올바르게 처리하도록 `S3_FORCE_SINGLE_REQUEST=true`를 설정해야 합니다.

### Cloudflare R2 {#cloudflare-r2}

Cloudflare R2는 ACL을 지원하지 않으므로 마스토돈이 ACL 설정을 시도하지 않도록 해야 합니다. 이를 위해 `S3_PERMISSION` 환경 변수를 빈 문자열로 설정합니다.

{{< hint style="warning" >}}
ACL을 지원하지 않으면 일시 정지된 사용자의 미디어 파일은 계속 접근 가능한 상태로 남습니다.
{{< /hint >}}

마스토돈용 자격 증명을 얻으려면 “Manage R2 API Tokens”에서 “Edit” 권한을 가진 새 API 토큰을 만듭니다.

{{< hint style="warning" >}}
이 절은 현재 작성 중입니다.
{{< /hint >}}
