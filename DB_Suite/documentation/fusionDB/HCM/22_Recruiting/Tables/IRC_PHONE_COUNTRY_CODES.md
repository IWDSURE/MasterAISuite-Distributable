# IRC_PHONE_COUNTRY_CODES

This table stores country-specific telephone prefix information along with the area code.
For example, The country code prefix for India is 91 and the country code prefix for France is 33. if it is Bahamas it is 1242.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircphonecountrycodes-5220.html#ircphonecountrycodes-5220](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircphonecountrycodes-5220.html#ircphonecountrycodes-5220)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_PHONE_COUNTRY_CODES_PK | PHONE_COUNTRY_CODE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PHONE_COUNTRY_CODE_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| COUNTRY_CODE | VARCHAR2 | 2 |  | Yes | Country code from the TERRITORY_CODE column in the fnd_territories_b table |
| PHONE_COUNTRY_CODE | VARCHAR2 | 30 |  | Yes | Country prefix for international phone numbers including area code, such as 33 for France |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_PHONE_COUNTRY_CODES_N1 | Non Unique | FUSION_TS_SEED | COUNTRY_CODE |
| IRC_PHONE_COUNTRY_CODES_N2 | Non Unique | FUSION_TS_SEED | PHONE_COUNTRY_CODE |
| IRC_PHONE_COUNTRY_CODES_PK | Unique | FUSION_TS_SEED | PHONE_COUNTRY_CODE_ID, ORA_SEED_SET1 |
| IRC_PHONE_COUNTRY_CODES_PK1 | Unique | FUSION_TS_SEED | PHONE_COUNTRY_CODE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
