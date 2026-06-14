# BEN_ACTN_TYP

BEN_ACTN_TYP is an action required to complete enrollment, either for enrollment results or enrollment events.  It includes Requirement to Designate Beneficiary, Designate  Dependent Provide Proof of Good Health,  Obtain Third Party Administrator Approval.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benactntyp-24846.html#benactntyp-24846](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benactntyp-24846.html#benactntyp-24846)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ACTN_TYP_PK | ACTN_TYP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ACTN_TYP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| TYPE_CD | VARCHAR2 | 30 |  |  | Action item type. |  |
| NAME | VARCHAR2 | 240 |  |  | Name of the action item type. |  |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Description. |  |
| EAT_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| EAT_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Action Type Attributes (BEN_ACTN_TYP_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| ACTN_TYP_LVL_CD | VARCHAR2 | 30 |  |  | ACTN_TYP_LVL_CD |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ACTN_TYP_N1 | Non Unique | Default | NAME |
| BEN_ACTN_TYP_PK | Unique | Default | ACTN_TYP_ID, ORA_SEED_SET1 |
| BEN_ACTN_TYP_PK1 | Unique | Default | ACTN_TYP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
