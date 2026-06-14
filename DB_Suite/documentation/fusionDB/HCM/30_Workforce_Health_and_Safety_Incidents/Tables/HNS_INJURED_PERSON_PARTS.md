# HNS_INJURED_PERSON_PARTS

HNS INJURED PERSON PARTS. This table stores body part information for an injured person.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinjuredpersonparts-30918.html#hnsinjuredpersonparts-30918](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinjuredpersonparts-30918.html#hnsinjuredpersonparts-30918)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_INJURED_PERSONS_PART_PK | INJURED_PERSON_PART_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INJURED_PERSON_PART_ID | NUMBER |  | 18 | Yes | Primary key for table HNS_INJURED_PERSON_PARTS |
| INJURED_PERSON_ID | NUMBER |  | 18 | Yes | Injured person identifier. Foreign key for HNS_INJURED_PERSONS table. |
| INJURED_PART_CODE | VARCHAR2 | 30 |  | Yes | Injured person part identifer. Lookup key for  FND_LOOKUP HNS_INJURED_PART. |
| INJURY_NATURE_CODE | VARCHAR2 | 1000 |  | Yes | INJURY_NATURE_CODE column :  The nature of injury. This is a lookup from FND_LOOKUP  NATURE. This is a comma delimited field with multiple nature_codes per injiured_part. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Flag to check whether is record is deleted. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_INJURED_PERSON_PARTS_N1 | Non Unique | FUSION_TS_TX_DATA | INJURED_PERSON_ID |
| HNS_INJURED_PERSON_PARTS_UK1 | Unique | FUSION_TS_TX_DATA | INJURED_PERSON_PART_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
