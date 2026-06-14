# PAY_YEAR_END_DOCS_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payyearenddocsvl-5767.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payyearenddocsvl-5767.html)

## Columns

- DOCUMENTS_OF_RECORD_ID
- PERSON_ID
- PERIOD_NAME
- DOCUMENT_NAME
- SYSTEM_DOCUMENT_TYPE
- TAX_REPORTING_UNIT
- DATE_FROM
- DATE_TO
- CREATION_DATE
- PUBLISH_DATE
- REL_ACTION_ID
- ATTACHMENT_ENTITY_NAME

## Query

```sql
SELECT hdr.documents_of_record_id DOCUMENTS_OF_RECORD_ID , hdr.person_id PERSON_ID , to_char(hdr.dei_information_number1) Period_Name, hdr.document_name DOCUMENT_NAME, hdt.system_document_type system_document_type, (Select EstablishmentPEO.NAME From XLE_ETB_PROFILES EstablishmentPEO, XLE_REGISTRATIONS RegistrationPEO, XLE_JURISDICTIONS_VL JurisdictionPEO, XLE_LOOKUPS XleLookupPEO, XLE_ENTITY_PROFILES LegalEntityPEO, HZ_GEOGRAPHIES GeographyPEO, HR_ALL_ORGANIZATION_UNITS_F_VL OrganizationUnitDPEOEstab, HR_ALL_ORGANIZATION_UNITS_F_VL OrganizationUnitDPEOPsu, HR_ORG_DETAILS_BY_CLASS_V OrganizationDetailDPEO, HR_ORG_UNIT_CLASSIFICATIONS_F OrgUnitClassificationDPEO Where EstablishmentPEO.ESTABLISHMENT_ID = OrganizationUnitDPEOEstab.ESTABLISHMENT_ID AND TRUNC(SYSDATE) BETWEEN OrganizationUnitDPEOEstab.EFFECTIVE_START_DATE AND OrganizationUnitDPEOEstab.EFFECTIVE_END_DATE AND EstablishmentPEO.GEOGRAPHY_ID = GeographyPEO.GEOGRAPHY_ID AND RegistrationPEO.SOURCE_TABLE (+) = 'XLE_ETB_PROFILES' AND EstablishmentPEO.ESTABLISHMENT_ID = RegistrationPEO.SOURCE_ID (+) AND RegistrationPEO.IDENTIFYING_FLAG (+) = 'Y' AND RegistrationPEO.JURISDICTION_ID = JurisdictionPEO.JURISDICTION_ID (+) AND XleLookupPEO.LOOKUP_TYPE (+) = 'XLE_REG_CODE_EST' AND XleLookupPEO.LOOKUP_CODE (+) = JurisdictionPEO.REGISTRATION_CODE_ETB AND LegalEntityPEO.LEGAL_ENTITY_ID =EstablishmentPEO.LEGAL_ENTITY_ID AND OrganizationUnitDPEOPsu.LEGAL_ENTITY_ID = NVL(LegalEntityPEO.PARENT_PSU_ID,LegalEntityPEO.LEGAL_ENTITY_ID) AND TRUNC(SYSDATE) BETWEEN OrganizationUnitDPEOPsu.EFFECTIVE_START_DATE AND OrganizationUnitDPEOPsu.EFFECTIVE_END_DATE AND OrganizationUnitDPEOPsu.ORGANIZATION_ID = OrganizationDetailDPEO.ORGANIZATION_ID AND OrganizationDetailDPEO.CLASSIFICATION_CODE = 'HCM_PSU' AND OrganizationDetailDPEO.ORG_INFORMATION_CONTEXT ='PER_PSU_PAYROLL_INFO' AND TRUNC(SYSDATE) BETWEEN OrganizationDetailDPEO.EFFECTIVE_START_DATE AND OrganizationDetailDPEO.EFFECTIVE_END_DATE AND OrganizationUnitDPEOEstab.ORGANIZATION_ID = OrgUnitClassificationDPEO.ORGANIZATION_ID AND TRUNC(SYSDATE) BETWEEN OrgUnitClassificationDPEO.EFFECTIVE_START_DATE AND OrgUnitClassificationDPEO.EFFECTIVE_END_DATE AND OrgUnitClassificationDPEO.CLASSIFICATION_CODE = 'HCM_TRU' AND OrganizationUnitDPEOEstab.ORGANIZATION_ID=hdr.dei_information_number4) TAX_REPORTING_UNIT , hdr.DATE_FROM, hdr.DATE_TO, hdr.CREATION_DATE, to_date(nvl(hdr.publish_date,SYSDATE)) as publish_date, hdr.related_object_id REL_ACTION_ID, 'HR_DOCUMENTS_OF_RECORD' Attachment_Entity_Name FROM hr_document_types_vl hdt , hr_documents_of_record hdr WHERE hdt.category_code IN ('PAYROLL','BENEF') AND hdt.sub_category_code IN ('PAYROLL_TAX','BENEF_ENRL_CHNG_TERMIN') AND hdt.system_document_type in (SELECT * FROM TABLE(CAST(PAY_STATISTICS_UTILITY_PKG.in_varchar_list(pay_core_utils.get_legislation_rule(hdt.LEGISLATION_CODE,'#YEAR_END_TAX_FORM')) as pay_number_varchar_t))) AND hdr.document_type_id = hdt.document_type_id AND (hdr.dei_information_category is null OR hdr.dei_information_category = hdt.system_document_type) union select hdr.documents_of_record_id DOCUMENTS_OF_RECORD_ID , hdr.person_id PERSON_ID , null Period_Name, hdr.document_name DOCUMENT_NAME, hdt.system_document_type system_document_type, (select TERRITORY_SHORT_NAME from fnd_territories_vl where TERRITORY_CODE=hdr.ISSUING_COUNTRY ) ISSUING_COUNTRY, hdr.DATE_FROM, hdr.DATE_TO, hdr.CREATION_DATE, nvl(hpiri.IRI_INFORMATION_DATE1,hdr.issued_date) as publish_date, hdr.related_object_id REL_ACTION_ID, 'HR_DOCUMENTS_OF_RECORD' Attachment_Entity_Name from hr_document_types_vl hdt , hr_documents_of_record hdr , HRY_PI_INBD_RECORDS hpir , hry_pi_inbd_record_information hpiri, pay_pay_relationships_dn pprd, per_legislative_data_groups ldg WHERE hdt.system_document_type = 'GLB_THIRD_PARTY_PAYROLL_DOCUMENTS' AND hdt.category_code = 'PAYROLL' AND hdr.document_type_id = hdt.document_type_id and ldg.legislative_data_group_id(+) = pprd.legislative_data_group_id AND hpir.inbd_record_id = hpiri.INBD_RECORD_ID AND hpir.documents_of_record_id = hdr.DOCUMENTS_OF_RECORD_ID and hpir.record_type = 'ORA_HRY_INBD_PAYROLL_DOC' and nvl(hpiri.IRI_INFORMATION_CONTEXT,'ORA_HRY_INBD_PAYROLL_DOC') = 'ORA_HRY_INBD_PAYROLL_DOC' and pprd.payroll_relationship_id(+) =hpir.PAYROLL_RELATIONSHIP_ID and pprd.person_id(+) =hpir.person_id order by DATE_TO desc, CREATION_DATE desc
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
