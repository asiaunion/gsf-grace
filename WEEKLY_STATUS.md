# GSF-Grace — Weekly Status

---

## [HUB] 프로젝트 요약 (전체 현황판용 공통 필드)

| 필드 | 값 |
|------|-----|
| 최종 업데이트 | 2026-06-15 |
| 프로젝트명 | GSF-Grace |
| 상태 | 🟢 Active |
| 목표 + 기한 | Vercel 배포 + 첫 콘텐츠 — 2026-08-01 베타 론칭 |
| 이번 주 최우선 액션 | Devotion(말씀) 콘텐츠 추가 / Walk P3 준비 |
| 다음 체크포인트 | 2026-06-21 |
| 블로커 | — |

---

## 배포 완료 콘텐츠 현황 (2026-06-15 기준)

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

### Devotion (말씀)
- 미배포 (폴더만 존재)

---

## 작업 이력

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
| 🟡 | Walk location 필드 추가 | 3/31, 12/12 등 |
| 🟡 | author 필드 추가 | AG 지시서 작성됨 |
| 🟡 | Devotion 첫 글 배포 | 말씀 카테고리 공백 |
| 🟢 | QA JA 타이틀 개행 CSS | 낮은 우선순위 |
| 🟢 | Nav 하드코딩 변수화 | |
| 🟢 | 뉴스레터 폼 연동 확인 | |
| 🟢 | content-pipeline git commit 확인 | |
