class Brewery:
    def brew(self):
        raise NotImplemented


class IPABrewery(Brewery):
    def brew(self):
        return "IPA"


class APABrewery(Brewery):
    def brew(self):
        return "APA"


class LagerBrewery(Brewery):
    def brew(self):
        return "Lager"


# It is correct implementation because now any brewery capable of brewing one kind of beer only. We can use these
# certain breweries for building new beer specifics:

class StrongIPABrewery(IPABrewery):
    def brew(self):
        return f"Strong {super().brew()}"