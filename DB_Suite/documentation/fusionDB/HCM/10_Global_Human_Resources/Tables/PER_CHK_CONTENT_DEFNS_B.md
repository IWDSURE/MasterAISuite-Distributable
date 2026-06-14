# PER_CHK_CONTENT_DEFNS_B

PER_CHK_CONTENT_DEFNS_B : This is base table for checklist content definition

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkcontentdefnsb-28747.html#perchkcontentdefnsb-28747](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkcontentdefnsb-28747.html#perchkcontentdefnsb-28747)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_CONTENT_DEFNS_B_PK | CHK_CONTENT_DEFN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CHK_CONTENT_DEFN_ID | NUMBER |  | 18 | Yes | CHK_CONTENT_DEFN_ID |  |
| CONTENT_DEFN_CODE | VARCHAR2 | 80 |  | Yes | Unique code for seed data purpose |  |
| CONTENT_TYPE | VARCHAR2 | 30 |  | Yes | Content Type
System Lookup: ORA_CHK_CONTENT_TYPE
Values:
ORA_NOTE - Note
ORA_EVENT - Events / Announcements
ORA_ONBOARDING_STEP - Onboarding Step |  |
| CONTENT_SUBTYPE | VARCHAR2 | 30 |  | Yes | Content Sub Type
System Lookup: ORA_CHK_CONTENT_SUBTYPE
Values: ORA_NOTE_DEFAULT - Default ( Title, Descripton )
ORA_NOTE_RICH_CONTENT - Rich Content ( Title, Content Details)
ORA_NOTE_EMBED_CONTENT - Embedded HTML Content (Title, HTML Content)
ORA_NOTE_MEETING - Meeting (Title, Event Date, Event Time, Event Location)
ORA_EVENT_DEFAULT - Default ( Image URL, Content Category, Title, Content URL, Event Date)
ORA_ONBOARDING_STAGES - Onboarding Stages (Title, Description)
ORA_ONBOARDING_TASK_HELP - Onboarding Task Help (Title, Description)
ORA_ONBOARDING_LINK_LIST - Onboarding List of Links (Title, Description, Content Items)
ORA_ONBOARDING_NOTE_LIST - Onboarding List of Notes (Title, Description, Content Items)
ORA_ONBOARDING_RICH_CONTENT - Rich Content ( Title, Description, Content Details)
ORA_ONBOARDING_EMBED_CONTENT - HTML Content ( Title, Description, HTML Content) |  |
| CONTENT_CATEGORY | VARCHAR2 | 30 |  |  | Content Category
Extensible Lookup: ORA_CHK_CONTENT_CATEGORY
Values - ORA_ANNOUNCEMENT - Announcement
ORA_EVENT - Event
ORA_INSIGHT - Insight |  |
| CONTENT_URL | VARCHAR2 | 240 |  |  | CONTENT_URL |  |
| IMAGE_URL | VARCHAR2 | 240 |  |  | Image URL |  |
| HTML_CONTENT | VARCHAR2 | 4000 |  |  | HTML Markup content |  |
| EVENT_DATE | DATE |  |  |  | Event Date |  |
| EVENT_TIME | VARCHAR2 | 10 |  |  | Event Time |  |
| EVENT_LOCATION | VARCHAR2 | 240 |  |  | Event Location |  |
| STATUS | VARCHAR2 | 30 |  | Yes | Content Status
System Lookup: ACTIVE_INACTIVE
Value: ACTIVE - Active
INACTIVE - Inactive |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| EMBEDDED_CONTENT | BLOB |  |  |  | Contains the embedded content |  |
| EVENT_OFFSET | NUMBER |  | 5 |  | Contains the event offset. |  |
| EMBEDDED_CONTENT_TYPE | VARCHAR2 | 100 |  |  | Determines the content type of embedded content. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHK_CONTENT_DEFNS_B_PK | Unique | FUSION_TS_TX_DATA | CHK_CONTENT_DEFN_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
