# HWM_RULE_RUN_INFO_HDR

Contains the rules created for OTL Time Calculation, Time Entry and Time Audit rules.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruleruninfohdr-16083.html#hwmruleruninfohdr-16083](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruleruninfohdr-16083.html#hwmruleruninfohdr-16083)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RULE_RUN_INFO_HDR_PK | RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| RUN_DATE_START | TIMESTAMP |  |  | Yes | RUN_DATE_START |
| RUN_DATE_STOP | TIMESTAMP |  |  |  | RUN_DATE_STOP |
| RUN_STATUS | VARCHAR2 | 30 |  |  | RUN_STATUS |
| PROCESS_TIME_SEC | NUMBER |  |  |  | PROCESS_TIME_SEC |
| REQUEST_SOURCE | VARCHAR2 | 80 |  |  | REQUEST_SOURCE |
| BUILDING_BLOCK_ID | NUMBER |  | 18 |  | BUILDING_BLOCK_ID |
| BUILDING_BLOCK_VERSION | NUMBER |  | 9 |  | BUILDING_BLOCK_VERSION |
| RESOURCE_ID | NUMBER |  | 18 |  | RESOURCE_ID |
| SUBRESOURCE_ID | NUMBER |  | 18 |  | SUBRESOURCE_ID |
| RUN_EVENT_TYPE | VARCHAR2 | 30 |  |  | RUN_EVENT_TYPE |
| RULE_TYPE | VARCHAR2 | 30 |  |  | RULE_TYPE |
| RULE_SET_ID | NUMBER |  | 18 |  | RULE_SET_ID |
| RULE_SET_NAME | VARCHAR2 | 80 |  |  | RULE_SET_NAME |
| RS_EFFECTIVE_START_DATE | DATE |  |  |  | RS_EFFECTIVE_START_DATE |
| RS_EFFECTIVE_END_DATE | DATE |  |  |  | RS_EFFECTIVE_END_DATE |
| RULE_ID | NUMBER |  | 18 |  | RULE_ID |
| RULE_NAME | VARCHAR2 | 80 |  |  | Name of the Rule |
| RUN_DETAIL_XML | CLOB |  |  |  | RUN_DETAIL_XML |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_RULE_RUN_INFO_HDR_N1 | Non Unique | Default | TRUNC("RUN_DATE_START") |
| HWM_RULE_RUN_INFO_HDR_N2 | Non Unique | Default | TRUNC("CREATION_DATE") |
| HWM_RULE_RUN_INFO_HDR_PK | Unique | FUSION_TS_TX_DATA | RUN_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
