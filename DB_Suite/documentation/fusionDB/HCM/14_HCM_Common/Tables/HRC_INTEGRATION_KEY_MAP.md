# HRC_INTEGRATION_KEY_MAP

HRC_INTEGRATION_KEY_MAP stores the  Integration Key Map definitions.  SurrogateId and SourceSystem id Key-Mapping is stored in this table

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcintegrationkeymap-17740.html#hrcintegrationkeymap-17740](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcintegrationkeymap-17740.html#hrcintegrationkeymap-17740)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_INTEGRATION_KEY_MAP_PK | GUID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| OBJECT_NAME | VARCHAR2 | 256 |  | Yes | OBJECT_NAME |  |
| GUID | RAW | 16 |  | Yes | GUID |  |
| SURROGATE_ID | NUMBER |  | 18 | Yes | SURROGATE_ID |  |
| SOURCE_SYSTEM_OWNER | VARCHAR2 | 256 |  | Yes | SOURCE_SYSTEM_OWNER |  |
| SOURCE_SYSTEM_ID | VARCHAR2 | 2000 |  | Yes | SOURCE_SYSTEM_ID |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| ORA_PART_KEY | DATE |  |  | Yes | The partition key used to determine the range interval. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_INTEGRATION_KEY_MAP_U1 | Unique | FUSION_TS_TX_DATA | OBJECT_NAME, SURROGATE_ID |
| HRC_INTEGRATION_KEY_MAP_U2 | Unique | Default | GUID |
| HRC_INTEGRATION_KEY_MAP_UK2 | Unique | Default | SOURCE_SYSTEM_ID, SOURCE_SYSTEM_OWNER, OBJECT_NAME |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
