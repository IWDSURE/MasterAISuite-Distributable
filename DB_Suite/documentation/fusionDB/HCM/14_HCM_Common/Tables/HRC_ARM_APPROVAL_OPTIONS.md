# HRC_ARM_APPROVAL_OPTIONS

This table stores the configurable options associated with each approval process.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcarmapprovaloptions-29568.html#hrcarmapprovaloptions-29568](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcarmapprovaloptions-29568.html#hrcarmapprovaloptions-29568)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ARM_APPROVAL_OPTIONS_PK | APPROVAL_OPTIONS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| APPROVAL_OPTIONS_ID | NUMBER |  | 18 | Yes | Primary key and unique identifier |
| AI_COMMENT_ENABLED | VARCHAR2 | 16 |  |  | Store AI Comment feature is enabled or not. |
| ARCHIVE_PERIOD | VARCHAR2 | 50 |  |  | Duration after which a completed transaction for the approval process can be moved from main transaction store to the archive data store. |
| PURGE_PERIOD | VARCHAR2 | 50 |  |  | Duration after which an archived transaction for the approval process becomes a candidate to be purged from the system. |
| PROCESS_ID | NUMBER |  | 18 | Yes | Foreign key to HRC_ARM_PROCESS tables. |
| APPROVAL_DISABLED | VARCHAR2 | 16 |  |  | Flag to indicate if approvals are disabled for an approval process. |
| ASYNC_BYPASS_ENABLED | VARCHAR2 | 16 |  |  | Store async bypass is enabled or not |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ALERT_ENABLED | VARCHAR2 | 16 |  |  | Used as a check before triggering alerts automatically |
| SEND_TO_USERS | VARCHAR2 | 16 |  |  | This is used to store whether the alerts should be sent to individual users or not |
| ALERT_TEMPLATE_OBJECT_GUID | VARCHAR2 | 32 |  |  | This is used for maintaining consistency of seeed data framework. |
| IS_PARALLEL_TXN_ENABLED | VARCHAR2 | 16 |  |  | Used to store user preference of enabling/disabling Parallel Transactions. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ARM_APPROVAL_OPTIONS_N20 | Non Unique | Default | SGUID |
| HRC_ARM_APPROVAL_OPTIONS_U1 | Unique | Default | APPROVAL_OPTIONS_ID, ORA_SEED_SET1 |
| HRC_ARM_APPROVAL_OPTIONS_U11 | Unique | Default | APPROVAL_OPTIONS_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
