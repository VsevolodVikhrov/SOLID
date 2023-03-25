class Beer:
    def __init__(self, brewery: str):
        self.brewery = brewery

    def get_brewery(self):
        return self.brewery


class IPA(Beer):
    def get_ipa_brewery(self):
        return self.brewery


class APA(Beer):
    def get_apa_brewery(self):
        return self.brewery


class Lager(Beer):
    def get_lager_brewery(self):
        return self.brewery


def print_breweries(beers: list):
    for beer in beers:
        if isinstance(beer, IPA):
            print(beer.get_ipa_brewery())
        elif isinstance(beer, APA):
            print(beer.get_apa_brewery())
        elif isinstance(beer, Lager):
           print(beer.get_lager_brewery())


beers_registry = [IPA("IPA_BREWERY"), APA("APA_BREWERY"), Lager("LAGER_BREWERY")]

print_breweries(beers_registry)

# Violating principle because Beer cannot be replaced by any of its subclasses
# without breaking a code or implementing case-specific handlers