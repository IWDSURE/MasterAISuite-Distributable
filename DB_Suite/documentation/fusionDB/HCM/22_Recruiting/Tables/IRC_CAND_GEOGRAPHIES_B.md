# IRC_CAND_GEOGRAPHIES_B

The geographies table stores data representing physical geographies for candidates

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandgeographiesb-23504.html#irccandgeographiesb-23504](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandgeographiesb-23504.html#irccandgeographiesb-23504)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_GEOGRAPHIES_B_PK | GEOGRAPHY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GEOGRAPHY_ID | NUMBER |  | 18 | Yes | Foreign key to HZ_GEOGRAPHIES table for generating the FQN.  Reference the geography_id in HZ_GEOGRAPHY_IDENTIFIERS to create the FQN alternates. |
| GEOGRAPHY_TYPE | VARCHAR2 | 30 |  | Yes | Type of geography. Type from HZ_GEOGRAPHY_TYPES_B |
| GEOGRAPHY_NAME | VARCHAR2 | 500 |  |  | Primary Name of the geography from HZ_GEOGRAPHIES |
| COUNTRY_ID | NUMBER |  | 18 |  | Element based on hierarchy structure and a foreign key to  the element in HZ_GEOGRAPHIES table. |
| COUNTRY | VARCHAR2 | 2 |  |  | Element based on hierarchy structure from HZ_GEOGRAPHIES table. |
| STATE_ID | NUMBER |  | 18 |  | Element based on hierarchy structure and a foreign key to  the element in HZ_GEOGRAPHIES table. |
| STATE | VARCHAR2 | 500 |  |  | Element based on hierarchy structure from HZ_GEOGRAPHIES table. |
| CITY_ID | NUMBER |  | 18 |  | Element based on hierarchy structure and a foreign key to  the element in HZ_GEOGRAPHIES table. |
| CITY | VARCHAR2 | 500 |  |  | Element based on hierarchy structure from HZ_GEOGRAPHIES table. |
| COUNTY_ID | NUMBER |  | 18 |  | Element based on hierarchy structure and a foreign key to  the element in HZ_GEOGRAPHIES table. |
| COUNTY | VARCHAR2 | 500 |  |  | Element based on hierarchy structure from HZ_GEOGRAPHIES table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_GEOGRAPHIES_B_N1 | Non Unique | Default | GEOGRAPHY_TYPE, COUNTRY |
| IRC_CAND_GEOGRAPHIES_B_PK | Unique | Default | GEOGRAPHY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
