# ANC_ABSENCE_PLANS_F

This base table stores absence plans data

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancabsenceplansf-30068.html#ancabsenceplansf-30068](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancabsenceplansf-30068.html#ancabsenceplansf-30068)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_ABSENCE_PLANS_F_PK | ABSENCE_PLAN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ABSENCE_PLAN_ID | NUMBER |  | 18 | Yes | ABSENCE_PLAN_ID |
| ELIG_FORFT_BALANCE_FLAG | VARCHAR2 | 30 |  |  | Loss of Eligibility Forfeit positive balance |
| GT_FORFT_BALANCE_FLAG | VARCHAR2 | 30 |  |  | Global transfer Forfeit positive balance |
| TERM_FORFT_BALANCE_FLAG | VARCHAR2 | 30 |  |  | Termination Forfeit positive balance |
| RATE_DATE_RULE | VARCHAR2 | 30 |  |  | RATE_DATE_RULE |
| DONATION_TYPE | VARCHAR2 | 30 |  |  | DONATION_TYPE |
| RTN_PSTV_BAL_TO_POOL_FLAG | VARCHAR2 | 30 |  |  | RETURN_POSITIVE_BALANCE_TO_POOL_FLAG |
| GT_ENROLL_POSITIVE_BAL_FLAG | VARCHAR2 | 30 |  |  | ENROLL_POSITIVE_BALANCE_FLAG for Global Transfer |
| GT_ENROLL_NEGATIVE_BAL_FLAG | VARCHAR2 | 30 |  |  | ENROLL_NEGATIVE_BALANCE_FLAG for Global Transfer |
| GT_TRANSFR_POSTIVE_BAL_FLAG | VARCHAR2 | 30 |  |  | TRANSFR_POSTIVE_BALANCE_FLAG for Global Transfer |
| GT_ROLLOVER_POSTIVE_BAL_FLAG | VARCHAR2 | 30 |  |  | RollOver Positive Balance for Global Transfer |
| GT_TRANSFR_LMT_RULE | VARCHAR2 | 30 |  |  | TRANSFR_LMT_RULE  for Global Transfer |
| GT_TRANSFR_LMT_FLAT_AMT | NUMBER |  |  |  | TRANSFR_LMT_FLAT_AMT for Global Transfer |
| GT_TRANSFR_LMT_FORMULA_ID | NUMBER |  | 18 |  | TRANSFR_LMT_FORMULA_ID for Global Transfer |
| GT_TRANSFR_LMT_PRORATE_RULE | VARCHAR2 | 30 |  |  | TRANSFR_LMT_PRORATE_RULE for Global Transfer |
| GT_TRFR_LMT_PRORATE_FORMULA_ID | NUMBER |  | 18 |  | TRANSFR_LMT_PRORATE_FORMULA_ID for Global Transfer |
| GT_TRANSFR_PLAN_CATEGORY | VARCHAR2 | 30 |  |  | TRANSFR_PLAN_CATEGORY for Global Transfer |
| GT_TRFR_TARGET_FORMULA_ID | NUMBER |  | 18 |  | TRANSFR_TARGET_FORMULA_ID for Global Transfer |
| ACCRUAL_POSTING_CD | VARCHAR2 | 30 |  |  | Accrual plan with incremental accrual method selected, new field for accrual posting |
| GT_TRANSFR_TO_RULES | VARCHAR2 | 30 |  |  | Transfer to Rules for Global Transfer |
| GT_ROLLOVER_TARGET_PLAN | VARCHAR2 | 30 |  |  | Rollover Target Plan for Global Transfer	Rollover Target Plan for Global Transfer |
| GT_ROLLOVER_LMT_RULE | VARCHAR2 | 30 |  |  | Rollover Limit Rule for Global Transfer |
| GT_ROLLOVER_LMT_FLAT_AMT | NUMBER |  |  |  | Rollover Flat Amount for Global Transfer |
| GT_ROLLOVER_LMT_FORMULA_ID | NUMBER |  | 18 |  | Rollover Limit Formula Id for Global Transfer |
| GT_ROLLOVER_PLAN_CONV_RATE | NUMBER |  |  |  | Rollover Plan Conversion Rate for Global Transfer |
| GT_ROLL_PRORATE_LMT_RULE | VARCHAR2 | 30 |  |  | Rollover Limit Proration Rule for Global Transfer |
| GT_ROLL_PRORATE_LMT_FRMLA_ID | NUMBER |  | 18 |  | Rollover Limit Proration Formula Id for Global Transfer |
| GT_ROLLOVER_TARGET_PLAN_ID | NUMBER |  | 18 |  | Rollover Target Plan Id for Global Transfer |
| GT_RETAIN_CARRYOVER_BAL_FLAG | VARCHAR2 | 30 |  |  | Retain Carryover Balance Flag for Local Transfer |
| ELIG_RETAIN_CARRYOVER_BAL_FLAG | VARCHAR2 | 30 |  |  | Retain Carryover Balance Flag for Local Transfer |
| ELIG_ROLLOVER_POSTIVE_BAL_FLAG | VARCHAR2 | 30 |  |  | Rollover Positive Balance Flag for Local Transfer |
| ELIG_ROLLOVER_TARGET_PLAN | VARCHAR2 | 30 |  |  | Rollover Target Plan for Local Transfer |
| ELIG_ROLLOVER_LMT_RULE | VARCHAR2 | 30 |  |  | Rollover Limit Rule for Local Transfer |
| ELIG_ROLLOVER_LMT_FLAT_AMT | NUMBER |  |  |  | Rollover Flat Amount for Local Transfer |
| ELIG_ROLLOVER_LMT_FORMULA_ID | NUMBER |  | 18 |  | Rollover Limit Formula Id for Local Transfer |
| ELIG_ROLLOVER_PLAN_CONV_RATE | VARCHAR2 | 30 |  |  | Rollover Plan conversion Rate for Local Transfer |
| ELIG_ROLLOVER_PLAN_CONVR_RATE | NUMBER |  |  |  | Rollover Plan conversion Rate for Local Transfer |
| ELIG_ROLL_PRORATE_LMT_RULE | VARCHAR2 | 30 |  |  | Rollover Limit Proration Rule for Local Transfer |
| ELIG_ROLL_PRORATE_LMT_FRMLA_ID | NUMBER |  | 18 |  | Rollover Limit Proration Formula Id for Local Transfer |
| ELIG_ROLLOVER_TARGET_PLAN_ID | NUMBER |  | 18 |  | Rollover Target Plan Id for Local Transfer |
| BEN_IMPACT_FLAG | VARCHAR2 | 30 |  |  | Benfits Integration Flag |
| PENDING_DISBURSE_FLAG | VARCHAR2 | 30 |  |  | Benfits Pending disbursement flag |
| ELECTION_DATE_RULE | VARCHAR2 | 240 |  |  | Benefits Election Date Rule |
| EXPIRATION_TERM_CD | VARCHAR2 | 30 |  |  | EXPIRATION_TERM_CD |
| BASE_NAME | VARCHAR2 | 240 |  |  | BASE_NAME |
| LEG_GROUPING_CD | VARCHAR2 | 30 |  |  | LEG_GROUPING_CD |
| DISABLE_ENT_OVERRIDE_FLAG | VARCHAR2 | 30 |  |  | DISABLE_ENT_OVERRIDE_FLAG |
| WS_CATEGORY_CD | VARCHAR2 | 30 |  |  | WS_CATEGORY_CD |
| ABSENCE_DURATION_FORMULA_ID | NUMBER |  | 18 |  | ABSENCE_DURATION_FORMULA_ID |
| VESTING_PERIOD_FORMULA_ID | NUMBER |  | 18 |  | VESTING_PERIOD_FORMULA_ID |
| VESTING_PERIOD_UOM | VARCHAR2 | 30 |  |  | VESTING_PERIOD_UOM |
| VESTING_PERIOD_DURATION | NUMBER |  |  |  | VESTING_PERIOD_DURATION |
| ACCRUAL_VESTING_CD | VARCHAR2 | 30 |  |  | ACCRUAL_VESTING_CD |
| ACCRUAL_METHOD_CD | VARCHAR2 | 30 |  |  | ACCRUAL_METHOD_CD |
| PARTIAL_ACCRUAL_PRORATION_RULE | VARCHAR2 | 30 |  |  | PARTIAL_ACCRUAL_PRORATION_RULE |
| PARTIAL_ACCRUAL_FORMULA_ID | NUMBER |  | 18 |  | PARTIAL_ACCRUAL_FORMULA_ID |
| ROUNDING_RULE | VARCHAR2 | 30 |  |  | ROUNDING_RULE |
| ROUNDING_PRECISION | NUMBER |  | 18 |  | ROUNDING_PRECISION |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| ANC_ABSENCE_PLANS_F_ALTCD | VARCHAR2 | 240 |  | Yes | ANC_ABSENCE_PLANS_F_ALTCD |
| LEGISLATION_CODE | VARCHAR2 | 30 |  | Yes | LEGISLATION_CODE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| PLAN_STATUS | VARCHAR2 | 30 |  |  | PLAN_STATUS |
| PLAN_UOM | VARCHAR2 | 30 |  |  | PLAN_UOM |
| PROCESSING_LEVEL_CD | VARCHAR2 | 30 |  |  | PROCESSING_LEVEL_CD |
| ENTL_METHOD_CD | VARCHAR2 | 30 |  |  | ENTL_METHOD_CD |
| PAY_ADVANCES_FLAG | VARCHAR2 | 30 |  |  | PAY_ADVANCES_FLAG |
| PLAN_MGMT_CD | VARCHAR2 | 30 |  |  | PLAN_MGMT_CD |
| PLAN_PERIOD_ID | NUMBER |  | 18 |  | PLAN_PERIOD_ID |
| PLAN_PERIOD_TYPE | VARCHAR2 | 30 |  |  | PLAN_PERIOD_TYPE |
| PERIOD_UOM | VARCHAR2 | 30 |  |  | PERIOD_UOM |
| CALENDAR_START_DAY | NUMBER |  |  |  | CALENDAR_START_DAY |
| CALENDAR_START_MONTH | VARCHAR2 | 30 |  |  | CALENDAR_START_MONTH |
| ANNIVERSARY_EVENT_RULE | VARCHAR2 | 30 |  |  | ANNIVERSARY_EVENT_RULE |
| ANNIVERSARY_EVENT_FORMULA_ID | NUMBER |  | 18 |  | ANNIVERSARY_EVENT_FORMULA_ID |
| ROLL_BACKWARD_END_RULE | VARCHAR2 | 30 |  |  | ROLL_BACKWARD_END_RULE |
| ROLL_BACKWARD_END_FORMULA_ID | NUMBER |  | 18 |  | ROLL_BACKWARD_END_FORMULA_ID |
| ROLL_FORWARD_START_RULE | VARCHAR2 | 30 |  |  | ROLL_FORWARD_START_RULE |
| ROLL_FORWARD_START_FORMULA_ID | NUMBER |  | 18 |  | ROLL_FORWARD_START_FORMULA_ID |
| ROLL_PERIOD_DURATION | NUMBER |  |  |  | ROLL_PERIOD_DURATION |
| ABSENCE_DURATION_DEFN_ID | NUMBER |  | 18 |  | ABSENCE_DURATION_DEFN_ID |
| OVERLAP_CD | VARCHAR2 | 30 |  |  | OVERLAP_CD |
| ENROLLMENT_START_RULE | VARCHAR2 | 30 |  |  | ENROLLMENT_START_RULE |
| ENROLLMENT_START_FORMULA_ID | NUMBER |  | 18 |  | ENROLLMENT_START_FORMULA_ID |
| WAIT_PERIOD_DUR_UOM | VARCHAR2 | 30 |  |  | WAIT_PERIOD_DUR_UOM |
| WAIT_PERIOD_DUR_UNITS | NUMBER |  |  |  | WAIT_PERIOD_DUR_UNITS |
| ENROLLMENT_END_RULE | VARCHAR2 | 30 |  |  | ENROLLMENT_END_RULE |
| ENROLLMENT_END_FORMULA_ID | NUMBER |  | 18 |  | ENROLLMENT_END_FORMULA_ID |
| ENTITLEMENT_END_RULE | VARCHAR2 | 30 |  |  | ENTITLEMENT_END_RULE |
| ENTITLEMENT_END_FORMULA_ID | NUMBER |  | 18 |  | ENTITLEMENT_END_FORMULA_ID |
| EMP_ENRL_POSITIVE_BALANCE_FLAG | VARCHAR2 | 30 |  |  | EMP_ENRL_POSITIVE_BALANCE_FLAG |
| EVAL_ENTITLEMENT_FLAG | VARCHAR2 | 30 |  |  | EVAL_ENTITLEMENT_FLAG |
| EMP_ENRL_NEGATIVE_BALANCE_FLAG | VARCHAR2 | 30 |  |  | EMP_ENRL_NEGATIVE_BALANCE_FLAG |
| EMP_ENRL_TERMINATE_ENTL_FLAG | VARCHAR2 | 30 |  |  | EMP_ENRL_TERMINATE_ENTL_FLAG |
| ENROLL_POSITIVE_BALANCE_FLAG | VARCHAR2 | 30 |  |  | ENROLL_POSITIVE_BALANCE_FLAG |
| ENROLL_NEGATIVE_BALANCE_FLAG | VARCHAR2 | 30 |  |  | ENROLL_NEGATIVE_BALANCE_FLAG |
| ENROLL_TERMINATE_ENTL_FLAG | VARCHAR2 | 30 |  |  | ENROLL_TERMINATE_ENTL_FLAG |
| ACC_DEFINITION_TYPE | VARCHAR2 | 30 |  |  | ACC_DEFINITION_TYPE |
| ACC_FORMULA_ID | NUMBER |  | 18 |  | ACC_FORMULA_ID |
| ACCRUAL_MODE | VARCHAR2 | 30 |  |  | ACCRUAL_MODE |
| ENTL_DEFINITION_TYPE | VARCHAR2 | 30 |  |  | ENTL_DEFINITION_TYPE |
| ENTL_FORMULA_ID | NUMBER |  | 18 |  | ENTL_FORMULA_ID |
| PRORATION_RULE | VARCHAR2 | 30 |  |  | PRORATION_RULE |
| PRORATION_FORMULA_ID | NUMBER |  | 18 |  | PRORATION_FORMULA_ID |
| CEIL_LIMIT_RULE | VARCHAR2 | 30 |  |  | CEIL_LIMIT_RULE |
| CEIL_LIMIT_FORMULA_ID | NUMBER |  | 18 |  | CEIL_LIMIT_FORMULA_ID |
| CEIL_LIMIT_PRORATE_RULE | VARCHAR2 | 30 |  |  | CEIL_LIMIT_PRORATE_RULE |
| CEIL_LMT_PRORATE_FORMULA_ID | NUMBER |  | 18 |  | CEIL_LMT_PRORATE_FORMULA_ID |
| CEIL_LIMIT_FLAT_AMT | NUMBER |  |  |  | CEIL_LIMIT_FLAT_AMT |
| CARRY_OVER_EXPIRED_FLAG | VARCHAR2 | 30 |  |  | CARRY_OVER_EXPIRED_FLAG |
| CARRY_OVER_EXPIRED_UNITS | NUMBER |  |  |  | CARRY_OVER_EXPIRED_UNITS |
| CARRY_OVER_EXPIRED_UOM | VARCHAR2 | 30 |  |  | CARRY_OVER_EXPIRED_UOM |
| CARRY_OVER_RULE | VARCHAR2 | 30 |  |  | CARRY_OVER_RULE |
| CARRY_OVER_FORMULA_ID | NUMBER |  | 18 |  | CARRY_OVER_FORMULA_ID |
| CARRY_OVER_PRORATE_RULE | VARCHAR2 | 30 |  |  | CARRY_OVER_PRORATE_RULE |
| CARRY_OVER_PRORATE_FORMULA_ID | NUMBER |  | 18 |  | CARRY_OVER_PRORATE_FORMULA_ID |
| CARRY_OVER_FLAT_AMT | NUMBER |  |  |  | CARRY_OVER_FLAT_AMT |
| PAY_RATE_FACTOR | NUMBER |  |  |  | PAY_RATE_FACTOR |
| ACC_PERIOD_FREQUENCY | VARCHAR2 | 30 |  |  | ACC_PERIOD_FREQUENCY |
| ACC_PERIOD_WFM_CALEDAR_ID | NUMBER |  | 18 |  | ACC_PERIOD_WFM_CALEDAR_ID |
| ACC_PERIOD_PAYROLL_FREQ_ID | NUMBER |  | 18 |  | ACC_PERIOD_PAYROLL_FREQ_ID |
| ACC_NEGATIVE_BAL_FLAG | VARCHAR2 | 30 |  |  | ACC_NEGATIVE_BAL_FLAG |
| ACC_NEGATIVE_BAL_LIMIT | NUMBER |  |  |  | ACC_NEGATIVE_BAL_LIMIT |
| EXPIRATION_LIMIT | NUMBER |  |  |  | EXPIRATION_LIMIT |
| EXPIRATION_UOM_CD | VARCHAR2 | 30 |  |  | EXPIRATION_UOM_CD |
| EXPIRATION_ACTION_CD | VARCHAR2 | 30 |  |  | EXPIRATION_ACTION_CD |
| MGR_EXPIRATION_UPDATE | VARCHAR2 | 30 |  |  | MGR_EXPIRATION_UPDATE |
| ADMIN_EXPIRATION_UPDATE | VARCHAR2 | 30 |  |  | ADMIN_EXPIRATION_UPDATE |
| ACC_NEGATIVE_BAL_UOM | VARCHAR2 | 30 |  |  | ACC_NEGATIVE_BAL_UOM |
| STATUTORY_FLAG | VARCHAR2 | 30 |  |  | STATUTORY_FLAG |
| PREV_EMP_ENTL_FLAG | VARCHAR2 | 30 |  |  | PREV_EMP_ENTL_FLAG |
| PREV_EMP_USAGE_FLAG | VARCHAR2 | 30 |  |  | PREV_EMP_USAGE_FLAG |
| CASH_OUT_FLAG | VARCHAR2 | 30 |  |  | CASH_OUT_FLAG |
| BALANCE_TRANSFER_FLAG | VARCHAR2 | 30 |  |  | BALANCE_TRANSFER_FLAG |
| OTHER_ADJUSTMENT_FLAG | VARCHAR2 | 30 |  |  | OTHER_ADJUSTMENT_FLAG |
| OTHER_REASONS | VARCHAR2 | 4000 |  |  | OTHER_REASONS |
| PLAN_USE_RATE_RULE | VARCHAR2 | 30 |  |  | PLAN_USE_RATE_RULE |
| PLAN_USE_FORMULA_ID | NUMBER |  | 18 |  | PLAN_USE_FORMULA_ID |
| PLAN_USE_RATE_ID | NUMBER |  | 18 |  | PLAN_USE_RATE_ID |
| PAYOUT_RATE_RULE | VARCHAR2 | 30 |  |  | PAYOUT_RATE_RULE |
| PAYOUT_RATE_FORMULA_ID | NUMBER |  | 18 |  | PAYOUT_RATE_FORMULA_ID |
| PAYOUT_RATE_ID | NUMBER |  | 18 |  | PAYOUT_RATE_ID |
| CASHOUT_RATE_RULE | VARCHAR2 | 30 |  |  | CASHOUT_RATE_RULE |
| CASHOUT_RATE_FORMULA_ID | NUMBER |  | 18 |  | CASHOUT_RATE_FORMULA_ID |
| CASHOUT_RATE_ID | NUMBER |  | 18 |  | CASHOUT_RATE_ID |
| LIABILITY_RATE_RULE | VARCHAR2 | 30 |  |  | LIABILITY_RATE_RULE |
| LIABILITY_RATE_ID | NUMBER |  | 18 |  | LIABILITY_RATE_ID |
| PAYROLL_IMPACT_FLAG | VARCHAR2 | 30 |  |  | PAYROLL_IMPACT_FLAG |
| LIABILITY_RATE_FORMULA_ID | NUMBER |  | 18 |  | LIABILITY_RATE_FORMULA_ID |
| PLAN_ACTIVATION_FLAG | VARCHAR2 | 30 |  |  | PLAN_ACTIVATION_FLAG |
| PAYROLL_MAPPING_ID | NUMBER |  | 18 |  | PAYROLL_MAPPING_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | INFORMATION_CATEGORY |
| INFORMATION1 | VARCHAR2 | 150 |  |  | INFORMATION1 |
| INFORMATION2 | VARCHAR2 | 150 |  |  | INFORMATION2 |
| INFORMATION3 | VARCHAR2 | 150 |  |  | INFORMATION3 |
| INFORMATION4 | VARCHAR2 | 150 |  |  | INFORMATION4 |
| INFORMATION5 | VARCHAR2 | 150 |  |  | INFORMATION5 |
| INFORMATION6 | VARCHAR2 | 150 |  |  | INFORMATION6 |
| INFORMATION7 | VARCHAR2 | 150 |  |  | INFORMATION7 |
| INFORMATION8 | VARCHAR2 | 150 |  |  | INFORMATION8 |
| INFORMATION9 | VARCHAR2 | 150 |  |  | INFORMATION9 |
| INFORMATION10 | VARCHAR2 | 150 |  |  | INFORMATION10 |
| INFORMATION11 | VARCHAR2 | 150 |  |  | INFORMATION11 |
| INFORMATION12 | VARCHAR2 | 150 |  |  | INFORMATION12 |
| INFORMATION13 | VARCHAR2 | 150 |  |  | INFORMATION13 |
| INFORMATION14 | VARCHAR2 | 150 |  |  | INFORMATION14 |
| INFORMATION15 | VARCHAR2 | 150 |  |  | INFORMATION15 |
| INFORMATION16 | VARCHAR2 | 150 |  |  | INFORMATION16 |
| INFORMATION17 | VARCHAR2 | 150 |  |  | INFORMATION17 |
| INFORMATION18 | VARCHAR2 | 150 |  |  | INFORMATION18 |
| INFORMATION19 | VARCHAR2 | 150 |  |  | INFORMATION19 |
| INFORMATION20 | VARCHAR2 | 150 |  |  | INFORMATION20 |
| INFORMATION21 | VARCHAR2 | 150 |  |  | INFORMATION21 |
| INFORMATION22 | VARCHAR2 | 150 |  |  | INFORMATION22 |
| INFORMATION23 | VARCHAR2 | 150 |  |  | INFORMATION23 |
| INFORMATION24 | VARCHAR2 | 150 |  |  | INFORMATION24 |
| INFORMATION25 | VARCHAR2 | 150 |  |  | INFORMATION25 |
| INFORMATION26 | VARCHAR2 | 150 |  |  | INFORMATION26 |
| INFORMATION27 | VARCHAR2 | 150 |  |  | INFORMATION27 |
| INFORMATION28 | VARCHAR2 | 150 |  |  | INFORMATION28 |
| INFORMATION29 | VARCHAR2 | 150 |  |  | INFORMATION29 |
| INFORMATION30 | VARCHAR2 | 150 |  |  | INFORMATION30 |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| INFORMATION_NUMBER1 | NUMBER |  |  |  | INFORMATION_NUMBER1 |
| INFORMATION_NUMBER2 | NUMBER |  |  |  | INFORMATION_NUMBER2 |
| INFORMATION_NUMBER3 | NUMBER |  |  |  | INFORMATION_NUMBER3 |
| INFORMATION_NUMBER4 | NUMBER |  |  |  | INFORMATION_NUMBER4 |
| INFORMATION_NUMBER5 | NUMBER |  |  |  | INFORMATION_NUMBER5 |
| INFORMATION_NUMBER6 | NUMBER |  |  |  | INFORMATION_NUMBER6 |
| INFORMATION_NUMBER7 | NUMBER |  |  |  | INFORMATION_NUMBER7 |
| INFORMATION_NUMBER8 | NUMBER |  |  |  | INFORMATION_NUMBER8 |
| INFORMATION_NUMBER9 | NUMBER |  |  |  | INFORMATION_NUMBER9 |
| INFORMATION_NUMBER10 | NUMBER |  |  |  | INFORMATION_NUMBER10 |
| INFORMATION_NUMBER11 | NUMBER |  |  |  | INFORMATION_NUMBER11 |
| INFORMATION_NUMBER12 | NUMBER |  |  |  | INFORMATION_NUMBER12 |
| INFORMATION_NUMBER13 | NUMBER |  |  |  | INFORMATION_NUMBER13 |
| INFORMATION_NUMBER14 | NUMBER |  |  |  | INFORMATION_NUMBER14 |
| INFORMATION_NUMBER15 | NUMBER |  |  |  | INFORMATION_NUMBER15 |
| INFORMATION_NUMBER16 | NUMBER |  |  |  | INFORMATION_NUMBER16 |
| INFORMATION_NUMBER17 | NUMBER |  |  |  | INFORMATION_NUMBER17 |
| INFORMATION_NUMBER18 | NUMBER |  |  |  | INFORMATION_NUMBER18 |
| INFORMATION_NUMBER19 | NUMBER |  |  |  | INFORMATION_NUMBER19 |
| INFORMATION_NUMBER20 | NUMBER |  |  |  | INFORMATION_NUMBER20 |
| INFORMATION_DATE1 | DATE |  |  |  | INFORMATION_DATE1 |
| INFORMATION_DATE2 | DATE |  |  |  | INFORMATION_DATE2 |
| INFORMATION_DATE3 | DATE |  |  |  | INFORMATION_DATE3 |
| INFORMATION_DATE4 | DATE |  |  |  | INFORMATION_DATE4 |
| INFORMATION_DATE5 | DATE |  |  |  | INFORMATION_DATE5 |
| INFORMATION_DATE6 | DATE |  |  |  | INFORMATION_DATE6 |
| INFORMATION_DATE7 | DATE |  |  |  | INFORMATION_DATE7 |
| INFORMATION_DATE8 | DATE |  |  |  | INFORMATION_DATE8 |
| INFORMATION_DATE9 | DATE |  |  |  | INFORMATION_DATE9 |
| INFORMATION_DATE10 | DATE |  |  |  | INFORMATION_DATE10 |
| INFORMATION_DATE11 | DATE |  |  |  | INFORMATION_DATE11 |
| INFORMATION_DATE12 | DATE |  |  |  | INFORMATION_DATE12 |
| INFORMATION_DATE13 | DATE |  |  |  | INFORMATION_DATE13 |
| INFORMATION_DATE14 | DATE |  |  |  | INFORMATION_DATE14 |
| INFORMATION_DATE15 | DATE |  |  |  | INFORMATION_DATE15 |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ANC_CHAR1 | VARCHAR2 | 255 |  |  | Absence Character column 1 |
| ANC_CHAR2 | VARCHAR2 | 255 |  |  | Absence Character column 2 |
| ANC_CHAR3 | VARCHAR2 | 255 |  |  | Absence Character column 3 |
| ANC_CHAR4 | VARCHAR2 | 255 |  |  | Absence Character column 4 |
| ANC_CHAR5 | VARCHAR2 | 255 |  |  | Absence Character column 5 |
| ANC_NUMBER1 | NUMBER |  |  |  | Absence Number column 1 |
| ANC_NUMBER2 | NUMBER |  |  |  | Absence Number column 2 |
| ANC_NUMBER3 | NUMBER |  |  |  | Absence Number column 3 |
| ANC_NUMBER4 | NUMBER |  |  |  | Absence Number column 4 |
| ANC_NUMBER5 | NUMBER |  |  |  | Absence Number column 5 |
| ANC_DATE1 | DATE |  |  |  | Absence Date column 1 |
| ANC_DATE2 | DATE |  |  |  | Absence Date column 2 |
| ANC_DATE3 | DATE |  |  |  | Absence Date column 3 |
| ANC_DATE4 | DATE |  |  |  | Absence Date column 4 |
| ANC_DATE5 | DATE |  |  |  | Absence Date column 5 |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTITLEMENT_START_DATE | VARCHAR2 | 30 |  |  | Qualification Plan Entitlement Start Date |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| COMP_MNUL_ADJRSN | VARCHAR2 | 4000 |  |  | COMP_MNUL_ADJRSN |
| COMP_EXP_ADJRSN | VARCHAR2 | 4000 |  |  | COMP_EXP_ADJRSN |
| MGR_MANUAL_ADJUSTMENT | VARCHAR2 | 20 |  |  | MGR_MANUAL_ADJUSTMENT |
| ADMIN_MANUAL_ADJUSTMENT | VARCHAR2 | 20 |  |  | ADMIN_MANUAL_ADJUSTMENT |
| ACC_LMT_RULE | VARCHAR2 | 30 |  |  | ACC_LMT_RULE |
| ACC_LMT_FLAT_AMT | NUMBER |  |  |  | ACC_LMT_FLAT_AMT |
| ACC_LIMIT_FORMULA_ID | NUMBER |  | 18 |  | ACC_LIMIT_FORMULA_ID |
| ACC_LIMIT_PRORATE_RULE | VARCHAR2 | 30 |  |  | ACC_LIMIT_PRORATE_RULE |
| ACC_LMT_PRORATE_FORMULA_ID | NUMBER |  | 18 |  | ACC_LMT_PRORATE_FORMULA_ID |
| RE_INSTATEMENT_FLAG | VARCHAR2 | 20 |  |  | Prior Balance Re-instatement |
| RE_ENRL_BAL_LMT | NUMBER |  |  |  | Balance Limit |
| TIME_FRAME_LMT | NUMBER |  |  |  | Timeframe Limit |
| TIME_FRAME_UOM | VARCHAR2 | 30 |  |  | Timeframe UOM |
| ACC_EMP_BAL_DISPLAY | VARCHAR2 | 30 |  |  | Worker Balance Display |
| ACC_MGR_BAL_DISPLAY | VARCHAR2 | 30 |  |  | Manager Balance Display |
| TRANSFR_POSITIVE_BALANCE_FLAG | VARCHAR2 | 30 |  |  | Transfer positive balance |
| TRANSFR_LMT_RULE | VARCHAR2 | 30 |  |  | Transfer Limit Rule |
| TRANSFR_LMT_FLAT_AMT | NUMBER |  |  |  | Transfer Limit Amount |
| TRANSFR_LMT_FORMULA_ID | NUMBER |  | 18 |  | Transfer Limit Formula |
| TRANSFR_LMT_PRORATE_RULE | VARCHAR2 | 30 |  |  | Transfer Limit Proration Rule |
| TRANSFR_LMT_PRORATE_FORMULA_ID | NUMBER |  | 18 |  | Transfer Limit Proration Formula |
| TRANSFR_PLAN_CATEGORY | VARCHAR2 | 30 |  |  | Transfer Plan Category |
| TRANSFR_TARGET_FORMULA_ID | NUMBER |  | 18 |  | Transfer Target Plan Formula |
| ROLLOVR_LMT_RULE | VARCHAR2 | 30 |  |  | Rollover Limit Rule |
| ROLLOVR_LMT_FLAT_AMT | NUMBER |  |  |  | Rollover Limit Amount |
| ROLLOVR_LMT_FORMULA_ID | NUMBER |  | 18 |  | Rollover Limit Formula |
| ROLLOVR_LMT_PRORATE_RULE | VARCHAR2 | 30 |  |  | Rollover Limit Proration Rule |
| ROLLOVR_LMT_PRORATE_FORMULA_ID | NUMBER |  | 18 |  | Rollover Limit Proration Formula |
| ROLLOVR_TARGET_PLAN | NUMBER |  | 18 |  | Rollover Target Plan |
| ROLLOVR_PLAN_CONVERSION_RATE | NUMBER |  |  |  | Rollover Target Plan Conversion Rate |
| YEAR_END_BALANCE_DISBURSE_FLAG | VARCHAR2 | 30 |  |  | Year End Balance Disburse |
| EMP_MANUAL_ADJUSTMENT | VARCHAR2 | 20 |  |  | Enable for worker flag |
| DISB_RULE | VARCHAR2 | 30 |  |  | Disbursement rule for donation plan |
| DISB_FORMULA_ID | NUMBER |  | 18 |  | DISB_FORMULA_ID |
| DISB_MIN_FLAT_AMT | NUMBER |  |  |  | DISB_MIN_FLAT_AMT |
| DISB_MAX_FLAT_AMT | NUMBER |  |  |  | DISB_MAX_FLAT_AMT |
| DISB_INCR_FLAT_AMT | NUMBER |  |  |  | DISB_INCR_FLAT_AMT |
| DON_ADMIN_MANUAL_ADJ | VARCHAR2 | 20 |  |  | DON_ADMIN_MANUAL_ADJ |
| DON_MGR_MANUAL_ADJ | VARCHAR2 | 20 |  |  | DON_MGR_MANUAL_ADJ |
| DON_EMP_MANUAL_ADJ | VARCHAR2 | 20 |  |  | DON_EMP_MANUAL_ADJ |
| DON_RULE | VARCHAR2 | 30 |  |  | Donation rule for donation plan |
| DON_FORMULA_ID | NUMBER |  | 18 |  | DON_FORMULA_ID |
| DON_MIN_FLAT_AMT | NUMBER |  |  |  | DON_MIN_FLAT_AMOUNT |
| DON_MAX_FLAT_AMT | NUMBER |  |  |  | DON_MAX_FLAT_AMT |
| DON_INCR_FLAT_AMT | NUMBER |  |  |  | DON_INCR_FLAT_AMT |
| ELECT_DISB_PAY_RATE_FACTOR | NUMBER |  |  |  | Default payment percentage for elective disbursements |
| YREND_DISB_PAY_RATE_FACTOR | NUMBER |  |  |  | Default payment percentage for year end disbursements |
| ELECT_DISB_VALID_FORMULA_ID | NUMBER |  | 18 |  | Disbursement validation formula for elective disbursements |
| YREND_DISB_VALID_FORMULA_ID | NUMBER |  | 18 |  | Disbursement validation formula for year end disbursements |
| COMP_MGR_MANUAL_ADJ | VARCHAR2 | 20 |  |  | Compensation plan manager disbursements |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| ALLOW_CASHOUT_COVR_ADMIN | VARCHAR2 | 80 |  |  | Allow disbursements from carryover for administrator |
| ALLOW_CASHOUT_COVR_MGR | VARCHAR2 | 80 |  |  | Allow disbursements from carryover for manager |
| ALLOW_CASHOUT_COVR_EMP | VARCHAR2 | 80 |  |  | Allow disbursements from carryover for employee |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_ABSENCE_PLANS_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| ANC_ABSENCE_PLANS_F_PK | Unique | Default | ABSENCE_PLAN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| ANC_ABSENCE_PLANS_F_PK1 | Unique | Default | ABSENCE_PLAN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
