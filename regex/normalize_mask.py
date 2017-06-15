import re


class Normalize:
    def __init__(self, string):
        self.string = string


    def read_string(self):
        number_mapping = {'\d': ' [0-9]', '\w': ' [0-9a-zA-Z]', '\s': ' _', '\S' : r' [^ ]', '\W': '\1'}
        for k, v in number_mapping.items():
            self.string = self.string.replace(k, v)


    def check_string(self):
        # alpha = re.search(r'(?P<range>\])[^\{]', self.string)
        # for k, v in alpha.groupdict({}).items():
        #     if k == 'range':
        #         self.string = re.sub(v, ']{1} ', self.string)
        self.string = re.sub('\]([^{*+])', r']{1}\1', self.string)
        self.string = re.sub(r'([^\\])\+', r' \1{1,} ', self.string)
        self.string = re.sub(r'\\(\W)', r' \1 ', self.string)
        self.string = re.sub(r'\*', '{0,}', self.string)
        self.string = re.sub(r'(\S)\[', r'\1 [', self.string)
    # def string_iterator(self):
    #     for item in self.string:
    #         if item == ']' and item !='{':
    #             item = re.sub(item, '1', '{1}')
    #             print(item)

    def run_normalize(self):
        self.read_string()
        print(self.string)
        print('---------')
        self.check_string()
        return self.string

a = Normalize(r"^\+996+(55|77|70)[0-9] \(\)\[\]\d{6}$")
b = a.run_normalize()
print(b)
