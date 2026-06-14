# PAY_PERSON_PAY_METHODS_F

personal payment methods definition

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypersonpaymethodsf-28409.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypersonpaymethodsf-28409.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_PERSON_PAY_METHODS_PK | PERSONAL_PAYMENT_METHOD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PERSONAL_PAYMENT_METHOD_ID | NUMBER |  | 18 | Yes | PERSONAL_PAYMENT_METHOD_ID |  |
| NAME | VARCHAR2 | 250 |  |  | NAME |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | PAYROLL_RELATIONSHIP_ID |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| PAYMENT_AMOUNT_TYPE | VARCHAR2 | 30 |  |  | PAYMENT_AMOUNT_FLAG |  |
| REMAINING_AMOUNT_FLAG | VARCHAR2 | 1 |  |  | REMAINING_AMOUNT_FLAG |  |
| ORG_PAYMENT_METHOD_ID | NUMBER |  | 18 | Yes | ORG_PAYMENT_METHOD_ID |  |
| BANK_ACCOUNT_ID | NUMBER |  | 18 |  | BANK_ACCOUNT_ID |  |
| AMOUNT | NUMBER |  |  |  | AMOUNT |  |
| PERCENTAGE | NUMBER |  | 22 |  | PERCENTAGE |  |
| PRIORITY | NUMBER |  | 18 |  | PRIORITY |  |
| RUN_TYPE_ID | NUMBER |  | 18 |  | RUN_TYPE_ID |  |
| THIRD_PARTY_PAYEE_ID | NUMBER |  | 18 |  | THIRD_PARTY_PAYEE_ID |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Personal Payment Attributes (PAY_PERSON_PAY_METHODS_DFF) |
| PPM_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | PPM_INFORMATION_CATEGORY | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| PPM_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Personal Payment Information (PAY_PERSON_PAY_METHODS_DDF) |
| TXN_SOURCE | VARCHAR2 | 10 |  |  | Transaction Source |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_PERSON_PAY_METHODS_FK1 | Non Unique | Default | LEGISLATIVE_DATA_GROUP_ID |
| PAY_PERSON_PAY_METHODS_F_N2 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID |
| PAY_PERSON_PAY_METHODS_N4 | Non Unique | Default | ORG_PAYMENT_METHOD_ID |
| PAY_PERSON_PAY_METHODS_PK | Unique | Default | PERSONAL_PAYMENT_METHOD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
