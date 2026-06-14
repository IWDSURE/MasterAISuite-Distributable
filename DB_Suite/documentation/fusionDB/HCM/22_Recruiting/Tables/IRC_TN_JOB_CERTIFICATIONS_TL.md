# IRC_TN_JOB_CERTIFICATIONS_TL

Table for storing the flattened License & Certification information of the requisition.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobcertificationstl-5949.html#irctnjobcertificationstl-5949](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobcertificationstl-5949.html#irctnjobcertificationstl-5949)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TN_JOB_CERTS_TL_PK | TN_JOB_CERTIFICATION_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TN_JOB_CERTIFICATION_ID | NUMBER |  | 18 | Yes | Part of the Primary Key for this table. Foreign key to IRC_TN_JOB_CERTIFICATIONS_B table. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| SECTION_NAME | VARCHAR2 | 240 |  |  | Stores the Section Name of the requisition. Derived from IRC_REQUISITIONS_B.PROFILE_ID, HRT_PROFILE_TYP_SECTIONS_VL.NAME. |
| CERTIFICATION_NAME | VARCHAR2 | 700 |  | Yes | Stores the Certification Name of the requisition. Derived from IRC_REQUISITIONS_B.PROFILE_ID, HRT_CONTENT_ITEMS_VL.NAME and HRT_CERTIFICATION_ITEMS_V.CERTIFICATION_NAME. |
| ESTABLISHMENT_NAME | VARCHAR2 | 2000 |  |  | Stores the Establishment Name of the requisition. Derived from IRC_REQUISITIONS_B.PROFILE_ID, HRT_ESTABLISHMENTS_CI_V.NAME and HRT_CERTIFICATION_ITEMS_V.EDUCATIONAL_ESTABLISHMENT. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TN_JOB_CERTS_TL_PK | Unique | Default | TN_JOB_CERTIFICATION_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
