# 마스토돈 한국어 문서

[Mastodon 공식 문서](https://docs.joinmastodon.org/)의 한국어 번역 저장소입니다. 영문 원문은 `content/en`, 한국어 번역은 같은 상대 경로의 `content/ko`에 있습니다. 사용자 안내부터 서버 운영, 앱 개발, 개발 기여, 연합 프로토콜, REST API 메서드와 엔터티까지 번역합니다.

원문 저장소는 [mastodon/documentation](https://github.com/mastodon/documentation)이며, 이 번역의 기준 커밋은 `f9e4c011`입니다. 원문과 번역은 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)에 따라 이용할 수 있습니다. 원저작자 표기와 원문 출처를 유지해 주세요.

## 로컬에서 보기

저장소는 Markdown을 정적 사이트로 변환하는 [Hugo](https://github.com/gohugoio/hugo)를 사용합니다. `.tool-versions` 및 배포 워크플로와 같은 **Hugo Extended 0.152.2**를 설치한 뒤 실행하세요. SCSS 처리를 위해 Extended 빌드가 필요합니다.

```sh
hugo server --baseURL http://localhost:1313/
```

한국어가 기본 언어이며 루트 주소에서 열립니다. 영어는 `/en/`, 기존 다른 언어는 각 언어 경로에서 볼 수 있습니다.

## 검증 및 빌드

Python 3 표준 라이브러리만으로 번역 파일의 대응, 코드 블록, 명시적 앵커, 링크 목적지와 shortcode의 구조를 확인할 수 있습니다.

```sh
python3 scripts/check_translation.py
python3 scripts/check_translation.py --report-english
hugo --minify
python3 scripts/check_site.py public --base-url https://yjsoft.github.io/mastodon-documentation-kr/
```

영문 잔존 보고는 검수 보조 자료입니다. 기술명이나 원문 예시도 표시될 수 있으므로 결과를 직접 확인해야 합니다. 구조 검증은 번역 의미의 정확성을 보장하지 않습니다.

## GitHub Pages 배포

[배포 워크플로](.github/workflows/deploy.yml)는 `main` 브랜치에 push하거나 Actions에서 직접 실행하면 사이트를 빌드하고 GitHub Pages로 배포합니다. GitHub 저장소의 **Settings → Pages → Build and deployment → Source**를 **GitHub Actions**로 설정해야 합니다.

기본 주소는 `https://yjsoft.github.io/mastodon-documentation-kr/`로 설정했습니다. 실제 배포 주소는 워크플로에서 GitHub Pages의 `base_url`을 사용하므로 사용자 지정 도메인도 반영합니다. 로컬 빌드에서 다른 주소를 쓰려면 다음과 같이 지정하세요.

```sh
hugo --minify --baseURL https://docs.example.com/
```

빌드 결과는 `public/`에 생성됩니다. 빌드만 실행하면 외부에 배포되지 않습니다.

## 번역에 참여하기

[한국어 번역 지침과 용어집](TRANSLATION.md), [문서 작성 지침 한국어판](DOCSTYLE.ko.md), [영문 작성 지침](DOCSTYLE.md)을 먼저 읽어 주세요. 원문의 업데이트는 `content/en`과 비교하여 한국어판에 반영합니다. API 식별자, 코드 예제, 경로, 버전 조건을 임의로 바꾸거나 생략하지 않습니다.

Mastodon 프로젝트에 기여할 때는 [기여 안내](https://github.com/mastodon/.github/blob/main/CONTRIBUTING.md)를 따릅니다. 공식 문서의 [아직 문서화되지 않은 주제 목록](https://github.com/mastodon/documentation/issues/1211)도 참고할 수 있습니다. 번역 범위와 검수 내역, 확인된 원문 문제는 [검수 기록](REVIEW.md)에 정리했습니다. 원래 저장소의 소개는 [README.en.md](README.en.md)에 보존되어 있습니다.
