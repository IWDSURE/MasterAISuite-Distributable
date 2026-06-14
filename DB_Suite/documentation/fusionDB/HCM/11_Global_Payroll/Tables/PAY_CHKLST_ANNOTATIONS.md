# PAY_CHKLST_ANNOTATIONS

Annotations describing the checklist

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paychklstannotations-21903.html#paychklstannotations-21903](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paychklstannotations-21903.html#paychklstannotations-21903)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_CHKLST_ANNOTATIONS_PK | CHECKLIST_ANNOTATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CHECKLIST_ANNOTATION_ID | NUMBER |  | 18 | Yes | CHECKLIST_ANNOTATION_ID |  |
| BASE_ANNOTATION_ID | NUMBER |  | 18 | Yes | BASE_ANNOTATION_ID |  |
| BASE_ANNOTATION_TXT | VARCHAR2 | 200 |  | Yes | BASE_ANNOTATION_TXT |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| BASE_CHECKLIST_ID | NUMBER |  | 18 | Yes | BASE_CHECKLIST_ID |  |
| OWNER_ID | NUMBER |  | 18 |  | OWNER_ID |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. | Obsolete |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| PAY_CHKLST_ANNOTATIONS_N20 | Non Unique | Default | SGUID | Obsolete |
| PAY_CHKLST_ANNOTATIONS_PK | Unique | Default | CHECKLIST_ANNOTATION_ID |  |
| PAY_CHKLST_ANNOTATIONS_U1 | Unique | Default | LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, BASE_ANNOTATION_TXT |  |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
