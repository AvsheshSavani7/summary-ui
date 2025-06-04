OUTSIDE_DATE_CLAUSES = {

    "Outside Date - Concise": {
        "question": "Contractual Outside Date",
        "conditions": [
            {
                "question": "Contractual Outside Date",
                "if": "termination.outside_date.primary_date.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "outside_date_timing": "termination.outside_date.primary_date.clause_text",
                        "signing_date": "timeline.agreement_signing_date.agreement_signing_date.clause_text",
                        "extensions_list": "termination.extension.extension_list.clause_text"
                    }
                },
                "false": {
                    "text_output": "Outside date was not specified in the agreement"
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Use the Signing Date below to compute the exact Outside Date if the clause states a number of months or days from that date.\n"
            "- If a specific calendar date is provided, extract and return it directly.\n"
            "- If an extension is specified (e.g., 'automatically extends for 3 months'), include it on a second line, exactly as described.\n"
            "- Do not include summaries, explanations, or fallback phrasing like 'cannot be determined'.\n"
            "- If no date can be calculated or extracted, return nothing.\n"
            "- Format: 'Outside Date = Month DD, YYYY' on one line. Optional extension logic on the next line.\n\n"
            "Clause Text:\n"
            "-- {outside_date_timing}\n"
            "-- Agreement Signing Date = \"{signing_date}\"\n"
            "-- {extensions_list}\n"
        ),
        "output_field": "consise_standard_summary",
        "reference_fields": [
            "termination.outside_date.primary_date.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 20,
        "summary_display_section": "Termination - Outside Date",
        "summary_display_sub_section": "Termination - Outside Date",
        "summary_rank": 10,
        "view_prompt": True
    },

    "Outside Date - Fulsome": {
        "question": "Contractual Outside Date",
        "conditions": [
            {
                "question": "Contractual Outside Date",
                "if": "termination.outside_date.primary_date.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "outside_date_timing": "termination.outside_date.primary_date.clause_text",
                        "signing_date": "timeline.agreement_signing_date.agreement_signing_date.clause_text",
                        "extensions_list": "termination.extension.extension_list.clause_text"
                    }
                },
                "false": {
                    "text_output": "Outside date was not specified in the agreement"
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Use the Signing Date below to compute the exact Outside Date if the clause states a number of months or days from that date.\n"
            "- If a specific calendar date is provided, extract and return it directly.\n"
            "- If an extension is specified (e.g., 'automatically extends for 3 months'), include it on a second line, exactly as described.\n"
            "- Include details related to the termination, what it is contingent on and any other critical details"
            "- Do not include summaries, explanations, or fallback phrasing like 'cannot be determined'.\n"
            "- If no date can be calculated or extracted, return nothing.\n"
            "- Format: 'Outside Date = Month DD, YYYY' on one line. Optional extension logic on the next line.\n\n"
            "Clause Text:\n"
            "-- {outside_date_timing}\n"
            "-- Agreement Signing Date = \"{signing_date}\"\n"
            "-- {extensions_list}\n"
        ),
        "output_field": "consise_standard_summary",
        "reference_fields": [
            "termination.outside_date.primary_date.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 40,
        "summary_display_section": "Termination - Outside Date",
        "summary_display_sub_section": "Termination - Outside Date",
        "summary_rank": 10,
        "view_prompt": True
    },

    "Extension Discretion - Fulsome": {
        "question": "Termination Discretion",
        "conditions": [
            {
                "question": "Termination Discretion",
                "if": "termination.outside_date.primary_date.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "outside_date_timing": "termination.outside_date.primary_date.clause_text",
                        "signing_date": "timeline.agreement_signing_date.agreement_signing_date.clause_text",
                        "extensions_list": "termination.extension.extension_list.clause_text"
                    }
                },
                "false": {
                    "text_output": "Outside date was not specified in the agreement"
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Please create a concise summary detailing how the extension is extended and specify specificaly who has discretion over the extension or stating that no parties have sole discretion.. If the extension is automatic or no party has sole discretion, state that no party has sole discretion over the ability to extend the outside date.\n"
            "- Do not include summaries, explanations, or fallback phrasing like 'cannot be determined'.\n"
            "Clause Text:\n"
            "-- {outside_date_timing}\n"
            "-- Agreement Signing Date = \"{signing_date}\"\n"
            "-- {extensions_list}\n"
        ),
        "output_field": "consise_standard_summary",
        "reference_fields": [
            "termination.outside_date.primary_date.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 40,
        "summary_display_section": "Termination - Outside Date",
        "summary_display_sub_section": "Extension Discretion",
        "summary_rank": 10,
        "view_prompt": True
    },

    "Extension Discretion Breach - Fulsome": {
        "question": "Termination Discretion Breach",
        "conditions": [
            {
                "question": "Termination Discretion Breach",
                "if": "termination.outside_date.primary_date.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "outside_date_timing": "termination.outside_date.primary_date.clause_text",
                        "signing_date": "timeline.agreement_signing_date.agreement_signing_date.clause_text",
                        "extensions_list": "termination.extension.extension_list.clause_text"
                    }
                },
                "false": {
                    "text_output": "Outside date was not specified in the agreement"
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Please create a concise summary detailing each party's ability to terminate the agreement by Termination Date given a material breach by that party which caused missing the outside date.\n"
            "- DO NOT specify or summarize extension details or outside date details realted to dates or timing.\n"
            "- Do not include summaries, explanations, or fallback phrasing like 'cannot be determined'.\n"
            "Clause Text:\n"
            "-- {outside_date_timing}\n"
            "-- Agreement Signing Date = \"{signing_date}\"\n"
            "-- {extensions_list}\n"
            "--- Example Output\n"
            "--- The ability to terminate the Agreement by the Termination Date shall not be available to any party if a material breach by such party has been the principal cause of the failure to close by the outside date.\n"
        ),
        "output_field": "consise_standard_summary",
        "reference_fields": [
            "termination.outside_date.primary_date.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 40,
        "summary_display_section": "Termination - Outside Date",
        "summary_display_sub_section": "Extension Discretion Breach",
        "summary_rank": 10,
        "view_prompt": True
    },

    "Termination Fee - Fulsome": {
        "question": "What is the Termination Fee",
        "conditions": [
            {
                "question": "What is the Termination Fee",
                "if": "termination.termination_fee.termination_fee.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "termination_fee": "termination.termination_fee.termination_fee.clause_text",
                    }
                },
                "false": {
                    "text_output": "Termination Fee Amount not Specified"
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- State the termination fee.\n"
            "- Do not include summaries, explanations, or fallback phrasing like 'cannot be determined'.\n"
            "Clause Text:\n"
            "-- {termination_fee}\n"

        ),
        "output_field": "consise_standard_summary",
        "reference_fields": [
            "termination.termination_fee.termination_fee.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 20,
        "summary_display_section": "Termination - Outside Date",
        "summary_display_sub_section": "Termination Fee",
        "summary_rank": 10,
        "view_prompt": True
    },

    "Reverse Termination Fee - Fulsome": {
        "question": "What is the Reverse Termination Fee",
        "conditions": [
            {
                "question": "What is the Reverse Termination Fee",
                "if": "termination.reverse_termination_fee.reverse_termination_fee.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "reverse_termination_fee": "termination.reverse_termination_fee.reverse_termination_fee.clause_text",
                    }
                },
                "false": {
                    "text_output": "Reverse Termination Fee date was not specified in the agreement"
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- State the Reverse Termination fee.\n"
            "- Do not include summaries, explanations, or fallback phrasing like 'cannot be determined'.\n"
            "Clause Text:\n"
            "-- {reverse_termination_fee}\n"
        ),
        "output_field": "consise_standard_summary",
        "reference_fields": [
            "termination.reverse_termination_fee.reverse_termination_fee.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 20,
        "summary_display_section": "Termination - Outside Date",
        "summary_display_sub_section": "Reverse Termination Fee",
        "summary_rank": 10,
        "view_prompt": True
    }
}
