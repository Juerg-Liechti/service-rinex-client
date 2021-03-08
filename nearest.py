import time
import openapi_client
from openapi_client.api import rinex_api
from openapi_client.model.error import Error
from openapi_client.model.nearest_station import NearestStation
from pprint import pprint
# Defining the host is optional and defaults to https://api.swipos-dev.ch/acacia
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.swipos.ch/acacia"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'rinex',
    password = ''
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rinex_api.RINEXApi(api_client)
    latitude = 46.38851 # float | Latitude of your position. *Example 46.38851*
    longitude = 7.05977 # float | Longitude of your position. *Example 7.05977*
    time_from = "2020-12-12T12:00G" 
    time_to = "2020-12-12T12:00G" # str | Filter for stations that were operational until this time point (e.g. yyyy-MM-ddThh:00G or yyyyMMddThh00G) (optional)

    # example passing only required values which don't have defaults set
    try:
        # The base station object of the nearest active AGNES station.
        api_response = api_instance.nearest(latitude, longitude, time_from=time_from, time_to=time_to)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RINEXApi->nearest: %s\n" % e)
