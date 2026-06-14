# HRC_DL_AUDIT_HEADERS

This table holds header data for each business object component of the audit output. Each row will be identified using AUDIT_HEADER_ID

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlauditheaders-21912.html#hrcdlauditheaders-21912](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlauditheaders-21912.html#hrcdlauditheaders-21912)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_AUDIT_HEADERS_PK | AUDIT_HEADER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AUDIT_HEADER_ID | NUMBER |  | 18 | Yes | Primary key. From sequence. |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | Foreign key to hrc_dl_business_objects table. The Business Object Id of the business object component that the audit header reports. |
| VO_MAPPING_ID | NUMBER |  | 18 |  | Foreign Key to hrc_dl_vo_maps table. The VO Map Id of the business object component that the audit header line reports, where a VO mapping was possible. Otherwise null. |
| MOST_RECENT_VO_MAP_FLAG | VARCHAR2 | 1 |  | Yes | N indicates that the current VO_MAPPING_ID is not the most recently created VO map, Y indicates that it is. X indicates unknown or where no VO_MAPPING_ID was possible. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise stripe identifier. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_AUDIT_HEADERS_U1 | Unique | Default | AUDIT_HEADER_ID |
| HRC_DL_AUDIT_HEADERS_U2 | Unique | Default | BUSINESS_OBJECT_ID, ENTERPRISE_ID |
| HRC_DL_AUDIT_HEADERS_N1 | Non Unique | Default | VO_MAPPING_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
