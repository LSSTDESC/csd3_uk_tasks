#!/usr/bin/env python

import os
import argparse
import lsst.daf.butler as daf_butler

parser = argparse.ArgumentParser()
parser.add_argument("repo_path", type=str,
                    help="Absolute path to destination data repo")
parser.add_argument("--export_file", type=str,
                    help="exported yaml file with registry info")
parser.add_argument("--record_validation_info", action="store_true",
                    default=False, help="enable storing of dataset info")

args = parser.parse_args()

export_file = os.path.abspath(args.export_file)
assert os.path.isfile(export_file)

butler = daf_butler.Butler(args.repo_path, writeable=True)

butler.import_(directory=args.repo_path,
               filename=export_file,
	       transfer=None,
	       record_validation_info=args.record_validation_info)
