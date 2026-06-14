# HWR_SKILLS_CONNECTOR_B

This table will be used to store the list of configurations for the skill connector.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrskillsconnectorb-20960.html#hwrskillsconnectorb-20960](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrskillsconnectorb-20960.html#hwrskillsconnectorb-20960)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SKILLS_CONNECTOR_B_PK | CONNECTOR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONNECTOR_ID | NUMBER |  | 18 | Yes | This is the Skill connector Id identifying the Skill connector entry in this table. |
| CONNECTOR_TYPE | VARCHAR2 | 64 |  | Yes | This is the connector type . ex : profile |
| CONNECTOR_CONFIG | CLOB |  |  | Yes | The is the connector configuration. should be an xml. |
| DFF_CONFIG_ID | NUMBER |  | 18 |  | This is the DFF Config  Id identifying the DFF CONFIG entry in the HWR_DFF_CONFIG_B. |
| APPLICATION_ID | NUMBER |  | 18 |  | This is the  Id identifying an application (FND_APPLICATION) |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SKILLS_CONNECTOR_B_N1 | Non Unique | Default | DFF_CONFIG_ID |
| HWR_SKILLS_CONNECTOR_B_N2 | Non Unique | Default | APPLICATION_ID |
| HWR_SKILLS_CONNECTOR_B_U1 | Unique | Default | CONNECTOR_ID, ORA_SEED_SET1 |
| HWR_SKILLS_CONNECTOR_B_U11 | Unique | Default | CONNECTOR_ID, ORA_SEED_SET2 |
| HWR_SKILLS_CONNECTOR_B_U2 | Unique | Default | CONNECTOR_TYPE, ORA_SEED_SET1 |
| HWR_SKILLS_CONNECTOR_B_U21 | Unique | Default | CONNECTOR_TYPE, ORA_SEED_SET2 |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
