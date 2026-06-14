# CEL_EXTERNAL_VENDORS

Table to store setup for integration with external vendors.

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celexternalvendors-20560.html#celexternalvendors-20560](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celexternalvendors-20560.html#celexternalvendors-20560)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_EXTERNAL_VENDORS_PK | VENDOR_CODE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VENDOR_CODE | VARCHAR2 | 30 |  | Yes | Code that identifies the vendor for external rewards management |
| ACCOUNT_TYPE_CODE | VARCHAR2 | 30 |  |  | Code that identifies the type of vendor account |
| POINT_VALUE | NUMBER |  |  |  | Conversion rate per point |
| CONTENT_ID | VARCHAR2 | 30 |  |  | Universal content management identifier of stored illustration |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | Y/N to indicate if the integration is enabled |
| WITHDRAW_POINTS_FLAG | VARCHAR2 | 1 |  |  | Y/N to indicate if points withdrawal is enabled or not |
| CLIENT_USERNAME | VARCHAR2 | 1024 |  |  | Username or Identifier of the client account with vendor |
| CLIENT_SECRET | VARCHAR2 | 1024 |  |  | Secret for the client account with vendor |
| CLIENT_KEY | VARCHAR2 | 300 |  |  | Key for the client, such as key to the rewards gallery |
| VENDOR_URL1 | VARCHAR2 | 4000 |  |  | Base URL for the vendor |
| VENDOR_URL2 | VARCHAR2 | 4000 |  |  | Alternate URL for the vendor, such as for rewards gallery |
| IMAGE_URL | VARCHAR2 | 4000 |  |  | URL for the vendor image |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_EXTERNAL_VENDORS_PK | Unique | Default | VENDOR_CODE |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
