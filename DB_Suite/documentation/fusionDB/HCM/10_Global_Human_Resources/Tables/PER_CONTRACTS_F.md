# PER_CONTRACTS_F

This table holds general details of a contract associated to an employment agreement. This is date-tracked. 
Main changes are related to the ability of identifying the set of Employment/Placement Terms this contract belongs to.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percontractsf-14367.html#percontractsf-14367](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percontractsf-14367.html#percontractsf-14367)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CONTRACTS_F_PK | CONTRACT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| CONTRACT_ID | NUMBER |  | 18 | Yes | System generated primary key. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_PERSONS. |  |
| REFERENCE | VARCHAR2 | 80 |  |  | Same as assignment number (for the row that represents work terms). |  |
| TYPE | VARCHAR2 | 30 |  |  | The type of contract. |  |
| STATUS | VARCHAR2 | 30 |  |  | The status of the contract. |  |
| STATUS_REASON | VARCHAR2 | 240 |  |  | The reason for the contracts existence. |  |
| ACTION_CODE | VARCHAR2 | 30 |  |  | Specifies the action performed on the particular record. For example: HIRE. |  |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Description of the contract. |  |
| DURATION | NUMBER |  | 25 |  | The duration of the contract. |  |
| DURATION_UNITS | VARCHAR2 | 30 |  |  | The units of time in which the duration is expressed. |  |
| CONTRACTUAL_JOB_TITLE | VARCHAR2 | 80 |  |  | The contractual job title - N.B. not related to PER_JOBS. |  |
| PARTIES | VARCHAR2 | 80 |  |  | The signatory parties (other than the employee). |  |
| START_REASON | VARCHAR2 | 30 |  |  | The reason for the contracts existence. |  |
| END_REASON | VARCHAR2 | 30 |  |  | The reason for ending the contract. |  |
| LEGISLATION_CODE | VARCHAR2 | 150 |  |  | LEGISLATION_CODE |  |
| NUMBER_OF_EXTENSIONS | NUMBER |  | 9 |  | The number of times the contract has been extended. |  |
| EXTENSION_REASON | VARCHAR2 | 80 |  |  | The reason for extending the contract. |  |
| EXTENSION_PERIOD | NUMBER |  | 25 |  | The period of time for which the contract has been extended. |  |
| EXTENSION_PERIOD_UNITS | VARCHAR2 | 30 |  |  | The units of time in which the extension period has been expressed. |  |
| CONTRACT_END_DATE | DATE |  |  |  | The date the contract is expected to end |  |
| CONTRACT_NUMBER | VARCHAR2 | 30 |  |  | Uniquely identifies a contract. If there are multiple contracts under a work relationship,sequence value will be incremented |  |
| PERIOD_OF_SERVICE_ID | NUMBER |  | 18 |  | Identifies the Employment Level. One to many relationship from PER_PERIODS_OF_SERVICE |  |
| CTR_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| DOC_STATUS | VARCHAR2 | 240 |  |  | This column holds the status of the physical contract. |  |
| DOC_STATUS_CHANGE_DATE | DATE |  |  |  | Holds the date that the doc_status column last changed its value. |  |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Identifies a set of Employment /Placement Terms. Foreign Key to PER_ALL_ASSIGNMENTS_M. |  |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Contract Attributes (PER_CONTRACT_DF) |
| CTR_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| WORK_TERMS_TYPE | VARCHAR2 | 30 |  |  | Obsolete. Do Not Use. |  |
| CTR_INFORMATION_DATE1 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_DATE2 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_DATE3 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_DATE4 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_DATE5 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_DATE6 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_DATE7 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_DATE8 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_DATE9 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_DATE10 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_DATE11 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_DATE12 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_DATE13 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_DATE14 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_DATE15 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION31 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION32 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION33 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION34 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION35 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION36 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION37 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION38 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION39 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION40 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION41 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION42 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION43 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION44 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION45 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION46 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION47 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION48 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION49 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION50 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER1 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER2 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER3 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER4 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER5 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER6 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER7 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER8 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER9 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER10 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER11 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER12 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER13 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER14 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER15 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER16 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER17 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER18 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER19 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |
| CTR_INFORMATION_NUMBER20 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Contract Legislative Information (PER_CONTRACT_LEG_DDF) |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CONTRACTS_F_N1 | Non Unique | Default | BUSINESS_GROUP_ID |
| PER_CONTRACTS_F_N2 | Non Unique | Default | PERSON_ID |
| PER_CONTRACTS_F_N3 | Non Unique | Default | ASSIGNMENT_ID |
| PER_CONTRACTS_F_N4 | Non Unique | Default | PERIOD_OF_SERVICE_ID |
| PER_CONTRACTS_F_PK | Unique | Default | CONTRACT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
