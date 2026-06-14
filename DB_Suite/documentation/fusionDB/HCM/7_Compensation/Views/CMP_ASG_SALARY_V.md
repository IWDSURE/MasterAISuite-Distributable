# CMP_ASG_SALARY_V

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpasgsalaryv-3894.html#cmpasgsalaryv-3894](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpasgsalaryv-3894.html#cmpasgsalaryv-3894)

## Columns

- SALARY_ID
- ASSIGNMENT_ID
- ELEMENT_ENTRY_ID
- PERSON_ID
- DATE_FROM
- DATE_TO
- NEXT_SAL_REVIEW_DATE
- SALARY_AMOUNT
- ELEMENT_TYPE_ID
- FTE_VALUE
- ADJUSTED_FTE
- LAST_CHANGE_AMOUNT
- LAST_CHANGE_PERCENT
- ANNUAL_SALARY
- ANNUAL_FT_SALARY
- CURRENCY_CODE
- SALARY_FREQUENCY
- QUINTILE
- QUARTILE
- COMPARATIO
- RANGE_POSITION
- GRADE_MIN
- GRADE_MID
- GRADE_MAX
- ZONE_NAME
- ZONE_TYPE_NAME
- ZONE_ID
- ZONE_TYPE_ID
- DIFFERENTIAL_FACTOR
- DIFFERENTIAL_GRADE_RATE_ID
- DIFF_GRADE_MIN_LIMIT
- PAYROLL_FREQUENCY_CODE
- PAYROLL_ANNUAL_FACTOR
- SALARY_BASIS_CODE
- SALARY_BASIS_ID
- SALARY_BASIS_NAME
- GRADE_RATE_ID
- ACTION_ID
- ACTION_NAME
- ACTION_REASON_ID
- ACTION_REASON
- JOB_ID
- WORK_AT_HOME
- LOCATION_ID
- BUSINESS_UNIT_ID
- GRADE_ID
- GRADE_CODE
- GRADE_NAME
- ASSIGMENT_START_DATE
- ASSIGMENT_END_DATE
- ASSIGNMENT_NUMBER
- RANGE_DIFF_ID
- SALARY_AMOUNT_SCALE
- LAST_UPDATED_BY
- CREATION_DATE
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER
- BUSINESS_GROUP_ID

## Query

