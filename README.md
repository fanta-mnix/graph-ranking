# PageRank for ranking graphs
This project implements a PageRank version inspired by the [original paper](http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf) for ranking graphs according to connectivity measures. The algorithm contains some minor tweaks to take advantage of [NumPy](http://www.numpy.org) capabilities.

## Installing
Make sure to run the `setup.sh` script. It will install all required dependencies.
 
## Running the sample
Use `python usage.py` to see it in action. Dependending on the size of the graph, it may take some time, but it will eventually print the top 10 results to to the console retrieved documents, according to PageRank index.

## Known issues
The implementation focus on simplicity and is not meant to be used with big datasets.

## Alternatives
https://github.com/ashkonf/PageRank
