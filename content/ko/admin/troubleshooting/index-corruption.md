---
title: 데이터베이스 인덱스 손상
description: 데이터베이스 인덱스 손상을 복구하는 방법
menu:
  docs:
    weight: 10
    parent: admin-troubleshooting
---

비교적 흔한 설정 문제로 데이터베이스 전체의 인덱스가 손상될 수 있습니다. 이 페이지에서는 발생 원인과 해결 방법을 설명합니다.

## 로캘 데이터와 정렬 규칙 {#explanation}

사용자명이나 게시물 식별자 같은 데이터베이스의 텍스트 값은 문자 순서와 대소문자 변환 방식을 정의하는 정렬 규칙으로 비교됩니다.
마스토돈은 데이터베이스를 설정할 때 기본 정렬 규칙을 포함한 데이터베이스 서버의 기본 로캘 설정을 사용합니다. 이 값은 흔히 운영 체제 설정으로 정해집니다.

안타깝게도 2018년 말 `glibc` 업데이트에서 여러 로캘의 정렬 규칙이 바뀌었습니다. 따라서 영향을 받은 로캘의 데이터베이스는 텍스트 값을 다른 순서로 정렬하게 됩니다.
데이터베이스 인덱스는 인덱싱하는 값의 순서에 의존하는 알고리즘 구조이므로 일부 인덱스에 불일치가 생깁니다.

자세한 정보: https://wiki.postgresql.org/wiki/Locale_data_changes https://postgresql.verite.pro/blog/2018/08/27/glibc-upgrade.html

## 이 문제의 영향을 받나요? {#am-i-affected}

데이터베이스의 정렬 설정이 `C` 또는 `POSIX`가 아니고(`SELECT datcollate FROM pg_database WHERE datname = current_database();`로 확인 가능),
glibc 2.28 이전 버전을 사용한 적이 있으며 2.28 이상으로 업데이트한 직후 데이터베이스 인덱스를 다시 만들지 않았다면 인덱스가 일치하지 않을 수 있습니다.

{{< hint style="info" >}}
PgHero의 “중복 인덱스” 경고 때문에 이 페이지를 찾았을 수도 있습니다. 이 경고는 때때로 마스토돈 배포나 업데이트 문제를 나타낼 수 있지만, **데이터베이스 인덱스 손상과는 관계가 없으며 데이터베이스의 기능상 문제를 나타내지 않습니다**.
{{< /hint >}}

