from typing import List
from pathlib import Path
import shutil

class Parser:
    def __init__(self):
        self.extensions: List[str] = []

    def valid_extension(self, extension):
        if extension in self.extensions:
            return True
        else:
            return False

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path) as file:
            return file.read()

    def write(self, path: Path, dest: Path, content: str, ext = '.html'):
        full_path= dest / path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(source.relative_to(path), dest)


class ResourceParser(Parser):
    def __init__(self):
        extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        Parser.copy(path,source,dest)
