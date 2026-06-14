# IRC_TN_JOB_CERTIFICATIONS_B

Table for storing the License & Certification information of the requisition.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobcertificationsb-5097.html#irctnjobcertificationsb-5097](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobcertificationsb-5097.html#irctnjobcertificationsb-5097)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TN_JOB_CERTS_B_PK | TN_JOB_CERTIFICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TN_JOB_CERTIFICATION_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| TN_JOB_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TN_JOBS_B table. |
| FA_CERTIFICATION_ID | NUMBER |  | 18 | Yes | Stores the Certification ID of the requisition. Derived from IRC_REQUISITIONS_B.PROFILE_ID, HRT_CERTIFICATION_ITEMS_V.CERTIFICATION_ID. |
| FA_SECTION_ID | NUMBER |  | 18 |  | Stores the Section ID of the requisition. Derived from IRC_REQUISITIONS_B.PROFILE_ID, HRT_CERTIFICATION_ITEMS_V.SECTION_ID. |
| FA_CONTENT_ITEM_ID | NUMBER |  | 18 |  | Stores the Content Item ID of the requisition. Derived from IRC_REQUISITIONS_B.PROFILE_ID, HRT_CERTIFICATION_ITEMS_V.CONTENT_ITEM_ID. |
| FA_CONTENT_ITEM_CODE | VARCHAR2 | 30 |  |  | Stores the Content Item Code of the requisition. Derived from IRC_REQUISITIONS_B.PROFILE_ID, HRT_CONTENT_ITEMS_VL.CONTENT_ITEM_CODE. |
| FA_ESTABLISHMENT_ID | NUMBER |  | 18 |  | Stores the Establishment ID Code of the requisition. Derived from IRC_REQUISITIONS_B.PROFILE_ID, HRT_CERTIFICATION_ITEMS_V.EDUCATIONAL_ESTABLISHMENT_ID. |
| FA_ESTABLISHMENT_CODE | VARCHAR2 | 30 |  |  | Stores the Establishment Code of the requisition. Derived from IRC_REQUISITIONS_B.PROFILE_ID, HRT_ESTABLISHMENTS_CI_V.SCHOOL_CODE. |
| FA_COUNTRY_CODE | VARCHAR2 | 30 |  |  | Stores the Country Code of the requisition. Derived from IRC_REQUISITIONS_B.PROFILE_ID, HRT_CERTIFICATION_ITEMS_V.COUNTRY_CODE. |
| FA_STATE_PROVINCE_CODE | VARCHAR2 | 360 |  |  | Stores the State Province Code of the requisition. Derived from IRC_REQUISITIONS_B.PROFILE_ID, HRT_CERTIFICATION_ITEMS_V.STATE_PROVINCE_CODE. |
| REQUIRED_FLAG | VARCHAR2 | 30 |  |  | Stores the Required Flag of the requisition. Derived from IRC_REQUISITIONS_B.PROFILE_ID, HRT_CERTIFICATION_ITEMS_V.REQUIRED_FLAG. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TN_JOB_CERTS_B_FK1 | Non Unique | Default | TN_JOB_ID |
| IRC_TN_JOB_CERTS_B_PK | Unique | Default | TN_JOB_CERTIFICATION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
