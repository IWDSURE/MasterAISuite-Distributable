# PER_ACT_OCCURRENCE_EXTRA_INFO

This table defines the extra information for action occurrences for an action

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractoccurrenceextrainfo-15772.html#peractoccurrenceextrainfo-15772](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractoccurrenceextrainfo-15772.html#peractoccurrenceextrainfo-15772)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ACT_OCCUR_EXTRA_INFO_PK | AOEI_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ACTION_OCCURRENCES table. |
| CONTEXT_CODE | VARCHAR2 | 80 |  | Yes | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AOEI_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SEQUENCE_NUMBER | NUMBER |  | 8 |  | Sequence of Numbers |
| AOEI_INFORMATION1 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION2 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION3 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION4 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION5 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION6 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION7 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION8 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION9 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION10 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION11 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION12 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION13 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION14 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION15 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION16 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION17 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION18 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION19 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION20 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION21 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION22 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION23 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION24 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION25 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION26 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION27 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION28 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION29 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION30 | VARCHAR2 | 200 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION31 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION32 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION33 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION34 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION35 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION36 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION37 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION38 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION39 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION40 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION41 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION42 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION43 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION44 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION45 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION46 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION47 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION48 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION49 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION50 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION51 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION52 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION53 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION54 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION55 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION56 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION57 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION58 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION59 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION60 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AOEI_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CATEGORY_CODE | VARCHAR2 | 80 |  |  | COLUMN1 |
| AOEI_ID | NUMBER |  | 18 | Yes | System generated primary key. Surrogate Key. |
| ATTRIBUTE1 | VARCHAR2 | 20 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  | 1 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ACT_OCCUR_EXTRA_INFO_N1 | Non Unique | FUSION_TS_TX_DATA | ACTION_OCCURRENCE_ID |
| PER_ACT_OCCUR_EXTRA_INFO_PK | Unique | FUSION_TS_TX_DATA | AOEI_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
