# AG 작업 지시서 — GSFGrace 홈페이지 리디자인 v2
> 작성: 2026-06-15 | 승인자: 김승주 목사님 | 검토: Claude
> 참조 시안: `gsfgrace-mockup-v2.html` (승인 완료)

---

## 개요

홈페이지 디자인을 "텍스트 중심, 이미지는 맥락 전달 위치"로 전면 재설계한다.
수정 대상 파일은 **3개**다. 반드시 순서대로 작업한다.

---

## 수정 파일 1: `src/pages/index.astro`

### 전체 구조 (현행 → 변경)

```
현행:                          변경 후:
Hero (배경이미지+오버레이)      Hero (텍스트 단독, 배경 없음)
PathLine                       <hr class="divider" />
About (텍스트만)                About + 이미지 (2단 그리드)
PathLine                       <hr class="divider-wide" />
Link Cards (이모지 카드)        Contents (텍스트 리스트)
```

### Hero 섹션 변경

**제거할 요소:**
- `hero-tag` (`GOOD SAMARITAN FLOURISHING`)
- `hero-eng` (`From strangers to neighbors...`)
- `hero-verse` (`「いのちを得、豊かに得るために」...`)
- `btn-secondary` (疑問に答える 버튼)
- 배경 이미지 (`background-image`, `::before` 오버레이 전체)
- `<PathLine />` (두 곳 모두)

**유지할 요소:**
- `hero-title`: `Receive Life. / Walk Together.`
- `hero-tagline`: `いのちを受けて、ともに歩む。`
- `btn-primary` → 텍스트 링크로 교체 (아래 참조)

**추가할 요소:**
- `hero-location`: `Nihonbashi, Tokyo` (eyebrow 위치, 제목 위)

**새 Hero HTML:**
```html
<section class="hero">
  <p class="hero-location">Nihonbashi, Tokyo</p>
  <h1 class="hero-title">
    Receive <span class="accent">Life.</span><br />
    Walk Together.
  </h1>
  <p class="hero-ja">
    いのちを受けて、<br />ともに歩む。
  </p>
  <a href="/story" class="hero-cta" id="hero-story-cta">はじめての方へ →</a>
</section>
```

**새 Hero CSS (기존 `.hero` 관련 스타일 전체 교체):**
```css
.hero {
  padding: 8.5rem 2rem 7rem;
  max-width: 760px;
  margin: 0 auto;
}

.hero-location {
  font-size: 0.7rem;
  letter-spacing: 0.28em;
  color: var(--color-muted);
  font-weight: 500;
  text-transform: uppercase;
  font-family: var(--font-sans);
  margin-bottom: 2.25rem;
}

.hero-title {
  font-family: var(--font-serif);
  font-size: clamp(2.8rem, 6.5vw, 4.6rem);
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -0.035em;
  color: var(--color-text);
  margin-bottom: 1.5rem;
}

.hero-title .accent {
  color: var(--color-accent);
}

.hero-ja {
  font-family: var(--font-serif);
  font-size: clamp(1.1rem, 2.6vw, 1.45rem);
  color: var(--color-muted);
  line-height: 1.85;
  margin-bottom: 3.75rem;
  font-weight: 300;
  letter-spacing: 0.05em;
}

.hero-cta {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--color-accent);
  text-decoration: none;
  font-family: var(--font-sans);
  border-bottom: 1.5px solid var(--color-accent);
  padding-bottom: 2px;
  transition: color 0.15s, border-color 0.15s;
  letter-spacing: 0.02em;
}

.hero-cta:hover {
  color: var(--color-accent-deep);
  border-color: var(--color-accent-deep);
}

@media (max-width: 768px) {
  .hero {
    padding: 5.5rem 1.5rem 4.5rem;
  }
}
```

---

### divider (PathLine 교체)

PathLine import 및 사용 제거. 아래 `<hr>` 두 종류로 대체:

```html
<!-- Hero 아래 -->
<hr class="divider" />

<!-- Image 섹션 아래 -->
<hr class="divider-wide" />
```

