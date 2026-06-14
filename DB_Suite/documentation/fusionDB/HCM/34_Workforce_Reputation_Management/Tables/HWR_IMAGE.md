# HWR_IMAGE

This image table stores images for business objects - goal, team or contest

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrimage-4141.html#hwrimage-4141](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrimage-4141.html#hwrimage-4141)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_IMAGE_PK | IMAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| IMAGE_ID | NUMBER |  | 18 | Yes | This is the primary key for the image table. |
| MIME_TYPE | VARCHAR2 | 20 |  | Yes | mime type of the image file i.e. jpeg |
| BO_TYPE | VARCHAR2 | 80 |  | Yes | This is the type of the business object - goal, team or contest. |
| BO_ID | NUMBER |  | 18 | Yes | This is the id of the business object - goal, team or contest |
| IMAGE_DATA | BLOB |  |  | Yes | This is the image that each business object is associated with. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_IMAGE_U1 | Unique | FUSION_TS_TX_DATA | IMAGE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
