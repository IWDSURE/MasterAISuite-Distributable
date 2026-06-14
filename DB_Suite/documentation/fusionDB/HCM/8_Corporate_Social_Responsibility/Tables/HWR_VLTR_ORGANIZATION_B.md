# HWR_VLTR_ORGANIZATION_B

This table stores base organization information

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrorganizationb-21982.html#hwrvltrorganizationb-21982](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrorganizationb-21982.html#hwrvltrorganizationb-21982)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_ORGANIZATION_B_PK | ORGANIZATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ORGANIZATION_ID | NUMBER |  | 18 | Yes | ORGANIZATION_ID |
| EIN | VARCHAR2 | 250 |  |  | EIN |
| ORGANIZATION_TYPE | VARCHAR2 | 100 |  |  | ORGANIZATION_TYPE |
| STATE | VARCHAR2 | 100 |  |  | APPROVAL_STATUS |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| ORGANIZATION_ADDRESS_ID | NUMBER |  | 18 |  | ORGANIZATION_ADDRESS_ID |
| CONTACT_EMAIL | VARCHAR2 | 254 |  |  | CONTACT_EMAIL |
| CONTACT_PHONE | VARCHAR2 | 100 |  |  | CONTACT_PHONE |
| CONTACT_FAX | VARCHAR2 | 100 |  |  | CONTACT_FAX |
| AREAS_OF_INTEREST | VARCHAR2 | 4000 |  |  | AREAS_OF_INTEREST |
| WEBSITE | VARCHAR2 | 254 |  |  | WEBSITE |
| PARENT_AFFILIATIONS | VARCHAR2 | 100 |  |  | PARENT_AFFILIATIONS |
| LOGO_FILE_ID | NUMBER |  | 18 |  | LOGO_FILE_ID |
| EINSTATUS | VARCHAR2 | 10 |  |  | EINSTATUS |
| CREATOR_PERSON_ID | NUMBER |  | 18 |  | CREATOR_PERSON_ID |
| SUBMITTED_BY | VARCHAR2 | 64 |  |  | SUBMITTED_BY |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LONGITUDE | NUMBER |  |  |  | Longitude |
| LATITUDE | NUMBER |  |  |  | LATITUDE |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_VLTR_ORGANIZATION_B_U1 | Unique | FUSION_TS_TX_IDX | ORGANIZATION_ID |  |
| HWR_VLTR_ORGANIZATION_B_U2 | Unique | FUSION_TS_TX_IDX | EIN | Obsolete |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
