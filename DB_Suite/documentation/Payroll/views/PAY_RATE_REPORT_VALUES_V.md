# PAY_RATE_REPORT_VALUES_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payratereportvaluesv-7354.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payratereportvaluesv-7354.html)

## Columns

- BASE_NAME
- PAYROLL_RELATIONSHIP_ID
- PAYROLL_TERM_ID
- PAYROLL_ASSIGNMENT_ID
- RATE_DEFINITION_ID
- START_DATE
- END_DATE
- VALUE
- PERIODICITY
- FTE_FLAG
- CURRENCY
- OVERALL_SALARY_FLAG
- QUARTERLY
- YEARLY
- MONTHLY
- WEEKLY
- DAILY
- HOURLY

## Query

```sql
select prd.base_name, prv.payroll_relationship_id, prv.payroll_term_id, prv.payroll_assignment_id, prv.rate_definition_id, prv.start_date, prv.end_date, prv.value, prv.periodicity, prv.fte_flag, NVL(prv.currency, prd.default_rtn_currency) currency, NVL(prd.OVERALL_SALARY_FLAG, 'N') overall_salary_flag, pay_rates.rate_converter(prv.value, prv.periodicity, 'QUARTER', nvl(ff.formula_name, 'DEFAULT'), prv.start_date, pldg.legislative_data_group_id, prv.enterprise_id, pldg.legislation_code) quarterly, pay_rates.rate_converter(prv.value, prv.periodicity, 'YEAR', nvl(ff.formula_name, 'DEFAULT'), prv.start_date, pldg.legislative_data_group_id, prv.enterprise_id, pldg.legislation_code) yearly, pay_rates.rate_converter(prv.value, prv.periodicity, 'CALENDAR MONTH', nvl(ff.formula_name, 'DEFAULT'), prv.start_date, pldg.legislative_data_group_id, prv.enterprise_id, pldg.legislation_code) monthly, pay_rates.rate_converter(prv.value, prv.periodicity, 'WEEK', nvl(ff.formula_name, 'DEFAULT'), prv.start_date, pldg.legislative_data_group_id, prv.enterprise_id, pldg.legislation_code) weekly, pay_rates.rate_converter(prv.value, prv.periodicity, 'DAILY', nvl(ff.formula_name, 'DEFAULT'), prv.start_date, pldg.legislative_data_group_id, prv.enterprise_id, pldg.legislation_code) daily, pay_rates.rate_converter(prv.value, prv.periodicity, 'HOURLY', nvl(ff.formula_name, 'DEFAULT'), prv.start_date, pldg.legislative_data_group_id, prv.enterprise_id, pldg.legislation_code) hourly from pay_rate_values prv, pay_pay_relationships_dn ppr, per_legislative_data_groups pldg, pay_rate_definitions_f prd, ff_formulas_f ff where prv.payroll_relationship_id = ppr.payroll_relationship_id and prv.rate_definition_id = prd.rate_definition_id and nvl(prd.conversion_formula_id, -99) = ff.formula_id (+) and pldg.legislative_data_group_id = ppr.legislative_data_group_id and prv.start_date between prd.effective_start_date and prd.effective_end_date
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
