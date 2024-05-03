# Getting started

This repository includes scripts and examples to extract time-series or variables for a specific location from ParFlowCLM DE06 simulations (https://adapter-projekt.org/). Selected variables are available on THREDDS-server (https://service.tereno.net/thredds/catalog/forecastnrw/products/catalog.html). 

This tool is designed to be able to exract information from ParFlowCLM DE06 for a location without having to download the data.

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
## Running the script
 To run the script you will need two files:
 1. Input file : this is a json file which includes information on the dataset you want to extract from. For an example please check ../examples.
    the file should include the data below:
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

stationID: enter a name for your station/location\
stationLat, stationLon: latidue and longitude of the station/location\
ParFlowData : the path to the dataset in the THREDDS server\

###The figures below demonstrates an example on how to access the path for the climatology of plant available water dataset\

![Thredds_server_1](https://github.com/suadha93/ParFlow_data_extraction_tool/assets/139210041/25ebd9c1-7df8-4461-946c-2e93d4aa4dcf)



2. The indicator file "DE-0055_INDICATOR_regridded_rescaled_SoilGrids250-v2017_BGRvector_newAllv.nc". the file is available under ../data
   This dataset is used to extract the latidudes and longitudes, and also it is important to ensure that the selected location does not fall directly in a water body.


### Notes

- The simulations are calculated for 15 layers from the surface to 60m depth in mm water column each depth represents the lower boundary of the layer, their thickness varies with depth. The depths (in meters) are available as follows: 60.0, 42.0, 27.0, 17.0, 7.0, 3.0, 2.0, 1.3, 0.8, 0.5, 0.3,0.17, 0.1, 0.05, 0.02. If the depth inserted as input falls between two layer, the data extracted will be for the lower boundary of the layer. 
