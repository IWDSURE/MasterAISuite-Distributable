# PER_ALL_PEOPLE_F

This table will store core personal data that is not expected to vary by Legislation Code, or has need of a global value that is independent of the Legislation Code context.	Data is stored with date effectivity, but need not functionally change over time. Values that are static over time will be duplicated to each new date effective instance of a row with the same person_id.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perallpeoplef-16815.html#perallpeoplef-16815](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perallpeoplef-16815.html#perallpeoplef-16815)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PEOPLE_F_PK | PERSON_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PERSON_ID | NUMBER |  | 18 | Yes | System generated part of the primary key. Surrogate key. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| START_DATE | DATE |  |  | Yes | Denormalized record of the effective_start_date of the earliest row for this person_id. Establishes the date when the person was created on the system. |  |
| APPLICANT_NUMBER | VARCHAR2 | 30 |  |  | Unique number for people who are applicants. This is in addition to PERSON_NUMBER. Allows global tracking of applicants. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| PERSON_NUMBER | VARCHAR2 | 30 |  | Yes | Number assigned to the person, to identify the person uniquely in any context, not dependent on being an employee, contingent worker, etc. |  |
| WAIVE_DATA_PROTECT | VARCHAR2 | 30 |  | Yes | This column is not currently used. |  |
| PRIMARY_EMAIL_ID | NUMBER |  | 18 |  | Refers to the row on PER_EMAIL_ADDRESSES that should be considered the primary email of the person |  |
| PRIMARY_PHONE_ID | NUMBER |  | 18 |  | Refers to the row on PER_PHONES that should be considered the primary phone of the person |  |
| MAILING_ADDRESS_ID | NUMBER |  | 18 |  | Identifies which address from PER_ADDRESSES is considered the mailing address for the person (note there is a similar column at Assignment level for recording taxation address details. This address does not have to serve that purpose). |  |
| PRIMARY_NID_ID | NUMBER |  | 18 |  | Refers to the row on PER_NATIONAL_IDENTIFIERS that should be considered the primary national identifier for the person. |  |
| PRIMARY_NID_NUMBER | VARCHAR2 | 30 |  |  | Denormalised value of the National ID number from the primary National ID row. |  |
| ATTRIBUTE31 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE32 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE33 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE34 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE35 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE36 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE37 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE38 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE39 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE40 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE41 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE42 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE43 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE44 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE45 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE46 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE47 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE48 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE49 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE50 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | All People Attributes (PER_ALL_PEOPLE_DFF) |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ALL_PEOPLE_F_N1 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_ALL_PEOPLE_F_N2 | Non Unique | Default | UPPER("PERSON_NUMBER"), EFFECTIVE_END_DATE, EFFECTIVE_START_DATE |
| PER_ALL_PEOPLE_F_N3 | Non Unique | Default | PRIMARY_EMAIL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_ALL_PEOPLE_F_N4 | Non Unique | Default | MAILING_ADDRESS_ID |
| PER_ALL_PEOPLE_F_N5 | Non Unique | Default | PRIMARY_NID_ID |
| PER_ALL_PEOPLE_F_N6 | Non Unique | Default | PRIMARY_PHONE_ID |
| PER_PEOPLE_F_N52 | Non Unique | Default | APPLICANT_NUMBER |
| PER_PEOPLE_F_PK | Unique | Default | PERSON_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_PEOPLE_F_U1 | Unique | Default | BUSINESS_GROUP_ID, UPPER("PERSON_NUMBER"), EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
