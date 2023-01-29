from datetime import datetime
from enum import Enum
from unittest import TestCase

from freezegun import freeze_time
from user_management import Post, Redactor, User


class Genders(Enum):
    FEMALE = "F"
    MALE = "M"


class TestUMUserRedactorInteraction(TestCase):
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

    def tearDown(self):
        Post.post_list = []

    def test_user_modify_redactor_post(self):
        """Test if TypeError is raised when user is trying to modify redactor's
        post.
        """

        red_post1 = self.test_red1.create_post("Red title 1", "Red content 11")
        with self.assertRaises(TypeError):
            self.test_user1.modify_post(red_post1)

    def test_user_delete_redactor_post(self):
        """Test if TypeError is raised when user is trying to delete redactor's
        post.
        """

        red_post1 = self.test_red1.create_post("Red title 1", "Red content 11")
        with self.assertRaises(TypeError):
            self.test_user1.delete_post(red_post1)

    def test_redactor_modify_user_post(self):
        """Test if Redactor.modify_post() method works correctly when redactor
        is trying to modify user's post.
        """

        with freeze_time("2022-12-12 12:00:00"):
            user_post1 = self.test_user1.create_post("User title 1", "User content 11")
            self.test_red1.modify_post(
                user_post1, "Red2 new title for user", "Red2 new content for user"
            )
            self.assertEqual(user_post1.title, "Red2 new title for user")
            self.assertEqual(user_post1.content, "Red2 new content for user")
            self.assertEqual(
                user_post1.modification_date, datetime(2022, 12, 12, 12, 0, 0)
            )
            self.assertEqual(user_post1.last_modification_author, self.test_red1.author)

    def test_redactor_delete_user_post(self):
        """Test if Redactor.delete_post() method works correctly when redactor
        is trying to delete user's post.
        """

        user_post1 = self.test_user1.create_post("User title 1", "User content 11")
        user_post2 = self.test_user1.create_post("User title 2", "User content 222")
        self.test_red1.delete_post(user_post1, self.test_user1)
        post_list = [user_post2]
        self.assertEqual(Post.post_list, post_list)
