# _handoff.md — Claude 부재 구간 핸드오프 기록 (GSF-Grace)
> AG가 GSF-Grace 배포 작업 완료 시마다 append 방식으로 기록.
> Claude가 다음 세션 시작 시 이 시 파일을 읽어 컨텍스트 복원.
> 규칙: `scratch/AGENTS.md` → 핸드오프 자동 기록 규칙 참조.

---

<!-- AG: 배포 완료 시 아래 형식으로 append -->
<!--
## [YYYY-MM-DD HH:MM] AG 배포 완료
- 작업 내용:
- 커밋 해시:
- 배포 URL:
- Claude 부재 여부:
- 특이사항:
-->

## [2026-06-18 18:25] AG 배포 완료
- 작업 내용: TASK 1~4 (Walk/Devotion 메타데이터 추가, Nav config 분리, ConvertKit 뉴스레터 폼 JA/KO 연동)
- 커밋 해시: af9ea5d, 389558b
- 배포 URL: https://gsfgrace.com
- Claude 부재 여부: 예
- 특이사항: Vercel 자동 배포 트리거를 위해 main 브랜치로 병합 후 푸시 완료

## [2026-06-18 18:30] AG 핫픽스 배포 완료
- 작업 내용: Vercel 환경변수 누락으로 인한 Kit API 401 오류 핫픽스
- 커밋 해시: bef8291
- 배포 URL: https://gsfgrace.com
- Claude 부재 여부: 예
- 특이사항: `import.meta.env` 환경변수 뒤에 하드코딩 Fallback 문자열(`|| '9581029'`)을 추가하여 Vercel 대시보드 환경변수 설정 없이도 동작하도록 수정 후 main 푸시 완료

## [2026-06-18 19:03] AG 배포 완료
- 작업 내용: 뉴스레터 구독 완료 후 사용할 `/thank-you` 페이지 생성 (JA/KO 지원)
- 커밋 해시: 2be45eb
- 배포 URL: https://gsfgrace.com/thank-you
- Claude 부재 여부: 예
- 특이사항: 지시서 내 TASK 2(Kit 대시보드 리다이렉트 변경)는 사용자가 직접 수행해야 함

## [2026-06-18 19:07] AG 배포 완료
- 작업 내용: `/thank-you` 페이지 내 서명 문구 업데이트(한자 및 한글 이름 표기 추가)
- 커밋 해시: 8450209
- 배포 URL: https://gsfgrace.com/thank-you
- Claude 부재 여부: 예
- 특이사항: `AG_thankyou_2026-06-18.md` 수정본 재적용 완료

## [2026-06-23] Claude 아르케 콘텐츠 1차 작업 완료 — 배포 대기

### 작업 내용
GSF-Calling 1차 정본(v1.5/v1.3/v0.3) 확정 내용을 gsfgrace.com 아르케 섹션에 반영.
신규 6개 파일 생성 + 기존 4개 파일 갱신. 총 10개 파일.

### 파일 목록 (`content-pipeline/_approved/`)

| 파일 | 상태 | 비고 |
|------|------|------|
| `arche_gsf-vision_ko.md` | 🆕 신규 | GSF 비전 KO |
| `arche_gsf-vision_ja.md` | 🆕 신규 | GSF ビジョン JA |
| `arche_gsf-manifesto_ko.md` | 🆕 신규 | GSF 매니페스토 KO |
| `arche_gsf-manifesto_ja.md` | 🆕 신규 | GSF マニフェスト JA (궁극的に 수정 포함) |
| `arche_gsf-statement_ko.md` | 🆕 신규 | GSF 스테이트먼트 KO |
| `arche_gsf-statement_ja.md` | 🆕 신규 | GSF ステートメント JA (꼬임 문장 수정 포함) |
| `arche_gsm_ko.md` | 🔄 갱신 | 서문 + G·S·M 신학 + 구조 정렬 |
| `arche_gsm_ja.md` | 🔄 갱신 | 同上 JA |
| `arche_nihonbashi-vision_ko.md` | 🔄 갱신 | 저희 + Flourishing 언어 정렬 |
| `arche_nihonbashi-vision_ja.md` | 🔄 갱신 | 同上 JA |

---

## [2026-06-23] Claude 아르케 콘텐츠 2차 작업 완료 — 배포 대기

