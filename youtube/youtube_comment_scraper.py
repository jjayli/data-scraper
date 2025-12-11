#유튜브 비디오 댓글 수집

import pandas as pd
import time
from youtube_comment_downloader import *

TARGET_VIDEO_ID = "VIDEO_ID_HERE" 
OUTPUT_FILENAME = f"youtube_comments_{TARGET_VIDEO_ID}.csv"

def scrape_youtube_comments(video_id: str) -> list:
    """
    Args:
        video_id (str): 수집할 영상의 고유 ID (The unique ID of the video to scrape).
        
    Returns:
        list: 수집된 댓글 데이터가 담긴 리스트 (A list containing the scraped comment data).
    """
    
    comment_data_list = []
    
    try:
        # 1. 다운로더 객체 생성
        downloader = YoutubeCommentDownloader()
        
        print(f"[정보] '{video_id}' 영상의 댓글 수집을 시작합니다.")
        
        # 2. 댓글 및 답글 모두 가져오기
        # get_comments_from_youtube 함수는 Generator 객체를 반환합니다.
        comments_generator = downloader.get_comments_from_youtube(
            video_id, 
            sort_by=SORT_BY_POPULAR
        )
        
        for comment in comments_generator:
            # 3. 최상위 댓글 정보 추출 및 저장
            comment_id = comment.get('cid')
            
            top_level_comment = {
                'comment_id': comment_id,
                'is_reply': False,
                'parent_id': None,
                'author': comment.get('author'),
                'text': comment.get('text'),
                'time': comment.get('time'),
                'votes': comment.get('votes'),
                'replies_count': comment.get('replies', 0),
                'photo': comment.get('photo')
            }
            comment_data_list.append(top_level_comment)
            
            # 4. 답글 처리
            replies = comment.get('replies', [])
            if replies:
                for reply in replies:
                    # 데이터 구조
                    reply_comment = {
                        'comment_id': reply.get('cid'),
                        'is_reply': True,
                        'parent_id': comment_id, # 부모 댓글 ID를 명시
                        'author': reply.get('author'),
                        'text': reply.get('text'),
                        'time': reply.get('time'),
                        'votes': reply.get('votes'),
                        'replies_count': 0, 
                        'photo': reply.get('photo')
                    }
                    comment_data_list.append(reply_comment)

        print(f"\n[성공] 총 {len(comment_data_list)}개의 댓글 및 답글 수집 완료.")
        return comment_data_list
                
    except Exception as e:
        print(f"\n[오류] 댓글 수집 중 오류 발생: {e}")
        return []

def export_to_csv(data_list: list, filename: str):
    """
    Converts the collected comment data to a Pandas DataFrame and saves it to a CSV file.
    """
    if not data_list:
        print("[경고] 저장할 데이터가 없습니다.")
        return

    try:
        # Pandas DataFrame 생성
        df = pd.DataFrame(data_list)
        
        # CSV 파일로 저장 (UTF-8-SIG 인코딩은 엑셀에서 한글 깨짐 방지를 위해 사용)
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        
        print(f"[성공] 데이터가 '{filename}' 파일로 저장되었습니다.")
    except Exception as e:
        print(f"[오류] CSV 파일 저장 중 오류 발생: {e}")


if __name__ == "__main__":
    try:
        import pandas as pd
    except ImportError:
        exit()

    if TARGET_VIDEO_ID == "VIDEO_ID_HERE":
        print("[경고] TARGET_VIDEO_ID를 실제 유튜브 영상 ID로 변경한 후 실행해주세요.")
    else:
        # 댓글 수집 실행
        collected_data = scrape_youtube_comments(TARGET_VIDEO_ID)
        
        # CSV로 저장 실행
        if collected_data:
            export_to_csv(collected_data, OUTPUT_FILENAME)
