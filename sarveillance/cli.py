import os
import sys
import ee
import sys
import argparse, pkg_resources
import geemap as gee
from geemap import cartoee
import pandas as pd
from sarveillance.utils import new_get_image_collection_gif
from sarveillance.sarexplorer import SAREXPLORER


def main():

    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base_name", "-b", 
        metavar="<base_name>",
        help="Name of base (See README)"
    )
    parser.add_argument(
        "--start_date", "-s",
        metavar="<start_date>",
        help="Start date in YYYY-MM-DD format",
    )
    parser.add_argument(
        "--end_date", "-e", 
        metavar="<end_date>",
        help="End date in YYYY-MM-DD format"
    )
    parser.add_argument(
        "--output", "-o",
        metavar="<output>",
        help="Directory for output, will be created if it doesn't exist",
    )
    parser.add_argument(
        "--version", "-v",
        action="version",
        version=pkg_resources.require("sarveillance")[0].version,
    )
    args = parser.parse_args()

    cartoee.get_image_collection_gif = new_get_image_collection_gif
    sar = SAREXPLORER(args)
    sar.run()
