# PAY_OBJECT_GROUP_STORE

Table used for Object Group flex support

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobjectgroupstore-20939.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobjectgroupstore-20939.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_OBJECT_GROUP_STORE_PK | OBJECT_GROUP_STORE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECT_GROUP_STORE_ID | NUMBER |  | 18 | Yes | OBJECT_GROUP_STORE_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| OBJECT_GROUP_ID | NUMBER |  | 18 | Yes | OBJECT_GROUP_ID |
| OBJECT_GROUP_LEVEL_ID | NUMBER |  | 18 |  | OBJECT_GROUP_LEVEL_ID |
| SEQUENCE_NUMBER | NUMBER |  | 18 |  | SEQUENCE_NUMBER |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | PAYROLL_RELATIONSHIP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| OBJ_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | OBJ_INFORMATION_CATEGORY |
| OBJ_INFORMATION1 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION1 |
| OBJ_INFORMATION2 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION2 |
| OBJ_INFORMATION3 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION3 |
| OBJ_INFORMATION4 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION4 |
| OBJ_INFORMATION5 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION5 |
| OBJ_INFORMATION6 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION6 |
| OBJ_INFORMATION7 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION7 |
| OBJ_INFORMATION8 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION8 |
| OBJ_INFORMATION9 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION9 |
| OBJ_INFORMATION10 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION10 |
| OBJ_INFORMATION11 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION11 |
| OBJ_INFORMATION12 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION12 |
| OBJ_INFORMATION13 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION13 |
| OBJ_INFORMATION14 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION14 |
| OBJ_INFORMATION15 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION15 |
| OBJ_INFORMATION16 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION16 |
| OBJ_INFORMATION17 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION17 |
| OBJ_INFORMATION18 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION18 |
| OBJ_INFORMATION19 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION19 |
| OBJ_INFORMATION20 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION20 |
| OBJ_INFORMATION21 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION21 |
| OBJ_INFORMATION22 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION22 |
| OBJ_INFORMATION23 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION23 |
| OBJ_INFORMATION24 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION24 |
| OBJ_INFORMATION25 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION25 |
| OBJ_INFORMATION26 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION26 |
| OBJ_INFORMATION27 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION27 |
| OBJ_INFORMATION28 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION28 |
| OBJ_INFORMATION29 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION29 |
| OBJ_INFORMATION30 | VARCHAR2 | 150 |  |  | OBJ_INFORMATION30 |
| OBJ_INFORMATION_NUMBER1 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER1 |
| OBJ_INFORMATION_NUMBER2 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER2 |
| OBJ_INFORMATION_NUMBER3 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER3 |
| OBJ_INFORMATION_NUMBER4 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER4 |
| OBJ_INFORMATION_NUMBER5 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER5 |
| OBJ_INFORMATION_NUMBER6 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER6 |
| OBJ_INFORMATION_NUMBER7 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER7 |
| OBJ_INFORMATION_NUMBER8 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER8 |
| OBJ_INFORMATION_NUMBER9 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER9 |
| OBJ_INFORMATION_NUMBER10 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER10 |
| OBJ_INFORMATION_NUMBER11 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER11 |
| OBJ_INFORMATION_NUMBER12 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER12 |
| OBJ_INFORMATION_NUMBER13 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER13 |
| OBJ_INFORMATION_NUMBER14 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER14 |
| OBJ_INFORMATION_NUMBER15 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER15 |
| OBJ_INFORMATION_NUMBER16 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER16 |
| OBJ_INFORMATION_NUMBER17 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER17 |
| OBJ_INFORMATION_NUMBER18 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER18 |
| OBJ_INFORMATION_NUMBER19 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER19 |
| OBJ_INFORMATION_NUMBER20 | NUMBER |  |  |  | OBJ_INFORMATION_NUMBER20 |
| OBJ_INFORMATION_DATE1 | DATE |  |  |  | OBJ_INFORMATION_DATE1 |
| OBJ_INFORMATION_DATE2 | DATE |  |  |  | OBJ_INFORMATION_DATE2 |
| OBJ_INFORMATION_DATE3 | DATE |  |  |  | OBJ_INFORMATION_DATE3 |
| OBJ_INFORMATION_DATE4 | DATE |  |  |  | OBJ_INFORMATION_DATE4 |
| OBJ_INFORMATION_DATE5 | DATE |  |  |  | OBJ_INFORMATION_DATE5 |
| OBJ_INFORMATION_DATE6 | DATE |  |  |  | OBJ_INFORMATION_DATE6 |
| OBJ_INFORMATION_DATE7 | DATE |  |  |  | OBJ_INFORMATION_DATE7 |
| OBJ_INFORMATION_DATE8 | DATE |  |  |  | OBJ_INFORMATION_DATE8 |
| OBJ_INFORMATION_DATE9 | DATE |  |  |  | OBJ_INFORMATION_DATE9 |
| OBJ_INFORMATION_DATE10 | DATE |  |  |  | OBJ_INFORMATION_DATE10 |
| OBJ_INFORMATION_DATE11 | DATE |  |  |  | OBJ_INFORMATION_DATE11 |
| OBJ_INFORMATION_DATE12 | DATE |  |  |  | OBJ_INFORMATION_DATE12 |
| OBJ_INFORMATION_DATE13 | DATE |  |  |  | OBJ_INFORMATION_DATE13 |
| OBJ_INFORMATION_DATE14 | DATE |  |  |  | OBJ_INFORMATION_DATE14 |
| OBJ_INFORMATION_DATE15 | DATE |  |  |  | OBJ_INFORMATION_DATE15 |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_OBJECT_GROUP_STORE_N1 | Non Unique | Default | OBJECT_GROUP_ID, PAYROLL_RELATIONSHIP_ID |
| PAY_OBJECT_GROUP_STORE_PK | Unique | Default | OBJECT_GROUP_STORE_ID, ORA_SEED_SET1 |
| PAY_OBJECT_GROUP_STORE_PK1 | Unique | Default | OBJECT_GROUP_STORE_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
