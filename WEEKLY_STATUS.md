# GSF-Grace — Weekly Status

---

## [HUB] 프로젝트 요약 (전체 현황판용 공통 필드)

| 필드 | 값 |
|------|-----|
| 최종 업데이트 | 2026-06-18 |
| 프로젝트명 | GSF-Grace |
| 상태 | 🟢 Active |
| 목표 + 기한 | Vercel 배포 + 첫 콘텐츠 — 2026-08-01 베타 론칭 |
| 이번 주 최우선 액션 | AG 잔여작업 일괄 실행 (TASK 1~4) + Kit 계정 준비 |
| 다음 체크포인트 | 2026-06-21 |
| 블로커 | TASK 4(Kit 연동): 목사님 Kit 계정 · Form ID · API Key 준비 필요 |

---

## 배포 완료 콘텐츠 현황 (2026-06-18 기준)

### Walk (니혼바시 에세이)
| slug | KO | JA |
|------|----|----|
| nihon-sketch-1 | ✅ | ✅ |
| nihon-sketch-2 | ✅ | ✅ |
| beginning-again-in-nihonbashi | ✅ | ✅ |
| closer-than-we-think | ✅ | ✅ |
| coming-to-tokyo | ✅ | ✅ |
| growing-familiar | ✅ | ✅ |
| learning-to-wait | ✅ | ✅ |
| the-last-gift | ✅ | ✅ |

### QA (궁금한 질문)
| slug | tag | KO | JA |
|------|-----|----|----|
| who-is-jesus | jesus | ✅ | ✅ |
| where-do-we-come-from | salvation | ✅ | ✅ |
| why-is-life-so-broken | salvation | ✅ | ✅ |
| will-god-accept-me | salvation | ✅ | ✅ |
| is-there-hope-beyond-death | salvation | ✅ | ✅ |

### Arche (αρχή)
| slug | KO | JA |
|------|----|----|
| nihonbashi-vision | ✅ | ✅ |
| gsm | ✅ | ✅ |

### Story (처음 오셨나요?)
| 페이지 | 상태 |
|--------|------|
| `/story` (JA) | ✅ |
| `/ko/story` (KO) | ✅ |

### Devotion (みことば / 말씀)
| slug | 본문 | 제목 | 날짜 | JA | KO |
|------|------|------|------|----|----|
| — | 創世記 28:10-19; 32:27-30 | 天への道が開かれるとき | 2026/6/10 | ✅ | — |
| — | 詩篇 23:1-6 | 荒野にも羊飼いはおられる | 2026/6/12 | ✅ | — |
| — | 詩篇 90:1-17 | 自らの日を数える知恵 | 2026/6/13 | ✅ | — |
| — | 詩篇 91:1-16 | 全能者の陰の下で | 2026/6/15 | ✅ | — |

---

## 작업 이력

- 2026-06-18: Devotion 4편 배포 완료 확인 (gsfgrace.com/devotion 라이브 확인)
- 2026-06-15: 세션 E — 라이브 사이트 전체 검증 완료 (Story KO/JA, QA 5개 KO/JA 정상 확인)
- 2026-06-15: QA 5개 전체 배포 완료 (3분복음 4파트 + who-is-jesus)
- 2026-06-15: nav 로고 리디자인 — GSF 버튼 유지 + Grace 브라스 볼드 텍스트 + 외곽 테두리 박스 배포 완료.
- 2026-06-15: QA 5개 글 시리즈 다음 글 링크 추가 (KO/JA) 배포 완료.
- 2026-06-15: 전체 prose 행간·max-width 통일, 인용구 스타일 변경, nav みことば/말씀 수정.
- 2026-06-15: Walk P1/P2 nihon-sketch-1,2 배포 완료 (KO/JA).
- 2026-06-15: Story 페이지 "걸어온 길과 걸어갈 길" KO/JA 배포 완료. 보관본 저장.
- 2026-06-15: Walk/Arche 카테고리 본문 중복 H1 타이틀 제거. Arche 문서 2건 배포.
- 2026-06-14: Astro v6 스캐폴딩 완료. GitHub 레포 생성 (asiaunion/gsf-grace). 7개 라우트 구조.

---

## 잔여 미결 항목

| 우선순위 | 항목 | 비고 |
|----------|------|------|
| 🔴 | **TASK 1** Walk location/author 필드 추가 (JA/KO 6쌍) | AG 지시서 발행됨 |
| 🔴 | **TASK 2** Devotion KO author 필드 명시 | AG 지시서 발행됨 |
| 🔴 | **TASK 3** Nav config 분리 (navItems 변수화) | AG 지시서 발행됨 |
| 🔴 | **TASK 4** 뉴스레터 Kit 연동 | ⚠️ Kit 계정·Form ID·API Key 준비 필요 |
| 🟡 | Walk P3 준비 | 기술 작업 완료 후 검토 |
| 🟢 | QA JA 타이틀 개행 CSS | 낮은 우선순위 |
| 🟢 | content-pipeline git commit 확인 | |

---

## 📝 작업 로그

### 2026-06-18 (세션 D)
- GSFGrace 잔여 작업 분석 완료 (Claude)
- AG 지시서 일괄 작성: `AG_지시서_잔여작업일괄_2026-06-18.md` (TASK 1~4)
- 뉴스레터 서비스 Buttondown → Kit(ConvertKit) 으로 결정
- TASK 4 블로커: 목사님 Kit 계정 준비 필요 (https://kit.com)

### 2026-06-18
- Devotion 4편 배포 완료 확인 (gsfgrace.com/devotion 라이브 스크린샷 확인)
  - 創世記 28:10-19 / 詩篇 23, 90, 91
- WEEKLY_STATUS.md 업데이트 (Devotion 현황 반영)

### 2026-06-15
- GSFGrace 로고 UI 일체형 버튼 디자인 개선
- Devotion 묵상 글 3편 추가 및 다국어(ko/ja) 배포
- Devotion 인트로 및 Story 뉴스레터 문구 수정
