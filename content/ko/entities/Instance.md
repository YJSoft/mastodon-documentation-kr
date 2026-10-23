---
title: 서버 (Instance)
description: 이 도메인에서 실행 중인 마스토돈 소프트웨어 서버를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/instance",
  "/entities/Instance",
  "/api/entities/instance",
  "/api/entities/Instance",
]
---

## 예시 {#example}

```json
{
  "domain": "mastodon.social",
  "title": "Mastodon",
  "version": "4.5.0-nightly.2025-07-11",
  "source_url": "https://github.com/mastodon/mastodon",
  "description": "The original server operated by the Mastodon gGmbH non-profit",
  "usage": {
    "users": {
      "active_month": 279347
    }
  },
  "thumbnail": {
    "url": "https://files.mastodon.social/site_uploads/files/000/000/001/@1x/57c12f441d083cde.png",
    "description": "Colourful illustration of a Mastodon (a sort of elephant) carrying a bindle and joining a group of other Mastodons. The other Mastodons have many different colours and are holding up a Welcome sign.",
    "blurhash": "UeKUpFxuo~R%0nW;WCnhF6RjaJt757oJodS$",
    "versions": {
      "@1x": "https://files.mastodon.social/site_uploads/files/000/000/001/@1x/57c12f441d083cde.png",
      "@2x": "https://files.mastodon.social/site_uploads/files/000/000/001/@2x/57c12f441d083cde.png"
    }
  },
  "icon": [
    {
      "src": "https://mastodon.social/packs/assets/android-chrome-36x36-DLiBQg3N.png",
      "size": "36x36"
    },
    {
      "src": "https://mastodon.social/packs/assets/android-chrome-48x48-C7lKWFwX.png",
      "size": "48x48"
    },
    {
      "src": "https://mastodon.social/packs/assets/android-chrome-72x72-9LRpA3QN.png",
      "size": "72x72"
    },
    {
      "src": "https://mastodon.social/packs/assets/android-chrome-96x96-BKKwkkY-.png",
      "size": "96x96"
    },
    {
      "src": "https://mastodon.social/packs/assets/android-chrome-144x144-D-ewI-KZ.png",
      "size": "144x144"
    },
    {
      "src": "https://mastodon.social/packs/assets/android-chrome-192x192-jYKJbpas.png",
      "size": "192x192"
    },
    {
      "src": "https://mastodon.social/packs/assets/android-chrome-256x256-DXt2vsq7.png",
      "size": "256x256"
    },
    {
      "src": "https://mastodon.social/packs/assets/android-chrome-384x384-CbK7cG33.png",
      "size": "384x384"
    },
    {
      "src": "https://mastodon.social/packs/assets/android-chrome-512x512-Dz2ThkhV.png",
      "size": "512x512"
    }
  ],
  "languages": [
    "en"
  ],
  "configuration": {
    "urls": {
      "streaming": "wss://streaming.mastodon.social",
      "status": "https://status.mastodon.social",
      "about": "https://mastodon.social/about",
      "privacy_policy": "https://mastodon.social/privacy-policy",
      "terms_of_service": null
    },
    "vapid": {
      "public_key": "BCk-QqERU0q-CfYZjcuB6lnyyOYfJ2AifKqfeGIm7Z-HiTU5T9eTG5GxVA0_OH5mMlI4UkkDTpaZwozy0TzdZ2M="
    },
    "accounts": {
      "max_display_name_lenth": 30,
      "max_note_length": 500,
      "max_featured_tags": 10,
      "max_pinned_statuses": 5,
      "max_profile_fields": 4,
      "profile_field_name_limit": 255,
      "profile_field_value_limit": 255
    },
    "statuses": {
      "max_characters": 500,
      "max_media_attachments": 4,
      "characters_reserved_per_url": 23
    },
    "media_attachments": {
      "description_limit": 1500,
      "image_matrix_limit": 33177600,
      "image_size_limit": 16777216,
      "supported_mime_types": [
        "image/jpeg",
        "image/png",
        "image/gif",
        "image/heic",
        "image/heif",
        "image/webp",
        "image/avif",
        "video/webm",
        "video/mp4",
        "video/quicktime",
        "video/ogg",
        "audio/wave",
        "audio/wav",
        "audio/x-wav",
        "audio/x-pn-wave",
        "audio/vnd.wave",
        "audio/ogg",
        "audio/vorbis",
        "audio/mpeg",
        "audio/mp3",
        "audio/webm",
        "audio/flac",
        "audio/aac",
        "audio/m4a",
        "audio/x-m4a",
        "audio/mp4",
        "audio/3gpp",
        "video/x-ms-asf"
      ],
      "video_frame_rate_limit": 120,
      "video_matrix_limit": 8294400,
      "video_size_limit": 103809024
    },
    "polls": {
      "max_options": 4,
      "max_characters_per_option": 50,
      "min_expiration": 300,
      "max_expiration": 2629746
    },
    "translation": {
      "enabled": true
    },
    "timelines_access": {
      "live_feeds": {
        "local": "public",
        "remote": "public"
      },
      "hashtag_feeds": {
        "local": "public",
        "remote": "public"
      },
      "trending_link_feeds": {
        "local": "public",
        "remote": "public"
      }
    },
    "limited_federation": false
  },
  "registrations": {
    "enabled": true,
    "approval_required": false,
    "reason_required": false,
    "message": null,
    "min_age": 16,
    "url": null,
    "oauth": true
  },
  "api_versions": {
    "mastodon": 6
  },
  "contact": {
    "email": "staff@mastodon.social",
    "account": {
      "id": "13179",
      "username": "Mastodon",
      "acct": "Mastodon",
      "display_name": "Mastodon",
      "locked": false,
      "bot": false,
      "discoverable": true,
      "indexable": false,
      "group": false,
      "created_at": "2016-11-23T00:00:00.000Z",
      "note": "<p>Free, open-source decentralized social media platform.</p>",
      "url": "https://mastodon.social/@Mastodon",
      "uri": "https://mastodon.social/users/Mastodon",
      "avatar": "https://files.mastodon.social/accounts/avatars/000/013/179/original/b4ceb19c9c54ec7e.png",
      "avatar_static": "https://files.mastodon.social/accounts/avatars/000/013/179/original/b4ceb19c9c54ec7e.png",
      "header": "https://files.mastodon.social/accounts/headers/000/013/179/original/1375be116fbe0f1d.png",
      "header_static": "https://files.mastodon.social/accounts/headers/000/013/179/original/1375be116fbe0f1d.png",
      "followers_count": 843930,
      "following_count": 34,
      "statuses_count": 344,
      "last_status_at": "2025-07-10",
      "hide_collections": false,
      "noindex": false,
      "emojis": [],
      "roles": [],
      "fields": [
        {
          "name": "Homepage",
          "value": "<a href=\"https://joinmastodon.org\" target=\"_blank\" rel=\"nofollow noopener me\" translate=\"no\"><span class=\"invisible\">https://</span><span class=\"\">joinmastodon.org</span><span class=\"invisible\"></span></a>",
          "verified_at": "2018-10-31T04:11:00.076+00:00"
        },
        {
          "name": "Patreon",
          "value": "<a href=\"https://patreon.com/mastodon\" target=\"_blank\" rel=\"nofollow noopener me\" translate=\"no\"><span class=\"invisible\">https://</span><span class=\"\">patreon.com/mastodon</span><span class=\"invisible\"></span></a>",
          "verified_at": null
        },
        {
          "name": "GitHub",
          "value": "<a href=\"https://github.com/mastodon\" target=\"_blank\" rel=\"nofollow noopener me\" translate=\"no\"><span class=\"invisible\">https://</span><span class=\"\">github.com/mastodon</span><span class=\"invisible\"></span></a>",
          "verified_at": "2023-07-21T13:27:45.996+00:00"
        }
      ]
    }
  },
  "rules": [
    {
      "id": "1",
      "text": "Sexually explicit or violent media must be marked as sensitive or with a content warning",
      "hint": "This includes content that is particularly provocative even if it may not show specific body parts, as well as dead bodies, bloody injuries, and other gore. Particularly obscene content may be prohibited entirely. Profile pictures and header images may not contain sexually explicit or violent media.",
      "translations": {
        "de": {
          "text": "Sexuell explizite Darstellungen oder solche von Gewalt müssen mit einer Inhaltswarnung versehen werden.",
          "hint": "Das beinhaltet ausdrücklich provokative Inhalte, auch wenn keine bestimmten Körperteile zu sehen sind, sowie Leichname, blutige Verletzungen und vergleichbare extreme Darstellungen. Besonders obszöne Inhalte können vollständig verboten werden. Profil- und Titelbilder dürfen keine sexuell expliziten oder Gewaltdarstellungen abbilden."
        },
        "es": {
          "text": "El contenido sexual explícito o violento debe marcarse como sensible o con una advertencia de contenido.",
          "hint": "Esto incluye contenido especialmente provocativo, aunque no muestre partes específicas del cuerpo, así como cadáveres, heridas sangrientas y otras escenas sangrientas. Los contenidos especialmente obscenos pueden prohibirse por completo. Las fotos de perfil y las imágenes de cabecera no pueden contener contenido sexual explícito o violento."
        },
        "fr": {
          "text": "Le contenu érotique, pornographique ou violent doit être marqué comme sensible ou avoir un avertissement de contenu.",
          "hint": "Cela inclut le contenu particulièrement provocateur même s’il ne montre pas particulièrement de parties intimes, ainsi que les photos de cadavres, de blessures sanglantes et autres scènes dérangeantes. Le contenu particulièrement obscène peut être complètement interdit. Les images de profil et d’en-tête ne doivent pas contenir de contenu sexuellement explicite ou violent."
        },
        "nl": {
          "text": "Seksueel expliciet of gewelddadig beeldmateriaal moet als ‘gevoelig’ gemarkeerd worden, of met een inhoudswaarschuwing gemarkeerd.",
          "hint": "Dit omvat ook inhoud die gedeeltelijk aanstootgevend is zelfs als het geen lichaamsdelen toont, en ook dode lichamen, bloederige verwondingen en andere gruwelijkheden. Zeer obscene inhoud kan helemaal verboden worden. Profielfoto’s en headerafbeeldingen mogen geen seksueel expliciete of geweldadige inhoud hebben."
        },
        "ru": {
          "text": "Сексуально откровенные или жестокие изображения или видео должны быть помечены как чувствительные или скрыты под спойлер.",
          "hint": "Это включает в себя особенно провоцирующий контент, даже если он не показывает определённые части тела, а также мёртвые тела, окровавленные раны и прочую кровь. Особенно жестокий контент может быть запрещён полностью. Аватары и обложки профилей не должны содержать сексуально откровенные или жестокие изображения."
        },
        "zh-CN": {
          "text": "色情或暴力媒体必须标记为敏感或有内容警告",
          "hint": "这包括特别挑逗性的内容，即使它可能没有显示特定的身体部位，以及尸体、血腥伤害和其他血腥内容。特别淫秽的内容可能会被完全禁止。个人资料图片和头像不得包含色情或暴力内容。"
        },
        "zh-TW": {
          "text": "性暗示或暴力媒體必須標示為敏感或附帶內容警示",
          "hint": "這包括特別挑釁的內容，即使它可能沒有顯示特定的身體部位，以及屍體、血腥傷害和其他血腥內容。特別猥褻的內容可能會被完全禁止。個人檔案圖片和標題圖片不得包含色情或暴力媒體。"
        }
      }
    },
    {
      "id": "2",
      "text": "No racism, sexism, homophobia, transphobia, ableism, xenophobia, or casteism.",
      "hint": "Transphobic behavior such as intentional misgendering and deadnaming is strictly prohibited. Promotion of \"conversion therapy\" is strictly prohibited. Criticism of governments and religions is permissible unless being used as a proxy for discrimination.",
      "translations": {
        "de": {
          "text": "Kein(e) Rassismus, Sexismus, Homophobie, Transphobie, Behindertenfeindlichkeit, Fremdenfeindlichkeit oder Kasteismus.",
          "hint": "Transphobes Verhalten wie die absichtliche Verwendung von falschen Anreden und Pronomen sowie Deadnaming ist strengstens verboten. Die Werbung für Konversionstherapien ist strengstens verboten. Die Kritik an Regierungen und Religionen ist zulässig, sofern sie nicht stellvertretend für Diskriminierung verwendet wird."
        },
        "es": {
          "text": "Prohibido el racismo, sexismo, homofobia, transfobia, ableísmo, xenofobia o casticismo.",
          "hint": "Queda terminantemente prohibido el comportamiento transfóbico, como el uso intencionado de nombres falsos o el \"deadnaming\". La promoción de la \"terapia de conversión\" está estrictamente prohibida. Se permiten las críticas a gobiernos y religiones, a menos que se utilicen como excusa para la discriminación."
        },
        "fr": {
          "text": "Pas de racisme, sexisme, homophobie, transphobie, validisme, xénophobie ou discrimination de caste.",
          "hint": "Les comportements intentionnellement transphobes, comme le mégenrage ou le morinommage (“deadnaming”) est strictement interdit. La promotion des “thérapies de conversion” est strictement interdite. La critique des gouvernements et religions est autorisée, sauf dans les cas ou elle est utilisée comme paravent pour de la discrimination."
        },
        "nl": {
          "text": "Geen racisme, seksisme, homofobie, transfobie, validisme, xenofobie of kastendiscriminatie.",
          "hint": "Transfobisch gedrag zoals opzettelijk misgenderen en deadnaming is ten strengste verboden. Het promoten van “conversie therapie” is ten strengste verboden. Kritiek op overheden en religies is toegestaan tenzij het wordt gebruikt als proxy voor racisme."
        },
        "ru": {
          "text": "Запрещается расизм, сексизм, гомофобия, трансфобия, эйблизм, ксенофобия и кастовость.",
          "hint": "Трансфобное поведение, такое как осознанный мисгендеринг и деднейминг, строго запрещено. Продвижение \"конверсионной терапии\" строго запрещено. Критика правительств и религий разрешена, кроме случаев, когда она используется как оправдание для дискриминации."
        },
        "zh-CN": {
          "text": "禁止种族主义、性别歧视、仇视同性恋、仇视变性者、异能者、仇外心理或种姓歧视。",
          "hint": "严禁变性仇视行为，如故意误用性别和死名。严禁宣传 “转换疗法”。允许批评政府和宗教，除非被用作歧视的代名词。"
        },
        "zh-TW": {
          "text": "禁止種族主義、性別主義、恐同主義、恐變性主義、能力主義、仇外主義或種性主義。",
          "hint": "嚴禁變性仇視行為，例如故意誤用性別和暱稱。嚴禁宣傳「扭轉治療」。允許批評政府和宗教，除非被用來代表歧視。"
        }
      }
    },
    {
      "id": "3",
      "text": "No incitement of violence or promotion of violent ideologies",
      "hint": "Calling for people or groups to be assassinated, murdered, or attacked physically is strictly prohibited. Support for violent groups or events is prohibited.",
      "translations": {
        "de": {
          "text": "Keine Anstiftung zu Gewalt oder Förderung gewalttätiger Ideologien.",
          "hint": "Der Aufruf zum Mord oder körperlichen Attacken auf Personen oder Gruppen ist strengstens verboten. Die Unterstützung gewalttätiger Gruppen oder Veranstaltungen ist verboten."
        },
        "es": {
          "text": "Prohibida la incitación a la violencia o la promoción de ideologías violentas.",
          "hint": "Está estrictamente prohibido hacer llamamientos para que se asesine, mate o agreda físicamente a personas o grupos. Está prohibido apoyar a grupos o acontecimientos violentos."
        },
        "fr": {
          "text": "Pas d’incitation à la violence ou de promotion d’idéologies violentes.",
          "hint": "L’appel au meutre, à la violence ou à l’action physique envers des personnes ou des groupes de personnes est strictement interdit. Le soutien à des groupes ou évènements violents est interdit."
        },
        "nl": {
          "text": "Niet aanzetten tot geweld of verspreiden van gewelddadige ideologieën.",
          "hint": "Mensen of groepen aanzetten tot moord, aanslagen of fysieke aanvallen is ten strengste verboden. Steun voor gewelddadige groeperingen of evenementen is verboden."
        },
        "ru": {
          "text": "Запрещается подстрекательство к жестокости или продвижение жестоких идеологий.",
          "hint": "Призывы к покушениям, убийствам и физическим атакам на людей или группы людей строго запрещены. Поддержка жестоких сообществ или событий запрещена."
        },
        "zh-CN": {
          "text": "不得煽动暴力或宣扬暴力意识形态",
          "hint": "严禁呼吁暗杀、谋杀或人身攻击他人或团体。禁止支持暴力团体或事件。"
        },
        "zh-TW": {
          "text": "嚴禁煽動暴力或宣揚暴力意識形態",
          "hint": "嚴禁呼籲暗殺、謀殺或人身攻擊他人或團體。嚴禁支持暴力團體或事件。"
        }
      }
    },
    {
      "id": "4",
      "text": "No harassment, block evasion, dogpiling, or doxxing of others",
      "hint": "Repeat attempts to communicate with users who have blocked you or creation of accounts solely to harass or insult individuals is strictly prohibited. Coordinated activity to attack other users is prohibited. Posting of private personal information about others is prohibited.",
      "translations": {
        "de": {
          "text": "Keine Belästigungen, Umgehung von Blockierungen, Dogpiling oder Doxxing.",
          "hint": "Wiederholte Kommunikationsversuche mit Profilen, die dich blockiert haben, oder die Erstellung neuer Konten, die ausschließlich dazu dienen, andere zu belästigen oder zu beleidigen, sind strengstens verboten. Koordinierte Angriffe auf andere Profile sind verboten. Die Veröffentlichung von privaten und persönlichen Informationen anderer ist verboten."
        },
        "es": {
          "text": "No acosar, evadir bloqueos, \"dogpiling\" (abuso en línea por grupos de acosadores) o doxeo de otros.",
          "hint": "Está estrictamente prohibido intentar comunicarse repetidamente con usuarios que te hayan bloqueado o crear cuentas con el único fin de acosar o insultar a otras personas. Queda prohibida la actividad coordinada para atacar a otros usuarios. Está prohibido publicar información personal privada sobre otras personas."
        },
        "fr": {
          "text": "Pas de harcèlement, d’esquive de blocage, de “dogpiling”, ou de divulgation de données personnelles d’autrui.",
          "hint": "Les tentatives répétées de communiquer avec des utilisateur·ices qui vont ont bloqué ainsi que la création de comptes pour harceler ou insulter autrui sont strictement interdites. Les attaques coordonnées contre autrui sont interdites. La publication de données personnelles d’autrui est interdite."
        },
        "nl": {
          "text": "Geen intimidatie, omzeilen van blokkades, groepsaanvallen of het verspreiden van privégegevens van anderen.",
          "hint": "Herhaalde pogingen tot communiceren met gebruikers die je hebben geblokkeerd, of het maken van accounts enkel om personen te intimideren of beledigen is ten strengste verboden. Gecoördineerde activiteit om andere gebruikers aan te vallen is verboden. Het plaatsen van privé-gegevens van anderen is verboden."
        },
        "ru": {
          "text": "Запрещается травля, избегание блокировок, набеги и разглашение личной информации других лиц.",
          "hint": "Повторяющиеся попытки взаимодействовать с пользователями, которые вас заблокировали, и создание учётных записей исключительно ради травли или оскорблений, строго запрещены. Скоординированная активность с целью атаки на других пользователей запрещена. Публикация личной информации других лиц запрещена."
        },
        "zh-CN": {
          "text": "不得骚扰、回避封禁、诽谤或攻击他人",
          "hint": "严禁重复尝试与已封禁您的用户交流，或仅为骚扰或侮辱他人而创建账户。严禁协同攻击其他用户。禁止发布他人的私人个人信息。"
        },
        "zh-TW": {
          "text": "嚴禁騷擾、迴避封鎖、煽動或誣衊他人",
          "hint": "嚴禁重複嘗試與已封鎖您的使用者溝通，或純粹為了騷擾或侮辱他人而建立帳號。禁止攻擊其他使用者的協調活動。禁止張貼他人的私人個人資訊。"
        }
      }
    },
    {
      "id": "7",
      "text": "Do not share information widely-known to be false and misleading",
      "hint": "False and misleading information and links from low-quality sources may not be posted, especially if they are likely to mislead or confuse others or endanger their safety.",
      "translations": {
        "de": {
          "text": "Verbreitet keine Informationen, von denen allgemein bekannt ist, dass sie falsch oder irreführend.",
          "hint": "Falsche und irreführende Informationen sowie Links aus unseriösen Quellen dürfen nicht gepostet werden, insbesondere wenn sie geeignet sind, andere in die Irre zu führen oder deren Sicherheit zu gefährden."
        },
        "es": {
          "text": "No compartas información ampliamente conocida por ser falsa y engañosa.",
          "hint": "No está permitido publicar información falsa y engañosa ni enlaces de fuentes de baja calidad, especialmente si pueden inducir a error o confusión a otras personas o poner en peligro su seguridad."
        },
        "fr": {
          "text": "Ne partagez pas d’informations connues pour être fausses ou trompeuses.",
          "hint": "Les informations fausses ou trompeuses, ainsi que les liens vers des sources de mauvaise qualité ne doivent pas être publiées, particulièrement si elles risquent de tromper, d’induire en erreur, de semer la confusion ou de mettre des personnes en danger."
        },
        "nl": {
          "text": "Deel geen informatie die algemeen bekend staat als onjuist en misleidend.",
          "hint": "Onjuiste en misleidende informatie en links naar onbetrouwbare bronnen mogen niet geplaatst worden, zeker als deze waarschijnlijk anderen misleiden of verwarren, of hun veiligheid in  gevaar brengt."
        },
        "ru": {
          "text": "Не публикуйте заведомо ложную и вводящую в заблуждение информацию.",
          "hint": "Запрещена публикация ложной и вводящей в заблуждение информации и ссылок из низкокачественных источников, особенно если это может сбить других людей с толку, запутать их, или подвергнуть их опасности."
        },
        "zh-CN": {
          "text": "不得分享众所周知的虚假和误导性信息\r\n",
          "hint": "不得发布虚假和误导性信息以及来自低质量来源的链接，尤其是可能误导或混淆他人或危及他人安全的信息。"
        },
        "zh-TW": {
          "text": "請勿分享廣為人知的虛假和誤導資訊",
          "hint": "不得張貼虛假和誤導資訊以及來自低品質來源的連結，尤其是可能誤導或混淆他人或危害他人安全的資訊。"
        }
      }
    },
    {
      "id": "1008",
      "text": "Content created by others must be attributed, and use of generative AI must be disclosed",
      "hint": "Content created by others must clearly provide a reference to the author, creator, or source. For adult content, this should include performers. Accounts may not solely post AI-generated content.",
      "translations": {
        "de": {
          "text": "Von anderen erstellte Inhalte müssen gekennzeichnet und die Nutzung generativer KI offengelegt werden.",
          "hint": "Von anderen erstellte Inhalte müssen durch einen eindeutigen Verweis auf den/die Autor*in oder die Quelle gekennzeichnet werden. Bei nicht jugendfreien Inhalten sollte dies auch die Darsteller*innen einschließen. Konten dürfen nicht ausschließlich KI-generierte Inhalte posten."
        },
        "es": {
          "text": "Los contenidos creados por terceros deben ser atribuidos y el uso de IA debe ser revelado.",
          "hint": "Los contenidos creados por terceros deben proporcionar claramente una referencia al autor, creador o fuente. En el caso de los contenidos para adultos, debe incluirse a los artistas. Las cuentas no pueden publicar únicamente contenidos generados por IA."
        },
        "fr": {
          "text": "Le contenu crée par autrui doit être attribué, et l’utilisation d’IA générative doit être marqué comme tel.",
          "hint": "Le contenu créé par autrui doit fournir une référence explicite à son auteur·ice, créateur·ice ou sa source. Cela inclut les acteur·ice de contenu pour adulte. Les comptes publiant exclusivement du contenu généré par IA sont interdits."
        },
        "nl": {
          "text": "Inhoud gemaakt door anderen moet worden toegeschreven, en het gebruik van generatieve AI moet worden aangegeven.",
          "hint": "Inhoud gemaakt door anderen moet een duidelijke referentie naar de auteur, maker of bron bevatten. Voor Content created by others must clearly provide a reference to the author, creator, or source. Voor inhoud voor volwassenen, moet het model worden vermeld. Accounts mogen niet uitsluitend door AI gegenereerde inhoud plaatsen."
        },
        "ru": {
          "text": "Контент, созданный другими, должен публиковаться с указанием авторства, а использование генеративного ИИ должно быть раскрыто.",
          "hint": "Контент, созданный другими, должен явным образом сопровождаться отсылкой к автору, создателю или источнику. Для контента для взрослых это включает в себя актёров. Учётные записи не могут публиковать исключительно контент, сгенерированный с помощью ИИ."
        },
        "zh-CN": {
          "text": "他人创建的内容必须注明出处，使用人工智能产生的内容必须公开和披露说明",
          "hint": "他人创建的内容必须明确注明作者、创建者或来源。对于成人内容，应包括表演者。账户不得仅发布人工智能生成的内容。"
        },
        "zh-TW": {
          "text": "由他人創作的內容必須註明來源，使用人工智能產生的內容必須公開和披露說明",
          "hint": "他人創作的內容必須清楚提供作者、創作人或來源的參照。對於成人內容，這應該包括表演者。帳戶不得僅發佈人工智能產生的內容。"
        }
      }
    }
  ]
}
```

