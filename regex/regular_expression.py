import re

#
# input_filename = "../regex/text.txt"
# result_file = "../regex/results.txt"
#
# inputfile = open(input_filename, mode='r', encoding='UTF8')
# resultfile = open(result_file, mode='w', encoding='UTF8')
# mytext = inputfile.read()
# inputfile.close()
lookfor = {'\d':"[0-5]"}

for k, v in lookfor.items():
    print(re.sub(k, lambda x: lookfor[x.replace(v)], v))

# results = re.findall(lookfor, mytext)

# for item in results:
#
#     resultfile.write(item)
#     print(item)


# resultfile.close()

# print("Total: " + str(len(results)))

PASSWORD_REGEX_STR = "^(?=.*[A-Za-z])(?=.*\\d)(?=.*[$@#$!%*?&=])[A-z\\d$@#$!%*?&=]{8,}$"
PIN_REGEX_STR = "\d{4}"
CODE_REGEX_STR = "\d+"
PROFILE_ID_REGEX = "\d{9}"
EXP_DATE_REGEX = "\d{4}"
CVV_REGEX = "\d{3}"
AMOUNT_REGEX = "\d{3}"
PHONE_REGEX_STR = "^\+996(55|77|70)[0-9]\\d{6}$"
EMAIL_REGEX_STR = '[^@]+@[^@]+\.[^@]+'
REGEX = ".*"
FIO_REGEX_STR = ".*"











def get_regex_date_format():
    return r'\w{3},\s\d{2}\s\w{3}\s\d{4}\s\d{2}:\d{2}:\d{2}\s[A-Z]{3}'


def get_request_regex():
    methods = r'\w+'
    host_symbols = r"[\w\.\-\d/:'0-9]"
    space = r'\s'
    query = r'(?:[?&][^\s&]+)*'
    protocol = r'HTTP/.*'
    request_regex = "(({methods}){space}+({host_symbols}+)({query}){space}+({protocol}))".format(
        methods=methods,
        space=space,
        host_symbols=host_symbols,
        query=query,
        protocol=protocol
        )
    return request_regex.encode()


def get_boundary_regex():
    return b'boundary=(.+)'


def get_content_disposition_regex():
    r = br'Content-Disposition:\s?(.*)\r\n'
    return r


def get_content_type_regex():
    r = br'Content-Type:\s?(.*)\r\n'
    return r


def get_multipart_body_regex():
    r = br'Content-Disposition:\s?.*(?:[\r\n]{0,1}Content-Type:\s?.*[\r\n]{0,1})?.*[\r\n]*([\s\S]*)'
    return r


def get_disposition_name_regex():
    r = br'name="(.*?)"'
    return r


def get_session_regex():
    r = br'session=(.*)\s?'
    return r


def get_template_tokenizer_regex():
    CONTROL = "{%.*?%}"
    EXPRESSIONS = "{{.*?}}"
    r = "(?s)({control}|{expressions})".format(control=CONTROL, expressions=EXPRESSIONS)
    return r