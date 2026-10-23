---
title: 기술 개요
description: 마스토돈의 아키텍처를 설명합니다.
menu:
  docs:
    weight: 10
    parent: dev
---

<style>
#TableOfContents {display: none}
</style>

## 소개 {#introduction}

마스토돈은 React.js 프런트엔드를 갖춘 Ruby on Rails 애플리케이션입니다. 해당 프레임워크의 표준 관행([MVC] 아키텍처, [REST] API 등)을 따르므로 Rails나 React.js에 익숙하다면 낯설지 않을 것입니다.

개발 환경에서 마스토돈을 작업하는 가장 좋은 방법은 Docker나 Vagrant를 사용하는 대신 시스템에 모든 의존성을 설치하는 것입니다. Ruby, Node.js, PostgreSQL, Redis가 필요하며, 이는 Rails 애플리케이션의 일반적인 의존성 구성입니다.

이 의존성의 설치 안내는 문서의 마스토돈 운영 절에 있는 [소스에서 설치하기](../admin/install) 페이지에서 확인할 수 있습니다. 마스토돈 운영 절의 설치 안내를 따른 다음 [개발 환경 설정하기](../dev/setup) 페이지에서 개발용 환경 구성에 관한 추가 지침을 확인합니다.

### 환경 {#environments}

“환경”은 특정 용도에 맞춘 설정값의 모음입니다.

일반적으로 다음 환경을 사용합니다.

- `development` -- 로컬에서 애플리케이션을 변경하고 유지 관리합니다.
- `test` -- 자동화된 테스트 모음을 실행합니다.
- `staging` -- 최종 사용자에게 기능을 미리 보여 줍니다.
- `production` -- 실제 배포와 사용을 위한 환경입니다.

마스토돈에는 개발, 테스트, 운영 환경을 위한 설정이 제공됩니다.

`RAILS_ENV`의 기본값은 `development`이므로 개발 모드로 실행하기 위해 별도 설정을 추가할 필요가 없습니다. 실제로 마스토돈의 모든 설정에는 개발 환경에 맞는 기본값이 있으므로, 사용자 정의가 필요하지 않으면 `.env` 파일도 필요 없습니다. 개발 환경과 운영 환경의 동작에는 다음과 같은 차이가 있습니다.

- Ruby 코드가 변경되면 자동으로 다시 불러오므로 변경 사항을 확인하기 위해 Rails 서버 프로세스를 재시작할 필요가 없습니다.
- 발생하는 모든 오류는 일반 오류 페이지 뒤에 숨겨지지 않고 브라우저에 스택 추적을 표시합니다.
- Vite는 계속 실행되면서 프런트엔드 파일이 변경되면 JS 및 CSS 에셋을 다시 컴파일하며, 페이지는 자동으로 새로 고침됩니다.
- 캐싱은 기본적으로 비활성화됩니다.
- `db:seed` 중에 이메일이 `admin@localhost:3000`이고 비밀번호가 `mastodonadmin`인 관리자 계정이 자동으로 생성됩니다.

마스토돈과 함께 배포되는 최상위 Docker 설정은 운영 환경에 최적화되어 있어 개발용으로는 매우 부적합합니다. 반면 Vagrant 설정과 `.devcontainer/` 안의 Docker 설정은 운영용이 아니라 개발용으로 특별히 구성되어 있습니다.

[MVC]: https://developer.mozilla.org/en-US/docs/Glossary/MVC
[REST]: https://developer.mozilla.org/en-US/docs/Glossary/REST
