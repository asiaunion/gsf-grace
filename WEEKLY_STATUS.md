# GSF-Grace — Weekly Status

---

## [HUB] 프로젝트 요약 (전체 현황판용 공통 필드)

| 필드 | 값 |
|------|-----|
| 최종 업데이트 | 2026-06-23 |
| 프로젝트명 | GSF-Grace |
| 상태 | 🟢 Active |
| 목표 + 기한 | GSF-Sermon 연계 포스팅 체계 구축 — 2026-08-01 베타 론칭 |
| 이번 주 최우선 액션 | GSF-Sermon 연계 포스팅 주제 구상 |
| 다음 체크포인트 | GSF-Sermon 첫 설교 준비 시 |
| 블로커 | 없음 |

---

## 콘텐츠 Phase 클로징 현황 (2026-06-19)

| Phase | 내용 | 상태 |
|-------|------|------|
| P1 | Story + 니혼 스케치 + Walk 초기 에세이들 | ✅ 완료 |
| P2 | 마유미 간증 + 걸어갈 길과 전망(arche) | ✅ 완료 (arche: "왜, 이곳이 존재하는가"로 풀어서 설명) |
| P3 | 시편 3편 Devotion (시23·시90·시91) | ✅ 완료 |
| P4 | QA 5편 (3분복음 4파트 + 하나님은 나 같은 사람도 받아주실까?) | ✅ 완료 (검색어 역설계 아닌 복음 직접 전달 방식) |
| P5 | 선교편지 6편 → Walk | ✅ 완료 |
| P6 | 출애굽 8편 시리즈 | 🔵 미착수 — 급하지 않음, 보류 |

> **P1~P5 종료 클로징 (2026-06-19)**
> 마유미 간증(Walk)은 미완이나 급하지 않아 보류.
> 출애굽 8편도 어조 변환 부담으로 후순위 유지.
> 이후 포스팅은 GSF-Sermon 연계 방식으로 전환.

---

## 배포 완료 콘텐츠 현황 (2026-06-19 기준)

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
| 선교편지 6편 → Walk | ✅ | ✅ |

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
| 걸어갈 길과 전망 → "왜, 이곳이 존재하는가" | ✅ | ✅ |

### Story (처음 오셨나요?)
| 페이지 | 상태 |
|--------|------|
| `/story` (JA) | ✅ |
| `/ko/story` (KO) | ✅ |

### Devotion (みことば / 말씀)
| slug | 본문 | 제목 | JA | KO |
|------|------|------|----|----|
| the-road-opens | 創世記 28:10-19; 32:27-30 | 天への道が開かれるとき | ✅ | ✅ |
| shepherd-in-the-wilderness | 詩篇 23:1-6 | 荒野にも羊飼いはおられる | ✅ | ✅ |
| number-our-days | 詩篇 90:1-17 | 自らの日を数える知恵 | ✅ | ✅ |
| under-the-shadow | 詩篇 91:1-16 | 全能者の陰の下で | ✅ | ✅ |

### 인프라 / 기능
| 항목 | 상태 | 비고 |
|------|------|------|
| Walk location/author 필드 (JA/KO 6쌍) | ✅ | TASK 1 |
| Devotion KO author 필드 명시 | ✅ | TASK 2 |
| Nav config 분리 (`src/config/nav.ts`) | ✅ | TASK 3 |
| Kit(ConvertKit) 뉴스레터 연동 | ✅ | TASK 4 — Form ID: 9581029 |
| `/thank-you` 페이지 | ✅ | Kit 리다이렉트 완료 |
| QA JA 타이틀 개행 CSS | ✅ | 완료 |

---

## 다음 단계 — GSF-Sermon 연계 포스팅

> **방향 전환 (2026-06-19)**
> P1~P5 초기 콘텐츠 풀 소진 완료. 이후 GSFGrace 포스팅은 GSF-Sermon 설교 연구와 연계.
> GSF-Sermon이 본격 가동되면 설교 연구 → Devotion/Walk 파생 포스팅으로 자연스럽게 연결.
> 그 전까지는 가벼운 주제를 구상해 간헐적으로 발행.

| 항목 | 내용 | 상태 |
|------|------|------|
| GSF-Sermon 연계 포스팅 주제 구상 | 누가-행전 연구 중 파생될 Devotion/Walk 후보 | 🔜 구상 중 |
| 마유미 간증 (Walk, author: Mayumi) | 소재 준비됨, 급하지 않음 | 🔵 보류 |
| 출애굽 8편 시리즈 (Devotion) | 어조 변환 부담, 후순위 | 🔵 보류 |

---

## 작업 이력

- 2026-06-19: P1~P5 클로징 확정 (승주님 확인) — 이후 GSF-Sermon 연계 방식으로 전환
- 2026-06-19: WEEKLY_STATUS.md 전면 갱신 (Claude)
- 2026-06-19: TASK 1~4 완료 반영
- 2026-06-18: TASK 1~4 일괄 배포 (AG, af9ea5d, 389558b)
- 2026-06-18: Kit 핫픽스 (bef8291), /thank-you 페이지 (2be45eb, 8450209)
- 2026-06-18: E2E 테스트 완료
- 2026-06-15: 라이브 사이트 전체 검증 완료
- 2026-06-14: Astro v6 스캐폴딩 완료, GitHub 레포 생성 (asiaunion/gsf-grace)


## 📝 작업 로그
### 2026-06-23
- AG_DEPLOY_arche-14files_2026-06-23.md 지시문에 따른 아르케 파일 12개 복사 및 배포 완료
- pubDate 역순 조정 완료 (6.18~6.23)
