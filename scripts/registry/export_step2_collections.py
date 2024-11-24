import os
import lsst.daf.butler as daf_butler

repo = "/repo/roman-desc-sims"
butler = daf_butler.Butler(repo)

# step2a, one TAGGED collection
collection = "u/descdm/step2a_output_w_2024_22"
refs = set()
for ref_iter in butler.registry.\
    queryDatasets('*', collections=collections).byParentDatasetType():
    refs = refs.union(set(_ for _ in ref_iter))
outdir = "step2a"
os.makedirs(outdir, exist_ok=True)
with butler.export(directory=outdir,
                   filename=f"step2a_run_data.yaml",
                   transfer=None) as exporter:
    exporter.saveDatasets(refs)
    exporter.saveCollection(collection)

# step2b, two RUN collections
collections = ["u/descdm/step2b_w_2024_22/20240809T204319Z",
               "u/descdm/step2b_DM-45773_w_2024_22/20240815T224442Z"]
outdir = "step2b"
os.makedirs(outdir, exist_ok=True)
for collection in collections:
    refs = set()
    for ref_iter in butler.registry.\
        queryDatasets('*', collections=[collection]).byParentDatasetType():
        refs = refs.union(set(_ for _ in ref_iter))
    collection_name = os.path.basename(os.path.dirname(collection))
    with butler.export(directory=outdir,
                       filename=f"{collection_name}.yaml",
                       transfer=None) as exporter:
        exporter.saveDatasets(refs)
        exporter.saveCollection(collection)

# step2d, one TAGGED collection
collection = "u/descdm/step2d_output_w_2024_22"
refs = set()
for ref_iter in butler.registry.\
    queryDatasets('*', collections=[collection]).byParentDatasetType():
    refs = refs.union(set(_ for _ in ref_iter))
outdir = "step2d"
os.makedirs(outdir, exist_ok=True)
with butler.export(directory=outdir,
                   filename=f"{os.path.basename(collection)}.yaml",
                   transfer=None) as exporter:
    exporter.saveDatasets(refs)
    exporter.saveCollection(collection)

# step2e, one RUN collection
collections = ["u/descdm/step2e_w_2024_22/20240821T220059Z"]
outdir = "step2e"
os.makedirs(outdir, exist_ok=True)
for collection in collections:
    refs = set()
    for ref_iter in butler.registry.\
        queryDatasets('*', collections=[collection]).byParentDatasetType():
        refs = refs.union(set(_ for _ in ref_iter))
    collection_name = os.path.basename(os.path.dirname(collection))
    with butler.export(directory=outdir,
                       filename=f"{collection_name}.yaml",
                       transfer=None) as exporter:
        exporter.saveDatasets(refs)
        exporter.saveCollection(collection)
