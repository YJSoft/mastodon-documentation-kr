---
title: 내 서버 운영하기
description:
menu:
  docs:
    weight: 9999
    parent: user
---

## 마스토돈 서버를 직접 운영하는 이유 {#why-would-you-want-to-run-your-own-mastodon-server}

- 웹에서 내 목소리를 온전히 통제할 수 있습니다. 다른 사람의 규칙이나 변덕에 좌우되지 않습니다. 내 서버는 내 소유이며 내 규칙에 따라 운영합니다. 내가 원하는 동안 계속 존재합니다.
- 내 서버에 있다고 해서 고립되는 것은 *아닙니다*. 다른 서버의 누구든 팔로우할 수 있고, 상대방도 나를 팔로우할 수 있습니다. 같은 서버에 있는 것처럼 메시지를 주고받을 수 있습니다.
- 가입을 제한하여 혼자 개인 마이크로블로그처럼 사용하거나, 가족·친구를 위한 초대 전용 커뮤니티를 운영하거나, 누구나 가입할 수 있는 서버를 운영할 수 있습니다. 선택은 자유입니다!

{{< hint style="warning" >}}
인터넷에 공개 서비스를 제공하려면 중재와 커뮤니티 관리가 필요합니다. 서버가 커질수록 이러한 업무도 복잡해진다는 점을 알아두세요.
{{< /hint >}}

## 마스토돈 서버 운영에 필요한 것 {#so-you-want-to-run-your-own-mastodon-server}

다음 항목이 필요합니다.

- **도메인 이름**. 나와 다른 사람이 서버에 접속하는 주소이자, 네트워크에서 나와 사용자를 식별하는 기준입니다.

  **구하는 방법**: Namecheap, Gandi 등 다양한 도메인 등록 업체를 이용할 수 있습니다. 선택한 도메인에 따라 연간 비용이 달라집니다.

  {{< hint style="info" >}}
  도메인에 Mastodon 문자 상표를 사용하려면 [마스토돈 상표 정책](https://joinmastodon.org/trademark)에 따라 Mastodon GmbH의 사전 서면 허가를 받아야 합니다.
  {{< /hint >}}
- **VPS**. 마스토돈 코드를 실행하고 항상 인터넷에 연결되어 있을 서버입니다.

  **구하는 방법**: DigitalOcean, Hetzner, Exoscale, Scaleway 등 다양한 호스팅 업체를 이용할 수 있습니다. 하드웨어 사양에 따라 월간 또는 연간 비용이 달라집니다.
- **이메일 서비스 제공자**. 마스토돈은 확인 링크와 여러 알림을 이메일로 보내야 합니다. SMTP 서버를 직접 운영할 수도 있지만, 안정적으로 운영하기는 외부 서비스를 사용하는 것보다 훨씬 어렵습니다.

  **구하는 방법**: Mailgun, SparkPost, Postmark, Sendgrid 등 SMTP API를 제공하는 이메일 호스팅 서비스를 이용할 수 있습니다. 발송량에 따른 월간 비용이 발생합니다.
- 선택 사항: **오브젝트 스토리지 제공자**. 마스토돈은 업로드한 파일을 VPS의 디스크에 저장할 수 있지만, 디스크 용량은 보통 한정되어 있고 나중에 늘리기 어려울 수 있습니다. 오브젝트 스토리지는 사용량에 따라 과금하는 사실상 무제한의 파일 저장 공간을 제공합니다.

  **구하는 방법**: Amazon S3, Exoscale, Wasabi, Google Cloud 등 S3 또는 OpenStack Swift 호환 API를 제공하는 서비스를 이용할 수 있습니다. 저장한 파일의 양과 접근 빈도에 따른 월간 비용이 발생합니다.

기술적인 작업을 다른 곳에 맡기고 싶다면 위의 요구 사항 대부분 또는 전부를 처리해 주는 **마스토돈 전문 호스팅 업체**를 선택할 수도 있습니다. 보통 도메인은 직접 구매해야 합니다. 다음과 같은 업체가 있습니다.

{{< caption-link url="https://masto.host" caption="Masto.host" >}}

{{< caption-link url="https://hostdon.jp" caption="Hostdon" >}}

{{< caption-link url="https://ossrox.org" caption="Ossrox" >}}

{{< caption-link url="https://weingaertner-it.de" caption="Weingärtner IT" >}}

{{< caption-link url="https://ungleich.ch/u/products/mastodon-hosting/" caption="ungleich.ch" >}}

{{< caption-link url="https://fedihost.co/" caption="FediHost" >}}

{{< caption-link url="https://qoddi.com/mastodon" caption="Qoddi App Platform" >}}

{{< caption-link url="https://www.saasweb.net/de/managed-hosting/managed-mastodon-server" caption="SaaS Web" >}}

{{< caption-link url="https://toot.io/mastodon_hosting.html" caption="Toot.io" >}}

{{< caption-link url="https://webape.site" caption="WebApe" >}}

관리형 호스팅은 소프트웨어를 설치하고 관리할 경험이 없거나 직접 하고 싶지 않은 사람에게 좋습니다. 반면 모든 구성 요소를 자신의 하드웨어에서 직접 운영하면 확장성, 성능과 맞춤 설정을 더 세밀하게 제어할 수 있습니다.

마스토돈은 수평 확장에 잘 대응합니다. 한 대의 서버로 감당할 수 없게 되면 여러 앱 서버, 백그라운드 작업자, 여러 Redis 백엔드와 PostgreSQL 복제본으로 나눌 수 있습니다. 다만 이런 구성은 원클릭 설치만으로 해결할 수 없습니다.

모든 구성 요소를 직접 설치하고 싶다면 다음 문서로 이동하세요.

{{< page-ref page="admin/prerequisites" >}}
