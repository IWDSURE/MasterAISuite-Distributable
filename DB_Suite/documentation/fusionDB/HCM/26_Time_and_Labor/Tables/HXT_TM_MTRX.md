# HXT_TM_MTRX

This is the table which represents the building blocks of a timecard MTRX row. This doesn't include the additional row attributes.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttmmtrx-18557.html#hxttmmtrx-18557](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttmmtrx-18557.html#hxttmmtrx-18557)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_TM_MTRX_PK | TM_MTRX_ROW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_MTRX_ROW_ID | NUMBER |  | 18 | Yes | Primary Key |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| TM_HEADER_ID | NUMBER |  | 18 | Yes | Foriegn key to HXT_TM_HEADER. |
| BLD_BLK_TYPE | VARCHAR2 | 150 |  | Yes | Whether the timecard MTRX row represents a RANGE or a MEASURE entry. |
| UNIT_OF_MEASURE | VARCHAR2 | 150 |  | Yes | Denotes the Unit of Measure. Possible values HOURS or DAYS. |
| DISPLAY_SEQUENCE | NUMBER |  | 18 |  | The sequence in which the rows are inserted. |
| DAILY_COMMENT_HAS_DATA_FLAG | VARCHAR2 | 1 |  |  | DAILY_COMMENT_HAS_DATA_FLAG |
| CALCULATED_FLAG | VARCHAR2 | 1 |  |  | This flag indicates whether this matrix row stores processed  data. |
| TC_START_DATE | TIMESTAMP |  |  |  | TC_START_DATE |
| TC_END_DATE | TIMESTAMP |  |  |  | TC_END_DATE |
| RESOURCE_ID | NUMBER |  | 18 |  | RESOURCE_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | BUSINESS_UNIT_ID |
| MEASURE1 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE2 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE3 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE4 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE5 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE6 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE7 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE8 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE9 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE10 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE11 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE12 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE13 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE14 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE15 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE16 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE17 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE18 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE19 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE20 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE21 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE22 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE23 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE24 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE25 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE26 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE27 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE28 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE29 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE30 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| MEASURE31 | NUMBER |  |  |  | Holds the measure detail for the timecard MTRX row. The columns would be populate if the BLD_BLK_TYPE is MEASURE. |
| START_TIME1 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME2 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME3 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME4 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME5 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME6 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME7 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME8 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME9 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME10 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME11 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME12 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME13 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME14 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME15 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME16 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME17 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME18 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME19 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME20 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME21 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME22 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME23 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME24 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME25 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME26 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME27 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME28 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME29 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME30 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| START_TIME31 | TIMESTAMP |  |  |  | Holds the Start Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME1 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME2 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME3 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME4 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME5 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME6 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME7 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME8 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME9 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME10 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME11 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME12 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME13 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME14 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME15 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME16 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME17 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME18 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME19 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME20 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME21 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME22 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME23 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME24 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME25 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME26 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME27 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME28 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME29 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME30 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| STOP_TIME31 | TIMESTAMP |  |  |  | Holds the Stop Time information for the building blocks. The columns would be populate if the BLD_BLK_TYPE is RANGE. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 150 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE_CHAR1 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR1_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR1_VALUE |
| ATTRIBUTE_CHAR2 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR2_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR2_VALUE |
| ATTRIBUTE_CHAR3 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR3_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR3_VALUE |
| ATTRIBUTE_CHAR4 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR4_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR4_VALUE |
| ATTRIBUTE_CHAR5 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR5_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR5_VALUE |
| ATTRIBUTE_CHAR6 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR6_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR6_VALUE |
| ATTRIBUTE_CHAR7 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR7_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR7_VALUE |
| ATTRIBUTE_CHAR8 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR8_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR8_VALUE |
| ATTRIBUTE_CHAR9 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR9_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR9_VALUE |
| ATTRIBUTE_CHAR10 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR10_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR10_VALUE |
| ATTRIBUTE_CHAR11 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR11_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR11_VALUE |
| ATTRIBUTE_CHAR12 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR12_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR12_VALUE |
| ATTRIBUTE_CHAR13 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR13_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR13_VALUE |
| ATTRIBUTE_CHAR14 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR14_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR14_VALUE |
| ATTRIBUTE_CHAR15 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR15_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR15_VALUE |
| ATTRIBUTE_CHAR16 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR16_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR16_VALUE |
| ATTRIBUTE_CHAR17 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR17_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR17_VALUE |
| ATTRIBUTE_CHAR18 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR18_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR18_VALUE |
| ATTRIBUTE_CHAR19 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR19_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR19_VALUE |
| ATTRIBUTE_CHAR20 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR20_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR20_VALUE |
| ATTRIBUTE_CHAR21 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR21_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR21_VALUE |
| ATTRIBUTE_CHAR22 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR22_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR22_VALUE |
| ATTRIBUTE_CHAR23 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR23_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR23_VALUE |
| ATTRIBUTE_CHAR24 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR24_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR24_VALUE |
| ATTRIBUTE_CHAR25 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR25_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR25_VALUE |
| ATTRIBUTE_CHAR26 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR26_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR26_VALUE |
| ATTRIBUTE_CHAR27 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR27_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR27_VALUE |
| ATTRIBUTE_CHAR28 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR28_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR28_VALUE |
| ATTRIBUTE_CHAR29 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR29_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR29_VALUE |
| ATTRIBUTE_CHAR30 | VARCHAR2 | 350 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR30_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_CHAR30_VALUE |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER1_VALUE |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER2_VALUE |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER3_VALUE |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER4_VALUE |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER5_VALUE |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER6_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER6_VALUE |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER7_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER7_VALUE |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER8_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER8_VALUE |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER9_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER9_VALUE |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER10_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER10_VALUE |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER11_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER11_VALUE |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER12_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER12_VALUE |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER13_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER13_VALUE |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER14_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER14_VALUE |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER15_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER15_VALUE |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER16_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER16_VALUE |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER17_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER17_VALUE |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER18_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER18_VALUE |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER19_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER19_VALUE |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER20_VALUE | VARCHAR2 | 350 |  |  | ATTRIBUTE_NUMBER20_VALUE |
| ATTRIBUTE_ALT_NAME1 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME1 |
| ATTRIBUTE_ALT_NAME1_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME1_VALUE |
| ATTRIBUTE_ALT_NAME2 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME2 |
| ATTRIBUTE_ALT_NAME2_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME2_VALUE |
| ATTRIBUTE_ALT_NAME3 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME3 |
| ATTRIBUTE_ALT_NAME3_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME3_VALUE |
| ATTRIBUTE_ALT_NAME4 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME4 |
| ATTRIBUTE_ALT_NAME4_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME4_VALUE |
| ATTRIBUTE_ALT_NAME5 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME5 |
| ATTRIBUTE_ALT_NAME5_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME5_VALUE |
| ATTRIBUTE_ALT_NAME6 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME6 |
| ATTRIBUTE_ALT_NAME6_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME6_VALUE |
| ATTRIBUTE_ALT_NAME7 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME7 |
| ATTRIBUTE_ALT_NAME7_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME7_VALUE |
| ATTRIBUTE_ALT_NAME8 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME8 |
| ATTRIBUTE_ALT_NAME8_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME8_VALUE |
| ATTRIBUTE_ALT_NAME9 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME9 |
| ATTRIBUTE_ALT_NAME9_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME9_VALUE |
| ATTRIBUTE_ALT_NAME10 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME10 |
| ATTRIBUTE_ALT_NAME10_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME10_VALUE |
| ATTRIBUTE_ALT_NAME11 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME11 |
| ATTRIBUTE_ALT_NAME11_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME11_VALUE |
| ATTRIBUTE_ALT_NAME12 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME12 |
| ATTRIBUTE_ALT_NAME12_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME12_VALUE |
| ATTRIBUTE_ALT_NAME13 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME13 |
| ATTRIBUTE_ALT_NAME13_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME13_VALUE |
| ATTRIBUTE_ALT_NAME14 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME14 |
| ATTRIBUTE_ALT_NAME14_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME14_VALUE |
| ATTRIBUTE_ALT_NAME15 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME15 |
| ATTRIBUTE_ALT_NAME15_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME15_VALUE |
| ATTRIBUTE_ALT_NAME16 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME16 |
| ATTRIBUTE_ALT_NAME16_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME16_VALUE |
| ATTRIBUTE_ALT_NAME17 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME17 |
| ATTRIBUTE_ALT_NAME17_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME17_VALUE |
| ATTRIBUTE_ALT_NAME18 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME18 |
| ATTRIBUTE_ALT_NAME18_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME18_VALUE |
| ATTRIBUTE_ALT_NAME19 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME19 |
| ATTRIBUTE_ALT_NAME19_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME19_VALUE |
| ATTRIBUTE_ALT_NAME20 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME20 |
| ATTRIBUTE_ALT_NAME20_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME20_VALUE |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE1_VALUE |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE2_VALUE |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE3_VALUE |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE4_VALUE |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE5_VALUE |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE6_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE6_VALUE |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE7_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE7_VALUE |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE8_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE8_VALUE |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE9_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE9_VALUE |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE10_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE10_VALUE |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE11_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE11_VALUE |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE12_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE12_VALUE |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE13_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE13_VALUE |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE14_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE14_VALUE |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE15_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE15_VALUE |
| TM_MTRX_ROW_CD | VARCHAR2 | 20 |  |  | Alternate key |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_TM_MTRX_N1 | Non Unique | Default | TM_HEADER_ID |
| HXT_TM_MTRX_N2 | Non Unique | Default | RESOURCE_ID |
| HXT_TM_MTRX_PK | Unique | Default | TM_MTRX_ROW_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
