# WLF_LEARNING_ITEMS_F

Table to store language-independent information of learning item objects.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearningitemsf-26151.html#wlflearningitemsf-26151](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearningitemsf-26151.html#wlflearningitemsf-26151)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LEARNING_ITEMS_F_PK | LEARNING_ITEM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| FEATURED_DATE | DATE |  |  |  | This column stores the featured date |
| FEATURED_END_DATE | DATE |  |  |  | This column stores the featured end date |
| FEATURED_FLAG | VARCHAR2 | 30 |  |  | Featured learning items recommended by Admin |
| ACCESS_PERMISSION_ID | NUMBER |  | 18 |  | LI level default access permission id |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LEARNING_ITEM_TYPE | VARCHAR2 | 32 |  | Yes | Polymorphic discriminator column { DOCUMENT, VIDEO, TUTORIAL ... }. |
| LEARNING_ITEM_SUB_TYPE | VARCHAR2 | 30 |  |  | Learning Item sub type for the learning item type like ELearning. eg: Tutorial, Video etc. |
| LEARNING_ITEM_CATEGORY | VARCHAR2 | 30 |  |  | Learning Item Category to differentiate same learning item type objects |
| LEARNING_ITEM_NUMBER | VARCHAR2 | 2000 |  |  | This column stores the learning item number |
| UUID | VARCHAR2 | 64 |  |  | UUID for Learning Item from table |
| LOCATION | VARCHAR2 | 4000 |  |  | Information about location of the content object. |
| STATUS | VARCHAR2 | 30 |  | Yes | Current status of the content object {ACTIVE, DELETED}. |
| SS_VIEW_MODE | VARCHAR2 | 30 |  |  | LI level default self-service view mode |
| ADMIN_ACCESS_MODE | VARCHAR2 | 30 |  |  | LI level default admin access mode |
| VISIBILITY | VARCHAR2 | 32 |  | Yes | Visibility of the content object {PUBLIC, PRIVATE, UNLISTED}. |
| THUMBNAIL_ID | NUMBER |  | 18 |  | Thumbnail associated with the content object. |
| DURATION | NUMBER |  |  |  | Video section duration or description duration for non-video section. |
| DURATION_UOM | VARCHAR2 | 30 |  |  | This column stores the duration uom |
| TRAILER_LI_ID | NUMBER |  | 18 |  | This column stores the trailer learning item id |
| LANGUAGE_ID | NUMBER |  | 18 |  | This column stores the language id |
| LANGUAGE_CODE | VARCHAR2 | 30 |  |  | Language of the learning item. FND Lookup column |
| AUTO_COMPETANCY_UPDATE_FLAG | VARCHAR2 | 1 |  |  | Indicates auto competancy update flag |
| ASSIGNMENT_RULE_ENABLED | VARCHAR2 | 1 |  |  | Indicates if assignment rule is enabled |
| ASSIGNMENT_RULE_ID | NUMBER |  | 18 |  | This column stores the assignment rule |
| ERES_ENABLED | VARCHAR2 | 1 |  |  | Indicates eres is enabled for learning item |
| SOURCE_INFO | VARCHAR2 | 240 |  |  | This column stores the source information |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | This column stores the source type |
| SOURCE_ID | NUMBER |  | 18 |  | This column stores the source id |
| START_DATE | TIMESTAMP |  |  |  | This column stores the start date |
| END_DATE | TIMESTAMP |  |  |  | This column stores the end date |
| OWNED_BY_ID | NUMBER |  | 18 | Yes | Indicates the person identifier who ownes the content object. |
| CREATED_BY_ID | NUMBER |  | 18 | Yes | Indicates the person identifier who created the content object. |
| ATTRIBUTION_ID | NUMBER |  | 18 |  | This column stores the attribution id |
| ATTRIBUTION_TYPE | VARCHAR2 | 30 |  |  | This column stores the attribution type |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| DELETED_BY_ID | NUMBER |  | 18 |  | Indicates the person identifier who deleted the content object. |
| DELETED_DATE | TIMESTAMP |  |  |  | Indicates the date and time of the deletion of the content object. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CO_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CO_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PRICE | NUMBER |  |  |  | Indicates the cost of the learning item |
| MIN_PRICE | NUMBER |  |  |  | Indicates the minimum cost of the learning item |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | Indicates the currency type of the price column |
| PRICING_RULE_ID | NUMBER |  | 18 |  | Identifier of pricing rule. Foreign key to WLF_PRICING_RULES_F. |
| ADMIN_ACCESS_PERMISSION_ID | NUMBER |  | 18 |  | Admin access permission identifier |
| ADMIN_VIEW_ACCESS_MODE | VARCHAR2 | 30 |  |  | This column stores various options for admin's view access mode for admin managed learning items |
| ADMIN_ADMINISTRATION_MODE | VARCHAR2 | 30 |  |  | This column stores various options for admin's administration access mode for admin managed learning items |
| INSTRUCT_ACCESS_PERMISSION_ID | NUMBER |  | 18 |  | Instructor access permission identifier |
| LI_START_DATE | TIMESTAMP |  |  |  | Indicates learning item start date |
| LI_END_DATE | TIMESTAMP |  |  |  | Indicates learning item end date |
| TIME_ZONE | VARCHAR2 | 30 |  |  | Indicates time zone of learning start and end dates |
| CALCULATED_RATING | NUMBER |  |  |  | Indicates learning item rating |
| RATING_COUNT | NUMBER |  |  |  | Indicates learning item rating count |
| IS_GLOBAL_AG | VARCHAR2 | 30 |  |  | The column will have value "Y" for GLOBAL access groups and "N" for follow and adhoc access groups |
| PAYMENT_RULE_ID | NUMBER |  | 18 |  | Identifier of pricing rule Payment Type. Foreign key to WLF_PAYMENT_RULES_F |
| LEARNING_ITEM_URL | VARCHAR2 | 4000 |  |  | This column stores external URL for a non-catalog learning item. |
| DELIVERY_PROVIDER | VARCHAR2 | 64 |  |  | This column represents storage provider for Video or Image. Strorage Provider is actual loaction where content binary data stored. Example : Akamai,UCM |
| THUMBNAIL_PROVIDER | VARCHAR2 | 64 |  |  | This column represents storage provider for Thumbanil or Cover Art images. Strorage Provider is actual loaction where content binary data stored. Example : Akamai,UCM |
| LI_CHANGE_EVENT_DATE | TIMESTAMP |  |  |  | Represents the time when learning item has material changes for learning item change event job to run. |
| RECONCILE_START_DATE | TIMESTAMP |  |  |  | Represents the time when reconcile is started to process learning item change event. |
| RECONCILE_END_DATE | TIMESTAMP |  |  |  | Represents the time when reconcile is completed to process learning item change event. |
| RECONCILE_JOB_ID | NUMBER |  | 18 |  | Represents the Latest Reconcile ESS JOB ID ran for processing learning item change event. |
| VIEW_COUNT | NUMBER |  | 18 |  | This attribute will store view count for a given learning item. |
| IS_XML_KEYWORDS_PROCESSED | VARCHAR2 | 3 |  |  | Column to have value 'Y' once xml keywords are processed after last update from application. |
| IS_SEARCH_TERMS_PROCESSED | VARCHAR2 | 3 |  |  | Column to have value 'Y' once search terms are processed after last update from application. |
| IN_ATTACHMENTS | VARCHAR2 | 30 |  |  | Indicates whether the content media file is in FND Attachments. Possible values are NEEDED/DONE/FAILED. |
| ENVIRONMENT_REFRESH | VARCHAR2 | 30 |  |  | Indicates whether the content item is enabled for environment refresh. Possible values are ENABLED/DISABLED. |
| IS_AI_SKILLS_PROCESSED | VARCHAR2 | 1 |  |  | Column to have value 'Y' once AI suggested skills are processed after last update from application. |
| IS_RECONCILE_READY | VARCHAR2 | 1 |  |  | Indicates reconcile is done for learning item |
| EFFORT_IN_SECONDS | NUMBER |  |  |  | This column stores the effort in seconds |
| SEND_ALERT | VARCHAR2 | 1 |  |  | Column to have value 'Y' to send alerts to learns after reconcilation. |
| PUBLISHER_TYPE | VARCHAR2 | 32 |  |  | This column stores the publisher type |
| AUTHOR_PERSON_ID | NUMBER |  | 18 |  | This column stores the author person id |
| AUTHOR_TYPE | VARCHAR2 | 32 |  |  | This column stores the author type |
| AUTHOR_DISPLAY_NAME | VARCHAR2 | 2000 |  |  | This column stores the author display name |
| AUTHOR_PERSON_NUMBER | VARCHAR2 | 30 |  |  | This column stores the author person number |
| INSTRUCTOR_PERSON_ID | NUMBER |  | 18 |  | This column stores the instructor person id |
| INSTRUCTOR_TYPE | VARCHAR2 | 32 |  |  | This column stores the instructor type |
| INSTRUCTOR_DISPLAY_NAME | VARCHAR2 | 2000 |  |  | This column stores the instructor display name |
| INSTRUCTOR_PERSON_NUMBER | VARCHAR2 | 30 |  |  | This column stores the instructor person number |
| PROVIDER | VARCHAR2 | 32 |  |  | This column stores the provider |
| PROVIDER_TYPE | VARCHAR2 | 32 |  |  | This column stores the provider type |
| COORDINATOR_PERSON_ID | NUMBER |  | 18 |  | Indicates person id of the coordinator |
| COORDINATOR_PERSON_NUMBER | VARCHAR2 | 32 |  |  | Indicates person number of the coordinator |
| BUSINESS_DRIVER | VARCHAR2 | 32 |  |  | This column stores the business driver |
| NOTIFICATION_PATTERN | VARCHAR2 | 32 |  |  | This column stores the notification pattern |
| LEARNING_LEVEL | VARCHAR2 | 32 |  |  | This column stores the learning level |
| CPE_TYPE | VARCHAR2 | 30 |  |  | This column stores continued professional education type. This column accepts values for lookup ORA_WLF_CPE_TYPE |
| PUBLISHER_NAME | VARCHAR2 | 2000 |  |  | This column stores the publisher name |
| CPE_POINTS | NUMBER |  |  |  | This column stores continued professional education points for the given continued professional education type stored in CPE_TYPE column |
| AUTHORED_ON_DATE | TIMESTAMP |  |  |  | Provider learning item authored date |
| PROVIDER_SKILLS_QUALIFICATIONS | CLOB |  |  |  | This column stores the skills and qualifications |
| PROVIDER_CATEGORY_TOPICS | CLOB |  |  |  | This column stores the categories and topics |
| PROVIDER_SOURCE | CLOB |  |  |  | This column stores the provider source mapping type and content codes |
| PROVIDER_CATEGORIES_STRUCTURED | CLOB |  |  |  | Categories and Topics Structured |
| LEARNING_ITEM_VERSION_NUMBER | NUMBER |  |  |  | Learning Item Version Number |
| REACTIVATE_REASON_CODE | VARCHAR2 | 30 |  |  | Reason code for reactivation |
| INACTIVATE_REASON_CODE | VARCHAR2 | 30 |  |  | Reason code for inactivation |
| DELETE_REASON_CODE | VARCHAR2 | 30 |  |  | Reason code for deletion |
| STATUS_CHANGE_COMMENTS | VARCHAR2 | 4000 |  |  | User Comments while triggering any status action on learning item |
| INACTIVATE_DATE | TIMESTAMP |  |  |  | Learning Item inactivation date |
| REACTIVATE_DATE | TIMESTAMP |  |  |  | Learning item reactivation date |
| ACTIVATION_DATE | TIMESTAMP |  |  |  | Learning Item activation date |
| SOURCE_PUBLISHED_DATE | TIMESTAMP |  |  |  | Content provider source publisher date |
| COMPLETION_CERTIFICATE_ENABLED | VARCHAR2 | 1 |  |  | Indicates if certificate is enabled or not |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| WLF_LEARNING_ITEMS_F_N1 | Non Unique | Default | LEARNING_ITEM_TYPE |  |
| WLF_LEARNING_ITEMS_F_N10 | Non Unique | Default | PRICE |  |
| WLF_LEARNING_ITEMS_F_N11 | Non Unique | Default | LANGUAGE_CODE |  |
| WLF_LEARNING_ITEMS_F_N12 | Non Unique | Default | LI_START_DATE |  |
| WLF_LEARNING_ITEMS_F_N13 | Non Unique | Default | LI_END_DATE |  |
| WLF_LEARNING_ITEMS_F_N14 | Non Unique | Default | CALCULATED_RATING |  |
| WLF_LEARNING_ITEMS_F_N15 | Non Unique | Default | END_DATE, EFFECTIVE_START_DATE |  |
| WLF_LEARNING_ITEMS_F_N16 | Non Unique | Default | START_DATE |  |
| WLF_LEARNING_ITEMS_F_N17 | Non Unique | Default | FEATURED_FLAG |  |
| WLF_LEARNING_ITEMS_F_N18 | Non Unique | Default | FEATURED_DATE |  |
| WLF_LEARNING_ITEMS_F_N19 | Non Unique | Default | IS_XML_KEYWORDS_PROCESSED |  |
| WLF_LEARNING_ITEMS_F_N2 | Non Unique | Default | OWNED_BY_ID |  |
| WLF_LEARNING_ITEMS_F_N20 | Non Unique | Default | IS_SEARCH_TERMS_PROCESSED |  |
| WLF_LEARNING_ITEMS_F_N22 | Non Unique | Default | UPPER("LEARNING_ITEM_NUMBER") |  |
| WLF_LEARNING_ITEMS_F_N23 | Non Unique | Default | REACTIVATE_DATE |  |
| WLF_LEARNING_ITEMS_F_N24 | Non Unique | Default | ACTIVATION_DATE |  |
| WLF_LEARNING_ITEMS_F_N25 | Non Unique | Default | DELETED_DATE |  |
| WLF_LEARNING_ITEMS_F_N26 | Non Unique | Default | INACTIVATE_DATE |  |
| WLF_LEARNING_ITEMS_F_N27 | Non Unique | Default | LEARNING_ITEM_CATEGORY |  |
| WLF_LEARNING_ITEMS_F_N3 | Non Unique | Default | LEARNING_ITEM_NUMBER | Obsolete |
| WLF_LEARNING_ITEMS_F_N4 | Non Unique | Default | VISIBILITY |  |
| WLF_LEARNING_ITEMS_F_N5 | Non Unique | Default | STATUS |  |
| WLF_LEARNING_ITEMS_F_N7 | Non Unique | Default | ATTRIBUTION_ID |  |
| WLF_LEARNING_ITEMS_F_N9 | Non Unique | Default | ASSIGNMENT_RULE_ID |  |
| WLF_LEARNING_ITEMS_F_N6 | Non Unique | Default | LANGUAGE_ID | Obsolete |
| WLF_LEARNING_ITEMS_F_U1 | Unique | Default | LEARNING_ITEM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |  |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
