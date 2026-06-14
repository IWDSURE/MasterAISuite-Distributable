# IRC_CX_SITE_LINKS_B

Site  Links Table. MLS table with site specific links.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitelinksb-6374.html#irccxsitelinksb-6374](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitelinksb-6374.html#irccxsitelinksb-6374)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_SITE_LINKS_B_PK | LINK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| LINK_ID | NUMBER |  | 18 | Yes | Identifier of the site link. System generated value. |  |
| OBJECT_STATUS | VARCHAR2 | 40 |  | Yes | Indicates the status of the object |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| VISIBLE_ON_MOBILE_FLAG | NUMBER |  | 1 | Yes | Indicates if link should be visible on mobile version. 1 true 0 false |  |
| IS_VISIBLE_FLAG | VARCHAR2 | 1 |  |  | Attribute to show hide link on page |  |
| LINK_NUMBER | VARCHAR2 | 240 |  | Yes | Defines number exposed in rest web service |  |
| PARENT_LINK_NUMBER | VARCHAR2 | 240 |  |  | Parent Link Number. Reference of parent link number. |  |
| LINK_TYPE_CODE | VARCHAR2 | 45 |  | Yes | Link Type. Link could belong to Header or Footer links. |  |
| LINK_ORDER | NUMBER |  | 18 | Yes | Link order of brand link for specific link type. For the same parent defines order of links |  |
| SITE_NUMBER | VARCHAR2 | 240 |  | Yes | Identifies site code for specific link type. All links will have site code defined. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_SITE_LINKS_B_FK1 | Non Unique | FUSION_TS_SEED | SITE_NUMBER |
| IRC_CX_SITE_LINKS_B_PK | Unique | FUSION_TS_SEED | LINK_ID |
| IRC_CX_SITE_LINKS_B_U1 | Unique | FUSION_TS_SEED | LINK_NUMBER |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
