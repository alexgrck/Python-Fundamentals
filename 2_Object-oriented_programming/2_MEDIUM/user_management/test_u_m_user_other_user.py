# User	modify_other_user_post
# User	delete_other_user_post

from enum import Enum
from unittest import TestCase
from user_management import Post, User


class Genders(Enum):
    FEMALE = "F"
    MALE = "M"


class TestUMUserInteraction(TestCase):
    def setUp(self):
        self.test_user1 = User(
            "TestName1",
            "TestSurname1",
            "testuser1@gmail.com",
            Genders.MALE,
            "13-12-1990",
        )
        self.test_user2 = User(
            "TestName2",
            "TestSurname2",
            "testuser2@gmail.com",
            Genders.FEMALE,
            "15-10-1995",
        )

    def tearDown(self):
        Post.post_list = []

    def test_user_modify_other_user_post(self):
        """Test if TypeError is raised when user is trying to modify other
        user's post.
        """

        user_post1 = self.test_user2.create_post("User title 1", "User content 11")
        with self.assertRaises(TypeError):
            self.test_user1.modify_post(user_post1)

    def test_user_delete_other_user_post(self):
        """Test if TypeError is raised when user is trying to delete other
        user's post.
        """

        user_post1 = self.test_user2.create_post("User title 1", "User content 11")
        with self.assertRaises(TypeError):
            self.test_user1.delete_post(user_post1)
