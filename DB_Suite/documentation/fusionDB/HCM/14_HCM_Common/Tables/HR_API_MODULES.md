# HR_API_MODULES

This table contains details of the business processes and row handlers which contain user hooks. This table will contain data sourced from HR core development. If
legislation group/partners and legislation vertical market groups implement additional APIs they will also own rows in this table.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrapimodules-20617.html#hrapimodules-20617](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrapimodules-20617.html#hrapimodules-20617)

## Primary Key

| Name | Columns |
|------|----------|
| HR_API_MODULES_PK | API_MODULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| API_MODULE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| API_MODULE_TYPE | VARCHAR2 | 30 |  | Yes | Module type of the API. |
| MODULE_NAME | VARCHAR2 | 30 |  | Yes | Module name of the API. |
| DATA_WITHIN_BUSINESS_GROUP | VARCHAR2 | 30 |  | Yes | Indicates if the data associated with this module is within the context of a business_group_id. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | NULL for APIs implemented and maintained by HR Core development. Not null for extra legislation or legislation vertical market business processes which will contain customer hooks. |
| MODULE_PACKAGE | VARCHAR2 | 30 |  |  | When API_MODULE_TYPE is 'BP' holds the name of the database package containing the business process procedure otherwise NULL. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HR_API_MODULES_PK | Unique | Default | API_MODULE_ID, ORA_SEED_SET1 |
| HR_API_MODULES_PK1 | Unique | Default | API_MODULE_ID, ORA_SEED_SET2 |
| HR_API_MODULES_U1 | Unique | Default | API_MODULE_TYPE, MODULE_NAME, ORA_SEED_SET1 |
| HR_API_MODULES_U11 | Unique | Default | API_MODULE_TYPE, MODULE_NAME, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
