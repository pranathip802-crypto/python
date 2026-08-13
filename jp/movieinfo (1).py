class Movie:
    def __init__(self, name, hero, heroine, rating):
        self.name = name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating

    def display(self):
        print("Movie:", self.name)
        print("Hero:", self.hero)
        print("Heroine:", self.heroine)
        print("Rating:", self.rating)


movie = Movie("Movie A", "Actor A", "Actress A", 8.5)

movie.display()