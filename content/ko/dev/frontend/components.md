---
title: 컴포넌트
description: 마스토돈 프런트엔드는 React Router 5와 Redux 기반의 클라이언트 측 React 앱입니다. 이 문서는 마스토돈 UI 개발을 빠르게 소개합니다.
menu:
    docs:
        parent: frontend
        weight: 10
---

## 위치와 파일 {#locations--files}

마스토돈의 React 컴포넌트는 다음 폴더 중 하나에 있습니다.

- `app/javascript/mastodon/components`: 여러 화면과 기능에서 재사용할 수 있는 UI 컴포넌트입니다.
- `app/javascript/mastodon/features`: 페이지(또는 “열”) 및 특정 기능에 사용되는 위젯입니다.

새 컴포넌트나 기능을 만들 때는 다음을 따릅니다.

- 새 폴더를 만들고 루트에 index.tsx(또는 .ts)를 둡니다.
- 폴더와 이름이 있는 파일에는 snake_case 명명 규칙을 사용합니다.

재사용할 새 컴포넌트를 만들 때는 `component_name.stories.tsx` 파일을 만들어 Storybook에 상태와 변형을 문서화합니다.

스타일을 지정하려면 `styles.module.scss` 파일을 추가하여 CSS Modules를 사용합니다. 폴더 하나에 여러 CSS 파일이 필요하면 `component_name.module.scss`를 사용합니다. 자세한 내용은 [스타일 지정 문서](/dev/frontend/css-and-styling)를 확인합니다.

## 일반적인 팁과 지침 {#general-tips-and-guidelines}

- React 컴포넌트는 클래스가 아닌 함수로 작성합니다.
- 새 컴포넌트와 유틸리티를 작성할 때는 TypeScript를 사용합니다.
- 타입이 없는 기존 JS 코드를 수정할 때는 먼저 TS로 변환하는 것이 적절한지 고려합니다. 다만 범위를 벗어나고 파일이 복잡하다면 무리하게 변환하지 않습니다.
- 같은 로직을 재사용하게 된다면 별도 컴포넌트나 React 훅으로 분리하는 것을 고려합니다.
- 일반적으로 하나의 “거대 컴포넌트”에 속성을 추가하기보다는 여러 전문 컴포넌트를 조합하는 방식을 권장합니다.
