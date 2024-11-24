cd /rds/project/rds-rPTGgs6He74/desc/roman-rubin-data

butler create repo

butler register-instrument /repo/roman-desc-sims lsst.obs.lsst.LsstCam

(time butler register-skymap --config-file ${DESC_ROMAN_DRP_DIR}/config/dc2_cells_v1_skymap.py /repo/roman-desc-sims) >& skymap_register.log

#1 min
(time ./import_registry_data.py --export_file calibs/roman-desc-sims/export.yaml /rds/project/rds-rPTGgs6He74/desc/roman-rubin-data/repo) &> calibs_import.log

(bash /rds/project/rds-rPTGgs6He74/desc/roman-rubin-data/shared/refcats/uw_stars_20240529_tp_aug_2021_downselect/ingest_refcats.sh) >& refcat_ingest.log

butler collection-chain /repo/roman-desc-sims LSSTCam/defaults LSSTCam/calib LSSTCam/calib/20240319 refcats skymaps

#12.5GB, 25 min
(time ./import_registry_data.py --export_file step1/000/step1_000_run_data.yaml /rds/project/rds-rPTGgs6He74/desc/roman-rubin-data/repo) &> step1_000_import.log

#1.8GB, 5 min
(time ./import_registry_data.py --export_file step2/step2a/step2a_output_w_2024_22.yaml /rds/project/rds-rPTGgs6He74/desc/roman-rubin-data/repo) &> step2a_import.log

#7 sec
(time ./import_registry_data.py --export_file step2/step2b/step2b_w_2024_22.yaml /rds/project/rds-rPTGgs6He74/desc/roman-rubin-data/repo) &> step2b_import.log

#3 sec
(time ./import_registry_data.py --export_file step2/step2b/step2b_DM-45773_w_2024_22.yaml /rds/project/rds-rPTGgs6He74/desc/roman-rubin-data/repo) &> step2b_DM-45773_import.log

#2GB, 5 min
(time ./import_registry_data.py --export_file step2/step2d/step2d_output_w_2024_22.yaml /rds/project/rds-rPTGgs6He74/desc/roman-rubin-data/repo) &> step2d_import.log

#3 sec
(time ./import_registry_data.py --export_file step2/step2e/step2e_w_2024_22.yaml /rds/project/rds-rPTGgs6He74/desc/roman-rubin-data/repo) &> step2e_import.log

(time python ./make_step1_tagged_collection.py) >& step1_tagged_collection.log

butler collection-chain /repo/roman-desc-sims u/descdm/step2_chain_w_2024_22 \
       u/descdm/step2e_w_2024_22/20240821T220059Z \
       u/descdm/step2d_output_w_2024_22 \
       u/descdm/step2b_DM-45773_w_2024_22/20240815T224442Z \
       u/descdm/step2b_w_2024_22/20240809T204319Z \
       u/descdm/step2a_output_w_2024_22
