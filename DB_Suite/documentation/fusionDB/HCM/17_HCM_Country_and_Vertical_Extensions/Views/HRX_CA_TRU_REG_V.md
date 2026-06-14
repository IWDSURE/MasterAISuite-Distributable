# HRX_CA_TRU_REG_V

## Details

**Schema:** FUSION

**Object owner:** HRX

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrxcatruregv-8848.html#hrxcatruregv-8848](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrxcatruregv-8848.html#hrxcatruregv-8848)

## Columns

- ORGANIZATION_ID
- ESTABLISHMENT_ID
- ESTAB_NAME
- REGISTRATION_NUMBER
- TRANSMITTER_NUMBER_TYPE
- EFFECTIVE_FROM
- EFFECTIVE_TO

## Query

```sql
SELECT tru.organization_id, tru.establishment_id, substr(tru.estab_name, 0, 100) estab_name, xle.registration_number, 'REGISTRATION_NUMBER' transmitter_number_type, xle.EFFECTIVE_FROM, xle.EFFECTIVE_TO FROM per_tax_reporting_units tru, xle_registrations xle, xle_jurisdictions_b juri WHERE juri.jurisdiction_code = 'Canada Federal Tax' AND juri.legislative_cat_code = 'FEDERAL_TAX' AND xle.jurisdiction_id = juri.jurisdiction_id AND xle.source_table = 'XLE_ETB_PROFILES' AND tru.establishment_id = xle.source_id UNION SELECT tru.organization_id, tru.establishment_id, substr(tru.estab_name, 0, 100) estab_name, substr(xle.registration_number, 0, 9) registration_number, 'REGISTRATION_NUMBER' transmitter_number_type, xle.EFFECTIVE_FROM, xle.EFFECTIVE_TO FROM per_tax_reporting_units tru, xle_registrations xle, xle_jurisdictions_b juri WHERE juri.jurisdiction_code = 'Canada Federal Tax' AND juri.legislative_cat_code = 'FEDERAL_TAX' AND xle.jurisdiction_id = juri.jurisdiction_id AND xle.source_table = 'XLE_ETB_PROFILES' AND tru.establishment_id = xle.source_id UNION SELECT organization_id, 1 establishment_id, org_information3 estab_name, org_information4 registration_number, org_information_context transmitter_number_type, EFFECTIVE_START_DATE EFFECTIVE_FROM, EFFECTIVE_END_DATE EFFECTIVE_TO FROM hr_organization_information_f WHERE org_information_context IN ( 'HRX_CA_TRU_T4_RULES', 'HRX_CA_TRU_T4A_RULES' ) AND org_information1 = 'Y' AND org_information3 IS NOT NULL AND org_information4 IS NOT NULL
```

---

[← Back to Index](../17_HCM_Country_and_Vertical_Extensions_Views_Index.md)
