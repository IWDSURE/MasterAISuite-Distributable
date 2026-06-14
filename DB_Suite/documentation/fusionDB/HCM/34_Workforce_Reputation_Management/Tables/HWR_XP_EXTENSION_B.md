# HWR_XP_EXTENSION_B

This is the table for the experience store extensions.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpextensionb-12788.html#hwrxpextensionb-12788](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpextensionb-12788.html#hwrxpextensionb-12788)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_XP_EXTENSION_B_PK | EXTENSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXTENSION_ID | NUMBER |  | 18 | Yes | The Unique database identifier for this extension. |
| CONTEXT_ID | NUMBER |  | 18 |  | The Unique database identifier for the context. |
| ACTIVITY_ID | NUMBER |  | 18 |  | The Unique database identifier for this activity. |
| RESULT_ID | NUMBER |  | 18 |  | The Unique database identifier for this result. |
| ID_IRI | VARCHAR2 | 2000 |  | Yes | The id iri for this extension. The ID should follow the IRI sandard. |
| VALUE | VARCHAR2 | 4000 |  |  | The value for this extension. Can be null. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_XP_EXTENSION_B_N1 | Non Unique | Default | CONTEXT_ID |
| HWR_XP_EXTENSION_B_N2 | Non Unique | Default | ACTIVITY_ID |
| HWR_XP_EXTENSION_B_N3 | Non Unique | Default | RESULT_ID |
| HWR_XP_EXTENSION_B_U1 | Unique | Default | EXTENSION_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
