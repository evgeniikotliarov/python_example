def make_car(mark, model, **other):
    car = {}
    car['mark'] = mark
    car['model'] = model
    for key, value in other.items():
        car[key] = value
    return car