```css
.divider {
  max-width: 760px;
  margin: 0 auto;
  border: none;
  border-top: 1px solid var(--color-line);
}

.divider-wide {
  max-width: 1080px;
  margin: 0 auto;
  border: none;
  border-top: 1px solid var(--color-line);
}
```

---

### About + 이미지 섹션 (신규)

기존 `section-about` 전체 교체:

```html
<section class="section-image" aria-labelledby="about-heading">
  <!-- 좌: 이미지 -->
  <figure class="image-visual" aria-hidden="true">
    <img
      src="/images/hero-nihonbashi.webp"
      alt="日本橋, 東京"
      class="image-photo"
      loading="lazy"
    />
    <figcaption class="image-caption">日本橋, 東京</figcaption>
  </figure>

  <!-- 우: About 텍스트 -->
  <div class="image-text">
    <p class="image-label">About GSFGrace</p>
    <h2 id="about-heading" class="image-heading">
      東京・日本橋から、<br />
      恵みのうちに、<br />
      ともに歩むために。
    </h2>
    <p class="image-body">
      キリスト教への疑問。信仰と日常。<br />
      東京で福音を生きる、一つひとつの歩み。
    </p>
    <p class="image-body">
      わたしたちは「読者」を増やすためでなく、<br />
      一人の隣人と出会うために、ここにいます。
    </p>
    <a href="/story" class="image-link" id="about-story-link">わたしたちについて →</a>
  </div>
</section>
```

```css
.section-image {
  max-width: 1080px;
  margin: 0 auto;
  padding: 5rem 2rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5rem;
  align-items: center;
}

.image-visual {
  position: relative;
  border-radius: 2px;
  overflow: hidden;
  aspect-ratio: 4 / 3;
  margin: 0;
  background: var(--color-line); /* 이미지 로드 전 fallback */
}

.image-photo {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* 올리브 + warm 오버레이 — 만남/생명 분위기 */
.image-visual::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    135deg,
    rgba(92, 107, 87, 0.22) 0%,
    rgba(72, 84, 63, 0.06) 55%,
    rgba(176, 135, 90, 0.14) 100%
  );
  pointer-events: none;
}

.image-caption {
  position: absolute;
  bottom: 0; left: 0;
  z-index: 2;
  padding: 1rem 1.25rem;
  font-size: 0.65rem;
  letter-spacing: 0.14em;
  color: rgba(255, 255, 255, 0.72);
  font-family: var(--font-sans);
  font-style: italic;
}

.image-label {
  font-size: 0.68rem;
  letter-spacing: 0.2em;
  color: var(--color-muted);
  font-weight: 600;
  text-transform: uppercase;
  font-family: var(--font-sans);
  margin-bottom: 1.5rem;
}

.image-heading {
  font-family: var(--font-serif);
  font-size: 1.6rem;
  font-weight: 600;
  line-height: 1.75;
  color: var(--color-text);
  margin-bottom: 1.5rem;
}

.image-body {
  font-size: 0.88rem;
  color: var(--color-muted);
  line-height: 2.05;
  font-family: var(--font-sans);
  margin-bottom: 1rem;
}

.image-link {
  display: inline-block;
  margin-top: 0.75rem;
  font-size: 0.85rem;
  color: var(--color-accent);
  font-weight: 600;
  text-decoration: none;
  font-family: var(--font-sans);
  border-bottom: 1px solid var(--color-accent);
  padding-bottom: 1px;
  transition: color 0.15s, border-color 0.15s;
}

.image-link:hover {
  color: var(--color-accent-deep);
  border-color: var(--color-accent-deep);
}

@media (max-width: 768px) {
  .section-image {
    grid-template-columns: 1fr;
    gap: 2.5rem;
    padding: 3.5rem 1.5rem;
  }
}
```

---

### Contents 섹션 (이모지 카드 → 텍스트 리스트)

기존 `section-links` 전체 교체:

