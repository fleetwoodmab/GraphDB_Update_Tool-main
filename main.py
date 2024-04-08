import eel 
import lib
from requests.auth import HTTPBasicAuth
import configparser

# Main reads the config and command line and updates a named graph in a repository in GraphDB with the data from one
# or more Poolparty SKOD concept schemes. Can only do one named graph per call.
# Named graphs that can be updated have to be amed in the config file.
# Credentials are in a different file, to store them seperatly and the default is uploaded to gitlab+
  
eel.init("web")   

config = configparser.ConfigParser()
config.read('config.ini')

config_auth = configparser.ConfigParser()
config_auth.read('credentials.ini')

@eel.expose
def update_graph(graph):
    # Parses command line argument (the graph to be updated) and config for description and a bit of help
    # GSEU goes to a different repository with different Endpoint
    named_graph = '<https://resource.geosphere.at/thes/' + graph + '>'

    in_url = config['endpoints']['in_url_start'] + graph + config['endpoints']['in_url_end']
    if graph == "gseu":
        out_url = config['endpoints']['out_test_host'] + '' + config['endpoints']['out_gseu_repo']
    else:
        out_url = config['endpoints']['out_test_host'] + '' + config['endpoints']['out_repo']
    nodes = config['nodes'][graph].split(",")
    in_auth = HTTPBasicAuth(config_auth['auth']['iuser'], config_auth['auth']['ipw'])
    out_auth = HTTPBasicAuth(config_auth['auth']['ouser'], config_auth['auth']['opw'])

    # Parses config from the config files

    if len(nodes) > 0:
        lib.delete_named_graph(out_url, named_graph, out_auth)
        for node in nodes:
            req = {
                "prettyPrint": True,
                "format": "n-quads",
                "nodeType": "conceptscheme",
                "rootNode": node
            }
            print(node)
            lib.load_data(url=in_url, req=req, auth=in_auth)
            lib.post_data(out_url, out_auth)
        exit(0)
    else:
        exit(1)

eel.start("index.html", mode='default')

# The loop iterates through one or more concept schemes and calls the functions for updating.

    





