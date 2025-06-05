LAW_JURISDICTION_CLAUSES = {

    #Concise 
        "Law and Jurisdiction : Governing Law ": {
            "question": "What are the efforts related to Law and Jurisdiction - Governing Law",
            "conditions": [
                {
                    "question": "Governing Law",
                    "if": "law_and_jurisdiction.governing_law.governing_law_exists.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "governing_law_info": "law_and_jurisdiction.governing_law.governing_law_jurisdiction.answer"
                        }
                    },
                    "false": {
                        "text_output": "Governing law was not included in the merger contract."
                    }
                }
            ],
            "prompt_template": (
                "Summarize the Governing Law below. Focus on the jurisdiction of the law.\n"
                "{governing_law_info}"
                "Give me single line summary of the Governing Law."
            ),
            "output_field": "governing_law_jurisdiction",
            
            "reference_fields": ["law_and_jurisdiction.governing_law.governing_law_jurisdiction.reference_section"],
            "use_short_reference": False,
            
            "summary_type": "Concise",
            "format_style": "phrase without bullet point",
            "max_words": 50,
            "summary_display_section": "Law and Jurisdiction",
            "summary_display_sub_section": "Governing Law",
            "summary_rank": 12,
            "view_prompt": True
        },

    #Fullsome 
        "Law and Jurisdiction : MAE Interpretation Jurisdiction": {
                "question": "What are the efforts related to Law and Jurisdiction - MAE Interpretation Jurisdiction",
                "conditions": [
                    {
                        "question": "MAE Interpretation Jurisdiction",
                        "if": "law_and_jurisdiction.mae_interpretation_jurisdiction.mae_interpretation_jurisdiction_exists.answer",
                        "type": "boolean",
                        "true": {
                            "add_to_prompt": {
                                "mae_interpretation_jurisdiction_info": "law_and_jurisdiction.mae_interpretation_jurisdiction.mae_interpretation_jurisdiction.answer"
                            }
                        },
                        "false": {
                            "text_output": "MAE Interpretation Jurisdiction was not included in the merger contract."
                        }
                    }
                ],
                "prompt_template": (
                    "Summarize the MAE Interpretation Jurisdiction below. Focus on the jurisdiction of the law."
                    "{mae_interpretation_jurisdiction_info}"
                
                ),
                "output_field": "mae_interpretation_jurisdiction",
                
                "reference_fields": ["law_and_jurisdiction.mae_interpretation_jurisdiction.mae_interpretation_jurisdiction.reference_section"],
                "use_short_reference": False,
                
                "summary_type": "Fulsome",
                "format_style": "paragraph",
                "max_words": 150,
                "summary_display_section": "Law and Jurisdiction",
                "summary_display_sub_section": "MAE Interpretation Jurisdiction",
                "summary_rank": 12,
                "view_prompt": True
            },

        "Law and Jurisdiction : Financing Jurisdiction": {
            "question": "What are the efforts related to Law and Jurisdiction - Financing Jurisdiction",
            "conditions": [
                {
                    "question": "Financing Jurisdiction",
                    "if": "law_and_jurisdiction.financing_jurisdiction.financing_jurisdiction_exists.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "financing_jurisdiction_info": "law_and_jurisdiction.financing_jurisdiction.financing_jurisdiction.answer"
                        }
                    },
                    "false": {
                        "text_output": "Financing Jurisdiction was not included in the merger contract."
                    }
                }
            ],
            "prompt_template": (
                "Summarize the Financing Jurisdiction below. Focus on the jurisdiction of the law."
                "{financing_jurisdiction_info}"
               
            ),
            "output_field": "financing_jurisdiction",
            
            "reference_fields": ["law_and_jurisdiction.financing_jurisdiction.financing_jurisdiction.reference_section"],
            "use_short_reference": False,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 150,
            "summary_display_section": "Law and Jurisdiction",
            "summary_display_sub_section": "Financing Jurisdiction",
            "summary_rank": 12,
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
            "summary_display_sub_section": "Arbitration Clause",
            "summary_rank": 12,
            "view_prompt": True
        }
}