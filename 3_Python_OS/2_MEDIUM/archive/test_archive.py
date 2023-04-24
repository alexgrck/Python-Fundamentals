from unittest import TestCase
from archive import ArchiveMixin
from test_class import TestingArchive_mixin
import os
from pathlib import Path
import shutil


class Test_Archive(TestCase):
    def setUp(self):
        self.test_archive = TestingArchive_mixin("test_folder")
        self.test_folder_path = Path(os.path.join(os.getcwd(), "test_folder"))
        Path.mkdir(self.test_folder_path)
        self.archive_path = Path(os.path.join(os.getcwd(), "test.zip"))
        self.extract_dir = Path(os.path.join(os.getcwd(), "unpacked"))
        self.test_files = ["test1.txt", "test2.txt"]
        for file in self.test_files:
            Path(os.path.join(os.getcwd(), "test_folder", file)).touch()
        self.file_to_add = Path(os.path.join(os.getcwd(), "test_folder", "test3.txt"))
        self.op_systems = {"posix": "tar.gz", "nt": "zip"}

    def tearDown(self):
        if os.path.exists(self.test_folder_path):
            shutil.rmtree(self.test_folder_path)
        if os.path.exists(self.extract_dir):
            shutil.rmtree(self.extract_dir)
        if os.path.exists(self.archive_path):
            os.remove(self.archive_path)

    def test_create_archive(self):
        self.test_archive.make_arch(self.test_folder_path, "test")
        self.assertTrue(os.path.exists(self.archive_path))
        shutil.unpack_archive(self.archive_path, self.extract_dir, "zip")
        extracted1 = Path(os.path.join(self.extract_dir, "test_folder", "test1.txt"))
        extracted2 = Path(os.path.join(self.extract_dir, "test_folder", "test2.txt"))
        self.assertTrue(os.path.exists(extracted1))
        self.assertTrue(os.path.exists(extracted2))

    def test_add_to_archive(self):
        shutil.make_archive(
            "test",
            self.op_systems.get(os.name, "tar.gz"),
            base_dir=os.path.basename(self.test_folder_path),
        )
        self.file_to_add.touch()
        self.test_archive.add_to_archive(self.archive_path, self.file_to_add)
        shutil.unpack_archive(self.archive_path, self.extract_dir, "zip")
        extracted1 = Path(os.path.join(self.extract_dir, "test_folder", "test1.txt"))
        extracted2 = Path(os.path.join(self.extract_dir, "test_folder", "test2.txt"))
        extracted3 = Path(os.path.join(self.extract_dir, "test3.txt"))
        self.assertTrue(os.path.exists(extracted1))
        self.assertTrue(os.path.exists(extracted2))
        self.assertTrue(os.path.exists(extracted3))

    def test_extract_archive(self):
        shutil.make_archive(
            "test",
            self.op_systems.get(os.name, "tar.gz"),
            base_dir=os.path.basename(self.test_folder_path),
        )
        self.test_archive.extract_archive(self.archive_path, self.extract_dir, "zip")
        extracted1 = Path(os.path.join(self.extract_dir, "test_folder", "test1.txt"))
        extracted2 = Path(os.path.join(self.extract_dir, "test_folder", "test2.txt"))
        self.assertTrue(os.path.exists(extracted1))
        self.assertTrue(os.path.exists(extracted2))

    def test_remove_from_archive(self):
        shutil.make_archive(
            "test",
            self.op_systems.get(os.name, "tar.gz"),
            base_dir=os.path.basename(self.test_folder_path),
        )
        self.test_archive.remove_from_archive(
            self.archive_path, "test_folder/test2.txt"
        )
        shutil.unpack_archive(self.archive_path, self.extract_dir, "zip")
        extracted1 = Path(os.path.join(self.extract_dir, "test_folder", "test1.txt"))
        extracted2 = Path(os.path.join(self.extract_dir, "test_folder", "test2.txt"))
        self.assertTrue(os.path.exists(extracted1))
        self.assertFalse(os.path.exists(extracted2))
