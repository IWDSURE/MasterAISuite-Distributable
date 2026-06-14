# HRC_ATOMPUB_WORKSPACES

Workspaces are server-defined groups of Collections.  The "app:workspace" element contains zero or more app:collection elements describing the Collections of Resources available for editing.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcatompubworkspaces-7221.html#hrcatompubworkspaces-7221](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcatompubworkspaces-7221.html#hrcatompubworkspaces-7221)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ATOMPUB_WORKSPACES_PK | WORKSPACE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORKSPACE_ID | NUMBER |  | 18 | Yes | Uniquely identifies an atom workspace row. |
| OBJECT_GUID | VARCHAR2 | 32 |  | Yes | The ATOM Workspace UUID which is a GUID |
| TITLE | VARCHAR2 | 2000 |  | Yes | Human readable title for the Workspace 
e.g. 
Oracle Fusion HCM Talent
<title type="text">Oracle Fusion HCM Talent</title> |
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
| HRC_ATOMPUB_WORKSPACES_N20 | Non Unique | HRC_ATOMPUB_WORKSPACES_N20 | SGUID |
| HRC_ATOMPUB_WORKSPACES_U1 | Unique | HRC_ATOMPUB_WORKSPACES_U1 | WORKSPACE_ID, ORA_SEED_SET1 |
| HRC_ATOMPUB_WORKSPACES_U11 | Unique | HRC_ATOMPUB_WORKSPACES_U1 | WORKSPACE_ID, ORA_SEED_SET2 |
| HRC_ATOMPUB_WORKSPACES_U2 | Unique | HRC_ATOMPUB_WORKSPACES_U2 | OBJECT_GUID, ORA_SEED_SET1 |
| HRC_ATOMPUB_WORKSPACES_U21 | Unique | HRC_ATOMPUB_WORKSPACES_U2 | OBJECT_GUID, ORA_SEED_SET2 |
| HRC_ATOMPUB_WORKSPACES_U3 | Unique | HRC_ATOMPUB_WORKSPACES_U3 | TITLE, ORA_SEED_SET1 |
| HRC_ATOMPUB_WORKSPACES_U31 | Unique | HRC_ATOMPUB_WORKSPACES_U3 | TITLE, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
