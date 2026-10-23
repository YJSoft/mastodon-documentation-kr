---
title: 새 서버 설정하기
description: 마스토돈 설치 후 할 일
menu:
  docs:
    weight: 50
    parent: admin
---

## 관리자 계정 만들기 {#admin}

기본적으로 브라우저에서 가입이 비활성화되어 있으므로 명령줄로 관리자 권한 계정을 만들어야 합니다. 사용자명을 `alice`라고 가정하면 다음과 같습니다.

```bash
RAILS_ENV=production bin/tootctl accounts create \
  alice \
  --email alice@example.com \
  --confirmed \
  --role Owner
```

무작위로 생성된 비밀번호가 터미널에 표시됩니다.

새 관리자 계정을 승인해야 합니다.

```bash
RAILS_ENV=production bin/tootctl accounts modify alice --approve
```

{{<hint style="warning">}}
마스토돈 4.0 이전에는 역할이 `user`, `moderator`, `admin` 중 하나로 고정되어 있었습니다. 마스토돈 4.0부터는 사용자 정의 역할 시스템이 있으며 기본 역할로 `Moderator`, `Admin`, `Owner`가 생성됩니다. 사용자 정의 역할 이름은 대소문자를 구분합니다.
{{</hint>}}

## 서버 정보 입력 {#info}

로그인한 다음 **사이트 설정** 페이지(**환경설정** -> **관리**)로 이동합니다. 이 정보를 입력해야 하는 기술적 요건은 없지만, 사람을 위한 서버 운영에는 필수적인 것으로 여겨집니다.

| 설정 | 의미 |
| :--- | :--- |
| 연락처 사용자명 | 서버 소유자가 누구인지 알 수 있도록 자신의 사용자명을 입력합니다. |
| 업무용 이메일 | 계정에 접근하지 못하는 사람이나 계정이 없는 사람도 연락할 수 있는 이메일 주소입니다. |
| 서버 설명 | 이 서버를 왜 시작했나요? 누구를 위한 서버인가요? 어떤 점이 다른가요? |
| 사용자 정의 확장 정보 | 다양한 정보를 넣을 수 있지만 **행동 강령**을 권장합니다. |

모두 입력한 다음 “변경 사항 저장”을 클릭합니다.
