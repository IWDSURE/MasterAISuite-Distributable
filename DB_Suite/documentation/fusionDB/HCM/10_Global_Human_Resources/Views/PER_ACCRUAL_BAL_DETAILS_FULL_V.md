# PER_ACCRUAL_BAL_DETAILS_FULL_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraccrualbaldetailsfullv-6622.html#peraccrualbaldetailsfullv-6622](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraccrualbaldetailsfullv-6622.html#peraccrualbaldetailsfullv-6622)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- PAYROLL_ASSIGNMENT_ID
- ACCRUAL_PLAN_ID
- ACCRUAL_CATEGORY
- ACCRUAL_UNITS
- ACCRUAL_TERM_START
- ACCRUAL_TERM_END
- LAST_ACCRUAL_DATE
- ENROLL_START_DATE
- ENROLL_END_DATE
- CONTINUOUS_SERVICE_DATE
- TERM_ACCRUAL_RATE
- MAX_CARRY_OVER
- CEILING_AMT
- ENTITLED_AMT
- ACCRUED_AMT
- CARRY_OVER_AMT
- ABSENCE_AMT
- OTHERS_AMT
- NET_ENTITLED_AMT
- LIABILITY_AMOUNT
- LIABILITY_CURRENCY
- PERIOD_NUM
- ACCRUAL_ELEMENT_TYPE
- PERIOD_START_DATE
- PERIOD_END_DATE
- TRANSACTION_DATE
- CONTRIBUTED_AMT
- BALANCE_INDICATOR
- ELEMENT_TYPE_ID
- INPUT_VALUE_ID
- ABSENCE_TYPE_ID
- STARTING_BALANCE
- CARRYOVER
- ACCRUED
- OTHER_CREDITS
- ABSENCES
- OTHER_DEBITS
- ENDING_BALANCE
- PROJECTED_AMT
- FORFEITED_AMT
- ACCRUAL_BAND_ID
- ABSENCE_REASON_ID
- ABSENCE_ATTENDANCE_ID
- CARRYOVER_EXPIRY_DATE
- INELIGIBILITY_END_DATE

## Query

