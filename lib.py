import requests
from rdflib import ConjunctiveGraph

# Loads data from Poolparty API transforms it to a graph
# removes the "thesaurus" from the graph name and stores it in a temp file

def load_data(url, req, auth):

    x = requests.post(url, json=req, auth=auth)
    temp = x.content.replace(b"/thesaurus>", b">")

    g = ConjunctiveGraph()
    g.parse(temp, format='nquads')

    g.serialize(destination='temp.nq', format='nquads')

# Loads the temp file and sends the data via post request to an Endpoint
def post_data(url, auth):

    headers = {
        'Content-Type': 'application/n-quads',
        'Accept': 'application/json'
    }

    with open('temp.nq', 'rb') as f:
        requests.post(url, data=f, headers=headers, auth=auth)


# Clears the graph
def delete_named_graph(url, named_graph, auth):
    query = "CLEAR GRAPH" + ' ' + named_graph
    headers = {"content-type": "application/sparql-update"}
    requests.post(url, data=query, headers=headers, auth=auth)
