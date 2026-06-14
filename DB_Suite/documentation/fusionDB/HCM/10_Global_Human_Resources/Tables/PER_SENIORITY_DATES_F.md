# PER_SENIORITY_DATES_F

This is transactional table for storing seniority dates.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persenioritydatesf-6926.html#persenioritydatesf-6926](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persenioritydatesf-6926.html#persenioritydatesf-6926)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SENIORITY_DATES_F_PK | SENIORITY_DATE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SENIORITY_DATE_ID | NUMBER |  | 18 | Yes | This is the unique Id for Seniority Date Item | Active |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. | Active |
| SENIORITY_DATE_CODE | VARCHAR2 | 30 |  | Yes | Code to identify the Seniority Date Item.Eg: ORA_ESD_P , ORA_JOB_SD_A | Active |
| PERSON_ID | NUMBER |  | 18 | Yes | Unique identifier (ID) that identifies teh person this item belongs to. | Active |
| ENTRY_DATE | DATE |  |  | Yes | First date in which the seniority attribute value was first assigned to this person at the given level. | Active |
| SENIORITY_DATE | DATE |  |  | Yes | The actual seniority date value based on which the length of service will be calculated for day | Active |
| BASE_SENIORITY_DATE | DATE |  |  | Yes | Seniority Date from the previous date effective row, used as reference for offsetting seniority date in this row. | Active |
| CALCULATION_TYPE | VARCHAR2 | 30 |  | Yes | Mode of calculation Manual when created by user and  Automatic.when created by ESS | Active |
| LEVEL_CODE | VARCHAR2 | 30 |  | Yes | Lookup code for the Seniority Level. | Active |
| LEVEL_OBJECT_ID | NUMBER |  | 18 | Yes | Unique identifier (ID) that identifies the level object. | Active |
| SENIORITY_FIELD | VARCHAR2 | 30 |  | Yes | Lookup code for the Triggering Field based on which this seniority is defined. | Active |
| SENIORITY_FIELD_KEY | VARCHAR2 | 150 |  |  | Unified redundant column that combines all three seniority key fields - Number, Text, Date |  |
| RECORD_CREATOR | VARCHAR2 | 30 |  | Yes | Creator process of this record. For example, HDL, UI, and ESS. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Unique identifier (ID) that identifies the enterprise | Active |
| MANUAL_ADJUSTMENT_DAYS | NUMBER |  | 18 |  | Offset number of days by which the seniority date gets adjusted in this change. | Active |
| TOTAL_MANUAL_ADJUSTMENT_DAYS | NUMBER |  | 18 |  | Total offset number of days by which the seniority date gets adjusted by manual change in all changes till this point in time. | Active |
| AUTO_ADJUSTMENT_DAYS | NUMBER |  | 18 |  | Offset number of days by which the seniority date gets adjusted in this change. | Active |
| TOTAL_AUTO_ADJUSTMENT_DAYS | NUMBER |  | 18 |  | Total offset number of days by which the seniority date gets adjusted by auto change in all changes till this point in time. | Active |
| TOTAL_ADJUSTMENT_DAYS | NUMBER |  | 18 |  | Total offset number of days by which the seniority date gets adjusted by all sources of change till this point in time. | Active |
| MANUAL_ADJUSTMENT_HOURS | NUMBER |  | 18 |  | Offset number of hours by which the seniority hours gets adjusted in this change. | Active |
| TOTAL_MANUAL_ADJUSTMENT_HOURS | NUMBER |  | 18 |  | Total offset number of hours by which the seniority hours gets adjusted by manual change in all changes till this point in time. | Active |
| AUTO_ADJUSTMENT_HOURS | NUMBER |  | 18 |  | Offset number of hours by which the seniority hours gets adjusted in this change. | Active |
| TOTAL_AUTO_ADJUSTMENT_HOURS | NUMBER |  | 18 |  | Total offset number of hours by which the seniority hours gets adjusted by auto change in all changes till this point in time. | Active |
| TOTAL_ADJUSTMENT_HOURS | NUMBER |  | 18 |  | Total offset number of days by which the seniority hours gets adjusted by auto and manual sources of change till this point in time. | Active |
| MANUAL_ADJUSTMENT_COMMENTS | VARCHAR2 | 300 |  |  | Optional comments regarding the adjustment in the seniority date for manual change. | Active |
| AUTO_ADJUSTMENT_COMMENTS | VARCHAR2 | 300 |  |  | Optional comments regarding the adjustment in the seniority date for an auto change | Active |
| GAP_IN_DAYS | NUMBER |  | 18 |  | Gap in days in the occupation of the seniority field. | Active |
| EXIT_DATE | DATE |  |  |  | Last date in which the seniority attribute value was assigned to this person at the given level. | Active |
| SENIORITY_HOURS | NUMBER |  | 18 |  | Seniority Hours loaded from Seniority Hours table. | Active |
| TOTAL_SENIORITY_HOURS | NUMBER |  | 18 |  | Total offset number of days by which the seniority hours gets adjusted by all sources (auto,manual and seniority hours table) of change till this point in time. | Active |
| LAST_SENIORITY_HRS_RUN_DATE | DATE |  |  |  | Date of which the ESS process ran last for this item. | Active |
| SENIORITY_HOURS_LOS | VARCHAR2 | 100 |  |  | Seniority Hours converted to Length of Service format |  |
| SENIORITY_LOS_YEARS | NUMBER |  | 18 |  | Number of years in Seniority Hours converted to Length of Service format. |  |
| SENIORITY_LOS_MONTHS | NUMBER |  | 18 |  | Number of months in Seniority Hours converted to Length of Service format. |  |
| SENIORITY_LOS_DAYS | NUMBER |  | 18 |  | Number of days in Seniority Hours converted to Length of Service format. |  |
| SENIORITY_LOS_TOTAL_DAYS | NUMBER |  | 18 |  | Seniority Hours converted to number of days. |  |
| LAST_ESS_RUN_DATE | TIMESTAMP |  |  |  | Indicates the date and time of the last update of the row by last ESS run process. |  |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | Indicates the request Id of last ESS process which updated the record. |  |
| OVERLAPPING_PERIOD_IN_DAYS | NUMBER |  | 18 |  | Days overlapping among two or more assignments of the same seniority attribute. (Reserved for future use) | Active |
| MARKED_FOR_RECALCULATION | VARCHAR2 | 30 |  |  | Whether this item is marked for recalculation. (Reserved for future use) | Active |
| SENIORITY_FIELD_NUMBER | NUMBER |  | 18 |  | Number based unique identifier (ID) that identifies the field based on which this seniority date rule is configured. For example, JobID and PositionID. | Active |
| SENIORITY_FIELD_DATE | DATE |  |  |  | Date based unique identifier (ID) that identifies the field based on which this seniority date rule is configured. This is reserved for future use when such an attribute is integrated. | Active |
| SENIORITY_FIELD_TEXT | VARCHAR2 | 150 |  |  | Text based unique identifier (ID) that identifies the field based on which this seniority date rule is configured. For example, LegislationCode. | Active |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | An unique identifier that identifies the source of data in case of non UI sources. For HDL, data set id. For ESS, request id. | Active |
| PREVIOUS_SENIORITY_DATE_ID | NUMBER |  | 18 |  | Unique Id of seniority date item based on which this item is calculated. (Internal Use) |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_SENIORITY_DATES_F_N2 | Non Unique | FUSION_TS_TX_DATA | SENIORITY_DATE_CODE, PERSON_ID, ENTRY_DATE, LEVEL_OBJECT_ID, SENIORITY_FIELD_KEY |
| PER_SENIORITY_DATES_F_U1 | Unique | FUSION_TS_TX_DATA | SENIORITY_DATE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
