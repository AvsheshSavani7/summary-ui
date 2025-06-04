TERMINATION_CLAUSES = {

    "Termination Conditions - Concise": {
        "question": "What are the termination rights and conditions - Concise?",
        "conditions": [
            {
                "question": "Termination Conditions Summary Present?",
                "if": "termination.termination_clause.concise_summary.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "termination_info": "termination.termination_clause.concise_summary.clause_text"
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "termination_info": "The Outside Date for the merger will be automatically extended to January 28, 2024 if the regulatory condition in Section 6.1(b) (or 6.1(c), to the extent related) has not been satisfied by the initial deadline, provided all other closing conditions are met or capable of being met. It will be automatically extended again to July 24, 2024 under the same criteria. Additionally, the Company and Parent may mutually agree in writing to further extend the deadline. Termination rights under Section 7.1(e) are not available to any party whose breach was the principal cause of the failure to close by the applicable deadline."
                    }
                }

            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the termination section of a merger agreement. You are to priorotize thuroughness and not losing details.\n\n"
            "Task:\n"
            "- Identify all of the unique terminations from the information and summarize them in a list chronologically with structured format based on the legnth of extention, trigger for the extension, parties that can enact the extension, and any details relevant to each extension.\n"
            "- Use paragraphs and numbered or bulleted subpoints as appropriate and to ensure a nice easy to read UI.\n\n"
            "- Be thurough and do not miss details, but ensure not to duplicate information"
            "Clause Text:\n"
            "{termination_info}"
        ),
        "output_field": "concise_termination_summary",
        "reference_fields": ["termination.termination_clause.concise_summary.reference_section"],
       
        "use_short_reference": False,
        "summary_type": "Fulsome",
        "format_style": "paragraph_with_bullets",  # You can use this to trigger mixed formatting logic
        "max_words": 300,
        "summary_display_section": "Termination Provisions",
        "summary_display_sub_section": "Termination Provisions",
        "summary_rank": 10,
        "view_prompt": False
    }
}
