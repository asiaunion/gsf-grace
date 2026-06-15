# GSFGrace 카테고리별 .md 템플릿
> 용도: ChatGPT가 이 프론트매터 스키마를 그대로 채워 완성본 .md를 출력
> ⚠️ 필드명·타입은 `src/content.config.ts`와 100% 일치해야 함 (불일치 시 AG 빌드 실패)
> 작성: Claude / 2026-06-15 (CTA 문구 v1.1 반영)

---

## 공통 규칙

- `slug`(파일명): 영문 소문자 + 하이픈만. 공백·한글·따옴표 금지.
- KO/JA 한 쌍은 **반드시 같은 slug**를 쓴다. 폴더(ja/ko)로 분리되므로 같은 파일명이어도
  충돌하지 않으며, 같아야 언어 스위처가 `/cat/x` ↔ `/ko/cat/x`로 상호 연결된다.
  (AG 라우터가 `post.id.split('/').pop()`로 파일명만 추출 → 폴더로 lang 구분.)
- 저장 경로: `src/content/{category}/{ja|ko}/{slug}.md`
  - JA: `src/content/qa/ja/why-suffering.md`
  - KO: `src/content/qa/ko/why-suffering.md`
- `draft: true`면 미배포. 검수 통과 후 AG가 `false`로.
- `pubDate`: YYYY-MM-DD.

---

## 1. devotion (오늘의 묵상)

```markdown
---
title: "제목"
lang: "ko"
pubDate: 2026-06-15
passage: "시편 23:1-6"
draft: true
---

(본문 250~500자. 말씀 한 구절 → 짧은 묵상 → 오늘의 한 걸음)

---
*더 깊은 이야기가 궁금하시다면, GSFGrace가 왜 이곳에 존재하는지 읽어보세요. → [처음 오셨나요](/ko/story)*
```
> JA 버전: `lang: "ja"`, passage는 일본어 성경표기, CTA는 일본어로 동일 취지.

---

## 2. qa (궁금한 질문) — SEO 핵심

```markdown
---
title: "なぜ神は苦しみを許すのか"
lang: "ja"
pubDate: 2026-06-15
tag: "suffering"
question: "신/하나님은 왜 고통을 허락하는가?"
description: "한 줄 요약 (검색 스니펫용, 80자 내외)"
draft: true
---

(본문 800~1,500자. 질문 공감 → 핵심 답 2~3개 → 결론 한 문장)

---
*질문에 대한 완전한 답보다, 우리는 함께 길을 걸어가는 것을 중요하게 생각합니다. → [처음 오셨나요](/story)*
```
> `tag`는 11개 중 하나: suffering, death, science, bible, jesus, church, prayer, salvation, relations, money, work

---

## 3. walk (니혼바시 에세이)

```markdown
---
title: "제목"
lang: "ko"
pubDate: 2026-06-15
location: "도쿄 니혼바시"
description: "한 줄 요약"
draft: true
---

(본문 600~1,200자. 도쿄 사역·일상의 한 장면 에세이)

---
*이 글에 담긴 이야기가 궁금하셨다면, GSFGrace가 시작된 이유를 소개합니다. → [처음 오셨나요](/ko/story)*
```

---

## 4. story (처음 오셨나요) — collection 아님, 페이지 직접 편집

story는 글이 쌓이는 collection이 아니라 **단 하나의 심장 페이지**다. (확정)
→ GPT는 프론트매터 없이 **본문만** 작성(KO+JA). AG가 `src/pages/story/index.astro`(JA),
`src/pages/ko/story/index.astro`(KO)의 본문 영역에 삽입한다.

```
(본문 1,200~2,000자. 부르심·도쿄·비전. 이 사이트의 심장)
(하단 CTA 대신 본문 끝에 기도/뉴스레터 초대를 자연스럽게 녹임)
```
> 메인 소스: `걸어온 길과 걸어갈 길`. 긴 별도 주제(`걸어갈 길과 전망` — 니혼바시 개척 비전)은
> story가 아니라 **arche collection**으로 분리.

---

## 5. arche (ἀρχή 신학 심층)

```markdown
---
title: "제목"
lang: "ko"
pubDate: 2026-06-15
description: "한 줄 요약"
draft: true
---

(본문 1,500~2,500자. 신학·지성의 깊이. 깊이 추구층 한정)

---
*이 질문이 어디서 시작되었는지 → [처음 오셨나요](/ko/story)*
```

---

## 검수자 체크리스트 (컨펌 전 5초 확인)

- [ ] 카테고리가 매핑표대로인가? (ARK·신설 없음)
- [ ] KO·JA 두 개 다 왔는가?
- [ ] 설교 어조가 빠졌는가? ("~축복합니다" 등)
- [ ] /story CTA가 있는가?
- [ ] 글자 수 상한 이내인가?
- [ ] slug가 영문-하이픈인가? KO/JA가 같은 slug인가?
- [ ] (qa) tag가 11개 중 하나, question·description 채워졌는가?
- [ ] 프론트매터 필드명 오타 없는가?
