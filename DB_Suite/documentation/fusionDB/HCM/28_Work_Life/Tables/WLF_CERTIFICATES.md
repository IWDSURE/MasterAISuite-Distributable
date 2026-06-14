# WLF_CERTIFICATES

Table to store the details of Certificates

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcertificates-15875.html#wlfcertificates-15875](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcertificates-15875.html#wlfcertificates-15875)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_CERTIFICATES_PK | CERTIFICATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CERTIFICATE_ID | NUMBER |  | 18 | Yes | This column will be used to save the unique Certificate Id |
| CERTIFICATE_TYPE | VARCHAR2 | 30 |  |  | This column is used to store the Certificate Type |
| CERTIFICATE_FILE_NAME | VARCHAR2 | 4000 |  |  | This column is used to store Certificate File Name |
| CERTIFICATE_REF_TYPE | VARCHAR2 | 30 |  |  | Column to store Certificate Reference Type |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | This column is used to store the learningItemId in case of certificate ref type value is overridden to ORA_SPECIFIC |
| LEARNING_ITEM_TYPE | VARCHAR2 | 30 |  |  | This column is used to store the Learning Item Type |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_CERTIFICATES_U1 | Unique | Default | CERTIFICATE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
