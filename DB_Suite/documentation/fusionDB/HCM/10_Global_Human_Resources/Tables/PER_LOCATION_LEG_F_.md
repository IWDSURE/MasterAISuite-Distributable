# PER_LOCATION_LEG_F_

PER_LOCATION_LEG_F stores the legislative attributes for a Location

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocationlegf-15578.html#perlocationlegf-15578](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocationlegf-15578.html#perlocationlegf-15578)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LOCATION_LEG_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, LOCATION_LEG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOCATION_LEG_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |
| LOCATION_ID | NUMBER |  | 18 |  | Foreign Key to PER_LOCATIONS table. |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES. |
| SEQUENCE_NUMBER | NUMBER |  | 8 |  | Sequence Number for multi row contexts |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LLE_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| LLE_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| LLE_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| LLE_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Who column: indicates the impersonator who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_LOCATION_LEG_FN1_ | Non Unique | Default | LOCATION_LEG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_LOCATION_LEG_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, LOCATION_LEG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_LOCATION_LEG_U2_ | Unique | Default | LAST_UPDATED_BY, LAST_UPDATE_DATE, LOCATION_LEG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
