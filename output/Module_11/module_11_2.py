def introspection_info(obj):
    obj_type = type(obj).__name__
    obj_attributes = dir(obj)
    obj_methods = [method for method in obj_attributes if callable(getattr(obj, method))]
    obj_module = obj.__module__ if hasattr(obj, '__module__') else None
    return {
        'type': obj_type,
        'attributes': obj_attributes,
        'methods': obj_methods,
        'module': obj_module
    }

number_info = introspection_info(42)
print(number_info)
