from pathlib import Path
import ssg.parsers as rp


class Site:
    def __init__(self, source, dest, parsers = None):
        print(f'bulding Site class wtih args {source} {dest}\n')
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = parsers or []

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
            elif path.is_file():
                self.run_parser(path)

    #check back for valid parser usage

    def load_parser(self, extension):
        for parser in self.parsers:
            if rp.ResourceParser.valid_extension(extension):
                return parser

    def run_parser(self,path):
        parser = self.load_parser(path.suffix)
        if parser is not None:
            self.load_parser(parser)




