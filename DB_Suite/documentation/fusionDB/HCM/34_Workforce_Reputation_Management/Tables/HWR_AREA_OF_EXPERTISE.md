# HWR_AREA_OF_EXPERTISE

This table stores area of expertise information

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrareaofexpertise-21043.html#hwrareaofexpertise-21043](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrareaofexpertise-21043.html#hwrareaofexpertise-21043)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_AREA_OF_EXPERTISE_PK | PERSON_ID, AREA_OF_EXPERTISE_CODE, AREA_OF_EXPERTISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_ID | NUMBER |  | 18 | Yes | This is the person ID of the profile for which area of expertise info is stored |
| AREA_OF_EXPERTISE_CODE | VARCHAR2 | 64 |  | Yes | This columns stores the area of expertise code. |
| AREA_OF_EXPERTISE_ID | VARCHAR2 | 4000 |  | Yes | This column stores the area of expertise. |
| EXPERTISE_ORDER | NUMBER |  | 18 |  | This column stores the order of area of expertise. |
| AOE_ATTR_1 | VARCHAR2 | 200 |  |  | AOE_ATTR_1: This is an extra column in case if needed |
| AOE_ATTR_2 | VARCHAR2 | 200 |  |  | AOE_ATTR_2: This is an extra column in case if needed |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_AREA_OF_EXPERTISE_U1 | Unique | Default | PERSON_ID, AREA_OF_EXPERTISE_CODE, AREA_OF_EXPERTISE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
