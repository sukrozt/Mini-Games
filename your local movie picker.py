import random as rd
acilis_mesaji= "selam. aşağıya filmleri yazıyosun ben de seçiyorum."
print(acilis_mesaji)
num_of_mov = int(input("kaç film seçeneği var?: "))
list_of_movies = []
for a in range(num_of_mov):
    film_ismi = input("filmin ismi: ")
    list_of_movies.append(film_ismi)
the_one = rd.choice(list_of_movies)
print("bugünün filmi:", the_one)
print("mısırın bol olsun")
