---
title: 코드 구조
description: 코드베이스의 각 부분을 어디에서 찾을 수 있는지 안내합니다.
menu:
  docs:
    weight: 30
    parent: dev
---

## 코드 구조 {#structure}

다음 개요는 완전하거나 절대적인 기준이 아니라 애플리케이션 구조를 파악하는 데 도움이 되는 대략적인 안내입니다.

### Ruby {#ruby}

`app/controllers`
: 비즈니스 로직을 템플릿에 연결하는 코드입니다.

`app/helpers`
: 공통 작업 등 뷰에서 사용할 수 있는 코드입니다.

`app/lib`
: 다른 분류에 속하지 않는 코드입니다.

`app/models`
: 데이터 엔터티와 관련 메서드를 나타냅니다.

`app/policies`
: 관련 메서드를 호출하기 전에 수행하는 권한 검사와 기타 검증입니다.

`app/serializers`
: 모델에서 JSON을 생성하는 코드입니다.

`app/services`
: 여러 모델이 관여하는 복잡한 논리 연산입니다.

`app/views`
: HTML이나 기타 출력을 생성하는 템플릿입니다.

`app/workers`
: 요청과 응답 주기 밖에서 실행되는 코드입니다.

`spec`
: 자동화된 테스트 모음입니다.

### JavaScript {#javascript}

`app/javascript/mastodon`
: 프런트엔드 React.js 애플리케이션 코드입니다.

`app/javascript/packs`
: React.js를 사용하지 않는 페이지의 코드입니다.

### CSS와 기타 에셋 {#assets}

`app/javascript/images`
: 이미지입니다.

`app/javascript/styles`
: Sass를 통해 CSS로 변환되는 코드입니다.

### 현지화 {#localizations}

`config/locales`
: YML 형식의 서버 측 현지화입니다.

`app/javascript/mastodon/locales`
: JSON 형식의 클라이언트 측 현지화입니다.

모든 로캘 파일은 형식과 키 순서를 일관되게 유지하도록 정규화되며, 이를 통해 버전 관리에서 변경되는 내용을 최소화합니다.

- `bundle exec i18n-tasks normalize`를 실행하여 서버 측 번역을 정규화합니다.
- `yarn run i18n:extract`를 실행하여 클라이언트 측 번역을 `en.json`으로 추출하고 정규화합니다.
