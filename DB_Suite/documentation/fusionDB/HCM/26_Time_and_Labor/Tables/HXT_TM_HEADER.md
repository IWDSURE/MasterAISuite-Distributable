# HXT_TM_HEADER

This table represents the timecard header available in the Webentry Timecard UI. It will hold all the header level information for the timecard like Timecard Header Comments,User Status, Resource Id, Resrouce Type, etc apart from holding the timecard header level attributes if configured with any.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttmheader-25539.html#hxttmheader-25539](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttmheader-25539.html#hxttmheader-25539)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_TM_HEADER_PK | TM_HEADER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TM_HEADER_ID | NUMBER |  | 18 | Yes | This will be the timecard id for the timecards stored in the UI table. | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| RESOURCE_ID | NUMBER |  | 18 | Yes | FK to PER_ALL_PEOPLE_F. The Id of the resource for whom the timecard has been entered. | Active |
| TCLAYST_ID | NUMBER |  | 18 |  | FK to HXT_TCLAYST_B. The Id of the layout set which was used to create the timecard. | Active |
| RESOURCE_TYPE | VARCHAR2 | 150 |  |  | Type of the Resource for whom the timecard has been entered. | Active |
| START_DATE | DATE |  |  | Yes | Denotes the Start Date of the timecard. | Active |
| END_DATE | DATE |  |  | Yes | Denotes the End Date of the timecard. | Active |
| OBJECT_TYPE | VARCHAR2 | 150 |  | Yes | If the data is for Timecard or Template. | Active |
| TIME_REPORTER_ID | NUMBER |  | 18 | Yes | Denotes who actually reported this timecard. FK to PER_ALL_PEOPLE_F. | Active |
| TIME_BLDG_BLK_ID | NUMBER |  | 18 |  | The timecard id link between the UI table and the time store table. Foriegn key to the HXT_TM_BLDG_BLKS Table.For template this will be null. | Active |
| TIME_BLDG_BLK_VERSION | NUMBER |  | 18 |  | The Time Building Block version link between the UI table and the time store table.Foriegn key to the HXT_TM_BLDG_BLKS Table.For template this will be null. | Active |
| LAST_COMMIT_TIME | TIMESTAMP |  |  |  | LAST_COMMIT_TIME |  |
| CALCULATED_TIME_HEADER_ID | NUMBER |  | 18 |  | CALCULATED_TIME_HEADER_ID |  |
| TM_BLDG_BLK_DAY_ID1 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID1 |  |
| TM_BLDG_BLK_DAY_ID2 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID2 |  |
| TM_BLDG_BLK_DAY_ID3 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID3 |  |
| TM_BLDG_BLK_DAY_ID4 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID4 |  |
| TM_BLDG_BLK_DAY_ID5 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID5 |  |
| TM_BLDG_BLK_DAY_ID6 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID6 |  |
| TM_BLDG_BLK_DAY_ID7 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID7 |  |
| TM_BLDG_BLK_DAY_ID8 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID8 |  |
| TM_BLDG_BLK_DAY_ID9 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID9 |  |
| TM_BLDG_BLK_DAY_ID10 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID10 |  |
| TM_BLDG_BLK_DAY_ID11 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID11 |  |
| TM_BLDG_BLK_DAY_ID12 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID12 |  |
| TM_BLDG_BLK_DAY_ID13 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID13 |  |
| TM_BLDG_BLK_DAY_ID14 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID14 |  |
| TM_BLDG_BLK_DAY_ID15 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID15 |  |
| TM_BLDG_BLK_DAY_ID16 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID16 |  |
| TM_BLDG_BLK_DAY_ID17 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID17 |  |
| TM_BLDG_BLK_DAY_ID18 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID18 |  |
| TM_BLDG_BLK_DAY_ID19 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID19 |  |
| TM_BLDG_BLK_DAY_ID20 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID20 |  |
| TM_BLDG_BLK_DAY_ID21 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID21 |  |
| TM_BLDG_BLK_DAY_ID22 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID22 |  |
| TM_BLDG_BLK_DAY_ID23 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID23 |  |
| TM_BLDG_BLK_DAY_ID24 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID24 |  |
| TM_BLDG_BLK_DAY_ID25 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID25 |  |
| TM_BLDG_BLK_DAY_ID26 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID26 |  |
| TM_BLDG_BLK_DAY_ID27 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID27 |  |
| TM_BLDG_BLK_DAY_ID28 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID28 |  |
| TM_BLDG_BLK_DAY_ID29 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID29 |  |
| TM_BLDG_BLK_DAY_ID30 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID30 |  |
| TM_BLDG_BLK_DAY_ID31 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_ID31 |  |
| TM_BLDG_BLK_DAY_VERSION1 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION1 |  |
| TM_BLDG_BLK_DAY_VERSION2 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION2 |  |
| TM_BLDG_BLK_DAY_VERSION3 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION3 |  |
| TM_BLDG_BLK_DAY_VERSION4 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION4 |  |
| TM_BLDG_BLK_DAY_VERSION5 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION5 |  |
| TM_BLDG_BLK_DAY_VERSION6 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION6 |  |
| TM_BLDG_BLK_DAY_VERSION7 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION7 |  |
| TM_BLDG_BLK_DAY_VERSION8 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION8 |  |
| TM_BLDG_BLK_DAY_VERSION9 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION9 |  |
| TM_BLDG_BLK_DAY_VERSION10 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION10 |  |
| TM_BLDG_BLK_DAY_VERSION11 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION11 |  |
| TM_BLDG_BLK_DAY_VERSION12 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION12 |  |
| TM_BLDG_BLK_DAY_VERSION13 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION13 |  |
| TM_BLDG_BLK_DAY_VERSION14 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION14 |  |
| TM_BLDG_BLK_DAY_VERSION15 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION15 |  |
| TM_BLDG_BLK_DAY_VERSION16 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION16 |  |
| TM_BLDG_BLK_DAY_VERSION17 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION17 |  |
| TM_BLDG_BLK_DAY_VERSION18 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION18 |  |
| TM_BLDG_BLK_DAY_VERSION19 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION19 |  |
| TM_BLDG_BLK_DAY_VERSION20 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION20 |  |
| TM_BLDG_BLK_DAY_VERSION21 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION21 |  |
| TM_BLDG_BLK_DAY_VERSION22 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION22 |  |
| TM_BLDG_BLK_DAY_VERSION23 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION23 |  |
| TM_BLDG_BLK_DAY_VERSION24 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION24 |  |
| TM_BLDG_BLK_DAY_VERSION25 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION25 |  |
| TM_BLDG_BLK_DAY_VERSION26 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION26 |  |
| TM_BLDG_BLK_DAY_VERSION27 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION27 |  |
| TM_BLDG_BLK_DAY_VERSION28 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION28 |  |
| TM_BLDG_BLK_DAY_VERSION29 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION29 |  |
| TM_BLDG_BLK_DAY_VERSION30 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION30 |  |
| TM_BLDG_BLK_DAY_VERSION31 | NUMBER |  | 18 |  | TM_BLDG_BLK_DAY_VERSION31 |  |
| DATA_SET_ID | NUMBER |  | 18 |  | FK to HXT_DATA_SETS.DATA_SET_ID. Used in the R12 Archiving solution. | Active |
| COMMENTS | VARCHAR2 | 1000 |  |  | Timecard level comments. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 150 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER1 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER2 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER3 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER4 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER5 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER6 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER7 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER8 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER9 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER10 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER11 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER12 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER13 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER14 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER15 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER16 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER17 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER18 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER19 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER20 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_TM_HEADER_N1 | Non Unique | Default | TIME_BLDG_BLK_ID |
| HXT_TM_HEADER_N2 | Non Unique | Default | RESOURCE_ID, START_DATE |
| HXT_TM_HEADER_PK | Unique | Default | TM_HEADER_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
