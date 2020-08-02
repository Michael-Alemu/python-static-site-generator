from pathlib import Path


class Site:
    def __init__(self, source, dest):
        print(f'bulding Site class wtih args {source} {dest}\n')
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)
        print(f'creating directory @ {directory}')

    def build(self):
        print('called build')
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob('*'):
            if path.is_dir():
                self.create_dir(path)
                print(f'bulding path in {path}\n')
            else:
                print(f'this path {path} is not a dir')
