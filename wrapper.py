#!/usr/bin/env python

"""
This module provides a wrapper for "data_extraction_tool" to run the tool from 
the command line and to demonstrate how to call the module from your own code.

PURPOSE:
The script allows for extracting data as specified in a JSON input file and 
outputs it either in CSV format to a file or as a Python numpy variable.

INPUTS:
- runctrl_file: str
  Filename (incl. path) of the JSON file containing the configuration data for 
  the extraction
- output_format: str
  Desired output format, either 'csv' or 'var'

OUTPUTS:
- numpy variable, always returned, and, if 'csv' is set,  
- csv file with timeseries at a certain station location

FUNCTIONALITIES:
1. Validation of the command line arguments to ensure proper usage.
2. Depending on the specified output format, it extracts data from a 
   THREDDS server as specified by the JSON file and saves it in numpy 
   array and alternatively as a CSV file.

USAGE:
- python wrapper.py data_input.json output_format
- ./wrapper.py data_input.json output_format

USAGE EXAMPLES:
- Extracts data from example_input.json and saves it as a CSV file:
  python wrapper.py example_input.json csv
- Extracts data from example_input.json as a variable and prints to standard 
  out:
  python wrapper.py example_input.json var
"""

import sys

import data_extraction_tool

__author__ = "Suad HAMMOUDEH, Klaus GEORGEN"
__copyright__ = "Copyright 2024, http://www.fz-juelich.de"
__credits__ = [""]
__license__ = "MIT"
__version__ = "v1.0.0"
__maintainer__ = "Suad HAMMOUDEH"
__email__ = "s.hammoudeh@fz-juelich.de"
__status__ = "Production"

def main():

    if len(sys.argv) != 3:
        print("USAGE: python wrapper.py data_input.json output_format")
        sys.exit(1)

    ctrl_file = sys.argv[1]
    output_format = sys.argv[2]
    print(ctrl_file, output_format)

    if output_format not in ["csv", "var"]:
        print("Invalid output format. Please choose either 'csv' or 'var'.")
        sys.exit(1)

    data = data_extraction_tool.data_extraction(ctrl_file, output_format)
    print("data shape: ", data.shape)
    print("data: ", data)

if __name__ == "__main__":

    main()