# HWR_WLNS_TOPIC_MAPPING_XREF

The reference table mapping the coaching topics to wellness topics.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnstopicmappingxref-28276.html#hwrwlnstopicmappingxref-28276](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnstopicmappingxref-28276.html#hwrwlnstopicmappingxref-28276)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_TOPIC_MAPPING_XREF_PK | TOPIC_ID, COACHING_TOPIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TOPIC_ID | NUMBER |  | 18 | Yes | This is the composite key for the table. |
| COACHING_TOPIC_ID | NUMBER |  | 18 | Yes | This is the composite key for the table. |
| IS_ACTIVE | VARCHAR2 | 5 |  | Yes | A flag indicating active topics to be used. Use Y for true (active) or N for false (not active). |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_TOPIC_MAPPING_XREF_U1 | Unique | Default | TOPIC_ID, COACHING_TOPIC_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
