---
title: CSS와 스타일 지정
description: 마스토돈 프런트엔드에서 컴포넌트의 스타일을 지정하는 방법
menu:
  docs:
    parent: frontend
    weight: 30
---

## 배경 {#background}

마스토돈 4.6 이전에는 `components.scss`와 같은 전역 SCSS 파일로 UI 스타일을 지정했습니다. 이 파일들은 자주 커져서 구조를 파악하기 어렵고, 의도하지 않은 부작용 없이 변경하기도 어려워졌습니다.

이를 개선하기 위해 4.6 릴리스의 새 기능을 [CSS Modules](https://github.com/css-modules/css-modules)로 만들기로 했습니다. 그러면 관련 컴포넌트 바로 옆에서 스타일을 정의할 수 있고 스타일 충돌 가능성도 줄어듭니다.

## CSS Modules 사용 방법 {#how-to-use-css-modules}

- 새 React 컴포넌트를 만들 때는 snake_case로 새 폴더를 만들고 `styles.module.scss` 파일을 추가합니다. `.module` 접미사를 빠뜨리면 스타일을 가져올 수 없습니다.
  - 폴더 하나에 여러 CSS 파일이 있으면 관련 하위 컴포넌트 이름과 일치하는 `component_name.module.scss`를 사용합니다.
- 컴포넌트에서 스타일을 가져와 사용합니다: `import classes from './styles.module.scss'`
- CSS Modules의 클래스 이름은 `.card`나 `.actions`처럼 간단하게 유지합니다. BEM 같은 명명 패턴은 필요 없습니다. 단어가 여러 개이면 컴포넌트에서 클래스에 쉽게 접근하도록 camelCase를 사용합니다.
- CSS Modules는 위치와 모듈 이름을 바탕으로 모듈 내 모든 클래스의 이름을 생성하므로, 테마 제작자가 비교적 안정적으로 참조할 수 있습니다.

## 변형의 스타일 지정 {#styling-variants}

컴포넌트의 변형에 스타일을 지정하는 방법은 다음 두 가지가 있습니다.

- `classNames` 유틸리티로 클래스를 조합합니다. 예:
  ```jsx
  <section
    className={classNames(
      classes.wrapper,
      !hasBorder && classes.wrapperWithoutBorder,
    )}
  >
  ```
- 컴포넌트 마크업에 사용자 정의 데이터 속성을 추가하고 이를 바탕으로 스타일을 지정합니다. 예:
  ```jsx
  <section
    className={classes.wrapper}
    data-has-border={hasBorder}
  >
  ```
  ```scss
  .wrapper {
    /* ... */
    &[data-has-border='true'] {
      border: 1px solid var(--color-border-primary);
    }
  }
  ```

## 하위 컴포넌트의 스타일 지정 {#styling-sub-components}

기존 전역 CSS 클래스(예: `.avatar`)를 사용하는 하위 컴포넌트에 스타일을 지정해야 한다면, `:global(.avatar)`처럼 클래스를 감싸 CSS Modules가 생성된 클래스 이름으로 바꾸지 못하도록 할 수 있습니다. 가능하면 이 방법은 피하고 새 로컬 클래스를 만들어 중첩된 컴포넌트에 전달합니다.

## 테마 {#theming}

색상에는 [디자인 토큰](/dev/frontend/design-tokens)을 사용하고, 사용자의 테마 환경설정은 [테마 안내](/dev/frontend/theming)에서 자세히 알아봅니다.
