class Beer:
    def __init__(self, beer_kind: str):
        self.beer_kind = beer_kind

    def get_beer_kind(self):
        return self.beer_kind

class BeerStorage:
    def get_beer(self, beer_id: int):
        pass

    def put_beer(self, beer: Beer):
        pass

# Beer can be used separately from its Storage,
# so possible changes in Storage will not affect parts of project that use Beer properties only