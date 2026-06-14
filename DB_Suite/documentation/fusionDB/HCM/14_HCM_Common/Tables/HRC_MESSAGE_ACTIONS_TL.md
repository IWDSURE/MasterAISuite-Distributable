# HRC_MESSAGE_ACTIONS_TL

This table is required to show the transalated action names and description

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessageactionstl-11277.html#hrcmessageactionstl-11277](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessageactionstl-11277.html#hrcmessageactionstl-11277)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_MESSAGE_ACTIONS_TL_PK | ACTION_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_ID | NUMBER |  | 18 | Yes | Unique identifier of hrc_message_actions_b table to map the row which the transalation is intented to |
| NAME | VARCHAR2 | 20 |  |  | Transalated name of the action based on the language column |
| DESCRIPTION | VARCHAR2 | 100 |  |  | Description on of the action in the transalated format. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identify the ENTERPRISE  to which the process belongs. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_MESSAGE_ACTIONS_TL_PK | Unique | Default | ACTION_ID, LANGUAGE, ORA_SEED_SET1 |
| HRC_MESSAGE_ACTIONS_TL_PK1 | Unique | Default | ACTION_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
