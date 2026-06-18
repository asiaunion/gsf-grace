# _handoff.md — Claude 부재 구간 핸드오프 기록
> AG가 배포 작업 완료 시마다 append 방식으로 기록.
> Claude가 다음 세션 시작 시 이 파일을 읽어 컨텍스트 복원.
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
- 커밋 해시: af9ea5d
- 배포 URL: https://gsfgrace.com
- Claude 부재 여부: 예
- 특이사항: Vercel 자동 배포 트리거를 위해 main 브랜치로 병합 후 푸시 완료
