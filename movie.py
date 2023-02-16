def user_input():
    print(""" 
     _     _     _____   _      _   _______   _______  _      _   _______   ______     _______    ________
     | \  / |   /     \   \    /       |      |         \    /    |         |_____|    |         |
     |  \/  |  |       |   \  /        |      |----      \  /     |----     |    \      -----    |-----
     |      |   \_____/     \/      ___|___   |______     \/      |______   |     \    ______|   |________
                                     
    """)
    movie_rating = int(input('Enter rating of the movie: '))
    movie_genre = input('Enter genre of the movie: ')

    movie_details = {'rating': movie_rating, 'genre': movie_genre}
    return movie_details


def check_eligibility(movie_rating, movie_genre):
    if movie_rating >= 8 and movie_genre == 'action':
        print('Great')
    else:
        print('Sorry! Not intrested')


userLikes = user_input()

check_eligibility(userLikes['rating'], userLikes['genre'])
