# HWR_EDUCATION_B

The education table stores profile education data.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwreducationb-24223.html#hwreducationb-24223](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwreducationb-24223.html#hwreducationb-24223)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_EDUCATION_B_PK | SOURCE_ID, EDUCATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EDUCATION_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the education table. |
| SOURCE_ID | NUMBER |  | 18 | Yes | The Id of the source for the profile which has the education. |
| ACTIVITIES | VARCHAR2 | 1000 |  |  | The list of activities the person participated in. |
| DEGREE | VARCHAR2 | 255 |  |  | The degree awarded to the person. |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | The description of the education. |
| END_DATE | TIMESTAMP |  |  |  | The date the person completed education. |
| FIELD_OF_STUDY | VARCHAR2 | 255 |  |  | The field of study of the person. |
| SCHOOL_INSTITUTION_NAME | VARCHAR2 | 255 |  |  | The name of the school or institution at which education took place. |
| START_DATE | TIMESTAMP |  |  |  | The date the person began education. |
| EDUCATION_TYPE | VARCHAR2 | 100 |  |  | The education type of the education. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_EDUCATION_B_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, EDUCATION_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
