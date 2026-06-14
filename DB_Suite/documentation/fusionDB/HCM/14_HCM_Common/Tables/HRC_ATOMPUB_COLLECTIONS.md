# HRC_ATOMPUB_COLLECTIONS

A Resource that contains a set of Member Resources. Collections are represented as Atom Feeds. Collections can be for one or more workspaces.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcatompubcollections-13136.html#hrcatompubcollections-13136](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcatompubcollections-13136.html#hrcatompubcollections-13136)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ATOMPUB_COLLECTIONS_PK | COLLECTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COLLECTION_ID | NUMBER |  | 18 | Yes | Uniquely identifies an atom collection row. |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | Specifies if the collection is enabled. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| PATH_NAME | VARCHAR2 | 2000 |  | Yes | The path name for the collection or feed.
e.g. 
employees/newhire |
| TITLE | VARCHAR2 | 2000 |  | Yes | Human readable title value (does not contain a xml tag) for the Collection Feed (e.g. Employee Newhire Feed). Denormalised from COLLECTION_XML for ordering. |
| ATOM_ID | VARCHAR2 | 32 |  | Yes | Collection ATOM Identifier value which is a GUID |
| SECURITY_TYPE | VARCHAR2 | 30 |  |  | Identifies the security context type for the collection. Based on the LOOKUP_TYPE of HRC_ATOMPUB_SECURITY_TYPE which contains the following lookup code values:
DOR      
LDG  
LOCATION
ORGANIZATION    
PAYROLL
PERSON
POSITION
PUBLIC_PERSON |
| SETTINGS_XML | CLOB |  |  |  | XML Fragment for Collection Settings. Containing root node is <fext:collectionSettings> |
| COLLECTION_XML | CLOB |  |  |  | XML Fragment for the collection. Containing root node is <feed> |
| CUSTOMIZATION_LEVEL | VARCHAR2 | 30 |  | Yes | Specifies the customization level for the collection. eg: ORA_U, ORA_S and ORA_E |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ATOMPUB_COLLECTIONS_N20 | Non Unique | Default | SGUID |
| HRC_ATOMPUB_COLLECTIONS_N3 | Non Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE |
| HRC_ATOMPUB_COLLECTIONS_U1 | Unique | FUSION_TS_TX_DATA | ATOM_ID, ORA_SEED_SET1 |
| HRC_ATOMPUB_COLLECTIONS_U11 | Unique | FUSION_TS_TX_DATA | ATOM_ID, ORA_SEED_SET2 |
| HRC_ATOMPUB_COLLECTIONS_U2 | Unique | FUSION_TS_TX_DATA | PATH_NAME, ORA_SEED_SET1 |
| HRC_ATOMPUB_COLLECTIONS_U21 | Unique | FUSION_TS_TX_DATA | PATH_NAME, ORA_SEED_SET2 |
| HRC_ATOMPUB_COLLECTIONS_U3 | Unique | Default | COLLECTION_ID, ORA_SEED_SET1 |
| HRC_ATOMPUB_COLLECTIONS_U31 | Unique | Default | COLLECTION_ID, ORA_SEED_SET2 |
| HRC_ATOMPUB_COLLECTION_N4 | Non Unique | Default | UPPER("TITLE") |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
