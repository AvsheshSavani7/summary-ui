FINANCING_SUMMARY_CLAUSES = {

    #Concise Ordinary Course
        "Financing Summary : Committed Financing - Concise": {
            "question": "What are the efforts related to Financing Summary - Committed Financing",
            "conditions": [
                {
                    "question": "Financing Summary - Committed Financing",
                    "if": "financing.committed_financing.committed_financing_present.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "financing_summary_present": "{{financing.committed_financing.committed_financing_present.clause_text}}",
                            "financing_summary_details": "{{financing.committed_financing.committed_financing_summary.answer}}"
                        }
                    },
                    "false": {
                        "text_output": "Committed financing was not included in the merger contract."
                    }
                }
            ],
            "prompt_template": (
                "You are a legal analyst summarizing the committed financing structure in a merger agreement.\n\n"
                "Task:\n"
                "- Determine whether the Parent has received committed financing to fund the transaction.\n"
                "- Focus on whether a Debt Commitment Letter has been delivered and name the financing sources (banks or institutions) if mentioned.\n"
                "- Return a single, clear, concise sentence simply confirming the financing and the parties involved.\n"
                "- Do not rephrase legal terms. Extract what is stated in plain terms.\n"
                "- Output a concise one-sentence summary like: 'Parent has received committed financing from [Bank Names].'\n"
                "- If no information is available, return nothing.\n\n"
                "-- Provided Fields:\n"
                "{financing_summary_present}\n"
                "{financing_summary_details}\n\n"
                "--- Example Output:\n"
                "Parent has received committed financing from Bank of America and Jefferies Finance."
            ),
            "output_field": "committed_financing_summary",
            
            "reference_fields": ["financing.committed_financing.committed_financing_summary.reference_section"],
            "use_short_reference": False,
            
            "summary_type": "Concise",
            "format_style": "paragraph",
            "max_words": 20,
            "summary_display_section": "Conditions & Financing",
            "summary_rank": 3.4,
            "view_prompt": True
        },

    #Fullsome Ordinary Course

        "Financing Summary : Committed Financing - Fulsome": {
            "question": "What are the efforts related to Financing Summary - Committed Financing",
            "conditions": [
                {
                    "question": "Financing Summary - Committed Financing",
                    "if": "financing.committed_financing.committed_financing_present.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "financing_summary_present": "{{financing.committed_financing.committed_financing_present.clause_text}}",
                            "financing_summary_details": "{{financing.committed_financing.committed_financing_summary.answer}}"
                        }
                    },
                    "false": {
                        "text_output": "Committed financing was not included in the merger contract."
                    }
                }
            ],
            "prompt_template": (
                "You are a legal analyst summarizing the committed financing structure in a merger agreement.\n\n"
                "Task:\n"
                "- Determine whether the Parent has received committed financing to fund the transaction.\n"
                "- Focus on whether a Debt Commitment Letter has been delivered and name the financing sources (banks or institutions) if mentioned.\n"
                "- Return a single, clear, concise sentence simply confirming the financing and the parties involved.\n"
                "- Do not rephrase legal terms. Extract what is stated in plain terms.\n"
                "- Output a concise one-sentence summary like: 'Parent has received committed financing from [Bank Names].'\n"
                "- If no information is available, return nothing.\n\n"
                "-- Provided Fields:\n"
                "{financing_summary_present}\n"
                "{financing_summary_details}\n\n"
                "--- Example Output:\n"
                "Parent has received committed financing from Bank of America and Jefferies Finance."
            ),
            "output_field": "committed_financing_summary",
            
            "reference_fields": ["financing.committed_financing.committed_financing_summary.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 50,
            "summary_display_section": "Financing",
            "summary_rank": 9.1,
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
                            "financing_summary_info": "{{financing.financing_efforts_summary.financing_efforts_summary.answer}}",
                            "financing_summary_text": "{{financing.financing_efforts_summary.financing_efforts_summary.clause_text}}"
                        }
                    },
                    "false": {
                        "text_output": ""
                    }
                }
            ],
            "prompt_template": (
                "You are a legal analyst reviewing a merger agreement Financing Efforts. Below is the full text of a clause:\n\n"
                "\n\n"
                "Your task is to write a precise, paraphrased 1-paragraph summary of the Financing Efforts that:\n"
                "- Uses some key quoted phrases from the clause if helpful, but avoid copying large sections\n"
                "- Avoids generic phrasing — aim to capture the nuance of the original clause.\n"
                "Write only one paragraph.\n\n"
                "{financing_summary_info}\n"
                "{financing_summary_text}\n\n"
                "--- Example\n"
                "Parent shall use reasonable best efforts to consummate the Financing in an amount sufficient, together with cash on hand and amounts available to be drawn on the Parent Credit Facility, to consummate the Merger.\n"
            ),
            "output_field": "financing_efforts_summary",
            
            "reference_fields": ["financing.financing_efforts_summary.financing_efforts_summary.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 30,
            "summary_display_section": "Financing",
            "summary_rank": 9.2,
            "view_prompt": True
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
                            "substitute_financing_notice_and_efforts_summary": "{{financing.substitute_financing_notice_and_efforts.substitute_financing_notice_and_efforts.answer}}",
                            "substitute_financing_notice_and_efforts_text": "{{financing.substitute_financing_notice_and_efforts.substitute_financing_notice_and_efforts.clause_text}}"
                        }
                    },
                    "false": {
                        "text_output": ""
                    }
                }
            ],
            "prompt_template": (
                "You are a legal analyst reviewing a merger agreement Substitute Financing Notice And Efforts. Below is the full text of a clause:\n\n"
        
                "Your task is to write a precise, paraphrased 1-paragraph summary of the Substitute Financing Notice And Efforts that:\n"
                "- Uses some key quoted phrases from the clause if helpful, but avoid copying large sections\n"
                "- Avoids generic phrasing — aim to capture the nuance of the original clause.\n\n"
                "Write only one paragraph.\n\n"
                "-- Contract Information\n"
                "{substitute_financing_notice_and_efforts_summary}\n"
                "{substitute_financing_notice_and_efforts_text}\n\n"
                "--- Examples\n"
                "Parent shall use reasonable best efforts to obtain the Debt Financing.  If any portion becomes unavailable, Parent shall use reasonable best efforts to obtain, as promptly as practicable alternative debt financing on terms and conditions, taken as a whole, no less favorable to Parent.\n"
                "Parent shall use reasonable best efforts to consummate the Debt Financing.  In the event any portion of the Debt Financing becomes unavailable, Parent shall cause Guarantor to use its reasonable best efforts to obtain alternative debt financing in an amount sufficient to enable Parent to consummate the transaction.\n"
                "If funds in the amounts set forth in the Debt Letters, or any portion thereof, become unavailable, Parent shall, as promptly as practicable, notify the company in writing and use reasonable best efforts to obtain substitute financing.\n"
            ),
            "output_field": "substitute_financing_notice_and_efforts_summary",
            "reference_fields": ["financing.substitute_financing_notice_and_efforts.substitute_financing_notice_and_efforts.reference_section"],
            "use_short_reference": True,
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 35,
            "summary_display_section": "Financing",
            "summary_rank": 9.3,
            "view_prompt": True
        }
}