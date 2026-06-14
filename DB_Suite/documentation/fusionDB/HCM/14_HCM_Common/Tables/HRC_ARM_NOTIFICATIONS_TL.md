# HRC_ARM_NOTIFICATIONS_TL

Approval model Table: This holds the translatable details of HRC_ARM_NOTIFICATIONS_B table

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcarmnotificationstl-24457.html#hrcarmnotificationstl-24457](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcarmnotificationstl-24457.html#hrcarmnotificationstl-24457)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ARM_NOTIFICATIONS_TL_PK | NOTIFICATION_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NOTIFICATION_ID | NUMBER |  | 18 | Yes | Primary Key and unique identifier |
| NOTIFICATION_HEADER | VARCHAR2 | 240 |  |  | Header to be attached to the Notification |
| NOTIFICATION_CONTENT | VARCHAR2 | 240 |  |  | Content attached to the Notification |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identify the ENTERPRISE  to which the composite belongs.  
Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ARM_NOTIFICATIONS_TL_N1 | Non Unique | Default | LAST_UPDATE_DATE |
| HRC_ARM_NOTIFICATIONS_TL_PK | Unique | Default | NOTIFICATION_ID, LANGUAGE |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
