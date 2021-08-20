from collections import defaultdict
from operator import itemgetter

def solution(genres, plays):
    answer = []
    play_count_by_genre = defaultdict(int)
    songs_in_genre = defaultdict(list)

    for i,(g, p) in enumerate(zip(genres, plays)):
        play_count_by_genre[g] += p
        songs_in_genre[g].append((-p, i))

    genre_rank = [genre for genre, play in sorted(play_count_by_genre.items(), key=itemgetter(1), reverse=True)]

    for genre in genre_rank:
        # print(genre)
        # print(sorted(songs_in_genre[genre])[:2])
        answer.extend([ song_id for minus_play, song_id in sorted(songs_in_genre[genre])[:2]])

    return answer