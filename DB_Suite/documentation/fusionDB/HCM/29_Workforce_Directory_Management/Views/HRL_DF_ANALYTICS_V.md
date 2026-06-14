# HRL_DF_ANALYTICS_V

## Details

**Schema:** FUSION

**Object owner:** HRL

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrldfanalyticsv-7718.html#hrldfanalyticsv-7718](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrldfanalyticsv-7718.html#hrldfanalyticsv-7718)

## Columns

- FLOW_CODE
- ANALYTIC_SOURCE
- CATEGORY_CODE
- VISIBILITY_CODE
- DISPLAY_SEQUENCE
- PERSON_ID
- ASSIGNMENT_ID
- TEXT_TITLE
- TEXT_METRIC
- TEXT_META
- BADGE_TEXT
- BADGE_STATUS
- PERIOD_CHN_IND_VAL
- PERIOD_CHN_IND_CMP
- CHART_TYPE
- CHART_COLOR
- CHART_DATA
- LINK_TYPE
- LINK_TEXT

## Query

```sql
SELECT /*+ LEADING(asg hdfs ana) */ hdfs.flow_code flow_code, hdfs.source_code analytic_source, hdfs.category_code category_code , hdfs.visibility_code visibility_code , hdfs.display_sequence display_sequence , asg.person_id person_id, asg.assignment_id assignment_id, ana.text_title text_title, ana.text_metric text_metric, ana.text_meta text_meta, ana.badge_text badge_text, ana.badge_status badge_status, ana.period_chn_ind_val period_chn_ind_val, ana.period_chn_ind_cmp period_chn_ind_cmp, ana.chart_type chart_type, ana.chart_color chart_color, ana.chart_data chart_data, hdfs.link_type link_type, ( hdfs.link_text || ana.link_text) link_text FROM per_all_assignments_f asg, hrl_data_feed_settings_vl hdfs, TABLE ( hrl_df_main.get_analytic_details(hdfs.setting_id, asg.person_id, asg.assignment_id) ) ana WHERE trunc(sysdate) BETWEEN asg.effective_start_date AND asg.effective_end_date AND hdfs.section_code = 'ORA_DF_ANALYTIC' AND hdfs.active_flag = 'Y' AND ((hdfs.visibility_code IN ('SELF','TEAM') and asg.person_id = NVL(HRC_SESSION_UTIL.GET_USER_PERSONID,-1)) OR (hdfs.visibility_code IN ('MGR','TEAM') and exists (select 1 from per_manager_hrchy_dn where manager_id = NVL(HRC_SESSION_UTIL.GET_USER_PERSONID,-1) and person_id = asg.person_id and trunc(sysdate) between effective_start_date and effective_end_date and manager_type = 'LINE_MANAGER')) )
```

---

[← Back to Index](../29_Workforce_Directory_Management_Views_Index.md)
