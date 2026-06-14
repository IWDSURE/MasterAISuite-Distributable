# WLF_LM_COURSE_PREREQUISITES

This table is used to store Course Prerequisites objects.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcourseprerequisites-16956.html#wlflmcourseprerequisites-16956](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcourseprerequisites-16956.html#wlflmcourseprerequisites-16956)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LM_COURSE_PREREQUISITES_PK | PREREQUISITE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PREREQUISITE_ID | NUMBER |  | 18 | Yes | PREREQUISITE_ID |
| PREREQUISITE_TYPE | VARCHAR2 | 32 |  | Yes | PREREQUISITE_TYPE |
| PREREQUISITE_OWNER_ID | NUMBER |  | 18 | Yes | PREREQUISITE_OWNER_ID |
| MANDATORY_FLAG | VARCHAR2 | 30 |  | Yes | MANDATORY_FLAG |
| COURSE_ID | NUMBER |  | 18 |  | COURSE_ID |
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
| PRQ_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | PRQ_ATTRIBUTE_CATEGORY |
| PRQ_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE1 |
| PRQ_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE2 |
| PRQ_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE3 |
| PRQ_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE4 |
| PRQ_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE5 |
| PRQ_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE6 |
| PRQ_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE7 |
| PRQ_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE8 |
| PRQ_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE9 |
| PRQ_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE10 |
| PRQ_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE11 |
| PRQ_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE12 |
| PRQ_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE13 |
| PRQ_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE14 |
| PRQ_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE15 |
| PRQ_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE16 |
| PRQ_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE17 |
| PRQ_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE18 |
| PRQ_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE19 |
| PRQ_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | PRQ_ATTRIBUTE20 |
| PRQ_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER1 |
| PRQ_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER2 |
| PRQ_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER3 |
| PRQ_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER4 |
| PRQ_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER5 |
| PRQ_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER6 |
| PRQ_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER7 |
| PRQ_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER8 |
| PRQ_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER9 |
| PRQ_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER10 |
| PRQ_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER11 |
| PRQ_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER12 |
| PRQ_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER13 |
| PRQ_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER14 |
| PRQ_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER15 |
| PRQ_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER16 |
| PRQ_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER17 |
| PRQ_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER18 |
| PRQ_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER19 |
| PRQ_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | PRQ_ATTRIBUTE_NUMBER20 |
| PRQ_ATTRIBUTE_DATE1 | DATE |  |  |  | PRQ_ATTRIBUTE_DATE1 |
| PRQ_ATTRIBUTE_DATE2 | DATE |  |  |  | PRQ_ATTRIBUTE_DATE2 |
| PRQ_ATTRIBUTE_DATE3 | DATE |  |  |  | PRQ_ATTRIBUTE_DATE3 |
| PRQ_ATTRIBUTE_DATE4 | DATE |  |  |  | PRQ_ATTRIBUTE_DATE4 |
| PRQ_ATTRIBUTE_DATE5 | DATE |  |  |  | PRQ_ATTRIBUTE_DATE5 |
| PRQ_ATTRIBUTE_DATE6 | DATE |  |  |  | PRQ_ATTRIBUTE_DATE6 |
| PRQ_ATTRIBUTE_DATE7 | DATE |  |  |  | PRQ_ATTRIBUTE_DATE7 |
| PRQ_ATTRIBUTE_DATE8 | DATE |  |  |  | PRQ_ATTRIBUTE_DATE8 |
| PRQ_ATTRIBUTE_DATE9 | DATE |  |  |  | PRQ_ATTRIBUTE_DATE9 |
| PRQ_ATTRIBUTE_DATE10 | DATE |  |  |  | PRQ_ATTRIBUTE_DATE10 |
| PRQ_ATTRIBUTE_DATE11 | DATE |  |  |  | PRQ_ATTRIBUTE_DATE11 |
| PRQ_ATTRIBUTE_DATE12 | DATE |  |  |  | PRQ_ATTRIBUTE_DATE12 |
| PRQ_ATTRIBUTE_DATE13 | DATE |  |  |  | PRQ_ATTRIBUTE_DATE13 |
| PRQ_ATTRIBUTE_DATE14 | DATE |  |  |  | PRQ_ATTRIBUTE_DATE14 |
| PRQ_ATTRIBUTE_DATE15 | DATE |  |  |  | PRQ_ATTRIBUTE_DATE15 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LM_COURSE_PREREQUISITES_U1 | Unique | Default | PREREQUISITE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
