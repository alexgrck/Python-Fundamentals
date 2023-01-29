from datetime import datetime
from enum import Enum
from unittest import TestCase

from freezegun import freeze_time
from user_management import Admin, Post, Redactor


class Genders(Enum):
    FEMALE = "F"
    MALE = "M"


class TestUMRedactorAdminInteraction(TestCase):
    def setUp(self):
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

    def test_redactor_modify_admin_post(self):
        """Test if Redactor.modify_post() method works correctly when redactor
        is trying to modify admin's post.
        """

        with freeze_time("2022-12-12 12:00:00"):
            admin_post1 = self.test_admin1.create_post(
                "Admin1 title 1", "Admin1 content 1"
            )
            self.test_red1.modify_post(admin_post1, "Red1 title 1", "Red1 content 11")
            self.assertEqual(admin_post1.title, "Red1 title 1")
            self.assertEqual(admin_post1.content, "Red1 content 11")
            self.assertEqual(
                admin_post1.modification_date, datetime(2022, 12, 12, 12, 0, 0)
            )
            self.assertEqual(
                admin_post1.last_modification_author, self.test_red1.author
            )

    def test_redactor_delete_admin_post(self):
        """Test if TypeError is raised when redactor is trying to delete
        admin's post.
        """

        admin_post1 = self.test_admin1.create_post("Admin title 1", "Admin content 1")
        with self.assertRaises(TypeError):
            self.test_red1.delete_post(admin_post1, self.test_admin1)

    def test_admin_edit_redactor_attributes(self):
        """Test if Admin.edit_attribute() method works correctly while editing
        redactor's attributes."""

        random_redactor = Redactor(
            "RandomRedName",
            "RandomRedSurname",
            "randred@gmail.com",
            Genders.MALE,
            "15-12-1990",
        )
        self.test_admin1.edit_attribute(
            random_redactor,
            {
                "name": "NewRedName",
                "email": "newredemail@gmail.com",
                "gender": Genders.FEMALE,
            },
        )
        self.assertEqual(random_redactor.name, "NewRedName")
        self.assertEqual(random_redactor.email, "newredemail@gmail.com")
        self.assertEqual(random_redactor.gender, Genders.FEMALE)
        self.assertEqual(random_redactor.author, "NewRedName RandomRedSurname")

    def test_admin_modify_redactor_post(self):
        """Test if Admin.modify_post() method works correctly when admin is
        trying to modify redactor's post.
        """

        with freeze_time("2022-12-12 12:00:00"):
            red_post1 = self.test_red1.create_post("Red1 title 1", "Red1 content 1")
            self.test_admin1.modify_post(
                red_post1, "Admin new title", "Admin new content"
            )
            self.assertEqual(red_post1.title, "Admin new title")
            self.assertEqual(red_post1.content, "Admin new content")
            self.assertEqual(
                red_post1.modification_date, datetime(2022, 12, 12, 12, 0, 0)
            )
            self.assertEqual(
                red_post1.last_modification_author, self.test_admin1.author
            )

    def test_admin_delete_redactor_post(self):
        """Test if Admin.delete_post() works correctly when deleting redactor's
        post.
        """

        red1_post1 = self.test_red1.create_post("Red1 title 1", "Red1 content 1")
        red1_post2 = self.test_red1.create_post("Red1 title 2", "Red1 content 11")
        self.test_admin1.delete_post(red1_post1)
        post_list = [red1_post2]
        self.assertEqual(Post.post_list, post_list)
