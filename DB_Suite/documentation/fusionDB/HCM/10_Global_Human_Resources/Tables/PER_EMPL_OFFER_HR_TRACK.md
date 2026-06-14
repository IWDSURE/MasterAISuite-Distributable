# PER_EMPL_OFFER_HR_TRACK

This table stores the value of the offer assignment id along with the action's performed on this table and the resulatant assignment id's generated due to the action.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peremplofferhrtrack-11952.html#peremplofferhrtrack-11952](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peremplofferhrtrack-11952.html#peremplofferhrtrack-11952)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EMPL_OFFER_HR_TRACK_PK | OFFER_HR_TRACK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OFFER_HR_TRACK_ID | NUMBER |  | 18 | Yes | OFFER_HR_TRACK_ID is the primary key of the table. Based on this we can get the details of the offer record. |
| PERSON_ID | NUMBER |  | 18 |  | This fieldis used to store the person id detailsalong with the assigment id details |
| OFFER_ASG_ID | NUMBER |  | 18 |  | This particular field will store the detailsof the only assignment id generated while creating the offer. |
| PWK_ASG_ID | NUMBER |  | 18 |  | This columnb stores the pwk assignment id whihc gets created while converting the offer to a pwk or creating the pwndingworker |
| EMP_CWK_ASG_ID | NUMBER |  | 18 |  | This column will have the detaiuls of the either empassignment id or pwk assignment id. Which got created while converting the pwk |
| ACTION_OCCURRENCES_ID | NUMBER |  | 18 |  | Action occurrence id generated whilemaking the changes to the assignment record either offer or pwk |
| ACTION_TYPE_CODE | VARCHAR2 | 30 |  |  | the string form of the action type code which describes the action code in text |
| GLB_TRFR_ASG_ID | NUMBER |  | 18 |  | This column holds the assignment id details generated while performing global transfer .i.e; creating the global transfer work relationship |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| INCUMBENT_VALIDATION_FLAG | VARCHAR2 | 30 |  |  | Accepts value of Y or N. If set to Y, then consider the offer assignment for incumbent validation. |
| POSITION_SYNCHRONIZATION_FLAG | VARCHAR2 | 30 |  |  | Accepts value of Y or N. If set to Y, then consider the offer assignment for synchronization from position. |
| PREV_ACTION_OCCURRENCES_ID | NUMBER |  | 18 |  | To store the previous Action occurrence id for the present offer assignment record. |
| CONVERSION_STATUS | VARCHAR2 | 30 |  |  | To store the status of offer assignment record. |
| TRANSACTION_ID | NUMBER |  | 18 |  | To store the Transaction_id of HRC_TXN_HEADER |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_EMPL_OFFER_HR_TRACK_N1 | Non Unique | FUSION_TS_TX_IDX | PWK_ASG_ID |
| PER_EMPL_OFFER_HR_TRACK_N2 | Non Unique | FUSION_TS_TX_IDX | EMP_CWK_ASG_ID |
| PER_EMPL_OFFER_HR_TRACK_N3 | Non Unique | FUSION_TS_TX_IDX | OFFER_ASG_ID |
| PER_EMPL_OFFER_HR_TRACK_PK | Unique | FUSION_TS_TX_IDX | OFFER_HR_TRACK_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
