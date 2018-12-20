import csv

class Trie:
    def __init__(self):
        self.lastNode = False   # will tell if word is completed
        self.children = {}      # will store all the further nodes

    def insert(self, name):
        curr = self
        for char in name:
            node = curr.children.get(char)
            if not node:
                node = Trie()
                curr.children[char] = node
            curr = node
        curr.lastNode = True       # word is completed

    def get_suggestions(self, query):
        cur = self
        for char in query:
            cur = cur.children.get(char)
            if cur is None:
                return
        for i in cur.suggestions_rec(query):   # whenever function will return a value it is returned to upper call
            yield i
    
    def suggestions_rec(self, query):
        cur = self
        if cur.lastNode:
            yield query

        for next_char, node in cur.children.items():
            for i in  node.suggestions_rec(query + next_char):
                yield i                                                 # recursively calling by adding one char each time


def createTrie():
    t = Trie()
    with open('data.csv') as csv_file:       # opening a csv file
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                row = (" ".join(row).replace("  "," ")).strip()   #joining first name, middle name and last name 
                if(row):
                    t.insert(str(row))                              #inserting in trie
                    line_count += 1
        print(line_count)
        return t