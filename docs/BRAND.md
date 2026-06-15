# GSFGrace — Brand & Design System
> Version: v2.0 (최종 확정)
> Created: 2026-06-14
> Updated: 2026-06-14 (오늘 하루 전체 결정 반영)
> Status: 디자인 안정화 완료 — 런칭 가능
> 검증 기준: `GSF-Calling/docs/00-Calling-and-Manifesto-ko.md` (헌장)
> 참조: `GSF-OS/Wiki/GSFGrace_Platform_Architecture.md` (v3.0)
> 라이브: https://gsfgrace.com

---

## 0. 한 줄 정의

> **GSFGrace는 "도쿄 라이프스타일 매거진"이 아니라, 거대한 도시에서 한 사람에게 멈춰 서는 사마리아인의 길(Hodos)이다.**

디자인의 목표는 "예쁨"이 아니라 **"이 사이트가 왜 존재하는가"를 한눈에 느끼게 하는 것**.

---

## 1. Brand Architecture (이중 구조)

| 레이어 | 내용 | 노출 |
|--------|------|------|
| **표층 키워드** | GOOD SAMARITAN FLOURISHING | Hero 태그, 양 언어 공통 |
| **심층 철학** | Hodos(길) ・ Bridge(다리) ・ Oikos(가족) | 콘텐츠·카피에 내장 |
| **태그라인** | いのちを受けて、ともに歩む。/ 생명을 받고, 함께 걷다. | Hero |

> ※ "Quiet · Merciful · Tokyo"는 폐기 아님 — meta description·SEO 키워드·내부 브랜드 키워드로 보존.

---

## 2. 색상 토큰 (확정)

```css
:root {
  /* Base */
  --color-bg:          #FAF8F3;
  --color-surface:     #FFFFFF;
  --color-text:        #1C1A17;   /* 강화 버전 (#292524보다 진하게) */
  --color-muted:       #57534E;   /* 강화 버전 (#78716C보다 진하게) */

  /* Accent */
  --color-accent:      #5C6B57;
  --color-accent-deep: #48543F;
  --color-accent-soft: #EBEDE7;

  /* Warm — 뉴스레터 CTA 단 1곳에만 */
  --color-warm:        #B0875A;

  --color-line:        #E3DFD5;

  /* Typography */
  --font-sans:  'Noto Sans JP', system-ui, sans-serif;
  --font-serif: 'Noto Serif JP', 'Yu Mincho', 'Hiragino Mincho ProN', Georgia, serif;

  /* Layout 폭 */
  --width-container: 1080px;
  --width-text:       720px;
}
```

### 사용 규칙
- olive(`#5C6B57`) = 메인. 버튼·링크·로고박스·악센트 전부.
- clay(`#B0875A`) = 뉴스레터 CTA 버튼 **단 1곳에만**. 남발 금지.
- violet 계열 전면 금지.

---

## 3. 타이포그래피 (확정)

| 용도 | 폰트 |
|------|------|
| Hero / 제목 / 성구 / Quote | Noto Serif JP (明朝) |
| 본문 / UI / 메뉴 | Noto Sans JP |
| 한국어 본문 | Pretendard |
| 한국어 제목 | Noto Serif KR |

- `font-display: swap` 필수
- 시스템 폴백: `'Yu Mincho', 'Hiragino Mincho ProN', Georgia, serif`

---

## 4. 레이아웃 구조 (확정)

| 영역 | 폭 | 비고 |
|---|---|---|
| Nav | 1080px | 정렬선 통일 기준 |
| Hero | 100vw 풀블리드 | 수채화 화면 끝까지 |
| Hero 텍스트 | 1080px 중앙 | |
| 본문 텍스트 (About 등) | 720px 중앙 | 가독성 최적 |

- `html, body { overflow-x: hidden; }` — 100vw 풀블리드 가로 스크롤 방지 필수.
- 참조 밸런스: gsfark.com (넓지만 안 휑한 1080px 폭).

---

## 5. 시각 시그니처 (확정)

1. **로고 박스** — olive(`#5C6B57`) 배경 + 흰 텍스트, `border-radius: 4px`, padding `0.45rem 0.85rem`. "GSFGrace / Hodos Tokyo" 2줄.
2. **1px 길 모티프** — 끝이 사라지는 가로 그라데이션 선. nav 아래·섹션 구분에 사용.
   ```css
   background: linear-gradient(to right, transparent, var(--color-line) 12%, var(--color-line) 88%, transparent);
   ```
3. **Hero 수채화 일러스트** — 니혼바시+올리브나무. 풀블리드 배경. 중앙 집중형 오버레이로 텍스트 가독성 확보.
4. **明朝 제목** — Noto Serif JP. Hero·카드 제목에 필수.

---

## 6. Nav 구조 (확정)

```
[GSFGrace 박스]  메뉴5개(1.5rem 간격)  日本語|한국어  ·····(여백)
```

- 로고·메뉴·스위처가 왼쪽에서 흘러가는 하나의 그룹
- 스위처는 메뉴 오른쪽 `margin-left: 1.5rem` (우측 끝 아님)
- 모바일: 로고(좌) — 스위처 — 햄버거(우), 스위처 `margin-left: auto`

