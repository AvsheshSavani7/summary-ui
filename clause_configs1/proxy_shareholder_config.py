PROXY_SHAREHOLDER_CLAUSES = {

    #FULSOME_PROXY_SHAREHOLDER
        "Filing Timing - Fulsome": {
            "question": "What are the timing requirements for the Proxy and F-4",
            "conditions": [
                {
                    "question": "What are the timing requirements for the Proxy and F-4",
                    "if": "proxy_statement.proxy_statement_filing_timing.proxy_statement_filing_timing.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "proxy_timing": "{{proxy_statement.proxy_statement_filing_timing.proxy_statement_filing_timing.clause_text}}"
                        }
                    },
                    "false": {
                        "text_output": "Timing related to the proxy filing has not been detailed"
                    }
                }
            ],
            "prompt_template": (
                "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
                "Task:\n"
                "- Identify the exact timing requirements as they apply to the Proxy and F-4.\n"
                "- Return as concise a sentence as possible without losing any key details for the timing related to the proxy statement and f4 and who is responsible for each\n"
                "- Do not paraphrase, generalize, or interpret the meaning.\n"
                "- Do not provide examples, commentary, or additional context.\n"
                "- The sentence should begin naturally, and reflect only what is written.\n\n"
                "Clause Text:\n"
                "{proxy_timing}"
                "--- Examples\n"
                "As promptly as practicable, the parties shall jointly prepare and file the Joint Proxy Statement/Prospectus in preliminary form and Parent shall prepare and file a Registration Statement on Form F-4."
                "As promptly as reasonably practicable and within 25 Business Days, Company shall file the preliminary Proxy Statement."
                "As promptly as reasonably practicable, Company shall prepare and file the Proxy Statement and Parent shall prepare and file a registration statement on Form F-4."
            ),
            "output_field": "fulsome_standard_summary",
            
            "reference_fields": ["proxy_statement.proxy_statement_filing_timing.proxy_statement_filing_timing.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 30,
            "summary_display_section": "Proxy, Shareholder Vote, Dissenting Shares",
            "summary_rank": 6.1,
            "view_prompt": True
        },

        "Effectiveness Efforts - Fulsome": {
            "question": "What are the efforts required for the F-4",
            "conditions": [
                {
                    "question": "What are the efforts required for the F-4",
                    "if": "proxy_statement.f4_effectiveness.f4_effectiveness_efforts.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "proxy_efforts": "{{proxy_statement.f4_effectiveness.f4_effectiveness_efforts.clause_text}}",
                            "proxy_timing": "{{proxy_statement.f4_effectiveness.f4_effectiveness_target_date.answer}}",
                            "proxy_timing_text": "{{proxy_statement.f4_effectiveness.f4_effectiveness_target_date.clause_text}}"
                        }
                    },
                    "false": {
                        "text_output": ""
                    }
                }
            ],
            "prompt_template": (
                "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
                "Task:\n"
                "- Identify the exact efforts standard and exact timing deadlines stated in the clause as they relate to the proxy statement.\n"
                "- Return as concise a sentence as possible without losing any key details for the exact efforts stated as related to the f4 and who is responsible for each.\n"
                "- Do not paraphrase, generalize, or interpret the meaning.\n"
                "- Do not provide examples, commentary, or additional context.\n"
                "- The sentence should begin naturally, and reflect only what is written.\n\n"
                "--- Detailed Information"
                "--- F4 Filing Efforts:\n"
                "{proxy_efforts}\n"
                "--- F4 Target Date\n"
                "{proxy_timing}\n"
                "--- F4 Target Date Clause Text:\n"
                "{proxy_timing_text}\n"
                "--- Examples\n"
                "Parties shall use reasonable best efforts to have the Joint Proxy Statement/Prospectus cleared by the SEC as promptly as practicable after its filing, and Parent shall use reasonable best efforts to have the Registration Statement declared effective as promptly as practicable after its filing.\n"
                "Company shall use reasonable best efforts to respond to SEC comments and cause the definitive Proxy Statement to be mailed as promptly as practicable (and within 10 Business Days) after being cleared by the SEC.\n"
                "Parties shall use reasonable best efforts to have the Form F-4 declared effective as promptly as practicable after such filing.\n"
            ),
            "output_field": "fullsom_standard_summary",
            
            "reference_fields": ["proxy_statement.f4_effectiveness.f4_effectiveness_efforts.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 30,
            "summary_display_section": "Proxy, Shareholder Vote, Dissenting Shares",
            "summary_rank": 6.2,
            "view_prompt": True
        },

        "Shareholder Meeting - Fulsome": {
            "question": "Shareholder Meeting Timeframe",
            "conditions": [
                {
                    "question": "Shareholder Meeting Timeframe",
                    "if": "proxy_statement.shareholder_meeting.shareholder_meeting_timing.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "shareholder_timing_answer": "{{proxy_statement.shareholder_meeting.shareholder_meeting_timing.answer}}",
                            "shareholder_timing_text": "{{proxy_statement.shareholder_meeting.shareholder_meeting_timing.clause_text}}",
                            "shareholder_deadline_answer": "{{proxy_statement.shareholder_meeting.shareholder_meeting_deadline.answer}}",
                            "shareholder_dealibne_text": "{{proxy_statement.shareholder_meeting.shareholder_meeting_deadline.clause_text}}"
                        }
                    },
                    "false": {
                        "text_output": ""
                    }
                }
            ],
            "prompt_template": (
                "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
                "Task:\n"
                "- Identify the timing requirements for the target shareholder vote.\n"
                "- Return as concise a sentence as possible without losing any key details for the exact timing requirents as stated related to the shareholder meeting.\n"
                "- Do not paraphrase, generalize, or interpret the meaning.\n"
                "- Do not provide examples, commentary, or additional context.\n"
                "- The sentence should begin naturally, and reflect only what is written.\n\n"
                "--- Shareholder Timing Answer:\n"
                "{shareholder_timing_answer}\n"
                "--- Shareholder Timing Text:\n"
                "{shareholder_timing_text}\n"
                "--- Shareholder Timing Dealine Answer:\n"
                "{shareholder_deadline_answer}\n"
                "--- Shareholder Timing Deadline Text:\n"
                "{shareholder_dealibne_text}\n"
                "-- Examples\n"
                "Promptly following the effectiveness of the Registration Statement (and within 40 days of the Company Record Date), Company shall hold the Company Stockholder Meeting.  Company may adjourn or postpone the Company Stockholder Meeting without the prior written consent of Parent to allow additional time to solicit proxies to obtain the Company Stockholder Approval or for an absence of a quorum, provided that Company may not, without the prior written consent of Parent, postpone the meeting more than three times for a period exceeding ten Business Days.\n"
                "Company shall hold its shareholder vote within 45 days following the mailing of the Proxy Statement\n"
                "Company shall hold the Company Stockholder Meeting within 50 days of the effectiveness of the Form F-4."
            ),
            "output_field": "fullsom_standard_summary",
            
            "reference_fields": ["proxy_statement.shareholder_meeting.shareholder_meeting_timing.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 30,
            "summary_display_section": "Proxy, Shareholder Vote, Dissenting Shares",
            "summary_rank": 6.3,
            "view_prompt": True
        },

        "Reaching a Quarum - Fulsome": {
            "question": "Shareholder Meeting Timeframe",
            "conditions": [
                {
                    "question": "Shareholder Meeting Timeframe",
                    "if": "proxy_statement.quorum_or_vote_failure.quorum_or_vote_failure_handling.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "shareholder_meeting_handling": "proxy_statement.quorum_or_vote_failure.quorum_or_vote_failure_handling.clause_text", 
                            "shareholder_meeting_deadline": "proxy_statement.quorum_or_vote_failure.quorum_or_vote_failure_deadline.clause_text"
                        }
                    },
                    "false": {
                        "text_output": "Timing related to the shareholder meeting has not been detailed"
                    }
                }
            ],
            "prompt_template": (
                "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
                "Task:\n"
                "- Identify the exact efforts standard and exact timing standard stated in the clause.\n"
                "- Return 1 paragraph without losing any key details the exact details required to reaching a quarum and any potential timing requirements, adjurnemtns or postponements. Please also note anythign related to record date shoudl that be applicable.\n"
                "- Do not paraphrase, generalize, or interpret the meaning.\n"
                "- Do not provide examples, commentary, or additional context.\n"
                "- The paragraph should begin naturally, and reflect only what is written.\n\n"
                "Clause Text:\n"
                "{shareholder_meeting_handling}\n\n"
                "{shareholder_meeting_deadline}"
            ),
            "output_field": "fullsom_standard_summary",
            
            "reference_fields": ["proxy_statement.quorum_or_vote_failure.quorum_or_vote_failure_handling.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 50,
            "summary_display_section": "Proxy and Shareholder Vote Best Efforts ",
            "summary_rank": 4,
            "view_prompt": True
        }
}      