# PER_CHECKLIST_CONTENTS

PER_CHECKLIST_CONTENTS : This table has checlist contents

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistcontents-16657.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistcontents-16657.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_CONTENTS_PK | CHECKLIST_CONTENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CHECKLIST_CONTENT_ID | NUMBER |  | 18 | Yes | CHECKLIST_CONTENT_ID |  |
| CHECKLIST_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_CHECKLISTS_B.CHECKLIST_ID |  |
| CONTENT_TYPE | VARCHAR2 | 30 |  | Yes | Content Type
System Lookup: ORA_CHK_CONTENT_TYPE
Values:
ORA_NOTE - Note
ORA_EVENT - Events / Announcements
ORA_ONBOARDING_STEP - Onboarding Step (This type is available only for checklist type ONBOARDING) |  |
| SEQUENCE | NUMBER |  | 9 |  | Sequence of the content |  |
| CHK_CONTENT_DEFN_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_CHK_CONTENT_DEFNS_B.CHK_CONTENT_DEFN_ID |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CHECKLIST_CONTENTS_N1 | Non Unique | FUSION_TS_TX_DATA | CHECKLIST_ID |
| PER_CHECKLIST_CONTENTS_PK | Unique | FUSION_TS_TX_DATA | CHECKLIST_CONTENT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
