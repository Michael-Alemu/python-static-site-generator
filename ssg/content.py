import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimeter = "^(?:-|+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, depth = 2)
        load(fm, Loader=FullLoader)
        cls(metadata, content)

    def __init__(self, metadata, content):
        data = metadata
        self.data = {'content': content}


    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if 'type' in self.data else None

    @data.setter
    def data(self, value):
        self.data['type'] = value

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
       len(self.data.keys())

    def __repr__(self):
        data ={}
        return str(data)













