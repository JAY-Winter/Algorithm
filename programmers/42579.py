def solution(genres, plays):
    answer = []
    
    # 장르별 플레이 횟수 초기 세팅
    song_dict = {genre: 0 for genre in genres}
    
    # 장르별 플레이 횟수 세팅
    for genre, play in zip(genres, plays):
        song_dict[genre] += play
        
    # 장르별 재생 횟수 구한 다음 횟수가 많은 순으로 정렬
    sorted_genre_cnt = sorted(song_dict.items(), key=lambda item: (-item[1]))
    
    # 매개변수로 받은 장르, 재생횟수를 index 를 포함해서 재정의
    songs_with_index = [(genre, play, index) for index, (genre, play) in enumerate(zip(genres, plays))]
    
    # index 까지 포함된 매개변수를 재생횟수가 많은 순으로 정렬
    sorted_songs = sorted(songs_with_index, key=lambda item: (-item[1]))
    
    # 총 재생횟수가 많은 순으로 정렬된 (장르, 카운트) 를 순회
    for el in sorted_genre_cnt:
        search_genre, _ = el
        temp_list = []
        # 재생횟수가 많은 순으로 정렬된 리스트를 순회
        for song in sorted_songs:
            genre, _, index = song
            # 찾고자하는 장르와 순회하고 있는 장르가 일치하고 장르별 리스트는 총 2개까지
            if search_genre == genre and len(temp_list) < 2:
                temp_list.append(index)
        answer += temp_list
    return answer


# 장르 별로 가장 많이 재생된 노래 두 개씩
# 노래는 고유 번호로 구분
# 수록 기준
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서 고유 번호가 낮은 노래를 먼저 수록

# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 리턴