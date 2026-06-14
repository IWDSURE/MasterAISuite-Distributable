# HWR_WLNS_COACH_TOPIC_XREF

This is a reference table mapping coaches with coaching topics.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnscoachtopicxref-29793.html#hwrwlnscoachtopicxref-29793](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnscoachtopicxref-29793.html#hwrwlnscoachtopicxref-29793)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_COACH_TOPIC_XREF_PK | COACHING_TOPIC_ID, COACH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COACHING_TOPIC_ID | NUMBER |  | 18 | Yes | This is the composite key, indicates the coaching topic identifier for the table. |
| COACH_ID | NUMBER |  | 18 | Yes | This is the composite key, indicates the coach identifier mapped to a coaching topic for the table. |
| IS_ACTIVE | VARCHAR2 | 5 |  | Yes | This column indicates the active status for the mapping of a caoching topic with a wellness coach. Use Y for true (active) or N for false (not active). |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_COACH_TOPIC_XREF_U1 | Unique | Default | COACHING_TOPIC_ID, COACH_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
