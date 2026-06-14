# HWR_PUBLICATION_B

The publication table stores profile publication data.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrpublicationb-31788.html#hwrpublicationb-31788](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrpublicationb-31788.html#hwrpublicationb-31788)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PUBLICATION_B_PK | SOURCE_ID, PUBLICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PUBLICATION_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the publication table. |
| SOURCE_ID | NUMBER |  | 18 | Yes | The Id of the source for this publication. |
| AUTHORS | VARCHAR2 | 1000 |  |  | The list of authors for this publication. |
| PUBLICATION_DATE | TIMESTAMP |  |  |  | The publication date of this publication. |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | The description of this publication. |
| TITLE | VARCHAR2 | 100 |  |  | The original title of this publication. |
| PUBLICATION_TYPE | VARCHAR2 | 100 |  |  | The publication type of this publication. |
| URL | VARCHAR2 | 4000 |  |  | The URL for accessing this publication. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_PUBLICATION_B_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, PUBLICATION_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
