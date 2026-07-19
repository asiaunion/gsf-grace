# AG 배포 지시문 — GSF-Grace 아르케 12개 파일
> 작성: Claude (2026-06-23)
> 담당: AG
> 우선순위: 즉시 실행
> 레포: GSF-Grace (`gsfgrace.com`)

---

## 배경

세션 S에서 GSF-Calling 1차 정본(v1.5/v1.3/v0.4) 기반으로 아르케 콘텐츠를 전면 작성 완료.
신규 슬러그 4개 추가 (ko+ja 각 1 = 8개) + 기존 슬러그 2개 갱신 (ko+ja 각 1 = 4개). 총 12개 파일 배포 대기 중.

---

## TASK 1 — 파일 12개 복사 (신규 8 + 덮어쓰기 4)

**레포 루트:** `/Users/gsf/.gemini/antigravity/scratch/projects/GSF-Grace`

소스: `content-pipeline/_approved/` → 대상: `src/content/arche/ko/` 및 `src/content/arche/ja/`

| 소스 파일 (`_approved/`) | 대상 경로 (`src/content/arche/`) | 비고 |
|--------------------------|----------------------------------|------|
| `arche_gsf-vision_ko.md` | `ko/gsf-vision.md` | 🆕 신규 |
| `arche_gsf-vision_ja.md` | `ja/gsf-vision.md` | 🆕 신규 |
| `arche_gsf-manifesto_ko.md` | `ko/gsf-manifesto.md` | 🆕 신규 |
| `arche_gsf-manifesto_ja.md` | `ja/gsf-manifesto.md` | 🆕 신규 |
| `arche_gsf-statement_ko.md` | `ko/gsf-statement.md` | 🆕 신규 |
| `arche_gsf-statement_ja.md` | `ja/gsf-statement.md` | 🆕 신규 |
| `arche_gsf-oikos-framework_ko.md` | `ko/gsf-oikos-framework.md` | 🆕 신규 |
| `arche_gsf-oikos-framework_ja.md` | `ja/gsf-oikos-framework.md` | 🆕 신규 |
| `arche_gsm_ko.md` | `ko/gsm.md` | 🔄 덮어쓰기 |
| `arche_gsm_ja.md` | `ja/gsm.md` | 🔄 덮어쓰기 |
| `arche_nihonbashi-vision_ko.md` | `ko/nihonbashi-vision.md` | 🔄 덮어쓰기 |
| `arche_nihonbashi-vision_ja.md` | `ja/nihonbashi-vision.md` | 🔄 덮어쓰기 |

> ⚠️ `gsm.md` · `nihonbashi-vision.md` 는 기존 파일 덮어쓰기. 백업 불필요 (git 이력로 복원 가능).

---

## TASK 2 — Astro content collection schema 확인

`src/content/config.ts` (또는 `content.config.ts`) 에서 `arche` collection 정의 확인.

**신규 슬러그가 schema 제약에 걸리지 않는지 확인:**
- `gsf-vision`, `gsf-manifesto`, `gsf-statement`, `gsf-oikos-framework`
- frontmatter 필드: `title`, `lang`, `pubDate`, `description`, `draft` — 기존 파일과 동일 구조

schema 변경 불필요하면 스킵. 변경 필요 시 Joseph에게 보고 후 처리.

---

## TASK 3 — 내부 링크 동작 확인 (빌드 후)

| 문서 | 링크 | 기대 URL |
|------|------|----------|
| GSF 매니페스토 KO | OIKOS Framework | `/ko/arche/gsf-oikos-framework` |
| GSF 매니페스토 JA | OIKOS Framework | `/arche/gsf-oikos-framework` |
| GSF 스테이트먼트 KO | OIKOS Framework | `/ko/arche/gsf-oikos-framework` |
| GSF 스테이트먼트 JA | OIKOS Framework | `/arche/gsf-oikos-framework` |
| OIKOS Framework KO | Good Samaritan Mission | `/ko/arche/gsm` |
| OIKOS Framework KO | 니혼바시 비전 | `/ko/arche/nihonbashi-vision` |
| OIKOS Framework JA | Good Samaritan Mission | `/arche/gsm` |
| OIKOS Framework JA | 니혼바시 비전 | `/arche/nihonbashi-vision` |

404 발생 시 Joseph에게 보고.

---

## TASK 4 — 빌드 · 배포

```bash
cd /Users/gsf/.gemini/antigravity/scratch/projects/GSF-Grace
git add src/content/arche/
git commit -m "feat(arche): deploy 12 files — GSF Foundations + OIKOS Framework"
git push origin main
```

Vercel 자동 배포 트리거 확인. 빌드 오류 시 Joseph에게 보고.

---

## TASK 5 — 완료 후 _handoff.md append

배포 완료 후 아래 형식으로 `content-pipeline/_handoff.md` 에 append:

```
## [YYYY-MM-DD HH:MM] AG 배포 완료
- 작업 내용: 아르케 12개 파일 배포 (신규 8 + 갱신 4 — GSF Foundations + OIKOS Framework)
- 커밋 해시: [hash]
- 배포 URL: https://gsfgrace.com/arche
- Claude 부재 여부: 예
- 특이사항: [있으면 기재]
```

---

## 참고 — 아르케 최종 구조

```
[A. GSF Foundations]
  ├── GSF 비전 / GSFビジョン           (ko/gsf-vision · ja/gsf-vision)
  ├── GSF 매니페스토 / GSFマニフェスト  (ko/gsf-manifesto · ja/gsf-manifesto)
  └── GSF 스테이트먼트 / GSFステートメント (ko/gsf-statement · ja/gsf-statement)

[B. GSF OIKOS Framework]
  └── 아직 오지 않은 공동체를 향하여    (ko/gsf-oikos-framework · ja/gsf-oikos-framework)

[C. 개별 실천 문서]
  ├── Good Samaritan Mission           (ko/gsm · ja/gsm)
  └── 니혼바시 비전 / 日本橋ビジョン    (ko/nihonbashi-vision · ja/nihonbashi-vision)
```
