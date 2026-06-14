# PAY_INSTALLED_LEGISLATIONS

This table contains details of legislations, both predefined and those created using the Configure Payroll Legislations task.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payinstalledlegislations-18305.html#payinstalledlegislations-18305](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payinstalledlegislations-18305.html#payinstalledlegislations-18305)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_INSTALLED_LEG_PK | APPLICATION_ID, LEGISLATION_CODE, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| APPLICATION_ID | NUMBER |  | 18 | Yes | APPLICATION_ID |
| LEGISLATION_CODE | VARCHAR2 | 5 |  | Yes | Foreign key to FND_TERRITORIES. |
| SEEDED_FLAG | VARCHAR2 | 5 |  | Yes | SEEDED_FLAG |
| INSTALLED_FLAG | VARCHAR2 | 5 |  | Yes | INSTALLED_FLAG |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEEDED_STATUS | VARCHAR2 | 30 |  |  | SEEDED_STATUS |
| PAYROLL_LICENSE | VARCHAR2 | 30 |  |  | PAYROLL_LICENSE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| PAY_INSTALLED_LEGISLATIONS_ID | NUMBER |  | 18 |  | PAY_INSTALLED_LEGISLATIONS_ID |
| ADDRESS_STYLE_CODE | VARCHAR2 | 30 |  | Yes | Address style used for PER_ADDRESSES_F |
| ADDRESS_VALIDATION_FLAG | VARCHAR2 | 30 |  | Yes | Address Business Logic Unit (BLU) validation flag |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| PIL_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Structure definition of the descriptive flexfield |
| PIL_INFORMATION1 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION2 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION3 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION4 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION5 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION6 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION7 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION8 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION9 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION10 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION11 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION12 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION13 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION14 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION15 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION16 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION17 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION18 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION19 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION20 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield |
| PIL_INFORMATION21 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION22 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION23 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION24 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION25 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION26 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION27 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION28 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION29 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION30 | VARCHAR2 | 150 |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION_NUMBER1 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_NUMBER2 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_NUMBER3 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_NUMBER4 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_NUMBER5 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_NUMBER6 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_NUMBER7 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_NUMBER8 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_NUMBER9 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_NUMBER10 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_NUMBER11 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_NUMBER12 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_NUMBER13 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_NUMBER14 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_NUMBER15 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_NUMBER16 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION_NUMBER17 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION_NUMBER18 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION_NUMBER19 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION_NUMBER20 | NUMBER |  |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION_DATE1 | DATE |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_DATE2 | DATE |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_DATE3 | DATE |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_DATE4 | DATE |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_DATE5 | DATE |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_DATE6 | DATE |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_DATE7 | DATE |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_DATE8 | DATE |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_DATE9 | DATE |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_DATE10 | DATE |  |  |  | Segment of the developer descriptive flexfield. |
| PIL_INFORMATION_DATE11 | DATE |  |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION_DATE12 | DATE |  |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION_DATE13 | DATE |  |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION_DATE14 | DATE |  |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |
| PIL_INFORMATION_DATE15 | DATE |  |  |  | Segment of the developer descriptive flexfield. Reserved for customer use. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_INSTALLED_LEG_PK | Unique | FUSION_TS_SEED | APPLICATION_ID, LEGISLATION_CODE, ENTERPRISE_ID, ORA_SEED_SET1 |
| PAY_INSTALLED_LEG_PK1 | Unique | FUSION_TS_SEED | APPLICATION_ID, LEGISLATION_CODE, ENTERPRISE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
