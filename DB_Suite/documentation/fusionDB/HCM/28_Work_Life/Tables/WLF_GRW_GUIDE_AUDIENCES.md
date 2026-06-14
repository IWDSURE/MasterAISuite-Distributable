# WLF_GRW_GUIDE_AUDIENCES

Table to store audiences associated with grow guides.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwguideaudiences-27962.html#wlfgrwguideaudiences-27962](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwguideaudiences-27962.html#wlfgrwguideaudiences-27962)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_GRW_GUIDE_AUDIENCES_PK | GUIDE_AUDIENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GUIDE_AUDIENCE_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| GUIDE_ID | NUMBER |  | 18 | Yes | ID of guide to which the audience is added. |
| STATUS | VARCHAR2 | 30 |  | Yes | Status of the added audience (e.g Active, InActive etc.) |
| AUDIENCE_TYPE | VARCHAR2 | 30 |  | Yes | Type of the Audiences containing collection of persons. (E.g. Hcm List, Organizations, Person Number CSV List etc.) |
| AUDIENCE_ID | NUMBER |  | 18 | Yes | ID of the Audience associated to guide. |
| ADDED_ON_DATE | TIMESTAMP |  |  | Yes | Date when the audience was added to guide. |
| REMOVED_ON_DATE | TIMESTAMP |  |  |  | Date when the audience was removed from guide. |
| PROCESSED_DATE | TIMESTAMP |  |  |  | Last processed date of the guide assignments reconcile job. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_GRW_GUIDE_AUDIENCES_N1 | Non Unique | Default | AUDIENCE_ID |
| WLF_GRW_GUIDE_AUDIENCES_N2 | Non Unique | Default | GUIDE_ID |
| WLF_GRW_GUIDE_AUDIENCES_U1 | Unique | Default | GUIDE_AUDIENCE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
