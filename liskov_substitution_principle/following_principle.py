class Beer:
    def __init__(self, brewery: str):
        self.brewery = brewery

    def get_brewery(self):
        return self.brewery


class IPA(Beer):
    def get_brewery(self):
        return self.brewery


class APA(Beer):
    def get_brewery(self):
        return self.brewery


class Lager(Beer):
    def get_brewery(self):
        return self.brewery


def print_breweries(beers: list):
    for beer in beers:
        print(beer.get_brewery())


beers_registry = [IPA("IPA_BREWERY"), APA("APA_BREWERY"), Lager("LAGER_BREWERY")]

print_breweries(beers_registry)

# Beer and any of its subclasses may replace each other because they have same interfaces