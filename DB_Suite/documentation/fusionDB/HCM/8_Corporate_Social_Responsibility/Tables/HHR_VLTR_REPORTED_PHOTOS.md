# HHR_VLTR_REPORTED_PHOTOS

This table stores all abused project photos which are uploaded by users

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrreportedphotos-24090.html#hhrvltrreportedphotos-24090](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrreportedphotos-24090.html#hhrvltrreportedphotos-24090)

## Primary Key

| Name | Columns |
|------|----------|
| hhr_vltr_reported_photos_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | ID |
| REPORTED_BY | VARCHAR2 | 64 |  | Yes | REPORTED_BY |
| PROJ_PHOTO_REL_ID | NUMBER |  | 18 | Yes | Project Photo Relation Id |
| COMMENTS | VARCHAR2 | 200 |  |  | COMMENTS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hhr_vltr_reported_photos_N1 | Non Unique | FUSION_TS_TX_IDX | PROJ_PHOTO_REL_ID |
| hhr_vltr_reported_photos_U1 | Unique | FUSION_TS_TX_IDX | ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
