import unittest
from person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person1 = Person(
            "Stanley", "Hudson", "", "Baker Street 20", "stanhud@yahoo.com"
        )
        self.person2 = Person(
            "Chandler",
            "Bing",
            "Muriel",
            "Grove Street 27",
            acquaintances=[Person("Joey", "Tribbiani"), Person("Ross", "Geller")],
        )

    def test_dunder_eq(self):
        """Tests if overriden dunder method '__eq__' returns correct value."""
        self.assertTrue(Person("Joey", "Tribbiani") in self.person2.acquaintances)
        self.assertFalse(Person("Rachel", "Green") in self.person2.acquaintances)

    def test_email_creating(self):
        """Tests if e-mail is created correctly if not given when instantiating object."""
        self.assertEqual(self.person2.email, "chandlerbing@gmail.com")

    def test_add_acquaintance_person1(self):
        """Tests if adding acquaintance to 'person1' object works correctly."""
        self.person1.add_acquaintance(Person("Michael", "Scott"))
        self.assertTrue(Person("Michael", "Scott") in self.person1.acquaintances)
        self.person1.add_acquaintance(Person("Dwight", "Schrute"))
        self.assertTrue(Person("Dwight", "Schrute") in self.person1.acquaintances)

    def test_add_acquaintance_person2(self):
        """Tests if adding acquaintance to 'person2' object works correctly."""
        self.person2.add_acquaintance(Person("Monica", "Geller"))
        self.assertTrue(Person("Monica", "Geller") in self.person2.acquaintances)

    def test_del_acquaintance_person1(self):
        """Tests if deleting acquaintance in 'person1' object works correctly."""
        self.person1.add_acquaintance(Person("Michael", "Scott"))
        self.person1.add_acquaintance(Person("Dwight", "Schrute"))
        self.person1.del_acquaintance(Person("Michael", "Scott"))
        self.assertFalse(Person("Michael", "Scott") in self.person1.acquaintances)
        self.assertTrue(Person("Dwight", "Schrute") in self.person1.acquaintances)

    def test_del_acquaintance_person2(self):
        """Tests if deleting acquaintance in 'person2' object works correctly."""
        self.person2.add_acquaintance(Person("Monica", "Geller"))
        self.person2.del_acquaintance(Person("Joey", "Tribbiani"))
        self.assertFalse(Person("Joey", "Tribbiani") in self.person2.acquaintances)
        self.assertTrue(Person("Ross", "Geller") in self.person2.acquaintances)
        self.assertTrue(Person("Monica", "Geller") in self.person2.acquaintances)
