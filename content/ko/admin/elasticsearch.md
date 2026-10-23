---
title: 전문 검색 설정하기
description: 작성하거나 좋아요를 누르거나 멘션된 게시물, 공개 색인 가능 게시물 및 계정을 검색하도록 Elasticsearch 설정하기
aliases:
- /admin/optional/elasticsearch
menu:
  docs:
    weight: 40
    parent: admin
---

마스토돈은 Elasticsearch가 있으면 전문 검색을 지원합니다. 이 기능을 구성할 것을 강력히 권장합니다.

마스토돈의 전문 검색으로 로그인한 사용자는 다음 항목을 찾을 수 있습니다.
- 검색 결과에 표시되도록 동의한 계정의 공개 게시물
- 자신의 게시물
- 자신을 향한 멘션
- 자신의 좋아요
- 자신의 북마크
- 계정(표시 이름, 사용자명, 자기소개)

전체 데이터베이스에서 임의의 문자열을 검색하는 것은 의도적으로 허용하지 않습니다.

{{< hint style="warning" >}}
Elasticsearch는 상당한 메모리를 요구하며 마스토돈 자체의 요구량을 쉽게 넘을 수 있습니다.
{{< /hint >}}

## Elasticsearch 설치 {#install}

{{< hint style="info" >}}
마스토돈은 현재 지원이 종료된 Elasticsearch 버전 7에서 테스트되었습니다. OpenSearch와 Elasticsearch 8, 9도 지원할 것으로 보이지만 해당 구성은 공식 지원 대상이 아닙니다. 이 문서의 설치 지침은 Elasticsearch 7에만 해당합니다.
{{< /hint >}}

공식 Elasticsearch 저장소를 apt에 추가합니다.

```bash
wget -O /usr/share/keyrings/elasticsearch.asc https://artifacts.elastic.co/GPG-KEY-elasticsearch
echo "deb [signed-by=/usr/share/keyrings/elasticsearch.asc] https://artifacts.elastic.co/packages/7.x/apt stable main" > /etc/apt/sources.list.d/elastic-7.x.list
```

이제 Elasticsearch를 설치할 수 있습니다.

```bash
apt update
apt install elasticsearch
```

