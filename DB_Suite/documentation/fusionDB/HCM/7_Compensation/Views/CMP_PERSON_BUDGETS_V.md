# CMP_PERSON_BUDGETS_V

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmppersonbudgetsv-7377.html#cmppersonbudgetsv-7377](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmppersonbudgetsv-7377.html#cmppersonbudgetsv-7377)

## Columns

- PERSON_EVENT_ID
- POOL_ID
- PLAN_ID
- PERIOD_ID
- BUDGET_POP_CD
- ACCESS_CD
- DIST_BUDGET_VAL
- WS_BUDGET_VAL
- DIST_BUDGET_ISSUE_VAL
- WS_BUDGET_ISSUE_VAL
- DFLT_DIST_BUDGET_VAL
- DFLT_WS_BUDGET_VAL
- DIST_BUDGET_ISSUE_DATE
- WS_BUDGET_ISSUE_DATE
- WS_BUDGET_VAL_LAST_UPD_DATE
- DIST_BUDGET_VAL_LAST_UPD_DATE
- WS_BUDGET_VAL_LAST_UPD_BY
- DIST_BUDGET_VAL_LAST_UPD_BY
- BUDGET_VAL_AMOUNT
- BUDGET_VAL_PERCENT
- OBJECT_VERSION_NUMBER
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- CREATED_BY
- CREATION_DATE
- OVERRIDE_OVER_BUDGET_CODE
- OVERRIDE_OVER_ALLOCATE_CODE
- BUDGET_LAST_UPD_DATE
- PUBLISHED_DIST_BUDGET_AMOUNT
- PUBLISHED_WS_BUDGET_AMOUNT
- PUBLISHED_DIST_BUDGET_PCT
- PUBLISHED_WS_BUDGET_PCT
- UNPUBLISHED_DIST_BUDGET_AMOUNT
- UNPUBLISHED_WS_BUDGET_AMOUNT
- UNPUBLISHED_DIST_BUDGET_PCT
- UNPUBLISHED_WS_BUDGET_PCT
- BUDGETING_STYLE
- TOTAL_ELIGIBLE_SALARY
- TOTAL_ELIGIBLE_WORKERS
- TOTAL_DIRECT_WORKERS
- OVERALL_BUDGET_AMOUNT
- USED_BUDGET
- REC_VAL_ALL
- REC_MN_VAL_ALL
- REC_MX_VAL_ALL
- USER_PREFERRED_EXCHANGE_RATE

## Query

