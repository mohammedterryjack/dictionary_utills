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
    return flattened_dict