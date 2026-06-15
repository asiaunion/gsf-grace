# GSFGrace 콘텐츠 파이프라인
> 설교·원고 → GSFGrace.com 블로그 콘텐츠 편집·배포 운영 폴더
> 작성: Claude / 2026-06-15

---

## 폴더 구성

```
content-pipeline/
├── README.md            ← 이 파일 (진입점)
├── EDIT_CHARTER.md      ← ① GPT 시스템 프롬프트 (제약·규칙)
├── CONTENT_TEMPLATES.md ← ② 출력 형식 (프론트매터 스키마)
├── CONTENT_MAPPING.md   ← ③ 소스→카테고리 매핑 (Phase 우선순위)
└── sources/             ← 설교·간증·선교편지 원문 (편집 원자재)
```

> 디자인·운영 문서(BRAND.md, AG 지시서)는 `../docs/`에 별도 보관.
> 최종 배포본은 `../src/content/`.

---

## ChatGPT에게 전달하는 방법

새 GPT 세션에 아래를 **순서대로** 붙여넣는다:

1. `EDIT_CHARTER.md` 전문 (시스템 프롬프트)
2. `CONTENT_TEMPLATES.md` 전문 (출력 형식)
3. `CONTENT_MAPPING.md`에서 편집할 글의 행 (카테고리·검색어 지정)
4. `sources/`의 해당 설교 원문 1편

→ GPT는 **KO+JA 완성본 .md 2개**를 코드블록으로 출력.
   (일본어 설교는 KO 대역본 + JA 편집본)

이후부터는 1~2를 다시 붙일 필요 없이, **설교 원문만** 전달하면 된다.

---

## 편집 → 배포 흐름

```
GPT 출력 (KO+JA .md)
  → (초기 몇 편: Claude 검수)
  → 승주님 컨펌
  → AG: 스키마 확인 → src/content/{cat}/{ja|ko}/ 저장
       → npm run build → draft:false → git push
  → Vercel 자동배포 → URL 확인
```

검수 기준: `CONTENT_TEMPLATES.md` 하단 "검수자 체크리스트".

---

## 현재 우선순위 (CONTENT_MAPPING 참조)

- **P1**: 일본어 완성본 3편 + 니혼 스케치 #1 (번역 부담 최소)
- **P2**: 걸어온 길(Story) + 마유미 간증(Contributors)
- **P3**: 시편 3편 (시23·시90·시91)
- 이후 Q&A 역설계 → 선교편지 → 출애굽 시리즈
