# HRC_LOADER_BATCH_KEY_MAP

This table contains the mapping of keys from other systems into Fusion.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloaderbatchkeymap-23799.html#hrcloaderbatchkeymap-23799](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloaderbatchkeymap-23799.html#hrcloaderbatchkeymap-23799)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_LOADER_BATCH_KEY_MAP_PK | KEY_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| KEY_MAP_ID | NUMBER |  | 18 | Yes | KEY_MAP_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SOURCE_ID | VARCHAR2 | 256 |  |  | SOURCE_ID |
| TARGET_ID | NUMBER |  | 18 |  | TARGET_ID |
| OBJECT_NAME | VARCHAR2 | 256 |  |  | OBJECT_NAME |
| ADDITIONAL_INFO | VARCHAR2 | 256 |  |  | ADDITIONAL_INFO |
| OWNER | VARCHAR2 | 256 |  |  | OWNER |
| STATUS | VARCHAR2 | 100 |  |  | STATUS |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_LOADER_BATCH_KEY_MAP_N1 | Non Unique | Default | OBJECT_NAME, SOURCE_ID |
| HRC_LOADER_BATCH_KEY_MAP_N2 | Non Unique | Default | OBJECT_NAME, TARGET_ID |
| HRC_LOADER_BATCH_KEY_MAP_PK | Unique | Default | KEY_MAP_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
