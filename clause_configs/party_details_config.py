PARTY_DETAILS_CLAUSES = {

   
    #Fullsome 
        "Party Details : Acquirer": {
                "question": "Who is the Acquirer? Provide the full legal name and jurisdiction of incorporation.",
                "conditions": [
                    {
                        "question": "acquirer",
                        "if": "party_details.acquirer.acquirer.answer",
                        "type": "non_empty",
                        "true": {
                            "add_to_prompt": {
                                "acquirer_name": "{{party_details.acquirer.acquirer.answer}}",
                                "acquirer_entity": "{{law_and_jurisdiction.incorporation_details.parent_incorporation_details.answer}}"
                            }
                        },
                        "false": {
                            "text_output": "Acquirer was not included in the merger contract."
                        }
                    }
                ],
                "prompt_template": (
                    "You are a legal analyst summarizing publicly available corporate information from a merger agreement.\n\n"
                    "Task:\n"
                    "- Write one short sentence starting with 'Acquirer is' that identifies the legal name and jurisdiction of incorporation.\n"
                    "- Use only the provided inputs. Do not guess or add extra phrasing.\n\n"
                    "Acquirer Name: {acquirer_name}\n"
                    "Acquirer Entity Type: {acquirer_entity}\n\n"
                    "--- Examples ---\n"
                    "Acquirer is Celgene Corporation, a Delaware corporation.\n"
                    "Acquirer is United States Steel Corporation, a Delaware corporation.\n"
                    "Acquirer is The AZEK Company Inc, a Delaware corporation.\n"
                ),
                "output_field": "acquirer",
                
                "reference_fields": ["party_details.acquirer.acquirer.reference_section"],
                "use_short_reference": False,
                
                "summary_type": "Fulsome",
                "format_style": "paragraph",
                "max_words": 25,
                "summary_display_section": "Party Details",
                "summary_rank": 1.2,
                "view_prompt": True
            },

        "Party Details : Target": {
            "question":"Who is the Target company? Provide its legal name and jurisdiction.",
            "conditions": [
                {
                    "question": "Target",
                    "if": "party_details.target.target.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "target_name": "{{party_details.target.target.answer}}",
                            "target_entity": "{{law_and_jurisdiction.incorporation_details.company_incorporation_details.answer}}"
                        }
                    },
                    "false": {
                        "text_output": "Target name was not included in the merger contract."
                    }
                }
            ],
                "prompt_template": (
                    "You are a legal analyst summarizing publicly available corporate information from a merger agreement.\n\n"
                    "Task:\n"
                    "- Write one short sentence starting with 'Company is' that identifies the legal name and jurisdiction of incorporation.\n"
                    "- Use only the provided inputs. Do not guess or add extra phrasing.\n\n"
                    "Company Name: {target_name}\n"
                    "Company Entity Type: {target_entity}\n\n"
                    "--- Examples ---\n"
                    "Company is Celgene Corporation, a Delaware corporation.\n"
                    "Company is United States Steel Corporation, a Delaware corporation.\n"
                    "Company is The AZEK Company Inc, a Delaware corporation.\n"
        ),
            "output_field": "target",
            
            "reference_fields": ["party_details.target.target.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 25,
            "summary_display_section": "Party Details",
            "summary_rank": 1.1,
            "view_prompt": True
        },

        "Party Details : Subsidiaries": {
            "question": "Which subsidiaries are mentioned in the agreement and what is their relationship to the Parent or Target?",
            "conditions": [
                {
                    "question": "Subsidiaries",
                    "if": "party_details.subsidiaries.subsidiaries_present.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "subsidiaries_info": "{{party_details.subsidiaries.target_subsidiaries.answer}}"
                        }
                    },
                    "false": {
                        "text_output": ""
                    }
                }
            ],
            "prompt_template": (
            "List and describe any subsidiaries involved in the transaction, specifying their relationship to the parent or target.\n\n"
            "{subsidiaries_info}"
        ),
            "output_field": "subsidiaries",
            "reference_fields": ["party_details.subsidiaries.target_subsidiaries.reference_section"],
            "use_short_reference": False,
            "summary_type": "OFF",
            "format_style": "paragraph",
            "max_words": 35,
            "summary_display_section": "Party Details",
            "summary_rank": 1,
            "view_prompt": True
        },

        "Party Details : Acquirer Subsidiaries": {
            "question": "Are any subsidiaries of the Acquirer involved in the transaction? List them and describe their role.",
            "conditions": [
                {
                    "question": "Subsidiaries",
                    "if": "party_details.subsidiaries.acquirer_subsidiaries_present.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "acquirer_subsidiaries_info": "{{party_details.subsidiaries.acquirer_subsidiaries.answer}}"
                        }
                    },
                    "false": {
                        "text_output": ""
                    }
                }
            ],
            "prompt_template": (
               "Describe the subsidiaries of the Acquirer that are involved in the transaction, including their legal structure and role.\n\n"
            "{acquirer_subsidiaries_info}"
        
            ),
            "output_field": "subsidiaries",
            "reference_fields": ["party_details.subsidiaries.acquirer_subsidiaries.reference_section"],
            "use_short_reference": False,
            "summary_type": "OFF",
            "format_style": "paragraph",
            "max_words": 35,
            "summary_display_section": "Party Details",
            "summary_rank": 1,
            "view_prompt": True
        },

        "Party Details : Transaction": {
            "question": "What is the structure of the transaction? Indicate whether it's a merger, acquisition, or another form, and who the surviving entity is.",
            "conditions": [
                {
                    "question": "Transaction Type",
                    "if": "party_details.transaction.transaction_type.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "transaction_info": "{{party_details.transaction.transaction_type.answer}}",
                            "transaction_details": "{{party_details.transaction.transaction_structure_notes.answer}}"
                        }
                    },
                    "false": {
                        "text_output": "Transaction was not included in the merger contract."
                    }
                }
            ],
            "prompt_template": (
                 "Summarize the structure of the transaction, clearly indicating if it's a merger, stock purchase, or other form, and identify the surviving entity if applicable.\n\n"
            "{transaction_info}\n"
            "{transaction_details}"
            ),
            "output_field": "transaction",
            "reference_fields": ["party_details.transaction.transaction_type.reference_section","party_details.transaction.transaction_structure_notes.reference_section"],
            "use_short_reference": False,
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 40,
            "summary_display_section": "Party Details",
            "summary_rank": 1.3,
            "view_prompt": True
        },

        "Party Details : Guarantor": {
            "question": "Who is the Merger Sub? Provide its name, jurisdiction, and its relationship to the Parent.",
            "conditions": [
                {
                    "question": "Merger Sub",
                    "if": "party_details.guarantor.guarantor_present.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "guarantor_info": "{{party_details.guarantor.guarantor_present.clause_text}}"
                        }
                    },
                    "false": {
                        "text_output": ""
                    }
                }
            ],
            "prompt_template": (
                 "Summarize the identity of the guarantor, including its incorporation and relationship to the Parent.\n\n"
            "{guarantor_info}"
        
            ),
            "output_field": "guarantor",
            "reference_fields": ["party_details.guarantor.guarantor_present.reference_section"],
            "use_short_reference": True,
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 20,
            "summary_display_section": "Party Details",
            "summary_rank": 1.4,
            "view_prompt": True
        },

        "Party Details : Merger Sub": {
            "question": "Who is the Merger Sub? Provide its name, jurisdiction, and its relationship to the Parent.",
            "conditions": [
                {
                    "question": "Merger Sub",
                    "if": "party_details.merger_sub_details.merger_sub_details.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "merger_sub_info": "{{party_details.merger_sub_details.merger_sub_details.answer}}"
                        }
                    },
                    "false": {
                        "text_output": "Merger Sub was not included in the merger contract."
                    }
                }
            ],
            "prompt_template": (
                 "Summarize the identity of the Merger Sub, including its incorporation and relationship to the Parent.\n\n"
            "{merger_sub_info}"
        
            ),
            "output_field": "merger_sub",
            "reference_fields": ["party_details.merger_sub_details.merger_sub_details.reference_section"],
            "use_short_reference": False,
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 30,
            "summary_display_section": "Party Details",
            "summary_rank": 1.5,
            "view_prompt": True
        }
}