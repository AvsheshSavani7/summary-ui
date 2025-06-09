LAW_JURISDICTION_CLAUSES = {

    #Concise 
        "Law and Jurisdiction : Governing Law - Concise": {
            "question": "What are the efforts related to Law and Jurisdiction - Governing Law",
            "conditions": [
                {
                    "question": "Governing Law",
                    "if": "law_and_jurisdiction.governing_law.governing_law_exists.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "governing_law_info": "{{law_and_jurisdiction.governing_law.governing_law_jurisdiction.clause_text}}"
                        }
                    },
                    "false": {
                        "text_output": ""
                    }
                }
            ],
            "prompt_template": (
                "You are a legal analyst reviewing a merger agreement.\n\n"
                "Task:\n"
                "- Identify the jurisdiction specified in the governing law clause.\n"
                "- Return a single, complete sentence that uses the **exact language** from the clause where possible.\n"
                "- Do not paraphrase, interpret, or add any commentary.\n"
                "- The sentence should begin naturally (e.g., 'This Agreement shall be governed by...') and reflect only what is written.\n\n"
                "-- Clause Text:\n"
                "{governing_law_info}\n\n"
                "--- Example Output:\n"
                "This Agreement shall be governed by the laws of the State of Delaware."
            ),
            "output_field": "governing_law_jurisdiction",
            
            "reference_fields": ["law_and_jurisdiction.governing_law.governing_law_jurisdiction.reference_section"],
            "use_short_reference": False,
            
            "summary_type": "Concise",
            "format_style": "sentence",
            "max_words": 20,
            "summary_display_section": "Other Items",
            "summary_rank": 6.5,
            "view_prompt": True
        },

        "Law and Jurisdiction : Financing Jurisdiction - Concise": {
            "question": "What are the efforts related to Law and Jurisdiction - Financing Jurisdiction",
            "conditions": [
                {
                    "question": "Financing Jurisdiction",
                    "if": "law_and_jurisdiction.financing_jurisdiction.financing_jurisdiction_exists.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "financing_jurisdiction_info": "{{law_and_jurisdiction.financing_jurisdiction.financing_jurisdiction.clause_text}}"
                        }
                    },
                    "false": {
                        "text_output": ""
                    }
                }
            ],
            "prompt_template": (
                "You are a legal analyst reviewing a merger agreement.\n\n"
                "Task:\n"
                "- Identify the jurisdiction specified in the clause relating to financing sources or financing-related disputes.\n"
                "- Return a single, complete sentence that uses the **exact language** from the clause where possible.\n"
                "- Do not paraphrase, interpret, or add any commentary.\n"
                "- The sentence should begin naturally (e.g., 'Matters relating to...') and reflect only what is written.\n\n"
                "-- Clause Text:\n"
                "{financing_jurisdiction_info}\n\n"
                "--- Example Output:\n"
                "Matters relating to any action or claim against any Financing Source Party shall be governed by the Laws of the State of New York."
            ),
            "output_field": "financing_jurisdiction",
            
            "reference_fields": ["law_and_jurisdiction.financing_jurisdiction.financing_jurisdiction.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Concise",
            "format_style": "Paragraph",
            "max_words": 25,
            "summary_display_section": "Other Items",
            "summary_rank": 6.6,
            "view_prompt": True
        },


    #Fullsome 

        "Law and Jurisdiction : Governing Law - Fulsome": {
            "question": "What are the efforts related to Law and Jurisdiction - Governing Law",
            "conditions": [
                {
                    "question": "Governing Law",
                    "if": "law_and_jurisdiction.governing_law.governing_law_exists.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "governing_law_info": "{{law_and_jurisdiction.governing_law.governing_law_jurisdiction.clause_text}}"
                        }
                    },
                    "false": {
                        "text_output": ""
                    }
                }
            ],
            "prompt_template": (
                "You are a legal analyst reviewing a merger agreement.\n\n"
                "Task:\n"
                "- Identify the jurisdiction specified in the governing law clause.\n"
                "- Return a single, complete sentence that uses the **exact language** from the clause where possible.\n"
                "- Do not paraphrase, interpret, or add any commentary.\n"
                "- The sentence should begin naturally (e.g., 'This Agreement shall be governed by...') and reflect only what is written.\n\n"
                "-- Clause Text:\n"
                "{governing_law_info}\n\n"
                "--- Example Output:\n"
                "This Agreement shall be governed by the laws of the State of Delaware."
            ),
            "output_field": "governing_law_jurisdiction",
            
            "reference_fields": ["law_and_jurisdiction.governing_law.governing_law_jurisdiction.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "sentence",
            "max_words": 20,
            "summary_display_section": "Governing Law",
            "summary_rank": 14.1,
            "view_prompt": True
        },

        "Law and Jurisdiction : MAE Interpretation Jurisdiction": {
                "question": "What are the efforts related to Law and Jurisdiction - MAE Interpretation Jurisdiction",
                "conditions": [
                    {
                        "question": "MAE Interpretation Jurisdiction",
                        "if": "law_and_jurisdiction.mae_interpretation_jurisdiction.mae_interpretation_jurisdiction_exists.answer",
                        "type": "boolean",
                        "true": {
                            "add_to_prompt": {
                                "mae_interpretation_jurisdiction_info": "{{law_and_jurisdiction.mae_interpretation_jurisdiction.mae_interpretation_jurisdiction.answer}}",
                                "mae_interpretation_jurisdiction_text": "{{law_and_jurisdiction.mae_interpretation_jurisdiction.mae_interpretation_jurisdiction.clause_text}}"
                            }
                        },
                        "false": {
                            "text_output": ""
                        }
                    }
                ],
                "prompt_template": (
                    "Summarize concisely the MAE Interpretation Jurisdiction. Focus on the jurisdiction of the MAE law.\n\n"
                    "--- Clause Texts\n"
                    "MAE Jurisdiction Answer: {mae_interpretation_jurisdiction_info}\n"
                    "MAE Jurisdiction Text: {mae_interpretation_jurisdiction_text}\n"
                
                ),
                "output_field": "mae_interpretation_jurisdiction",
                
                "reference_fields": ["law_and_jurisdiction.mae_interpretation_jurisdiction.mae_interpretation_jurisdiction.reference_section"],
                "use_short_reference": True,
                
                "summary_type": "Fulsome",
                "format_style": "paragraph",
                "max_words": 20,
                "summary_display_section": "Governing Law",
                "summary_rank": 14.2,
                "view_prompt": True
            },

        "Law and Jurisdiction : Arbitration Clause": {
            "question": "What are the efforts related to Law and Jurisdiction - Arbitration Clause",
            "conditions": [
                {
                    "question": "Arbitration Clause",
                    "if": "law_and_jurisdiction.arbitration_clause.arbitration_clause_exists.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "arbitration_clause_info": "law_and_jurisdiction.arbitration_clause.arbitration_clause.answer"
                        }
                    },
                    "false": {
                        "text_output": "Arbitration Clause was not included in the merger contract."
                    }
                }
            ],
            "prompt_template": (
                "Summarize the Arbitration Clause below. Focus on the jurisdiction of the law."
                "{arbitration_clause_info}"
        
            ),
            "output_field": "arbitration_clause",
            "reference_fields": ["law_and_jurisdiction.arbitration_clause.arbitration_clause.reference_section"],
            "use_short_reference": False,
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 150,
            "summary_display_section": "Law and Jurisdiction",
            "summary_rank": 1,
            "view_prompt": True
        },

        "Law and Jurisdiction : Financing Jurisdiction - Fulsome": {
            "question": "What are the efforts related to Law and Jurisdiction - Financing Jurisdiction",
            "conditions": [
                {
                    "question": "Financing Jurisdiction",
                    "if": "law_and_jurisdiction.financing_jurisdiction.financing_jurisdiction_exists.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "financing_jurisdiction_info": "{{law_and_jurisdiction.financing_jurisdiction.financing_jurisdiction.clause_text}}"
                        }
                    },
                    "false": {
                        "text_output": ""
                    }
                }
            ],
            "prompt_template": (
                "You are a legal analyst reviewing a merger agreement.\n\n"
                "Task:\n"
                "- Identify the jurisdiction specified in the clause relating to financing sources or financing-related disputes.\n"
                "- Return a single, complete sentence that uses the **exact language** from the clause where possible.\n"
                "- Do not paraphrase, interpret, or add any commentary.\n"
                "- The sentence should begin naturally (e.g., 'Matters relating to...') and reflect only what is written.\n\n"
                "-- Clause Text:\n"
                "{financing_jurisdiction_info}\n\n"
                "--- Example Output:\n"
                "Matters relating to any action or claim against any Financing Source Party shall be governed by the Laws of the State of New York."
            ),
            "output_field": "financing_jurisdiction",
            
            "reference_fields": ["law_and_jurisdiction.financing_jurisdiction.financing_jurisdiction.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "Paragraph",
            "max_words": 25,
            "summary_display_section": "Specific Performance",
            "summary_rank": 15.3,
            "view_prompt": True
        },

}