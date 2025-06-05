FINANCING_SUMMARY_CLAUSES = {

    #Concise Ordinary Course
        "Financing Summary : Committed Financing ": {
            "question": "What are the efforts related to Financing Summary - Committed Financing",
            "conditions": [
                {
                    "question": "Financing Summary - Committed Financing",
                    "if": "financing.committed_financing.committed_financing_present.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "financing_summary_info": "financing.committed_financing.committed_financing_summary.answer"
                        }
                    },
                    "false": {
                        "text_output": "Committed financing was not included in the merger contract."
                    }
                }
            ],
            "prompt_template": (
                "Summarize the Committed Financing below. Focus on Parent received committed financing from Bank."
                "{financing_summary_info}"
            ),
            "output_field": "committed_financing_summary",
            
            "reference_fields": ["financing.committed_financing.committed_financing_summary.reference_section"],
            "use_short_reference": False,
            
            "summary_type": "Concise",
            "format_style": "bullet",
            "max_words": 50,
            "summary_display_section": "Financing",
            "summary_display_sub_section": "Committed Financing",
           "summary_rank": 9,
            "view_prompt": True
        },

    #Fullsome Ordinary Course

        "Financing Summary : Committed Financing": {
            "question": "What are the efforts related to Financing Summary - Committed Financing",
            "conditions": [
                {
                    "question": "Financing Summary - Committed Financing",
                    "if": "financing.committed_financing.committed_financing_present.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "financing_summary_info": "financing.committed_financing.committed_financing_summary.answer"
                        }
                    },
                    "false": {
                        "text_output": "No detailed clause for committed financing found."
                    }
                }
            ],
            "prompt_template": (
                "You are a legal analyst reviewing a merger agreement Committed Financing. Below is the full text of a clause:\n\n"
                "\n\n"
                "Your task is to write a precise, paraphrased 1-paragraph summary of the Committed Financing that:\n"
                "- Focus on Parent received committed financing from Bank\n"
                "- Uses some key quoted phrases from the clause if helpful, but avoid copying large sections\n"
                "- Avoids generic phrasing — aim to capture the nuance of the original clause.\n\n"
                "Write only one paragraph."
                "{financing_summary_info}"
            ),
            "output_field": "committed_financing_summary",
            
            "reference_fields": ["financing.committed_financing.committed_financing_summary.reference_section"],
            "use_short_reference": False,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 150,
            "summary_display_section": "Financing",
            "summary_display_sub_section": "Committed Financing",
           "summary_rank": 9,
            "view_prompt": True
        },

        "Financing Summary : Financing Efforts Summary": {
            "question": "What are the efforts related to Financing Summary - Financing Efforts Summary",
            "conditions": [
                {
                    "question": "Financing Efforts Summary",
                    "if": "financing.financing_efforts_summary.financing_efforts_summary.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "financing_summary_info": "financing.financing_efforts_summary.financing_efforts_summary.answer"
                        }
                    },
                    "false": {
                        "text_output": "No detailed clause for committed financing found."
                    }
                }
            ],
            "prompt_template": (
                "You are a legal analyst reviewing a merger agreement Financing Efforts. Below is the full text of a clause:\n\n"
                "\n\n"
                "Your task is to write a precise, paraphrased 1-paragraph summary of the Financing Efforts that:\n"
                "- Uses some key quoted phrases from the clause if helpful, but avoid copying large sections\n"
                "- Avoids generic phrasing — aim to capture the nuance of the original clause.\n\n"
                "Write only one paragraph."
                "{financing_summary_info}"
            ),
            "output_field": "financing_efforts_summary",
            
            "reference_fields": ["financing.financing_efforts_summary.financing_efforts_summary.reference_section"],
            "use_short_reference": False,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 150,
            "summary_display_section": "Financing",
            "summary_display_sub_section": "Financing Efforts Summary",
           "summary_rank": 9,
            "view_prompt": False
        },

        "Financing Summary : Substitute Financing Notice And Efforts": {
            "question": "What are the efforts related to Financing Summary - Substitute Financing Notice And Efforts",
            "conditions": [
                {
                    "question": "Substitute Financing Notice And Efforts",
                    "if": "financing.substitute_financing_notice_and_efforts.substitute_financing_notice_and_efforts.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "substitute_financing_notice_and_efforts_summary": "financing.substitute_financing_notice_and_efforts.substitute_financing_notice_and_efforts.answer"
                        }
                    },
                    "false": {
                        "text_output": "No detailed clause for substitute financing notice and efforts found."
                    }
                }
            ],
            "prompt_template": (
                "You are a legal analyst reviewing a merger agreement Substitute Financing Notice And Efforts. Below is the full text of a clause:\n\n"
        
                "Your task is to write a precise, paraphrased 1-paragraph summary of the Substitute Financing Notice And Efforts that:\n"
                "- Uses some key quoted phrases from the clause if helpful, but avoid copying large sections\n"
                "- Avoids generic phrasing — aim to capture the nuance of the original clause.\n\n"
                "Write only one paragraph."
                "{substitute_financing_notice_and_efforts_summary}"
            ),
            "output_field": "substitute_financing_notice_and_efforts_summary",
            "reference_fields": ["financing.substitute_financing_notice_and_efforts.substitute_financing_notice_and_efforts.reference_section"],
            "use_short_reference": False,
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 150,
            "summary_display_section": "Financing",
            "summary_display_sub_section": "Substitute Financing Notice And Efforts",
           "summary_rank": 9,
            "view_prompt": False
        }
}