# whitespace_checker.py

def check(json_data, rule):
    for key, value in json_data.items():
        if isinstance(value, str) and value.strip() != value:
            return (f"Whitespace found in value of key '{key}'")
    return ("Whitespace check complete.")
