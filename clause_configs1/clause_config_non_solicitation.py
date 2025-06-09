# =========================
# Test Config & Data
# =========================
CLAUSE_CONFIG = {
    "THIS IS A TEST New": {
        "question": "Does the agreement include a match right clause?",
        "conditions": [
            {
                "question": "Is a match right clause included?",
                "if": "non_solicitation.match_right_clause.match_right_initial_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "match_clause": "The Company must notify the Parent and provide a three-day window to match any Superior Proposal."
                    },
                    "add_references": ["non_solicitation.match_right_clause.match_right_initial_included.reference_section"]
                },
                "false": {
                    "text_output": "No match right clause is included in the agreement."
                }
            }
           
            
        ],
        "prompt_template": (
            "Summarize the match right obligations under the agreement:\n\n"
            "- Clause Text: {match_clause}"
        ),
        "output_field": "match_right_summary",
        "reference_fields": [
        "non_solicitation.match_right_clause.match_right_initial.match_right_initial_included.reference_section"
        ],

        "use_short_reference": True,
        "summary_type": "concise",
        "format_style": "paragraph",
        "max_words": 100,
        "summary_display_section": "Non-Solicitation Terms",
        "summary_rank": 1,
        "view_prompt": True
    },

    # Example 2 – Enum Check
    "Go Shop - Enum": {
        "question": "What kind of go shop clause is included?",
        "conditions": [
            {
                "question": "Type of go shop clause?",
                "if": "non_solicitation.go_shop_clause.go_shop_type.answer",
                "type": "enum",
                "value": "broad",
                "true": {
                    "add_to_prompt": {
                        "go_shop_clause": "The Company has broad rights to solicit alternate proposals."
                    }
                },
                "false": {
                    "text_output": "A go shop clause is not broadly permitted."
                }
            }
        ],
        "prompt_template": "Summarize the nature of the go shop rights:\n\n- Details: {go_shop_clause}",
        "output_field": "go_shop_summary",
        "reference_fields": ["non_solicitation.go_shop_clause.reference_section"],
        "use_short_reference": True,
        "summary_type": "concise",
        "format_style": "bullet",
        "max_words": 50,
        "summary_display_section": "Non-Solicitation Terms",
        "summary_rank": 2,
        "view_prompt": True
    },

    # Example 3 – Numeric Comparison
    "Termination Fee Ratio": {
        "question": "Is the termination fee higher than 3%?",
        "conditions": [
            {
                "question": "Fee ratio threshold",
                "if": "termination.termination_fee.ratio.answer",
                "type": "number",
                "comparator": ">",
                "compare_to": 0.03,
                "true": {
                    "add_to_prompt": {
                        "fee_ratio_clause": "The termination fee exceeds 3% of deal equity value."
                    }
                },
                "false": {
                    "text_output": "Termination fee is within standard threshold."
                }
            }
        ],
        "prompt_template": "Summarize the implications of the termination fee ratio:\n\n- Info: {fee_ratio_clause}",
        "output_field": "termination_fee_summary",
        "reference_fields": ["termination.termination_fee.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words": 100,
        "summary_display_section": "Termination Provisions",
        "summary_rank": 3,
        "view_prompt": True
    },

    # Example 4 – Non-empty Check
    "Financing Sources Disclosure": {
        "question": "Does the agreement disclose financing sources?",
        "conditions": [
            {
                "question": "Presence of disclosure",
                "if": "financing.financing_sources.disclosure_text",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "financing_info": "The agreement lists the committed financing sources for the transaction."
                    }
                },
                "false": {
                    "text_output": "Financing sources are not disclosed in the agreement."
                }
            }
        ],
        "prompt_template": "Explain whether financing sources are disclosed:\n\n- Disclosure: {financing_info}",
        "output_field": "financing_sources_summary",
        "reference_fields": ["financing.financing_sources.reference_section"],
        "use_short_reference": True,
        "summary_type": "concise",
        "format_style": "bullet",
        "max_words": 75,
        "summary_display_section": "Financing Terms",
        "summary_rank": 4,
        "view_prompt": True
    },

    # Example 5 – Fallback Path
    "Divestiture Cap Presence": {
        "question": "Is a divestiture cap specified?",
        "conditions": [
            {
                "question": "Presence of cap",
                "if": "regulatory.divestiture.divestiture_cap.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "divestiture_cap": "The agreement caps divestiture obligations at a specified threshold."
                    }
                },
                "false": {
                    "text_output": "The agreement does not specify a divestiture cap."
                },
                "default": {
                    "text_output": "No information about divestiture cap found."
                }
            }
        ],
        "prompt_template": "Explain any divestiture cap obligations:\n\n- Terms: {divestiture_cap}",
        "output_field": "divestiture_cap_summary",
        "reference_fields": ["regulatory.divestiture.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words": 90,
        "summary_display_section": "Regulatory Terms",
        "summary_rank": 5,
        "view_prompt": True
    }
}
print("Config file loaded with clauses:", list(CLAUSE_CONFIG.keys()))