---
title: 디자인 토큰 참고 자료
description: 마스토돈 4.6에서 도입한 디자인 토큰 개요
menu:
  docs:
    parent: frontend
    weight: 50
---

## 디자인 토큰이란? {#what-are-design-tokens}

디자인 토큰은 색상, 크기 및 기타 디자인 값에 사용 목적을 나타내는 이름을 붙인 것입니다. 각 토큰은 작은 디자인 결정을 나타내므로, UI에서 이미 비슷한 용도로 사용 중인 값과 일관되는 값을 선택하는 데 도움이 됩니다.

마스토돈 4.6에서는 테마 색상과 관련된 _테마 토큰_만 도입했습니다. 간격과 글꼴 크기 등의 추가 토큰은 추후 추가할 예정입니다.

테마 토큰은 [`app/javascript/styles/mastodon/theme`](https://github.com/mastodon/mastodon/tree/main/app/javascript/styles/mastodon/theme)에 정의되어 있습니다.

## 일반적인 구조 {#general-structure}

테마 토큰은 `--color-text-primary`나 `--color-bg-brand-soft`와 같은 형태입니다.

각 토큰 이름의 첫 번째 부분은 `color`처럼 토큰 값의 유형을 나타냅니다.

이름의 두 번째 부분은 토큰의 사용 위치를 나타내는 세 가지 범주 중 하나입니다.

- `-text`
- `-bg` (배경)
- `-border`

토큰 이름의 다음 부분은 `-primary`, `-brand`, `-error`, `-on-brand-base`처럼 의미상의 역할이나 맥락으로 토큰을 더 세분화합니다.

마지막으로 토큰 이름에 추가 수식어가 붙기도 합니다. 예를 들어 대부분의 배경 토큰은 일관된 `-base`, `-soft`, `-softest` 패턴을 따릅니다.

## 토큰 조합하기 {#pairing-tokens}

어떤 토큰을 함께 사용할 수 있는지 항상 명확하지는 않습니다. 다음 지침은 안전하게 토큰 조합을 시작하는 데 도움이 됩니다.

- 일반적으로 한 맥락에서 잘 어울린다고 해서 관련 없는 토큰을 섞어 사용하지 않습니다. 모든 색상 모드에서 충분한 색상 대비를 보장하도록 항상 서로 대응하는 텍스트와 배경 조합을 찾습니다.
  {{< hint style="info" >}}
  예를 들어 `bg-brand-base` 위에 `text-inverted`를 사용하면 어두운 모드에서 읽기 어려워지므로 이렇게 사용해서는 안 됩니다. 대신 `bg-brand-base`에는 `text-on-brand-base`만 사용합니다. 마찬가지로 `text-inverted`는 `bg-inverted`와만 사용합니다.
  {{< /hint >}}

- 중립 텍스트 토큰인 `text-primary`와 `text-secondary`는 다음 중립 배경이나 부드러운 배경 어디에나 안전하게 사용할 수 있습니다.
  - `bg-primary`
  - `bg-secondary`
  - `bg-brand-soft` / `bg-brand-softest`
  - `bg-error-soft` / `bg-error-softest`
  - `bg-warning-soft` / `bg-warning-softest`
  - `bg-success-soft` / `bg-success-softest`

- 또한 텍스트 토큰 `text-brand`, `text-brand-hover`, `text-error`, `text-warning`, `text-success`는 각각 대응하는 `-soft`, `-softest` 배경 및 `bg-primary`, `bg-secondary`와 함께 사용할 수 있습니다.

- 서로 다른 그룹의 의미 토큰을 혼합하지 않습니다. 예를 들어 미적인 이유로 `text-brand`와 `bg-error-softest`를 조합해서는 안 됩니다.

## 참고 자료 {#reference}

### 텍스트 토큰 {#text-tokens}

| 토큰 | 용도 |
|-------|---------|
| `--color-text-primary` | 본문 콘텐츠와 표준 UI 텍스트의 기본 글자색 |
| `--color-text-secondary` | 보조 문구와 메타데이터에 사용하는 약간 흐린 글자색 |
| `--color-text-tertiary` | 덜 두드러지는 콘텐츠의 흐린 글자색(기존) |
| `--color-text-inverted` | 토스트 알림 등 반전된 배경 위의 텍스트 |
| `--color-text-brand` | 강조되거나 상호작용 가능한 텍스트의 브랜드 색상 |
| `--color-text-brand-soft` | 은은한 브랜드 텍스트에 사용하는 부드러운 브랜드 색상(기존) |
| `--color-text-on-brand-base` | 단색 'brand' 배경 위에 배치하는 글자색 |
| `--color-text-brand-on-inverted` | 반전된 배경 위에 배치하는 브랜드 글자색(기존) |
| `--color-text-error` | 오류나 파괴적인 동작을 나타내는 텍스트 |
| `--color-text-on-error-base` | 단색 'error' 배경 위에 배치하는 글자색 |
| `--color-text-warning` | 경고를 나타내는 텍스트 |
| `--color-text-on-warning-base` | 단색 'warning' 배경 위에 배치하는 글자색 |
| `--color-text-success` | 유효한 사용자 입력 등 성공을 나타내는 텍스트 |
| `--color-text-on-success-base` | 단색 'success' 배경 위에 배치하는 글자색 |
| `--color-text-disabled` | 비활성화된 컨트롤의 텍스트(기존) |
| `--color-text-on-disabled` | 'disabled' 배경 위에 배치하는 텍스트(기존) |
| `--color-text-bookmark-highlight` | 선택된 '북마크' 동작의 아이콘 색상(기존) |
| `--color-text-favourite-highlight` | 선택된 '좋아요' 동작의 아이콘 색상(기존) |
| `--color-text-on-media` | 미디어 모달 안에 배치하는 텍스트(기존) |
| `--color-text-status-links` | 게시물 안의 링크 색상(기존) |


### 배경 토큰 {#background-tokens}

#### 중립 배경 {#neutral-backgrounds}

| 토큰 | 용도 |
|-------|---------|
| `--color-bg-primary` | 주요 콘텐츠 영역의 기본 배경 |
| `--color-bg-secondary` | 표면을 은은하게 구분하는 보조 배경 |
| `--color-bg-tertiary` | 표면을 더 강하게 구분하는 세 번째 배경(기존) |

#### 유틸리티 배경 {#utility-backgrounds}

| 토큰 | 용도 |
|-------|---------|
| `--color-bg-inverted` | 기본 배경에 대해 반전된 맥락의 배경 |
| `--color-bg-overlay-base` | 대화 상자와 뒷배경에 사용하는 어두운 오버레이 |
| `--color-bg-overlay-highlight` | 은은한 마우스 오버 상태에 사용하는 밝은 오버레이 |
| `--color-bg-overlay` | 모달 대화 상자 뒷배경의 단색 오버레이(기존) |
| `--color-bg-media` | 미디어 위에 겹쳐 배치하는 요소의 약간 투명한 배경(기존) |
| `--color-bg-media-base` | 위 토큰의 불투명한 기본 색상(기존) |
| `--color-bg-disabled` | 비활성화된 기본 버튼 등 비활성 컨트롤의 단색 배경(기존) |

#### 브랜드 배경 {#brand-backgrounds}

| 토큰 | 용도 |
|-------|---------|
| `--color-bg-brand-base` | 기본 버튼과 유사한 컨트롤의 불투명 브랜드 색상 |
| `--color-bg-brand-base-hover` | 마우스 오버 효과를 위한 위 색상의 약간 다른 변형(기존) |
| `--color-bg-brand-soft` | 강조된 콘텐츠에 은은한 색조를 더하는 배경 |
| `--color-bg-brand-softest` | 강조된 콘텐츠에 더 은은한 색조를 더하는 배경 |

#### 오류 배경 {#error-backgrounds}

| 토큰 | 용도 |
|-------|---------|
| `--color-bg-error-base` | 파괴적인 버튼의 불투명 오류 색상 |
| `--color-bg-error-base-hover` | 마우스 오버 효과를 위한 위 색상의 약간 다른 변형(기존) |
| `--color-bg-error-soft` | 오류 콘텐츠에 은은한 색조를 더하는 배경 |
| `--color-bg-error-softest` | 오류 콘텐츠에 더 은은한 색조를 더하는 배경 |

#### 경고 배경 {#warning-backgrounds}

| 토큰 | 용도 |
|-------|---------|
| `--color-bg-warning-base` | 버튼의 불투명 경고 색상(기존) |
| `--color-bg-warning-soft` | 경고 콘텐츠에 은은한 색조를 더하는 배경 |
| `--color-bg-warning-softest` | 경고 콘텐츠에 더 은은한 색조를 더하는 배경 |

#### 성공 배경 {#success-backgrounds}

| 토큰 | 용도 |
|-------|---------|
| `--color-bg-success-base` | 버튼의 불투명 성공 색상(기존) |
| `--color-bg-success-soft` | 성공 콘텐츠에 은은한 색조를 더하는 배경 |
| `--color-bg-success-softest` | 성공 콘텐츠에 더 은은한 색조를 더하는 배경 |

### 테두리 토큰 {#border-tokens}

| 토큰 | 용도 |
|-------|---------|
| `--color-border-primary` | 테두리와 구분선의 기본 색상 |
| `--color-border-brand` | 상호작용 가능한 콘텐츠의 테두리와 외곽선에 사용하는 브랜드 색상 |
| `--color-border-brand-soft` | 강조된 콘텐츠 주위 테두리의 부드러운 브랜드 색상 |
| `--color-border-error` | 오류가 있는 상호작용 가능한 콘텐츠의 테두리 색상 |
| `--color-border-success-soft` | 인증된 링크 카드의 테두리 색상 |
| `--color-border-warning-soft` | 경고 안내 상자의 테두리 색상(기존) |
| `--color-border-error-soft` | 오류 안내 상자의 테두리 색상(기존) |
| `--color-border-media` | 임베드된 게시물 미디어(이미지와 동영상)의 은은한 테두리(기존) |

### 기타 기존 토큰 {#other-legacy-tokens}

다음 토큰은 새 디자인에는 사용하지 않지만 이전 UI 요소를 지원하기 위해 남아 있습니다.

#### 그림자 토큰(기존) {#shadow-tokens-legacy}

| 토큰 | 용도 |
|-------|---------|
| `--dropdown-shadow` | 드롭다운 메뉴의 표준 `box-shadow` 값 |
| `--overlay-icon-shadow` | 미디어 위에 겹친 아이콘의 그림자 `filter` 값 |

#### 그래프와 차트용 토큰(기존) {#tokens-for-graphs-and-charts-legacy}

| 토큰 | 용도 |
|-------|---------|
| `--color-graph-primary-stroke` | 차트 도형 윤곽선의 표준 색상 |
| `--color-graph-primary-fill` | 차트 도형 채움의 표준 색상 |
| `--color-graph-warning-stroke` | 차트 도형 윤곽선의 경고 색상 |
| `--color-graph-warning-fill` | 차트 도형 채움의 경고 색상 |
| `--color-graph-disabled-stroke` | 비활성화된 차트의 도형 윤곽선 색상 |
| `--color-graph-disabled-fill` | 비활성화된 차트의 도형 채움 색상 |

#### 서식 있는 텍스트용 토큰(기존) {#tokens-for-rich-text-formatting-legacy}

| 토큰 | 용도 |
|-------|---------|
| `--rich-text-container-color` | 게시물에 삽입된 코드나 인라인 인용의 배경색 |
| `--rich-text-text-color` | 게시물에 삽입된 코드나 인라인 인용의 글자색 |
| `--rich-text-decorations-color` | 게시물에 삽입된 인라인 인용에 표시되는 아이콘 색상 |
