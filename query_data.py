#!/usr/bin/env python

import os
import argparse
import lucene
from java.nio.file import Paths
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.analysis.core import WhitespaceAnalyzer
from org.apache.lucene.queryparser.classic import QueryParser

# command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--index-dir', default=os.path.expanduser('~/data/automates/index'))
parser.add_argument('--max-hits', type=int, default=10)
args = parser.parse_args()

# initialize lucene
lucene.initVM()
directory = SimpleFSDirectory(Paths.get(args.index_dir))
index_reader = DirectoryReader.open(directory)
searcher = IndexSearcher(index_reader)
analyzer = WhitespaceAnalyzer()
query_parser = QueryParser('text', analyzer)

# function to retrieve results based on a query string
def search(query_string):
    query = query_parser.parse(query_string)
    top_docs = searcher.search(query, args.max_hits)
    for score_doc in top_docs.scoreDocs:
        doc = searcher.doc(score_doc.doc)
        yield doc.get('filename')

# get queries and display results
running = True
while running:
    query_string = input('> ')
    if query_string is None:
        running = False
    else:
        print(list(search(query_string)))
