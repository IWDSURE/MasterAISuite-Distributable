# HRC_DL_SOURCE_KEY_AUDIT

HRC_DL_SOURCE_KEY_AUDIT maintains information on update of source keys.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlsourcekeyaudit-15275.html#hrcdlsourcekeyaudit-15275](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlsourcekeyaudit-15275.html#hrcdlsourcekeyaudit-15275)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_SOURCE_KEY_AUDIT_PK | SOURCE_KEY_AUDIT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SOURCE_KEY_AUDIT_ID | NUMBER |  | 18 | Yes | AUDIT_ID |
| FUSION_GUID | VARCHAR2 | 64 |  | Yes | FUSION_GUID |
| SURROGATE_ID | NUMBER |  | 18 | Yes | SURROGATE_ID |
| INTEGRATION_OBJECT_NAME | VARCHAR2 | 256 |  | Yes | INTEGRATION_OBJECT_NAME |
| OLD_SOURCE_OWNER | VARCHAR2 | 256 |  | Yes | OLD_SOURCE_OWNER |
| OLD_SOURCE_ID | VARCHAR2 | 2000 |  | Yes | OLD_SOURCE_ID |
| NEW_SOURCE_OWNER | VARCHAR2 | 256 |  | Yes | NEW_SOURCE_OWNER |
| NEW_SOURCE_ID | VARCHAR2 | 2000 |  | Yes | NEW_SOURCE_ID |
| REASON | VARCHAR2 | 4000 |  |  | REASON |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_SOURCE_KEY_AUDIT_N1 | Non Unique | Default | FUSION_GUID |
| HRC_DL_SOURCE_KEY_AUDIT_N2 | Non Unique | Default | INTEGRATION_OBJECT_NAME, SURROGATE_ID |
| HRC_DL_SOURCE_KEY_AUDIT_N3 | Non Unique | Default | INTEGRATION_OBJECT_NAME, OLD_SOURCE_OWNER, OLD_SOURCE_ID |
| HRC_DL_SOURCE_KEY_AUDIT_U1 | Unique | Default | SOURCE_KEY_AUDIT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
