# HRT_PROFILE_TP_SC_PRP_TL_BK

Backup table for HRT_PROFILE_TP_SC_PRP_TL

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletpscprptlbk-8761.html#hrtprofiletpscprptlbk-8761](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletpscprptlbk-8761.html#hrtprofiletpscprptlbk-8761)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_TP_SC_PRP_TL_BK_PK | INSTANCE_ID, SECTION_PROP_ID, BUSINESS_GROUP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INSTANCE_ID | NUMBER |  | 18 | Yes | Instance Id |
| SECTION_PROP_ID | NUMBER |  | 18 | Yes | Section Prop Id |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| ATTRIBUTE_LABEL | VARCHAR2 | 240 |  |  | Attribute Label |
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
| HRT_PROFILE_TP_SC_PRP_TL_BK_U1 | Unique | Default | INSTANCE_ID, SECTION_PROP_ID, BUSINESS_GROUP_ID, LANGUAGE, ORA_SEED_SET1 |
| HRT_PROFIL_TP_SC_PRP_TL_BK_U11 | Unique | Default | INSTANCE_ID, SECTION_PROP_ID, BUSINESS_GROUP_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
