# PAY_ORG_PAY_METHODS_F

table to define payment methods for org

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payorgpaymethodsf-4763.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payorgpaymethodsf-4763.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ORG_PAYMENT_METHODS_F_PK | ORG_PAYMENT_METHOD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ORG_PAYMENT_METHOD_ID | NUMBER |  | 18 | Yes | ORG_PAYMENT_METHOD_ID |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| BANK_ACCOUNT_ID | NUMBER |  | 18 |  | BANK_ACCOUNT_ID |  |
| PAYMENT_TYPE_ID | NUMBER |  | 18 | Yes | PAYMENT_TYPE_ID |  |
| CURRENCY_CODE | VARCHAR2 | 15 |  |  | CURRENCY_CODE |  |
| DEFINED_BALANCE_ID | NUMBER |  | 18 |  | Foreign key to PAY_DEFINED_BALANCES. |  |
| THIRD_PARTY_FLAG | VARCHAR2 | 30 |  |  | THIRD_PARTY_FLAG |  |
| BASE_ORG_PAY_METHOD_NAME | VARCHAR2 | 80 |  | Yes | BASE_ORG_PAY_METHOD_NAME |  |
| TYPE | VARCHAR2 | 30 |  |  | TYPE |  |
| ORGANIZATION_ID | NUMBER |  | 18 |  | ORGANIZATION_ID |  |
| TIME_DEFINITION_ID | NUMBER |  | 18 |  | TIME_DEFINITION_ID |  |
| PARENT_ORG_PAY_METHOD_ID | NUMBER |  | 18 |  | PARENT_ORG_PAY_METHOD_ID |  |
| DEFER_PAYMENT_MODE | VARCHAR2 | 30 |  |  | If the Payment Date is a weekend or bank holiday should the Payment be made before or after the holiday. |  |
| PRE_VALIDATION_REQUIRED | VARCHAR2 | 30 |  |  | PRE_VALIDATION_REQUIRED |  |
| VALIDATION_DAYS | NUMBER |  | 18 |  | VALIDATION_DAYS |  |
| VALIDATION_VALUE | VARCHAR2 | 15 |  |  | VAIDATION_VALUE |  |
| EXT_DELIVERY_OPTION_ID | NUMBER |  | 18 |  | EXT_DELIVERY_OPTION_ID |  |
| THIRD_PARTY_DEL_OPTION_ID | NUMBER |  | 18 |  | THIRD_PARTY_DEL_OPTION_ID |  |
| ROLLUP_PAYMENT_FLAG | VARCHAR2 | 30 |  |  | Indicates whether Payments can be rolled up across employees when paying. |  |
| PAYMENT_REFERENCE_FLAG | VARCHAR2 | 30 |  |  | Indicates whether multiple payments from a single employee needs to be separated out by reference number. |  |
| EFT_TEXT | VARCHAR2 | 120 |  |  | Text that appears in the header of the XML |  |
| EFT_TEXT2 | VARCHAR2 | 120 |  |  | EFT_TEXT2 |  |
| EFT_TRANSACTION_LIMIT | NUMBER |  | 32 |  | EFT_TRANSACTION_LIMIT |  |
| EFT_FILE_LIMIT | NUMBER |  | 32 |  | EFT_FILE_LIMIT |  |
| EFT_REFERENCE | VARCHAR2 | 30 |  |  | Reference Code for used on the EFT Payment. |  |
| EFT_USER_REFERENCE | VARCHAR2 | 30 |  |  | EFT_USER_REFERENCE |  |
| EFT_USER_REFERENCE_TYPE | VARCHAR2 | 30 |  |  | EFT_USER_REFERENCE_TYPE |  |
| EFT_USER_NAME | VARCHAR2 | 30 |  |  | EFT_USER_NAME |  |
| EFT_BUREAU_REFERENCE | VARCHAR2 | 30 |  |  | EFT_BUREAU_REFERANCE |  |
| EFT_BUREAU_REFERENCE_TYPE | VARCHAR2 | 30 |  |  | EFT_BUREAU_REFERENCE_TYPE |  |
| EFT_BUREAU_NAME | VARCHAR2 | 30 |  |  | EFT_BUREAU_NAME |  |
| EFT_BALANCING_FLAG | VARCHAR2 | 1 |  |  | This is used to indicate that a XML generated should produce a balancing entry. Y or N |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Org Payment Attributes (PAY_ORG_PAY_METHODS_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| PMETH_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | PMETH_INFORMATION_CATEGORY | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |
| PMETH_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Org Payment Information (PAY_ORG_PAY_METHODS_DDF) |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ORG_PAY_METHODS_F_FK4 | Non Unique | Default | DEFINED_BALANCE_ID |
| PAY_ORG_PAY_METHODS_F_N1 | Non Unique | Default | PARENT_ORG_PAY_METHOD_ID |
| PAY_ORG_PAY_METHODS_F_PK | Unique | Default | ORG_PAYMENT_METHOD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
