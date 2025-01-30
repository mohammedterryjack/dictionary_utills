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

def flatten(value:Any, parent_key:str='', sep:str='__') -> dict[str,str|bool|int|float]:
    """Recursively flattens a nested dictionary with keys separated by '__'."""
    
    flattened = {}
    if isinstance(value, dict):
        for k, v in value.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            flattened.update(flatten(v, new_key, sep))
    elif isinstance(value, list):
        for i, v in enumerate(value):
            new_key = f"{parent_key}{sep}{i}" if parent_key else str(i)
            flattened.update(flatten(v, new_key, sep))
    else:
        flattened[parent_key] = value
    return flattened
