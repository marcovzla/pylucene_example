#!/usr/bin/env python

import os
import glob
import argparse
import lucene
from java.nio.file import Paths
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.index import IndexWriter, IndexWriterConfig
from org.apache.lucene.analysis.core import WhitespaceAnalyzer
from org.apache.lucene.document import Document, StoredField, TextField, Field

# command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--index-dir', default=os.path.expanduser('~/data/automates/index'))
parser.add_argument('input_dir')
args = parser.parse_args()

# initialize lucene
lucene.initVM()
directory = SimpleFSDirectory(Paths.get(args.index_dir))
analyzer = WhitespaceAnalyzer()
writerConfig = IndexWriterConfig(analyzer)
writerConfig.setOpenMode(IndexWriterConfig.OpenMode.CREATE)
writer = IndexWriter(directory, writerConfig)

def make_document(filename):
    with open(filename) as f:
        text = f.read()
    doc = Document()
    doc.add(StoredField("filename", filename))
    doc.add(TextField("text", text, Field.Store.NO))
    return doc

for filename in glob.glob(os.path.join(args.input_dir, '*.txt')):
    print(f'indexing {filename}')
    doc = make_document(filename)
    writer.addDocument(doc)

writer.close()