### 메뉴 5개 (JA / KO)

| JA | KO | 경로 |
|---|---|---|
| はじめての方へ (olive 텍스트) | 처음 오셨나요? | /story / /ko/story |
| 疑問に答える | 궁금한 질문 | /qa / /ko/qa |
| 今日のみことば | 오늘의 묵상 | /devotion / /ko/devotion |
| 日本橋エッセイ | 니혼바시 에세이 | /walk / /ko/walk |
| ἀρχή | ἀρχή | /arche / /ko/arche |

---

## 7. i18n 구조 (확정)

- `defaultLocale: 'ja'`, `locales: ['ja', 'ko']`, `prefixDefaultLocale: false`
- JA = 무접두사 (`/story`) / KO = `/ko/` 접두사 (`/ko/story`)
- hreflang ja / ko / x-default 전 페이지 적용
- KO 페이지 7종 생성: index / story / qa / devotion / walk / faith-life / arche
- KO **고정 UI**(메뉴·Hero·About·Footer)는 완성. 개별 글 번역은 글 작성 시 JA/KO 쌍으로.

---

## 8. 카피 세트 (JA/KO 확정)

### Hero
```
태그:    GOOD SAMARITAN FLOURISHING   (JA/KO 공통)

대제목:  Receive Life. / Walk Together.

JA:  いのちを受けて、ともに歩む。
     From strangers to neighbors. / From neighbors to family.
     「いのちを得、豊かに得るために」— ヨハネ 10:10
     CTA: はじめての方へ → / 疑問に答える

KO:  생명을 받고, 함께 걷다.
     낯선 이에서 이웃으로. / 이웃에서 가족으로.
     "생명을 얻고, 더 풍성히 얻게 하려" — 요한복음 10:10
     CTA: 처음 오셨나요? → / 궁금한 질문
```

### About (JA/KO 통일 — 1단 텍스트)
```
JA:  ABOUT GSFGRACE
     東京・日本橋から、
     恵みのうちに、ともに歩むために。
     キリスト教への疑問。信仰と日常。東京で福音を生きる、一つひとつの歩み。
     わたしたちは「読者」を増やすためでなく、一人の隣人と出会うために、ここにいます。
     わたしたちについて →

KO:  ABOUT GSFGRACE
     도쿄 니혼바시에서,
     은혜 안에서 함께 걷기 위해.
     기독교를 향한 질문. 신앙과 일상. 도쿄에서 복음을 살아가는, 하나하나의 걸음.
     우리는 '독자'를 늘리기 위해서가 아니라, 한 사람의 이웃을 만나기 위해 여기 있습니다.
     우리에 대하여 →
```

### Story 헤더
```
JA:  はじめての方へ / なぜ、この場所が存在するのか。
     東京は、世界でもっとも孤独な都市のひとつです…
     日本橋 ——「日本の橋」。わたしたちは一つの「いのちの橋」を架けたいのです。
     「行って、あなたも同じようにしなさい」— ルカ 10:37

KO:  처음 오셨나요? / 왜, 이곳이 존재하는가.
     도쿄는 세계에서 가장 고독한 도시 중 하나입니다…
     니혼바시(日本橋) — '일본의 다리'. 우리는 하나의 '생명의 다리'를 놓고자 합니다.
     "가서 너도 이와 같이 하라" — 누가복음 10:37
```

### 뉴스레터 CTA
```
JA:  東京からの手紙 / 頻度の約束はありません。ただ、誠実に。/ [手紙を受け取る] clay색
KO:  도쿄에서 보내는 편지 / 횟수를 약속하지는 않습니다. 다만, 신실하게. / [편지 받기] clay색
```

### Prayer (Footer)
```
JA:  祈りで共に / 東京のために祈ってください。日本橋に、福音の家族が立てられますように。
KO:  기도로 함께 / 도쿄를 위해 기도해 주세요. 니혼바시에 복음의 가족이 세워지도록.
```

### Q&A 하단 CTA
```
JA: この記事を書いた人は? →    KO: 이 글을 쓴 사람은? →
```

---

## 9. 사진 가이드라인 (확정)

- **Hero 사진 ❌, 일러스트 ⭕** — 수채화 일러스트(니혼바시+올리브나무)로 확정.
- 사진은 중간 섹션에 작게, 저채도/흑백으로만.
- **직접 촬영 실사진 목표** (스마트폰, 흑백 후처리): 니혼바시·스미다강·멈춰선 발·빈 의자·손.
- 실사진 준비 시 Story/Walk 등 "우리가 선 자리" 섹션에 배치. Hero 수채화와 역할 분담.
- 현재 About: placeholder 제거, 텍스트 단독. 실사진 준비 시 2단 복원.

---

## 10. 금지 사항

- ❌ violet/보라 계열 색
- ❌ sans-serif 제목
- ❌ Hero 큰 사진 (일러스트는 OK)
- ❌ 스톡 사진 (임시 일러스트는 OK)
- ❌ "発信" 등 미디어·마케팅 용어
- ❌ clay 색 남발 (뉴스레터 1곳만)
- ❌ 버튼 radius 4px 초과
- ❌ `overflow-x` 미처리 (100vw 풀블리드 필수 세트)