```html
<section class="section-contents" aria-label="コンテンツへのリンク">
  <p class="contents-label">Contents</p>
  <ul class="contents-list">
    <li>
      <a href="/qa" class="contents-item" id="home-qa-link">
        <span class="ci-title">疑問に答える</span>
        <span class="ci-desc">なぜ神は苦しみを許すのか？ 科学と信仰は矛盾するか？</span>
        <span class="ci-arrow">→</span>
      </a>
    </li>
    <li>
      <a href="/devotion" class="contents-item" id="home-devotion-link">
        <span class="ci-title">今日のみことば</span>
        <span class="ci-desc">毎日の短い聖書の黙想</span>
        <span class="ci-arrow">→</span>
      </a>
    </li>
    <li>
      <a href="/walk" class="contents-item" id="home-walk-link">
        <span class="ci-title">日本橋エッセイ</span>
        <span class="ci-desc">東京での宣教の日々の記録</span>
        <span class="ci-arrow">→</span>
      </a>
    </li>
  </ul>
</section>
```

```css
.section-contents {
  max-width: 760px;
  margin: 0 auto;
  padding: 3.5rem 2rem 4.5rem;
}

.contents-label {
  font-size: 0.68rem;
  letter-spacing: 0.2em;
  color: var(--color-muted);
  font-weight: 600;
  text-transform: uppercase;
  font-family: var(--font-sans);
  margin-bottom: 1.75rem;
}

.contents-list {
  list-style: none;
}

.contents-list li {
  border-top: 1px solid var(--color-line);
}

.contents-list li:last-child {
  border-bottom: 1px solid var(--color-line);
}

.contents-item {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  padding: 1.25rem 0;
  text-decoration: none;
  gap: 1.5rem;
  transition: none;
}

.contents-item:hover .ci-title {
  color: var(--color-accent);
}

.contents-item:hover .ci-arrow {
  transform: translateX(4px);
}

.ci-title {
  font-family: var(--font-serif);
  font-size: 1.05rem;
  color: var(--color-text);
  font-weight: 600;
  flex-shrink: 0;
  transition: color 0.15s;
}

.ci-desc {
  font-size: 0.78rem;
  color: var(--color-muted);
  font-family: var(--font-sans);
  flex: 1;
  line-height: 1.6;
}

.ci-arrow {
  font-size: 0.9rem;
  color: var(--color-accent);
  flex-shrink: 0;
  transition: transform 0.15s;
}

@media (max-width: 600px) {
  .contents-item {
    flex-wrap: wrap;
    gap: 0.5rem;
  }
  .ci-desc {
    flex-basis: 100%;
    margin-left: 0;
  }
}
```

---

## 수정 파일 2: `src/components/Footer.astro`

### 변경 내용

1. **뉴스레터 섹션 전체 제거** (`footer-newsletter`, `newsletter-form`, `newsletter-input`, `newsletter-btn`)
2. **기도 섹션 전체 제거** (`footer-prayer`, `prayer-text`)
3. **`footer-story-cta` 제거**
4. **`PathLine` import 및 `<PathLine />` 제거**
5. **copyright 문자열 변경**:
   - 현행: `` © ${new Date().getFullYear()} GSFGrace — Hodos Tokyo ``
   - 변경: `GSFGrace — Good Samaritan Flourishing ✦ 日本橋, 東京`
   - (ko도 동일하게 통일, © 연도 제거)
6. **footer 배경** `#1c1917` → `var(--color-bg)` (밝은 배경으로)
7. **footer 텍스트** → `var(--color-muted)`

**새 Footer 구조:**
```astro
---
const { lang = 'ja' } = Astro.props as { lang?: 'ja' | 'ko' };
---

<footer class="site-footer">
  <div class="footer-inner">
    <p class="footer-copy">
      <span class="footer-brand">GSFGrace</span>
      {' '}— Good Samaritan Flourishing ✦ 日本橋, 東京
    </p>
  </div>
</footer>

<style>
  .site-footer {
    border-top: 1px solid var(--color-line);
    padding: 2.25rem 2rem;
    background: var(--color-bg);
  }

  .footer-inner {
    max-width: 1080px;
    margin: 0 auto;
    text-align: center;
  }

  .footer-copy {
    font-size: 0.75rem;
    color: var(--color-muted);
    font-family: var(--font-sans);
    letter-spacing: 0.05em;
  }

  .footer-brand {
    font-weight: 700;
    color: var(--color-text);
    font-family: var(--font-serif);
  }
</style>
```

