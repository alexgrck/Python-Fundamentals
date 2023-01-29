from datetime import datetime
from enum import Enum
from unittest import TestCase
from freezegun import freeze_time
from user_management import Post, Redactor


class Genders(Enum):
    FEMALE = "F"
    MALE = "M"


class TestUMRedactorInteraction(TestCase):
    def setUp(self):
        self.test_red1 = Redactor(
            "TestNameRed1",
            "TestSurnameRed1",
            "testred1@gmail.com",
            Genders.MALE,
            "17-02-1965",
        )
        self.test_red2 = Redactor(
            "TestNameRed2",
            "TestSurnameRed2",
            "testred2@gmail.com",
            Genders.FEMALE,
            "26-05-2000",
        )

    def tearDown(self):
        Post.post_list = []

    def test_redactor_modify_other_redactor_post(self):
        """Test if Redactor.modify_post() method works correctly when redactor
        is trying to modify other redactor's post.
        """

        with freeze_time("2022-12-12 12:00:00"):
            red_post1 = self.test_red2.create_post("Red1 title 1", "Red1 content 11")
            self.test_red1.modify_post(
                red_post1, "Red2 new title 1", "Red2 new content 11"
            )
            self.assertEqual(red_post1.title, "Red2 new title 1")
            self.assertEqual(red_post1.content, "Red2 new content 11")
            self.assertEqual(
                red_post1.modification_date, datetime(2022, 12, 12, 12, 0, 0)
            )
            self.assertEqual(red_post1.last_modification_author, self.test_red1.author)

    def test_redactor_delete_other_redactor_post(self):
        """Test if Redactor.delete_post() method works correctly when redactor
        is trying to delete other redactor's post
        """

        red2_post1 = self.test_red2.create_post(
            "Red2 post1 title", "Red2 post1 content"
        )
        red2_post2 = self.test_red2.create_post(
            "Red2 post2 title", "Red2 post2 content"
        )
        self.test_red1.delete_post(red2_post1, self.test_red2)
        post_list = [red2_post2]
        self.assertEqual(Post.post_list, post_list)
