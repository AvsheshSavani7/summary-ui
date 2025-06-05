SPECIFIC_PERFORMANCE_CLAUSES = {

    "Specific Performance - Concise": {
        "question": "Does the Contract Contain Specific Performance",
        "conditions": [
            {
                "question": "Does the Contract Contain Specific Performance",
                "if": "specific_performance.specific_performance.specific_performance_available.answer",
                "type": "boolean",
                "true": {
                        "add_to_prompt": {
                            "specific_performance": "specific_performance.specific_performance.specific_performance_available.clause_text"
                        }
                    },
                "false": {
                    "text_output": "Parties are not entitled to specific performance."
                }
            }
        ],
        "prompt_template": (
            "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Identify whether specific performance is available per the contract and the exact parties involved.\n"
            "- Return as concise a sentence as possible without losing any key details for whether specific performance is available and for which parties.\n"
            "- Do not paraphrase, generalize, or interpret the meaning.\n"
            "- Do not provide examples, commentary, or additional context.\n"
            "- The sentence should begin naturally, and reflect only what is written.\n\n"
            "Clause Text:\n"
            "{specific_performance}"
        ),
        "output_field": "fulsome_standard_summary",
        "reference_fields": [
            "specific_performance.specific_performance.specific_performance_available.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 20,
        "summary_display_section": "Specific Performance",
        "summary_display_sub_section": "Specific Performance",
        "summary_rank": 13,
        "view_prompt": True
    },

    "Specific Performance - Fulsome": {
        "question": "Does the Contract Contain Specific Performance",
        "conditions": [
            {
                "question": "Does the Contract Contain Specific Performance",
                "if": "specific_performance.specific_performance.specific_performance_available.answer",
                "type": "boolean",
                "true": {
                        "add_to_prompt": {
                            "specific_performance_available": "specific_performance.specific_performance.specific_performance_available.clause_text",
                            "specific_performance_limitations": "specific_performance.specific_performance.specific_performance_limitations.clause_text"
                        }
                    },
                "false": {
                    "text_output": "Parties are not entitled to specific performance."
                }
            }
        ],
        "prompt_template": (
            "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Identify whether specific performance is available per the contract and the exact parties involved.\n"
            "- Return 1 sentence without losing any key details for whether specific performance is available and for which parties.\n"
            "- Do not paraphrase, generalize, or interpret the meaning.\n"
            "- Do not provide examples, commentary, or additional context.\n"
            "- The sentence should begin naturally, and reflect only what is written.\n\n"
            "Clause Text:\n"
            "{specific_performance_available}\n"
            "{specific_performance_limitations}\n"
        ),
        "output_field": "fulsome_standard_summary",
        "reference_fields": [
            "specific_performance.specific_performance.specific_performance_available.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 30,
        "summary_display_section": "Specific Performance",
        "summary_display_sub_section": "Specific Performance",
        "summary_rank": 13,
        "view_prompt": True
    },

    "Specific Performance Financing - Fulsome": {
        "question": "Are there limitations from financing on Specific Performance",
        "conditions": [
            {
                "question": "Are there limitations from financing on Specific Performance",
                "if": "specific_performance.specific_performance.specific_performance_financing_condition.answer",
                "type": "boolean",
                "true": {
                        "add_to_prompt": {
                            "specific_performance_financing": "specific_performance.specific_performance.specific_performance_financing_condition.clause_text"
                        }
                    },
                "false": {
                    "text_output": "There are no mentioned limitions on Specific Performance related to the availability of debt or equity financing"
                }
            }
        ],
        "prompt_template": (
            "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Identify whether specific performance is limited by debt or equity financing being secured.\n"
            "- Return a concise response without losing any key details for whether specific performance is limited by debt or equity financing being secured.\n"
            "- Do not paraphrase, generalize, or interpret the meaning.\n"
            "- Do not provide examples, commentary, or additional context.\n"
            "- The sentence should begin naturally, and reflect only what is written.\n\n"
            "Clause Text:\n"
            "{specific_performance_financing}"
        ),
        "output_field": "fulsome_standard_summary",
        "reference_fields": [
            "specific_performance.specific_performance.specific_performance_financing_condition.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 30,
        "summary_display_section": "Specific Performance",
        "summary_display_sub_section": "Financing",
        "summary_rank": 13,
        "view_prompt": True
    }

}
