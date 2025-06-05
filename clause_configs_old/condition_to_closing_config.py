CONDITION_TO_CLOSING_CLAUSES = {
    
    #Consice conditions to closing
    
    "Conditions to Closing : Mutual Conditions List": {
        "question": "Mutual Conditions List",
        "conditions": [
            {
                "question": "Mutual Conditions List",
                "if": "conditions_to_closing.mutual_conditions_list.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "mutual_conditions_list": "conditions_to_closing.mutual_conditions_list.answer",
                    }
                },
                "false": {
                    "text_output": "No mutual conditions found."
                   
                }
            },
        ],
        "prompt_template": (
             "Below are mutual closing conditions from a merger agreement:\n\n"
            "-{mutual_conditions_list}\n"
             "Summarize as a single sentence: 'Mutual conditions include: ...' Use M&A terms."
           
        ),
        "output_field": "mutual_conditions_list",
        "reference_fields": ["conditions_to_closing.mutual_conditions_list.reference_section"],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "bullet",
        "max_words":80,
        "summary_display_section": "Conditions to Closing",
        "summary_display_sub_section": "Mutual Conditions List",
        "summary_rank": 5,
        "view_prompt": True
    },

    "Conditions to Closing : Parent Closing Conditions": {
        "question": "Parent Closing Conditions",
        "conditions": [
            {
                "question": "Parent Closing Conditions",
                "if": "conditions_to_closing.parent_closing_conditions.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "parent_closing_conditions": "conditions_to_closing.parent_closing_conditions.answer",
                    }
                },
                "false": {
                    "text_output": "No Parent closing conditions found."
                
                }
            },
            
            
        ],
        "prompt_template": (
            "Conditions to Parent’s obligation to close:\n\n"
            "-{parent_closing_conditions}\n"
            "Summarize in one sentence using M&A terms."
           
        ),
        "output_field": "parent_closing_conditions",
        "reference_fields": ["conditions_to_closing.parent_closing_conditions.reference_section"],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "bullet",
        "max_words":80,
        "summary_display_section": "Conditions to Closing",
        "summary_display_sub_section": "Parent Closing Conditions",
        "summary_rank": 5,
        "view_prompt": True
    },

    "Conditions to Closing : Company Closing Conditions": {
        "question": "Is superior proposal engagement specified for the transaction?",
        "conditions": [
            {
                "question": "Company Closing Conditions",
                "if": "conditions_to_closing.company_closing_conditions.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "company_closing_conditions": "conditions_to_closing.company_closing_conditions.answer",
                    }
                },
                "false": {
                    "text_output": "No Company closing conditions found."
                
                }
            },
            
            
        ],
        "prompt_template": (
            "Conditions to Company’s obligation to close:\n\n"
            "-{company_closing_conditions}\n"
            "Summarize in one sentence using M&A terms."
           
        ),
        "output_field": "company_closing_conditions",
        "reference_fields": ["conditions_to_closing.company_closing_conditions.reference_section"],
        "use_short_reference": True,
         "summary_type": "Concise",
        "format_style": "bullet",
        "max_words":80,
        "summary_display_section": "Conditions to Closing",
        "summary_display_sub_section": "Company Closing Conditions",
        "summary_rank": 5,
        "view_prompt": True
    },
    
    #Fullsome conditions to closing
    
     "Conditions to Closing : Non-Customary Conditions": {
        "question": "Non-Customary Conditions",
        "conditions": [
            {
                "question": "financial_conditions_minimum_cash_threshold",
                "if": "conditions_to_closing.financial_conditions_minimum_cash_threshold.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "non_customary_conditions": "Minimum cash threshold"
                    }
                },
                "false": {}
            },
            {
                "question": "financial_conditions_maximum_net_debt",
                "if": "conditions_to_closing.financial_conditions_maximum_net_debt.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "non_customary_conditions": "Maximum net debt"
                    }
                },
                "false": {}
            },
            {
                "question": "financial_conditions_minimum_any_condition",
                "if": "conditions_to_closing.financial_conditions_minimum_any_condition.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "non_customary_conditions": "Minimum financial metric"
                    }
                },
                "false": {}
            },
            {
                "question": "tax_conditions_tax_opinion_required",
                "if": "conditions_to_closing.tax_conditions_tax_opinion_required.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "non_customary_conditions": "Tax opinion condition"
                    }
                },
                "false": {}
            }
        ],
        "prompt_template": (
            "Non-customary conditions identified in the agreement:\n\n"
            "{non_customary_conditions}"
        ),
        "output_field": "non_customary_conditions",
        "reference_fields": [
            "conditions_to_closing.financial_conditions_minimum_cash_threshold.reference_section",
            "conditions_to_closing.financial_conditions_maximum_net_debt.reference_section",
            "conditions_to_closing.financial_conditions_minimum_any_condition.reference_section",
            "conditions_to_closing.tax_conditions_tax_opinion_required.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "bullet",
        "max_words": 100,
        "summary_display_section": "Conditions to Closing",
        "summary_display_sub_section": "Non-Customary Conditions",
        "summary_rank": 5,
        "view_prompt": True,
        "join_type": "bullets"
},
   

    
    "Conditions to Closing : Additional Conditions": {
        "question": "Additional Conditions",
        "conditions": [
             {
            "question": "target shareholder approval with threshold",
            "if": "conditions_to_closing.target_shareholder_approval_required.answer",
            "type": "boolean",
            "true": {
                "add_to_prompt": {
                        "additional_conditions": "conditions_to_closing.target_shareholder_approval_threshold.answer",
                    },
            },
            "false": {
                "text_output":"No additional conditions found."
                
            }
        },
            {
                "question": "hsr clearance required",
                "if": "conditions_to_closing.hsr_clearance_required.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "other_customary_conditions": "conditions_to_closing.other_customary_conditions.answer"
                    }
                },
                "false": {
                    "text_output": {
                        "other_customary_conditions": "No additional conditions found."
                    }
                }
            }
        ],
        "prompt_template": (
            "Summarize the following list into a single sentence starting with:\n"
            "'Key conditions include: ...'\n\n"
            "Additional conditions: {additional_conditions}\n"
            "Other customary conditions: {other_customary_conditions}\n"
        ),
        "output_field": "additional_conditions",
        "reference_fields": ["conditions_to_closing.target_shareholder_approval_required.reference_section", "conditions_to_closing.hsr_clearance_required.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 100,
        "summary_display_section": "Conditions to Closing",
        "summary_display_sub_section": "Additional Conditions",
        "summary_rank": 5,
        "view_prompt": True
},
    
   
}