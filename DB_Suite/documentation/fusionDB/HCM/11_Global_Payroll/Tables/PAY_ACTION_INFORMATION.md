# PAY_ACTION_INFORMATION

Table for Payroll Action Information

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactioninformation-4349.html#payactioninformation-4349](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactioninformation-4349.html#payactioninformation-4349)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ACTION_INFORMATION_PK | ACTION_INFORMATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_INFORMATION_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| ACTION_INFORMATION_CATEGORY | VARCHAR2 | 80 |  | Yes | Developer descriptive flexfield column. |
| ACTION_CONTEXT_TYPE | VARCHAR2 | 15 |  | Yes | Type of context archived in table. |
| ACTION_CONTEXT_ID | NUMBER |  | 18 | Yes | Foreign key  to PAY_ACTION_CONTEXTS. |
| PAYROLL_ACTION_ID | NUMBER |  | 18 |  | PAYROLL_ACTION_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| EFFECTIVE_DATE | DATE |  |  |  | Effective date of the record. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment ID for which this action is archived |
| JURISDICTION_CODE | VARCHAR2 | 15 |  |  | Archived context information |
| GROUP_LABEL_ID | NUMBER |  | 18 |  | GROUP_LABEL_ID |
| REPORT_RECORD_ID | NUMBER |  | 18 |  | REPORT_RECORD_ID |
| PARENT_ACT_INFO_ID | NUMBER |  | 18 |  | PARENT_ACT_INFO_ID |
| EXPIRE_ID | NUMBER |  | 8 |  | EXPIRE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ACTION_INFORMATION1 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION2 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION3 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION4 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION5 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION6 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION7 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION8 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION9 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION10 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION11 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION12 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION13 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION14 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION15 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION16 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION17 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION18 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION19 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION20 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION21 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION22 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION23 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION24 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION25 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION26 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION27 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION28 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION29 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION30 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION31 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION32 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION33 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION34 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION35 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION36 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION37 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION38 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION39 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION40 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION41 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION42 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION43 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION44 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION45 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION46 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION47 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION48 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION49 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION50 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION51 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION52 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION53 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION54 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION55 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION56 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION57 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION58 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION59 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION60 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION61 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION62 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION63 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION64 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION65 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION66 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION67 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION68 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION69 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION70 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION71 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION72 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION73 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION74 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION75 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION76 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION77 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION78 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION79 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION80 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION81 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION82 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION83 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION84 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION85 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION86 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION87 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION88 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION89 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION90 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION91 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION92 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION93 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION94 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION95 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION96 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION97 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION98 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION99 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION100 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION101 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION102 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION103 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION104 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION105 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION106 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION107 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION108 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION109 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION110 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION111 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION112 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION113 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION114 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION115 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION116 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION117 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION118 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION119 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION120 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION121 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION122 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION123 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION124 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION125 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION126 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION127 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION128 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION129 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION130 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION131 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION132 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION133 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION134 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION135 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION136 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION137 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION138 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION139 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION140 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION141 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION142 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION143 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION144 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION145 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION146 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION147 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION148 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION149 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION150 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION151 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION152 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION153 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION154 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION155 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION156 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION157 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION158 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION159 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION160 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION161 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION162 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION163 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION164 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION165 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION166 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION167 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION168 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION169 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION170 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION171 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION172 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION173 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION174 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION175 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION176 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION177 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION178 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION179 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION180 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION181 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION182 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION183 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION184 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION185 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION186 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION187 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION188 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION189 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION190 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION191 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION192 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION193 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION194 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION195 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION196 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION197 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION198 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION199 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION200 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION201 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION202 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION203 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION204 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION205 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION206 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION207 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION208 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION209 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION210 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION211 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION212 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION213 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION214 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION215 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION216 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION217 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION218 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION219 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION220 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION221 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION222 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION223 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION224 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION225 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION226 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION227 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION228 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION229 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION230 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION231 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION232 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION233 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION234 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION235 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION236 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION237 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION238 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION239 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION240 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION241 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION242 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION243 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION244 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION245 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION246 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION247 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION248 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION249 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION250 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION251 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION252 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION253 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION254 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION255 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION256 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION257 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION258 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION259 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION260 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION261 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION262 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION263 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION264 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION265 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION266 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION267 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION268 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION269 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION270 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION271 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION272 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION273 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION274 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION275 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION276 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION277 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION278 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION279 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION280 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION281 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION282 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION283 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION284 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION285 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION286 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION287 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION288 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION289 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION290 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION291 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION292 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION293 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION294 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION295 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION296 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION297 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION298 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION299 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ACTION_INFORMATION300 | VARCHAR2 | 240 |  |  | Developer descriptive flexfield column. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ACTION_INFORMATION_N1 | Non Unique | Default | ACTION_CONTEXT_ID, ACTION_CONTEXT_TYPE, PARENT_ACT_INFO_ID |
| PAY_ACTION_INFORMATION_N2 | Non Unique | Default | REPORT_RECORD_ID, GROUP_LABEL_ID |
| PAY_ACTION_INFORMATION_N3 | Non Unique | Default | REPORT_RECORD_ID, ACTION_CONTEXT_ID, ACTION_CONTEXT_TYPE |
| PAY_ACTION_INFORMATION_N4 | Non Unique | Default | GROUP_LABEL_ID |
| PAY_ACTION_INFORMATION_N5 | Non Unique | Default | PARENT_ACT_INFO_ID |
| PAY_ACTION_INFORMATION_N6 | Non Unique | Default | ACTION_CONTEXT_ID, ACTION_CONTEXT_TYPE, ACTION_INFORMATION_CATEGORY, ACTION_INFORMATION5 |
| PAY_ACTION_INFORMATION_N7 | Non Unique | Default | PAYROLL_ACTION_ID |
| PAY_ACTION_INFORMATION_N8 | Non Unique | Default | REPORT_RECORD_ID, PERSON_ID |
| PAY_ACTION_INFORMATION_PK | Unique | Default | ACTION_INFORMATION_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
