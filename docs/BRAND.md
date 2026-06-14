# GSFGrace — Brand & Design System
> Version: v1.0 (확정)
> Created: 2026-06-14
> Status: 디자인 방향 확정 — 구현 대기
> 검증 기준: `GSF-Calling/docs/00-Calling-and-Manifesto-ko.md` (헌장)
> 참조: `GSF-OS/Wiki/GSFGrace_Platform_Architecture.md` (v3.0)

---

## 0. 한 줄 정의

> **GSFGrace는 "도쿄 라이프스타일 매거진"이 아니라, 거대한 도시에서 한 사람에게 멈춰 서는 사마리아인의 길(Hodos)이다.**

디자인의 목표는 "예쁨"이 아니라 **"이 사이트가 왜 존재하는가"를 한눈에 느끼게 하는 것**이다.

---

## 1. Brand Architecture (이중 구조)

| 레이어 | 내용 | 노출 |
|--------|------|------|
| **표층 키워드** | Quiet ・ Merciful ・ Tokyo | Hero 태그, 메타 |
| **심층 철학** | Hodos(길) ・ Bridge(다리) ・ Oikos(가족) | 콘텐츠·카피에 내장 |
| **태그라인** | 東京・日本橋から。一人に立ち止まる、その道を。 | Hero |

- **Tokyo**는 장소이자 가장 강력한 차별 자산 (헌장: "니혼바시 = 일본의 다리")
- **Hodos/Bridge/Oikos**는 키워드로 꺼내지 않고 "보이지 않게 작동하는 의미"로 둔다
- 비유: Apple은 "California"를 쓰고 "Think Different"를 별도로 둔다

---

## 2. 색상 토큰 (확정)

```css
:root {
  /* Base */
  --color-bg:          #FAF8F3;  /* 화선지/온백색 */
  --color-surface:     #FFFFFF;
  --color-text:        #292524;  /* soft black (순흑 아님) */
  --color-muted:       #78716C;

  /* Accent — 길/올리브/긍휼 */
  --color-accent:      #5C6B57;  /* olive-sage: 생명·길·평안 (메인) */
  --color-accent-deep: #48543F;  /* hover */
  --color-accent-soft: #EBEDE7;

  /* Warm — Mercy의 따뜻함 (단 1곳: 뉴스레터 CTA에만) */
  --color-warm:        #B0875A;  /* clay/gold */

  --color-line:        #E3DFD5;  /* 1px 길 모티프, 구분선 */
}
```