[PostgreSQL의 `amcheck` 모듈](https://www.postgresql.org/docs/10/amcheck.html)로 인덱스 일관성을 검사할 수 있습니다. 데이터베이스 서버의 슈퍼유저로 마스토돈 데이터베이스에 연결하고 다음을 실행합니다. 시간이 걸릴 수 있습니다.

```SQL
CREATE EXTENSION IF NOT EXISTS amcheck;
SELECT bt_index_check(c.oid)
FROM pg_index i
JOIN pg_class c ON i.indexrelid = c.oid
WHERE c.relname IN ('index_account_domain_blocks_on_account_id_and_domain',
  'index_account_proofs_on_account_and_provider_and_username',
  'index_accounts_on_username_and_domain_lower', 'index_accounts_on_uri',
  'index_accounts_on_url', 'index_conversations_on_uri',
  'index_custom_emoji_categories_on_name',
  'index_custom_emojis_on_shortcode_and_domain',
  'index_devices_on_access_token_id', 'index_domain_allows_on_domain',
  'index_domain_blocks_on_domain', 'index_email_domain_blocks_on_domain',
  'index_invites_on_code', 'index_markers_on_user_id_and_timeline',
  'index_media_attachments_on_shortcode', 'index_preview_cards_on_url',
  'index_statuses_on_uri', 'index_tags_on_name_lower',
  'index_tombstones_on_uri', 'index_unavailable_domains_on_domain',
  'index_users_on_email', 'index_webauthn_credentials_on_external_id'
);
```

오류가 발생하면 데이터베이스가 손상되어 수정이 필요합니다. 오류가 없어도 확실히 하려면 더 정밀한 검사가 필요할 수 있습니다.
앞의 검사와 달리 정밀 검사는 실행 중 테이블을 잠그므로 서버의 가용성에 영향을 줍니다.

```SQL
CREATE EXTENSION IF NOT EXISTS amcheck;
SELECT bt_index_parent_check(c.oid)
FROM pg_index i
JOIN pg_class c ON i.indexrelid = c.oid
WHERE c.relname IN ('index_account_domain_blocks_on_account_id_and_domain',
  'index_account_proofs_on_account_and_provider_and_username',
  'index_accounts_on_username_and_domain_lower', 'index_accounts_on_uri',
  'index_accounts_on_url', 'index_conversations_on_uri',
  'index_custom_emoji_categories_on_name',
  'index_custom_emojis_on_shortcode_and_domain',
  'index_devices_on_access_token_id', 'index_domain_allows_on_domain',
  'index_domain_blocks_on_domain', 'index_email_domain_blocks_on_domain',
  'index_invites_on_code', 'index_markers_on_user_id_and_timeline',
  'index_media_attachments_on_shortcode', 'index_preview_cards_on_url',
  'index_statuses_on_uri', 'index_tags_on_name_lower',
  'index_tombstones_on_uri', 'index_unavailable_domains_on_domain',
  'index_users_on_email', 'index_webauthn_credentials_on_external_id'
);
```

오류 없이 성공한다면 데이터베이스가 일관된 상태일 것이므로 `db:migrate` 실행 시 마스토돈이 표시하는 경고를 무시해도 안전합니다.

## 문제 해결 {#fixing}

영향을 받았는데 조치를 하지 않으면 시간이 지날수록 데이터베이스 불일치가 심해질 수 있습니다. 따라서 가능한 한 빨리 수정하는 것이 중요합니다.

마스토돈 3.2.2 이상에는 이 손상을 최대한 복구하는 반대화형 스크립트가 포함됩니다. 이전 버전을 사용한다면 먼저 3.2.2로 업데이트합니다. 해당 손상 때문에 3.2.2 데이터베이스 마이그레이션이 실패할 수도 있지만, 그 후 데이터베이스는 3.2.2에 포함된 유지 관리 도구로 복구할 수 있는 상태가 됩니다.

데이터베이스를 수정하기 전에 **마스토돈을 중지하고 데이터베이스를 백업합니다**. 그런 다음 **마스토돈이 계속 중지된 상태에서** 유지 관리 스크립트를 실행합니다.

```bash
RAILS_ENV=production bin/tootctl maintenance fix-duplicates
```

스크립트는 데이터베이스를 순회하여 중복을 자동으로 찾아 수정합니다. 일부 작업은 데이터를 파괴할 수 있습니다. 가장 파괴적인 경우에는 유지할 레코드와 버릴 레코드를 선택하라는 메시지가 표시됩니다. 어떤 경우든 전체 데이터베이스에서 중복을 찾는 데 매우 오랜 시간이 걸립니다.

{{< hint style="warning" >}}
일부 중복 레코드는 같은 사용자명을 사용하는 서로 다른 로컬 사용자처럼 해결할 수 없는 충돌이 있을 수 있습니다. 이런 경우 중복 제거 작업이 **일부 데이터를 파괴할 수 있으며**, 변경 없이 유지할 레코드와 변경할 레코드를 선택해야 합니다.
따라서 이 스크립트는 반대화형입니다. 어떤 경우든 전체 데이터베이스에서 중복을 찾는 데 매우 오랜 시간이 걸립니다.
{{< /hint >}}

{{< hint style="danger" >}}
**유지 관리 스크립트가 인덱스를 일시적으로 제거하므로, 추가 중복이 생기지 않도록 전체 과정 동안 마스토돈을 완전히 중지해야 합니다.**
{{< /hint >}}

## 문제 예방 {#avoiding-the-issue}

문제를 피하려면 libc 업데이트 직후 데이터베이스 인덱스를 다시 만듭니다.
이 작업에는
[SQL 명령 `REINDEX`](https://www.postgresql.org/docs/current/sql-reindex.html)
또는
[`reindexdb` 명령줄 도구](https://www.postgresql.org/docs/current/app-reindexdb.html)
가 유용할 수 있습니다.
