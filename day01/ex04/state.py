import sys

def check(di, val):
    for key in di:
        if di[key] == val:
            return True
    return False

def keykey(di, val):
    for key in di:
        if di[key] == val:
            return key

def ex04():
    states = {
"Oregon" : "OR", "Alabama" : "AL",
"New Jersey": "NJ", "Colorado" : "CO"
}
    capital_cities = {"OR": "Salem",
"AL": "Montgomery", "NJ": "Trenton",
"CO": "Denver"}
    if len(sys.argv) == 2:
        st =  sys.argv[1]
        if not (check(capital_cities, st)):
            print("Unknown capital city")
        else:
            if not (check(states,keykey(capital_cities, st))):
                print("Unknown capital city")
            else:
                print(keykey(states, keykey(capital_cities, st)))




if __name__ == '__main__':
    ex04()
