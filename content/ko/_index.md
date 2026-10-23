---
title: 마스토돈이란 무엇인가요?
description: 마스토돈 문서에 오신 것을 환영합니다!
menu:
  docs:
    weight: -99
---

## 마이크로블로그란 무엇인가요? {#microblogging}

블로그가 웹사이트에 글을 올리는 활동이라면, **마이크로블로그**는 프로필에 짧은 글을 이어서 올리는 활동입니다. 텍스트 게시물을 작성하고 사진, 오디오, 동영상 등의 미디어나 투표를 첨부할 수 있습니다. 마스토돈에서는 친구를 팔로우하고 새로운 친구를 만날 수 있습니다.

## 연합이란 무엇인가요? {#federation}

**연합**은 탈중앙화의 한 형태입니다. 모두가 이용하는 하나의 중앙 서비스 대신, 여러 서비스가 존재하며 각 서비스를 원하는 만큼의 사람들이 이용할 수 있습니다.

| 중앙화 형태 | 예시 |
| :--- | :--- |
| 중앙집중형 | Twitter, Facebook, Instagram |
| 연합형 | 이메일, XMPP, 전화망, 우편 |
| 분산형 | BitTorrent, IPFS, Scuttlebutt |

마스토돈 서버는 독립적으로 운영할 수 있습니다. 일반적인 웹사이트처럼 가입하고, 글을 쓰고, 사진을 올리고, 다른 사람과 대화할 수 있습니다. 일반적인 웹사이트와 _달리_, 마스토돈 서버끼리는 서로 연동하여 다른 서버의 사용자와도 소통할 수 있습니다. 이메일 주소만 알면 Gmail 계정으로 Outlook, Fastmail, Protonmail 등 다른 이메일 서비스 사용자에게 메일을 보낼 수 있는 것처럼, **주소만 알면 어느 서버의 사용자든 멘션하거나 메시지를 보낼 수 있습니다**.

{{< figure src="assets/network-models.jpg" caption="왼쪽부터: 중앙집중형, 연합형, 분산형" >}}

## ActivityPub이란 무엇인가요? {#fediverse}

마스토돈은 표준화된 개방형 프로토콜인 **ActivityPub**으로 연합을 구현합니다. ActivityPub으로 연합을 구현한 다른 소프트웨어도 마스토돈 서버끼리 통신하는 것처럼 마스토돈과 원활하게 소통할 수 있습니다.

**연합우주**(fediverse, “federated universe”)는 ActivityPub과 월드 와이드 웹을 통해 서로 소통할 수 있는 모든 웹사이트를 가리킵니다. 모든 마스토돈 서버뿐 아니라 다음과 같은 다른 소프트웨어도 포함합니다.

- Pleroma: 모듈식 마이크로블로그 엔진
- Pixelfed: 미디어 게시물을 공유하고 감상할 수 있는 연합형 이미지 공유 플랫폼
- Misskey: 마이크로블로그와 사용자 지정 가능한 대시보드를 제공하는 소프트웨어
- PeerTube: 채널에 동영상을 올릴 수 있는 소프트웨어
- Plume: 긴 글을 게시할 수 있는 소프트웨어
- 그 밖에도 개인 웹사이트를 비롯한 다양한 서비스가 있습니다!

연합우주 자체에는 하나의 브랜드가 없습니다. 그래서 “연합우주에서 팔로우하세요”보다는 “마스토돈에서 팔로우하세요”라는 말을 더 자주 들을 수 있지만, 기술적으로는 앞의 표현이 더 정확합니다.

## 실제로 어떤 의미가 있나요? {#implications}

### 서비스 제공자와 정책 선택 {#choice}

