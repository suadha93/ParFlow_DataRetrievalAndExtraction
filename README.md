# Data extraction tool for the hydrological model ParFlow

# Purpose

This repository provides scripts and examples for extracting time-series data and variables from an open-access research dataset. The dataset contains experimental simulation results and derived diagnostics from ParFlow hydrological model runs, specifically ParFlowCLM DE06. You can find more information about the project [here](https://adapter-projekt.org/).

# Dataset information

The dataset includes a selection of variables and diagnostics accessible via a THREDDS server:
- [THREDDS catalog](https://service.tereno.net/thredds/catalog/forecastnrw/products/catalog.html)
- [Detailed dataset information](https://datapub.fz-juelich.de/slts/FZJ_ParFlow_DE06_hydrologic_forecasts/index.html)


### The figures below demonstrates an example on how to access the path of the datasets, in this case, the climatology of plant available water dataset for the year 2023.

The climatology are stored under climatology_v2.
&nbsp;

![Thredds_server_1](https://github.com/suadha93/ParFlow_data_extraction_tool/assets/139210041/53b02f0f-bbef-4693-87bd-63835831364d)


After clicking on the dataset, it will take you to a similar page as below. 
&nbsp;

![Thredds_server_2](https://github.com/suadha93/ParFlow_data_extraction_tool/assets/139210041/b5aade15-2a03-4b88-b3cc-8e9b1ba52e46)

There are two ways to access the datasets in order to use the extraction tool, the first option is to access it using OPENDAP, where you won't need to download the data, the second option will be to download the dataset using the HTTPserver.
If you chose to access the dataset using OPENDAP, you have to copy the data url shown below and add it to the JSON input file as ParFlowData.
&nbsp;

![Thredds_server_3](https://github.com/suadha93/ParFlow_data_extraction_tool/assets/139210041/6084e4cc-1e48-47da-87a6-0e2c7051c7a7)


# Prerequisites

Ensure you have Python installed, then install the necessary packages:

- `numpy`
- `netCDF4`
- `datetime`
- `csv`
- `json`


For more information on how to install packages follow the steps available [here](https://packaging.python.org/en/latest/tutorials/installing-packages/)                                         

       
Below are step-by-step instructions on how to install the tool and usage examples.

## Installation

Clone the repository as usual

``` bash
git clone https://github.com/suadha93/ParFlow_data_extraction_tool.git
```
Navigate to the repository

``` bash
cd ParFlow_data_extraction_tool
```
 
To use the tool within other projects, you have to extend your local PYTHONPATH, to tell python where to find it. You can do this by:

``` bash
cd ParFlow_data_extraction_tool
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

To run the script you will need input file, a JSON file which includes information on the dataset you want to extract from. Examples are provided in the Usage section.
    the file should include the following infromation:
    bash
             		
	     {
        "IndicatorPath": "https://github.com/suadha93/ParFlow_data_extraction_tool/DE-0055_INDICATOR_regridded_rescaled_SoilGrids250-v2017_BGRvector_newAllv_d.nc",
        "locations": [
             {
            "stationID": " ",
            "stationLat": " ",
            "stationLon": " ",
            "ParFlowData": " ",
            "Depth": " "
           }
        ]
	    }
    
   stationID: name for your station/location\
   stationLat, stationLon: latitude and longitude of the station/location\
   ParFlowData : the path to the dataset in the THREDDS server, or where the dataset is saved\
   Depth: the needed depth in meters 

#### Note:

- The simulations are calculated for 15 layers from the surface to 60m depth in mm water column each depth represents the lower boundary of the layer, their thickness varies with depth. The depths (in meters) are available as follows: 60.0, 42.0, 27.0, 17.0, 7.0, 3.0, 2.0, 1.3, 0.8, 0.5, 0.3,0.17, 0.1, 0.05, 0.02. If the depth inserted as input falls between two layer, the data extracted will be for the lower boundary of the layer. 


## Usage
We have provided a convenient wrapper function that simplifies the extraction of time-series data and variables. To run the wrapper, use the following command format:
bash
```
python wrapper.py data_input.json output_format
```
- data_input.json: Path to the JSON file containing the input data.
- output_format: Desired output format, either 'csv' or 'var'.
- 
Alternatively, you can directly use the tool in your script as follows:

### Extracting a time-series

 
```
from data_extraction_tool import data_extraction_csv
data_input = 'path/to/your/data_input.json"
data_extraction_csv(data_input)
```
This will generate a CSV file for each station specified in the input file.

### Extracting a variable

```
from data_extraction_tool import data_extraction_variable
data_input = 'path/to/your/data_input.json"
data = data_extraction_variable(data_input)
```
The results will return the variables as an array. If more than one station is specified, all results will be returned in one array. It is important to ensure that all stations are within the same time period. If they are not, calculate each variable separately.




