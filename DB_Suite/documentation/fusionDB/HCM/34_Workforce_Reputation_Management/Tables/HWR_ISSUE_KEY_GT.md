# HWR_ISSUE_KEY_GT

This is a global temporary table to help with in queries on the HWR_ISSUE_B table.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrissuekeygt-26507.html#hwrissuekeygt-26507](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrissuekeygt-26507.html#hwrissuekeygt-26507)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SOURCE_ID | NUMBER |  | 18 | Yes | This is the id of the source on the HWR_SOURCE_B table. |
| CONTROL_KEY | VARCHAR2 | 64 |  | Yes | This is the control_key on the HWR_REP_CONTROL_B table. |
| SRC_POST_ID | VARCHAR2 | 500 |  | Yes | This is the source post id for the post. |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