### 사용 규칙
- **olive(`#5C6B57`)** = 메인. 버튼·링크·악센트 전부.
- **clay(`#B0875A`)** = 뉴스레터 CTA 버튼 **단 1곳에만**. 남발 금지.
- **순흑(#000)·violet 계열 전면 금지.** 기존 `#7c3aed` 계열은 전부 제거.

---

## 3. 타이포그래피 (확정)

| 용도 | 폰트 | 비고 |
|------|------|------|
| Hero / 제목 / 성구 / Quote | **Noto Serif JP** (明朝) | 묵상·말씀의 깊이 |
| 본문 / UI | Noto Sans JP | 가독성 |
| 한국어 본문 | Pretendard | KO 페이지 |
| 한국어 제목 | Noto Serif KR | 명조 통일 |
| ὁδός / 道 / 로고 | serif | 고전적 무게 |

- **明朝(Serif)를 제목에 쓰는 것이 핵심.** sans 제목은 매거진처럼 보인다.
- `font-display: swap` 필수 (일본어 웹폰트 무거움)
- 시스템 명조 폴백: `'Noto Serif JP', 'Yu Mincho', 'Hiragino Mincho ProN', serif`

---

## 4. 시각 시그니처 (정체성 핵심)

정체성은 "예쁜 카피"가 아니라 **반복되는 시각 요소**로 박힌다.

1. **道 (michi)** — 로고·파비콘·섹션 구분에 작게 반복. "이 사이트 = 道" 각인.
2. **1px 길 모티프** — 끝이 사라지는 가로 그라데이션 선. nav 아래·섹션 구분·footer에 일관 사용.
   ```css
   background: linear-gradient(to right, transparent, var(--color-line) 12%, var(--color-line) 88%, transparent);
   ```
3. **흑백 사진** — 직접 촬영한 니혼바시·스미다강 (준비되는 대로 교체).

---

## 5. 사진 가이드라인

### 원칙
- **Hero에 큰 사진 ❌** — olive 단색 + 명조 타이포 + 1px 길선만으로 충분.
- 사진은 **중간 섹션에 작게, 저채도/흑백**으로만.
- **스톡 사진 지양.** 직접 촬영이 정체성을 만든다 (헌장: "우리가 선 니혼바시").

### 직접 촬영 (목표)
- 스마트폰으로 충분. 진정성 > 화질.
- 전부 **흑백/저채도** 후처리로 톤 통일.
- 피사체: 니혼바시 다리(필수) / 스미다강 / 골목 / 멈춰 선 발·신발 / 빈 의자 / 손.
- 사람 얼굴은 초상권 주의 → 뒷모습·실루엣·부분만.

### 임시 (촬영 전)
- **흑백 SVG placeholder** 사용 (AG 지시서 참조). "남의 사진"보다 "사진 자리(흑백 톤)"가 정체성에 유리.
- 촬영 완료 시 placeholder만 교체.

---

## 6. 카피 세트 (Manifesto 언어 — 확정)

### ① Hero
```
QUIET ・ MERCIFUL ・ TOKYO

Receive Life.
Become Mercy.

東京・日本橋から。
一人に立ち止まる、その道を。

— to stop for the one. a way called Hodos.

「わたしは道であり、真理であり、命である」— ヨハネ 14:6

[はじめての方へ →]  [疑問に答える]
```

### ② About (홈 중간)
```
ABOUT GSFGRACE

東京・日本橋から、
福音を — 届けるためではなく、
ともに歩むために。

キリスト教への疑問。信仰と日常。
東京で福音を生きる、一つひとつの歩み。

わたしたちは「読者」を増やすためでなく、
一人の隣人と出会うために、ここにいます。

わたしたちについて →
```

### ③ Story 헤더 (/story)
```
はじめての方へ

なぜ、この場所が存在するのか。

東京は、世界でもっとも孤独な都市のひとつです。
3,700万人が暮らし、それでも多くの人が
一人で生き、一人で去っていきます。

日本橋 ——「日本の橋」。
江戸の昔から、すべての道がここから始まりました。

わたしたちは、この場所から
一つの「いのちの橋」を架けたいのです。

「行って、あなたも同じようにしなさい」— ルカ 10:37
```

### ④ 뉴스레터 CTA
```
東京からの手紙

新しい記事と、東京での宣教の歩みを、
ときどきお届けします。
頻度の約束はありません。ただ、誠実に。

[手紙を受け取る]   ← clay #B0875A (유일한 warm)
```

### ⑤ Prayer (Footer)
```
祈りで共に

東京のために祈ってください。
日本橋に、福音の家族が立てられますように。
```

### ⑥ Q&A 하단 CTA
```
この記事を書いた人は? →   (→ /story)
```

---

## 7. 헌장 정합성 체크 (검증 완료)

| 카피 | 헌장 근거 |
|------|-----------|
| 一人に立ち止まる | §4 "He moved toward the wounded" |
| 届けるためではなく、ともに歩む | §7 "We do not seek followers" / §11 "not to gather subscribers" |
| いのちの橋を架けたい | §11 "lay a bridge of life" |
| 福音の家族 | §11 "where strangers become family" |
| 頻度の約束はありません | 스펙 "빈도 약속 없음" |

---

## 8. 금지 사항 (Do NOT)

- ❌ violet/보라 계열 색
- ❌ sans-serif 제목 (매거진처럼 보임)
- ❌ Hero 큰 사진
- ❌ 스톡 사진 (임시 placeholder는 OK)
- ❌ "発信(발신)" 등 미디어·마케팅 용어
- ❌ clay 색 남발 (뉴스레터 1곳만)
- ❌ 채도 높은 색·과한 그림자·둥근 버튼(radius는 4px)

---

## 변경 이력

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-06-14 | v1.0 | 디자인 확정 (Claude·ChatGPT 협업 → Claude 정리). olive-earth 방향, Manifesto 카피 세트, 흑백 임시 사진 전략 |
