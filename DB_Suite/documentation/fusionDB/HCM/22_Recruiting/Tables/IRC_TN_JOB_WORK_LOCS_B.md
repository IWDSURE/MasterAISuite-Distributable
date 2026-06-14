# IRC_TN_JOB_WORK_LOCS_B

Table for storing the work location information of the requisition.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobworklocsb-7394.html#irctnjobworklocsb-7394](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobworklocsb-7394.html#irctnjobworklocsb-7394)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TN_JOB_WORK_LOCS_B_PK | TN_JOB_WORK_LOC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TN_JOB_WORK_LOC_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| TN_JOB_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_TN_JOBS_B_PK. |
| PRIMARY_FLAG | VARCHAR2 | 1 |  |  | Flag to differentiate Primary Vs Secondary Locations. |
| FA_LOCATION_ID | NUMBER |  | 18 | Yes | Location ID from FA. |
| FA_LOCATION_CODE | VARCHAR2 | 60 |  | Yes | Name of the location from FA. |
| ADDRESS_LINE_1 | VARCHAR2 | 240 |  |  | First line of address. |
| ADDRESS_LINE_2 | VARCHAR2 | 240 |  |  | Second line of address. |
| ADDRESS_LINE_3 | VARCHAR2 | 240 |  |  | Third line of address. |
| ADDRESS_LINE_4 | VARCHAR2 | 240 |  |  | Fourth line of address. |
| BUILDING | VARCHAR2 | 240 |  |  | Building name of the address. |
| TOWN_OR_CITY | VARCHAR2 | 60 |  |  | Name of the Town or City for the address. |
| POSTAL_CODE | VARCHAR2 | 30 |  |  | Postal code of the address. |
| COUNTRY | VARCHAR2 | 60 |  |  | Country of the address. |
| REGION_1 | VARCHAR2 | 120 |  |  | Primary region in which the address is located. |
| REGION_2 | VARCHAR2 | 120 |  |  | Sub-region of Region 1. |
| REGION_3 | VARCHAR2 | 120 |  |  | Sub-region of Region 2. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TN_JOB_WORK_LOCS_B_FK1 | Non Unique | Default | TN_JOB_ID |
| IRC_TN_JOB_WORK_LOCS_B_PK | Unique | default | TN_JOB_WORK_LOC_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