### 작업 내용
GSF 문서 구조 재정의 (Ark ↔ Grace → OIKOS) + OIKOS Framework 신규 추가.
총 6개 파일 수정/신규.

### 확정된 아르케 문서 구조 (최종)

```
[A. GSF Foundations]
  ├── GSF 비전 / GSFビジョン
  ├── GSF 매니페스토 / GSFマニフェスト  → OIKOS Framework 링크
  └── GSF 스테이트먼트 / GSFステートメント
       (Ark ↔ Grace → OIKOS 흐름 명시)
       → OIKOS Framework 링크

[B. GSF OIKOS Framework]  ← 허브 문서 (짧음)
  └── 아직 오지 않은 공동체를 향하여 / まだ来ていない共同体へ
       → Good Samaritan Mission 링크
       → 니혼바시 비전 링크

[C. 개별 실천 문서]
  ├── Good Samaritan Mission (KO/JA)
  └── 니혼바시 비전 / 日本橋ビジョン (KO/JA)
```

### 파일 목록 (`content-pipeline/_approved/`)

| 파일 | 상태 | 비고 |
|------|------|------|
| `arche_gsf-statement_ko.md` | 🔄 갱신 | Ark↔Grace→OIKOS 구조 반영 + Grace 말미 링크 문구 보강 |
| `arche_gsf-statement_ja.md` | 🔄 갱신 | 同上 JA |
| `arche_gsf-manifesto_ko.md` | 🔄 갱신 | 링크 → gsf-oikos-framework |
| `arche_gsf-manifesto_ja.md` | 🔄 갱신 | 링크 → gsf-oikos-framework |
| `arche_gsf-oikos-framework_ko.md` | 🆕 신규 | 허브 문서 (GSM + 니혼바시 비전 안내) |
| `arche_gsf-oikos-framework_ja.md` | 🆕 신규 | 同上 JA |

### GSF-Calling repo 변경

| 파일 | 상태 | 비고 |
|------|------|------|
| `02-GSF-Statement.md` | 🔄 v0.4 | §1·§5 구조 재정렬 |
| `03-GSF-OIKOS-Framework.md` | 🆕 v0.1 | Statement 미래형 대응 문서 신규 생성 |

### Cursor 배포 지시 (전체 누적)

1. `_approved/arche_gsf-*.md` 8개 → `src/content/arche/` 복사/덮어쓰기
2. `_approved/arche_gsm_*.md` 2개 → `src/content/arche/` 덮어쓰기
3. `_approved/arche_nihonbashi-vision_*.md` 2개 → `src/content/arche/` 덮어쓰기
4. Astro content collection schema — 신규 슬러그 확인
   - `gsf-vision`, `gsf-manifesto`, `gsf-statement`, `gsf-oikos-framework`
   - KO: `/ko/arche/`, JA: `/arche/`
5. 내부 링크 동작 확인
   - Manifesto → `/ko/arche/gsf-oikos-framework` / `/arche/gsf-oikos-framework`
   - Statement → `/ko/arche/gsf-oikos-framework` / `/arche/gsf-oikos-framework`
   - OIKOS Framework → `/ko/arche/gsm` + `/ko/arche/nihonbashi-vision`
6. 배포 완료 후 이 파일에 append

### 특이사항
- GSF-Calling `02-GSF-Statement.md` v0.4 — §1·§5 수정 완료
- GSF-Calling `03-GSF-OIKOS-Framework.md` v0.1 신규 생성
- OIKOS Framework는 허브 문서 (짧음) — GSM·니혼바시 비전 본문은 개별 파일 유지
- Claude 부재 여부: 아니오 (Claude 작성, Cursor 배포 담당)

## [2026-06-23 23:17] AG 배포 완료
- 작업 내용: 아르케 12개 파일 배포 (신규 8 + 갱신 4 — GSF Foundations + OIKOS Framework)
- 커밋 해시: aad69d5
- 배포 URL: https://gsfgrace.com/arche
- Claude 부재 여부: 예

## [2026-06-23 23:23] AG 추가 수정 완료
- 작업 내용: 아르케 문서 12개 pubDate를 흐름(Foundations -> OIKOS -> Missions)에 따라 오늘로부터 하루씩 과거로 거슬러 올라가며 재설정 (06-18 ~ 06-23)
- 커밋 해시: 6645e9f
- 배포 URL: https://gsfgrace.com/arche
- Claude 부재 여부: 예
