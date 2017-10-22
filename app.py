import numpy as np

from rank import *
from pprint import pprint

goals = {
    'excellence': {'practice', 'study', 'team'},  # Excellence is built with: practice, study and team
    'practice': {'pro-bono', 'practice-default'},  # 'practice-default' was introduced because 'practice' consists of more than Pro Bono
    'team': {'excellence', 'reputation'},
    'study': {'master', 'study-default'},
    'pro-bono': set(),
    'reputation': {'portfolio', 'pro-bono', 'excellence', 'blogging', 'networking', 'talks', 'master', 'team'},
    'master': set(),
    'portfolio': {'practice', 'study'},  # study? excellence?
    'blogging': set(),
    'networking': {'master', 'team', 'talks', 'blogging'},  # What is my reach | talks? blogging?
    'talks': {'reputation', 'networking', 'excellence'},
    'practice-default': set(),
    'study-default': set()
}

pprint(calculate_rank(goals))
