---
title: 테마 만들기
description: 마스토돈 테마 제작을 소개하는 문서입니다. 주로 테마 제작자를 대상으로 하지만 마스토돈 스타일 작업에 관심 있는 누구에게나 유용한 정보도 담고 있습니다.
menu:
  docs:
    parent: frontend
    weight: 40
---

## 기초 작업 {#the-groundwork}

마스토돈 기본 테마의 진입점은 `app/javascript/styles/application.scss`입니다. 자신만의 테마를 만들려면 이 파일을 복제하고 `config/themes.yml` 파일에 새 항목을 추가합니다. 예:

```yml
default: styles/application.scss
my_theme: styles/my_theme.scss
```

그런 다음 에셋을 다시 빌드하고(`RAILS_ENV=production bundle exec rails assets:precompile`) 마스토돈 서비스나 Docker 컨테이너를 재시작합니다.

이 작업을 마치면 사용자 정의 테마를 다음 위치에서 선택할 수 있습니다.
- 사용자는 **환경설정 > 외형 > 테마**에서 선택합니다.
- 서버 기본 테마는 **관리 > 서버 설정 > 디자인**에서 선택합니다.

## 사용자 정의 스타일 {#custom-styles}

위 단계를 마치면 새 테마 진입점이 만들어지지만, 스타일은 마스토돈 기본 테마와 같습니다.

이제 `app/javascript/styles/mastodon` CSS 폴더 전체를 복제하여 수정할 수도 있지만, 마스토돈 UI의 색상만 변경하려면 `mastodon/theme` 폴더를 복사하는 것으로 충분합니다.

그런 다음 진입점 파일(`config/themes.yml`에서 참조하는 파일)을 수정하여 원본 대신 복사한 테마 폴더를 가져오도록 해야 합니다.

**예:** `mastodon/theme` 폴더를 `app/javascript/styles/my_theme`으로 복제했다면 `my_theme.scss`를 열고 `@use 'mastodon/theme'`을 `@use 'my_theme'`으로 바꿉니다.

이제 `my_theme/_base.scss`, `my_theme/_dark.scss`, `my_theme/_light.scss` 파일에 정의된 테마 토큰을 변경하여 새 색상 테마를 만들 수 있으며, 변경 사항이 UI에 반영됩니다.

## `color-scheme`과 `contrast` 환경설정 존중하기 {#respecting-color-scheme-and-contrast-preferences}

마스토돈 4.6 이전에는 밝은 모드, 어두운 모드, 고대비 등의 테마 변형을 별도 테마로 구현해야 했습니다. 4.6에서는 이러한 환경설정을 독립적인 설정으로 제공하도록 변경되었습니다.

새롭게 제공되는 사용자 옵션은 다음과 같습니다.
- **색 구성표:** 자동, 밝게, 어둡게
- **대비:** 자동, 높게

현재 값은 HTML 속성 `data-color-scheme`과 `data-contrast`에 반영되므로 스타일의 적용 범위를 지정하는 데 사용할 수 있습니다.


```scss
.component {
  color: black;
  background: black;

  [data-color-scheme='dark'] & {
    color: white;
    background: black;
  }
}
```

{{< hint style="info" >}}
“자동” 설정은 항상 실제 표시되는 옵션으로 변환됩니다. `color-scheme`은 `light` 또는 `dark`이며, `contrast`는 `default` 또는 `high`입니다.
{{< /hint >}}

`light-dark()` CSS 함수로도 같은 결과를 얻을 수 있습니다.

```scss
.component {
  color: light-dark(black, white);
  background: light-dark(white, black);
}
```

일반적으로 `color-scheme`과 `contrast`에 따라 달라지는 스타일은 테마 토큰 수준에서 처리하는 것을 권장합니다. 기본 제공 토큰 목록은 [디자인 토큰 참고 자료](/dev/frontend/design-tokens)를 확인합니다.
