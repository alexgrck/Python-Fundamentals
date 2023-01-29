class MixinPathMethods:
    def scan_path(self, depth, path, ext=".csv"):
        if depth > 0:
            str_depth = "*" + (r"\*" * depth) + ext
            return [file for file in path.glob(str_depth)]
        return [file for file in path.glob(f"**/*{ext}")]

    def create_file(self, abs_path):
        abs_path.touch()

    def delete_file(self, abs_path):
        abs_path.unlink()
