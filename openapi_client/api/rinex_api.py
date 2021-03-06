"""
    swipos Service API

     ![](https://api3.geo.admin.ch/_static/bg_header_logo.png) *** The swipos Service API provides tools for interfacing with the Swiss Positioning Service swipos. This is the main documentation which includes all the API documentation for developers.  At the moment, the swipos Service API only consists of the RINEX API. More APIs might be added at a later time.  # RINEX  The swipos RINEX API offers an interface to the AGNES station information and their RINEX data. RINEX data is available for full hours, or it can be requested for a desired duration. Via the API, you can request RINEX data for the last 100 days.  When using the API, the following conventions apply:  ## Time Dates, times and durations are expressed in a swisstopo-created custom format that is based on **ISO 8601**.  GPS time is usually given in seconds, and is related to the international atomic time (TAI). This differs from the Universal Time Coordinated (UTC), which is kept synchronized to the earth's rotation by leap seconds. The relation can be expressed as *GPSTime = UTC + 18s*  To simplify the use of the API, we kept the formats proposed in ISO 8601, and added **G** as a timezone indicator instead of the **Z** used for UTC time. Times that do not end with **G** are treated as having invalid format.  The API accepts only durations of up to 6 hours, so all durations must start with PT (period, time), followed by the duration in hours and/or minutes.  If requesting an hour file, it is enough to fill the hour; it is not necessary to give minutes or seconds.  **Examples:**  - basic format: `yyyyMMddThhmmG / 20200821T1313G` OR `yyyMMddThhG / 20210217T05G` - extended format: `yyyy-MM-ddThh:mmG / 2020-08-21T13:13G` - duration (in hours, minutes): `PTnHmmM / PT3H30M`  As of now, times without the timezone G will not be considered valid times.   ### Epochs The RINEX data is recorded at the base station and will be sent every hour to the swipos servers. One hour file contains 3600 epochs if all recordings were successful. An hour file will be available around 20 minutes after the hour has ended.  Please note, that the delivered RINEX files may not contain 100% of the epochs due to recording issues.  ## Coordinate system Unless otherwise stated, the RINEX API uses latitude and longitude in decimal degrees in the **ETRS89** reference system.  **Example:**   `46.28310, 7.53854`  **Note:** The coordinates in the base station information are to be used for representation only, they are not intended for geodetic calculations. The geocentric coordinates contained in the RINEX file as approximate position can be used as precise coordinates.  ## RINEX 3.03 format The delivered RINEX format is 3.03 with 1 second sampling rate as recorded at the base station. To manipulate the RINEX, the RINEX GNSS Data Conversion and Manipulation Toolbox \"gfzrnx\" is used: Nischan,  Thomas  (2016):  GFZRNX  -  RINEX  GNSS  Data  Conversion  and  Manipulation  Toolbox. [GFZ  DataServices](http://dx.doi.org/10.5880/GFZ.1.1.2016.002)  The RINEX files are compressed with [hananaka](https://terras.gsi.go.jp/ja/crx2rnx.html). The download includes both the observation and navigation files.   ## Station code The base station is always identified by its 4 character station code, which is case sensitive and must use capital letters, as returned by the /list endpoint.  **Example:**   `ZIM2`  ## Authentication  The API uses basic authentication for all calls.  ## API specification The api specification was defined as openapi version 3.0.0 [openapi spec](https://github.com/OAI/OpenAPI-Specification/).   Here you can find the current developement api specification [api-docs.yml](https://swipos-dev-apidoc.s3.eu-central-1.amazonaws.com/api-docs.yml).   Here you can find the current productive api specification [api-docs.yml](https://swipos-apidoc.s3.eu-central-1.amazonaws.com/api-docs.yml).   To generate clients use [openapi-generator](https://openapi-generator.tech/).   swisstopo offers no support for client implementations. This is a test release.  ### Versioning Versions are named after plants. Version are alphabetically sorted, where letters later in the alphabet corresnpond with a version published later in time. For minor releases, the second or third letter of the name is significant.  **Examples:**  - `acacia` - 1st release - `aconite` - 1st minor release - `babysbreath` - 2nd release   # noqa: E501

    The version of the OpenAPI document: acacia
    Contact: swipos@swisstopo.ch
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.base_station import BaseStation
from openapi_client.model.error import Error
from openapi_client.model.nearest_station import NearestStation
from openapi_client.model.request_data import RequestData
from openapi_client.model.scheduled_request import ScheduledRequest


class RINEXApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __list(
            self,
            **kwargs
        ):
            """Returns a list of all AGNES stations.  # noqa: E501

            The request returns an array of BaseStation objects, which for each base station give the station code, postion and if the station is still operational.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [BaseStation]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.list = _Endpoint(
            settings={
                'response_type': ([BaseStation],),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/rinex/station/list',
                'operation_id': 'list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list
        )

        def __nearest(
            self,
            latitude,
            longitude,
            **kwargs
        ):
            """The base station object of the nearest active AGNES station.  # noqa: E501

            Specify a point and get the closest active AGNES station back. If no time arguments are supplied, returns nearest station without consideration if the station is operational at the moment or not. In case of 'time_from' argument, returns nearest station that was active at that moment. In case of 'time_from' and 'time_to' or 'period' arguments, returns a station with activity in described time frame.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.nearest(latitude, longitude, async_req=True)
            >>> result = thread.get()

            Args:
                latitude (float): Latitude of your position. *Example 46.38851*
                longitude (float): Longitude of your position. *Example 7.05977*

            Keyword Args:
                time_from (str): Filter for stations that were operational starting at this time point (e.g. yyyy-MM-ddThh:00G or yyyyMMddThh00G). [optional]
                time_to (str): Filter for stations that were operational until this time point (e.g. yyyy-MM-ddThh:00G or yyyyMMddThh00G). [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                NearestStation
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['latitude'] = \
                latitude
            kwargs['longitude'] = \
                longitude
            return self.call_with_http_info(**kwargs)

        self.nearest = _Endpoint(
            settings={
                'response_type': (NearestStation,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/rinex/station/nearest',
                'operation_id': 'nearest',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'latitude',
                    'longitude',
                    'time_from',
                    'time_to',
                ],
                'required': [
                    'latitude',
                    'longitude',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'latitude':
                        (float,),
                    'longitude':
                        (float,),
                    'time_from':
                        (str,),
                    'time_to':
                        (str,),
                },
                'attribute_map': {
                    'latitude': 'latitude',
                    'longitude': 'longitude',
                    'time_from': 'time_from',
                    'time_to': 'time_to',
                },
                'location_map': {
                    'latitude': 'query',
                    'longitude': 'query',
                    'time_from': 'query',
                    'time_to': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__nearest
        )

        def __request_data(
            self,
            request_data,
            **kwargs
        ):
            """Request up to 6 hours of rinex data from one AGNES station.  # noqa: E501

            Use this you need data from more than one RINEX hour files. For requesting, you need the AGNES station code as well as the starting date and time. You can either give a duration or an end time. The result will be submitted to the provided callback url. **Note** One request can handle a maximum of 6 hours at once. If you need one hour only, use 'request-hour' instead.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.request_data(request_data, async_req=True)
            >>> result = thread.get()

            Args:
                request_data (RequestData):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ScheduledRequest
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['request_data'] = \
                request_data
            return self.call_with_http_info(**kwargs)

        self.request_data = _Endpoint(
            settings={
                'response_type': (ScheduledRequest,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/rinex/station/request-data',
                'operation_id': 'request_data',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'request_data',
                ],
                'required': [
                    'request_data',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'request_data':
                        (RequestData,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'request_data': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__request_data
        )

        def __request_hour(
            self,
            station_code,
            time,
            **kwargs
        ):
            """Request an existing hour RINEX file for a station code.  # noqa: E501

            Request the hour file from a station with the station_code (eg. SAA2) and hour (eg. \"2020-08-17T13:00G\" or \"2020081713G\"). The endpoint will return the coresponding rinex hour file. *Note* The hour file is written in GPS time, so has 18s offset to UTC times. Use this if you need a full hour.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.request_hour(station_code, time, async_req=True)
            >>> result = thread.get()

            Args:
                station_code (str): Station code
                time (str): Requesting hour starting at (e.g. yyyy-MM-ddThh:00G or yyyyMMddThh00G)

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                file_type
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['station_code'] = \
                station_code
            kwargs['time'] = \
                time
            return self.call_with_http_info(**kwargs)

        self.request_hour = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/rinex/station/request-hour',
                'operation_id': 'request_hour',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'station_code',
                    'time',
                ],
                'required': [
                    'station_code',
                    'time',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'station_code':
                        (str,),
                    'time':
                        (str,),
                },
                'attribute_map': {
                    'station_code': 'station_code',
                    'time': 'time',
                },
                'location_map': {
                    'station_code': 'query',
                    'time': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'octet_stream/zip',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__request_hour
        )
