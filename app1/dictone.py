import json
from difflib import get_close_matches
global data

#def load():
#    with open("data.json") as d:
#        data = json.load(d)

def lookup(term):
    with open("data.json") as d:
#    a = open("data.json")
        data = json.load(d)
#    a.close()
#    load()
    term = term.lower()
    if term in data:
        return data[term]
    else:
        res = get_close_matches(term, data.keys())
        if res:
            i = input("Did you mean \'" + res[0] + "\'? ")
            if i:
                if i.lower()[0] == 'y':
                    return data[res[0]]
            return "Sorry, try searching agian."
        else:
            return "Sorry, that wasn't found in the dictionary."

def main():
    search = input("Enter word to look up: ")
    print(lookup(search))

if __name__ == '__main__': main()
