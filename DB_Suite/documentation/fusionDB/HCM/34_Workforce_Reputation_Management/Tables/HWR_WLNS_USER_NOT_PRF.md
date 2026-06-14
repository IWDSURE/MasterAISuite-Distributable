# HWR_WLNS_USER_NOT_PRF

This table stores the notification preferences of wellness users.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsusernotprf-23562.html#hwrwlnsusernotprf-23562](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsusernotprf-23562.html#hwrwlnsusernotprf-23562)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_USER_NOT_PRF_PK | USER_ID, NOTIFICATION_PREFERENCE |

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| USER_ID | VARCHAR2 | 500 | Yes | This column is a FK to HWR_WLNS_USER table. |
| NOTIFICATION_PREFERENCE | VARCHAR2 | 256 | Yes | This columns indicates user's notifiaction preference. |
| CONTACT_INFO | VARCHAR2 | 500 |  | This column stores the contact info for the corresponding notification preference in NOTIFICATION_PREFERENCE column |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_USER_NOT_PRF_U1 | Unique | FUSION_TS_TX_DATA | USER_ID, NOTIFICATION_PREFERENCE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
