def all_thing_is_obj(object: any) -> int:
    object_type = type(object)
    
    if object_type == int:
        print(f"Type not found")
    elif object_type == str:
        print(f"{object} is in the kitchen : {object_type}")
    else:
        object_type_name = object_type.__name__[0].upper() + object_type.__name__[1:]
        print(f"{object_type_name} : {object_type}")
    return 42
