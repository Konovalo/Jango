import sys

def ex03():
    states = {"Oregon" : "OR", "Alabama" : "AL","New Jersey": "NJ", "Colorado" : "CO"}
    capital_cities = {"OR": "Salem","AL": "Montgomery", "NJ": "Trenton","CO": "Denver"}
    if len(sys.argv) == 2:
        st =  sys.argv[1]
        if not (st in states):
            print("Unknown state")
        else:
            if not (states[st] in capital_cities):
                print("Unknown state")
            else:
                print(capital_cities[states[st]])




if __name__ == '__main__':
    ex03()
