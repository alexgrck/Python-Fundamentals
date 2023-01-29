import unittest
from email_builder import EmailBuilder


class TestEmailBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = EmailBuilder()

    def test_update_from(self):
        """Test method update_from() of EmailBuilder class."""
        self.builder.update_from("johndoe@gmail.com")
        self.assertEqual(self.builder.email.from_, "johndoe@gmail.com")

    def test_update_to(self):
        """Test method update_to() of EmailBuilder class."""
        self.builder.update_to("janedope@gmail.com")
        self.assertEqual(self.builder.email.to_, "janedope@gmail.com")

    def test_update_title(self):
        """Test method update_title() of EmailBuilder class."""
        self.builder.update_title("Some title")
        self.assertEqual(self.builder.email.title, "Some title")

    def test_update_content(self):
        """Test method update_content() of EmailBuilder class."""
        self.builder.update_content("Some content")
        self.assertEqual(self.builder.email.content, "Some content")

    def test_update_cc(self):
        """Test method update_cc() of EmailBuilder class."""
        self.builder.update_cc(["alice123@gmail.com"])
        self.assertEqual(self.builder.email.cc, ["alice123@gmail.com"])

    def test_update_bcc(self):
        """Test method update_bcc() of EmailBuilder class."""
        self.builder.update_bcc(["bob456@gmail.com"])
        self.assertEqual(self.builder.email.bcc, ["bob456@gmail.com"])

    def test_update_html(self):
        """Test method update_html() of EmailBuilder class."""
        self.builder.update_html("https://google.com")
        self.assertEqual(self.builder.email.html, "https://google.com")

    def test_chaining_methods(self):
        """Test chaining all methods contained in EmailBuilder class."""
        self.builder.update_from("johndoe@gmail.com").update_to(
            "janedope@gmail.com"
        ).update_title("Some title").update_content("Some content").update_cc(
            ["alice123@gmail.com"]
        ).update_bcc(
            ["bob456@gmail.com"]
        ).update_html(
            "https://google.com"
        )
        self.assertEqual(self.builder.email.from_, "johndoe@gmail.com")
        self.assertEqual(self.builder.email.to_, "janedope@gmail.com")
        self.assertEqual(self.builder.email.title, "Some title")
        self.assertEqual(self.builder.email.content, "Some content")
        self.assertEqual(self.builder.email.cc, ["alice123@gmail.com"])
        self.assertEqual(self.builder.email.bcc, ["bob456@gmail.com"])
        self.assertEqual(self.builder.email.html, "https://google.com")

    def test_plain_strings_to_cc_bcc(self):
        """Test whether TypeError is raised if e-mails addresses input by
        update_cc() or update_bcc() methods are not aggregated in the list
        (does not concern inputting single e-mail address - in such case
        TypeError is not raised).
        """
        for x in range(2):
            with self.assertRaises(TypeError):
                self.builder.update_cc("alice123@gmail.com", "bob456@gmail.com")
                self.builder.update_bcc("alice456@gmail.com", "bob789@gmail.com")
