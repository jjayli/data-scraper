# YouTube 데이터 수집 스크립트 모음

📌 프로젝트 소개 (Introduction)

   이 프로젝트는 유튜브와 관련된 데이터를 수집하기 위한 파이썬 스크립트들을 모아 놓는 프로젝트입니다.
   
   수집된 데이터는 주로 텍스트 분석, 트렌드 모니터링, 데이터 엔지니어링 포트폴리오 구축 등에 활용됩니다.
   
   모든 스크립트는 최대한 Google API 키 없이 동작하도록 설계되어, 접근이 용이합니다.
   
   수집된 결과는 분석이 용이하도록 구조화된 CSV 형태로 저장됩니다.

📂 수집 내용 (Scraping Content)

   수집 항목
  
    댓글, 작성자, 좋아요 수, 작성 시간 정보 등


🛠️ 시작하기 (Getting Started)

 1. 환경 설정

  Python 3.8 이상 환경. 아래 명령어를 사용하여 필요한 라이브러리를 설치 필요.

    pip install youtube-comment-downloader pandas


 2. 스크립트 사용 예시

  youtube/youtube_comment_scraper.py를 실행하는 방법

   youtube/youtube_comment_scraper.py 파일을 엽니다.

   스크립트 상단의 TARGET_VIDEO_ID 변수에 원하는 영상의 고유 ID를 기입합니다.
   
   터미널을 열고 다음 명령을 순서대로 실행합니다.
   
   터미널에서 youtube 디렉토리로 이동
   
    cd youtube
   
   스크립트 실행
   
    python youtube_comment_scraper.py


📜 라이선스 (License)

 이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 최상위 경로의 LICENSE 파일을 참조해주세요.
