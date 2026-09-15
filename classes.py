class Media:
    def __init__(self, title, creator, year):
        self.title = title
        self.creator = creator
        self.year = year

class Music(Media):
    def __init__(self, title, creator, year, tracks):
        super().__init__(title, creator, year)
        self.tracks = tracks

    def show_info_music(self):
        return f"Titel: {self.title}, Artist: {self.creator}, År: {self.year}, Låtar: {self.tracks}"

class Movie(Media):
    def __init__(self, title, creator, year, length):
        super().__init__(title, creator, year)
        self.length = length

    def show_info_movie(self):
        return f"Titel: {self.title}, Regissör: {self.creator}, År: {self.year}, Längd: {self.length} min"

class Book(Media):
    def __init__(self, title, creator, year, pages):
        super().__init__(title, creator, year)
        self.pages = pages

    def show_info_book(self):
        return f"\nTitel: {self.title}, Författare: {self.creator}, År: {self.year}, Sidor: {self.pages}"



        