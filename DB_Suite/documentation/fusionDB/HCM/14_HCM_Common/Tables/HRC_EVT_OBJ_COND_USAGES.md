# HRC_EVT_OBJ_COND_USAGES

An Event Condition provides qualifying criteria for an object and is used to refine the circumstances under which the event will be detected.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtobjcondusages-25029.html#hrcevtobjcondusages-25029](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtobjcondusages-25029.html#hrcevtobjcondusages-25029)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_OBJ_COND_USAGES_PK | OBJ_COND_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJ_COND_USAGE_ID | NUMBER |  | 18 | Yes | Specifies an object condition usage ID which can be used to identify an event condition. |
| OBJ_CONDITION_ID | NUMBER |  | 18 | Yes | Specifies an object contidion ID which can be used to identify an event condition. |
| PRODUCT_CODE | VARCHAR2 | 30 |  | Yes | Identifies the product code |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| DELETED_FLAG | VARCHAR2 | 1 |  | Yes | Identifies if the condition is deleted.. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_EVT_OBJ_COND_USAGES_N20 | Non Unique | HRC_EVT_OBJ_COND_USAGES_N20 | SGUID |
| HRC_EVT_OBJ_COND_USAGES_PK | Unique | HRC_EVT_OBJ_COND_USAGES_PK | OBJ_COND_USAGE_ID, ORA_SEED_SET1 |
| HRC_EVT_OBJ_COND_USAGES_PK1 | Unique | HRC_EVT_OBJ_COND_USAGES_PK1 | OBJ_COND_USAGE_ID, ORA_SEED_SET2 |
| HRC_EVT_OBJ_COND_USAGES_U1 | Unique | HRC_EVT_OBJ_COND_USAGES_U1 | OBJ_CONDITION_ID, PRODUCT_CODE, ORA_SEED_SET1 |
| HRC_EVT_OBJ_COND_USAGES_U11 | Unique | HRC_EVT_OBJ_COND_USAGES_U11 | OBJ_CONDITION_ID, PRODUCT_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