{{< hint style="warning" >}}
**보안 경고:** Elasticsearch는 기본적으로 localhost에만 바인딩하여 외부 네트워크에서 접근할 수 없도록 되어 있습니다. `/etc/elasticsearch/elasticsearch.yml`의 `network.host`에서 바인딩 주소를 확인할 수 있습니다. 인증 계층이 없으므로 Elasticsearch에 접근할 수 있는 사람은 그 안의 모든 데이터에 접근하고 수정할 수 있습니다. 따라서 접근을 안전하게 보호하는 것이 매우 중요합니다. [주 설치 지침](../prerequisites/#install-a-firewall-and-only-allow-ssh-http-and-https-ports)처럼 22, 80, 443 포트만 노출하는 방화벽을 권장합니다. 여러 호스트를 사용한다면 내부 트래픽을 보호하는 방법을 알아야 합니다.
{{< /hint >}}

Elasticsearch를 시작하기 전에 RAM 사용량을 제한할 수 있습니다. 다음 내용으로 새 파일 `/etc/elasticsearch/jvm.options.d/limit-ram.options`를 만들어 RAM 한도를 설정합니다.

```java-properties
# Limit RAM size to 24 GB
-Xms16g
-Xmx24g
```

이 설정은 시작 시점부터 RAM 16GB를 예약하고 최대 24GB까지 사용하게 합니다. [Elasticsearch 메모리 관리 및 문제 해결](https://www.elastic.co/blog/managing-and-troubleshooting-elasticsearch-memory/)도 확인합니다.


{{< hint style="info" >}}
Elasticsearch 클러스터 성능을 극대화하려면 해당 컴퓨터의 다른 서비스에 영향을 주지 않으면서 지속적으로 제공할 수 있는 RAM 용량을 파악하고 `Xms`와 `Xmx`를 모두 그 값으로 설정합니다. Elasticsearch가 이 메모리를 예약하여 항상 전부 사용할 수 있으므로 검색이 많은 상황에서 성능이 향상됩니다.
{{< /hint >}}

Elasticsearch를 시작합니다.

```bash
systemctl daemon-reload
systemctl enable --now elasticsearch
```

## 마스토돈 설정 {#config}

`.env.production`을 편집하여 다음 변수를 추가합니다.

```bash
ES_ENABLED=true
ES_HOST=localhost
ES_PORT=9200
ES_PRESET= # single_node_cluster, small_cluster or large_cluster
# ES_USER=
# ES_PASS=
```

_참고_: TLS를 사용한다면 호스트명 앞에 `https://`를 붙입니다. 예: `https://elastic.example.com`

### 올바른 사전 설정 선택 {#choosing-the-correct-preset}

`ES_PRESET` 값은 Elasticsearch 규모에 따라 결정되며 구성에 가장 적절한 인덱스 샤드 및 복제본 수를 설정하는 데 사용됩니다.
- Elasticsearch 클러스터에 노드가 하나뿐이라면 `single_node_cluster`를 사용합니다. 인덱스는 복제본 없이 구성됩니다.
- 클러스터 노드가 6개 미만이면 `small_cluster`를 사용합니다. 인덱스에 복제본 1개를 구성합니다.
- 클러스터 노드가 6개 이상이면 `large_cluster`를 사용합니다. 더 많은 노드에 분산되도록 `small_cluster`보다 많은 샤드를 구성합니다.

한 컴퓨터에서 여러 마스토돈 서버를 실행하며 모두 같은 Elasticsearch 설치를 사용할 계획이라면, 인덱스를 구분하도록 각각 고유한 `ES_PREFIX` 값을 설정해야 합니다.

### 보안 {#security}

기본적으로 Elasticsearch는 인증을 처리하지 않으며 모든 요청이 전체 관리자 권한으로 이루어집니다. 클러스터의 Elasticsearch 보안 기능을 구성할 것을 강력히 권장합니다.

설정 방법은 [공식 문서](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/security-minimal-setup.html)를 참고합니다. 다음 과정을 안내합니다.
- 보안 기능 활성화(`xpack.security.enabled: true`)
- 내장 사용자의 비밀번호 생성

그런 다음 마스토돈 연결용 사용자 정의 역할을 만들 수 있습니다.

예를 들어 다음과 같습니다. Elastic 관리자 비밀번호를 사용하도록 코드를 조정합니다.

```sh
curl -X POST -u elastic:admin_password "localhost:9200/_security/role/mastodon_full_access?pretty" -H 'Content-Type: application/json' -d'
{
  "cluster": ["monitor"],
  "indices": [{
    "names": ["*"],
    "privileges": ["read", "monitor", "write", "manage"]
  }]
}
'
```

[Elasticsearch 역할 생성 문서](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/security-api-put-role.html)

역할을 만들면 마스토돈 서버용 사용자를 만들고 해당 역할을 지정할 수 있습니다.

예를 들어 다음과 같습니다. Elastic 관리자 비밀번호를 사용하고 새 `mastodon` 사용자의 비밀번호를 지정하도록 코드를 조정합니다.

```sh
curl -X POST -u elastic:admin_password "localhost:9200/_security/user/mastodon?pretty" -H 'Content-Type: application/json' -d'
{
  "password" : "l0ng-r4nd0m-p@ssw0rd",
  "roles" : ["mastodon_full_access"]
}
'
```

[Elasticsearch 사용자 생성 문서](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/security-api-put-user.html)

이제 새 사용자의 자격 증명을 사용하도록 마스토돈을 설정해야 합니다.

`.env.production`에서 설정을 조정합니다.

```bash
ES_USER=mastodon
ES_PASS=l0ng-r4nd0m-p@ssw0rd
```

모두 완료했습니다. 이제 Elasticsearch 서버가 훨씬 안전해졌을 것입니다!

#### 공유 환경에서 권한 줄이기 {#reduced-permissions-in-shared-environments}

여러 마스토돈 설치나 다른 앱 등이 같은 ES 서버를 공유한다면, 위의 `ES_PREFIX`로 생성된 검색 인덱스를 분리하는 것 외에도 만든 역할의 접근 권한을 더 제한할 수 있습니다.

예를 들어 `"names": ["*"]`를 `"names": ["app_prefix_*"]`로 바꾸면 해당 역할의 사용자는 적절한 인덱스에 대해서만 작업할 수 있습니다. 여기서 `app_prefix`는 인덱스 접두사로 사용하는 값과 일치해야 합니다.

### 인덱스 채우기 {#populate-the-indices}

새 설정을 저장한 다음 마스토돈 프로세스를 재시작하여 적용합니다.

```bash
systemctl restart mastodon-sidekiq
systemctl reload mastodon-web
```

이제 Elasticsearch 인덱스를 만들고 데이터로 채웁니다.

```bash
su - mastodon
cd live
RAILS_ENV=production bin/tootctl search deploy
```

{{< hint style="info" >}}
Elasticsearch 인덱스 생성에는 JVM(Java 가상 머신)이 제공하는 것보다 많은 메모리가 필요할 수 있습니다. 생성 중 Elasticsearch가 중단된다면 더 많은 메모리를 할당해 봅니다.

1. ```/etc/elasticsearch/jvm.options.d/``` 디렉터리에 파일을 만들고 엽니다. 예: ```nano /etc/elasticsearch/jvm.options.d/ram.options```
2. 다음 텍스트를 추가하고 필요에 맞게 메모리 할당량을 조정합니다. 일반적으로 Elasticsearch에는 가용 메모리의 약 25~50%를 사용합니다. 가용량보다 많은 메모리를 할당하지 않습니다.

    ```java-properties
    # Xms represents the initial size of total heap space
    # Xmx represents the maximum size of total heap space
    # Both values should be the same
    -Xms2048m
    -Xmx2048m
    ```

3. 파일을 저장합니다.
4. ```systemctl restart elasticsearch```로 Elasticsearch를 재시작합니다.
5. 인덱스 생성을 다시 시도합니다. 여전히 중단된다면 더 큰 값으로 설정해 봅니다.
{{< /hint >}}

## 다른 언어의 검색 최적화 {#search-optimization-for-other-languages}

기본 분석기는 영어와 다른 서구 언어에 맞춰져 있어 다른 언어에서는 성능이 낮을 수 있습니다. Elasticsearch가 지원하는 어떤 언어로든 이 설정을 변경할 수 있습니다. 변경 준비에는 [chewy 인덱스 문서][chewy index docs]가 유용할 수 있습니다.

{{< hint style="warning" >}}
언어 지원 추가에는 코드 변경이 필요하며 Ruby 코드 수정과 ES 확장 설치에 익숙한 경우에만 시도해야 합니다.
{{< /hint >}}

[chewy index docs]: https://github.com/toptal/chewy?tab=readme-ov-file#index-definition

### 중국어 검색 최적화 {#chinese-search-optimization}

Elasticsearch에서 인덱스를 만들기 전에 다음 확장을 반드시 설치합니다.

- [elasticsearch-analysis-ik](https://github.com/medcl/elasticsearch-analysis-ik)
- [elasticsearch-analysis-stconvert](https://github.com/medcl/elasticsearch-analysis-stconvert)

설치 후에는 검색 인덱스를 생성하는 코드 정의를 수정해야 합니다. 모든 인덱스 정의 파일(`app/chewy/*_index.rb`)에서 다음과 같이 변경합니다.

- 모든 `tokenizer: 'VALUE'`(whitespace, standard, keyword 등)를 `tokenizer: 'ik_max_word'`로 바꿉니다.
- `analyzer: { content: ... }` 정의가 있는 모든 인덱스에서 `filter`와 `analyzer` 절 사이에 다음을 추가합니다.

  ```ruby
    char_filter: {
      tsconvert: {
        type: 'stconvert',
        keep_both: false,
        delimiter: '#',
        convert_type: 't2s',
      },
    },
  ```

- 같은 파일의 모든 `content: ...` 절에 `char_filter: %w(tsconvert)` 옵션을 추가하여 이 필터를 사용합니다.
