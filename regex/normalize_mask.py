import re


class Normalize:
    def __init__(self, string):
        self.string = string


    def read_string(self):
        number_mapping = {'\d': ' [0-9]','\w': ' [a-zA-Z]'}
        for k, v in number_mapping.items():
            self.string = self.string.replace(k, v)


    def check_string(self):
        print(self.string)
        self.string = re.sub('\][^{]', ']{1} ', self.string)


    def run_normalize(self):
        self.read_string()
        self.check_string()
        return self.string

a = Normalize("\d\w0\d{0,9}")
b = a.run_normalize()
print(b)
