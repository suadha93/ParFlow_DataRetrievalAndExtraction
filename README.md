# Purpose

This repository provides scripts and examples for extracting time-series data and variables from an open-access research dataset. The dataset contains experimental simulation results and derived diagnostics from ParFlow hydrological model runs, specifically ParFlowCLM DE06. You can find more information about the project [here](https://adapter-projekt.org/).

# Dataset information

The dataset includes a selection of variables and diagnostics accessible via a THREDDS server:
- [THREDDS catalog](https://service.tereno.net/thredds/catalog/forecastnrw/products/catalog.html)
- [Detailed dataset information](https://datapub.fz-juelich.de/slts/FZJ_ParFlow_DE06_hydrologic_forecasts/index.html)


The figures below demonstrates an example on how to access the path of the datasets, in this case, the climatology of plant available water dataset for the year 2023.

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
 
To use the tool within other projects, you have to extend your local PYTHONPATH, to inform python where to find it. You can do this by:

``` bash
cd ParFlow_data_extraction_tool
export PYTHONPATH=$PYTHONPATH:$(pwd)
```
To run the script, you will need an input file, specifically a JSON file that includes information about the dataset you want to extract from. Examples are provided in the "Usage" section. The file should include the following information:

```
{
    "IndicatorPath": " ",
    "locations": [
        {
            "stationID": " ",
            "stationLat": ,
            "stationLon": ,
            "ParFlowData": " ",
            "Depth": 
        }
    ]
}
```
   IndicatorPath: the path to the indicator netcdf file, string\
   stationID: name for your station/location, string\
   stationLat, stationLon: latitude and longitude of the station/location, integer\
   ParFlowData : the path to the dataset in the THREDDS server, or where the dataset is saved, string\
   Depth: the needed depth in meters, integer

#### Note:

- The simulations are calculated for 15 layers from the surface to 60m depth in mm water column each depth represents the lower boundary of the layer, their thickness varies with depth. The depths (in meters) are available as follows: 60.0, 42.0, 27.0, 17.0, 7.0, 3.0, 2.0, 1.3, 0.8, 0.5, 0.3,0.17, 0.1, 0.05, 0.02. If the depth inserted as input falls between two layer, the data extracted will be for the lower boundary of the layer.


## Usage

### Examples for the input file 
As mentioned abpve to run the script, you will need an input file, specifically a JSON file. Below are some examples of how the JSON file should be structured:

### Example 1: single location extraction
```
{
    "IndicatorPath": "https://github.com/suadha93/ParFlow_data_extraction_tool/DE-0055_INDICATOR_regridded_rescaled_SoilGrids250-v2017_BGRvector_newAllv.nc",
    "locations": [
        {
            "stationID": "example_station_1",
            "stationLat": 51.21998,
            "stationLon": 4.83778,
            "ParFlowData": "https://service.tereno.net/thredds/dodsC/forecastnrw/products/climatology_v2/paw_DE05_ECMWF-HRES_hindcast_r1i1p2_FZJ-IBG3-ParFlowCLM380_hgfadapter-h00-v02bJurecaGpuProdClimatologyTl_1hr2daily_20220101-20221231.nc",
            "Depth": 10
        }
    ]
}
```
### Example 2: multiple locations extraction, same variable
```
{
    "IndicatorPath": "https://github.com/suadha93/ParFlow_data_extraction_tool/DE-0055_INDICATOR_regridded_rescaled_SoilGrids250-v2017_BGRvector_newAllv.nc",
    "locations": [
        {
            "stationID": "example_station_1",
            "stationLat": 50.93686,
            "stationLon": 6.36174,
            "ParFlowData": "https://service.tereno.net/thredds/dodsC/forecastnrw/products/climatology_v2/wtd_DE05_ECMWF-HRES_hindcast_r1i1p2_FZJ-IBG3-ParFlowCLM380_hgfadapter-h00-v02bJurecaGpuProdClimatologyTl_1day_20230101-20231231.nc",
            "Depth": 7
        },
        {
            "stationID": "example_station_2",
            "stationLat": 52.37677,
            "stationLon": 5.04244,
            "ParFlowData": "https://service.tereno.net/thredds/dodsC/forecastnrw/products/climatology_v2/wtd_DE05_ECMWF-HRES_hindcast_r1i1p2_FZJ-IBG3-ParFlowCLM380_hgfadapter-h00-v02bJurecaGpuProdClimatologyTl_1day_20230101-20231231.nc",
            "Depth": 7
        }
    ]
}
```
### Example 3: multiple locations extraction, different variables and different depths
```
{
    "IndicatorPath": "https://github.com/suadha93/ParFlow_data_extraction_tool/DE-0055_INDICATOR_regridded_rescaled_SoilGrids250-v2017_BGRvector_newAllv.nc",
    "locations": [
        {
            "stationID": "example_station_1",
            "stationLat": 50.94666,
            "stationLon": 6.36094,
            "ParFlowData": "https://service.tereno.net/thredds/dodsC/forecastnrw/products/forecasts_daily/vwc_DE05_ECMWF-HRES_forecast_r1i1p2_FZJ-IBG3-ParFlowCLM380_hgfadapter-d00-v4_1day_2024052012.0012-0240.nc",
            "Depth": 10
        },
        {
            "stationID": "example_station_2",
            "stationLat": 50.94819, 
            "stationLon": 6.35748,
            "ParFlowData": "https://service.tereno.net/thredds/dodsC/forecastnrw/products/forecasts_daily/vsf_DE05_ECMWF-HRES_forecast_r1i1p2_FZJ-IBG3-ParFlowCLM380_hgfadapter-d00-v4_1day_2024052012.0012-0240.nc",
            "Depth": "5"
        },
        {
            "stationID": "example_station_3",
            "stationLat": 50.93718,
            "stationLon": 6.35851,
            "ParFlowData": "https://service.tereno.net/thredds/dodsC/forecastnrw/products/forecasts_daily/tet_DE05_ECMWF-HRES_forecast_r1i1p2_FZJ-IBG3-ParFlowCLM380_hgfadapter-d00-v4_1day_2024051912.0012-0240.nc",
            "Depth": "15"
        }
    ]
}
```

We have provided a wrapper function that simplifies the extraction of time-series data and variables. To run the wrapper, use the following command format:

```
python wrapper.py data_input.json output_format
```
- data_input.json: Path to the JSON file containing the input data.
- output_format: Desired output format, either 'csv' or 'var'.

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




