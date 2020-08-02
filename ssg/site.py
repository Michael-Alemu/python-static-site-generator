from pathlib import Path


class Site:
    def __init__(self, source, dest) -> None:
        super().__init__()
        print(f'bulding Site class wtih args {source} {dest}\n')
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path) -> None:
        directory = Path.home().joinpath(self.dest, path.relative_to(self.source))
        Path.mkdir(directory, parents=True, exist_oK=True)
        print(f'creating directory @ {directory}')

    def build(self) -> None:
        print('called build')
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
                print(f'bulding path in {path}\n')
            else:
                print(f'this path {path} is not a dir')
