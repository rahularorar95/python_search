from flask import Flask
import operator
from flask import request,render_template
from utils import Trie,createTrie
import json

app = Flask(__name__) # intializing App

namesTrie= createTrie()  # Creating a trie structure in begining so that we can search a particular string in O(N) where N is length of string 

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def search_api():
    query = json.loads(request.data)
    results = []
    results =  list(namesTrie.get_suggestions(query))
    print(results)
    scorecard = {name: round(calculate_score(query, name)) for name in results}         # calculating score and creating a dictionary {"name":"score"}
    results = sorted(scorecard.items(), key=operator.itemgetter(1), reverse=True)       # sorting based on score
    return json.dumps({'results': results})                                             # returning a json response

def calculate_score(query,name):
    return (len(query)/len(name)) * 100
