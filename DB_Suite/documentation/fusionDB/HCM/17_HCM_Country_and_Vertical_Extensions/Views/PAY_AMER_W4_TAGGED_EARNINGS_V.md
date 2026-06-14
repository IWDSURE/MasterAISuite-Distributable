# PAY_AMER_W4_TAGGED_EARNINGS_V

## Details

**Schema:** FUSION

**Object owner:** HRX

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payamerw4taggedearningsv-5125.html#payamerw4taggedearningsv-5125](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payamerw4taggedearningsv-5125.html#payamerw4taggedearningsv-5125)

## Columns

- STATE
- DIR_CARD_COMP_ID

## Query

```sql
SELECT DISTINCT hzg.geography_name State,rep.dir_card_comp_id /*tagged earnings*/ FROM pay_entry_usages peu , PAY_REL_GROUPS_DN pa , PAY_REL_GROUPS_f paaf , pay_element_entry_values_f peiv, pay_element_entries_f pee , pay_input_values_f piv , pay_element_types_f pet , pay_ele_classifications pec , hz_geographies hzg , hz_geography_identifiers hzgi , pay_dir_rep_card_usages_f prepu, pay_dir_rep_cards_f rep /* ,pay_dir_card_comp_defs_f sc, pay_dir_card_components_f tc*/ WHERE /* rep.dir_card_comp_id =100000042961022 AND*/ prepu.dir_rep_card_id =rep.dir_rep_card_id AND pa.parent_rel_group_id =prepu.relationship_group_id AND peu.payroll_term_id =pa.parent_rel_group_id AND paaf.relationship_group_id= pa.relationship_group_id AND prepu.effective_start_date BETWEEN paaf.effective_start_date AND paaf.effective_end_date AND peiv.element_entry_id= peu.element_entry_id AND pee.element_entry_id = peu.element_entry_id AND prepu.effective_start_date BETWEEN pee.effective_start_date AND pee.effective_end_date AND piv.element_type_id =pee.element_type_id AND piv.base_name = 'State' AND piv.input_value_id = peiv.input_value_id AND pet.element_type_id =pee.element_type_id AND pet.classification_id =pec.classification_id AND pec.base_classification_name IN ('Standard Earnings', 'Supplemental Earnings') AND hzg.geography_id = hzgi.geography_id AND hzg.geography_use ='MASTER_REF' AND hzg.country_code ='US' AND hzgi.identifier_subtype ='GEO_CODE' AND hzgi.geography_type ='STATE' AND hzgi.identifier_value =CONCAT(peiv.screen_entry_value,'-0-0') /*and rep.dir_card_comp_id=tc.dir_card_comp_id and sc.base_component_name like 'US_WTH_TAXATION' and tc.dir_card_comp_def_id= tc.dir_card_comp_def_id;*/
```

---

[← Back to Index](../17_HCM_Country_and_Vertical_Extensions_Views_Index.md)
