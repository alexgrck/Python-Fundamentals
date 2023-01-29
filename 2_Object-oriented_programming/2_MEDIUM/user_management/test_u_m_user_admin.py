from datetime import datetime
from enum import Enum
from unittest import TestCase
from freezegun import freeze_time
from user_management import Admin, Post, User


class Genders(Enum):
    FEMALE = "F"
    MALE = "M"


class TestUMtUserAdminInteraction(TestCase):
    def setUp(self):
        self.test_user1 = User(
            "TestName1",
            "TestSurname1",
            "testuser1@gmail.com",
            Genders.MALE,
            "13-12-1990",
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

    def test_user_modify_admin_post(self):
        """Test if TypeError is raised when user is trying to modify admin's
        post.
        """

        admin_post1 = self.test_admin1.create_post("Admin title 1", "Admin content 1")
        with self.assertRaises(TypeError):
            self.test_user1.modify_post(admin_post1)

    def test_user_delete_admin_post(self):
        """Test if TypeError is raised when user is trying to delete redactor's
        post.
        """

        admin_post1 = self.test_admin1.create_post("Admin title 1", "Admin content 1")
        with self.assertRaises(TypeError):
            self.test_user1.delete_post(admin_post1)

    def test_admin_edit_user_attributes(self):
        """Test if Admin.edit_attribute() method works correctly while editing
        user's attributes."""

        random_user = User(
            "RandUsername",
            "RandUsersurname",
            "randomuser@gmail.com",
            Genders.FEMALE,
            "18-06-2002",
        )
        self.test_admin1.edit_attribute(
            random_user,
            {"surname": "NewUsersurname", "email": "newuseremail@gmail.com"},
        )
        self.assertEqual(random_user.surname, "NewUsersurname")
        self.assertEqual(random_user.email, "newuseremail@gmail.com")
        self.assertEqual(random_user.author, "RandUsername NewUsersurname")

    def test_admin_modify_user_post(self):
        """Test if Admin.modify_post() method works correctly when admin is
        trying to modify user's post.
        """

        with freeze_time("2022-12-12 12:00:00"):
            user_post1 = self.test_user1.create_post("User title 1", "User content 11")
            self.test_admin1.modify_post(
                user_post1, "Admin new title 2", "Admin new content 2"
            )
            self.assertEqual(user_post1.title, "Admin new title 2")
            self.assertEqual(user_post1.content, "Admin new content 2")
            self.assertEqual(
                user_post1.modification_date, datetime(2022, 12, 12, 12, 0, 0)
            )
            self.assertEqual(
                user_post1.last_modification_author, self.test_admin1.author
            )

    def test_admin_delete_user_post(self):
        """Test if Admin.delete_post() works correctly when deleting user's
        post.
        """

        user1_post1 = self.test_user1.create_post("User1 title 1", "User1 content 11")
        user1_post2 = self.test_user1.create_post("User1 title 2", "User1 content 22")
        self.test_admin1.delete_post(user1_post1)
        post_list = [user1_post2]
        self.assertEqual(Post.post_list, post_list)
