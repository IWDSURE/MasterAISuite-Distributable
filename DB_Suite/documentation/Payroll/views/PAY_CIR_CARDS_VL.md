# PAY_CIR_CARDS_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycircardsvl-8683.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycircardsvl-8683.html)

## Columns

- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- DIR_CARD_ID
- LEGISLATIVE_DATA_GROUP_NAME
- LEGISLATIVE_DATA_GROUP_ID
- DIR_CARD_DEFINITION_NAME
- DIR_CARD_DEFINITION_ID
- SOURCE_ID
- SOURCE_TYPE
- CARD_SEQUENCE
- LEVEL_CODE
- CARD_LEVEL
- DIR_CARD_DEFINITION_BASE_NAME
- CARD_DISCRIMINATOR

## Query

```sql
select pdcf.effective_start_date, pdcf.effective_end_date, pdcf.dir_card_id, pldgv.name legislative_data_group_name, pldgv.legislative_data_group_id, pdcdv.display_name dir_card_definition_name, pdcf.dir_card_definition_id, pdcf.source_id, pdcf.source_type, pdcf.card_sequence, pdclf.LEVEL_CODE, decode(pdclf.LEVEL_CODE,'HCM_TRU','TRU','HCM_PSU','PSU',pdclf.LEVEL_CODE) card_level, pdcdv.base_display_name dir_card_definition_base_name, pldgv.legislation_code||'_'||pdcdv.base_display_name card_discriminator from pay_dir_cards_f pdcf, pay_dir_card_definitions_vl pdcdv, PAY_DIR_CARD_LEVELS_F pdclf, per_legislative_data_groups_vl pldgv where pdcdv.dir_card_definition_id=pdcf.dir_card_definition_id and pldgv.legislative_data_group_id=pdcf.legislative_data_group_id AND pdclf.LEVEL_CODE=pdcf.SOURCE_TYPE AND pdclf.DIR_CARD_DEFINITION_ID=pdcf.DIR_CARD_DEFINITION_ID AND pdcf.effective_start_date between pdclf.effective_start_date and pdclf.effective_end_date
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
