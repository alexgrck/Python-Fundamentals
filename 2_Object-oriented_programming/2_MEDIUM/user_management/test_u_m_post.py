from datetime import datetime
from enum import Enum
from unittest import TestCase

from freezegun import freeze_time
from user_management import Post, User, Redactor, Admin


class Genders(Enum):
    FEMALE = "F"
    MALE = "M"


class TestUMPost(TestCase):
    def setUp(self):
        self.test_user1 = User(
            "TestName1",
            "TestSurname1",
            "testuser1@gmail.com",
            Genders.MALE,
            "13-12-1990",
        )
        self.test_red1 = Redactor(
            "TestNameRed1",
            "TestSurnameRed1",
            "testred1@gmail.com",
            Genders.MALE,
            "17-02-1965",
        )
        self.test_admin1 = Admin(
            "TestNameAd1",
            "TestSurnameAd1",
            "testad1@gmail.com",
            Genders.MALE,
            "20-02-1999",
        )

    def tearDown(self):
        Post.post_list = []

    def test_post_list(self):
        """Test if created posts are correctly added to Post.post_list."""

        user_post1 = self.test_user1.create_post("User title 1", "User content 11")
        red_post1 = self.test_red1.create_post("Red title 1", "Red content 11")
        admin_post1 = self.test_admin1.create_post("Ad title 1", "Ad content 11")
        post_list = [user_post1, red_post1, admin_post1]
        self.assertEqual(Post.post_list, post_list)

    def test_modify_post(self):
        """Test if Post.modify_post() method works correctly."""

        with freeze_time("2022-12-12 12:00:00"):
            user_post1 = self.test_user1.create_post("User title 1", "User content 11")
            user_post1.modify_post("New title", "New content")
            self.assertEqual(user_post1.title, "New title")
            self.assertEqual(user_post1.content, "New content")
            self.assertEqual(
                user_post1.modification_date, datetime(2022, 12, 12, 12, 0, 0)
            )

    def test_content_size(self):
        """Test if instances of Post can be compared between each other basing
        on their lenghts of content.
        """

        user_post1 = self.test_user1.create_post("User title 1", "User content 11")
        red_post1 = self.test_red1.create_post("Red title 1", "Red content 11")
        admin_post1 = self.test_admin1.create_post("Ad title 1", "Ad content 11")
        self.assertGreater(user_post1.content, red_post1.content)
        self.assertLess(admin_post1.content, red_post1.content)
