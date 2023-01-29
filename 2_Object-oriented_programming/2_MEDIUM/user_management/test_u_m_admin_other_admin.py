from datetime import datetime
from enum import Enum
from unittest import TestCase

from freezegun import freeze_time
from user_management import Admin, Post


class Genders(Enum):
    FEMALE = "F"
    MALE = "M"


class TestUMAdminInteraction(TestCase):
    def setUp(self):
        self.test_admin1 = Admin(
            "TestNameAd2",
            "TestSurnameAd2",
            "testad2@gmail.com",
            Genders.FEMALE,
            "30-11-1985",
        )
        self.test_admin2 = Admin(
            "TestNameAd1",
            "TestSurnameAd1",
            "testad1@gmail.com",
            Genders.MALE,
            "20-02-1999",
        )

    def tearDown(self):
        Post.post_list = []

    def test_admin_edit_other_admin_attributes(self):
        """Test if Admin.edit_attribute() method works correctly while editing
        other admin's attributes."""
        random_admin = Admin(
            "AdminName",
            "AdminSurname",
            "adminemail@gmail.com",
            Genders.MALE,
            "30-11-1989",
        )
        self.test_admin1.edit_attribute(
            random_admin,
            {"surname": "NewAdminSurname", "email": "newredemail@gmail.com"},
        )
        self.assertEqual(random_admin.surname, "NewAdminSurname")
        self.assertEqual(random_admin.email, "newredemail@gmail.com")
        self.assertEqual(random_admin.author, "AdminName NewAdminSurname")

    def test_admin_modify_other_admin_post(self):
        """Test if Admin.modify_post() method works correctly when admin is
        trying to modify other admin's post.
        """

        with freeze_time("2022-12-12 12:00:00"):
            admin_post1 = self.test_admin2.create_post(
                "Admin title 1", "Admin content 11"
            )
            self.test_admin1.modify_post(
                admin_post1, "Admin new title 1", "Admin new content 11"
            )
            self.assertEqual(admin_post1.title, "Admin new title 1")
            self.assertEqual(admin_post1.content, "Admin new content 11")
            self.assertEqual(
                admin_post1.modification_date, datetime(2022, 12, 12, 12, 0, 0)
            )
            self.assertEqual(
                admin_post1.last_modification_author, self.test_admin1.author
            )

    def test_admin_delete_other_admin_post(self):
        """Test if Admin.delete_post() works correctly when deleting other
        admin's post.
        """

        admin2_post1 = self.test_admin2.create_post(
            "Admin2 title 1", "Admin2 content 11"
        )
        admin2_post2 = self.test_admin2.create_post(
            "Admin2 title 2", "Admin2 content 22"
        )
        self.test_admin1.delete_post(admin2_post1)
        post_list = [admin2_post2]
        self.assertEqual(Post.post_list, post_list)
