This directory contains information on weather data file
formats of the Cumulus grapher by SandaySoft. See the
wiki at http://wiki.sandaysoft.com/a/Category:Log_Files

Fields on the data/dayfile.txt
    00 (A): Date as 2 figure day [separator] 2 figure month [separator] 2 figure year 
	   - the separator is that set in the windows system short date format (see setup)
    01 (B): Highest wind gust
    02 (C): Bearing of highest wind gust (integer)
    03 (D): Time of highest wind gust
    04 (E): Minimum temperature
    05 (F): Time of minimum temperature
    06 (G): Maximum temperature
    07 (H): Time of maximum temperature
    08 (I): Minimum sea level pressure
    09 (J): Time of minimum pressure
    10 (K): Maximum sea level pressure
    11 (L): Time of maximum pressure
    12 (M): Maximum rainfall rate
    13 (N): Time of maximum rainfall rate
    14 (O): Total rainfall for the day
    15 (P): Average temperature for the day 

(This point represents the minimum length of all records)

    16 (Q): Total wind run
    17 (R): Highest Average Wind Speed
    18 (S): Time of Highest Avg. Wind speed
    19 (T): Lowest humidity (integer)
    20 (U): Time of lowest humidity
    21 (V): Highest humidity (integer)
    22 (W): Time of highest humidity
    23 (X): Total evapotranspiration (Only valid for Davis stations, shows zero otherwise)
    24 (Y): Total hours of sunshine (only valid if sunshine sensor connnected)
    25 (Z): High Heat index
    26 (AA): Time of high heat index
    27 (AB): High Apparent temperature
    28 (AC): Time of high apparent temperature
    29 (AD): Low apparent temperature
    30 (AE): Time of low apparent temperature
    31 (AF): High hourly rain
    32 (AG): Time of high hourly rain
    33 (AH): Low wind chill
    34 (AI): Time of low wind chill
    35 (AJ): High dew point
    36 (AK): Time of high dew point
    37 (AL): Low dew point
    38 (AM): Time of low dew point 

The next 3 entries were added in version 1.9.2 Build 1004

    39 (AN): Today's dominant/average wind direction (integer)
    40 (AO): Heating degree days
    41 (AP): Cooling degree days 

Added in version 1.9.3 build 1036 (these only show valid values if appropriate sensors exist)

    42 (AQ): High solar radiation
    43 (AR): Time of high solar radiation
    44 (AS): High UV Index
    45 (AT): Time of high UV Index 

Example data
01/08/11,19.3,61,10:22,12.5,06:58,23.8,14:49,1014.26,20:46,1018.83,09:28,0.0,00:00,0.0,17.8,21.6,4.6,10:44,36,14:14,86,01:56,3.56,8.9,23.8,14:49,23.1,14:50,12.3,06:59,0.0,00:00,12.5,06:58,11.3,00:16,6.9,14:34,354,2.0,1.5
02/08/11,16.1,20,16:55,14.7,06:45,24.2,13:54,1013.79,19:13,1015.65,11:14,0.0,00:00,0.0,18.9,13.7,8.0,15:55,42,20:42,85,06:50,2.79,4.9,24.2,13:54,24.3,13:55,15.1,06:40,0.0,00:00,14.7,06:45,14.8,11:59,7.0,21:09,57,1.0,1.7
03/08/11,14.5,36,17:23,14.9,05:50,24.6,14:46,1012.70,18:44,1015.99,08:34,0.0,00:00,0.0,19.4,17.2,4.8,16:04,50,14:38,79,07:04,3.05,5.8,24.6,14:46,25.4,14:47,15.0,05:50,0.0,00:00,14.9,05:50,14.2,20:01,8.9,00:16,32,0.8,1.9
04/08/11,17.7,16,15:43,14.1,06:20,25.3,15:06,1013.08,18:42,1015.31,08:28,0.0,00:00,0.0,20.2,19.4,8.1,14:12,52,18:20,92,06:55,3.30,9.1,25.3,15:06,26.8,14:55,14.9,06:20,0.0,00:00,14.1,06:20,15.8,14:55,12.5,06:25,36,1.0,2.9
05/08/11,16.1,32,12:52,14.2,06:12,22.2,14:07,1013.89,00:01,1016.36,09:43,0.0,00:00,0.0,18.6,21.6,5.2,13:00,62,15:57,87,06:11,3.30,8.4,22.2,14:07,23.5,14:10,14.8,07:19,0.0,00:00,14.2,06:12,15.4,10:33,12.0,06:03,34,0.9,1.3
06/08/11,16.1,309,11:15,14.3,05:29,22.4,17:12,1014.46,20:02,1016.97,10:38,0.0,00:00,0.0,18.4,19.2,5.5,16:21,55,13:33,92,05:20,2.79,7.9,22.4,17:12,23.3,18:17,15.1,06:09,0.0,00:00,14.3,05:29,14.2,18:12,10.9,10:38,32,1.1,1.3
07/08/11,17.7,342,13:24,12.9,05:47,24.1,14:53,1013.92,19:49,1016.43,09:36,0.0,00:00,0.0,18.4,19.1,6.3,14:06,48,12:45,89,05:36,3.30,9.0,24.1,14:53,24.6,15:48,13.3,05:47,0.0,00:00,12.9,05:47,14.6,15:52,10.7,11:33,11,1.6,1.7