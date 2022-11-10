""" B - Fully pair? """
def main():
    """ print paired dance activity """
    use_char = input()
    checked_char = ""
    result = ""
    no_pair = 0
    for char in use_char:
        if checked_char.find(char) == -1:
            checked_char += char
    for unique_char in checked_char:
        if use_char.count(unique_char) % 2 != 0:
            result += unique_char
            no_pair += 1
    if no_pair == 0:
        result = "fully paired"
    print(result)
main()