---

## 11. Decision Log (의사결정 이력)

### D-001. Hero 슬로건 (2026-06-14)
- **후보 A**: `Receive Life. Become Mercy.` — 헌장 §11 공식 슬로건. 능동적 긍휼. 고유성 강함.
- **후보 B**: `Receive Life. Walk Together.` ★**채택**
  - 근거: 헌장 §4 "회복될 때까지 함께 걷는다". Become Mercy를 추상 선언이 아닌 삶의 현장(ともに歩む)에서 살아냄 — 더 성육신적.
- **결정**: B 채택. **A는 폐기 아님** — Story·About·묵상 등에서 심층 신학어로 계속 사용.

### D-002. Hero 태그 (2026-06-14)
- **후보 A**: `QUIET ・ MERCIFUL ・ TOKYO` — 내부 브랜드 키워드.
- **후보 B**: `GOOD SAMARITAN FLOURISHING` ★**채택**
  - 근거: ChatGPT 시안과 일치. GSF 브랜드 정체성 첫 화면 직접 노출.
- **결정**: B 채택. A는 SEO·메타태그·내부 키워드로 보존.

### D-003. 로고 처리 (2026-06-14)
- **1차 시도**: 텍스트형 (굵게 800, 1.25rem) — 명시성 부족 확인.
- **확정**: olive 박스 + 흰 텍스트, radius 4px ★**채택**
  - 근거: "GSFGrace / Hodos Tokyo" 2줄 구조에 박스가 정리감 제공. 굵게 단독으로는 1080px 넓은 폭에서 존재감 부족.

### D-004. About 카피 (2026-06-14)
- **초안**: `福音を — 届けるためではなく、ともに歩む` (부정 비교 구문)
- **확정**: `恵みのうちに、ともに歩むために。` / `은혜 안에서 함께 걷기 위해.` ★**채택**
  - 근거: 부정 구문 제거 → 긍정 선언만. 은혜(恵み = GSFGrace) 브랜드 정체성 강화.

### D-005. 성구 (2026-06-14)
- **초안**: 요한복음 14:6 ("나는 길이다") — Hodos 정체성.
- **확정**: 요한복음 10:10 축약 ★**채택**
  - JA: `「いのちを得、豊かに得るために」`
  - KO: `"생명을 얻고, 더 풍성히 얻게 하려"`
  - 근거: 헌장 제1 핵심 성구. "Receive Life" 슬로건과 직접 일치. 14:6은 로고 "Hodos Tokyo"가 이미 담당.

### D-006. Hero 이미지 (2026-06-14)
- **원칙 수정**: "Hero 사진 ❌" → "Hero 사진 ❌, 일러스트 ⭕"
- **확정**: 니혼바시+올리브나무 수채화 일러스트 풀블리드 ★**채택**
  - 올리브나무 = 생명·예수 그리스도 상징. 사람 실루엣 우하단.
  - 스톡 사진보다 신학적 상징이 명확하고 "매거진 느낌" 없음.
  - 실사진(직접 촬영) 준비 시 Story/Walk에 배치. Hero는 수채화 유지 권장.

### D-007. 레이아웃 폭 (2026-06-14)
- **초안**: Nav 1100px / Hero 720px 박스 / About 640px — 3개 혼재로 밸런스 결함.
- **확정**: 1080px 단일 기준 + Hero 100vw 풀블리드 ★**채택**
  - 근거: GSFArk.com 밸런스 참조. "넓지만 안 휑한" 폭. 정렬선 통일.

### D-008. 언어 스위처 위치 (2026-06-14 — 반복 수정 끝 확정)
- **반복 원인**: "우측 끝"(표준 위치)으로 설계했으나, 1080px 넓은 폭에서 메뉴와 스위처 간격이 너무 벌어져 "동떨어진" 느낌.
- **확정**: 메뉴 오른쪽 `margin-left: 1.5rem` ★**채택**
  - 로고·메뉴·스위처가 왼쪽에서 하나의 그룹으로 흘러감. 우측 여백 자연스럽게 남음.
  - 모바일은 `margin-left: auto` 유지 (햄버거 옆 우측 끝).

### D-009. About 이미지 (2026-06-14)
- **초안**: 니혼바시 placeholder SVG (좌) + 텍스트 (우) 2단.
- **확정**: 이미지 제거, 텍스트 단독 ★**채택**
  - 근거: Hero 수채화가 강렬해 바로 아래 빈 회색 박스가 완성도 저하. 실사진 준비 시 2단 복원.

---

## 변경 이력

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-06-14 | v1.0 | 초기 디자인 확정 (olive-earth 방향, Manifesto 카피, 흑백 임시 사진) |
| 2026-06-14 | v2.0 | 전체 결정 통합 박제 — Hero 풀블리드, 로고 박스, 1080px, i18n, JA/KO 카피, Decision Log D-001~D-009 |