```sql
SELECT bal_det.person_id ,bal_det.assignment_id ,bal_det.payroll_assignment_id ,bal_det.accrual_plan_id ,bal_det.accrual_category ,bal_det.accrual_units ,bal_det.accrual_start_date accrual_term_start ,bal_det.accrual_end_date accrual_term_end ,bal_period.last_accrual_date ,bal_period.enroll_start_date ,bal_period.enroll_end_date ,bal_period.continuous_service_date ,bal_period.accrual_rate term_accrual_rate ,bal_period.max_carry_over ,bal_period.ceiling ceiling_amt ,bal_period.entitled_amt ,bal_period.accrued_amt ,bal_period.carry_over_amt ,bal_period.absence_amt ,bal_period.others_amt ,bal_period.net_entitled_amt ,bal_period.liability_value liability_amount ,bal_period.currency_code liability_currency ,sum(decode(bal_det.element_type, 'ACR',1,0)) over (partition by bal_det.assignment_id, bal_det.accrual_plan_id, bal_det.accrual_start_date order by bal_det.start_date, bal_det.end_date ) Period_Num ,bal_det.element_type accrual_element_type ,max(decode(bal_det.element_type, 'ACR',bal_det.start_date,null)) over (partition by bal_det.assignment_id, bal_det.accrual_plan_id, bal_det.accrual_start_date order by bal_det.start_date, bal_det.end_date ) period_start_date ,max(decode(bal_det.element_type, 'ACR',bal_det.end_date,null)) over (partition by bal_det.assignment_id, bal_det.accrual_plan_id, bal_det.accrual_start_date order by bal_det.start_date, bal_det.end_date ) period_end_date ,case when bal_det.element_type in('ACR','COV') Then bal_det.period_end_date else bal_det.start_date END transaction_date ,bal_det.contributed_amt ,decode(ROW_NUMBER() OVER (PARTITION BY bal_det.assignment_id, bal_det.accrual_plan_id, bal_det.accrual_start_date, bal_det.start_date order by bal_det.start_date),1,1,0) Balance_Indicator ,bal_det.element_type_id ,bal_det.input_value_id ,decode(bal_det.absence_type_id, 0, null, bal_det.absence_type_id) absence_type_id ,sum(bal_det.contributed_amt) over (partition by bal_det.assignment_id, bal_det.accrual_plan_id, bal_det.accrual_start_date order by bal_det.start_date) - sum(bal_det.contributed_amt) over (partition by bal_det.assignment_id, bal_det.accrual_plan_id, bal_det.accrual_start_date, bal_det.start_date order by bal_det.start_date) Starting_Balance ,decode(bal_det.element_type, 'COV', (bal_det.contributed_amt)) Carryover ,decode(bal_det.element_type, 'ACR', (bal_det.contributed_amt)) Accrued ,decode(bal_det.element_type, 'OTH', decode(sign(bal_det.contributed_amt), 1, bal_det.contributed_amt)) Other_Credits ,decode(bal_det.element_type, 'ABS', (bal_det.contributed_amt)) Absences ,decode(bal_det.element_type, 'OTH', decode(sign(bal_det.contributed_amt), -1, bal_det.contributed_amt)) Other_Debits ,sum(bal_det.contributed_amt) over (partition by bal_det.assignment_id, bal_det.accrual_plan_id, bal_det.accrual_start_date order by bal_det.start_date) Ending_Balance ,null projected_amt ,null forfeited_amt ,max(nvl(bal_det.accrual_band_id,0)) OVER (PARTITION BY bal_det.assignment_id, bal_det.accrual_plan_id, bal_det.accrual_start_date order by bal_det.start_date) accrual_band_id ,paa.abs_attendance_reason_id absence_reason_id ,bal_det.absence_attendance_id ,null carryover_expiry_date ,null ineligibility_end_date FROM (SELECT bal.person_id ,bal.assignment_id ,bal.payroll_assignment_id ,bal.accrual_plan_id ,bal.accrual_category ,bal.accrual_units ,bal.accrual_start_date ,bal.accrual_end_date ,bal_det.element_type ,bal_det.absence_type_id ,bal_det.accrual_band_id ,bal_det.absence_attendance_id ,bal_det.element_type_id ,bal_det.input_value_id ,sum(decode(bal_det.element_type, 'ACR',1,0)) over (partition by bal.assignment_id, bal_det.accrual_plan_id, bal.accrual_start_date order by bal_det.start_date, bal_det.end_date, bal_det.contributed_amt desc) Period_Num ,bal_det.element_type accrual_element_type ,max(decode(bal_det.element_type, 'ACR',bal_det.start_date,null)) over (partition by bal.assignment_id, bal_det.accrual_plan_id, bal.accrual_start_date order by bal_det.start_date, bal_det.end_date, bal_det.contributed_amt desc) period_start_date ,max(decode(bal_det.element_type, 'ACR',bal_det.end_date,null)) over (partition by bal.assignment_id, bal_det.accrual_plan_id, bal.accrual_start_date order by bal_det.start_date, bal_det.end_date, bal_det.contributed_amt desc) period_end_date ,case when bal_det.element_type in ('ACR') Then bal_det.end_date else bal_det.start_date END transaction_date ,contributed_amt ,bal_det.start_date ,bal_det.end_date from ( SELECT paaf.person_id ,paaf.assignment_id ,ppa.payroll_assignment_id ,pab.accrual_plan_id ,pab.accrual_category ,pab.accrual_units ,bal.accrual_start_date ,bal.accrual_end_date FROM per_accrual_plans_vl pab ,pay_element_entries_f peef ,pay_entry_usages peu ,pay_payroll_assignments ppa ,per_all_assignments_f paaf ,table(per_accrual_bal_functions.get_accrual_balance_all(ppa.payroll_assignment_id, pab.accrual_plan_id, trunc(sysdate), 'Y')) bal WHERE 1=1 and peu.element_entry_id = peef.element_entry_id and peu.usage_level = 'PA' and peu.payroll_assignment_id = ppa.payroll_assignment_id and pab.accrual_element_type_id= peef.element_type_id and ppa.hr_assignment_id = paaf.assignment_id and trunc(sysdate) between peef.effective_start_date and peef.effective_end_date and trunc(sysdate) between paaf.effective_start_date and paaf.effective_end_date and trunc(sysdate) between peu.date_from and peu.date_to ) bal ,table(per_accrual_bal_functions.get_accrual_balance_detail(bal.payroll_assignment_id, bal.accrual_plan_id, bal.accrual_end_date)) bal_det where 1=1 and bal.accrual_plan_id = bal_det.accrual_plan_id ) bal_det ,table(per_accrual_bal_functions.get_accrual_balance(bal_det.payroll_assignment_id, bal_det.accrual_plan_id, bal_det.period_end_date)) bal_period ,per_absence_attendances paa WHERE 1=1 and bal_det.accrual_plan_id = bal_period.accrual_plan_id and bal_det.absence_attendance_id = paa.absence_attendance_id(+)
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
