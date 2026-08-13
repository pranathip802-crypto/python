class Movie:
    def __init__(self, name, hero, heroine, rating):
        self.name = name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating


movie1 = Movie("Movie A", "Actor A", "Actress A", 8.5)
movie2 = Movie("Movie B", "Actor B", "Actress B", 7.8)

print(movie1.name, movie1.hero, movie1.heroine, movie1.rating)
print(movie2.name, movie2.hero, movie2.heroine, movie2.rating)