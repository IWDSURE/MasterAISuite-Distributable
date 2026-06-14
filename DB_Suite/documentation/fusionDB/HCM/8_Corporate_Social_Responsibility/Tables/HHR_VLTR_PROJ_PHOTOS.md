# HHR_VLTR_PROJ_PHOTOS

This table is used to store information about the photos of a project uploaded by the volunteers.

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrprojphotos-13824.html#hhrvltrprojphotos-13824](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrprojphotos-13824.html#hhrvltrprojphotos-13824)

## Primary Key

| Name | Columns |
|------|----------|
| HHR_VLTR_PROJ_PHOTOS_PK | PROJ_PHOTO_REL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROJ_PHOTO_REL_ID | NUMBER |  | 18 | Yes | PROJ_PHOTO_REL_ID |
| PROJECT_ID | NUMBER |  | 18 | Yes | PROJECT_ID |
| PHOTO_ID | NUMBER |  | 18 | Yes | PHOTO_ID |
| STATUS | VARCHAR2 | 100 |  |  | STATUS |
| SUBMITTED_BY | VARCHAR2 | 64 |  |  | SUBMITTED_BY |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hhr_vltr_proj_photos_U1 | Unique | FUSION_TS_TX_IDX | PROJ_PHOTO_REL_ID |
| hhr_vltr_proj_photos_U2 | Unique | FUSION_TS_TX_IDX | PROJECT_ID, PHOTO_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
