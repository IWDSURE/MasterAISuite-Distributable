# HXT_TCLAYSET_TAF

The table HXT_TCLAYST_TAF table contains the list of time repository attributes that are supported by a given layout set.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttclaysettaf-17438.html#hxttclaysettaf-17438](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttclaysettaf-17438.html#hxttclaysettaf-17438)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_TCLAYSET_TAF_PK | TCLAYSET_TAF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCLAYSET_TAF_ID | NUMBER |  | 18 | Yes | TCLAYSET_TAF_ID |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| TAF_ID | NUMBER |  | 18 | Yes | TAF_ID |
| LAYOUTSET_ID | NUMBER |  | 18 | Yes | LAYOUTSET_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_TCLAYSET_TAF_PK | Unique | Default | TCLAYSET_TAF_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
