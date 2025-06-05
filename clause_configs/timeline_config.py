TIMELINE_CLAUSES = {

    "Timeline - Fulsome": {
        "question": "What are the critical timeline items from the deal",
        "conditions": [
            {
                "question": "What are the critical timeline items from the deal",
                "if": "timeline.agreement_signing_date.agreement_signing_date.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "timeline_info_signing_date": "timeline.agreement_signing_date.agreement_signing_date.clause_text",
                        "timeline_info_confidentiality_date": "timeline.confidentiality_agreement_signing_date.confidentiality_agreement_signing_date.clause_text",
                        "timeline_info_announcement_date": "timeline.announcement_date.announcement_date.clause_text",
                        "timeline_info_proxy_filing_date": "timeline.proxy_filing_deadline.proxy_filing_deadline.clause_text",
                        "timeline_info_shareholder_vote_date": "timeline.shareholder_vote_deadline.shareholder_vote_deadline.clause_text",
                        "timeline_info_outside_date_date": "timeline.outside_date.outside_date.clause_text",
                        "timeline_info_hsr_filing_date": "timeline.hsr_filing_deadline.hsr_filing_deadline.clause_text",
                        "timeline_info_second_request_date": "timeline.second_request_deadline.second_request_deadline.clause_text",
                        "timeline_info_cfius_date": "timeline.cfius_filing_deadline.cfius_filing_deadline.clause_text",
                        "timeline_info_regulatory_outside_date": "timeline.regulatory_approval_outside_date.regulatory_approval_outside_date.clause_text",
                        "timeline_info_termination_rights_trigger_date": "timeline.termination_rights_trigger_dates.termination_rights_trigger_dates.clause_text",
                        "timeline_info_marketing_period_date": "timeline.marketing_period_dates.marketing_period_dates.clause_text",
                        "timeline_info_inside_data_date": "timeline.inside_date.inside_date.clause_text",
                        "timeline_info_closing_date": "timeline.closing_date.closing_date.clause_text",
                        "timeline_info_conditions_end_date": "conditions_satisfaction_end_date.conditions_satisfaction_end_date.clause_text"
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "termination_info": "No Timeline details have been disclosed as part of the merger"
                    }
                }

            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the timeline items of a merger agreement.\n\n"
            "Task:\n"
            "- For each individual included Clause Text item, identify if there is an exact date that is specified or can be calculated (from a prior known date). "
            "If it is x days from an unknown exact date, then it cannot be known and should not be included. "
            "If it is an exact number of days from a known date, then include the logic and the calculated date.\n"
            "- Create a list of all exact or calculated dates. If an exact date is not stated or cannot be calculated then skip and do not include.\n"
            "- For any included dates use the format XXXXXX Date = and then the stated or calculated date.\n"
            "- Create the list chronologically from earliest to latest with 1 item per line.\n\n"
            "Clause Text:\n"
            "-- Signing Date = \"{timeline_info_signing_date}\"\n"
            "-- Confidentiality Sign Date = \"{timeline_info_confidentiality_date}\"\n"
            "-- Announcement Date = \"{timeline_info_announcement_date}\"\n"
            "-- Proxy Filing Date = \"{timeline_info_proxy_filing_date}\"\n"
            "-- Sharreholder Vote Date = \"{timeline_info_shareholder_vote_date}\"\n"
            "-- Outside Date = \"{timeline_info_outside_date_date}\"\n"
            "-- HSR Filing Date = \"{timeline_info_hsr_filing_date}\"\n"
            "-- Second Request Date = \"{timeline_info_second_request_date}\"\n"
            "-- CFIUS Date = \"{timeline_info_cfius_date}\"\n"
            "-- Regulatory Outside Date = \"{timeline_info_regulatory_outside_date}\"\n"
            "-- Termination Trigger Date = \"{timeline_info_termination_rights_trigger_date}\"\n"
            "-- Marketing Period Date = \"{timeline_info_marketing_period_date}\"\n"
            "-- Inside Date = \"{timeline_info_inside_data_date}\"\n"
            "-- Closing Date = \"{timeline_info_closing_date}\"\n"
            "-- Conditions End Date = \"{timeline_info_conditions_end_date}\"\n"


        ),
        "output_field": "fulsome_termination_summary",
        "reference_fields": ["termination.termination_clause.concise_summary.reference_section"],
       
        "use_short_reference": False,
        "summary_type": "Fulsome",
        "format_style": "List with no bullets",  # You can use this to trigger mixed formatting logic
        "max_words": 300,
        "summary_display_section": "Termination Provisions",
        "summary_rank": 1,
        "view_prompt": True
    }
}