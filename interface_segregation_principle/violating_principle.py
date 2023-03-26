class Brewery:
    def brew_IPA(self):
        raise NotImplemented

    def brew_APA(self):
        raise NotImplemented

    def brew_lager(self):
        raise NotImplemented


class IPABrewery(Brewery):
    def brew_IPA(self):
        return "IPA"

    def brew_APA(self):
        pass

    def brew_lager(self):
        pass


class APABrewery(Brewery):
    def brew_IPA(self):
        pass

    def brew_APA(self):
        return "APA"

    def brew_lager(self):
        pass


class LagerBrewery(Brewery):
    def brew_IPA(self):
        pass

    def brew_APA(self):
        pass

    def brew_lager(self):
        return "Lager"


# Class Brewery violates principle because any of it subclasses must implement all methods to avoid exceptions, however
# in most cases subclass must be able to brew one kind of beer only. If we decide to implement new method
# to Brewery class then all of its subclasses must implement it as well