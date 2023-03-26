SMALL_BAR_SIZE = "small bar"
HUGE_BAR_SIZE = "huge bar"
BEER_VOLUME_UNIT = 500


class Bar:
    def __init__(self, name: str, size: str):
        self.name = name
        self.size = size


class MalankaBar(Bar):
    def __init__(self):
        super().__init__(name=self.__class__.__name__, size=SMALL_BAR_SIZE)


class SpinBar(Bar):
    def __init__(self):
        super().__init__(name=self.__class__.__name__, size=HUGE_BAR_SIZE)


class BeerDelivery:
    def __init__(self, customer: Bar):
        self.customer = customer

    def get_beer_volume(self):
        return BEER_VOLUME_UNIT


class SmallBeerDelivery(BeerDelivery):
    pass


class MediumBeerDelivery(BeerDelivery):
    def get_beer_volume(self):
        return super().get_beer_volume() * 2


class HugeBeerDelivery(MediumBeerDelivery):
    def get_beer_volume(self):
        return super().get_beer_volume() * 2


# It is correct code because BeerDelivery is open to extension by its subclasses
# and there is no need to modify BeerDelivery class to adjust it towards new type of customers