# HWM_GRP_INCL_GRPS

Contains Included Groups for Group Defintion

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpinclgrps-26088.html#hwmgrpinclgrps-26088](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpinclgrps-26088.html#hwmgrpinclgrps-26088)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_GRP_INCL_GRPS_PK | GRP_INCL_GRP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GRP_INCL_GRP_ID | NUMBER |  | 18 | Yes | GRP_INCL_GRP_ID |
| GRP_OR_VALUESET_CD | VARCHAR2 | 30 |  |  | GRP_OR_VALUESET_CD |
| GRP_ID | NUMBER |  | 18 |  | GRP_ID |
| INCL_GRP_ID | NUMBER |  | 18 |  | INCL_GRP_ID |
| INCL_FLAG | VARCHAR2 | 30 |  |  | INCL_FLAG |
| ORDER_NUM | NUMBER |  | 9 |  | ORDER_NUM |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_GRP_INCL_GRPS_N1 | Non Unique | FUSION_TS_TX_DATA | GRP_ID, INCL_GRP_ID |
| HWM_GRP_INCL_GRPS_U1 | Unique | FUSION_TS_TX_DATA | GRP_INCL_GRP_ID, ORA_SEED_SET1 |
| HWM_GRP_INCL_GRPS_U11 | Unique | FUSION_TS_TX_DATA | GRP_INCL_GRP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
