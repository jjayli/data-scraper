#유튜브 관련 데이터 수집 스크립트 모음#

📌프로젝트 소개 (Introduction)

  * 유튜브와 관련된 데이터를 수집하기 위한 파이썬 스크립트들을 모아 놓는 프로젝트. 
  * 수집된 데이터는 주로 텍스트 분석, 트렌드 모니터링, 데이터 엔지니어링 구축 등에 활용.
  * 모든 스크립트는 최대한 API 키 없이 동작하도록 설계.
  * 수집된 결과는 분석이 용이하도록 구조화된 CSV 형태로 저장.

📂 수집 내용

  youtube/
  * 유튜브 영상의 댓글, 답글 등 관련 데이터를 수집하는 스크립트.
    (댓글 텍스트, 작성자, 좋아요 수, 시간 정보, 채널 정보 등)

🛠️ 시작하기 (Getting Started)

  1. 환경 설정
    * Python 3.8 이상 환경.
    * 필요 라이브러리: pip install youtube-comment-downloader pandas
    
  2. 스크립트 사용 예시
    * youtube/youtube_comment_scraper.py 파일 열기.
    * 스크립트 상단의 TARGET_VIDEO_ID 변수를 원하는 영상 ID 기입.
    * 터미널에서 스크립트 실행
    * 터미널에서 youtube 디렉토리로 이동: cd youtube
    * 스크립트 실행: python youtube_comment_scraper.py
    * 스크립트 실행 후, 각 디렉토리 내에 수집된 데이터의 CSV 파일이 생성. 


📜 라이선스 (License)
이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 LICENSE 파일을 참조.
