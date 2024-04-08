This script pushes data from PoolParty to GraphDB. Change cred entials_default.ini to credentials.ini and add you credentials.

Usage: python main.py <graphname>
All valid graphnames can be seen in config.ini

Structure of the project:
main.py is the main programm, there the config and credentials are loaded and then a loop loads the data and pushes it to the other endpoint.
lib.py is a libary with load, post and clear graph functions.
config.ini is a config file where endpoints, graphs, and concept schemes are stored
credentials.ini contains the credentials to Poolparty and GraphDB. Not uploaded to Gitlab
credentials_default.ini is a template of credentials.ini that IS uploaded to Gitlab.

For more information: christian.linsberger@geosphere.at


