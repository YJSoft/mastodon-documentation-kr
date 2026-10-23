---
title: CAPTCHA
description: 자동 가입 봇 완화하기
menu:
  docs:
    weight: 30
    parent: admin-optional
---

마스토돈 4.2부터는 봇의 새 계정 가입을 완화하기 위해 CAPTCHA 기술을 지원합니다.
CAPTCHA를 활성화하면 새 가입자는 이메일 확인 과정에서 챌린지 응답을 완료해야 합니다.

![가입자에게 표시되는 CAPTCHA](/assets/captcha/user-view.png)

{{< hint style="danger" >}}
일부 사용자에게는 중앙화된 CAPTCHA 서비스 사용이 보안과 개인정보 보호 측면에서 우려가 될 수 있습니다.
또한 CAPTCHA는 가입 과정의 접근성을 크게 낮출 수 있으며, 특히 시각장애가 있거나 저시력인 사람에게 영향을 줍니다.
{{</ hint >}}

현재 마스토돈에서 지원하는 유일한 제공자는 hCaptcha입니다.
향후 다른 제공자가 추가될 수 있습니다.

## hCaptcha {#hcaptcha}

- [hcaptcha.com](https://www.hcaptcha.com)에서 무료 hCaptcha 계정을 만듭니다.
- 가입 후 hCaptcha 대시보드에서 마스토돈 서버 도메인을 새 사이트로 추가하고 사이트 키를 얻습니다.
- hCaptcha의 계정 설정 메뉴에서 비밀 키를 얻습니다.
- 마스토돈 환경 설정에 `HCAPTCHA_SITE_KEY`와 `HCAPTCHA_SECRET_KEY`로 값을 추가합니다.
- 서버에서 실행 중인 마스토돈 서비스를 재시작합니다.
- 마스토돈 웹 인터페이스에서 **관리** > **서버 설정** > **가입**으로 이동하고 “새 사용자가 계정을 확인하려면 CAPTCHA를 풀도록 요구” 체크박스를 선택합니다.

![관리자 CAPTCHA 설정 화면](/assets/captcha/admin-view.png)
