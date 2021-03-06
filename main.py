"""
Python 3.10 structure pattern matching feature
"""

def pattern_match(item):
    """
    Example pattern matching
    """
    match item:
        case "Kofi":
            print("Is a string")
        case 90:
            print("Is a integer")
        case True | False:
            print("Is a boolean")
        case _:
            print("Type is unknown")

def main():
    """
    Script's entrypoint
    """
    pattern_match("Kofi")
    pattern_match(90)
    pattern_match(True)
    pattern_match(None)
    pattern_match(9.87)
    pattern_match(False)

if __name__ == "__main__":
    main()
