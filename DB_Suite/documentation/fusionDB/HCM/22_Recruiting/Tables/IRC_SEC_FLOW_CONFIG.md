# IRC_SEC_FLOW_CONFIG

This table is used to store secondary flow  configuration based on candidate selection process action context (IRC_STEP_ACTION_USAGES_B.STEP_ACTION_USAGE_ID).

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsecflowconfig-3270.html#ircsecflowconfig-3270](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsecflowconfig-3270.html#ircsecflowconfig-3270)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_SEC_FLOW_CONFIG_PK | SEC_FLOW_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEC_FLOW_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for the table. System generated. |
| STEP_ACTION_USAGE_ID | NUMBER |  | 18 | Yes | CSP step with for which this configuration is being created.Foreign key IRC_STEP_ACTION_USAGES_B table. (Life cycle action context) |
| APPLY_FLOW_ID | NUMBER |  | 18 |  | Secondary flow  type  is to be used for capturing candidate data. Foreign key IRC_APPLY_FLOWS_B.APPLY_FLOW_ID |
| CAND_NOTIF_TMPL_ID | NUMBER |  | 18 |  | Email template that is to be used for  candidate automatic notifications. Foreign key IRC_DESCRIPTIONS_B.DESCRIPTION_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_SEC_FLOW_CONFIG_FK1 | Unique | Default | STEP_ACTION_USAGE_ID |
| IRC_SEC_FLOW_CONFIG_FK2 | Non Unique | Default | APPLY_FLOW_ID |
| IRC_SEC_FLOW_CONFIG_FK3 | Non Unique | Default | CAND_NOTIF_TMPL_ID |
| IRC_SEC_FLOW_CONFIG_PK | Unique | Default | SEC_FLOW_CONFIG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
