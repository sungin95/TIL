import json
from pprint import pprint

# 해야 할것. 무비를 리스트로 만들다. 
# 리스트를 하나하나 result에 적용하고 result를 리스트에 넣는다. 
# 끝

def movie_info(movies, genres):
    result_list = []
    for movie in movies:
        genre_names = []
        n = len(genres)
        for i in range(n):
            if genres[i].get('id') in movie.get('genre_ids'):
                genre_names.append(genres[i].get('name'))
        result = {
            'genre_names' : genre_names,
            'id' : movie.get('id'),
            'overview' : movie.get('overview'),
            'title' : movie.get('title'),
            'vote_average' : movie.get('vote_average'),
        }
        result_list.append(result)
    return result_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))