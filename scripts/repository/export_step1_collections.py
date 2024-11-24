import os
import lsst.daf.butler as daf_butler

repo = "/repo/roman-desc-sims"

butler = daf_butler.Butler(repo)
pattern = "u/descdm/step1_*_w_2024_22/*",
coll_types = [daf_butler.CollectionType.RUN]
run_collections = sorted(set(butler.registry.queryCollections(
    pattern, collectionTypes=coll_types)))

for run_collection in run_collections:
    subset = run_collection.split('/')[2].split('_')[1]
    refs = set()
    for ref_iter in butler.registry.\
        queryDatasets('*', collections=[run_collection]).byParentDatasetType():
        refs = refs.union(set(_ for _ in ref_iter))
    refs = list(refs)
    print(len(refs), flush=True)

    os.makedirs(subset, exist_ok=True)
    with butler.export(directory=subset,
                       filename=f"step1_{subset}_run_data.yaml",
                       transfer=None) as exporter:
        exporter.saveDatasets(refs)
        exporter.saveCollection(run_collection)
