# HRC_SDL_MAPS

This table store details about business objects.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdlmaps-28336.html#hrcsdlmaps-28336](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdlmaps-28336.html#hrcsdlmaps-28336)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SDL_MAPS_PK | BO_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BO_MAP_ID | NUMBER |  | 18 | Yes | BO_MAP_ID |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| DATE_EFFECTIVITY_TYPE | VARCHAR2 | 30 |  | Yes | DATE_EFFECTIVITY_TYPE |
| EXTENSIBLE_FLEXFIELD_FLAG | VARCHAR2 | 4 |  | Yes | EXTENSIBLE_FLEXFIELD_FLAG |
| TRANSLATION_FLAG | VARCHAR2 | 4 |  | Yes | TRANSLATION_FLAG |
| HASH_VALUE | VARCHAR2 | 100 |  | Yes | HASH_VALUE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LESD_CHANGE_ALLOWED_FLAG | VARCHAR2 | 4 |  |  | LESD_CHANGE_ALLOWED_FLAG |
| LEED_CHANGE_ALLOWED_FLAG | VARCHAR2 | 4 |  |  | LEED_CHANGE_ALLOWED_FLAG |
| TRANSLATION_BUSINESS_OBJECT_ID | NUMBER |  | 18 |  | TRANSLATION_BUSINESS_OBJECT_ID |
| INTKEY_SUPPORT_FLAG | VARCHAR2 | 4 |  |  | INTKEY_SUPPORT_FLAG |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SDL_MAPS_U1 | Unique | Default | BUSINESS_OBJECT_ID |
| HRC_SDL_MAPS_U2 | Unique | Default | BO_MAP_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
