from datetime import datetime
from enum import Enum
from unittest import TestCase

from freezegun import freeze_time
from user_management import Post, Redactor


class Genders(Enum):
    FEMALE = "F"
    MALE = "M"


class TestUMRedactor(TestCase):
    def setUp(self):
        self.test_red1 = Redactor(
            "TestNameRed1",
            "TestSurnameRed1",
            "testred1@gmail.com",
            Genders.MALE,
            "17-02-1965",
        )

    def tearDown(self):
        Post.post_list = []

    def test_author_attribute(self):
        """Test if attribute "author" is created correctly while initializing
        Redactor instance.
        """

        self.assertEqual(self.test_red1.author, "TestNameRed1 TestSurnameRed1")

    def test_update_email(self):
        """Test if Redactor.update_email() method works correctly."""

        random_red = Redactor(
            "RandomRedName",
            "RandomRedSurname",
            "randred@gmail.com",
            Genders.MALE,
            "15-12-1990",
        )
        random_red.update_email("randnewred@gmail.com")
        self.assertEqual(random_red.email, "randnewred@gmail.com")

    def test_create_post(self):
        """Test if Redactor.create_post() method works correctly."""

        with freeze_time("2022-12-12 12:00:00"):
            red_post1 = self.test_red1.create_post("Red title 2", "Red content 22")
            self.assertEqual(red_post1.title, "Red title 2")
            self.assertEqual(red_post1.content, "Red content 22")
            self.assertEqual(red_post1.creation_date, datetime(2022, 12, 12, 12, 0, 0))

    def test_modify_post(self):
        """Test if Redactor.modify_post() method works correctly when redactor
        is trying to modify its own post.
        """

        with freeze_time("2022-12-12 12:00:00"):
            red_post1 = self.test_red1.create_post("Red title 2", "Red content 22")
            self.test_red1.modify_post(
                red_post1, "Red new title 2", "Red new content 2"
            )
            self.assertEqual(red_post1.title, "Red new title 2")
            self.assertEqual(red_post1.content, "Red new content 2")
            self.assertEqual(
                red_post1.modification_date, datetime(2022, 12, 12, 12, 0, 0)
            )
            self.assertEqual(red_post1.last_modification_author, self.test_red1.author)

    def test_delete_post(self):
        """Test if Redactor.delete_post() method works correctly when redactor
        is trying to delete its own or other redactor's post
        """

        red1_post1 = self.test_red1.create_post(
            "Red1 post1 title", "Red1 post1 content"
        )
        red1_post2 = self.test_red1.create_post(
            "Red1 post2 title", "Red1 post2 content"
        )
        self.test_red1.delete_post(red1_post1, self.test_red1)
        post_list = [red1_post2]
        self.assertEqual(Post.post_list, post_list)
