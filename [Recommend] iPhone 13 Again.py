""" [Recommend] iPhone 13 Again """
def first():
    """iPhone 13 mini"""
    text_str = str(input())
    num_gb = str(input())
    if text_str == "iPhone 13 mini":
        if num_gb == "128 GB":
            print(25900)
        elif num_gb == "256 GB":
            print(29900)
        elif num_gb == "512 GB":
            print(37900)
        else:
            print("Not Available")
    elif text_str == "iPhone 13 Pro Max":
        print(third(text_str, num_gb))
    elif text_str == "iPhone 13 Pro":
        print(second(num_gb, text_str))
    elif text_str == "iPhone 13":
        print(fourth(num_gb, text_str))
    else:
        print("Not Available")
def second(num_gb, text_str):
    """iPhone 13 Pro"""
    if text_str == "iPhone 13 Pro":
        if num_gb == "128 GB":
            return 38900
        elif num_gb == "256 GB":
            return 42900
        elif num_gb == "512 GB":
            return 50900
        elif num_gb == "1 TB":
            return 58900
        else:
            return "Not Available"
    else:
        return "Not Available"

def third(text_str, num_gb):
    """iPhone 13 Pro Max"""
    if text_str == "iPhone 13 Pro Max":
        if num_gb == "128 GB":
            return 42900
        elif num_gb == "256 GB":
            return 46900
        elif num_gb == "512 GB":
            return 54900
        elif num_gb == "1 TB":
            return 62900
        else:
            return "Not Available"
    else:
        return "Not Available"
def fourth(num_gb, text_str):
    """iPhone 13"""
    if text_str == "iPhone 13":
        if num_gb == "128 GB":
            return 29900
        elif num_gb == "256 GB":
            return 33900
        elif num_gb == "512 GB":
            return 41900
        else:
            return "Not Available"
    else:
        return "Not Available"
first()
