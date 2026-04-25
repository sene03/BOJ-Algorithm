from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    genres_count = defaultdict(int)
    genres_song = defaultdict(list)
    
    for s, (g, p) in enumerate(zip(genres, plays)):
        genres_count[g] += p
        genres_song[g].append((s, p))

    genres_count = dict(sorted(
        genres_count.items(), 
        key=lambda x: x[1], 
        reverse=True))
    
    for genre, _ in genres_count.items():
        songs = genres_song[genre]

        songs.sort(key=lambda x: (-x[1], x[0])) # 재생수 내림차순, 고유번호 오름차순
        
        # append top 2 to the answer list
        for s in songs[:2]:
            answer.append(s[0])
            
    return answer