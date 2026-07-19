# AG 지시서 — /thank-you 페이지 생성
> 작성: Claude / 2026-06-18  
> 우선순위: P1

## 배경
Kit 구독 확인 후 리다이렉트 페이지를 GSFGrace 자체 페이지로 교체.
현재: app.kit.com/confirm-subscription (영어 고정)
목표: gsfgrace.com/thank-you (JA/KO + 니혼바시 이미지)

---

## TASK 1. src/pages/thank-you.astro 생성

이미지: public/images/hero-nihonbashi.webp 사용 (없으면 nihonbashi.png fallback)

파일 전체 내용:

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout
  title="ご登録ありがとうございます — GSFGrace"
  description="GSFGrace ニュースレター登録完了ページ"
  lang="ja"
>
  <article class="thankyou-page">

    <div class="thankyou-image">
      <img
        src="/images/hero-nihonbashi.webp"
        alt="東京 日本橋"
        width="1080"
        height="320"
        onerror="this.src='/images/nihonbashi.png'"
      />
    </div>

    <div class="thankyou-body">

      <section class="thankyou-section">
        <p class="thankyou-tag">購読完了</p>
        <h1 class="thankyou-title">ご登録ありがとうございます。</h1>
        <p class="thankyou-text">
          東京・日本橋からの手紙を、まもなくお届けします。<br />
          新しい記事と宣教のあゆみを、静かにお届けできることを楽しみにしています。
        </p>
        <p class="thankyou-sign">— 金承柱 김승주 (GSFGrace / 日本橋)</p>
      </section>

      <hr class="thankyou-divider" />

      <section class="thankyou-section">
        <p class="thankyou-tag">구독 완료</p>
        <h2 class="thankyou-title">구독해 주셔서 감사합니다.</h2>
        <p class="thankyou-text">
          도쿄 니혼바시에서 보내는 편지를 곧 전해 드리겠습니다.<br />
          새로운 글과 선교 소식을 조용히, 그러나 진심을 담아 나누겠습니다.
        </p>
        <p class="thankyou-sign">— 金承柱 김승주 (GSFGrace / 니혼바시)</p>
      </section>

      <div class="thankyou-links">
        <a href="/" class="btn-home">← 日本語トップへ</a>
        <a href="/ko" class="btn-home">← 한국어 홈으로</a>
      </div>

    </div>
  </article>
</BaseLayout>

<style>
  .thankyou-page {
    padding: 2rem 0 4rem;
    max-width: var(--width-text);
    margin: 0 auto;
  }
  .thankyou-image {
    width: 100%;
    margin-bottom: 2.5rem;
    border-radius: 4px;
    overflow: hidden;
  }
  .thankyou-image img {
    width: 100%;
    max-height: 320px;
    object-fit: cover;
    display: block;
  }
  .thankyou-body {
    padding: 0 0.5rem;
  }
  .thankyou-section {
    margin-bottom: 2rem;
  }
  .thankyou-tag {
    font-size: 0.72rem;
    letter-spacing: 0.18em;
    color: var(--color-accent);
    font-weight: 600;
    text-transform: uppercase;
    margin-bottom: 0.75rem;
    font-family: var(--font-sans);
  }
  .thankyou-title {
    font-size: clamp(1.4rem, 3vw, 2rem);
    font-weight: 700;
    color: var(--color-text);
    font-family: var(--font-serif);
    margin-bottom: 1rem;
    line-height: 1.5;
  }
  .thankyou-text {
    font-size: 1rem;
    line-height: 2.0;
    color: var(--color-text);
    font-family: var(--font-sans);
    margin-bottom: 0.75rem;
  }
  .thankyou-sign {
    font-size: 0.9rem;
    color: var(--color-muted);
    font-family: var(--font-sans);
    font-style: italic;
  }
  .thankyou-divider {
    border: none;
    border-top: 1px solid var(--color-line);
    margin: 2rem 0;
  }
  .thankyou-links {
    display: flex;
    gap: 1rem;
    margin-top: 2.5rem;
    flex-wrap: wrap;
  }
  .btn-home {
    display: inline-block;
    padding: 0.55rem 1.25rem;
    border: 1px solid var(--color-accent);
    border-radius: 4px;
    color: var(--color-accent);
    font-size: 0.875rem;
    font-family: var(--font-sans);
    font-weight: 600;
    text-decoration: none;
    transition: background 0.15s, color 0.15s;
  }
  .btn-home:hover {
    background: var(--color-accent);
    color: #fff;
    text-decoration: none;
  }
</style>
```

---

## 검증
```bash
cd scratch/projects/GSF-Grace && npm run build
```
- 빌드 에러 없음
- 로컬 http://localhost:4321/thank-you 접속 확인
  - 니혼바시 이미지 표시
  - JA/KO 텍스트 표시
  - 홈 링크 작동

## 보고 항목
- thank-you.astro 생성 확인
- 빌드 성공 여부
- 커밋 해시
- 배포 URL: https://gsfgrace.com/thank-you

---

## TASK 2 (목사님 직접 — AG 불필요)
AG 배포 완료 후 아래 Kit 설정 변경:

app.kit.com → Grow → Landing Pages & Forms
→ Clare form → Settings → Incentive 탭
→ "After confirming redirect to:" URL 입력란
→ 기존값 삭제 후 입력: https://gsfgrace.com/thank-you
→ Save
