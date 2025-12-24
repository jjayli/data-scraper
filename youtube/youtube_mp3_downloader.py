# 1. yt-dlp 설치
# !pip install yt-dlp
# !apt-get update -y
# !apt-get install ffmpeg -y
import yt_dlp
from google.colab import files
import os

def download_youtube_as_mp3():
    # 1. 유튜브 URL 입력받기
    url = input("추출하고 싶은 유튜브 URL을 입력하세요: ")

    # 2. 저장 설정 (고음질 320kbps MP3)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        
        # 재생목록 무시 설정 추가
        'noplaylist': True, 
    }

    try:
        print(f"\n'{url}' 에서 오디오 추출을 시작합니다...")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 정보 가져오기 및 다운로드
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
            # 파일명 확장자 mp3로 변경
            base, ext = os.path.splitext(filename)
            mp3_filename = base + ".mp3"
            
            print(f"\n변환 완료: {mp3_filename}")
            
            # 3. 브라우저로 파일 내보내기
            print("파일 다운로드를 시작합니다...")
            files.download(mp3_filename)
            
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

# 함수 실행
download_youtube_as_mp3()
