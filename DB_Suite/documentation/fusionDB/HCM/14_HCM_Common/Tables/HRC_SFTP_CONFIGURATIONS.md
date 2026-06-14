# HRC_SFTP_CONFIGURATIONS

Contains file upload configuration data.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsftpconfigurations-25253.html#hrcsftpconfigurations-25253](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsftpconfigurations-25253.html#hrcsftpconfigurations-25253)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SFTP_CONFIGURATIONS_PK | CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIG_ID | NUMBER |  | 18 | Yes | Represents the unique configuration id. |
| CONFIG_NAME | VARCHAR2 | 240 |  | Yes | Represents the name of the configuration. |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Configuration description. |
| ENABLED | VARCHAR2 | 30 |  | Yes | Represents the enabled state of the configuration. |
| HOST | VARCHAR2 | 100 |  | Yes | Configuration host. |
| PORT | NUMBER |  | 9 |  | Configuration port. |
| REMOTE_FOLDER | VARCHAR2 | 1020 |  |  | The folder on the ftp server  where the file needs to be placed. |
| AUTH_TYPE | VARCHAR2 | 30 |  |  | Represents the type of authentication. |
| USER_NAME | VARCHAR2 | 30 |  |  | Represents the user name to be used for authentication. |
| PASSWORD | VARCHAR2 | 256 |  |  | Represents the password to be used for authentication. |
| KEY_FILE_NAME | VARCHAR2 | 255 |  |  | Represents the name of the key  file. |
| KEY_VALUE | VARCHAR2 | 4000 |  |  | Represents the value of the key. |
| KEY_PASSPHRASE | VARCHAR2 | 180 |  |  | Represents the behavior and scope of the key. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SFTP_CONFIGURATIONS_PK | Unique | FUSION_TS_TX_DATA | CONFIG_ID |
| HRC_SFTP_CONFIGURATIONS_U1 | Unique | FUSION_TS_TX_DATA | CONFIG_NAME |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
