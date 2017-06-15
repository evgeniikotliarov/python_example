BAD_AREA_CODES = open('../regex/text.txt', 'r').read().split('\n')

def is_valid_phone(phone_number, country_code='US'):
    if country_code:
        country_code = country_code.upper()

    phone_number = filter(lambda n: n.isdigit() or n == 'x', phone_number)

    ext = None
    check_ext = phone_number.split('x')
    if len(check_ext) > 1:
        if len(check_ext) > 2:
            return False
        phone_number, ext = check_ext

    if len(phone_number) == 11 and phone_number[0] == '1':
        phone_number = phone_number[1:]
    if len(phone_number) != 10:
        return False

    area_code = phone_number[ :3]
    head      = phone_number[3:6]
    tail      = phone_number[6: ]

    if area_code in BAD_AREA_CODES:
        return False
    if head[0] == '1':
        return False
    if head[1:] == '11':
        return False

    return True