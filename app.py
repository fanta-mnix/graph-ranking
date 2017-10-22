from rank import *
from pprint import pprint

links = {
    'webpage-1': {'webpage-2', 'webpage-4', 'webpage-5', 'webpage-6', 'webpage-8', 'webpage-9', 'webpage-10'},
    'webpage-2': {'webpage-5', 'webpage-6'},
    'webpage-3': {'webpage-10'},
    'webpage-4': {'webpage-9'},
    'webpage-5': {'webpage-2', 'webpage-4'},
    'webpage-6': set(), # dangling page
    'webpage-7': {'webpage-1', 'webpage-3', 'webpage-4'},
    'webpage-8': {'webpage-1'},
    'webpage-9': {'webpage-1', 'webpage-2', 'webpage-3', 'webpage-8', 'webpage-10'},
    'webpage-10': {'webpage-2', 'webpage-3', 'webpage-8', 'webpage-9'},
}

pprint(calculate_rank(links))