```sql
Select bud.PERSON_EVENT_ID, bud.POOL_ID, bud.PLAN_ID, bud.PERIOD_ID, bud.BUDGET_POP_CD, bud.ACCESS_CD, bud.DIST_BUDGET_VAL, bud.WS_BUDGET_VAL, bud.DIST_BUDGET_ISSUE_VAL, bud.WS_BUDGET_ISSUE_VAL, bud.DFLT_DIST_BUDGET_VAL, bud.DFLT_WS_BUDGET_VAL, bud.DIST_BUDGET_ISSUE_DATE, bud.WS_BUDGET_ISSUE_DATE, bud.WS_BUDGET_VAL_LAST_UPD_DATE, bud.DIST_BUDGET_VAL_LAST_UPD_DATE, bud.WS_BUDGET_VAL_LAST_UPD_BY, bud.DIST_BUDGET_VAL_LAST_UPD_BY, bud.BUDGET_VAL_AMOUNT, bud.BUDGET_VAL_PERCENT, bud.OBJECT_VERSION_NUMBER, bud.LAST_UPDATE_DATE, bud.LAST_UPDATED_BY, bud.LAST_UPDATE_LOGIN, bud.CREATED_BY, bud.CREATION_DATE, bud.OVERRIDE_OVER_BUDGET_CODE, bud.OVERRIDE_OVER_ALLOCATE_CODE, bud.BUDGET_LAST_UPD_DATE, decode((pool.budgeting_style),'EMP',(summ.s1_emp_bdgt_val_all), 'AMT', bud.dist_budget_issue_val, 'PER', (bud.dist_budget_issue_val)*(summ.s1_elig_sal_val_all)/100) published_dist_budget_amount, decode((pool.budgeting_style),'EMP',(summ.s1_emp_bdgt_val_direct) ,'AMT', bud.ws_budget_issue_val, 'PER',(bud.ws_budget_issue_val)*(summ.s1_elig_sal_val_direct)/100) published_ws_budget_amount, decode((pool.budgeting_style),'EMP',(summ.s1_emp_bdgt_val_all*100/(decode(summ.s1_elig_sal_val_all,0,null,summ.s1_elig_sal_val_all))) ,'AMT', (bud.dist_budget_issue_val*100)/(decode(summ.s1_elig_sal_val_all,0,null,summ.s1_elig_sal_val_all)), 'PER', bud.dist_budget_issue_val) published_dist_budget_pct, decode((pool.budgeting_style),'EMP',(summ.s1_emp_bdgt_val_direct*100/(decode(summ.s1_elig_sal_val_direct,0,null,summ.s1_elig_sal_val_direct))) ,'AMT', (bud.ws_budget_issue_val*100)/(decode(summ.s1_elig_sal_val_direct,0,null,summ.s1_elig_sal_val_direct)), 'PER', bud.ws_budget_issue_val) published_ws_budget_pct, decode(bud.dist_budget_issue_val,bud.dist_budget_val,0, decode(pool.budgeting_style,'AMT',bud.dist_budget_val,'PER',(bud.dist_budget_val)*(summ.s1_elig_sal_val_all)/100)) unpublished_dist_budget_amount, decode(bud.ws_budget_issue_val,bud.ws_budget_val,0, decode(pool.budgeting_style,'AMT',bud.ws_budget_val,'PER',(bud.ws_budget_val)*(summ.s1_elig_sal_val_direct)/100)) unpublished_ws_budget_amount, decode(bud.dist_budget_issue_val,bud.dist_budget_val,0, decode(pool.budgeting_style,'AMT',(bud.dist_budget_val*100)/(decode(summ.s1_elig_sal_val_all,0,null,summ.s1_elig_sal_val_all)),'PER',bud.dist_budget_val)) unpublished_dist_budget_pct, decode(bud.ws_budget_issue_val,bud.ws_budget_val,0, decode(pool.budgeting_style,'AMT',(bud.ws_budget_val*100)/(decode(summ.s1_elig_sal_val_direct,0,null,summ.s1_elig_sal_val_direct)),'PER',bud.ws_budget_val)) unpublished_ws_budget_pct , pool.budgeting_style, summ.s1_elig_sal_val_all total_eligible_salary, summ.s1_elig_count_all total_eligible_workers, summ.s1_elig_count_direct total_direct_workers, decode(pool.budgeting_style,'EMP', summ.s1_emp_bdgt_val_all, 'AMT', nvl(bud.dist_budget_issue_val, nvl(summ.s1_ws_bdgt_iss_val_all,0) + nvl(bud.ws_budget_issue_val,0)), 'PER', nvl(bud.dist_budget_issue_val * summ.s1_elig_sal_val_all/100, nvl(summ.s1_ws_bdgt_iss_val_all,0) + nvl(bud.ws_budget_issue_val*summ.s1_elig_sal_val_direct/100,0))) overall_budget_amount, wsalloc.s1_ws_val_all + nvl(usage.usage_val,0) used_budget, summ.s1_rec_val_all rec_val_all , summ.s1_rec_mn_val_all rec_mn_val_all , summ.s1_rec_mx_val_all rec_mx_val_all , nvl(xchgRate.XCHG_RATE,decode(GL_CURRENCY_API.GET_CLOSEST_RATE_SQL(plan.corporate_currency,FND_GLOBAL.CURRENCY,sysdate,'Corporate',366),0,1,-1,1,-2,1,GL_CURRENCY_API.GET_CLOSEST_RATE_SQL(plan.corporate_currency,FND_GLOBAL.CURRENCY,sysdate,'Corporate',366))) AS user_preferred_exchange_rate FROM cmp_person_budgets bud, cmp_budget_pools_b pool, (SELECT person_event_id s1_person_event_id, pool_id s1_pool_id, plan_id , period_id , component_id, person_id, SUM(elig_count_all) s1_elig_count_all, SUM(elig_count_direct) s1_elig_count_direct, SUM(elig_sal_val_all) s1_elig_sal_val_all, SUM(elig_sal_val_direct) s1_elig_sal_val_direct, SUM(emp_bdgt_val_all) s1_emp_bdgt_val_all, SUM(emp_bdgt_val_direct) s1_emp_bdgt_val_direct, SUM(ws_bdgt_iss_val_all) s1_ws_bdgt_iss_val_all, SUM(REC_VAL_ALL) s1_rec_val_all, SUM(REC_MN_VAL_ALL) s1_rec_mn_val_all, SUM(REC_MX_VAL_ALL) s1_rec_mx_val_all FROM cmp_cwb_summary GROUP BY person_event_id, pool_id, plan_id, period_id, component_id,person_id ) summ, (select sum(s.ws_val_direct) s1_ws_val_direct , sum(s.ws_val_all) s1_ws_val_all, p.plan_id plan_id, s.person_event_id person_event_id, s.period_id, p.pool_id, s.person_id, decode(sum(s.elig_count_direct), sum(s.elig_count_all), 'N', 'Y') is_bdgt_mgr from cmp_cwb_summary s, cmp_cwb_plan_definitions p where p.definition_type = 'COMPONENT' and s.component_id = p.component_id and s.period_id = p.period_id and p.period_id = s.period_id and p.plan_id = s.plan_id and s.plan_id = p.plan_id group by p.plan_id, s.person_event_id, s.period_id, p.pool_id, s.person_id) wsalloc, (select sum(u.usage_val) usage_val, max(h.mgr_person_event_id) s2_mgr_person_event_id, max(pool_id) s2_pool_id from cmp_budget_usages u, cmp_cwb_hrchy h where h.emp_person_event_id = u.person_event_id and u.enabled='Y' and h.lvl_num < 99999 and h.lvl_num > -1 group by mgr_person_event_id,pool_id ) usage, cmp_plans_vl plan, CMP_CWB_XCHG xchgRate Where bud.person_event_id = summ.s1_person_event_id and bud.pool_id = summ.s1_pool_id and summ.person_id = wsalloc.person_id and summ.s1_pool_id = wsalloc.pool_id and summ.plan_id = wsalloc.plan_id and summ.PERIOD_ID = wsalloc.PERIOD_ID and bud.person_event_id = wsalloc.person_event_id(+) and bud.person_event_id = usage.s2_mgr_person_event_id(+) and bud.pool_id = usage.s2_pool_id(+) and bud.pool_id = pool.pool_id and plan.plan_id = bud.plan_id and xchgRate.plan_id(+) = bud.plan_id and xchgRate.period_id (+)= bud.period_id and xchgRate.currency(+) = FND_GLOBAL.CURRENCY
```

---

[← Back to Index](../7_Compensation_Views_Index.md)
