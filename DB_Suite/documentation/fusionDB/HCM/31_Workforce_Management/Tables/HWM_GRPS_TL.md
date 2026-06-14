# HWM_GRPS_TL

Contains Translated values for Group Defintion

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpstl-4505.html#hwmgrpstl-4505](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpstl-4505.html#hwmgrpstl-4505)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_GRPS_TL_PK | GRP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| GRP_ID | NUMBER |  | 18 | Yes | GRP_ID |  |
| GROUP_NAME | VARCHAR2 | 180 |  |  | GROUP_NAME | Obsolete |
| GROUP_NAME#01 | VARCHAR2 | 960 |  |  | GROUP_NAME#01 | Active |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | DESCRIPTION |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWM_GRPS_TL_N1 | Non Unique | Default | UPPER("GROUP_NAME") | Obsolete |
| HWM_GRPS_TL_N2 | Non Unique | Default | UPPER("GROUP_NAME#01") |  |
| HWM_GRPS_TL_U1 | Unique | FUSION_TS_TX_DATA | GRP_ID, LANGUAGE, ORA_SEED_SET1 |  |
| HWM_GRPS_TL_U11 | Unique | FUSION_TS_TX_DATA | GRP_ID, LANGUAGE, ORA_SEED_SET2 |  |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
