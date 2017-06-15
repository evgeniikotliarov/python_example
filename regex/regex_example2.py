import datetime
import re


number_mapping = {'\d': '[0-9]',
                  '\w': '[a-zA-Z]',
                  '3': 'three'}
s = "\d testing \w 3"
for k, v in number_mapping.items():
    s = s.replace(k, v)
print(s)
# print( re.sub(r'\d', lambda x: number_mapping[x.group()], s))

def valid_date(datestring):
        try:
                mat=re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', datestring)
                if mat is not None:
                        datetime.datetime(*(map(int, mat.groups()[-1::-1])))
                        return True
        except ValueError:
                pass
        return False


def phone_format(phone_number):
    clean_phone_number = re.sub('[^0-9]+', '', phone_number)
    formatted_phone_number = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(clean_phone_number[:-1])) + clean_phone_number[-1]
    return formatted_phone_number