# WLF_CAP_DEFAULT_CERTIFICATES

Table to store learning catalog default certificates.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcapdefaultcertificates-3313.html#wlfcapdefaultcertificates-3313](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcapdefaultcertificates-3313.html#wlfcapdefaultcertificates-3313)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_CAP_DEFAULT_CERTIFICAT_PK | CERTIFICATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CERTIFICATE_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| CERTIFICATE_TYPE | VARCHAR2 | 30 |  |  | This column is used to store the Certificate Type |
| CERTIFICATE_FILE_NAME | VARCHAR2 | 4000 |  |  | This column is used to store Certificate File Name |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | This column is used to store the learningItemId of catalog admin profile |
| CATALOG_LI_TYPE | VARCHAR2 | 30 |  |  | This column is used to store the Catalog Learning Item Type |
| COMPLETION_CERTIFICATE_ENABLED | VARCHAR2 | 1 |  |  | This column indicates if certificate is enabled or not |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_CAP_DEF_CERTIFICATES_N1 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_CAP_DEF_CERTIFICATES_N2 | Non Unique | Default | CERTIFICATE_FILE_NAME |
| WLF_CAP_DEF_CERTIFICATES_U1 | Unique | Default | CERTIFICATE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
