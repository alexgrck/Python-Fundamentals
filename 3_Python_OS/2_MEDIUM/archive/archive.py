import os
import sys
from shutil import make_archive, unpack_archive
from zipfile import ZipFile


class ArchiveMixin:
    def make_arch(self, path, arch_name, dir_name):
        archive_name = os.path.expanduser(os.path.join(path, "~", arch_name))
        platforms = {"Windows": "win32", "Linux": "linux", "macOS": "darwin"}
        if sys.platform.startswith("linux"):
            make_archive(archive_name, "gztar", root_dir=path, base_dir=dir_name)
        elif sys.platform.startswith("win32"):
            make_archive(archive_name, "zip", root_dir=path, base_dir=dir_name)

    # https://docs.python.org/3/library/sys.html#sys.platform
    # macOS
    # linuxowe, macosy - systemy unixowe
    # inny wybór rozszerzenia
    # czyściej, słownik
    # nie rozumiem expanduser
    # skoro podajemy arch_name, to czemu folder ma samą tyldę?
    # przetestować w csv i json

    def add_to_archive(self, zip_file_path, file_path):
        with ZipFile(zip_file_path, "a") as archive:
            archive.write(file_path)
        # zipfile?
        # pass

    def extract_archive(self, archive_path, extract_dir, archive_format):
        unpack_archive(archive_path, extract_dir, archive_format)

    def remove_from_archive(self):
        pass


# zrobić pliki i klasę testową i próbować

# w sumie to takiego zipa tworzymy
