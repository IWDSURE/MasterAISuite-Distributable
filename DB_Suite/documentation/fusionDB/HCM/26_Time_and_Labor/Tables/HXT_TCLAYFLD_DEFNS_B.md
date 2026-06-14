# HXT_TCLAYFLD_DEFNS_B

The table HXT_TCLAYFLD_DEFNS_B table contains the definition of each layout field which can be later associated to a layout set via the configuration screen.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttclayflddefnsb-13148.html#hxttclayflddefnsb-13148](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttclayflddefnsb-13148.html#hxttclayflddefnsb-13148)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_TCLAYFLD_DEFNS_B_PK | TCLAYFLD_DEFNS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCLAYFLD_DEFNS_ID | NUMBER |  | 18 | Yes | TCLAYFLD_DEFNS_ID |
| TCLAYFLD_DEFNS_CD | VARCHAR2 | 510 |  |  | TCLAYFLD_DEFNS_CD |
| TCLAY_ID | NUMBER |  | 18 |  | TCLAY_ID |
| P_TCLAYFLD_DEFNS_ID | NUMBER |  | 18 |  | Id of the parent layout field, referred to TCLAYFLD_DEFNS_ID. NULL means it is a parent LC. |
| TCLAYFLD_DEFNS_INSTANCE_FLAG | VARCHAR2 | 3 |  | Yes | 'Y' means it is an instance; 'N' or null means it is a template. |
| TCLAYFLD_TMPL_ID | NUMBER |  | 18 |  | Id of the template of the instance LC. Null if it is not an instance. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DISPLAY_SEQUENCE | NUMBER |  | 18 |  | DISPLAY_SEQUENCE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| TCLAYFLD_ATTRIBUTE_CATEGORY | VARCHAR2 | 150 |  |  | Context attribute for the Flexfield. |
| TCLAYFLD_ATTRIBUTE_CHAR1 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR2 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR3 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR4 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR5 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR6 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR7 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR8 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR9 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR10 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR11 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR12 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR13 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR14 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR15 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR16 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR17 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR18 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR19 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR20 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR21 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR22 | VARCHAR2 | 150 |  |  | TCLAYFLD_ATTRIBUTE_CHAR22 |
| TCLAYFLD_ATTRIBUTE_CHAR23 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR24 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR25 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR26 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR27 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR28 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR29 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_CHAR30 | VARCHAR2 | 150 |  |  | Flexfield Attributes of type Char. |
| TCLAYFLD_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Flexfield Attributes of type Number. |
| TCLAYFLD_ATTRIBUTE_DATE1 | DATE |  |  |  | Flexfield Attributes of type Date |
| TCLAYFLD_ATTRIBUTE_DATE2 | DATE |  |  |  | Flexfield Attributes of type Date |
| TCLAYFLD_ATTRIBUTE_DATE3 | DATE |  |  |  | Flexfield Attributes of type Date |
| TCLAYFLD_ATTRIBUTE_DATE4 | DATE |  |  |  | Flexfield Attributes of type Date |
| TCLAYFLD_ATTRIBUTE_DATE5 | DATE |  |  |  | Flexfield Attributes of type Date |
| TCLAYFLD_ATTRIBUTE_DATE6 | DATE |  |  |  | Flexfield Attributes of type Date |
| TCLAYFLD_ATTRIBUTE_DATE7 | DATE |  |  |  | Flexfield Attributes of type Date |
| TCLAYFLD_ATTRIBUTE_DATE8 | DATE |  |  |  | Flexfield Attributes of type Date |
| TCLAYFLD_ATTRIBUTE_DATE9 | DATE |  |  |  | Flexfield Attributes of type Date |
| TCLAYFLD_ATTRIBUTE_DATE10 | DATE |  |  |  | Flexfield Attributes of type Date |
| TCLAYFLD_ATTRIBUTE_DATE11 | DATE |  |  |  | Flexfield Attributes of type Date |
| TCLAYFLD_ATTRIBUTE_DATE12 | DATE |  |  |  | Flexfield Attributes of type Date |
| TCLAYFLD_ATTRIBUTE_DATE13 | DATE |  |  |  | Flexfield Attributes of type Date |
| TCLAYFLD_ATTRIBUTE_DATE14 | DATE |  |  |  | Flexfield Attributes of type Date |
| TCLAYFLD_ATTRIBUTE_DATE15 | DATE |  |  |  | Flexfield Attributes of type Date |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_TCLAYFLD_DEFNS_B_N1 | Non Unique | Default | P_TCLAYFLD_DEFNS_ID |
| HXT_TCLAYFLD_DEFNS_B_N2 | Non Unique | Default | TCLAY_ID |
| HXT_TCLAYFLD_DEFNS_B_N20 | Non Unique | Default | SGUID |
| HXT_TCLAYFLD_DEFNS_B_N3 | Non Unique | Default | TCLAYFLD_TMPL_ID |
| HXT_TCLAYFLD_DEFNS_B_PK | Unique | Default | TCLAYFLD_DEFNS_ID, ORA_SEED_SET1 |
| HXT_TCLAYFLD_DEFNS_B_PK1 | Unique | Default | TCLAYFLD_DEFNS_ID, ORA_SEED_SET2 |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
