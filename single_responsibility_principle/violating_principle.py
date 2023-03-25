class Beer:
    def __init__(self, beer_kind: str):
        self.beer_kind = beer_kind

    def get_beer_kind(self):
        return self.beer_kind

    def put_beer(self, beer):
        pass


# Violating principle because there is a method for storage management and method for beer properties management