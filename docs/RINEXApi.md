# openapi_client.RINEXApi

All URIs are relative to *https://api.swipos-dev.ch/acacia*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](RINEXApi.md#list) | **GET** /rinex/station/list | Returns a list of all AGNES stations.
[**nearest**](RINEXApi.md#nearest) | **GET** /rinex/station/nearest | The base station object of the nearest active AGNES station.
[**request_data**](RINEXApi.md#request_data) | **POST** /rinex/station/request-data | Request up to 6 hours of rinex data from one AGNES station.
[**request_hour**](RINEXApi.md#request_hour) | **GET** /rinex/station/request-hour | Request an existing hour RINEX file for a station code.


# **list**
> [BaseStation] list()

Returns a list of all AGNES stations.

The request returns an array of BaseStation objects, which for each base station give the station code, postion and if the station is still operational.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import rinex_api
from openapi_client.model.base_station import BaseStation
from pprint import pprint
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

    # example, this endpoint has no required or optional parameters
    try:
        # Returns a list of all AGNES stations.
        api_response = api_instance.list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RINEXApi->list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[BaseStation]**](BaseStation.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nearest**
> NearestStation nearest(latitude, longitude)

The base station object of the nearest active AGNES station.

Specify a point and get the closest active AGNES station back. If no time arguments are supplied, returns nearest station without consideration if the station is operational at the moment or not. In case of 'time_from' argument, returns nearest station that was active at that moment. In case of 'time_from' and 'time_to' or 'period' arguments, returns a station with activity in described time frame.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import rinex_api
from openapi_client.model.error import Error
from openapi_client.model.nearest_station import NearestStation
from pprint import pprint
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
    latitude = 46.38851 # float | Latitude of your position. *Example 46.38851*
    longitude = 7.05977 # float | Longitude of your position. *Example 7.05977*
    time_from = "time_from_example" # str | Filter for stations that were operational starting at this time point (e.g. yyyy-MM-ddThh:00G or yyyyMMddThh00G) (optional)
    time_to = "time_to_example" # str | Filter for stations that were operational until this time point (e.g. yyyy-MM-ddThh:00G or yyyyMMddThh00G) (optional)

    # example passing only required values which don't have defaults set
    try:
        # The base station object of the nearest active AGNES station.
        api_response = api_instance.nearest(latitude, longitude)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RINEXApi->nearest: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # The base station object of the nearest active AGNES station.
        api_response = api_instance.nearest(latitude, longitude, time_from=time_from, time_to=time_to)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RINEXApi->nearest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **float**| Latitude of your position. *Example 46.38851* |
 **longitude** | **float**| Longitude of your position. *Example 7.05977* |
 **time_from** | **str**| Filter for stations that were operational starting at this time point (e.g. yyyy-MM-ddThh:00G or yyyyMMddThh00G) | [optional]
 **time_to** | **str**| Filter for stations that were operational until this time point (e.g. yyyy-MM-ddThh:00G or yyyyMMddThh00G) | [optional]

### Return type

[**NearestStation**](NearestStation.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A base station object and its distance to your position |  -  |
**400** | Bad Request. Possible reasons are  102 - No base station for given criteria  103 - Invalid latitude or longitude format  104 - No parameters given  108 - Mandatory parameter &#39;latitude&#39; is missing. OR Mandatory parameter &#39;longitude&#39; is missing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_data**
> ScheduledRequest request_data(request_data)

Request up to 6 hours of rinex data from one AGNES station.

Use this you need data from more than one RINEX hour files. For requesting, you need the AGNES station code as well as the starting date and time. You can either give a duration or an end time. The result will be submitted to the provided callback url. **Note** One request can handle a maximum of 6 hours at once. If you need one hour only, use 'request-hour' instead.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import rinex_api
from openapi_client.model.scheduled_request import ScheduledRequest
from openapi_client.model.error import Error
from openapi_client.model.request_data import RequestData
from pprint import pprint
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
    request_data = RequestData(
        station_code="AIGE",
        time_from="2020-08-17T13:00G",
        time_to="2020-08-17T13:23G",
        duration="PT23M",
        callback_url="https://myserver.com/send/callback/here",
        include_log="true",
        observation_only="true",
    ) # RequestData | 

    # example passing only required values which don't have defaults set
    try:
        # Request up to 6 hours of rinex data from one AGNES station.
        api_response = api_instance.request_data(request_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RINEXApi->request_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_data** | [**RequestData**](RequestData.md)|  |

### Return type

[**ScheduledRequest**](ScheduledRequest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | An object representing a scheduled request. |  -  |
**400** | Bad Request. Possible reasons are  101 - Could not create url on s3  104 - There are no params at all  105 - Can not get data for time in future (or this recent)  106 - No base station data for given time and station code  107 - Field &#39;time_from&#39; or &#39;time_to&#39; is not of proper format / Duration is not a valid ISO8601 value / Mandatory field &#39;station_code&#39; is not of length 4  108 - Mandatory field &#39;time_from&#39;, &#39;duration&#39; or &#39;station_code&#39; is missing  109 - One of fields &#39;time_from&#39;,&#39;time_to&#39; or &#39;duration&#39; is not of proper format  110 - Duration is less than allowed minimum  111 - Duration is greater than allowed maximum  113 - Can not get data for period in future (or this recent)  114 - Time frame must be within a single day  115 - Invalid callback url  116 - Invalid email format  117 - Could not queue a task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_hour**
> file_type request_hour(station_code, time)

Request an existing hour RINEX file for a station code.

Request the hour file from a station with the station_code (eg. SAA2) and hour (eg. \"2020-08-17T13:00G\" or \"2020081713G\"). The endpoint will return the coresponding rinex hour file. *Note* The hour file is written in GPS time, so has 18s offset to UTC times. Use this if you need a full hour.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import rinex_api
from openapi_client.model.error import Error
from pprint import pprint
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
    station_code = "station_code_example" # str | Station code
    time = "time_example" # str | Requesting hour starting at (e.g. yyyy-MM-ddThh:00G or yyyyMMddThh00G)

    # example passing only required values which don't have defaults set
    try:
        # Request an existing hour RINEX file for a station code.
        api_response = api_instance.request_hour(station_code, time)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RINEXApi->request_hour: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_code** | **str**| Station code |
 **time** | **str**| Requesting hour starting at (e.g. yyyy-MM-ddThh:00G or yyyyMMddThh00G) |

### Return type

**file_type**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: octet_stream/zip, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A RINEX file. |  -  |
**400** | Bad Request. Possible reasons are  104 - There are no params at all  105 - Can not get data for time in future (or this recent)  106 - No base station data for given time and station code  107 - Mandatory field &#39;station_code&#39; must be 4 capital letters and/or mandatory field &#39;time&#39; is not given as yyyy-mm-ddThh:mmG or yyyymmddhhmmG  108 - Mandatory field &#39;station_code&#39; and/or &#39;time&#39; is missing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

