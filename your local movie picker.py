#I always struggled which movie which I'll watch at night.
#Here's the simpliest solution. Let the automation decide for you.

import random as rd
acilis_mesaji= "selam. aşağıya filmleri yazıyosun ben de seçiyorum."
print(acilis_mesaji)
num_of_mov = int(input("kaç film seçeneği var?: "))
list_of_movies = []
for a in range(num_of_mov):
    film_ismi = input("filmin ismi: ")
    list_of_movies.append(film_ismi)
the_one = rd.choice(list_of_movies)
print(f"bugünün filmi: {the_one}\nmısırın bol olsun")

