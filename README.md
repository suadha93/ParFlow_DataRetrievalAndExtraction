# Getting started

This repository includes scripts and examples to extract time-series or variables for a specific location from ParFlow simulations, in particular ParFlowCLM DE06 (https://adapter-projekt.org/). Selected variables are available on THREDDS-server (https://service.tereno.net/thredds/catalog/forecastnrw/products/catalog.html). 

## Prepare the repository for the extraction tool

Clone the repository as usual

``` bash
git clone https://icg4geo.icg.kfa-juelich.de/SoftwareTools/parflowclm_de06_data_extraction_tool.git
```
and initialize and update the submodules afterwards

``` bash
cd ParFlow_data_extraction_tool
git submodule init 
git submodule update
```
 
To use the tool within other projects, you have to extend your local PYTHONPATH, to tell python where to find it. You can do this by:
``` bash
cd ParFlow_data_extraction_tool
export PYTHONPATH=$PYTHONPATH:$(pwd)
```
after the repository is cloned, some libraries need to be installed

``` bash
import os
import sys

cwd = os.getcwd()
tool_path = f"{cwd}/ParFlowCLM_DE06_data_extraction_tool"
sys.path.append(tool_path)
```
### Note
For running the tool other packages should be installed as well:

- numpy
- netCDF4
- datetime 
- csv 
- json 

For more information on how to install packages follow the steps available here: https://packaging.python.org/en/latest/tutorials/installing-packages/

## Running the script
 To run the script you will need two files:
 1. Input file : this is a JSON file which includes information on the dataset you want to extract from. For an example please check ../examples.
    the file should include the following infromation:
    ``` bash
      [
        { 
          "stationID": " ",
          "stationLat":  ,
          "stationLon": ,
          "ParFlowData": " ",
          "Depth": 
        }
      ]  
     ```

   stationID: name for your station/location\
   stationLat, stationLon: latitude and longitude of the station/location\
   ParFlowData : the path to the dataset in the THREDDS server, or where the dataset is saved\
   Depth: the needed depth 

2. The indicator file "DE-0055_INDICATOR_regridded_rescaled_SoilGrids250-v2017_BGRvector_newAllv.nc". the file is available under ../data
   This dataset is used to extract the latidudes and longitudes, and also it is important to ensure that the selected location does not fall directly in a water body.
   
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



### Note:

- The simulations are calculated for 15 layers from the surface to 60m depth in mm water column each depth represents the lower boundary of the layer, their thickness varies with depth. The depths (in meters) are available as follows: 60.0, 42.0, 27.0, 17.0, 7.0, 3.0, 2.0, 1.3, 0.8, 0.5, 0.3,0.17, 0.1, 0.05, 0.02. If the depth inserted as input falls between two layer, the data extracted will be for the lower boundary of the layer. 
