# HWR_CONTACT_INFO_B

The contact info table stores profile contact info data.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcontactinfob-28987.html#hwrcontactinfob-28987](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcontactinfob-28987.html#hwrcontactinfob-28987)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CONTACT_INFO_B_PK | SOURCE_ID, CONTACT_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTACT_INFO_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the contact info table. |
| SOURCE_ID | NUMBER |  | 18 | Yes | The Id of the source for the profile which has the contact info. |
| CONTACT_INFO_REPO | NUMBER |  | 18 |  | The unique Id for writing to repo. |
| ADDRESS | VARCHAR2 | 1000 |  |  | The street address of the person. |
| EMAIL | VARCHAR2 | 800 |  |  | The email address of the person. |
| HASHING_TYPE | VARCHAR2 | 100 |  |  | The hashing type of the contact info. |
| ONLINE_ACCOUNT | VARCHAR2 | 255 |  |  | The online account of the person. |
| ONLINE_ACCT_HOMEPAGE | VARCHAR2 | 4000 |  |  | The URL for the online account homepage of the person. |
| PHONE | VARCHAR2 | 200 |  |  | The primary phone number of the person. |
| URL | VARCHAR2 | 4000 |  |  | The URL of the person's homepage. |
| LATITUDE | NUMBER |  |  |  | This is the geographical latitude of the person. |
| LONGITUDE | NUMBER |  |  |  | This is the geographical longitude of the person. |
| ADDRESS_LINE_1 | VARCHAR2 | 240 |  |  | This is the first line of the address for this person. |
| ADDRESS_LINE_2 | VARCHAR2 | 240 |  |  | This is the second line of the address for this person. |
| ADDRESS_LINE_3 | VARCHAR2 | 240 |  |  | This is the third line of the address for this person. |
| ADDRESS_LINE_4 | VARCHAR2 | 240 |  |  | This is the fourth line of the address for this person. |
| BUILDING | VARCHAR2 | 240 |  |  | This is the building part of the address. |
| FLOOR_NUMBER | VARCHAR2 | 40 |  |  | This is the floor number part of the address. |
| TOWN_OR_CITY | VARCHAR2 | 128 |  |  | This is the town or city part of the address. |
| REGION_1 | VARCHAR2 | 120 |  |  | This is the first region part of the address (most specific). |
| REGION_2 | VARCHAR2 | 120 |  |  | This is the second region part of the address. |
| REGION_3 | VARCHAR2 | 120 |  |  | This is the third region part of the address (least specific). |
| COUNTRY | VARCHAR2 | 60 |  |  | This is the country or 2-letter ISO country code part of the address. |
| POSTAL_CODE | VARCHAR2 | 30 |  |  | This is the postal code part of the address. |
| LONG_POSTAL_CODE | VARCHAR2 | 30 |  |  | This is the long postal code part of the address. |
| TIMEZONE_CODE | VARCHAR2 | 50 |  |  | This is the timezone code of the address. |
| DERIVED_LOCALE | VARCHAR2 | 240 |  |  | This is the derived locale composed of other address fields based on local standards. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_CONTACT_INFO_B_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, CONTACT_INFO_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
