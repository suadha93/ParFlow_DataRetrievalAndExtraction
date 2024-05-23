#!/usr/bin/env python

import os
import sys
from data_extraction_tool import data_extraction_csv, data_extraction_variable


__author__ = "Suad Hammoudeh"
__copyright__ = "Copyright 2024, http://www.fz-juelich.de"
__credits__ = [""]
__license__ = "MIT"
__version__ = "2024-05-08"
__maintainer__ = "Suad Hammoudeh"
__email__ = "s.hammoudeh@fz-juelich.de"


def wrapper():

    """
This module provides a wrapper for data extraction using the data_extraction_tool library.

The script allows for extracting data from a specified JSON input file and outputting it
either in CSV format or as a Python variable.

Parameters
----------
data_input.json : str
    Path to the JSON file containing the input data.
output_format : str
    Desired output format, either 'csv' or 'var'.

Returns
-------
None

Notes
-----
This script includes the following functionalities:
1. Validates the command line arguments to ensure proper usage.
2. Depending on the specified output format, it either:
   a. Extracts data from the JSON file and saves it as a CSV file using data_extraction_csv.
   b. Extracts data from the JSON file as a variable using data_extraction_variable and prints a success message along with the extracted data.

Usage
-----
python wrapper.py data_input.json output_format

Examples
--------
python wrapper.py example_input.json csv
    Extracts data from example_input.json and saves it as a CSV file.

python wrapper.py example_input.json var
    Extracts data from example_input.json as a variable and prints the extracted data.

"""

    if len(sys.argv) != 3:
        print("Usage: python wrapper.py data_input.json output_format (csv or var)")
        sys.exit(1)

    data_input = sys.argv[1]
    output_format = sys.argv[2]

    if output_format not in ["csv", "var"]:
        print("Invalid output format. Please choose 'csv' or 'var'.")
        sys.exit(1)

    if output_format == "csv":
        data_extraction_csv(data_input)
    elif output_format == "var":
        data = data_extraction_variable(data_input)
        print("Variable extracted successfully:", data)

if __name__ == "__main__":
    wrapper()
