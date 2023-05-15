import os
import shutil
from pathlib import Path
from unittest import TestCase

from test_class import TestingArchiveMixin


class TestArchive(TestCase):
    def setUp(self):
        # stworzyć jeden folder, w którym będę miała foldery do pakowania i wypakowywania,
        # żeby później w teardown class usuwać tylko ten folder
        self.test_archive = TestingArchiveMixin("main", "to_be_archived")
        self.test_folder_path = Path.cwd().joinpath("main", "to_be_archived")
        # Path(
        #     os.path.join(os.getcwd(), "main", "to_be_archived")
        # )
        Path.mkdir(self.test_folder_path, parents=True)
        # os.chdir(str(self.test_folder_path.parent))
        # Path(os.path.join(os.getcwd(), "main", "test.zip"))
        self.test_files = ["test1.txt", "test2.txt"]
        for file in self.test_files:
            # Path(os.path.join(os.getcwd(), "main", "to_be_archived", file)).touch()
            self.test_folder_path.joinpath(file).touch()
        self.extract_dir = self.test_folder_path.parent
        self.archive_path = self.extract_dir.joinpath("test.zip")
        self.file_to_add = self.test_folder_path.joinpath("test3.txt")
        # zmockować to
        self.op_systems = {"posix": "tar.gz", "nt": "zip"}

    def tearDown(self):
        # os.chdir(os.getcwd())
        shutil.rmtree(self.test_folder_path.parent)
        # shutil.rmtree(Path.cwd().joinpath("main"))

    # self.test_folder_path.rmdir()
    # if os.path.exists(self.test_folder_path):
    #     shutil.rmtree(self.test_folder_path)
    # if os.path.exists(self.extract_dir):
    # os.chdir(os.getcwd())
    # shutil.rmtree(self.extract_dir)

    # if os.path.exists(self.archive_path):
    #     os.remove(self.archive_path)

    def test_create_archive(self):
        print("CREATING")
        self.test_archive.make_arch(self.test_folder_path, "test")
        # self.assertTrue(os.path.exists(self.archive_path))
        print(self.assertTrue(self.archive_path.exists()))
        shutil.unpack_archive(self.archive_path, self.extract_dir, "zip")
        extracted1 = self.extract_dir.joinpath("to_be_archived", "test1.txt")
        extracted2 = self.extract_dir.joinpath("to_be_archived", "test2.txt")
        print(extracted1)
        print(extracted2)
        # Path(os.path.join(self.extract_dir, "to_be_archived", "test1.txt"))
        # extracted2 = Path(os.path.join(self.extract_dir, "to_be_archived", "test2.txt"))
        print(self.assertTrue(os.path.exists(extracted1)))
        print(self.assertTrue(os.path.exists(extracted2)))

    # def test_add_to_archive(self):
    #     shutil.make_archive(
    #         "test",
    #         self.op_systems.get(os.name, "tar.gz"),
    #         base_dir=os.path.basename(self.test_folder_path),
    #     )
    #     self.file_to_add.touch()
    #     self.test_archive.add_to_archive(self.archive_path, self.file_to_add)
    #     shutil.unpack_archive(self.archive_path, self.extract_dir, "zip")
    #     extracted1 = Path(os.path.join(self.extract_dir, "test_folder", "test1.txt"))
    #     extracted2 = Path(os.path.join(self.extract_dir, "test_folder", "test2.txt"))
    #     extracted3 = Path(os.path.join(self.extract_dir, "test3.txt"))
    #     self.assertTrue(os.path.exists(extracted1))
    #     self.assertTrue(os.path.exists(extracted2))
    #     self.assertTrue(os.path.exists(extracted3))

    # def test_extract_archive(self):
    #     shutil.make_archive(
    #         "test",
    #         self.op_systems.get(os.name, "tar.gz"),
    #         base_dir=os.path.basename(self.test_folder_path),
    #     )
    #     self.test_archive.extract_archive(self.archive_path, self.extract_dir, "zip")
    #     extracted1 = Path(os.path.join(self.extract_dir, "test_folder", "test1.txt"))
    #     extracted2 = Path(os.path.join(self.extract_dir, "test_folder", "test2.txt"))
    #     self.assertTrue(os.path.exists(extracted1))
    #     self.assertTrue(os.path.exists(extracted2))

    # def test_remove_from_archive(self):
    #     shutil.make_archive(
    #         "test",
    #         self.op_systems.get(os.name, "tar.gz"),
    #         base_dir=os.path.basename(self.test_folder_path),
    #     )
    #     self.test_archive.remove_from_archive(
    #         self.archive_path, "test_folder/test2.txt"
    #     )
    #     shutil.unpack_archive(self.archive_path, self.extract_dir, "zip")
    #     extracted1 = Path(os.path.join(self.extract_dir, "test_folder", "test1.txt"))
    #     extracted2 = Path(os.path.join(self.extract_dir, "test_folder", "test2.txt"))
    #     self.assertTrue(os.path.exists(extracted1))
    #     self.assertFalse(os.path.exists(extracted2))
