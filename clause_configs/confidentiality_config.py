CONFIDENTIALITY_CLAUSES = {
    "Confidentiality and Clean Room - Concise": {
        "question": "Confidentiality and Clean Room - Concise?",
        "conditions": [
            {
                "question": "Confidentiality and Clean Room - Concise",
                "if": "confidentiality_and_clean_room.confidentiality.confidentiality_exists.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "confidentiality": "{{confidentiality_and_clean_room.confidentiality.confidentiality_exists.clause_text}}",
                        "clean_room": "{{confidentiality_and_clean_room.clean_room.clean_room_signing_date.clause_text}}"
                    }
                },
                "false": {
                    "text_output": "No confidentiality sign date was found in the agreement"
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the confidentiality signing for a merger agreement.\n\n"
            "Task:\n"
            "- Return a single sentence.\n"
            "- Start exactly with the phrase: 'Confidentiality Agreement dated'.\n"
            "- If applicable, continue the sentence with any clean room agreement detail (e.g., 'and supplemented by a Clean Team Agreement dated...').\n"
            "- Do not include any additional context or parties (e.g., 'between the Parent and the Company').\n\n"
            "-- You are reviewing the following two clauses:\n"
            "1. Confidentiality Agreement Clause: {confidentiality}\n"
            "2. Clean Room / Clean Team Agreement Clause: {clean_room}\n\n"
            "--- Examples:\n"
            "Confidentiality Agreement dated November 23, 2018.\n"
            "Confidentiality Agreement dated August 29, 2023 and supplemented by a Clean Team Agreement dated October 11, 2023.\n"
            "Confidentiality Agreement dated January 23, 2025.\n"
        ),
        "output_field": "confidentiality_summary",
        "reference_fields": ["confidentiality_and_clean_room.confidentiality.confidentiality_exists.reference_section"],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 20,
        "summary_display_section": "Presigning",
        "summary_rank": 1,
        "view_prompt": True
    }
}
