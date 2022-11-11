""" https://youtu.be/D1DUcpQ8pIA?list=TLPQMjcwODIwMjKXrDrAcfe-1g&t=84 """
def main():
    """ เพลงรัก ^^ """
    text = input()
    box_dict = dict()
    for i in text:
        box_dict[i] = text.count(i)
    sort_box_dict = sorted(box_dict.items(), \
    key=lambda fon: ord(fon[0]) + (999 if fon[0].isupper() else 0))
    txt = ""
    for j, k in sort_box_dict:
        while k > 0:
            if k > 5:
                txt += "-----|"
                k -= 5
            else:
                txt += k*"-"
                k -= k
        print(j, ":", txt)
        txt = ""
main()
