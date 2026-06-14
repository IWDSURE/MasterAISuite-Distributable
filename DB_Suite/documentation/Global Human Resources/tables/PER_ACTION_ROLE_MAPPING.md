# PER_ACTION_ROLE_MAPPING

This table stores all the roles based on which an action need to be filtered

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractionrolemapping-24558.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractionrolemapping-24558.html)

## Primary Key

| Name | Columns |
|------|----------|
| per_action_role_mapping_PK | ACT_ROLE_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACT_ROLE_MAP_ID | NUMBER |  | 18 | Yes | ACT_ROLE_MAP_ID |
| ROLE_ID | NUMBER |  | 18 |  | ROLE_ID |
| ACTION_TYPE_CODE | VARCHAR2 | 30 |  |  | ACTION_TYPE_CODE |
| TYPE | VARCHAR2 | 10 |  |  | Possible values ACTION/USAGE |
| ACT_USG_ID | NUMBER |  | 18 | Yes | Action id or Action Reason Usage Id |
| ROLE_COMMON_NAME | VARCHAR2 | 4000 |  | Yes | Role Common Name from PER_ROLES_DN_VL table |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| per_action_role_mapping_PK | Unique | Default | ACT_ROLE_MAP_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
