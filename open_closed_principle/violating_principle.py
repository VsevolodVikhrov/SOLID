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
        if self.customer.size == SMALL_BAR_SIZE:
            return BEER_VOLUME_UNIT
        elif self.customer.size == HUGE_BAR_SIZE:
            return BEER_VOLUME_UNIT * 4


# It violates principle because if we want to introduce new bar size in future we will have to add another
# "if-else" statement to get_beer_volume method. So it is modification but not extension