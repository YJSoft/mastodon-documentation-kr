---
title: 상태 관리
description: 마스토돈 프런트엔드에서 데이터와 상태를 관리하는 방법을 알아봅니다.
menu:
  docs:
    parent: frontend
    weight: 20
---

## 어떤 종류의 상태인가요? {#which-type-of-state}

전역 상태에는 Redux를 사용하지만, 모든 상태를 Redux에 넣어야 하는 것은 아닙니다.

UI 컴포넌트 내부에서만 사용하고 탐색 중에 유지할 필요가 없다면 **React 컴포넌트 상태를 사용합니다**.

뷰와 탐색 사이에서도 유지해야 한다면 **Redux 상태를 사용합니다**. 원격 데이터를 일종의 캐시로 저장하는 데에도 Redux를 사용합니다.

## Redux 슬라이스 {#redux-slices}

새 기능의 상태에는 액션과 리듀서를 별도 파일로 나누는 대신 Redux [슬라이스 패턴](https://redux-toolkit.js.org/tutorials/quick-start#create-a-redux-state-slice)을 사용해야 합니다. 슬라이스는 `app/javascript/mastodon/reducers/slices`에 있습니다.

## 기타 지침 {#other-guidelines}

- 새 상태 로직을 작성할 때는 TypeScript를 사용합니다.
- 새 기능을 구현할 때는 Immutable.js를 사용하지 않습니다.
