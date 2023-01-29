from datetime import datetime
from enum import Enum
from unittest import TestCase

from freezegun import freeze_time
from user_management import Admin, Post, Redactor, User


class Genders(Enum):
    FEMALE = "F"
    MALE = "M"


class TestUserManagementUser(TestCase):
    def setUp(self):
        self.test_user1 = User(
            "TestName1",
            "TestSurname1",
            "testuser1@gmail.com",
            Genders.MALE,
            "13-12-1990",
        )

    def tearDown(self):
        Post.post_list = []

    def test_author_attribute(self):
        """Test if attribute "author" is created correctly while initializing
        User instance.
        """

        self.assertEqual(self.test_user1.author, "TestName1 TestSurname1")

    def test_update_email(self):
        """Test if User.update_email() method works correctly."""

        random_user = User(
            "RandomUserName",
            "RandomUserSurname",
            "randuser@gmail.com",
            Genders.MALE,
            "15-12-1990",
        )
        random_user.update_email("newrand@gmail.com")
        self.assertEqual(random_user.email, "newrand@gmail.com")

    def test_create_post(self):
        """Test if User.create_post() method works correctly."""

        with freeze_time("2022-12-12 12:00:00"):
            user_post1 = self.test_user1.create_post("User title 1", "User content 11")
            self.assertEqual(user_post1.title, "User title 1")
            self.assertEqual(user_post1.content, "User content 11")
            self.assertEqual(user_post1.creation_date, datetime(2022, 12, 12, 12, 0, 0))

    def test_modify_post(self):
        """Test if User.modify_post() method works correctly when user is
        trying to modify its own post.
        """

        with freeze_time("2022-12-12 12:00:00"):
            user_post1 = self.test_user1.create_post("User title 1", "User content 11")
            self.test_user1.modify_post(user_post1, "New title", "New content")
            self.assertEqual(user_post1.title, "New title")
            self.assertEqual(user_post1.content, "New content")
            self.assertEqual(
                user_post1.modification_date, datetime(2022, 12, 12, 12, 0, 0)
            )
            self.assertEqual(
                user_post1.last_modification_author, self.test_user1.author
            )

    def test_delete_post(self):
        """Test if User.delete_post() method works correctly when user is
        trying to delete its own post.
        """

        user_post1 = self.test_user1.create_post("User title 1", "User content 11")
        user_post2 = self.test_user1.create_post("User title 2", "User content 222")
        self.test_user1.delete_post(user_post1)
        post_list = [user_post2]
        self.assertEqual(Post.post_list, post_list)
