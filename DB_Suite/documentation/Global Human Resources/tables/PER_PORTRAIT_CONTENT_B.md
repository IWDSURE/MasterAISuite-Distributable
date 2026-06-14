# PER_PORTRAIT_CONTENT_B

This table is new for Fusion,And has been created to handle user preferences to choose whether to show/hide ui regions in portrait.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perportraitcontentb-19419.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perportraitcontentb-19419.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PORTRAIT_CONTENT_B_PK | PORTRAIT_CONTENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PORTRAIT_CONTENT_ID | NUMBER |  | 18 | Yes | System generated primary key |
| PORTRAIT_CONTENT_ITEM_KEY | VARCHAR2 | 50 |  | Yes | A keyword provided as name of a Portrait Card or Card Region in Portrait Settings page. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PORTRAIT_CARD_FLAG | VARCHAR2 | 1 |  | Yes | Indicates whether the Portrait content item is a card or not |
| PARENT_CONTENT_ITEM_KEY | VARCHAR2 | 50 |  |  | Indicates which Portrait card the content item belongs to |
| ALLOW_USER_CONTROL_FLAG | VARCHAR2 | 1 |  | Yes | Indicates whether the user is allowed to control preferences for this content item |
| DEFAULT_MANAGER_VISIBLE | VARCHAR2 | 1 |  | Yes | Indicates whether the selected card is by default visible to the Manager or not, while viewing Portrait of the Employee in manager hierarchy. |
| DEFAULT_CONNECTIONS_VISIBLE | VARCHAR2 | 1 |  | Yes | Indicates whether the selected card is by default visible in Portrait to the Connections in the network or not. |
| DEFAULT_EVERYONE_VISIBLE | VARCHAR2 | 1 |  | Yes | Indicates whether the selected card is by default visible in Portrait to every or not. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| DISPLAY_CARD_IN_PORTRAIT | VARCHAR2 | 1 |  | Yes | indicates whether the card should be displayed on the portrait page |
| CARD_ORDER | NUMBER |  | 2 | Yes | Number of the card in the user customised card order |
| PORTRAIT_CARD_NUMBER | NUMBER |  | 2 | Yes | Default number of the card in the portrait |
| PORTRAIT_ADMIN_FLAG | VARCHAR2 | 1 |  | Yes | indicates whether the card should be visible only to the user with administrator previleges |
| DEFAULT_CARD | VARCHAR2 | 1 |  | Yes | indicates whether the card is a default card to be displayed |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_PORTRAIT_CONTENT_B_PK | Unique | Default | PORTRAIT_CONTENT_ID, ORA_SEED_SET1 |
| PER_PORTRAIT_CONTENT_B_PK1 | Unique | Default | PORTRAIT_CONTENT_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
