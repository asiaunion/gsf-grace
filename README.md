# GSFGrace — Hodos Tokyo

> ὁδός — 道 — 길 | Receive Life. Become Mercy.

**GSFGrace**는 도쿄 니혼바시에서 발신하는 복음 채널입니다.

## 기술 스택

- **Framework**: [Astro](https://astro.build) v6
- **Deployment**: [Vercel](https://vercel.com)
- **Domain**: [gsfgrace.com](https://gsfgrace.com)

## 사이트 구조

| 경로 | 역할 | 우선순위 |
|------|------|---------|
| `/` | 홈 | — |
| `/story` | 처음 오셨나요? (부르심·비전) | ★★★ |
| `/devotion` | 오늘의 묵상 | ★★ |
| `/faith-life` | 삶과 신앙 에세이 | ★★ |
| `/walk` | 걸어가며 (도쿄 사역 일지) | ★★★ |
| `/qa/[tag]/[slug]` | 궁금한 질문 (SEO 핵심) | ★★★ |
| `/arche` | アルケ — 지적 깊이 (準備中) | ★ |

## 언어 전략

**JA First** — 일본어가 기본 언어  
KO Secondary — 한국어 지원  
EN — 추후 예정

## 개발

```bash
# 의존성 설치 (monorepo workspace에서 실행)
cd /path/to/scratch  # 루트 워크스페이스
npm install --legacy-peer-deps

# 개발 서버 (GSF-Grace 디렉토리에서)
cd projects/GSF-Grace
npm run dev

# 빌드
npm run build
```

## Phase 1 목표

- 뉴스레터 구독자 50명
- Q&A 30개 (태그별 2~3개)
- Walk 20개
- **정기 연락하는 사람 5명 (Oikos의 씨앗)**

## 참고 설계 문서

- `projects/GSF-OS/Wiki/GSFGrace_Platform_Architecture.md` — v3.0 승인 완료
- `projects/GSF-Calling/docs/00-Calling-and-Manifesto-ko.md` — 헌장

---

*承柱 목사, 도쿄 니혼바시에서*