마스토돈은 누구나 웹사이트를 운영하는 데 사용할 수 있는 소프트웨어입니다. 따라서 기존 마스토돈 서버 중에서 서비스 제공자를 선택하거나, 원한다면 직접 마스토돈 서버를 만들 수 있습니다. 마스토돈 프로젝트는 [joinmastodon.org](https://joinmastodon.org)에서 추천 서비스 제공자 목록을 관리하며, 주제와 언어에 따라 찾아볼 수 있습니다. 민감할 수 있는 콘텐츠에 특정 태그를 붙이도록 요구하는 등 더 엄격한 중재 정책을 적용하는 서버도 있고, 더 느슨한 정책을 적용하는 서버도 있습니다. 다만 서버 선택 목록에 있는 모든 서버는 [마스토돈 서버 서약](https://joinmastodon.org/covenant)에 동의합니다. 이는 혐오 표현을 적극적으로 중재하고, 매일 백업하며, 비상시 대응할 관리자를 최소 한 명 더 두고, 서비스를 종료할 경우 최소 3개월 전에 알리겠다는 약속입니다.

> 모든 구성원이 안전하다고 느끼는 커뮤니티를 유지하기는 쉽지 않습니다. 마스토돈은 이를 위한 기본적인 체계와 도구를 풍부하게 제공하며, 변화를 이끌 힘을 하나의 영리 기업에서 커뮤니티 자체로 옮깁니다.
>
> -- Eugen Rochko, 2018년 7월 6일, [“Cage the Mastodon”](https://blog.joinmastodon.org/2018/07/cage-the-mastodon/)

> 중앙집중형 소셜 미디어 플랫폼은 규칙과 그 집행, 플랫폼의 개발과 방향을 CEO가 결정하는 위계 구조를 가집니다. [...] 탈중앙화된 네트워크는 플랫폼 소유자를 사실상 없앰으로써 소유자의 통제권을 의도적으로 내려놓습니다.
>
> -- Eugen Rochko, 2018년 12월 30일, [“Why does decentralization matter?”](https://blog.joinmastodon.org/2018/12/why-does-decentralization-matter/)

### 운영 자금과 수익화 {#monetization}

마스토돈 서버는 서로 다른 개인이나 조직이 완전히 독립적으로 운영합니다. 마스토돈 소프트웨어 자체에는 수익화 수단이 구현되어 있지 않습니다.

유료 계정을 제공하는 운영자도 있고, 기존 인프라를 활용하는 기업도 있습니다. Patreon 등의 서비스를 통해 사용자에게 후원받는 운영자도 있으며, 자신과 친구 몇 명을 위한 개인 서버의 비용을 직접 부담하는 운영자도 있습니다. 계정이 있는 서버를 지원하고 싶다면 후원 방법이 있는지 확인해 보세요.

마스토돈 개발 역시 [Patreon](https://patreon.com/mastodon)과 [OpenCollective](https://opencollective.com/mastodon)를 통한 크라우드펀딩으로 이루어집니다. **벤처캐피털의 투자는 받지 않습니다.**

> 제 생각에 “즉각적이고 공개적이며 전 세계적인 메시지와 대화”는 실제로 _전 세계의 것_이어야 합니다. 스스로 운영할 수 있는 독립적인 조직과 주체들 사이에 분산되어야 합니다. 이익을 위해 대화를 이용할 유인이 없는 공공재여야 합니다.
>
> -- Eugen Rochko, 2018년 3월 3일, [“Twitter is not a public utility”](https://blog.joinmastodon.org/2018/03/twitter-is-not-a-public-utility/)

### 서로 다른 소프트웨어 간의 상호 운용성 {#interoperability}

예를 들어 Twitter 계정에서 Instagram 사용자를 팔로우하고, 계정을 옮기지 않고도 그 사람의 사진에 댓글을 달 수 있다고 생각해 보세요. Twitter와 Instagram이 같은 프로토콜을 사용하는 연합형 서비스라면 가능한 일입니다. 마스토돈 계정으로는 **호환되는 다른 모든 웹사이트와 소통할 수 있습니다.** _**그 웹사이트가 마스토돈을 사용하지 않아도 됩니다.**_ 게시물을 만들고 상호작용하는 데 필요한 ActivityPub 프로토콜의 일부를 소프트웨어가 지원하기만 하면 됩니다. 마스토돈과 상호 운용하는 데 필요한 기술 사양은 [ActivityPub](spec/activitypub), [WebFinger](spec/webfinger), [보안](spec/security)을 참고하세요. ActivityPub으로 가능한 일에 관한 자세한 설명은 [Why ActivityPub is the future](https://blog.joinmastodon.org/2018/06/why-activitypub-is-the-future/)를 참고하세요.

> 이 플랫폼들은 모두 다르고 서로 다른 필요에 초점을 맞춥니다. 하지만 기반은 같습니다. 다른 사람이 올린 글을 받아보기 위해 구독한다는 것입니다. 그렇기에 서로 호환됩니다.
>
> -- Eugen Rochko, 2018년 6월 27일, [“Why ActivityPub is the future”](https://blog.joinmastodon.org/2018/06/why-activitypub-is-the-future/)

### 자유 소프트웨어 {#libre}

독점 서비스와 달리, **파생 저작물에도 같은 자유를 보장한다면 누구나 마스토돈 소스 코드를 실행하고, 살펴보고, 검토하고, 복사하고, 수정하고, 배포하고, 재사용할 완전한 자유가 있습니다.** 마스토돈 사용자가 서비스 제공자를 선택할 수 있듯이, 누구나 마스토돈에 기능을 기여하거나 다른 기능을 담은 수정판을 공개할 수 있습니다. 소프트웨어 포크라고도 하는 이러한 수정판은 원래 마스토돈 프로젝트와 같은 자유를 보장해야 합니다. 예를 들어 [glitch-soc](https://glitch-soc.github.io/docs/)는 여러 실험적인 기능을 추가한 배포판입니다. 테마를 조금 바꾸거나 코드 일부를 수정한 개인 포크도 많이 있습니다. 마스토돈은 사용자의 자유를 존중하는 자유 소프트웨어이므로 이러한 맞춤 변경은 허용될 뿐 아니라 권장됩니다.

> 궁극적인 힘은 사람들이 자신의 공간과 커뮤니티를 만들고, 원하는 대로 소프트웨어를 수정할 수 있도록 하는 데 있습니다. 그러면서도 서로 다른 커뮤니티의 사람들이 교류할 수 있는 능력은 잃지 않아야 합니다.
>
> -- Eugen Rochko, 2017년 2월 20일, [“The power to build communities: A response to Mark Zuckerberg”](https://blog.joinmastodon.org/2017/02/the-power-to-build-communities/)

> 탈중앙화는 디지털 세계의 생물다양성이며 건강한 생태계의 특징입니다. 연합우주처럼 탈중앙화된 네트워크에서는 서로 다른 사용자 인터페이스, 소프트웨어, 운영 방식이 공존하며 협력할 수 있습니다.
>
> -- Eugen Rochko, 2018년 12월 30일, [“Why does decentralization matter?”](https://blog.joinmastodon.org/2018/12/why-does-decentralization-matter/)

## 다음 단계 선택하기 {#next-steps}

마스토돈 사용 방법을 알아보세요.

{{< page-ref page="user/signup" >}}

마스토돈 설치 방법을 알아보세요.

{{< page-ref page="admin/prerequisites" >}}

마스토돈 앱 개발 방법을 알아보세요.

{{< page-ref page="client/intro" >}}

마스토돈 백엔드와 기여 방법을 알아보세요.

{{< page-ref page="dev/overview" >}}
