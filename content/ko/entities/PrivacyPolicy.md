---
title: 개인정보 처리방침 (PrivacyPolicy)
description: 서버 개인정보 처리방침을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/privacypolicy",
  "/entities/PrivacyPolicy",
  "/api/entities/privacypolicy",
  "/api/entities/PrivacyPolicy",
]
---

## 예시 {#example}

```json
{
  "updated_at": "2022-10-07T00:00:00+00:00",
  "content": "<p>This privacy policy describes how example.com (&quot;example.com&quot;, &quot;we&quot;, &quot;us&quot;) collects,\nprotects and uses the personally identifiable information you may provide\nthrough the example.com website or its API.</p>\n\n<h1>What information do we collect?</h1>\n\n<ul>\n<li><strong>Basic account information</strong>: If you register on this server, you may be\nasked to enter a username, an e-mail address and a password.</li>\n<li><strong>Posts, following and other public information</strong>: The list of people you\nfollow is listed publicly, the same is true for your followers.</li>\n<li><strong>Direct and followers-only posts</strong>: All posts are stored and processed on the\nserver. You may\ntoggle an option to approve and reject new followers manually in the settings.\n<strong>Please keep in mind that the operators of the server and any receiving\nserver may view such messages</strong>, and that recipients may screenshot, copy or\notherwise re-share them. <strong>Do not share any sensitive information over\nMastodon.</strong></li>\n<li><strong>IPs and other metadata</strong>: When you log in, we record the IP address you log\nin from, as well as the name of your browser application.</li>\n</ul>\n\n<hr>\n\n<p>This document is CC-BY-SA. Originally adapted from the <a href=\"https://github.com/discourse/discourse\">Discourse privacy\npolicy</a>.</p>\n"
}
```

## 속성 {#attributes}

### `updated_at` {#updated_at}

**설명:** 개인정보 처리방침의 마지막 갱신 시각을 나타내는 타임스탬프입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
4.0.0 - 추가

### `content` {#content}

**설명:** 렌더링된 HTML 형식의 개인정보 처리방침 내용입니다.\
**유형:** 문자열 (HTML)\
**버전 이력:**\
4.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/instance#privacy_policy" caption="GET /api/v1/instance/privacy_policy" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/privacy_policy_serializer.rb" caption="app/serializers/rest/privacy_policy_serializer.rb" >}}