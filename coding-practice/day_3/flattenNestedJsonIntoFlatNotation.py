#input json {"a":{"b":1,"c":{"d":2}}}
def flatten_json(nested_json, parent_key='', separator='.'):
    """
    Flattens a nested JSON object into a flat notation.

    Args:
        nested_json (dict): The nested JSON object to flatten.
        parent_key (str): The base key for recursion (used internally).
        separator (str): The separator to use for flattened keys.

    Returns:
        dict: A flattened JSON object.
    """
    items = []
    for key, value in nested_json.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_json(value, new_key, separator).items())
        else:
            items.append((new_key, value))
    return dict(items)

# Example usage:
nested_json = {"a": {"b": 1, "c": {"d": 2}}}
flattened_json = flatten_json(nested_json)
print(flattened_json)