```sql
SELECT psa.salary_id, psa.assignment_id, psa.element_entry_id, asg.person_id, psa.date_from, psa.date_to, psa.next_sal_review_date, psa.salary_amount, psa.element_type_id, cmp_ff_dbi_pkg.get_fte_value(psa.assignment_id,decode(psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from) ,psa.date_to)) fte_value, asg.adjusted_fte, cmp_ff_dbi_pkg.get_salary_adjustment_amount(psa.SALARY_ID,psa.DATE_FROM) last_change_Amount, cmp_salary_entry_api.get_salary_chg_percent(psa.salary_id,psa.date_from) last_change_percent, cmp_salary_entry_api.get_annualized_salary(psa.assignment_id, psa.date_from, 0) annual_salary, cmp_salary_entry_api.get_annualized_ft_salary(psa.assignment_id, psa.date_from, 0) annual_ft_salary, psa.currency_code, psa.salary_frequency, cmp_ff_dbi_pkg.get_quintile(asg.grade_id,psa.salary_id, psa.assignment_id,decode (psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from) ,psa.date_to),psa.fte_value) as quintile, cmp_ff_dbi_pkg.get_quartile(asg.grade_id,psa.salary_id, psa.assignment_id,decode (psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from) ,psa.date_to),psa.fte_value) as quartile, cmp_ff_dbi_pkg.get_comparatio(asg.grade_id,psa.salary_id, psa.assignment_id,decode (psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from) ,psa.date_to),psa.fte_value) as comparatio, cmp_ff_dbi_pkg.get_range_position(asg.grade_id,psa.salary_id, psa.assignment_id,decode (psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from) ,psa.date_to),psa.fte_value) as range_position, cmp_ff_dbi_pkg.get_grade_min(asg.grade_id,psa.salary_id, psa.assignment_id,decode (psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from) ,psa.date_to),psa.fte_value) as grade_min, cmp_ff_dbi_pkg.get_grade_mid(asg.grade_id,psa.salary_id, psa.assignment_id,decode (psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from) ,psa.date_to),psa.fte_value) as grade_mid, cmp_ff_dbi_pkg.get_grade_max(asg.grade_id,psa.salary_id, psa.assignment_id,decode (psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from) ,psa.date_to),psa.fte_value) as grade_max, cmp_ff_dbi_pkg.get_zone_name(psa.assignment_id, decode (psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from) ,psa.date_to), psa.range_diff_id) as zone_name, cmp_ff_dbi_pkg.get_zone_type_name(psa.assignment_id, decode (psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from) ,psa.date_to), psa.range_diff_id ) as zone_type_name, cmp_ff_dbi_pkg.get_zone_id(psa.assignment_id, decode (psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from) ,psa.date_to), psa.range_diff_id) as zone_id, cmp_ff_dbi_pkg.get_zone_type_id(psa.assignment_id, decode (psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from) ,psa.date_to), psa.range_diff_id ) as zone_type_id, cmp_ff_dbi_pkg.get_range_differential_factor(psa.SALARY_ID,greatest(psa.date_from,least(trunc(sysdate),psa.date_to))) differential_factor, cmp_ff_dbi_pkg.get_diff_grade_rate_id (psa.assignment_id, psa.salary_id, psa.salary_basis_id, decode (psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from) ,psa.date_to)) differential_grade_rate_id, cmp_ff_dbi_pkg.get_grade_rate_min_sal_limit (psa.assignment_id, psa.salary_id, psa.salary_basis_id, decode (psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from) ,psa.date_to)) diff_grade_min_limit, decode(psa.salary_basis_code,'PERIOD',upper(cmp_ff_dbi_pkg.get_payroll_freq_code(psa.ASSIGNMENT_ID, greatest(psa.date_from,least(trunc(sysdate),psa.date_to))))) payroll_frequency_code, decode(psa.salary_basis_code,'PERIOD',upper(cmp_ff_dbi_pkg.get_payroll_factor( psa.ASSIGNMENT_ID, psa.SALARY_BASIS_ID,greatest(psa.date_from,least(trunc(sysdate),psa.date_to))))) payroll_annual_factor, psa.salary_basis_code, psa.salary_basis_id, psa.display_name as salary_basis_name, psa.grade_rate_id, psa.action_id, psa.action_name, psa.action_reason_id, psa.action_reason, asg.job_id, psa.WORK_AT_HOME, asg.location_id, asg.business_unit_id, asg.grade_id, asg.grade_code, asg.grade_name, asg.assigment_start_date, asg.assigment_end_date, asg.assignment_number, psa.range_diff_id, psa.salary_amount_scale, psa.last_updated_by, psa.creation_date, psa.last_update_date, psa.last_update_login, psa.object_version_number, psa.business_group_id FROM (SELECT csa.salary_id, csa.element_entry_id, csa.assignment_id, csa.date_from, csa.date_to, csa.next_sal_review_date, csa.salary_amount, csb.element_type_id, csa.WORK_AT_HOME, NVL (fte.value, 1) fte_value, ele.input_currency_code as currency_code, csb.salary_basis_code, hlk.meaning as salary_frequency, csb.grade_rate_id, csa.action_id, act.action_name, csa.action_reason_id, rea.action_reason, csb.range_diff_id, NVL(csb.amount_decimal_precision,2) AS salary_amount_scale, csa.created_by, csa.last_updated_by, csa.creation_date, csa.last_update_date, csa.last_update_login, csa.object_version_number, csb.salary_basis_name as display_name, csb.salary_basis_id, csb.business_group_id FROM cmp_salary csa, cmp_salary_bases_vl csb, pay_element_types_vl ele, hcm_lookups hlk, per_assign_work_measures_f fte, per_actions_vl act, per_action_reasons_vl rea WHERE csa.salary_basis_id = csb.salary_basis_id AND act.action_id (+) = csa.action_id AND rea.action_reason_id (+) = csa.action_reason_id AND csa.business_group_id = csb.business_group_id AND hlk.lookup_code = csb.salary_basis_code AND hlk.lookup_type = 'CMP_SALARY_BASIS' AND csb.element_type_id = ele.element_type_id AND csa.date_from BETWEEN ele.effective_start_date AND ele.effective_end_date AND fte.assignment_id (+) = csa.assignment_id AND fte.unit(+) = 'FTE' AND decode (csa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),csa.date_from),csa.date_to) BETWEEN fte.effective_start_date(+) AND fte.effective_end_date(+) ) psa, (SELECT asg.assignment_id, asg.person_id, asg.job_id, asg.location_id, asg.business_unit_id, grd.grade_id, grd.grade_code, grd.name AS grade_name, asg.assignment_number, asg.effective_start_date AS assigment_start_date, asg.effective_end_date AS assigment_end_date, asg.adjusted_fte FROM per_all_assignments_m asg, per_grades_f_vl grd WHERE asg.effective_latest_change = 'Y' AND grd.grade_id (+) = asg.grade_id AND asg.effective_start_date BETWEEN grd.effective_start_date(+) AND grd.effective_end_date(+) ) asg, per_rate_values_f prv WHERE psa.assignment_id = asg.assignment_id AND asg.grade_id = prv.rate_object_id(+) AND psa.grade_rate_id = prv.rate_id(+) AND decode (psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from),psa.date_to) BETWEEN asg.assigment_start_date AND asg.assigment_end_date AND decode (psa.date_to,to_date('31/12/4712','DD/MM/YYYY'),greatest(trunc(sysdate),psa.date_from),psa.date_to) BETWEEN prv.effective_start_date(+) AND prv.effective_end_date(+)
```

---

[← Back to Index](../7_Compensation_Views_Index.md)
