# Data retrieval and extraction tool for THREDDS-based ParFlow hydrologic model netCDF data

This repository provides standalone Python scripts and example run-control JSON files for retrieving and extracting 1D time-series data from netCDF file-based post-processed simulation results from specific experimental forecasting simulations of the integrated hydrological model [ParFlow](https://github.com/parflow), which are shared a through a [dedicated THREDDS data server](https://datapub.fz-juelich.de/slts/FZJ_ParFlow_DE06_hydrologic_forecasts/index.html). 

The tools in conjunction with the specific experimental ParFlow forecasts allow to extract and retrieve different types of forecasting data (hindcasts or near-realtime forecasts) for a number of ParFlow variables and post-processed diagnostics, for single or multiple locations and/or depths and export them in a numpy array or additionally in a meta-data enriched csv file, e.g., for further use in spreadsheet tools. **As data are extracted from THREDDS server-based netCDF files, only the specified data is effiently extracted and retrieved, without the need to download large data files.**

The tools provided here serve (i) as a means to access and retrieve data from specific experiments, they are also meant (ii) as a basis to expand analysis tools to use this specific dataset, but they are (iii) also generic enough to be used as an example on how to extract timeseries data from gridded netCDF data.

## Setup and installation

### Prerequisites

`Python v3.x` with the following non-standard packages in their recent version that are not part of the Python standard library:
- `numpy`
- `netCDF4`

We developed and tested the tool under Linux and macOS.

### Obtain code

``` bash
git clone https://github.com/kgoergen/ParFlow_data_extraction_tool.git
```

No environmental settings are needed.

## Usage

There are three modes on how to run the tool: 
1. Use the `wrapper.py` to run on the command line
2. In an interactive Python environment
3. From your own Python code, see the `wrapper.py` as an example on how to implement the tool 

**See also usage examples and explanations in the preambles of the py-scripts.**

### Basic command line usage

Using the `wrapper.py` (mode 1), that simplifies the extraction of time-series, just do the following:

``` bash
cd ParFlow_data_extraction_tool
python wrapper.py data_input.json output_format
```

(Command line) parameters:
- data_input.json: JSON file (including path) containing the run-control data which specifies which data(sets) to retrieve timeseries from for which geographic location(s) and which depth(s)
- output_format: output format, either 'csv' or 'var'; the `data_extraction_tool.py` always returns a data array, no matter which option is set; specify 'csv' to obtain also a csv file per json record

### Interactively

t.b.a.

### From within your project

t.b.a.

See `wrapper.py` on how to call the function from the module.

### Notes on outputs
- In case there is more than one record in the json file multiple csv files are written, one record per file.
- Aside from the csv file the extracted and retrieved data is also always returend as a Python numpy ndarray. If more than one JSON record (i.e., multiple locations, depths, variables / diagnostics) is specified, all results will be combind in a single array, with each dataset occupying its own row. The structure of the array is as follows:
- The csv files are always written to the directory form where the `wrapper.py` is called.

```
[
 [ results for record_0],
 [ results for record_1],
 [ results for record_2],
 ...
]
```

### Inputs

Aside from the netCDF files on the THREDDS server, the tool needs two inputs.

#### JSON run-control file structure and examples

In order to systematically test the tool and to provide the user with a range of examples, different `JSON` files are provided. The JSON runcontrol files specify wich netCDF files shall be used (hindcast or forecast, which diagnostic) and for which locations timeseries are to be exracted at which depth. One JSON file may have multiple records. The structure of the JSON file should be as follows:

```
{
    "indicatorFile": "<path and filename of the indicator netCDF file, [string]>",
    "locations": [
        {
            "locationID": "<name for your location, used as indifier, can be any string, no blanks, [string]>",
            "locationLat": <latitude of location [decimal degrees], maximum 5 digits, [float]>,
            "locationLon": <longitude of location [decimal degrees], maximum 5 digits, [float]>,
            "simData": "<path and filename or URL on THREDDS server of the netCDF simulation data file, [string]>",
            "depth": <deph for which data is to be extracted [m], can be positive of negative, [float]>
        }
    ]
}
```

#### External parameter or 'indicator' file

- The tool needs a so-called "indicator" file, which contains information on the hydrofacies distribution in ParFlow that is used in the extraction ool to dertermine whether a specified location is on a water body (river, lake, ocean grid element or not) and the model grid specification as Lon and Lat coordinate arrays in decimal degrees, which specify the model grid centre points. 
- The indicator file is specific to a certain simulaiton experiment and its setup and configuration.
- Here we provide the indicator file `DE-0055_INDICATOR_regridded_rescaled_SoilGrids250-v2017_BGRvector_newAllv.nc`. serves as input to the JSON file.
   
### Usage example

``` bash
python3 wrapper.py example1_1Loc_1Var_climatology.json csv
```

## Main functionalities and conceptual considerations

- **For technical details of the implementation see the py-codes, the headers and in-line comments.**
- A key feature of the tool is that it does not download the entire dataset from the server. Instead, it extracts data from a specific netCDF dataset, for specific locations and depths, based on netCDF files on a THREDDS data server and returns the data as a numpy ndarray and saves it optionally as a CSV file.
- The tool does not include any find functionality, i.e., in order to know how to specify the retrieval request as defined in the JSON file, you need to inspect and consult the dataset website (see below) and inspect the THREDDS server data catalogue a priori.
- The tools are deliberately reduced to some core functionalities to demonstrate the basic usage. Other than standard Python libraries they do not require any other third-party modules. They do not contain a full data retrieval functionality (e.g., incl. polygon data, which is to come) or further analyses tools.
- By means of the JSON files and multiple records per file, it is possible to configure very specific retrievals. E.g., a single variable or diagnostic (like volumetric soi moisture content) for multiple locations at the same depth; or several variables, always at the same location, each one for multiple depths, etc. Each JSON record results in a separate lightweight retrieval (and csv file); all retrieved data vectors per JSON file are combined into a single numpy ndarray, though. I.e., retrieving data for multiple depths for the same variable and same location results in a depth profile along axis 0 in the ndarray, etc.
- Ocean area are treated as missing values, it is nevertheless possible to retrieve data over an ocean grid element. In such a case, the tool issues a wrning and offers alternative locations. The is true for areas where rivers or lakes are located. Please consult the references on the ParFlow simulations for details.
- The user just needs to determine the location at the precision they desire. The tool will find the closest grid element on the model grid. Providing locations at a precioion of more than 5 digits decimal degrees does not make sense. The depth can be specified between 0m and 60m. The tool will find the matching depth layer on the model vertical grid.
- For better understanding of the operations, standard output is written. You need to comment yourself if this is too verbose.

## Dataset information

### Data source

This repository contains tools, which are in conjunction with the ["Experimental FZJ ParFlow DE06 hydrologic forecasts"](https://doi.org/10.26165/JUELICH-DATA/GROHKP), an open-access, free research dataset, that features experimental [ParFlow integrated hydrologic model](https://github.com/parflow/parflow) forecasts and diagnostics, distributed via a THREDDS data server. The [landing page of the dataset](https://datapub.fz-juelich.de/slts/FZJ_ParFlow_DE06_hydrologic_forecasts/index.html) contains all relevant information on the dataset, associated scientific publications, and the terms of use and licensing and citation information which is to be observed. 

### Data access via the THREDDS server

1. Start off from the [landing page of the dataset](https://datapub.fz-juelich.de/slts/FZJ_ParFlow_DE06_hydrologic_forecasts/index.html) 
2. On the [THREDDS data server](https://service.tereno.net/thredds/catalog/forecastnrw/products/catalog.html) navigate the directory of interest, e.g., the [daily forecasts](https://service.tereno.net/thredds/catalog/forecastnrw/products/forecasts_daily/catalog.html)
3. Select a variable of your choice, e.g., "vwc" (volumetric water content) and click on the filename to follow the URL to the individual data record (filename follows a data reference syntax with a controlled vocabulary and looks, e.g. like this: `vwc_DE05_ECMWF-HRES_forecast_r1i1p2_FZJ-IBG3-ParFlowCLM380_hgfadapter-d00-v4_1day_2024062412.0012-0240.nc`)
4. On the data record page click on "Access" and "OpenDAP", which takes you to the "OPeNDAP Dataset Access Form" of the specific netCDF data file 
5. Copy/paste the "Data URL" to your JSON file `simData` entry to retrieve a timeseries from this dataset

A detailed descrption of the THREDDS server functionality is beyond the scope of this README.

Alternatively to 4.: Click on "HTTPServer" to download the complete netCDF file to you local computer, this is NOT recommended as it contradicts the whole idea of using the THREDDS server via OPeNDAP in a first place.

## Limitations

- The ParFlow DE06 experimental forecast dataset also includes ensemble data; these cannot be used unless the `variable` is manually specified in the code of `data_extraction_tool.py`.
- Different variables which different time spans which can't be covered in one query. Therefore, when dealing with different time spans (e.g., a variable from climatology_v2 and one from a forecast_daily), it is necessary to create a separate query for each.
- If intending to use the tool beyond the foreseen applicaiton with the ParFlow post-processed netCDF files files, these files need to be CF compliant and follow certain standard in terms of specification of the dimensions and coordinate axes specifications.

## License

The tools in this repository is free, open source software and is licensed under the MIT-License.