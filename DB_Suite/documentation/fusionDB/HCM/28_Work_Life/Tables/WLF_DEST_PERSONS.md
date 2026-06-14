# WLF_DEST_PERSONS

Table to store person  information of assignment destinations

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfdestpersons-12432.html#wlfdestpersons-12432](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfdestpersons-12432.html#wlfdestpersons-12432)

## Primary Key

| Name | Columns |
|------|----------|
| wlf_dest_persons_PK | DESTINATION_PERSON_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DESTINATION_PERSON_ID | NUMBER |  | 18 | Yes | DESTINATION_PERSON_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| WORK_ASSIGNMENT_ID | NUMBER |  | 18 |  | Identifier for the work assignment of the person |
| JOB_ID | NUMBER |  | 18 |  | Specifies the job associated with person's work assignment |
| POSITION_ID | NUMBER |  | 18 |  | Specifies the position associated with person's work assignment |
| JOB_FAMILY_ID | NUMBER |  | 18 |  | Specifies the job family associated with person's job |
| STATUS | VARCHAR2 | 30 |  |  | Status |
| JOB_RUN_DATE | TIMESTAMP |  |  | Yes | JOB_RUN_DATE |
| DESTINATION_ID | NUMBER |  | 18 | Yes | DESTINATION_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| wlf_dest_persons_N1 | Non Unique | Default | DESTINATION_ID, JOB_RUN_DATE |
| wlf_dest_persons_N2 | Non Unique | Default | PERSON_ID |
| wlf_dest_persons_N3 | Non Unique | Default | WORK_ASSIGNMENT_ID |
| wlf_dest_persons_U1 | Unique | Default | DESTINATION_PERSON_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
