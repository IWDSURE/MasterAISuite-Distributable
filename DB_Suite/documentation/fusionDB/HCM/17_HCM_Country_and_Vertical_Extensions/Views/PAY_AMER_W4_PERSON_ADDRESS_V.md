# PAY_AMER_W4_PERSON_ADDRESS_V

## Details

**Schema:** FUSION

**Object owner:** HRX

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payamerw4personaddressv-5564.html#payamerw4personaddressv-5564](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payamerw4personaddressv-5564.html#payamerw4personaddressv-5564)

## Columns

- STATE
- DIR_CARD_COMP_ID

## Query

```sql
SELECT DISTINCT paf.region_2 State,rep.dir_card_comp_id /*Person Address*/ FROM per_all_assignments_m hra , PAY_REL_GROUPS_DN pa , PAY_REL_GROUPS_f paaf , PER_PERSON_ADDR_USAGES_F pau , per_addresses_f paf , pay_dir_rep_card_usages_f prepu , pay_dir_rep_cards_f rep /*,pay_dir_card_comp_defs_f sc, pay_dir_card_components_f tc*/ WHERE /*rep.dir_card_comp_id =100000042961022 AND*/ prepu.dir_rep_card_id =rep.dir_rep_card_id AND prepu.relationship_group_id=pa.parent_rel_group_id AND paaf.relationship_group_id = pa.relationship_group_id AND hra.assignment_id =pa.assignment_id AND prepu.effective_start_date BETWEEN paaf.effective_start_date AND paaf.effective_end_date AND prepu.effective_start_date BETWEEN pa.start_date AND pa.end_date AND pau.person_id =hra.person_id AND upper(pau.address_type) IN ( 'US_RESIDENT_TAX_ADDRESS','HOME' ) AND paF.address_id IN (pau.address_id,NVL(hra.tax_address_id,pau.address_id)) /*and rep.dir_card_comp_id=tc.dir_card_comp_id and sc.base_component_name like 'US_WTH_TAXATION' and tc.dir_card_comp_def_id= tc.dir_card_comp_def_id*/
```

---

[← Back to Index](../17_HCM_Country_and_Vertical_Extensions_Views_Index.md)
