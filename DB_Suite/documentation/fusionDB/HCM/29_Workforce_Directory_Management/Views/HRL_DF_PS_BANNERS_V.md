# HRL_DF_PS_BANNERS_V

## Details

**Schema:** FUSION

**Object owner:** HRL

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrldfpsbannersv-6018.html#hrldfpsbannersv-6018](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrldfpsbannersv-6018.html#hrldfpsbannersv-6018)

## Columns

- BANNER_SOURCE
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
- TRACK_PAYLOAD

## Query

```sql
SELECT hdfs.source_code banner_source, hdfs.visibility_code visibility_code, hdfs.display_sequence display_sequence , asg.person_id person_id, asg.assignment_id assignment_id, ban.text_overline text_overline, ban.text_title text_title, ban.text_description text_description, ban.start_date start_date, ban.end_date end_date, ban.bg_img_url bg_img_url, hdfs.link_type link_type, (hdfs.link_text || ban.link_text) link_text, ban.link_label link_label, ban.track_payload track_payload FROM per_all_assignments_f asg, hrl_data_feed_settings_vl hdfs, TABLE ( hrl_df_main.get_banner_details(hdfs.setting_id, asg.person_id, asg.assignment_id) ) ban WHERE trunc(sysdate) BETWEEN asg.effective_start_date AND asg.effective_end_date AND hdfs.flow_code = 'ORA_DF_PS' AND hdfs.section_code = 'ORA_DF_BANNER' AND hdfs.active_flag = 'Y'
```

---

[← Back to Index](../29_Workforce_Directory_Management_Views_Index.md)
