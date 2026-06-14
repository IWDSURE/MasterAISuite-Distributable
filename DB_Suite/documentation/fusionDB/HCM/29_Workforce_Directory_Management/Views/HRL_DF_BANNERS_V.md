# HRL_DF_BANNERS_V

## Details

**Schema:** FUSION

**Object owner:** HRL

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrldfbannersv-8205.html#hrldfbannersv-8205](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrldfbannersv-8205.html#hrldfbannersv-8205)

## Columns

- FLOW_CODE
- BANNER_SOURCE
- CATEGORY_CODE
- VISIBILITY_CODE
- DISPLAY_SEQUENCE
- PERSON_ID
- ASSIGNMENT_ID
- TEXT_OVERLINE
- TEXT_TITLE
- TEXT_DESCRIPTION
- START_DATE
- END_DATE
- BG_IMG_URL
- LINK_TYPE
- LINK_TEXT
- LINK_LABEL
- LINK2_TYPE
- LINK2_TEXT
- LINK2_LABEL
- TRACK_PAYLOAD

## Query

```sql
SELECT /*+ LEADING(asg hdfs ban) */ hdfs.flow_code flow_code, hdfs.source_code banner_source, hdfs.category_code category_code , hdfs.visibility_code visibility_code, hdfs.display_sequence display_sequence , asg.person_id person_id, asg.assignment_id assignment_id, ban.text_overline text_overline, ban.text_title text_title, ban.text_description text_description, ban.start_date start_date, ban.end_date end_date, ban.bg_img_url bg_img_url, ban.link_type link_type, (hdfs.link_text || ban.link_text) link_text, ban.link_label link_label, ban.link2_type link2_type, ban.link2_text link2_text, ban.link2_label link2_label, ban.track_payload track_payload FROM per_all_assignments_f asg, hrl_data_feed_settings_vl hdfs, TABLE ( hrl_df_main.get_banner_details(hdfs.setting_id, asg.person_id, asg.assignment_id) ) ban WHERE trunc(sysdate) BETWEEN asg.effective_start_date AND asg.effective_end_date AND hdfs.section_code = 'ORA_DF_BANNER' AND hdfs.active_flag = 'Y' AND ((hdfs.visibility_code = 'SELF' and asg.person_id = NVL(HRC_SESSION_UTIL.GET_USER_PERSONID,-1)) OR (hdfs.visibility_code = 'MGR' and exists (select 1 from per_manager_hrchy_dn where manager_id = NVL(HRC_SESSION_UTIL.GET_USER_PERSONID,-1) and person_id = asg.person_id and trunc(sysdate) between effective_start_date and effective_end_date and manager_type = 'LINE_MANAGER')) )
```

---

[← Back to Index](../29_Workforce_Directory_Management_Views_Index.md)
