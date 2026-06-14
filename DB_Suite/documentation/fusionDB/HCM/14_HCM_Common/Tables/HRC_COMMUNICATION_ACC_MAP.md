# HRC_COMMUNICATION_ACC_MAP

This table stores the mapping between config_id and account_id for HCM Communications

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** hrc_communication_acc_map

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccommunicationaccmap-23707.html#hrccommunicationaccmap-23707](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccommunicationaccmap-23707.html#hrccommunicationaccmap-23707)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_COMMUNICATION_ACC_MAP_PK | MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MAPPING_ID | NUMBER |  | 18 | Yes | Unique Identifier to identify the mapping between communication config and account records |
| CONFIG_ID | NUMBER |  | 18 |  | Unique Identifier to identify the configuration record |
| ACCOUNT_ID | NUMBER |  | 18 |  | Unique Identifier to identify the email entry record |
| IS_ACTIVE | VARCHAR2 | 1 |  |  | Flag that indicates if the communication account is active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_COMMUNICATION_ACC_MAP_PK | Unique | hrc_communication_acc_map_IND | MAPPING_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
