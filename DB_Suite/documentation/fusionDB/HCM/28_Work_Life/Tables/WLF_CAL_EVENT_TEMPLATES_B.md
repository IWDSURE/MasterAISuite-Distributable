# WLF_CAL_EVENT_TEMPLATES_B

Table to store learner and instructor default event calendar template details.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcaleventtemplatesb-11208.html#wlfcaleventtemplatesb-11208](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcaleventtemplatesb-11208.html#wlfcaleventtemplatesb-11208)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_CAL_EVENT_TEMPLATES_B_PK | EVENT_TEMPLATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_TEMPLATE_ID | NUMBER |  | 18 | Yes | System generated unique identifier to define template record Id |
| EVENT_TEMPLATE_CODE | VARCHAR2 | 64 |  | Yes | Code to uniquely identify the template. Primary used for seed framework |
| EVENT_TEMPLATE_TYPE | VARCHAR2 | 64 |  | Yes | Define whether its learner template or customer template |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_CAL_EVENT_TEMPLATEST_B_PK | Unique | Default | EVENT_TEMPLATE_ID, ORA_SEED_SET1 |
| WLF_CAL_EVENT_TEMPLATEST_B_PK1 | Unique | Default | EVENT_TEMPLATE_ID, ORA_SEED_SET2 |
| WLF_CAL_EVENT_TEMPLATEST_B_U1 | Unique | Default | EVENT_TEMPLATE_CODE, ORA_SEED_SET1 |
| WLF_CAL_EVENT_TEMPLATEST_B_U2 | Unique | Default | EVENT_TEMPLATE_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
