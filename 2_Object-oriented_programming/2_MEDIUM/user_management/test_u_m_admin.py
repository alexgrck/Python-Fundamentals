from datetime import datetime
from enum import Enum
from unittest import TestCase

from freezegun import freeze_time
from user_management import Admin, Post


class Genders(Enum):
    FEMALE = "F"
    MALE = "M"


class TestUMAdmin(TestCase):
    def setUp(self):
        self.test_admin1 = Admin(
            "TestNameAd2",
            "TestSurnameAd2",
            "testad2@gmail.com",
            Genders.FEMALE,
            "30-11-1985",
        )

    def tearDown(self):
        Post.post_list = []

    def test_author_attribute(self):
        """Test if attribute "author" is created correctly while initializing
        Admin instance.
        """

        self.assertEqual(self.test_admin1.author, "TestNameAd2 TestSurnameAd2")

    def test_create_post(self):
        """Test if Admin.create_post() method works correctly."""

        with freeze_time("2022-12-12 12:00:00"):
            admin_post1 = self.test_admin1.create_post(
                "Admin title 2", "Admin content 22"
            )
            self.assertEqual(admin_post1.title, "Admin title 2")
            self.assertEqual(admin_post1.content, "Admin content 22")
            self.assertEqual(
                admin_post1.creation_date, datetime(2022, 12, 12, 12, 0, 0)
            )

    def test_modify_post(self):
        """Test if Admin.modify_post() method works correctly when admin is
        trying to modify its own post.
        """

        with freeze_time("2022-12-12 12:00:00"):
            admin_post1 = self.test_admin1.create_post(
                "Admin title 2", "Admin content 22"
            )
            self.test_admin1.modify_post(
                admin_post1, "Admin new title 2", "Admin new content 2"
            )
            self.assertEqual(admin_post1.title, "Admin new title 2")
            self.assertEqual(admin_post1.content, "Admin new content 2")
            self.assertEqual(
                admin_post1.modification_date, datetime(2022, 12, 12, 12, 0, 0)
            )
            self.assertEqual(
                admin_post1.last_modification_author, self.test_admin1.author
            )

    def test_delete_post(self):
        """Test if Admin.delete_post() works correctly when deleting its own
        post.
        """

        admin1_post1 = self.test_admin1.create_post(
            "Admin1 title 1", "Admin1 content 11"
        )
        admin1_post2 = self.test_admin1.create_post(
            "Admin1 title 2", "Admin1 content 22"
        )
        self.test_admin1.delete_post(admin1_post1)
        post_list = [admin1_post2]
        self.assertEqual(Post.post_list, post_list)
