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
                                "acquirer_info": "party_details.acquirer.acquirer.answer"
                            }
                        },
                        "false": {
                            "text_output": "Acquirer was not included in the merger contract."
                        }
                    }
                ],
                "prompt_template": (
                    "Summarize the acquirer's identity, including the full legal name and jurisdiction of incorporation. "
            "Start the sentence with 'Parent is' or 'Acquirer is'.\n\n"
            "{acquirer_info}"
                
                ),
                "output_field": "acquirer",
                
                "reference_fields": ["party_details.acquirer.acquirer.reference_section"],
                "use_short_reference": False,
                
                "summary_type": "Fulsome",
                "format_style": "paragraph",
                "max_words": 25,
                "summary_display_section": "Party Details",
                "summary_display_sub_section": "Acquirer",
                "summary_rank": 1,
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
                            "target_info": "party_details.target.target.answer"
                        }
                    },
                    "false": {
                        "text_output": "Target was not included in the merger contract."
                    }
                }
            ],
            "prompt_template": (
            "Summarize the target's identity, including the legal name and jurisdiction. "
            "Start with 'Company is'.\n\n"
            "{target_info}"
        ),
            "output_field": "target",
            
            "reference_fields": ["party_details.target.target.reference_section"],
            "use_short_reference": False,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 25,
            "summary_display_section": "Party Details",
            "summary_display_sub_section": "Target",
            "summary_rank": 1,
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
                            "subsidiaries_info": "party_details.subsidiaries.target_subsidiaries.answer"
                        }
                    },
                    "false": {
                        "text_output": "Subsidiaries were not included in the merger contract."
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
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 35,
            "summary_display_section": "Party Details",
            "summary_display_sub_section": "Subsidiaries",
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
                            "acquirer_subsidiaries_info": "party_details.subsidiaries.acquirer_subsidiaries.answer"
                        }
                    },
                    "false": {
                        "text_output": "Acquirer Subsidiaries were not included in the merger contract."
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
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 35,
            "summary_display_section": "Party Details",
            "summary_display_sub_section": "Acquirer Subsidiaries",
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
                            "transaction_info": "party_details.transaction.transaction_type.answer",
                            "transaction_details": "party_details.transaction.transaction_structure_notes.answer"
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
            "summary_display_sub_section": "Transaction",
            "summary_rank": 1,
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
                            "merger_sub_info": "party_details.merger_sub_details.merger_sub_details.answer"
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
            "summary_display_sub_section": "Merger Sub",
            "summary_rank": 1,
            "view_prompt": True
        },
}