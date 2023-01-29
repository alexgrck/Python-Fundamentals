from abc import ABC, abstractmethod


class Convert(ABC):

    base_unit = ""

    def __init__(self, input_):
        self.input_ = input_

    @abstractmethod
    def convert(self, multiplier=None, to_add=None):
        """Return input for converting a unit."""
        return round(self.input_ * multiplier + to_add, 2)

    @abstractmethod
    def to_si(self):
        raise NotImplementedError("Method was not implemented.")

    def __eq__(self, other):
        if self.base_unit == other.base_unit:
            return self.to_si() == other.to_si()
        raise TypeError(
            f"You may not compare {self.__class__.__name__} with {other.__class__.__name__}."
        )

    def __lt__(self, other):
        if self.base_unit == other.base_unit:
            return self.to_si() < other.to_si()
        raise TypeError(
            f"You may not compare {self.__class__.__name__} with {other.__class__.__name__}."
        )


class Fahrenheit(Convert):

    base_unit = "K"

    def convert(self):
        """Return Celsius value converted from Fahrenheit."""
        return super().convert(multiplier=(5 / 9), to_add=(-160 / 9))

    def to_si(self):
        """Return Kelvin value converted from Fahrenheit."""
        return round(self.convert() + 273.15, 2)


class Celsius(Convert):

    base_unit = "K"

    def convert(self):
        """Return Fahrenheit value converted from Celsius."""
        return super().convert(multiplier=(9 / 5), to_add=32)

    def to_si(self):
        """Return Kelvin value converted from Celsius."""
        return super().convert(to_add=273.15)


class Inch(Convert):

    base_unit = "m"

    def convert(self):
        """Return centimeters value converted from inches."""
        return super().convert(multiplier=2.54)

    def to_si(self):
        """Return metre value converted from inches."""
        return round(self.convert() / 100, 2)


class Centimeter(Convert):

    base_unit = "m"

    def convert(self):
        """Return inches value converted from centimeters."""
        return super().convert(multiplier=(1 / 2.54))

    def to_si(self):
        """Return metre value converted from centimeters."""
        return super().convert(multiplier=(1 / 100))


class Mile(Convert):

    base_unit = "m"

    def convert(self):
        """Return kilometers value converted from miles."""
        return super().convert(multiplier=1.609344)

    def to_si(self):
        """Return metre value converted from miles."""
        return round(self.convert() * 1000, 2)


class Kilometer(Convert):

    base_unit = "m"

    def convert(self):
        """Return miles value converted from kilometers."""
        return super().convert(multiplier=(1 / 1.609344))

    def to_si(self):
        """Return metre value converted from kilometers."""
        return super().convert(multiplier=1000)


class GallonImp(Convert):

    base_unit = "m^3"

    def convert(self):
        """Return liters value converted from imperial gallons."""
        return super().convert(multiplier=4.54609)

    def to_si(self):
        """Return cube meters value converted from imperial gallons."""
        return round(self.convert() / 1000, 2)


class Liter(Convert):

    base_unit = "m^3"

    def convert(self):
        """Return imperial gallons value converted from liters."""
        return super().convert(multiplier=(1 / 4.54609))

    def to_si(self):
        """Return cube meters value converted from liters."""
        return super().convert(multiplier=(1 / 1000))
