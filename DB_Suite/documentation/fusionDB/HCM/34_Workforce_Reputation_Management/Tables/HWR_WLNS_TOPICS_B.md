# HWR_WLNS_TOPICS_B

The base table for wellness topics.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnstopicsb-23479.html#hwrwlnstopicsb-23479](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnstopicsb-23479.html#hwrwlnstopicsb-23479)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_TOPICS_B_PK | TOPIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TOPIC_ID | NUMBER |  | 18 | Yes | This is the primary key for the hwr_wlns_topics_b table. |
| TOPIC_SOURCE | VARCHAR2 | 10 |  | Yes | This describes the source of the wellness topics, can be seeded, custom. |
| IS_ACTIVE | VARCHAR2 | 5 |  | Yes | A flag indicating active topics to be used. Use Y for true (active) or N for false (not active). |
| PARENT_ID | NUMBER |  | 18 | Yes | This is the parent general topic ID that current topic associated with. |
| CATEGORY_ID | NUMBER |  | 18 | Yes | The category id for wellness general category. |
| CATEGORY_KEY | VARCHAR2 | 400 |  | Yes | The category key for wellness category. |
| TOPIC_KEY | VARCHAR2 | 400 |  | Yes | The topic key for wellness topics. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| WLNS_TOPICS_ATTR_1 | VARCHAR2 | 400 |  |  | This stores wellness topic attribute 1. |
| WLNS_TOPICS_ATTR_2 | VARCHAR2 | 400 |  |  | This stores wellness topic attribute 2. |
| WLNS_TOPICS_ATTR_3 | VARCHAR2 | 400 |  |  | This stores wellness topic attribute 3. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
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
| HWR_WLNS_TOPICS_B_U1 | Unique | Default | TOPIC_ID, ORA_SEED_SET1 |
| HWR_WLNS_TOPICS_B_U11 | Unique | Default | TOPIC_ID, ORA_SEED_SET2 |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
