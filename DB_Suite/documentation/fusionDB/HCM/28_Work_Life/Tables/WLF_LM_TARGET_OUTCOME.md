# WLF_LM_TARGET_OUTCOME

This table is used to store target outcome objects.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmtargetoutcome-31778.html#wlflmtargetoutcome-31778](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmtargetoutcome-31778.html#wlflmtargetoutcome-31778)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LM_TARGET_OUTCOME_PK | TARGET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TARGET_ID | NUMBER |  | 18 | Yes | TARGET_ID |
| TARGET_TYPE | VARCHAR2 | 32 |  | Yes | TARGET_TYPE |
| TARGET_OWNER_ID | NUMBER |  | 18 | Yes | TARGET_OWNER_ID |
| MARKING_FLAG | VARCHAR2 | 30 |  | Yes | MARKING_FLAG |
| PROFILE_CONTENT_TYPE_ID | NUMBER |  | 18 |  | PROFILE_CONTENT_TYPE_ID |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | CONTENT_ITEM_ID |
| CONTENT_ITEM_RATING | NUMBER |  | 18 |  | CONTENT_ITEM_RATING |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TRG_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | TRG_ATTRIBUTE_CATEGORY |
| TRG_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE1 |
| TRG_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE2 |
| TRG_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE3 |
| TRG_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE4 |
| TRG_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE5 |
| TRG_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE6 |
| TRG_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE7 |
| TRG_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE8 |
| TRG_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE9 |
| TRG_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE10 |
| TRG_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE11 |
| TRG_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE12 |
| TRG_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE13 |
| TRG_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE14 |
| TRG_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE15 |
| TRG_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE16 |
| TRG_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE17 |
| TRG_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE18 |
| TRG_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE19 |
| TRG_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | TRG_ATTRIBUTE20 |
| TRG_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER1 |
| TRG_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER2 |
| TRG_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER3 |
| TRG_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER4 |
| TRG_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER5 |
| TRG_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER6 |
| TRG_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER7 |
| TRG_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER8 |
| TRG_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER9 |
| TRG_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER10 |
| TRG_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER11 |
| TRG_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER12 |
| TRG_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER13 |
| TRG_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER14 |
| TRG_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER15 |
| TRG_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER16 |
| TRG_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER17 |
| TRG_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER18 |
| TRG_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER19 |
| TRG_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | TRG_ATTRIBUTE_NUMBER20 |
| TRG_ATTRIBUTE_DATE1 | DATE |  |  |  | TRG_ATTRIBUTE_DATE1 |
| TRG_ATTRIBUTE_DATE2 | DATE |  |  |  | TRG_ATTRIBUTE_DATE2 |
| TRG_ATTRIBUTE_DATE3 | DATE |  |  |  | TRG_ATTRIBUTE_DATE3 |
| TRG_ATTRIBUTE_DATE4 | DATE |  |  |  | TRG_ATTRIBUTE_DATE4 |
| TRG_ATTRIBUTE_DATE5 | DATE |  |  |  | TRG_ATTRIBUTE_DATE5 |
| TRG_ATTRIBUTE_DATE6 | DATE |  |  |  | TRG_ATTRIBUTE_DATE6 |
| TRG_ATTRIBUTE_DATE7 | DATE |  |  |  | TRG_ATTRIBUTE_DATE7 |
| TRG_ATTRIBUTE_DATE8 | DATE |  |  |  | TRG_ATTRIBUTE_DATE8 |
| TRG_ATTRIBUTE_DATE9 | DATE |  |  |  | TRG_ATTRIBUTE_DATE9 |
| TRG_ATTRIBUTE_DATE10 | DATE |  |  |  | TRG_ATTRIBUTE_DATE10 |
| TRG_ATTRIBUTE_DATE11 | DATE |  |  |  | TRG_ATTRIBUTE_DATE11 |
| TRG_ATTRIBUTE_DATE12 | DATE |  |  |  | TRG_ATTRIBUTE_DATE12 |
| TRG_ATTRIBUTE_DATE13 | DATE |  |  |  | TRG_ATTRIBUTE_DATE13 |
| TRG_ATTRIBUTE_DATE14 | DATE |  |  |  | TRG_ATTRIBUTE_DATE14 |
| TRG_ATTRIBUTE_DATE15 | DATE |  |  |  | TRG_ATTRIBUTE_DATE15 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LM_TARGET_OUTCOME_U1 | Unique | Default | TARGET_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
