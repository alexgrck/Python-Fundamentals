import os

from shutil import make_archive, unpack_archive
from zipfile import ZipFile


class ArchiveMixin:
    def make_arch(self, path, arch_name):
        op_systems = {"posix": "tar.gz", "nt": "zip"}
        os.chdir(os.path.dirname(path))
        make_archive(
            arch_name,
            op_systems.get(os.name, "tar.gz"),
            base_dir=os.path.basename(path),
        )

    def add_to_archive(self, archive_path, file_path):
        with ZipFile(archive_path, "a") as archive:
            archive.write(file_path, os.path.basename(file_path))

    def extract_archive(self, archive_path, extract_dir, archive_format):
        unpack_archive(archive_path, extract_dir, archive_format)

    def remove_from_archive(self, archive_path, file_to_delete):
        temp_path = os.path.join(os.path.dirname(archive_path), "temp")
        temp_file = os.path.join(temp_path, file_to_delete)
        os.mkdir(temp_path)
        with ZipFile(archive_path, "r") as archive:
            archive.extractall(temp_path)
        arch_name = os.path.basename(os.path.splitext(archive_path)[0])
        os.remove(archive_path)
        os.remove(temp_file)
        os.chdir(temp_path)
        with ZipFile(archive_path, "a") as archive:
            for root, dirs, files in os.walk(temp_path):
                for file in files:
                    archive.write(os.path.relpath(os.path.join(root, file)))
