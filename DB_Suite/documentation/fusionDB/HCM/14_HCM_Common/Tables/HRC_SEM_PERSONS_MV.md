# HRC_SEM_PERSONS_MV

This table is to store the mutli-value fields associated with a person.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsempersonsmv-20579.html#hrcsempersonsmv-20579](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsempersonsmv-20579.html#hrcsempersonsmv-20579)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_PERSONS_MV_PK | PERSON_MV_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_MV_ID | NUMBER |  | 18 | Yes | This is the primary column of Person multi-value table. |
| PERSON_ID | NUMBER |  | 18 | Yes | This is the primary key of the person table. |
| PERSON_LANGUAGE | VARCHAR2 | 512 |  |  | The languages that a candidate knows |
| LICENSE | VARCHAR2 | 512 |  |  | The title of the license or certification |
| POOL | VARCHAR2 | 512 |  |  | The pools that the candidate is a member of |
| JOB | VARCHAR2 | 512 |  |  | The jobs that the candidate has applied to |
| IS_ERROR | NUMBER |  | 8 |  | This column indicates if there is an error in indexing event. |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | This column contains the error message of the indexing event. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SEM_PERSONS_MV_N1 | Non Unique | FUSION_TS_TX_DATA | PERSON_ID |
| HRC_SEM_PERSONS_MV_U1 | Unique | FUSION_TS_TX_DATA | PERSON_MV_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
