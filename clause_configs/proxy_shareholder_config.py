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
                            "proxy_timing": "proxy_statement.proxy_statement_filing_timing.proxy_statement_filing_timing.clause_text"
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
                "- Identify the exact efforts standard and exact timing standard stated in the clause.\n"
                "- Return as concise a sentence as possible without losing any key details for the timing related to the proxy statement and f4 and who is responsible for each\n"
                "- Do not paraphrase, generalize, or interpret the meaning.\n"
                "- Do not provide examples, commentary, or additional context.\n"
                "- The sentence should begin naturally, and reflect only what is written.\n\n"
                "Clause Text:\n"
                "{proxy_timing}"
            ),
            "output_field": "fulsome_standard_summary",
            
            "reference_fields": ["proxy_statement.proxy_statement_filing_timing.proxy_statement_filing_timing.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 30,
            "summary_display_section": "Proxy and Shareholder Vote Best Efforts ",
            "summary_rank": 1,
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
                            "proxy_efforts": "proxy_statement.f4_effectiveness.f4_effectiveness_efforts.clause_text"
                        }
                    },
                    "false": {
                        "text_output": "Efforts related to the proxy filing has not been detailed"
                    }
                }
            ],
            "prompt_template": (
                "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
                "Task:\n"
                "- Identify the exact efforts standard and exact timing standard stated in the clause.\n"
                "- Return as concise a sentence as possible without losing any key details for the exact efforts stated as related to the f4 and who is responsible for each\n"
                "- Do not paraphrase, generalize, or interpret the meaning.\n"
                "- Do not provide examples, commentary, or additional context.\n"
                "- The sentence should begin naturally, and reflect only what is written.\n\n"
                "Clause Text:\n"
                "{proxy_efforts}"
            ),
            "output_field": "fullsom_standard_summary",
            
            "reference_fields": ["proxy_statement.f4_effectiveness.f4_effectiveness_efforts.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 30,
            "summary_display_section": "Proxy and Shareholder Vote Best Efforts ",
            "summary_rank": 2,
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
                            "shareholder_timing": "proxy_statement.shareholder_meeting.shareholder_meeting_timing.clause_text"
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
                "- Return as concise a sentence as possible without losing any key details for the exact timing requirents as stated related to the shareholder meeting.\n"
                "- Do not paraphrase, generalize, or interpret the meaning.\n"
                "- Do not provide examples, commentary, or additional context.\n"
                "- The sentence should begin naturally, and reflect only what is written.\n\n"
                "Clause Text:\n"
                "{shareholder_timing}"
            ),
            "output_field": "fullsom_standard_summary",
            
            "reference_fields": ["proxy_statement.shareholder_meeting.shareholder_meeting_timing.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 30,
            "summary_display_section": "Proxy and Shareholder Vote Best Efforts ",
            "summary_rank": 3,
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