## 속성 {#attributes}

### `domain` {#domain}

**설명:** 서버의 WebFinger 도메인 이름입니다.\
**유형:** 문자열\
**버전 이력:**\
4.0.0 - 추가

### `title` {#title}

**설명:** 웹사이트 제목입니다.\
**유형:** 문자열\
**버전 이력:**\
4.0.0 - 추가

### `version` {#version}

**설명:** 서버에 설치한 마스토돈 버전입니다.\
**유형:** 문자열\
**버전 이력:**\
4.0.0 - 추가

### `source_url` {#source_url}

**설명:** AGPL 라이선스 요구 사항에 따른 이 서버 소프트웨어의 소스 코드 URL입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
4.0.0 - 추가

### `description` {#description}

**설명:** 관리자가 작성한 짧은 일반 텍스트 설명입니다.\
**유형:** 문자열\
**버전 이력:**\
4.0.0 - 추가

### `wrapstodon` {#wrapstodon}

**설명:** 현재 Wrapstodon([연간 보고서]({{< relref "methods/annual_reports" >}})) 캠페인 식별자(연도)입니다(있는 경우).\
**유형:** {{<nullable>}} 문자열\
**버전 이력:**\
4.6.0 - 추가

### `usage` {#usage}

**설명:** 이 서버의 사용 데이터입니다.\
**유형:** 해시\
**버전 이력:**\
4.0.0 - 추가

