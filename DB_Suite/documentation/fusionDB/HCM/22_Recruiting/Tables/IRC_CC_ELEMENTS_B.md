# IRC_CC_ELEMENTS_B

Details of the sites which is used to publish the jobs.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircccelementsb-25025.html#ircccelementsb-25025](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircccelementsb-25025.html#ircccelementsb-25025)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CC_ELEMENTS_B_PK | ELEMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ELEMENT_ID | NUMBER |  | 18 | Yes | Primary key, auto generated value. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| ELEMENT_NUMBER | VARCHAR2 | 240 |  | Yes | Unique identifier of the element,  auto generated value. |  |
| PARENT_ELEMENT_NUMBER | VARCHAR2 | 240 |  |  | Number of the parent element of the child element, can be null if this is root element. |  |
| ELEMENT_ORDER | NUMBER |  | 18 | Yes | The order of this custom content element. |  |
| ELEMENT_TYPE | VARCHAR2 | 20 |  | Yes | Type of the element, that will say of what concrete type this element is. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CC_ELEMENTS_B_N2 | Non Unique | Default | PARENT_ELEMENT_NUMBER |
| IRC_CC_ELEMENTS_B_U1 | Unique | Default | ELEMENT_ID |
| IRC_CC_ELEMENTS_B_U2 | Unique | Default | ELEMENT_NUMBER |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
