"""
    swipos Service API

     ![](https://api3.geo.admin.ch/_static/bg_header_logo.png) *** The swipos Service API provides tools for interfacing with the Swiss Positioning Service swipos. This is the main documentation which includes all the API documentation for developers.  At the moment, the swipos Service API only consists of the RINEX API. More APIs might be added at a later time.  # RINEX  The swipos RINEX API offers an interface to the AGNES station information and their RINEX data. RINEX data is available for full hours, or it can be requested for a desired duration. Via the API, you can request RINEX data for the last 100 days.  When using the API, the following conventions apply:  ## Time Dates, times and durations are expressed in a swisstopo-created custom format that is based on **ISO 8601**.  GPS time is usually given in seconds, and is related to the international atomic time (TAI). This differs from the Universal Time Coordinated (UTC), which is kept synchronized to the earth's rotation by leap seconds. The relation can be expressed as *GPSTime = UTC + 18s*  To simplify the use of the API, we kept the formats proposed in ISO 8601, and added **G** as a timezone indicator instead of the **Z** used for UTC time. Times that do not end with **G** are treated as having invalid format.  The API accepts only durations of up to 6 hours, so all durations must start with PT (period, time), followed by the duration in hours and/or minutes.  If requesting an hour file, it is enough to fill the hour; it is not necessary to give minutes or seconds.  **Examples:**  - basic format: `yyyyMMddThhmmG / 20200821T1313G` OR `yyyMMddThhG / 20210217T05G` - extended format: `yyyy-MM-ddThh:mmG / 2020-08-21T13:13G` - duration (in hours, minutes): `PTnHmmM / PT3H30M`  As of now, times without the timezone G will not be considered valid times.   ### Epochs The RINEX data is recorded at the base station and will be sent every hour to the swipos servers. One hour file contains 3600 epochs if all recordings were successful. An hour file will be available around 20 minutes after the hour has ended.  Please note, that the delivered RINEX files may not contain 100% of the epochs due to recording issues.  ## Coordinate system Unless otherwise stated, the RINEX API uses latitude and longitude in decimal degrees in the **ETRS89** reference system.  **Example:**   `46.28310, 7.53854`  **Note:** The coordinates in the base station information are to be used for representation only, they are not intended for geodetic calculations. The geocentric coordinates contained in the RINEX file as approximate position can be used as precise coordinates.  ## RINEX 3.03 format The delivered RINEX format is 3.03 with 1 second sampling rate as recorded at the base station. To manipulate the RINEX, the RINEX GNSS Data Conversion and Manipulation Toolbox \"gfzrnx\" is used: Nischan,  Thomas  (2016):  GFZRNX  -  RINEX  GNSS  Data  Conversion  and  Manipulation  Toolbox. [GFZ  DataServices](http://dx.doi.org/10.5880/GFZ.1.1.2016.002)  The RINEX files are compressed with [hananaka](https://terras.gsi.go.jp/ja/crx2rnx.html). The download includes both the observation and navigation files.   ## Station code The base station is always identified by its 4 character station code, which is case sensitive and must use capital letters, as returned by the /list endpoint.  **Example:**   `ZIM2`  ## Authentication  The API uses basic authentication for all calls.  ## API specification The api specification was defined as openapi version 3.0.0 [openapi spec](https://github.com/OAI/OpenAPI-Specification/).   Here you can find the current developement api specification [api-docs.yml](https://swipos-dev-apidoc.s3.eu-central-1.amazonaws.com/api-docs.yml).   Here you can find the current productive api specification [api-docs.yml](https://swipos-apidoc.s3.eu-central-1.amazonaws.com/api-docs.yml).   To generate clients use [openapi-generator](https://openapi-generator.tech/).   swisstopo offers no support for client implementations. This is a test release.  ### Versioning Versions are named after plants. Version are alphabetically sorted, where letters later in the alphabet corresnpond with a version published later in time. For minor releases, the second or third letter of the name is significant.  **Examples:**  - `acacia` - 1st release - `aconite` - 1st minor release - `babysbreath` - 2nd release   # noqa: E501

    The version of the OpenAPI document: acacia
    Contact: swipos@swisstopo.ch
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.request_data import RequestData


class TestRequestData(unittest.TestCase):
    """RequestData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRequestData(self):
        """Test RequestData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RequestData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
