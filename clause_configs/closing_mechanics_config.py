CLOSING_MECHANICS_CLAUSES = {
   

    # Fulsome Closing Mechanics

    "Target Closing": {
        "question": "Does the agreement include a closing date?",
        "conditions": [
            {
                "question": "Is a closing date included?",
                "if": "closing_mechanics.target_date.target_date.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "closing_date": "{{closing_mechanics.target_date.target_date.answer}}"
                    }
                    
                },
                "false": {
                    "text_output": "No closing date is included in the agreement."
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst summarizing the target date in a merger agreement.\n"
            "\n"
            "Write a professional, clear, one-sentence bullet summarizing the target date.\n"
            "- Clause Text: {closing_date}"
        ),
        "output_field": "closing_date_summary",
        "reference_fields": [
        "closing_mechanics.target_date.target_date.reference_section"
        ],

        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 20,
        "summary_display_section": "Closing",
        "summary_rank": 3.1,
        "view_prompt": True
    },

    "Closing Mechanics : Marketing Period": {
        "question": "Is marketing period specified ?",
        "conditions": [
            {
                "question": "Target board approval",
                "if": "closing_mechanics.marketing_period.has_marketing_period.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "marketing_period": "{{closing_mechanics.marketing_period.marketing_period_details.answer}}"
                    }
                },
                "false": {
                    "text_output": ""
                    
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a merger agreement. Below is the full text of a clause:\n\n"
            "\n\n"
            "Your task is to write a precise, paraphrased 1-paragraph summary of the clause that:\n"
            "- States the main obligation (e.g., use of commercially reasonable efforts to operate in ordinary course)\n"
            "- Clearly lists the exceptions or carve-outs (e.g., required by law, agreed in writing, etc.)\n"
            "- Includes any specific operational duties or examples mentioned (e.g., preserving relationships, asset protection)\n"
            "- Uses some key quoted phrases from the clause if helpful, but avoid copying large sections\n"
            "- Avoids generic phrasing — aim to capture the nuance of the original clause.\n\n"
            "Write only one paragraph."
            "- Marketing Period: {marketing_period}\n"
        ),
        "output_field": "closing_mechanics_summary",
        "reference_fields": ["closing_mechanics.marketing_period.marketing_period_details.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words":150,
        "summary_display_section": "Closing",
        "summary_rank": 3.2,
        "view_prompt": True
    },


     "Closing Mechanics : Inside Date": {
        "question": "Is inside date specified ?",
        "conditions": [
            {
                "question": "Inside Date",
                "if": "closing_mechanics.inside_date.has_inside_date.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "inside_date": "{{closing_mechanics.inside_date.inside_date_details.answer}}"
                    }
                },
                "false": {
                    "text_output": ""
                    
                }
            },
            
        ],
        "prompt_template": (
             "You are a legal analyst reviewing a merger agreement. Below is the full text of a clause:\n\n"
            "\n\n"
            "Your task is to write a precise, paraphrased 1-paragraph summary of the clause that:\n"
            "- States the main obligation (e.g., use of commercially reasonable efforts to operate in ordinary course)\n"
            "- Clearly lists the exceptions or carve-outs (e.g., required by law, agreed in writing, etc.)\n"
            "- Includes any specific operational duties or examples mentioned (e.g., preserving relationships, asset protection)\n"
            "- Uses some key quoted phrases from the clause if helpful, but avoid copying large sections\n"
            "- Avoids generic phrasing — aim to capture the nuance of the original clause.\n\n"
            "Write only one paragraph."
            "- Inside Date: {inside_date}\n"
        ),
        "output_field": "closing_mechanics_summary",
        "reference_fields": ["closing_mechanics.inside_date.inside_date_details.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words":150,
        "summary_display_section": "Closing",
        "summary_rank": 3.3,
        "view_prompt": True
    }
}