import os
import sys

from data_extraction_tool import data_extraction_csv, data_extraction_variable

def wrapper():
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
