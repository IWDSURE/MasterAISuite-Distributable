# PER_CONTACT_RELSHIPS_F_

This table store the effective dated Person-Person relationship details for a person

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percontactrelshipsf-13572.html#percontactrelshipsf-13572](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percontactrelshipsf-13572.html#percontactrelshipsf-13572)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CONTACT_RELSHIPS_F_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, CONTACT_RELATIONSHIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity |  |
| STATUTORY_DEPENDENT | VARCHAR2 | 30 |  |  | Identifies the person contact as dependent. |  |
| BENEFICIARY_FLAG | VARCHAR2 | 30 |  |  | Identifies if the relationship is beneficiary or not. | Active |
| EXISTING_PERSON | VARCHAR2 | 30 |  |  | Indicate whether the contact relationship is created from an existing person |  |
| BONDHOLDER_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the person is a potential EE bondholder. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. | Active |
| CONT_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive flexfield structure defining column. | Active |
| CONT_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Oracle-reserved descriptive flexfield structure defining column. | Active |
| CONTACT_PERSON_ID | NUMBER |  | 18 |  | Person identifier of second person in the relationship. Foreign key to PER_ALL_PEOPLE_F. | Active |
| CONTACT_RELATIONSHIP_ID | NUMBER |  | 18 | Yes | System generated part of the primary key. Surrogate key. | Active |
| CONTACT_TYPE | VARCHAR2 | 30 |  |  | Type of relationship between the two people concerned. | Active |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. | Active |
| DEPENDENT_FLAG | VARCHAR2 | 30 |  |  | Identifier if the relationship is dependent or not. | Active |
| END_LIFE_REASON_ID | NUMBER |  | 18 |  | Identifies the reason the relationship ended. Foreign key to BEN_LER_F. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| PERSON_ID | NUMBER |  | 18 |  | Person identifier of first person in the relationship. Foreign key to PER_ALL_PEOPLE_F. | Active |
| PERSONAL_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the relationship is a personal relationship. | Active |
| PRIMARY_CONTACT_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the second person of the relationship is the primary contact of the first person in the relationship. | Active |
| RLTD_PER_RSDS_W_DSGNTR_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the two people in the relationship live at the same address. | Active |
| SEQUENCE_NUMBER | NUMBER |  | 9 |  | The unique sequence number for the relationship used to identify contacts with a third party organization. | Active |
| START_LIFE_REASON_ID | NUMBER |  | 18 |  | Identifies the reason the relationship started. Foreign key to BEN_LER_F. | Active |
| THIRD_PARTY_PAY_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the contact receives third party payments from the employee. | Active |
| CONT_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| CONT_INFORMATION1 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION2 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION3 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION4 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION5 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION6 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION7 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION8 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION9 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION10 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION11 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION12 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION13 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION14 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION15 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION16 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION17 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION18 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION19 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| CONT_INFORMATION20 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Active |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. | Active |
| EMERGENCY_CONTACT_FLAG | VARCHAR2 | 30 |  |  | Flag which distinguishes emergency contacts from other types of relationship | Active |
| CONT_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| CONT_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| CONT_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| CONT_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| CONT_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| CONT_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| CONT_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| CONT_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| CONT_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| CONT_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION21 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. |  |
| CONT_INFORMATION22 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. |  |
| CONT_INFORMATION23 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. |  |
| CONT_INFORMATION24 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. |  |
| CONT_INFORMATION25 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. |  |
| CONT_INFORMATION26 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. |  |
| CONT_INFORMATION27 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. |  |
| CONT_INFORMATION28 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. |  |
| CONT_INFORMATION29 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. |  |
| CONT_INFORMATION30 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. |  |
| CONT_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CONT_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |  |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |  |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PCRFN1_ | Non Unique | Default | CONTACT_RELATIONSHIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LAST_UPDATE_DATE |
| PER_CONTACT_RELSHIPS_F_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, CONTACT_RELATIONSHIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
