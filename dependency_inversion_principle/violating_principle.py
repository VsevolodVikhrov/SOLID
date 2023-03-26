class CraftyBrewingProcess:
    def brew(self, beer_kind: str, volume: int):
        return f"{beer_kind} + crafty stuff" * volume


class Brewery:
    def __init__(self, crafty_brewing_process: CraftyBrewingProcess):
        self.crafty_brewing_process = crafty_brewing_process

    def get_IPA(self, volume: int):
        self.crafty_brewing_process.brew(beer_kind="IPA", volume=volume)

    def get_APA(self, volume: int):
        self.crafty_brewing_process.brew(beer_kind="APA", volume=volume)


# Brewery is the high-level component and CraftyBrewingProcess is the low-level component.
# It violates the principle because high-level modules should not depend on low-level level modules,
# it should depend upon its abstraction