---

## 수정 파일 3: `src/components/Nav.astro`

### 변경 내용

1. **로고에서 `brand-sub` (`Hodos Tokyo`) 제거**

현행:
```astro
<a href={...} class="nav-brand" aria-label="GSFGrace Home">
  <span class="brand-name">GSFGrace</span>
  <span class="brand-sub">Hodos Tokyo</span>
</a>
```

변경:
```astro
<a href={lang === 'ko' ? '/ko' : '/'} class="nav-brand" aria-label="GSFGrace Home">
  <span class="brand-name">GSFGrace</span>
</a>
```

2. **`.nav-brand` CSS 수정** — `flex-direction: column` 불필요, 단순화:
```css
.nav-brand {
  display: inline-block;
  background: var(--color-accent);
  padding: 0.42rem 0.88rem;
  border-radius: 4px;
  text-decoration: none;
  line-height: 1;
}

.brand-name {
  font-size: 1.05rem;
  font-weight: 800;
  color: #fff;
  letter-spacing: -0.01em;
  font-family: var(--font-serif);
}
```

3. **`.brand-sub` 스타일 완전 삭제**

---

## 이미지 처리 (중요)

`/public/images/hero-nihonbashi.webp` — 현재 Hero 배경으로 사용 중이던 파일.
About 섹션 이미지로 재활용한다. **파일 이동/변경 불필요.**

> ⚠️ 승주 목사님 확인 사항: ChatGPT가 생성한 수채화 느낌 이미지를
> `/public/images/hero-nihonbashi.webp`로 교체하거나,
> 새 파일명(`nihonbashi-watercolor.webp`)으로 추가 후 img src 경로 수정 필요.
> 이미지 파일 교체는 AG가 아닌 목사님이 직접 처리.

---

## 제거 대상 (사용하지 않게 되는 것들)

- `PathLine.astro` import — index.astro, Footer.astro 양쪽에서 제거
  (파일 자체는 삭제하지 말고 보존)
- `.hero::before` (radial gradient overlay) CSS
- `.btn-primary`, `.btn-secondary` CSS
- `.hero-tag`, `.hero-eng`, `.hero-verse` CSS
- `.section-about`, `.about-*` CSS 전체
- `.section-links`, `.link-card*` CSS 전체

---

## 검증 체크리스트

작업 완료 후 AG가 직접 확인:

- [ ] `localhost` 로컬 빌드 후 렌더링 확인
- [ ] Hero: 배경 이미지 없음, 텍스트만 표시
- [ ] Hero 타이틀 "Life." — accent 색(올리브) 적용
- [ ] `いのちを受けて、ともに歩む。` — hero 타이틀보다 작고, muted 색
- [ ] About 섹션: 이미지 좌 / 텍스트 우, 2단 그리드
- [ ] Contents: 이모지 없음, 텍스트 리스트 + 가로선
- [ ] Footer: 한 줄 카피만 (`GSFGrace — Good Samaritan Flourishing ✦ 日本橋, 東京`)
- [ ] 뉴스레터/기도 섹션 없음
- [ ] 로고: `GSFGrace` 단독, `Hodos Tokyo` 없음
- [ ] 모바일(375px) 레이아웃 이상 없음
- [ ] 한국어(`/ko`) 페이지도 정상 렌더링
- [ ] Vercel 배포 후 `gsfgrace.com` 최종 확인

---

## 작업 범위 외 (건드리지 말 것)

- `BaseLayout.astro` CSS 변수 — 변경 없음
- 각 하위 페이지 (`/story`, `/qa`, `/devotion`, `/walk`, `/arche`) — 변경 없음
- `PathLine.astro` 파일 자체 — 삭제 말고 보존
- `hero-nihonbashi.webp` 파일 — 이미지 교체는 목사님 담당
