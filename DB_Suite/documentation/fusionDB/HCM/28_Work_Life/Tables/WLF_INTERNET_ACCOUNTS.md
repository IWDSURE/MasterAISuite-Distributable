# WLF_INTERNET_ACCOUNTS

Table to store the internet account (e.g., Email, Calendar, etc.,) details.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfinternetaccounts-16044.html#wlfinternetaccounts-16044](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfinternetaccounts-16044.html#wlfinternetaccounts-16044)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_INTERNET_ACCOUNTS_PK | INTERNET_ACCOUNT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTERNET_ACCOUNT_ID | NUMBER |  | 18 | Yes | System generate unique identifier. |
| ACCOUNT_CODE | VARCHAR2 | 30 |  | Yes | Unique code assigned to each account. |
| ACCOUNT_NAME | VARCHAR2 | 200 |  | Yes | Specifies account name (e.g, Quotation from Supplier, Supplier Recall Letter, etc.,) |
| FAMILY | VARCHAR2 | 80 |  | Yes | Specifies the product family associated with the internet account. |
| PRODUCT | VARCHAR2 | 100 |  | Yes | Specifies the product associated with the internet account. |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Describes the internet account. |
| STATUS | VARCHAR2 | 30 |  | Yes | Lookup code that specifies if the account is active or not (e.g., ACTIVE/INACTIVE). |
| USERNAME | VARCHAR2 | 254 |  | Yes | Specifies username (e.g., Email Address) of the internet account. |
| PROVIDER_CODE | VARCHAR2 | 30 |  | Yes | Lookup code that specifies the provider. (e.g., GMAIL/MSGRAPH). |
| CLIENT_ID | VARCHAR2 | 150 |  |  | Specifies the Client ID associated with the internet account. |
| TENANT_ID | VARCHAR2 | 36 |  |  | Specifies the Tenant ID associated with the internet account. |
| AGENT_ENABLED | VARCHAR2 | 1 |  |  | Specifies if the connection is enabled to be invoked from AI agents (e.g., Y/N). |
| HYBRID_SEARCH_ENABLED | VARCHAR2 | 1 |  |  | Specifies if the emails from this account should be vectorized for hybrid search |
| POLL_INTERVAL | VARCHAR2 | 30 |  |  | Defines how frequently the system polls the email inbox for new messages. |
| ADDITIONAL_INFO | CLOB |  |  |  | Used to specify any additional information about the account. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_INTERNET_ACCOUNTS_N1 | Non Unique | WLF_INTERNET_ACCOUNTS_N1 | FAMILY, PRODUCT |
| WLF_INTERNET_ACCOUNTS_U1 | Unique | Default | INTERNET_ACCOUNT_ID |
| WLF_INTERNET_ACCOUNTS_U2 | Unique | WLF_INTERNET_ACCOUNTS_U2 | ACCOUNT_CODE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
