ORDINARY_COURSE_CLAUSES = {

    #Concise Ordinary Course
        "Ordinary Course Covenant - Concise": {
            "question": "What are the efforts related to Ordinary Course - Concise",
            "conditions": [
                {
                    "question": "Ordinary Course Efforts - Concise",
                    "if": "ordinary_course.company_ordinary_course_covenant.company_conduct_covenant_summary.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "company_ordinary_course_answer": "{{ordinary_course.company_ordinary_course_covenant.company_conduct_covenant_summary.answer}}",
                            "company_ordinary_course_text": "{{ordinary_course.company_ordinary_course_covenant.company_conduct_covenant_summary.clause_text}}",
                            "parent_ordinary_course_answer": "{{ordinary_course.parent_ordinary_course_covenant.parent_conduct_covenant_summary.answer}}",
                            "parent_ordinary_course_text": "{{ordinary_course.parent_ordinary_course_covenant.parent_conduct_covenant_summary.clause_text}}"
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
            "- Identify the exact efforts standard stated in the clause related to ordinary course operations for both the parent and company if applicable and if so ensure to state efforts for both parties.\n"
            "- Return a single sentence that uses the **exact language** from the clause, including both the subject (who the obligation applies to) and the efforts standard.\n"
            "- Do not paraphrase, interpret, summarize, or omit any part of the language.\n"
            "- Do not include examples, commentary, or rewording.\n"
            "- The sentence must begin naturally (e.g., 'The Company shall...') and reflect the original clause wording.\n\n"
            "-- Clause Text:\n"
            "Company Ordinary Course Answer.\n"
            "{company_ordinary_course_answer}\n"
            "Company Ordinary Course Clause Text.\n"
            "{company_ordinary_course_text}\n"
            "Parent Ordinary Course Answer.\n"
            "{parent_ordinary_course_answer}\n"
            "Parent Ordinary Course Clause Text.\n"
            "{parent_ordinary_course_text}\n"
            "--- Example Outputs:\n"
            "- X shall conduct its business in all material respects in the ordinary course and use commercially reasonable efforts to do certain specified things.\n"
            "- AZEK shall use commercially reasonable efforts to conduct business in the ordinary course.\n"
            "- Both CELG and BMY shall use commercially reasonable efforts to conduct business in the ordinary course consistent with past practice."
        ),
            "output_field": "concise_standard_summary",
            
            "reference_fields": ["ordinary_course.company_ordinary_course_covenant.company_conduct_covenant_summary.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Concise",
            "format_style": "paragraph",
            "max_words": 30,
            "summary_display_section": "Other Items",
            "summary_rank": 6.2,
            "view_prompt": True
        },

    #Fullsome Ordinary Course
         "Ordinary Course Covenant - Fulsome": {
            "question": "What are the efforts related to Ordinary Course - Concise",
            "conditions": [
                {
                    "question": "Ordinary Course Efforts - Concise",
                    "if": "ordinary_course.company_ordinary_course_covenant.company_conduct_covenant_summary.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "company_ordinary_course_answer": "{{ordinary_course.company_ordinary_course_covenant.company_conduct_covenant_summary.answer}}",
                            "company_ordinary_course_text": "{{ordinary_course.company_ordinary_course_covenant.company_conduct_covenant_summary.clause_text}}",
                            "parent_ordinary_course_answer": "{{ordinary_course.parent_ordinary_course_covenant.parent_conduct_covenant_summary.answer}}",
                            "parent_ordinary_course_text": "{{ordinary_course.parent_ordinary_course_covenant.parent_conduct_covenant_summary.clause_text}}"
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
            "- Identify the exact efforts standard stated in the clause related to ordinary course operations for both the parent and company if applicable and if so ensure to state efforts for both parties.\n"
            "- Return a single sentence that uses the **exact language** from the clause, including both the subject (who the obligation applies to) and the efforts standard.\n"
            "- Do not paraphrase, interpret, summarize, or omit any part of the language.\n"
            "- Do not include examples, commentary, or rewording.\n"
            "- The sentence must begin naturally (e.g., 'The Company shall...') and reflect the original clause wording.\n\n"
            "-- Clause Text:\n"
            "Company Ordinary Course Answer.\n"
            "{company_ordinary_course_answer}\n"
            "Company Ordinary Course Clause Text.\n"
            "{company_ordinary_course_text}\n"
            "Parent Ordinary Course Answer.\n"
            "{parent_ordinary_course_answer}\n"
            "Parent Ordinary Course Clause Text.\n"
            "{parent_ordinary_course_text}\n"
            "--- Example Outputs:\n"
            "- X shall conduct its business in all material respects in the ordinary course and use commercially reasonable efforts to do certain specified things.\n"
            "- AZEK shall use commercially reasonable efforts to conduct business in the ordinary course.\n"
            "- Both CELG and BMY shall use commercially reasonable efforts to conduct business in the ordinary course consistent with past practice."
        ),
            "output_field": "Fulsome_standard_summary",
            
            "reference_fields": ["ordinary_course.company_ordinary_course_covenant.company_conduct_covenant_summary.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 30,
            "summary_display_section": "Ordinary Course Covenants ",
            "summary_rank": 13.1,
            "view_prompt": True
        }

}