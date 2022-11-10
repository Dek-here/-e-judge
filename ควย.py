import json
 
def main():
    """Main function"""
    player = dict()
    txt = input()
    player.update(json.loads(txt))
    print(player)
main()