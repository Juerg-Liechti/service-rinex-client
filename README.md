# openapi-client

![](https://api3.geo.admin.ch/_static/bg_header_logo.png)
***
The swipos Service API provides tools for interfacing with the Swiss Positioning Service swipos.
This is the main documentation which includes all the API documentation for developers.

At the moment, the swipos Service API only consists of the RINEX API. More APIs might be added at a later time.

# RINEX

The swipos RINEX API offers an interface to the AGNES station information and their RINEX data. RINEX data is available for full hours, or it can be requested for a desired duration. Via the API, you can request RINEX data for the last 100 days.

When using the API, the following conventions apply:

## Time
Dates, times and durations are expressed in a swisstopo-created custom format that is based on **ISO 8601**.

GPS time is usually given in seconds, and is related to the international atomic time (TAI). This differs from the Universal Time Coordinated (UTC), which is kept synchronized to the earth's rotation by leap seconds. The relation can be expressed as *GPSTime = UTC + 18s*

To simplify the use of the API, we kept the formats proposed in ISO 8601, and added **G** as a timezone indicator instead of the **Z** used for UTC time. Times that do not end with **G** are treated as having invalid format.

The API accepts only durations of up to 6 hours, so all durations must start with PT (period, time), followed by the duration in hours and/or minutes.

If requesting an hour file, it is enough to fill the hour; it is not necessary to give minutes or seconds.

**Examples:**

- basic format: `yyyyMMddThhmmG / 20200821T1313G` OR `yyyMMddThhG / 20210217T05G`
- extended format: `yyyy-MM-ddThh:mmG / 2020-08-21T13:13G`
- duration (in hours, minutes): `PTnHmmM / PT3H30M`

As of now, times without the timezone G will not be considered valid times.


### Epochs
The RINEX data is recorded at the base station and will be sent every hour to the swipos servers. One hour file contains 3600 epochs if all recordings were successful. An hour file will be available around 20 minutes after the hour has ended.

Please note, that the delivered RINEX files may not contain 100% of the epochs due to recording issues.

## Coordinate system
Unless otherwise stated, the RINEX API uses latitude and longitude in decimal degrees in the **ETRS89** reference system.

**Example:**
  `46.28310, 7.53854`

**Note:** The coordinates in the base station information are to be used for representation only, they are not intended for geodetic calculations. The geocentric coordinates contained in the RINEX file as approximate position can be used as precise coordinates.

## RINEX 3.03 format
The delivered RINEX format is 3.03 with 1 second sampling rate as recorded at the base station.
To manipulate the RINEX, the RINEX GNSS Data Conversion and Manipulation Toolbox \"gfzrnx\" is used:
Nischan,  Thomas  (2016):  GFZRNX  -  RINEX  GNSS  Data  Conversion  and  Manipulation  Toolbox.
[GFZ  DataServices](http://dx.doi.org/10.5880/GFZ.1.1.2016.002)

The RINEX files are compressed with [hananaka](https://terras.gsi.go.jp/ja/crx2rnx.html). The download includes both the observation and navigation files.


## Station code
The base station is always identified by its 4 character station code, which is case sensitive and must use capital letters, as returned by the /list endpoint.

**Example:**
  `ZIM2`

## Authentication

The API uses basic authentication for all calls.

## API specification
The api specification was defined as openapi version 3.0.0 [openapi spec](https://github.com/OAI/OpenAPI-Specification/).  
Here you can find the current developement api specification [api-docs.yml](https://swipos-dev-apidoc.s3.eu-central-1.amazonaws.com/api-docs.yml).  
Here you can find the current productive api specification [api-docs.yml](https://swipos-apidoc.s3.eu-central-1.amazonaws.com/api-docs.yml).  
To generate clients use [openapi-generator](https://openapi-generator.tech/).


swisstopo offers no support for client implementations.
This is a test release.

### Versioning
Versions are named after plants. Version are alphabetically sorted, where letters later in the alphabet corresnpond with a version published later in time. For minor releases, the second or third letter of the name is significant.

**Examples:**

- `acacia` - 1st release
- `aconite` - 1st minor release
- `babysbreath` - 2nd release


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: acacia
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://swisstopo.ch/swipos](https://swisstopo.ch/swipos)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from pprint import pprint
from openapi_client.api import rinex_api
from openapi_client.model.base_station import BaseStation
from openapi_client.model.error import Error
from openapi_client.model.nearest_station import NearestStation
from openapi_client.model.request_data import RequestData
from openapi_client.model.scheduled_request import ScheduledRequest
# Defining the host is optional and defaults to https://api.swipos-dev.ch/acacia
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.swipos-dev.ch/acacia"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rinex_api.RINEXApi(api_client)
    
    try:
        # Returns a list of all AGNES stations.
        api_response = api_instance.list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RINEXApi->list: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.swipos-dev.ch/acacia*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RINEXApi* | [**list**](docs/RINEXApi.md#list) | **GET** /rinex/station/list | Returns a list of all AGNES stations.
*RINEXApi* | [**nearest**](docs/RINEXApi.md#nearest) | **GET** /rinex/station/nearest | The base station object of the nearest active AGNES station.
*RINEXApi* | [**request_data**](docs/RINEXApi.md#request_data) | **POST** /rinex/station/request-data | Request up to 6 hours of rinex data from one AGNES station.
*RINEXApi* | [**request_hour**](docs/RINEXApi.md#request_hour) | **GET** /rinex/station/request-hour | Request an existing hour RINEX file for a station code.


## Documentation For Models

 - [BaseStation](docs/BaseStation.md)
 - [CallbackAnswer](docs/CallbackAnswer.md)
 - [Error](docs/Error.md)
 - [NearestStation](docs/NearestStation.md)
 - [RequestData](docs/RequestData.md)
 - [ScheduledRequest](docs/ScheduledRequest.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author

swipos@swisstopo.ch


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in openapi_client.apis and openapi_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from openapi_client.api.default_api import DefaultApi`
- `from openapi_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import openapi_client
from openapi_client.apis import *
from openapi_client.models import *
```

