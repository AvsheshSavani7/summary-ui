OUTSIDE_DATE_CLAUSES = {

    #Concise Summaries

    "Outside Date - Concise": {
        "question": "Contractual Outside Date",
        "conditions": [
            {
                "question": "Contractual Outside Date",
                "if": "termination.outside_date.primary_date.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "outside_date_timing": "{{termination.outside_date.primary_date.answer}}",
                        "extensions_list_answer": "{{termination.extension.extension_list.answer}}",
                        "extensions_list": "{{termination.extension.extension_list.clause_text}}"
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
            "- State the outside date if known, and then summarize any applicable extentions with included timing and reasons.\n"
            "- If an extension is specified (e.g., 'automatically extends for 3 months'), include it as part of the original sentences, exactly as described.\n"
            "- Ensure to summarize all extensions covered by the merger, with the reasons, parties, and timing.\n"
            "- Do not include summaries, explanations, or fallback phrasing like 'cannot be determined'.\n\n"
            "Clause Text:\n"
            "-- Outside Date: {outside_date_timing}\n"
            "-- Extensions List Answer: {extensions_list_answer}\n"
            "-- Extensions List: {extensions_list}\n\n"
            "--- Examples\n"
            "Outside date is September 18, 2025; automatically extends to March 18, 2025 and then June 18, 2025 if any Required Approvals remain outstanding.\n"
            "Outside date is March 23, 2026; automatically extends for 3 months if antitrust review/s remain outstanding."
            "Outside date is January 2, 2020; may be extended twice, by either party, for sixty days if any antitrust condition remains outstanding."

        ),
        "output_field": "consise_standard_summary",
        "reference_fields": [
            "termination.outside_date.primary_date.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 50,
        "summary_display_section": "Regulatory",
        "summary_rank": 4.1,
        "view_prompt": True
    },

    #Fulsome Summaries

    "Outside Date - Fulsome": {
        "question": "Contractual Outside Date",
        "conditions": [
            {
                "question": "Contractual Outside Date",
                "if": "termination.outside_date.primary_date.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "outside_date_timing": "{{termination.outside_date.primary_date.answer}}",
                        "extensions_list_answer": "{{termination.extension.extension_list.answer}}",
                        "extensions_list": "{{termination.extension.extension_list.clause_text}}"
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
            "- State the outside date if known, and then summarize any applicable extentions with included timing and reasons.\n"
            "- If an extension is specified (e.g., 'automatically extends for 3 months'), include it as part of the original sentences, exactly as described.\n"
            "- Ensure to summarize all extensions covered by the merger, with the reasons, parties, and timing.\n"
            "- Do not include summaries, explanations, or fallback phrasing like 'cannot be determined'.\n\n"
            "Clause Text:\n"
            "-- Outside Date: {outside_date_timing}\n"
            "-- Extensions List Answer: {extensions_list_answer}\n"
            "-- Extensions List: {extensions_list}\n\n"
            "--- Examples\n"
            "Outside date is September 18, 2025; automatically extends to March 18, 2025 and then June 18, 2025 if any Required Approvals remain outstanding.\n"
            "Outside date is March 23, 2026; automatically extends for 3 months if antitrust review/s remain outstanding."
            "Outside date is January 2, 2020; may be extended twice, by either party, for sixty days if any antitrust condition remains outstanding."

        ),
        "output_field": "consise_standard_summary",
        "reference_fields": [
            "termination.outside_date.primary_date.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 50,
        "summary_display_section": "Termination",
        "summary_rank": 10.1,
        "view_prompt": True
    },

    "Extension Discretion - Fulsome (not completed)": {
        "question": "Termination Discretion",
        "conditions": [
            {
                "question": "Termination Discretion",
                "if": "termination.outside_date.primary_date.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "outside_date_timing": "{{termination.outside_date.primary_date.clause_text}}",
                        "signing_date": "{{timeline.agreement_signing_date.agreement_signing_date.clause_text}}",
                        "extensions_list": "{{termination.extension.extension_list.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Please create a concise summary detailing how the extension is extended and specify specificaly who has discretion over the extension or stating that no parties have sole discretion.. If the extension is automatic or no party has sole discretion, state that no party has sole discretion over the ability to extend the outside date.\n"
            "- Do not include summaries, explanations, or fallback phrasing like 'cannot be determined'.\n"
            "Clause Text:\n"
            "-- Outside Date Timing: {outside_date_timing}\n"
            "-- Agreement Signing Date = \"{signing_date}\"\n"
            "-- Extensions List: {extensions_list}\n"
        ),
        "output_field": "consise_standard_summary",
        "reference_fields": [
            "termination.outside_date.primary_date.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 40,
        "summary_display_section": "Termination",
        "summary_rank": 10.2,
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
                        "outside_date_timing": "{{termination.outside_date.primary_date.clause_text}}",
                        "signing_date": "{{timeline.agreement_signing_date.agreement_signing_date.clause_text}}",
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
        "summary_type": "Off",
        "format_style": "paragraph",
        "max_words": 40,
        "summary_display_section": "Termination - Outside Date",
        "summary_rank": 5,
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
        "summary_type": "Off",
        "format_style": "paragraph",
        "max_words": 20,
        "summary_display_section": "Termination - Outside Date",
        "summary_rank": 6,
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
        "summary_type": "Off",
        "format_style": "paragraph",
        "max_words": 20,
        "summary_display_section": "Termination - Outside Date",
        "summary_rank": 7,
        "view_prompt": True
    }
}
