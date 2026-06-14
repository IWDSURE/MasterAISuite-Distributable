# CMP_TRANSACTIONS

It stores compensation transaction data , such as data related to employee reassignment, change eligibility and variable pay. It also holds data used by compensation workbench notifications.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptransactions-15918.html#cmptransactions-15918](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptransactions-15918.html#cmptransactions-15918)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TRANSACTIONS_PK | TRANSACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TRANSACTION_ID | NUMBER |  | 18 | Yes | TRANSACTION_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| TRANSACTION_TYPE | VARCHAR2 | 30 |  | Yes | TRANSACTION_TYPE |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| ATTRIBUTE1 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE11 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE12 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE13 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE14 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE15 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE16 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE17 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE18 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE19 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE20 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE21 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE22 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE23 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE24 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE25 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE26 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE27 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE28 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE29 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE30 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE31 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE32 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE33 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE34 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE35 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE36 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE37 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE38 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE39 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE40 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TRANSACTIONS_N1 | Non Unique | Default | ATTRIBUTE1, TRANSACTION_TYPE, ATTRIBUTE4 |
| CMP_TRANSACTIONS_N2 | Non Unique | Default | ATTRIBUTE2, TRANSACTION_TYPE |
| CMP_TRANSACTIONS_N3 | Non Unique | Default | ATTRIBUTE3, TRANSACTION_TYPE |
| CMP_TRANSACTIONS_N38 | Non Unique | Default | ATTRIBUTE38, TRANSACTION_TYPE |
| CMP_TRANSACTIONS_N4 | Non Unique | Default | TRANSACTION_TYPE, STATUS |
| CMP_TRANSACTIONS_PK | Unique | Default | TRANSACTION_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
