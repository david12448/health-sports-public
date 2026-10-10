# 공개 정보구조와 SEO 준비 상태

## 탐색 UI
- 10개 1차 카테고리와 18개 검색용 주제 인덱스를 시범 구축.
- 공개 항목은 검수 준비 상태만 표기; 의료 절차 설명은 공개하지 않음.
- 단어 검색 + 주제 필터, 모바일 반응형, 긴급 119 안내, 보조기기 접근성 기본 적용.
- 데이터와 내부 수집 소스 원본을 분리; 공개 데이터에 수집 원본 URL/매핑/비밀정보를 넣지 않음.

## 고정 URL 계획 (검수 후 도입)
- /emergency/burn/
- /emergency/choking/
- /symptoms/chest-pain/
- /body/hand/
- /departments/dentistry/
- /care/traditional-medicine/
- /procedures/cosmetic-safety/
- /habits/smartphone-posture/
- /exercise/squat/
기존 GitHub Pages 및 쿼리 주소가 존재하게 되면 리디렉션/호환 레이어를 유지하고 경로 직접 접속/새로고침 테스트를 실시한다. 커스텀 서브도메인 확정 전에는 canonical을 생성하지 않는다.

## 게시 승인 전 상태
- 분류 UI에 noindex 설정 유지.
- 119 위험 신호 안내는 간결히 표시. 증상별 진단/절차는 비공개 초안과 전문가 검증 후에 게시.
- 외부 공식 자료 원본 링크/매핑은 향후 서버 측 리다이렉트로 운영. GitHub Pages 정적 코드만으로 링크 목적지를 영구 은닉할 수 없음을 인지한다.
- 광고·제휴는 의료정보와 분리하고 응급 콘텐츠에서 배제.
- 스포츠 경기 정보는 추후 별도 데이터 모듈로 연계하며 도박성 서비스 기능을 제공하지 않는다.

## 테스트
Pull request 시 Python 표준 라이브러리로 JSON 구조/공개 데이터 내부 URL 노출 여부/상태를 검사한다. GitHub Actions에 정기 스케줄은 지정하지 않았다.
