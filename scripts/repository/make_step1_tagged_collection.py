import os
from collections import defaultdict
import click
import pandas as pd
import lsst.daf.butler as daf_butler

repo = "/repo/roman-desc-sims"
butler = daf_butler.Butler(repo, writeable=True)

step = "step1"
collections = sorted(set(butler.registry.queryCollections(
    f"u/descdm/{step}_???_w_2024_22/2024*",
    collectionTypes=[daf_butler.CollectionType.RUN])))
print("# collections:", len(collections), end='\n\n', flush=True)
#print(collections, flush=True, end='\n\n')

tagged_collection = f"u/descdm/{step}_products_w_2024_22"

try:
    butler.registry.queryCollections(tagged_collection)
except daf_butler.registry.MissingCollectionError:
    pass
else:
    print(f"Collection {tagged_collection} exists. ", flush=True)
    if click.confirm("Overwrite?", default=True):
        butler.registry.removeCollection(tagged_collection)
    else:
        sys.exit(0)

butler.registry.registerCollection(tagged_collection)

dstypes = {'calexp', 'src'}

for i, collection in enumerate(collections):
    refs = sorted(set(butler.registry.queryDatasets(
        dstypes, collections=[collection])))
    print(i, len(refs), flush=True)
    butler.registry.associate(tagged_collection, refs)
