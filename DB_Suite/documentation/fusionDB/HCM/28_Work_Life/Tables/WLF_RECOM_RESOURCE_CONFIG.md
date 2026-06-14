# WLF_RECOM_RESOURCE_CONFIG

This table stores the recommender configuration details.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecomresourceconfig-27579.html#wlfrecomresourceconfig-27579](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecomresourceconfig-27579.html#wlfrecomresourceconfig-27579)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_RECOM_RES_CONFIG_PK | RECOM_RESOURCE_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECOM_RESOURCE_CONFIG_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| RECOMMENDATION_PROFILE_ID | NUMBER |  | 18 | Yes | References RECOMMENDATION_PROFILE_ID from WLF_RECOMMENDATION_PROFILES table. |
| OBJECT_ID | NUMBER |  | 18 |  | Object Id reference on which recommendation is made. |
| OBJECT_CATEGORY | VARCHAR2 | 30 |  | Yes | Represents category of the the object |
| OBJECT_TYPE | VARCHAR2 | 30 |  |  | Represents the type of the object on which recommendations is made. |
| OBJECT_SUB_TYPE | VARCHAR2 | 30 |  |  | Represents the subtype of the object on which recommendations is made. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| STATUS | VARCHAR2 | 30 |  | Yes | This column represents status of the row. |
| ADDED_ON_DATE | TIMESTAMP |  |  | Yes | Indicates the date when the row is added |
| REMOVED_ON_DATE | TIMESTAMP |  |  |  | Indicates the date when row is removed |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_RECOM_RES_CONFIG_U1 | Unique | Default | RECOM_RESOURCE_CONFIG_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
