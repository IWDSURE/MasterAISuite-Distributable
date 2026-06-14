# FAI_RAG_DOC_CHUNK_METADATA

Fusion AI Rag Document Chunk Metadata.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** FAI_RAG_DOC_CHUNK_METADATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/fairagdocchunkmetadata-25829.html#fairagdocchunkmetadata-25829](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/fairagdocchunkmetadata-25829.html#fairagdocchunkmetadata-25829)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_RAG_DOC_CHUNK_METADATA_PK | CHUNK_METADATA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USE_CASE_PARTITION | VARCHAR2 | 400 |  |  | Partitioning key based on use case segmentation. |
| USE_CASE_ID | VARCHAR2 | 100 |  | Yes | The associated use case identifier. |
| CHUNK_METADATA_ID | NUMBER |  | 18 | Yes | Unique chunk metadata Identifier. |
| CHUNK_ID | NUMBER |  | 18 | Yes | Chunk ID. Unique identifier per chunk. |
| RAG_DOCUMENT_ID | NUMBER |  | 18 | Yes | Unique rag document identifier. |
| CHUNK_TEXT | JSON |  |  |  | A segment of text within a document. |
| CHUNK_ORDER | NUMBER |  | 18 |  | The sequential order of the chunk within a document. |
| EXPANDED_CHUNK_TEXT | CLOB |  |  |  | An expanded text chunk, including preceding or subsequent content. |
| DOCUMENT_TYPE | VARCHAR2 | 100 |  |  | Specifies the type of the document (e.g. application/pdf). |
| DOCUMENT_TITLE | VARCHAR2 | 1000 |  |  | The title heading of the document. |
| DOCUMENT_ID | VARCHAR2 | 100 |  |  | Unique identifier of a document in its source system. |
| DOCUMENT_STATUS | VARCHAR2 | 100 |  |  | Specifies current processing status of the document. |
| ENTITY_ID | VARCHAR2 | 100 |  |  | The identifier of the entity associated with the document. |
| DOCUMENT_CATEGORY | VARCHAR2 | 1000 |  |  | The category the document is classified in. |
| ENTITY_NAME | VARCHAR2 | 100 |  |  | Specifies the name of the entity associated with the document. |
| DOCUMENT_PROPERTIES | JSON |  |  |  | Additional properties of the document. |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | Active flag. |
| EXPIRATION_DATE | TIMESTAMP |  |  |  | Document Expiration Date. |
| SECURITY_CLASSIFICATION_1 | JSON |  |  |  | Custom security classification column 1. |
| SECURITY_CLASSIFICATION_2 | JSON |  |  |  | Custom security classification column 2. |
| PARENT_OBJECT_ID | VARCHAR2 | 200 |  |  | Parent ID for the current object. |
| GRANDPARENT_OBJECT_ID | VARCHAR2 | 200 |  |  | Grand parent ID for the current object. |
| ROOT_OBJECT_ID | VARCHAR2 | 200 |  |  | Root object ID for the current object. |
| FILTER_JSON_1 | JSON |  |  |  | Custom json field No 1. |
| FILTER_JSON_2 | JSON |  |  |  | Custom json field No 2. |
| FILTER_JSON_3 | JSON |  |  |  | Custom json field No 3. |
| FILTER_JSON_4 | JSON |  |  |  | Custom json field No 4. |
| FILTER_JSON_5 | JSON |  |  |  | Custom json field No 5. |
| FILTER_JSON_6 | JSON |  |  |  | Custom json field No 6. |
| FILTER_JSON_7 | JSON |  |  |  | Custom json field No 7. |
| FILTER_JSON_8 | JSON |  |  |  | Custom json field No 8. |
| FILTER_JSON_9 | JSON |  |  |  | Custom json field No 9. |
| FILTER_JSON_10 | JSON |  |  |  | Custom json field No 10. |
| FILTER_JSON_11 | JSON |  |  |  | Custom json field No 11. |
| FILTER_JSON_12 | JSON |  |  |  | Custom json field No 12. |
| FILTER_JSON_13 | JSON |  |  |  | Custom json field No 13. |
| FILTER_JSON_14 | JSON |  |  |  | Custom json field No 14. |
| FILTER_JSON_15 | JSON |  |  |  | Custom json field No 15. |
| FILTER_JSON_16 | JSON |  |  |  | Custom json field No 16. |
| FILTER_JSON_17 | JSON |  |  |  | Custom json field No 17. |
| FILTER_JSON_18 | JSON |  |  |  | Custom json field No 18. |
| FILTER_JSON_19 | JSON |  |  |  | Custom json field No 19. |
| FILTER_JSON_20 | JSON |  |  |  | Custom json field No 20. |
| FILTER_JSON_21 | JSON |  |  |  | Custom json field No 21. |
| FILTER_JSON_22 | JSON |  |  |  | Custom json field No 22. |
| FILTER_JSON_23 | JSON |  |  |  | Custom json field No 23. |
| FILTER_JSON_24 | JSON |  |  |  | Custom json field No 24. |
| FILTER_JSON_25 | JSON |  |  |  | Custom json field No 25. |
| FILTER_JSON_26 | JSON |  |  |  | Custom json field No 26. |
| FILTER_JSON_27 | JSON |  |  |  | Custom json field No 27. |
| FILTER_JSON_28 | JSON |  |  |  | Custom json field No 28. |
| FILTER_JSON_29 | JSON |  |  |  | Custom json field No 29. |
| FILTER_JSON_30 | JSON |  |  |  | Custom json field No 30. |
| FILTER_JSON_31 | JSON |  |  |  | Custom json field No 31. |
| FILTER_JSON_32 | JSON |  |  |  | Custom json field No 32. |
| FILTER_JSON_33 | JSON |  |  |  | Custom json field No 33. |
| FILTER_JSON_34 | JSON |  |  |  | Custom json field No 34. |
| FILTER_JSON_35 | JSON |  |  |  | Custom json field No 35. |
| FILTER_JSON_36 | JSON |  |  |  | Custom json field No 36. |
| FILTER_JSON_37 | JSON |  |  |  | Custom json field No 37. |
| FILTER_JSON_38 | JSON |  |  |  | Custom json field No 38. |
| FILTER_JSON_39 | JSON |  |  |  | Custom json field No 39. |
| FILTER_JSON_40 | JSON |  |  |  | Custom json field No 40. |
| FILTER_NUMBER_1 | NUMBER |  | 18 |  | Custom number field No 1. |
| FILTER_NUMBER_2 | NUMBER |  | 18 |  | Custom number field No 2. |
| FILTER_NUMBER_3 | NUMBER |  | 18 |  | Custom number field No 3. |
| FILTER_NUMBER_4 | NUMBER |  | 18 |  | Custom number field No 4. |
| FILTER_NUMBER_5 | NUMBER |  | 18 |  | Custom number field No 5. |
| FILTER_NUMBER_6 | NUMBER |  | 18 |  | Custom number field No 6. |
| FILTER_NUMBER_7 | NUMBER |  | 18 |  | Custom number field No 7. |
| FILTER_NUMBER_8 | NUMBER |  | 18 |  | Custom number field No 8. |
| FILTER_NUMBER_9 | NUMBER |  | 18 |  | Custom number field No 9. |
| FILTER_NUMBER_10 | NUMBER |  | 18 |  | Custom number field No 10. |
| FILTER_NUMBER_11 | NUMBER |  | 18 |  | Custom number field No 11. |
| FILTER_NUMBER_12 | NUMBER |  | 18 |  | Custom number field No 12. |
| FILTER_NUMBER_13 | NUMBER |  | 18 |  | Custom number field No 13. |
| FILTER_NUMBER_14 | NUMBER |  | 18 |  | Custom number field No 14. |
| FILTER_NUMBER_15 | NUMBER |  | 18 |  | Custom number field No 15. |
| FILTER_NUMBER_16 | NUMBER |  | 18 |  | Custom number field No 16. |
| FILTER_NUMBER_17 | NUMBER |  | 18 |  | Custom number field No 17. |
| FILTER_NUMBER_18 | NUMBER |  | 18 |  | Custom number field No 18. |
| FILTER_NUMBER_19 | NUMBER |  | 18 |  | Custom number field No 19. |
| FILTER_NUMBER_20 | NUMBER |  | 18 |  | Custom number field No 20. |
| FILTER_NUMBER_21 | NUMBER |  | 18 |  | Custom number field No 21. |
| FILTER_NUMBER_22 | NUMBER |  | 18 |  | Custom number field No 22. |
| FILTER_NUMBER_23 | NUMBER |  | 18 |  | Custom number field No 23. |
| FILTER_NUMBER_24 | NUMBER |  | 18 |  | Custom number field No 24. |
| FILTER_NUMBER_25 | NUMBER |  | 18 |  | Custom number field No 25. |
| FILTER_NUMBER_26 | NUMBER |  | 18 |  | Custom number field No 26. |
| FILTER_NUMBER_27 | NUMBER |  | 18 |  | Custom number field No 27. |
| FILTER_NUMBER_28 | NUMBER |  | 18 |  | Custom number field No 28. |
| FILTER_NUMBER_29 | NUMBER |  | 18 |  | Custom number field No 29. |
| FILTER_NUMBER_30 | NUMBER |  | 18 |  | Custom number field No 30. |
| FILTER_NUMBER_31 | NUMBER |  | 18 |  | Custom number field No 31. |
| FILTER_NUMBER_32 | NUMBER |  | 18 |  | Custom number field No 32. |
| FILTER_NUMBER_33 | NUMBER |  | 18 |  | Custom number field No 33. |
| FILTER_NUMBER_34 | NUMBER |  | 18 |  | Custom number field No 34. |
| FILTER_NUMBER_35 | NUMBER |  | 18 |  | Custom number field No 35. |
| FILTER_NUMBER_36 | NUMBER |  | 18 |  | Custom number field No 36. |
| FILTER_NUMBER_37 | NUMBER |  | 18 |  | Custom number field No 37. |
| FILTER_NUMBER_38 | NUMBER |  | 18 |  | Custom number field No 38. |
| FILTER_NUMBER_39 | NUMBER |  | 18 |  | Custom number field No 39. |
| FILTER_NUMBER_40 | NUMBER |  | 18 |  | Custom number field No 40. |
| FILTER_CHAR_1 | VARCHAR2 | 4000 |  |  | Custom char field No 1. |
| FILTER_CHAR_2 | VARCHAR2 | 4000 |  |  | Custom char field No 2. |
| FILTER_CHAR_3 | VARCHAR2 | 4000 |  |  | Custom char field No 3. |
| FILTER_CHAR_4 | VARCHAR2 | 4000 |  |  | Custom char field No 4. |
| FILTER_CHAR_5 | VARCHAR2 | 4000 |  |  | Custom char field No 5. |
| FILTER_CHAR_6 | VARCHAR2 | 4000 |  |  | Custom char field No 6. |
| FILTER_CHAR_7 | VARCHAR2 | 4000 |  |  | Custom char field No 7. |
| FILTER_CHAR_8 | VARCHAR2 | 4000 |  |  | Custom char field No 8. |
| FILTER_CHAR_9 | VARCHAR2 | 4000 |  |  | Custom char field No 9. |
| FILTER_CHAR_10 | VARCHAR2 | 4000 |  |  | Custom char field No 10. |
| FILTER_CHAR_11 | VARCHAR2 | 4000 |  |  | Custom char field No 11. |
| FILTER_CHAR_12 | VARCHAR2 | 4000 |  |  | Custom char field No 12. |
| FILTER_CHAR_13 | VARCHAR2 | 4000 |  |  | Custom char field No 13. |
| FILTER_CHAR_14 | VARCHAR2 | 4000 |  |  | Custom char field No 14. |
| FILTER_CHAR_15 | VARCHAR2 | 4000 |  |  | Custom char field No 15. |
| FILTER_CHAR_16 | VARCHAR2 | 4000 |  |  | Custom char field No 16. |
| FILTER_CHAR_17 | VARCHAR2 | 4000 |  |  | Custom char field No 17. |
| FILTER_CHAR_18 | VARCHAR2 | 4000 |  |  | Custom char field No 18. |
| FILTER_CHAR_19 | VARCHAR2 | 4000 |  |  | Custom char field No 19. |
| FILTER_CHAR_20 | VARCHAR2 | 4000 |  |  | Custom char field No 20. |
| FILTER_CHAR_21 | VARCHAR2 | 4000 |  |  | Custom char column 21. |
| FILTER_CHAR_22 | VARCHAR2 | 4000 |  |  | Custom char column 22. |
| FILTER_CHAR_23 | VARCHAR2 | 4000 |  |  | Custom char column 23. |
| FILTER_CHAR_24 | VARCHAR2 | 4000 |  |  | Custom char column 24. |
| FILTER_CHAR_25 | VARCHAR2 | 4000 |  |  | Custom char column 25. |
| FILTER_CHAR_26 | VARCHAR2 | 4000 |  |  | Custom char column 26. |
| FILTER_CHAR_27 | VARCHAR2 | 4000 |  |  | Custom char column 27. |
| FILTER_CHAR_28 | VARCHAR2 | 4000 |  |  | Custom char column 28. |
| FILTER_CHAR_29 | VARCHAR2 | 4000 |  |  | Custom char column 29. |
| FILTER_CHAR_30 | VARCHAR2 | 4000 |  |  | Custom char column 30. |
| FILTER_CHAR_31 | VARCHAR2 | 4000 |  |  | Custom char column 31. |
| FILTER_CHAR_32 | VARCHAR2 | 4000 |  |  | Custom char column 32. |
| FILTER_CHAR_33 | VARCHAR2 | 4000 |  |  | Custom char column 33. |
| FILTER_CHAR_34 | VARCHAR2 | 4000 |  |  | Custom char column 34. |
| FILTER_CHAR_35 | VARCHAR2 | 4000 |  |  | Custom char column 35. |
| FILTER_CHAR_36 | VARCHAR2 | 4000 |  |  | Custom char column 36. |
| FILTER_CHAR_37 | VARCHAR2 | 4000 |  |  | Custom char column 37. |
| FILTER_CHAR_38 | VARCHAR2 | 4000 |  |  | Custom char column 38. |
| FILTER_CHAR_39 | VARCHAR2 | 4000 |  |  | Custom char column 39. |
| FILTER_CHAR_40 | VARCHAR2 | 4000 |  |  | Custom char column 40. |
| FILTER_CHAR_41 | VARCHAR2 | 4000 |  |  | Custom char column 41. |
| FILTER_CHAR_42 | VARCHAR2 | 4000 |  |  | Custom char column 42. |
| FILTER_CHAR_43 | VARCHAR2 | 4000 |  |  | Custom char column 43. |
| FILTER_CHAR_44 | VARCHAR2 | 4000 |  |  | Custom char column 44. |
| FILTER_CHAR_45 | VARCHAR2 | 4000 |  |  | Custom char column 45. |
| FILTER_CHAR_46 | VARCHAR2 | 4000 |  |  | Custom char column 46. |
| FILTER_CHAR_47 | VARCHAR2 | 4000 |  |  | Custom char column 47. |
| FILTER_CHAR_48 | VARCHAR2 | 4000 |  |  | Custom char column 48. |
| FILTER_CHAR_49 | VARCHAR2 | 4000 |  |  | Custom char column 49. |
| FILTER_CHAR_50 | VARCHAR2 | 4000 |  |  | Custom char column 50. |
| FILTER_CHAR_51 | VARCHAR2 | 4000 |  |  | Custom char column 51. |
| FILTER_CHAR_52 | VARCHAR2 | 4000 |  |  | Custom char column 52. |
| FILTER_CHAR_53 | VARCHAR2 | 4000 |  |  | Custom char column 53. |
| FILTER_CHAR_54 | VARCHAR2 | 4000 |  |  | Custom char column 54. |
| FILTER_CHAR_55 | VARCHAR2 | 4000 |  |  | Custom char column 55. |
| FILTER_CHAR_56 | VARCHAR2 | 4000 |  |  | Custom char column 56. |
| FILTER_CHAR_57 | VARCHAR2 | 4000 |  |  | Custom char column 57. |
| FILTER_CHAR_58 | VARCHAR2 | 4000 |  |  | Custom char column 58. |
| FILTER_CHAR_59 | VARCHAR2 | 4000 |  |  | Custom char column 59. |
| FILTER_CHAR_60 | VARCHAR2 | 4000 |  |  | Custom char column 60. |
| FILTER_CHAR_61 | VARCHAR2 | 4000 |  |  | Custom char column 61. |
| FILTER_CHAR_62 | VARCHAR2 | 4000 |  |  | Custom char column 62. |
| FILTER_CHAR_63 | VARCHAR2 | 4000 |  |  | Custom char column 63. |
| FILTER_CHAR_64 | VARCHAR2 | 4000 |  |  | Custom char column 64. |
| FILTER_CHAR_65 | VARCHAR2 | 4000 |  |  | Custom char column 65. |
| FILTER_CHAR_66 | VARCHAR2 | 4000 |  |  | Custom char column 66. |
| FILTER_CHAR_67 | VARCHAR2 | 4000 |  |  | Custom char column 67. |
| FILTER_CHAR_68 | VARCHAR2 | 4000 |  |  | Custom char column 68. |
| FILTER_CHAR_69 | VARCHAR2 | 4000 |  |  | Custom char column 69. |
| FILTER_CHAR_70 | VARCHAR2 | 4000 |  |  | Custom char column 70. |
| FILTER_CHAR_71 | VARCHAR2 | 4000 |  |  | Custom char column 71. |
| FILTER_CHAR_72 | VARCHAR2 | 4000 |  |  | Custom char column 72. |
| FILTER_CHAR_73 | VARCHAR2 | 4000 |  |  | Custom char column 73. |
| FILTER_CHAR_74 | VARCHAR2 | 4000 |  |  | Custom char column 74. |
| FILTER_CHAR_75 | VARCHAR2 | 4000 |  |  | Custom char column 75. |
| FILTER_CHAR_76 | VARCHAR2 | 4000 |  |  | Custom char column 76. |
| FILTER_CHAR_77 | VARCHAR2 | 4000 |  |  | Custom char column 77. |
| FILTER_CHAR_78 | VARCHAR2 | 4000 |  |  | Custom char column 78. |
| FILTER_CHAR_79 | VARCHAR2 | 4000 |  |  | Custom char column 79. |
| FILTER_CHAR_80 | VARCHAR2 | 4000 |  |  | Custom char column 80. |
| FILTER_CHAR_81 | VARCHAR2 | 4000 |  |  | Custom char column 81. |
| FILTER_CHAR_82 | VARCHAR2 | 4000 |  |  | Custom char column 82. |
| FILTER_CHAR_83 | VARCHAR2 | 4000 |  |  | Custom char column 83. |
| FILTER_CHAR_84 | VARCHAR2 | 4000 |  |  | Custom char column 84. |
| FILTER_CHAR_85 | VARCHAR2 | 4000 |  |  | Custom char column 85. |
| FILTER_CHAR_86 | VARCHAR2 | 4000 |  |  | Custom char column 86. |
| FILTER_CHAR_87 | VARCHAR2 | 4000 |  |  | Custom char column 87. |
| FILTER_CHAR_88 | VARCHAR2 | 4000 |  |  | Custom char column 88. |
| FILTER_CHAR_89 | VARCHAR2 | 4000 |  |  | Custom char column 89. |
| FILTER_CHAR_90 | VARCHAR2 | 4000 |  |  | Custom char column 90. |
| FILTER_CHAR_91 | VARCHAR2 | 4000 |  |  | Custom char column 91. |
| FILTER_CHAR_92 | VARCHAR2 | 4000 |  |  | Custom char column 92. |
| FILTER_CHAR_93 | VARCHAR2 | 4000 |  |  | Custom char column 93. |
| FILTER_CHAR_94 | VARCHAR2 | 4000 |  |  | Custom char column 94. |
| FILTER_CHAR_95 | VARCHAR2 | 4000 |  |  | Custom char column 95. |
| FILTER_CHAR_96 | VARCHAR2 | 4000 |  |  | Custom char column 96. |
| FILTER_CHAR_97 | VARCHAR2 | 4000 |  |  | Custom char column 97. |
| FILTER_CHAR_98 | VARCHAR2 | 4000 |  |  | Custom char column 98. |
| FILTER_CHAR_99 | VARCHAR2 | 4000 |  |  | Custom char column 99. |
| FILTER_CHAR_100 | VARCHAR2 | 4000 |  |  | Custom char column 100. |
| FILTER_TIME_1 | TIMESTAMP |  |  |  | Custom time column 1. |
| FILTER_TIME_2 | TIMESTAMP |  |  |  | Custom time column 2. |
| FILTER_TIME_3 | TIMESTAMP |  |  |  | Custom time column 3. |
| FILTER_TIME_4 | TIMESTAMP |  |  |  | Custom time column 4. |
| FILTER_TIME_5 | TIMESTAMP |  |  |  | COLUMN1 |
| FILTER_TIME_6 | TIMESTAMP |  |  |  | Custom time column 6. |
| FILTER_TIME_7 | TIMESTAMP |  |  |  | Custom time column 7. |
| FILTER_TIME_8 | TIMESTAMP |  |  |  | Custom time column 8. |
| FILTER_TIME_9 | TIMESTAMP |  |  |  | Custom time column 9. |
| FILTER_TIME_10 | TIMESTAMP |  |  |  | Custom time column 10. |
| FILTER_TIME_11 | TIMESTAMP |  |  |  | Custom time column 11. |
| FILTER_TIME_12 | TIMESTAMP |  |  |  | Custom time column 12. |
| FILTER_TIME_13 | TIMESTAMP |  |  |  | Custom time column 13. |
| FILTER_TIME_14 | TIMESTAMP |  |  |  | Custom time column 14. |
| FILTER_TIME_15 | TIMESTAMP |  |  |  | Custom time column 15. |
| FILTER_TIME_16 | TIMESTAMP |  |  |  | Custom time column 16. |
| FILTER_TIME_17 | TIMESTAMP |  |  |  | Custom time column 17. |
| FILTER_TIME_18 | TIMESTAMP |  |  |  | Custom time column 18. |
| FILTER_TIME_19 | TIMESTAMP |  |  |  | Custom time column 19. |
| FILTER_TIME_20 | TIMESTAMP |  |  |  | Custom time column 20. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_RAG_DOC_CHUNK_MDATA_PK | Unique | FAI_RAG_DOC_CHUNK_METADATA_PK | CHUNK_METADATA_ID |
| FAI_RAG_DOC_CHUNK_MDATA_UK1 | Unique | FAI_RAG_DOC_CHUNK_METADATA_T1 | CHUNK_ID, USE_CASE_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
