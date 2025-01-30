def flatten(
    nested_dict: dict,
    flattened_dict: dict | None = None,
    prefix: str | None = None,
) -> dict:
    """Recursively unpack a nested dictionary into a flattened dictionary"""
    flattened_dict = flattened_dict if flattened_dict else dict()
    for k, v in nested_dict.items():
        key = f"{prefix}__{k}" if prefix else k
        if not isinstance(v, dict):
            flattened_dict[key] = v
        else:
            flatten(
                nested_dict=v,
                flattened_dict=flattened_dict,
                prefix=key,
            )
    return flattened_

from typing import Any 

def flatten(value:Any, parent_key:str='', delim:str='__') -> dict[str,str|bool|int|float]:
    """Recursively flattens a nested dictionary or list
    
    eg
    {a:1, b:[2,3], c:{d:4}, e:[{f:5},{f:6}, [7, {f:8}]}
    >>
    {a:1, b__0:2, b__1:3, c__d:4, e__0__f:5, e__1__f:6, e__2__0:7, e__2__1__f:8}
    """
    
    flattened = {}
    if isinstance(value, dict):
        for k, v in value.items():
            child_key = f"{parent_key}{sep}{k}" if parent_key else k
            flattened.update(flatten(value=v, parent_key=child_key, delim=delim))
    elif isinstance(value, list):
        for i, v in enumerate(value):
            child_key = f"{parent_key}{sep}{i}" if parent_key else str(i)
            flattened.update(flatten(value=v, parent_key=child_key, delim=delim))
    else:
        flattened[parent_key] = value
    return flattened
