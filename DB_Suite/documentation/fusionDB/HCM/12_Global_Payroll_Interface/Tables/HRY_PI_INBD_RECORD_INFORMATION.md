# HRY_PI_INBD_RECORD_INFORMATION

Stores details about payrolls processed by third-party payroll providers, such as earnings, deductions, and messages.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypiinbdrecordinformation-9557.html#hrypiinbdrecordinformation-9557](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypiinbdrecordinformation-9557.html#hrypiinbdrecordinformation-9557)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_PI_INBD_RECORD_INFO_PK | INBD_RECORD_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INBD_RECORD_INFO_ID | NUMBER |  | 18 | Yes | Primary Key for Inbound Record |
| INBD_RECORD_ID | NUMBER |  | 18 | Yes | Foreign key to HRY_PI_INBD_RECORDS |
| IRI_INFORMATION_CONTEXT | VARCHAR2 | 30 |  | Yes | Descriptive Flexfield: structure definition of the descriptive flexfield. |
| IRI_INFORMATION1 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION2 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION3 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION4 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION5 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION6 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION7 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION8 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION9 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION10 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION11 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION12 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION13 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION14 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION15 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION16 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION17 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION18 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION19 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION20 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION21 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION22 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION23 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION24 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION25 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION26 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION27 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION28 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION29 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION30 | VARCHAR2 | 150 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION31 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION32 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION33 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION34 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION35 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION36 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION37 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION38 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION39 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION40 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION41 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION42 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION43 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION44 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION45 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION46 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION47 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION48 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION49 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION50 | VARCHAR2 | 200 |  |  | Information Column to hold Character data type |
| IRI_INFORMATION_NUMBER1 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER2 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER3 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER4 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER5 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER6 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER7 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER8 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER9 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER10 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER11 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER12 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER13 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER14 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER15 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER16 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER17 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER18 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER19 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER20 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER21 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER22 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER23 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER24 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER25 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER26 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER27 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER28 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER29 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_NUMBER30 | NUMBER |  |  |  | Information Column to hold Number data type |
| IRI_INFORMATION_DATE1 | DATE |  |  |  | Information Column to hold Date data type |
| IRI_INFORMATION_DATE2 | DATE |  |  |  | Information Column to hold Date data type |
| IRI_INFORMATION_DATE3 | DATE |  |  |  | Information Column to hold Date data type |
| IRI_INFORMATION_DATE4 | DATE |  |  |  | Information Column to hold Date data type |
| IRI_INFORMATION_DATE5 | DATE |  |  |  | Information Column to hold Date data type |
| IRI_INFORMATION_DATE6 | DATE |  |  |  | Information Column to hold Date data type |
| IRI_INFORMATION_DATE7 | DATE |  |  |  | Information Column to hold Date data type |
| IRI_INFORMATION_DATE8 | DATE |  |  |  | Information Column to hold Date data type |
| IRI_INFORMATION_DATE9 | DATE |  |  |  | Information Column to hold Date data type |
| IRI_INFORMATION_DATE10 | DATE |  |  |  | Information Column to hold Date data type |
| IRI_INFORMATION_DATE11 | DATE |  |  |  | Information Column to hold Date data type |
| IRI_INFORMATION_DATE12 | DATE |  |  |  | Information Column to hold Date data type |
| IRI_INFORMATION_DATE13 | DATE |  |  |  | Information Column to hold Date data type |
| IRI_INFORMATION_DATE14 | DATE |  |  |  | Information Column to hold Date data type |
| IRI_INFORMATION_DATE15 | DATE |  |  |  | Information Column to hold Date data type |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_PI_INBD_RECORD_INFO_N1 | Non Unique | FUSION_TS_TX_IDX | INBD_RECORD_ID, IRI_INFORMATION_CONTEXT |
| HRY_PI_INBD_RECORD_INFO_PK | Unique | FUSION_TS_TX_IDX | INBD_RECORD_INFO_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
