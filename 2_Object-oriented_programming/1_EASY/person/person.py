from unidecode import unidecode


class Person:
    def __init__(
        self,
        first_name,
        surname,
        second_name="",
        address="",
        email="",
        acquaintances=None,
    ):
        self.first_name = first_name
        self.surname = surname
        self.second_name = second_name
        self.email = email or unidecode(first_name + surname).lower() + "@gmail.com"
        self.address = address
        self.acquaintances = [] if acquaintances is None else acquaintances

    def __eq__(self, other):
        if self.first_name == other.first_name and self.surname == other.surname:
            return True
        return False

    def add_acquaintance(self, acquaintance):
        self.acquaintances.append(acquaintance)
        return self.acquaintances

    def del_acquaintance(self, acquaintance):
        if acquaintance in self.acquaintances:
            self.acquaintances.remove(acquaintance)
        return self.acquaintances