#### `usage[users]` {#users}

**설명:** 서버 사용자 관련 사용 데이터입니다.\
**유형:** 해시\
**버전 이력:**\
4.0.0 - 추가

##### `usage[users][active_month]` {#active_month}

**설명:** 지난 4주간의 활성 사용자 수입니다. `configuration[limited_federation]`이 설정된 서버에서는 0으로 지정됩니다.\
**유형:** 정수\
**버전 이력:**\
4.0.0 - 추가

### `thumbnail` {#thumbnail}

**설명:** 서버를 나타내는 이미지입니다.\
**유형:** 해시\
**버전 이력:**\
4.0.0 - 추가

#### `thumbnail[url]` {#thumbnail-url}

**설명:** 썸네일 이미지 URL입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
4.0.0 - 추가

#### `thumbnail[description]` {#thumbnail-description}

**설명:** 썸네일의 대체 텍스트입니다(시각 장애가 있는 사람이 이미지 내용을 이해하도록 돕는 설명).\
**유형:** 문자열\
**버전 이력:**\
4.6.0 - 추가

#### `thumbnail[blurhash]` {{<optional>}} {#blurhash}

**설명:** 미디어를 아직 다운로드하지 않았을 때 색상이 있는 미리보기 썸네일을 생성하기 위해 [BlurHash 알고리즘](https://github.com/woltapp/blurhash)으로 계산한 해시입니다.\
**유형:** 문자열 (Blurhash)\
**버전 이력:**\
4.0.0 - 추가

#### `thumbnail[versions]` {{<optional>}} {#thumbnail-versions}

**설명:** 고밀도 픽셀(DPI) 화면용 확대 해상도 이미지 링크입니다.\
**유형:** 해시\
**버전 이력:**\
4.0.0 - 추가

##### `thumbnail[versions][@1x]` {{<optional>}} {#1x}

**설명:** 1배 해상도 썸네일 이미지 URL입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
4.0.0 - 추가

##### `thumbnail[versions][@2x]` {{<optional>}} {#2x}

**설명:** 2배 해상도 썸네일 이미지 URL입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
4.0.0 - 추가

### `icon` {#icon}

**설명:** 이 서버에 설정된 아이콘의 사용 가능한 크기 목록입니다.\
**유형:** 배열: [InstanceIcon](#InstanceIcon)\
**버전 이력:**\
4.3.0 - 추가

### `languages` {#languages}

**설명:** 웹사이트와 운영진의 기본 언어입니다.\
**유형:** 배열: 문자열 (ISO 639-1 두 글자 코드)\
**버전 이력:**\
4.0.0 - 추가

### `configuration` {#configuration}

**설명:** 이 웹사이트에 설정된 값과 제한입니다.\
**유형:** 해시\
**버전 이력:**\
4.0.0 - 추가

#### `configuration[urls]` {#urls}

**설명:** 클라이언트 앱에 유용한 URL입니다.\
**유형:** 해시\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[urls][streaming]` {#streaming}

**설명:** 스트리밍 API에 연결할 WebSocket URL입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[urls][status]` {#status_url}

**설명:** 설정되어 있는 경우 서버 상태 페이지의 URL입니다.\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
4.1.0 - 추가

##### `configuration[urls][about]` {#about_url}

**설명:** 서버 소개 페이지 URL입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
4.4.0 - 추가

##### `configuration[urls][privacy_policy]` {#privacy_policy}

**설명:** 서버 개인정보 처리방침 URL입니다.\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
4.4.0 - 추가

##### `configuration[urls][terms_of_service]` {#terms_of_service}

**설명:** 있는 경우, 서버의 현재 이용약관 URL입니다.\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
4.4.0 - 추가

#### `configuration[vapid][public_key]` {#vapid_public_key}
**설명:** 푸시 알림에 사용하는 서버의 VAPID 공개 키이며 [WebPushSubscription#server_key]({{< relref "entities/WebPushSubscription#server_key" >}})와 같습니다.\
**유형:** 문자열\
**버전 이력:**\
4.3.0 - 추가

#### `configuration[accounts]` {#accounts}

**설명:** 계정 관련 제한입니다.\
**유형:** 해시\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[accounts][max_display_name_length]` {#max_display_name_length}

**설명:** 계정 표시 이름의 최대 허용 길이입니다.\
**유형:** 정수\
**버전 이력:**\
4.6.0 - 추가

##### `configuration[accounts][max_note_length]` {#max_note_length}

**설명:** 계정 소개의 최대 허용 길이입니다.\
**유형:** 정수\
**버전 이력:**\
4.6.0 - 추가

##### `configuration[accounts][max_avatar_description_length]` {#max_avatar_description_length}

**설명:** 계정 아바타 설명의 최대 허용 길이입니다.\
**유형:** 정수\
**버전 이력:**\
4.6.0 - 추가

##### `configuration[accounts][max_header_description_length]` {#max_header_description_length}

**설명:** 계정 프로필 헤더 설명의 최대 허용 길이입니다.\
**유형:** 정수\
**버전 이력:**\
4.6.0 - 추가

##### `configuration[accounts][max_featured_tags]` {#max_featured_tags}

**설명:** 계정별 허용되는 최대 추천 태그 수입니다.\
**유형:** 정수\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[accounts][max_pinned_statuses]` {#max_pinned_statuses}

**설명:** 계정별 최대 고정 게시물 수입니다.\
**유형:** 정수\
**버전 이력:**\
4.3.0 - 추가

##### `configuration[accounts][max_profile_fields]` {#max_profile_fields}

**설명:** 설정할 수 있는 사용자 지정 프로필 필드의 최대 개수입니다.\
**유형:** 정수\
**버전 이력:**\
4.6.0 - 추가

##### `configuration[accounts][profile_field_name_limit]` {#profile_field_name_limit}

**설명:** 프로필 필드 이름의 최대 문자 수입니다.\
**유형:** 정수\
**버전 이력:**\
4.6.0 - 추가

##### `configuration[accounts][profile_field_value_limit]` {#profile_field_value_limit}

**설명:** 프로필 필드 값의 최대 문자 수입니다.\
**유형:** 정수\
**버전 이력:**\
4.6.0 - 추가

#### `configuration[statuses]` {#statuses}

**설명:** 게시물 작성 관련 제한입니다.\
**유형:** 해시\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[statuses][max_characters]` {#max_characters}

**설명:** 게시물당 최대 허용 문자 수입니다.\
**유형:** 정수\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[statuses][max_media_attachments]` {#max_media_attachments}

**설명:** 게시물에 추가할 수 있는 최대 미디어 첨부 파일 수입니다.\
**유형:** 정수\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[statuses][characters_reserved_per_url]` {#characters_reserved_per_url}

**설명:** 게시물의 각 URL은 정확히 이 문자 수로 간주합니다.\
**유형:** 정수\
**버전 이력:**\
4.0.0 - 추가

#### `configuration[media_attachments]` {#media_attachments}

**설명:** 허용되는 첨부 파일에 관한 힌트입니다.\
**유형:** 해시\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[media_attachments][supported_mime_types]` {#supported_mime_types}

**설명:** 업로드할 수 있는 MIME 유형을 포함합니다.\
**유형:** 배열: 문자열\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[media_attachments][description_limit]` {#description_limit}

**설명:** 설명의 최대 문자 수입니다.\
**유형:** 정수\
**버전 이력:**\
4.4.0 - 추가

##### `configuration[media_attachments][image_size_limit]` {#image_size_limit}

**설명:** 업로드한 이미지의 최대 크기(바이트)입니다.\
**유형:** 정수\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[media_attachments][image_matrix_limit]` {#image_matrix_limit}

**설명:** 업로드 이미지의 최대 픽셀 수(너비 곱하기 높이)입니다.\
**유형:** 정수\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[media_attachments][video_size_limit]` {#video_size_limit}

**설명:** 업로드한 동영상의 최대 크기(바이트)입니다.\
**유형:** 정수\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[media_attachments][video_frame_rate_limit]` {#video_frame_rate_limit}

**설명:** 업로드한 동영상의 최대 프레임 속도입니다.\
**유형:** 정수\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[media_attachments][video_matrix_limit]` {#video_matrix_limit}

**설명:** 업로드 동영상의 최대 픽셀 수(너비 곱하기 높이)입니다.\
**유형:** 정수\
**버전 이력:**\
4.0.0 - 추가

#### `configuration[polls]` {#polls}

**설명:** 투표 관련 제한입니다.\
**유형:** 해시\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[polls][max_options]` {#max_options}

**설명:** 각 투표에서 허용하는 최대 선택지 수입니다.\
**유형:** 정수\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[polls][max_characters_per_option]` {#max_characters_per_option}

**설명:** 각 투표 선택지에서 허용하는 문자 수입니다.\
**유형:** 정수\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[polls][min_expiration]` {#min_expiration}

**설명:** 허용되는 최소 투표 기간(초)입니다.\
**유형:** 정수\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[polls][max_expiration]` {#max_expiration}

**설명:** 허용되는 최대 투표 기간(초)입니다.\
**유형:** 정수\
**버전 이력:**\
4.0.0 - 추가

#### `configuration[translation]` {#translation}

**설명:** 번역 관련 힌트입니다.\
**유형:** 해시\
**버전 이력:**\
4.0.0 - 추가

##### `configuration[translation][enabled]` {#translation-enabled}

**설명:** 서버에서 번역 API를 사용할 수 있는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.0.0 - 추가

#### `configuration[timelines_access]` {#timelines_access}

**설명:** 서로 다른 타임라인의 접근 제한입니다.\
**유형:** 해시\
**버전 이력:**\
4.5.0 - 추가

#### `configuration[timelines_access][live_feeds]` {#timelines_access-live_feeds}

**설명:** [공개 피드]({{< relref "methods/timelines#public" >}}) 접근 제한입니다.\
**유형:** 해시\
**버전 이력:**\
4.5.0 - 추가

#### `configuration[timelines_access][live_feeds][local]` {#timelines_access-live_feeds-local}

**설명:** 공개 피드의 로컬 게시물 접근 제한입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`public` = 방문자와 로그인한 사용자 모두 공개 피드의 로컬 게시물에 접근할 수 있습니다.\
`authenticated` = 공개 피드의 로컬 게시물에 접근하려면 인증이 필요합니다.\
`disabled` = “실시간 및 주제 피드 보기” [권한]({{< relref "entities/Role#permissions" >}})이 있는 사용자만 공개 피드의 로컬 게시물에 접근할 수 있습니다.\
**버전 이력:**\
4.5.0 - 추가

#### `configuration[timelines_access][live_feeds][remote]` {#timelines_access-live_feeds-remote}

**설명:** 공개 피드의 원격 게시물 접근 제한입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`public` = 방문자와 로그인한 사용자 모두 공개 피드의 원격 게시물에 접근할 수 있습니다.\
`authenticated` = 공개 피드의 원격 게시물에 접근하려면 인증이 필요합니다.\
`disabled` = “실시간 및 주제 피드 보기” [권한]({{< relref "entities/Role#permissions" >}})이 있는 사용자만 공개 피드의 원격 게시물에 접근할 수 있습니다.\
**버전 이력:**\
4.5.0 - 추가

#### `configuration[timelines_access][hashtag_feeds]` {#timelines_access-hashtag_feeds}

**설명:** [해시태그 피드]({{< relref "methods/timelines#tag" >}}) 접근 제한입니다.\
**유형:** 해시\
**버전 이력:**\
4.5.0 - 추가

#### `configuration[timelines_access][hashtag_feeds][local]` {#timelines_access-hashtag_feeds-local}

**설명:** 해시태그 피드의 로컬 게시물 접근 제한입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`public` = 방문자와 로그인한 사용자 모두 해시태그 피드의 로컬 게시물에 접근할 수 있습니다.\
`authenticated` = 해시태그 피드의 로컬 게시물에 접근하려면 인증이 필요합니다.\
**버전 이력:**\
4.5.0 - 추가

#### `configuration[timelines_access][hashtag_feeds][remote]` {#timelines_access-hashtag_feeds-remote}

**설명:** 해시태그 피드의 원격 게시물 접근 제한입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`public` = 방문자와 로그인한 사용자 모두 해시태그 피드의 원격 게시물에 접근할 수 있습니다.\
`authenticated` = 해시태그 피드의 원격 게시물에 접근하려면 인증이 필요합니다.\
`disabled` = “실시간 및 주제 피드 보기” [권한]({{< relref "entities/Role#permissions" >}})이 있는 사용자만 해시태그 피드의 원격 게시물에 접근할 수 있습니다.\
**버전 이력:**\
4.5.0 - 추가

#### `configuration[timelines_access][trending_link_feeds]` {#timelines_access-trending_link_feeds}

**설명:** [유행 링크 피드]({{< relref "methods/timelines#link" >}}) 접근 제한입니다.\
**유형:** 해시\
**버전 이력:**\
4.5.0 - 추가

#### `configuration[timelines_access][trending_link_feeds][local]` {#timelines_access-trending_link_feeds-local}

**설명:** 유행 링크 피드의 로컬 게시물 접근 제한입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`public` = 방문자와 로그인한 사용자 모두 유행 링크 피드의 로컬 게시물에 접근할 수 있습니다.\
`authenticated` = 유행 링크 피드의 로컬 게시물에 접근하려면 인증이 필요합니다.\
**버전 이력:**\
4.5.0 - 추가

#### `configuration[timelines_access][trending_link_feeds][remote]` {#timelines_access-trending_link_feeds-remote}

**설명:** 유행 링크 피드의 원격 게시물 접근 제한입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`public` = 방문자와 로그인한 사용자 모두 유행 링크 피드의 원격 게시물에 접근할 수 있습니다.\
`authenticated` = 유행 링크 피드의 원격 게시물에 접근하려면 인증이 필요합니다.\
`disabled` = “실시간 및 주제 피드 보기” [권한]({{< relref "entities/Role#permissions" >}})이 있는 사용자만 유행 링크 피드의 원격 게시물에 접근할 수 있습니다.\
**버전 이력:**\
4.5.0 - 추가

#### `configuration[limited_federation]` {#limited-federation}

**설명:** 명시적으로 허용된 도메인으로 연합을 제한하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.4.0 - 추가

### `registrations` {#registrations}

**설명:** 이 웹사이트 가입에 관한 정보입니다.\
**유형:** 해시\
**버전 이력:**\
4.0.0 - 추가

#### `registrations[enabled]` {#registrations-enabled}

**설명:** 가입이 활성화되어 있는지 나타냅니다. `registrations_mode`가 `none`이거나 서버가 `single_user_mode`이면 `false`입니다.\
**유형:** 불리언\
**버전 이력:**\
4.0.0 - 추가

#### `registrations[approval_required]` {#approval_required}

**설명:** 가입에 중재자 승인이 필요한지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.0.0 - 추가

#### `registrations[message]` {#registrations-message}

**설명:** 가입이 닫혀 있을 때 표시할 사용자 지정 메시지입니다. 가입이 열려 있으면 `null`입니다.\
**유형:** {{<nullable>}} 문자열 (HTML)\
**버전 이력:**\
4.0.0 - 추가

#### `registrations[min_age]` {#registrations-min_age}

**설명:** 설정되어 있는 경우, 가입에 필요한 최소 나이입니다.\
**유형:** {{<nullable>}} 정수\
**버전 이력:**\
4.4.0 - 추가

#### `registrations[reason_required]` {#registrations-reason_required}

**설명:** 가입 시 사용자가 가입 사유를 제공해야 하는지 나타냅니다. `registrations[approval_required]`가 true일 때만 적용됩니다.\
**유형:** {{<nullable>}} 불리언\
**버전 이력:**\
4.4.0 - 추가

#### `registrations[oauth]` {#registrations-oauth}

**설명:** OAuth 가입 흐름(`prompt=create`)을 지원하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
5.0.0 - 추가

#### `registrations[url]` {#registrations-url}

**설명:** 외부 인증을 사용할 때 계정 가입을 위한 사용자 지정 URL입니다.\
**유형:** {{<nullable>}} 문자열 (URL)\
**버전 이력:**\
4.2.0 - 추가

### `api_versions` {#api-versions}

**설명:** 클라이언트가 이 서버에서 사용할 수 있는 API 엔드포인트와 기능을 판단할 수 있도록 제공하는 기계 판독용 API 버전 정보입니다. 특히 포크와 개발 빌드에서 사람이 읽는 버전 문자열을 분석하는 것보다 신뢰할 수 있는 기능 감지 방법을 제공합니다. 최소한 `mastodon` 속성을 포함하며, 다른 구현은 자체 추가 속성을 가질 수 있습니다.\
**유형:** 해시\
**버전 이력:**\
4.3.0 - 추가

### `api_versions[mastodon]` {#api_versionsmastodon}

**설명:** 중요한 API 변경이 있을 때 증가하는 API 버전 번호입니다. 클라이언트는 포크나 야간 빌드의 "4.4+hometown-123" 같은 복잡한 버전 문자열을 분석하는 대신 이 값으로 API 호환성을 판단할 수 있습니다. 이 번호는 사람이 읽는 버전 번호와 독립적으로 증가합니다.\
**유형:** 정수\
**버전 이력:**\
4.3.0 - 추가

### `contact` {#contact}

**설명:** 웹사이트 담당자 연락에 관한 힌트입니다.\
**유형:** 해시\
**버전 이력:**\
4.0.0 - 추가

#### `contact[email]` {#contact-email}

**설명:** 문의나 문제에 관해 메시지를 보낼 수 있는 이메일 주소입니다.\
**유형:** 문자열 (이메일)\
**버전 이력:**\
4.0.0 - 추가

#### `contact[account]` {#contact-account}

**설명:** 문의나 문제에 관해 네트워크 내에서 직접 연락할 수 있는 계정입니다.\
**유형:** {{<nullable>}} [Account]({{< relref "entities/Account" >}})\
**버전 이력:**\
4.0.0 - 추가

### `rules` {#rules}

**설명:** 웹사이트 규칙의 항목별 목록입니다.\
**유형:** 배열: [Rule]({{< relref "entities/Rule" >}})\
**버전 이력:**\
4.0.0 - 추가

## InstanceIcon 속성 {#InstanceIcon}

### `src` {#src}

**설명:** 아이콘 URL입니다.\
**유형:** 문자열\
**버전 이력:**\
4.3.0 - 추가

### `size` {#size}

**설명:** 아이콘 크기입니다.\
**유형:** 문자열 (`12x34` 형식이며 `12`는 아이콘 너비, `34`는 아이콘 높이)\
**버전 이력:**\
4.3.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/instance#v2" caption="GET /api/v2/instance" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/instance_serializer.rb" caption="app/serializers/rest/instance_serializer.rb" >}}
