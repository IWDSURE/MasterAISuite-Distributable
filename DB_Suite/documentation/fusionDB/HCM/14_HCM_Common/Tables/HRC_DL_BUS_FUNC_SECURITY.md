# HRC_DL_BUS_FUNC_SECURITY

HRC_DL_BUS_FUNC_SECURITY table is used by data loader to restrict the secured object available to customers.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbusfuncsecurity-29560.html#hrcdlbusfuncsecurity-29560](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbusfuncsecurity-29560.html#hrcdlbusfuncsecurity-29560)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_BUS_FUNC_SECURITY_PK | BUS_FUNC_SECURITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BUS_FUNC_SECURITY_ID | NUMBER |  | 18 | Yes | BUS_FUNC_SECURITY_ID |
| BUS_OBJ_INCLUSION_ID | NUMBER |  | 18 | Yes | BUS_OBJ_INCLUSION_ID |
| FUNC_SECURITY_RESOURCE_NAME | VARCHAR2 | 500 |  |  | FUNC_SECURITY_RESOURCE_NAME |
| FUNC_SECURITY_ENABLED | VARCHAR2 | 5 |  | Yes | FUNC_SECURITY_ENABLED |
| SGUID | VARCHAR2 | 32 |  | Yes | SGUID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_BUS_FUNC_SECURITY_N1 | Non Unique | HRC_DL_BUS_FUNC_SECURITY_N1 | BUS_OBJ_INCLUSION_ID |
| HRC_DL_BUS_FUNC_SECURITY_PK | Unique | HRC_DL_BUS_FUNC_SECURITY_PK | BUS_FUNC_SECURITY_ID, ORA_SEED_SET1 |
| HRC_DL_BUS_FUNC_SECURITY_PK1 | Unique | HRC_DL_BUS_FUNC_SECURITY_PK | BUS_FUNC_SECURITY_ID, ORA_SEED_SET2 |
| HRC_DL_BUS_FUNC_SECURITY_U20 | Unique | HRC_DL_BUS_FUNC_SECURITY_U20 | SGUID, ORA_SEED_SET1 |
| HRC_DL_BUS_FUNC_SECURITY_U201 | Unique | HRC_DL_BUS_FUNC_SECURITY_U20 | SGUID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
