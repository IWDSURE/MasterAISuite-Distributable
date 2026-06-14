# HWR_PER_ORGANIZATION_B

The organization table is used to store the identity of an organization.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperorganizationb-12710.html#hwrperorganizationb-12710](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperorganizationb-12710.html#hwrperorganizationb-12710)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PER_ORGANIZATION_B_PK | HWR_ORG_ID |

## Columns

| Name | Datatype | Length | Not-null | Comments | Status |
|---|---|---|---|---|---|
| HWR_ORG_ID | VARCHAR2 | 500 | Yes | This is the primary key for the organization tables. The number should be generated from the sequence. |  |
| ORG_SIZE | NUMBER |  | Yes | The number of employees in an organization. | Active |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_PER_ORGANIZATION_B_U1 | Unique | FUSION_TS_TX_DATA | HWR_ORG_ID | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
