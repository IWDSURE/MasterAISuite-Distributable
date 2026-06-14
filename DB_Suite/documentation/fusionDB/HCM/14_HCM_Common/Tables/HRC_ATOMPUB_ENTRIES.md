# HRC_ATOMPUB_ENTRIES

Represents  entries, acting as a container for metadata and data associated with an entry.  An element can appear as a child of the atom:feed element, or it can 
appear as the document (i.e., top-level) element of a stand-alone Atom Entry Document.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcatompubentries-19989.html#hrcatompubentries-19989](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcatompubentries-19989.html#hrcatompubentries-19989)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ATOMPUB_ENTRIES_PK | ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ENTRY_ID | NUMBER |  | 18 | Yes | Uniquely identifies an atom entry  row. |  |
| COLLECTION_ID | NUMBER |  | 18 | Yes | Foreign Key to HRC_ATOMPUB_COLLECTIONS.COLLECTION_ID |  |
| ATOM_ID | VARCHAR2 | 32 |  | Yes | The ATOM Entry UUID which is a GUID |  |
| TITLE | VARCHAR2 | 2000 |  | Yes | Specifies the <title> tag value containing Human readable title for the entry |  |
| UPDATED | TIMESTAMP |  |  | Yes | Updated entry timestamp. Can be set to a future time. |  |
| ARCHIVED | TIMESTAMP |  |  | Yes | Entry archived timestamp |  |
| PURGED | TIMESTAMP |  |  | Yes | Entry purged timestamp |  |
| SECURITY_ID | NUMBER |  | 18 |  | The security identifier which is a fusion surrogate key value based on the HRC_ATOMPUB_COLLECTIONS.SECURITY_TYPE value |  |
| SOURCE_ENTRY_ID | NUMBER |  | 18 |  | Identifies a source atom entry. Foreign Key to HRC_ATOM_ENTRIES.ENTRY_ID

If an atom:entry is copied from one feed into another feed then SOURCE_ENTRY_ID points to the original entry. |  |
| ENTRY_XML | CLOB |  |  |  | XML Fragment for Entry. Containing root node is <entry> |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. | Obsolete |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| REFERENCE_ID | VARCHAR2 | 80 |  |  | Reference ID for atompub entries |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRC_ATOMPUB_ENTRIES_N1 | Non Unique | FUSION_TS_TX_DATA | COLLECTION_ID, UPDATED, ARCHIVED, PURGED | Obsolete |
| HRC_ATOMPUB_ENTRIES_N2 | Non Unique | FUSION_TS_TX_DATA | COLLECTION_ID, ARCHIVED, PURGED | Obsolete |
| HRC_ATOMPUB_ENTRIES_N20 | Non Unique | Default | SGUID | Obsolete |
| HRC_ATOMPUB_ENTRIES_N3 | Non Unique | Default | ENTRY_XML | Obsolete |
| HRC_ATOMPUB_ENTRIES_N4 | Non Unique | Default | COLLECTION_ID, UPPER("TITLE") |  |
| HRC_ATOMPUB_ENTRIES_N5 | Non Unique | Default | SOURCE_ENTRY_ID |  |
| HRC_ATOMPUB_ENTRIES_U1 | Unique | FUSION_TS_TX_DATA | ATOM_ID |  |
| HRC_ATOMPUB_ENTRIES_U2 | Unique | Default | ENTRY_ID |  |
| HRC_ATOMPUB_ENTRIES_U4 | Unique | Default | COLLECTION_ID, UPDATED, ENTRY_ID, ARCHIVED, PURGED |  |
| HRC_ATOMPUB_ENTRIES_U5 | Unique | Default | COLLECTION_ID, CREATION_DATE, ENTRY_ID, ARCHIVED, PURGED |  |
| HRC_ATOMPUB_ENTRIES_U6 | Unique | Default | COLLECTION_ID, UPDATED, ENTRY_ID, ARCHIVED, PURGED, REFERENCE_ID |  |
| HRC_ATOMPUB_ENTRIES_U7 | Unique | Default | COLLECTION_ID, CREATION_DATE, ENTRY_ID, ARCHIVED, PURGED, REFERENCE_ID |  |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
