# Let's make BrewingProcess interface to follow principle


class BrewingProcess:
    def brew(self, beer_kind: str, volume: int):
        raise NotImplemented


# The BrewingProcess interface has a brew method. Now we can pass an argument of type BrewingProcess to Brewery class:


class Brewery:
    def __init__(self, brewing_process: BrewingProcess):
        self.brewing_process = brewing_process

    def get_IPA(self, volume: int):
        self.brewing_process.brew(beer_kind="IPA", volume=volume)

    def get_APA(self, volume: int):
        self.brewing_process.brew(beer_kind="APA", volume=volume)


# Now it does not matter what the type of BrewingProcess passed to Brewery, it is capable to brew a beer
# without bothering to know the type of required process


class CraftyBrewingProcess(BrewingProcess):
    def brew(self, beer_kind: str, volume: int):
        return f"{beer_kind} + crafty stuff" * volume


class HomeBrewingProcess(BrewingProcess):
    def brew(self, beer_kind: str, volume: int):
        return f"{beer_kind} + homemade stuff" * volume

# We can create many BrewingProcess types and pass it to Brewery class, and it will work perfectly

# Now both high-level modules and low-level modules depend on abstractions.
# Brewery class (high level module) depends on the BrewingProcess interface(abstraction) and
# the BrewingProcess kinds (low level modules) are depend on the BrewingProcess interface(abstraction)
# Also it forces us to follow LSP principle.