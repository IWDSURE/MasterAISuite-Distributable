# IRC_ESIGNATURES

This table contains ESignatures.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircesignatures-3980.html#ircesignatures-3980](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircesignatures-3980.html#ircesignatures-3980)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_ESIGNATURES_PK | ESIGNATURE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ESIGNATURE_ID | NUMBER |  | 18 | Yes | Primary key of the table. System generated. |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | The type of object to which the Esignature is related. |
| OBJECT_ID | NUMBER |  | 18 | Yes | The primary key of the object to which the current ESignature is related. |
| VALUE_HASH | VARCHAR2 | 100 |  |  | Hash of the value provided when using ESignature. |
| IP_ADDRESS | VARCHAR2 | 100 |  |  | IP adress of the HTTP connection when ESignature get used. |
| FULL_NAME | VARCHAR2 | 1000 |  |  | Signee's full name at the moment of the ESignature. |
| PERSON_ID | NUMBER |  | 18 | Yes | Signee's person unique identifier. |
| SIGNATURE_DATE | TIMESTAMP |  |  | Yes | Date time when eSignature was used. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| DISCRIMINANT_OBJECT_ID | NUMBER |  | 18 |  | Column introduced to support multiple secondary esignatures per object type. Will store the Primary key of the discriminant object. |
| DISCRIMINANT_OBJECT_TYPE | VARCHAR2 | 30 |  |  | Column introduced to support multiple secondary esignatures per object type. Will store the lookup code of the discriminant object. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_ESIGNATURES_FK1 | Non Unique | Default | PERSON_ID |
| IRC_ESIGNATURES_FK2 | Non Unique | Default | OBJECT_TYPE, OBJECT_ID |
| IRC_ESIGNATURES_U1 | Unique | Default | ESIGNATURE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
