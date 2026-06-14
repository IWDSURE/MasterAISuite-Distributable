# HRC_EVT_OBJ_HANDLER_USAGES

Contains mapping of handlers and conditions for the given reference type and id

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** hrc_evt_obj_handler_usages

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtobjhandlerusages-11089.html#hrcevtobjhandlerusages-11089](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtobjhandlerusages-11089.html#hrcevtobjhandlerusages-11089)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_OBJ_HANDLER_USAGES_PK | OBJ_INST_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJ_INST_USAGE_ID | NUMBER |  | 18 | Yes | Unique Identifier |
| EVENT_HANDLER_ID | NUMBER |  | 18 | Yes | Identifier of Event Handler |
| OBJ_CONDITION_ID | NUMBER |  | 18 | Yes | Identifier of Objecct Condition |
| OBJ_INST_REF_TYPE | VARCHAR2 | 200 |  | Yes | Identifier of Objecct Ref Type eg: ABS_PLAN |
| OBJ_INST_REF_ID | VARCHAR2 | 200 |  | Yes | Identifier of Objecct Ref Id eg: XYZ |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_EVT_OBJ_HANDLER_USAGES_N1 | Non Unique | HRC_EVT_OBJ_HANDLER_USAGES_U1 | EVENT_HANDLER_ID, OBJ_CONDITION_ID |
| HRC_EVT_OBJ_HANDLER_USAGES_PK | Unique | HRC_EVT_OBJ_HANDLER_USAGES_PK | OBJ_INST_USAGE_ID |
| HRC_EVT_OBJ_HANDLER_USAGES_U2 | Unique | HRC_EVT_OBJ_HANDLER_USAGES_U2 | OBJ_INST_REF_TYPE, OBJ_INST_REF_ID, OBJ_CONDITION_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
