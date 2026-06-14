# PAY_DOR_FILES_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydorfilesvl-3115.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydorfilesvl-3115.html)

## Columns

- ATTACHMENTENTITYNAME
- CONTEXT
- DOCUMENTS_OF_RECORD_ID
- PAYROLL_RELATIONSHIP_ID
- PERSON_ID
- DISPLAY_CHAR_VALUE1
- DISPLAY_CHAR_VALUE2
- DISPLAY_CHAR_VALUE3
- DISPLAY_DATE_VALUE1
- DISPLAY_DATE_VALUE2
- DISPLAY_DATE_VALUE3
- DISPLAY_NUM_VALUE1
- DISPLAY_NUM_VALUE2
- DISPLAY_NUM_VALUE3
- USER_TYPE
- PUBLISH_DATE
- CREATION_DATE

## Query

```sql
select distinct ('HR_DOCUMENTS_OF_RECORD') AS AttachmentEntityName, Context, DOCUMENTS_OF_RECORD_ID, PAYROLL_RELATIONSHIP_ID, PERSON_ID, Display_Char_Value1, Display_Char_Value2, Display_Char_Value3, NVL(Display_Date_Value1,Display_Date_Value2) AS Display_Date_Value1, NVL(Display_Date_Value2,SYSDATE) AS Display_Date_Value2, NVL(Display_Date_Value3,SYSDATE) Display_Date_Value3, Display_Num_Value1, Display_Num_Value2, Display_Num_Value3, User_Type, Publish_Date, CREATION_DATE from ( SELECT 'YED' Context, hdr.documents_of_record_id DOCUMENTS_OF_RECORD_ID , NULL payroll_relationship_id, hdr.person_id PERSON_ID , to_char(hdr.dei_information_number1) Display_Char_Value1, hdt.system_document_type Display_Char_Value2, (Select EstablishmentPEO.NAME From XLE_ETB_PROFILES EstablishmentPEO, XLE_REGISTRATIONS RegistrationPEO, XLE_JURISDICTIONS_VL JurisdictionPEO, XLE_LOOKUPS XleLookupPEO, XLE_ENTITY_PROFILES LegalEntityPEO, HZ_GEOGRAPHIES GeographyPEO, HR_ALL_ORGANIZATION_UNITS_F_VL OrganizationUnitDPEOEstab, HR_ALL_ORGANIZATION_UNITS_F_VL OrganizationUnitDPEOPsu, HR_ORG_DETAILS_BY_CLASS_V OrganizationDetailDPEO, HR_ORG_UNIT_CLASSIFICATIONS_F OrgUnitClassificationDPEO Where EstablishmentPEO.ESTABLISHMENT_ID = OrganizationUnitDPEOEstab.ESTABLISHMENT_ID AND TRUNC(SYSDATE) BETWEEN OrganizationUnitDPEOEstab.EFFECTIVE_START_DATE AND OrganizationUnitDPEOEstab.EFFECTIVE_END_DATE AND EstablishmentPEO.GEOGRAPHY_ID = GeographyPEO.GEOGRAPHY_ID AND RegistrationPEO.SOURCE_TABLE (+) = 'XLE_ETB_PROFILES' AND EstablishmentPEO.ESTABLISHMENT_ID = RegistrationPEO.SOURCE_ID (+) AND RegistrationPEO.IDENTIFYING_FLAG (+) = 'Y' AND RegistrationPEO.JURISDICTION_ID = JurisdictionPEO.JURISDICTION_ID (+) AND XleLookupPEO.LOOKUP_TYPE (+) = 'XLE_REG_CODE_EST' AND XleLookupPEO.LOOKUP_CODE (+) = JurisdictionPEO.REGISTRATION_CODE_ETB AND LegalEntityPEO.LEGAL_ENTITY_ID =EstablishmentPEO.LEGAL_ENTITY_ID AND OrganizationUnitDPEOPsu.LEGAL_ENTITY_ID = NVL(LegalEntityPEO.PARENT_PSU_ID,LegalEntityPEO.LEGAL_ENTITY_ID) AND TRUNC(SYSDATE) BETWEEN OrganizationUnitDPEOPsu.EFFECTIVE_START_DATE AND OrganizationUnitDPEOPsu.EFFECTIVE_END_DATE AND OrganizationUnitDPEOPsu.ORGANIZATION_ID = OrganizationDetailDPEO.ORGANIZATION_ID AND OrganizationDetailDPEO.CLASSIFICATION_CODE = 'HCM_PSU' AND OrganizationDetailDPEO.ORG_INFORMATION_CONTEXT ='PER_PSU_PAYROLL_INFO' AND TRUNC(SYSDATE) BETWEEN OrganizationDetailDPEO.EFFECTIVE_START_DATE AND OrganizationDetailDPEO.EFFECTIVE_END_DATE AND OrganizationUnitDPEOEstab.ORGANIZATION_ID = OrgUnitClassificationDPEO.ORGANIZATION_ID AND TRUNC(SYSDATE) BETWEEN OrgUnitClassificationDPEO.EFFECTIVE_START_DATE AND OrgUnitClassificationDPEO.EFFECTIVE_END_DATE AND OrgUnitClassificationDPEO.CLASSIFICATION_CODE = 'HCM_TRU' AND OrganizationUnitDPEOEstab.ORGANIZATION_ID=hdr.dei_information_number4) Display_Char_Value3 , hdr.DATE_TO Display_Date_Value1, null Display_Date_Value2, null Display_Date_Value3, null Display_Num_Value1, null Display_Num_Value2, null Display_Num_Value3, hdr.CREATION_DATE, 'EMP' User_Type, to_date(nvl(hdr.publish_date,SYSDATE)) as publish_date FROM hr_document_types_vl hdt , hr_documents_of_record hdr WHERE hdt.category_code IN ('PAYROLL','BENEF') AND hdt.sub_category_code IN ('PAYROLL_TAX','BENEF_ENRL_CHNG_TERMIN') AND hdt.system_document_type in (SELECT * FROM TABLE(CAST(PAY_STATISTICS_UTILITY_PKG.in_varchar_list(pay_core_utils.get_legislation_rule(hdt.LEGISLATION_CODE,'#YEAR_END_TAX_FORM')) as pay_number_varchar_t))) AND hdr.document_type_id = hdt.document_type_id AND (hdr.dei_information_category is null OR hdr.dei_information_category = hdt.system_document_type) union SELECT 'PAYSLIP' Context, hdr.documents_of_record_id , prd.payroll_relationship_id payroll_relationship_id , hdr.person_id PERSON_ID , decode(nvl(fnd_profile.value('ORA_PAY_PAYSLIP_DISPLAY_NET_PAY_BALANCE_CURRENCY'),'N'),'N', nvl((select MAX(OPM.CURRENCY_CODE) from PAY_PERSONAL_PAYMENT_METHODS_F ppm , PAY_ORG_PAY_METHODS_F opm where ppm.ORG_PAYMENT_METHOD_ID=opm.ORG_PAYMENT_METHOD_ID and ppm.PAYROLL_RELATIONSHIP_ID=PRD.PAYROLL_RELATIONSHIP_ID AND hdr.issued_date BETWEEN OPM.EFFECTIVE_START_DATE AND OPM.EFFECTIVE_END_DATE),ldg.default_currency_code),ldg.default_currency_code) Display_Char_Value1, null Display_Char_Value2, null Display_Char_Value3, nvl(hdr.issued_date,hdr.dei_information_date2) Display_Date_Value1, hdr.date_from Display_Date_Value2, hdr.date_to Display_Date_Value3, hdr.dei_information_number3 Display_Num_Value1, null Display_Num_Value2, null Display_Num_Value3, hdr.CREATION_DATE, decode(PAY_FLOW_COMMON_UTIL_PKG.check_security(hdr.PERSON_ID,'PER_ALL_PEOPLE_F','PERSON_ID','PAY_ACCESS_WORKER_PAYSLIP_DATA'),'N','EMP','ADMIN') User_Type, nvl(hdr.dei_information_date1,hdr.issued_date) as publish_date FROM hr_document_types_vl hdt , hr_documents_of_record hdr , pay_payroll_rel_actions pra , pay_pay_relationships_dn prd, per_legislative_data_groups ldg WHERE hdt.system_document_type = 'GLB_PAYSLIP' AND hdt.category_code = 'PAYROLL' AND hdt.sub_category_code = 'PAYROLL_PAYMENT' AND hdr.document_type_id = hdt.document_type_id and ldg.legislative_data_group_id = prd.legislative_data_group_id AND prd.PERSON_ID = hdr.person_id AND pra.payroll_rel_action_id = hdr.related_object_id AND prd.payroll_relationship_id = pra.payroll_relationship_id union SELECT 'PAYSLIP' Context, hdr.documents_of_record_id , hpir.PAYROLL_RELATIONSHIP_ID , hdr.person_id PERSON_ID , decode(nvl(fnd_profile.value('ORA_PAY_PAYSLIP_DISPLAY_NET_PAY_BALANCE_CURRENCY'),'N'),'N', nvl((select MAX(OPM.CURRENCY_CODE) from PAY_PERSONAL_PAYMENT_METHODS_F ppm , PAY_ORG_PAY_METHODS_F opm where ppm.ORG_PAYMENT_METHOD_ID=opm.ORG_PAYMENT_METHOD_ID and ppm.PAYROLL_RELATIONSHIP_ID=hpir.PAYROLL_RELATIONSHIP_ID AND hdr.issued_date BETWEEN OPM.EFFECTIVE_START_DATE AND OPM.EFFECTIVE_END_DATE),ldg.default_currency_code),ldg.default_currency_code) Display_Char_Value1, null Display_Char_Value2, null Display_Char_Value3, nvl(hdr.issued_date,hdr.dei_information_date2) Display_Date_Value1, hdr.date_from Display_Date_Value2, hdr.date_to Display_Date_Value3, hpiri.IRI_INFORMATION_NUMBER2 Display_Num_Value1, null Display_Num_Value2, null Display_Num_Value3, hdr.CREATION_DATE, decode(PAY_FLOW_COMMON_UTIL_PKG.check_security(hdr.person_id,'PER_ALL_PEOPLE_F','PERSON_ID','PAY_ACCESS_WORKER_PAYSLIP_DATA'),'N','EMP','ADMIN') User_Type, nvl(hpiri.IRI_INFORMATION_DATE1,hdr.issued_date) as publish_date FROM fusion.hr_document_types_vl hdt , fusion.hr_documents_of_record hdr , fusion.HRY_PI_INBD_RECORDS hpir , fusion.hry_pi_inbd_record_information hpiri, pay_pay_relationships_dn pprd, per_legislative_data_groups ldg WHERE hdt.system_document_type = 'GLB_THIRD_PARTY_PAYSLIP' AND hdt.category_code = 'PAYROLL' AND hdr.document_type_id = hdt.document_type_id and ldg.legislative_data_group_id = pprd.legislative_data_group_id AND hpir.inbd_record_id = hpiri.INBD_RECORD_ID(+) AND hpir.documents_of_record_id(+) = hdr.DOCUMENTS_OF_RECORD_ID and nvl(hpir.record_type,'ORA_HRY_PAYSLIP_DOR') = 'ORA_HRY_PAYSLIP_DOR' and nvl(hpiri.IRI_INFORMATION_CONTEXT,'ORA_HRY_THIRD_PARTY_PAYSLIP') = 'ORA_HRY_THIRD_PARTY_PAYSLIP' and pprd.payroll_relationship_id(+) =hpir.PAYROLL_RELATIONSHIP_ID ) order by DISPLAY_DATE_VALUE1 desc, CREATION_DATE desc
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
