import os
import shutil
from pathlib import Path
from unittest import TestCase
import stat
from zipfile import ZipFile
from test_class import TestingArchiveMixin


class TestArchive(TestCase):
    def setUp(self):
        self.test_archive = TestingArchiveMixin("main", "to_be_archived")
        self.main_dir = os.path.join(os.getcwd(), "main")
        self.to_be_archived = os.path.join(self.main_dir, "to_be_archived")
        Path(self.to_be_archived).mkdir(parents=True)
        self.test_files = ["test1.txt", "test2.txt"]
        for file in self.test_files:
            Path(self.to_be_archived).joinpath(file).touch()
        self.archive_path = os.path.join(self.main_dir, "test.zip")
        self.extract_dir = os.path.join(self.main_dir, "unpacked")
        Path(self.extract_dir).mkdir()
        self.file_to_add = os.path.join(self.to_be_archived, "test3.txt")
        self.extracted1 = os.path.join(self.extract_dir, "to_be_archived", "test1.txt")
        self.extracted2 = os.path.join(self.extract_dir, "to_be_archived", "test2.txt")
        self.extracted3 = os.path.join(self.extract_dir, "test3.txt")
        self.op_systems = {"posix": "tar.gz", "nt": "zip"}

    def tearDown(self):
        os.chdir(os.path.dirname(os.getcwd()))
        shutil.rmtree(self.main_dir)

    def test_create_archive(self):
        self.test_archive.make_arch(self.to_be_archived, "test")
        self.assertTrue(os.path.exists(self.archive_path))

        shutil.unpack_archive(self.archive_path, self.extract_dir, "zip")
        self.assertTrue(os.path.exists(self.extracted1))
        self.assertTrue(os.path.exists(self.extracted2))

    def test_add_to_archive(self):
        os.chdir(self.main_dir)
        shutil.make_archive(
            "test",
            self.op_systems.get(os.name, "tar.gz"),
            base_dir=os.path.basename(self.to_be_archived),
        )
        Path(self.file_to_add).touch()

        self.test_archive.add_to_archive(self.archive_path, self.file_to_add)

        shutil.unpack_archive(self.archive_path, self.extract_dir, "zip")
        self.assertTrue(os.path.exists(self.extracted1))
        self.assertTrue(os.path.exists(self.extracted2))
        self.assertTrue(os.path.exists(self.extracted3))

    def test_extract_archive(self):
        os.chdir(self.main_dir)
        shutil.make_archive(
            "test",
            self.op_systems.get(os.name, "tar.gz"),
            base_dir=os.path.basename(self.to_be_archived),
        )

        self.test_archive.extract_archive(self.archive_path, self.extract_dir, "zip")

        self.assertTrue(os.path.exists(self.extracted1))
        self.assertTrue(os.path.exists(self.extracted2))

    def test_remove_from_archive(self):
        os.chdir(self.main_dir)
        shutil.make_archive(
            "test",
            self.op_systems.get(os.name, "tar.gz"),
            base_dir=os.path.basename(self.to_be_archived),
        )

        self.test_archive.remove_from_archive(
            self.archive_path,
            os.path.join(os.path.basename(self.to_be_archived), "test2.txt"),
        )

        shutil.unpack_archive(self.archive_path, self.extract_dir, "zip")
        extracted1 = Path(os.path.join(self.extract_dir, "to_be_archived", "test1.txt"))
        extracted2 = Path(os.path.join(self.extract_dir, "to_be_archived", "test2.txt"))
        self.assertTrue(os.path.exists(extracted1))
        self.assertFalse(os.path.exists(extracted2))
