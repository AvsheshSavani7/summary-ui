ORDINARY_COURSE_CLAUSES = {

    #Concise Ordinary Course
        "Ordinary Course Covenant - Concise": {
            "question": "What are the efforts related to Ordinary Course - Concise",
            "conditions": [
                {
                    "question": "Ordinary Course Efforts - Concise",
                    "if": "ordinary_course.ordinary_course_covenant.concise_standard_summary.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "ordinary_course_info": "ordinary_course.ordinary_course_covenant.concise_standard_summary.clause_text"
                        }
                    },
                    "false": {
                        "text_output": "Ordinary Course of Business is not disclosed in the agreement."
                    }
                }
            ],
            "prompt_template": (
                "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
                "Task:\n"
                "- Identify the exact efforts standard stated in the clause.\n"
                "- Return a single concise sentence that uses the **exact efforts language** from the clause.\n"
                "- Do not paraphrase, generalize, or interpret the meaning.\n"
                "- Do not provide examples, commentary, or additional context.\n"
                "- The sentence should begin naturally (e.g., 'The Company shall...') and reflect only what is written.\n\n"
                "Clause Text:\n"
                "{ordinary_course_info}"
            ),
            "output_field": "concise_standard_summary",
            
            "reference_fields": ["ordinary_course.ordinary_course_covenant.concise_standard_summary.reference_section"],
            "use_short_reference": False,
            
            "summary_type": "Concise",
            "format_style": "paragraph",
            "max_words": 20,
            "summary_display_section": "Ordinary Course",
            "summary_display_sub_section": "Covenant",
            "summary_rank": 11,
            "view_prompt": True
        },

    #Fullsome Ordinary Course
        "Ordinary Course Covenant - Fulsome": {
            "question": "What are the efforts related to Ordinary Course - Fulsome",
            "conditions": [
                {
                    "question": "Ordinary Course Efforts - Fulsome",
                    "if": "ordinary_course.ordinary_course_covenant.concise_standard_summary.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "ordinary_course_info": "ordinary_course.ordinary_course_covenant.concise_standard_summary.clause_text"
                        }
                    },
                    "false": {
                        "text_output": "Ordinary Course of Business is not disclosed in the agreement."
                    }
                }
            ],
            "prompt_template": (
                "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
                "Task:\n"
                "- Identify the exact efforts standard stated in the clause, but incorporate only in the summary and not as a stand alone item.\n"
                "- Summarize the clause language without losing any critical details and **exact language** from the clause.\n"
                "- Do not paraphrase, generalize, interpret the meaning, or duplicate concepts.\n"
                "- Do not provide examples, commentary, or additional context.\n"
                "Clause Text:\n"
                "{ordinary_course_info}"
            ),
            "output_field": "fulsome_standard_summary",
            
            "reference_fields": ["ordinary_course.ordinary_course_covenant.concise_standard_summary.reference_section"],
            "use_short_reference": False,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 125,
            "summary_display_section": "Ordinary Course",
            "summary_display_sub_section": "Covenant",
            "summary_rank": 11,
            "view_prompt": False
        }
}