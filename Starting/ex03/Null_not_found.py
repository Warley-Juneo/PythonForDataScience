import math

def use_print(string: str, object: any) -> None:
    print(f"{string}: {object} {type(object)}")
    return

def NULL_not_found(object: any) -> int:
    type_object = type(object)
    
    if type_object == type(None):
        use_print("Nothing", object)
    elif type_object == float and math.isnan(object):
        use_print("NaN", object)
    elif type_object == int and object == 0:
        use_print("Zero", object)
    elif type_object == str and object == ' ':
        use_print("Empty", object)
    elif type_object == bool and object == False:
        use_print("Fake", object)
    else:
        print("Type not Found")
        return 1
    return 0