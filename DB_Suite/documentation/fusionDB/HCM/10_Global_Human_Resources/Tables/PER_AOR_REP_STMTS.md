# PER_AOR_REP_STMTS

This table holds the details of sql statements and these sqls will be used to calculate assignment representatives.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraorrepstmts-31529.html#peraorrepstmts-31529](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraorrepstmts-31529.html#peraorrepstmts-31529)

## Primary Key

| Name | Columns |
|------|----------|
| PER_AOR_REP_STMTS_PK | SCOPE_ATTRS_LIST |

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| SCOPE_ATTRS_LIST | VARCHAR2 | 4000 | Yes | This is list of Scope Attributes combination. |
| AORS_COUNT | NUMBER |  |  | This is number of AOR Rows with this combination. |
| SQL_STMT | CLOB |  |  | AOR Row SQL statement |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_AOR_REP_STMTS_PK | Unique | Default | SCOPE_ATTRS_LIST |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
