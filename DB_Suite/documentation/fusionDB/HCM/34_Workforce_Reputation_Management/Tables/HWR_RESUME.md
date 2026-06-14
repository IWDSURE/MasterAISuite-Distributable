# HWR_RESUME

The resume table stores resume documents.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrresume-18548.html#hwrresume-18548](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrresume-18548.html#hwrresume-18548)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_RESUME_PK | SOURCE_ID, RESUME_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RESUME_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the resume table. |
| ORIGINAL_ID | VARCHAR2 | 400 |  |  | This is the original ID of the resume from the source. |
| SOURCE_ID | NUMBER |  | 18 | Yes | This is the primary key for the social data source tables. |
| DOWNLOAD_DATE | TIMESTAMP |  |  |  | This is the download date of the resume document. |
| RESUME_TEXT | CLOB |  |  |  | This is the text version of the resume document. |
| RESUME | BLOB |  |  |  | This is the resume document in its original format. |
| MIME_TYPE | VARCHAR2 | 200 |  |  | This is the MIME type of the resume document. |
| RESUME_METADATA | VARCHAR2 | 4000 |  |  | This is additional metadata extracted from the resume document. |
| CHECKSUM | VARCHAR2 | 200 |  |  | This is the checksum of the resume document. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_RESUME_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, RESUME_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
