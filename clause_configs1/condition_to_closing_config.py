CONDITION_TO_CLOSING_CLAUSES = {
    
    #Consice conditions to closing

    "Conditions to Closing : Highlight Conditions": {
        "question": "Additional Conditions",
        "conditions": [
             {
            "question": "target shareholder approval with threshold",
            "if": "conditions_to_closing.target_shareholder_approval_required.answer",
            "type": "boolean",
            "true": {
                "add_to_prompt": {
                        "target_shareholder_vote": "{{conditions_to_closing.target_shareholder_approval_required.clause_text}}",
                        "target_shareholder_threshold": "{{conditions_to_closing.target_shareholder_approval_threshold.clause_text}}"
                    },
            },
            "false": {
                "add_to_prompt": {
                        "target_shareholder_vote": "Target shareholder requirements and thresholds are not specified in the merger agreement",
                        "target_shareholder_threshold": ""
                },
            }
            },
            {
            "question": "Parent Shareholder Approval with threshold",
            "if": "conditions_to_closing.parent_shareholder_approval_required.answer",
            "type": "boolean",
            "true": {
                "add_to_prompt": {
                        "parent_shareholder_vote": "{{conditions_to_closing.parent_shareholder_approval_required.clause_text}}",
                        "parent_shareholder_threshold_answer": "{{conditions_to_closing.parent_shareholder_approval_threshold.answer}}",
                        "parent_shareholder_threshold_text": "{{conditions_to_closing.parent_shareholder_approval_threshold.clause_text}}"
                    },
            },
            "false": {
                "add_to_prompt": {
                        "parent_shareholder_vote": "{{conditions_to_closing.parent_shareholder_approval_required.clause_text}}",
                        "parent_shareholder_threshold_answer": "{{conditions_to_closing.parent_shareholder_approval_threshold.answer}}",
                        "parent_shareholder_threshold_text": "{{conditions_to_closing.parent_shareholder_approval_threshold.clause_text}}"
                },
            }
            },

            {
            "question": "Parent Shareholder Approval with threshold",
            "if": "conditions_to_closing.parent_shareholder_approval_threshold.answer",
            "type": "enum",
            "not_in": ["", "Not found", None],
            "true": {
                "add_to_prompt": {
                        "parent_shareholder_vote": "{{conditions_to_closing.parent_shareholder_approval_required.clause_text}}",
                        "parent_shareholder_threshold_answer": "{{conditions_to_closing.parent_shareholder_approval_threshold.answer}}",
                        "parent_shareholder_threshold_text": "{{conditions_to_closing.parent_shareholder_approval_threshold.clause_text}}"
                    },
            },
            "false": {
                "add_to_prompt": {
                        "parent_shareholder_vote": "{{conditions_to_closing.parent_shareholder_approval_required.clause_text}}",
                        "parent_shareholder_threshold_answer": "{{conditions_to_closing.parent_shareholder_approval_threshold.answer}}",
                        "parent_shareholder_threshold_text": "{{conditions_to_closing.parent_shareholder_approval_threshold.clause_text}}"
                },
            }
            },
            # {
            #     "question": "hsr clearance required",
            #     "if": "conditions_to_closing.hsr_clearance_required.answer",
            #     "type": "boolean",
            #     "true": {
            #         "add_to_prompt": {
            #             "hsr_clearance": "{{conditions_to_closing.hsr_clearance_required.clause_text}}"
            #         }
            #     },
            #     "false": {
            #         "add_to_prompt": {
            #             "hsr_clearance": "{{conditions_to_closing.hsr_clearance_required.clause_text}}"
            #        }
            #     }
            # },
            #             {
            #     "question": "Other Customary Conditions",
            #     "if": "conditions_to_closing.other_customary_conditions.answer",
            #     "type": "non_empty",
            #     "true": {
            #         "add_to_prompt": {
            #             "other_conditions": "{{conditions_to_closing.other_customary_conditions.answer}}"
            #         }
            #     },
            #     "false": {
            #         "add_to_prompt": {
            #             "other_conditions": ""
            #        }
            #     }
            # }
        ],
        "prompt_template": (
            "You are a legal analyst summarizing the key conditions to closing in a merger agreement.\n\n"
            "Task:\n"
            "- Review the provided fields and construct a single clear easy to read sentence summarizing the condition for company and parent voting and required thresholds.\n"
            "- The sentence must begin with: 'Subject to...'\n"
            "--- Clause Texts:\n"
            "  • Target shareholder approval (use threshold from {target_shareholder_vote})\n"
            "  • Target shareholder approval (use threshold from {target_shareholder_threshold})\n"
            "  • Parent shareholder approval (use threshold from {parent_shareholder_vote})\n"
            "  • Parent shareholder approval (use threshold from {parent_shareholder_threshold_answer})\n"
            "  • Parent shareholder approval (use threshold from {parent_shareholder_threshold_text})\n"
            # "  • HSR clearance ({hsr_clearance})\n"
            # "- If {other_conditions} exists and is non-empty, conclude the sentence with: 'and other customary conditions including:' and then provide a bulleted list with the items from {other_conditions} without duplicating any items already detailed.\n"
            # "- If {other_conditions} is empty, end the sentence without mentioning customary conditions and do not include any list.\n"
            # "- Avoid repeating any condition already described in the summary sentence.\n"
            "- Do not include party names, clause references, or rephrase terms beyond the provided text.\n"
            "- The final summary sentence should be no more than 50 words.\n\n"
            # "- HSR Clearance: {hsr_clearance}\n"
            # "- Other Customary Conditions: {other_conditions}\n\n"
            "--- Example Output:\n"
            "Subject to majority shareholder approval.\n"
            # "• Parent Share Issuance approved for listing on the NYSE\n"
            # "• Form F-4 effective under the Securities Act\n"
            # "• No Governmental Authority Order or Law enjoining or prohibiting the Merger.\n"
        ),
        "output_field": "additional_conditions",
        "reference_fields": ["conditions_to_closing.target_shareholder_approval_required.reference_section"],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 25,
        "summary_display_section": "Conditions & Financing",
        "summary_rank": 3.1,
        "view_prompt": True
},

    "Conditions to Closing : Regulatory Clearances Required": {
        "question": "Regulatory Clearances Required",
        "conditions": [
             {
            "question": "Regulatory Clearances Required",
            "if": "best_efforts.regulatory_efforts.effort_scope.answer",
            "type": "non_empty",
            "true": {
                "add_to_prompt": {
                        "regulatory_requirements": "{{best_efforts.regulatory_efforts.effort_scope.answer}}",
                        "regulatory_requirements_text": "{{best_efforts.regulatory_efforts.effort_scope.answer}}"
                    },
            },
                "false": {
                    "text_output": ""
                }
            },
        ],
        "prompt_template": (
            "You are a legal analyst summarizing regulatory closing conditions in a merger agreement.\n\n"
            "Task:\n"
            "- Write **one concise sentence** summarizing all regulatory approvals required to close the transaction.\n"
            "- If the Hart-Scott-Rodino Antitrust Improvements Act (HSR) is mentioned, refer to it as 'the HSR Act'.\n"
            "- If any parties are included like the DOJ or FTC that would fall under the HSR, and the HSR is already included, do not mention those agencies.\n"
            "- If foreign or other antitrust approvals are mentioned, summarize as 'all other required antitrust approvals'.\n"
            "- Do **not** use phrases like 'requisite regulatory approvals' if specific items are listed.\n"
            "- Avoid repeating the same requirement in different forms.\n"
            "- Use formal but succinct M&A language.\n\n"
            "-- Provided Fields:\n"
            "- Regulatory Requirements: {regulatory_requirements}\n"
            "- Raw Text (if needed): {regulatory_requirements_text}\n\n"
            "--- Example Output:\n"
            "Subject to clearance under HSR and other foreign antitrust laws, and other customary conditions."
        ),

        "output_field": "regulatory_conditions",
        "reference_fields": ["best_efforts.regulatory_efforts.effort_scope.reference_section"],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 100,
        "summary_display_section": "Conditions & Financing",
        "summary_rank": 3.2,
        "view_prompt": True
},

    "Conditions to Closing : Non-Customary Conditions": {
        "question": "Non-Customary Conditions",
        "conditions": [
            {
                "question": "financial_conditions_minimum_cash_threshold",
                "if": "conditions_to_closing.financial_conditions_minimum_cash_threshold.answer",
                "type": "enum",
                "not_in": ["", "Not found", None],
                "true": {
                    "add_to_prompt": {
                        "minimum_cash": "{{conditions_to_closing.financial_conditions_minimum_cash_threshold.clause_text}}"
                    }
                },
                "false": {}
            },
            {
                "question": "financial_conditions_maximum_net_debt",
                "if": "conditions_to_closing.financial_conditions_maximum_net_debt.answer",
                "type": "enum",
                "not_in": ["", "Not found", None],
                "true": {
                    "add_to_prompt": {
                        "max_net_debt": "{{conditions_to_closing.financial_conditions_maximum_net_debt.clause_text}}"
                    }
                },
                "false": {}
            },
            {
                "question": "financial_conditions_minimum_any_condition",
                "if": "conditions_to_closing.financial_conditions_minimum_any_condition.answer",
                "type": "enum",
                "not_in": ["", "Not found", None],
                "true": {
                    "add_to_prompt": {
                        "min_any_condition": "{{conditions_to_closing.financial_conditions_minimum_any_condition.clause_text}}"
                    }
                },
                "false": {}
            },
            {
                "question": "tax_conditions_tax_opinion_required",
                "if": "conditions_to_closing.tax_conditions_tax_opinion_required.answer",
                "type": "enum",
                "not_in": ["", "Not found", None],
                "true": {
                    "add_to_prompt": {
                        "non_customary_conditions": "{{conditions_to_closing.tax_conditions_tax_opinion_required.clause_text}}"
                    }
                },
                "false": {}
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a merger agreement for non-customary closing conditions.\n\n"
            "Task:\n"
            "- Review each labeled clause below.\n"
            "- If the clause contains a condition, summarize it clearly in a bullet point.\n"
            "- If a clause is missing or blank, return nothing for that item.\n"
            "- Only include bullet points for clauses that contain substantive conditions.\n\n"
            "-- Clauses (labeled):\n"
            "Minimum Cash Threshold:\n{minimum_cash}\n\n"
            "Maximum Net Debt:\n{max_net_debt}\n\n"
            "Minimum Financial Metric:\n{min_any_condition}\n\n"
            "Tax Opinion Condition:\n{non_customary_conditions}\n\n"
            "--- Example Output:\n"
            "- The agreement requires the company to maintain a minimum cash balance of $100 million at closing.\n"
            "- Net debt at closing must not exceed $500 million.\n"
            "- A tax opinion is required as a condition to closing.\n\n"
            "--- Additional Instructions:\n"
            "- Return bullet points only for the clauses that contain relevant, non-empty content.\n"
            "- Do not include headings, labels, or commentary in the output.\n"
            "- Each bullet should be one complete sentence in plain, formal language."
        ),
        "output_field": "non_customary_conditions",
        "reference_fields": [
            "conditions_to_closing.financial_conditions_minimum_cash_threshold.reference_section",
            "conditions_to_closing.financial_conditions_maximum_net_debt.reference_section",
            "conditions_to_closing.financial_conditions_minimum_any_condition.reference_section",
            "conditions_to_closing.tax_conditions_tax_opinion_required.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "bullet",
        "max_words": 100,
        "summary_display_section": "Conditions & Financing",
        "summary_rank": 3.3,
        "view_prompt": True,
        "join_type": "bullets"
},
    
   
    #Fullsome conditions to closing
    
  

    

    "Conditions to Closing : Mutual Conditions List": {
        "question": "Mutual Conditions List",
        "conditions": [
            {
                "question": "Mutual Conditions List",
                "if": "conditions_to_closing.mutual_conditions_list.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "mutual_conditions_list": "{{conditions_to_closing.mutual_conditions_list.answer}}",
                    }
                },
                "false": {
                    "text_output": "No mutual conditions found."
                   
                }
            },
        ],
        "prompt_template": (
            "Below are mutual closing conditions from a merger agreement:\n\n"
            "Mutual Conditions to Close List: - {mutual_conditions_list}\n"
            "Summarize as a single sentence: 'Mutual conditions include: ...' Use M&A terms."
           
        ),
        "output_field": "mutual_conditions_list",
        "reference_fields": ["conditions_to_closing.mutual_conditions_list.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "Paragraph",
        "max_words":100,
        "summary_display_section": "Conditions",
        "summary_rank": 5.1,
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
                        "parent_closing_conditions": "{{conditions_to_closing.parent_closing_conditions.answer}}",
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
        "summary_type": "Fulsome",
        "format_style": "Paragraph",
        "max_words":100,
        "summary_display_section": "Conditions",
        "summary_rank": 5.2,
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
                        "company_closing_conditions": "{{conditions_to_closing.company_closing_conditions.answer}}",
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
         "summary_type": "Fulsome",
        "format_style": "Paragraph",
        "max_words":100,
        "summary_display_section": "Conditions",
        "summary_rank": 5.3,
        "view_prompt": True
    },

    "Conditions to Closing : Shareholder Approval - Fulsome": {
        "question": "Additional Conditions",
        "conditions": [
             {
            "question": "target shareholder approval with threshold",
            "if": "conditions_to_closing.target_shareholder_approval_required.answer",
            "type": "boolean",
            "true": {
                "add_to_prompt": {
                        "target_shareholder_vote": "{{conditions_to_closing.target_shareholder_approval_required.clause_text}}",
                        "target_shareholder_threshold": "{{conditions_to_closing.target_shareholder_approval_threshold.clause_text}}"
                    },
            },
            "false": {
                "add_to_prompt": {
                        "target_shareholder_vote": "Target shareholder requirements and thresholds are not specified in the merger agreement",
                        "target_shareholder_threshold": ""
                },
            }
            },
            {
            "question": "Parent Shareholder Approval with threshold",
            "if": "conditions_to_closing.parent_shareholder_approval_required.answer",
            "type": "boolean",
            "true": {
                "add_to_prompt": {
                        "parent_shareholder_vote": "{{conditions_to_closing.parent_shareholder_approval_required.clause_text}}",
                        "parent_shareholder_threshold_answer": "{{conditions_to_closing.parent_shareholder_approval_threshold.answer}}",
                        "parent_shareholder_threshold_text": "{{conditions_to_closing.parent_shareholder_approval_threshold.clause_text}}"
                    },
            },
            "false": {
                "add_to_prompt": {
                        "parent_shareholder_vote": "{{conditions_to_closing.parent_shareholder_approval_required.clause_text}}",
                        "parent_shareholder_threshold_answer": "{{conditions_to_closing.parent_shareholder_approval_threshold.answer}}",
                        "parent_shareholder_threshold_text": "{{conditions_to_closing.parent_shareholder_approval_threshold.clause_text}}"
                },
            }
            },

            {
            "question": "Parent Shareholder Approval with threshold",
            "if": "conditions_to_closing.parent_shareholder_approval_threshold.answer",
            "type": "enum",
            "not_in": ["", "Not found", None],
            "true": {
                "add_to_prompt": {
                        "parent_shareholder_vote": "{{conditions_to_closing.parent_shareholder_approval_required.clause_text}}",
                        "parent_shareholder_threshold_answer": "{{conditions_to_closing.parent_shareholder_approval_threshold.answer}}",
                        "parent_shareholder_threshold_text": "{{conditions_to_closing.parent_shareholder_approval_threshold.clause_text}}"
                    },
            },
            "false": {
                "add_to_prompt": {
                        "parent_shareholder_vote": "{{conditions_to_closing.parent_shareholder_approval_required.clause_text}}",
                        "parent_shareholder_threshold_answer": "{{conditions_to_closing.parent_shareholder_approval_threshold.answer}}",
                        "parent_shareholder_threshold_text": "{{conditions_to_closing.parent_shareholder_approval_threshold.clause_text}}"
                },
            }
            },
            # {
            #     "question": "hsr clearance required",
            #     "if": "conditions_to_closing.hsr_clearance_required.answer",
            #     "type": "boolean",
            #     "true": {
            #         "add_to_prompt": {
            #             "hsr_clearance": "{{conditions_to_closing.hsr_clearance_required.clause_text}}"
            #         }
            #     },
            #     "false": {
            #         "add_to_prompt": {
            #             "hsr_clearance": "{{conditions_to_closing.hsr_clearance_required.clause_text}}"
            #        }
            #     }
            # },
            #             {
            #     "question": "Other Customary Conditions",
            #     "if": "conditions_to_closing.other_customary_conditions.answer",
            #     "type": "non_empty",
            #     "true": {
            #         "add_to_prompt": {
            #             "other_conditions": "{{conditions_to_closing.other_customary_conditions.answer}}"
            #         }
            #     },
            #     "false": {
            #         "add_to_prompt": {
            #             "other_conditions": ""
            #        }
            #     }
            # }
        ],
        "prompt_template": (
            "You are a legal analyst summarizing the key conditions to closing in a merger agreement.\n\n"
            "Task:\n"
            "- Review the provided fields and construct a single clear easy to read sentence summarizing the condition for company and parent voting and required thresholds.\n"
            "- The sentence must begin with: 'Subject to...'\n"
            "--- Clause Texts:\n"
            "  • Target shareholder approval (use threshold from {target_shareholder_vote})\n"
            "  • Target shareholder approval (use threshold from {target_shareholder_threshold})\n"
            "  • Parent shareholder approval (use threshold from {parent_shareholder_vote})\n"
            "  • Parent shareholder approval (use threshold from {parent_shareholder_threshold_answer})\n"
            "  • Parent shareholder approval (use threshold from {parent_shareholder_threshold_text})\n"
            # "  • HSR clearance ({hsr_clearance})\n"
            # "- If {other_conditions} exists and is non-empty, conclude the sentence with: 'and other customary conditions including:' and then provide a bulleted list with the items from {other_conditions} without duplicating any items already detailed.\n"
            # "- If {other_conditions} is empty, end the sentence without mentioning customary conditions and do not include any list.\n"
            # "- Avoid repeating any condition already described in the summary sentence.\n"
            "- Do not include party names, clause references, or rephrase terms beyond the provided text.\n"
            "- The final summary sentence should be no more than 50 words.\n\n"
            # "- HSR Clearance: {hsr_clearance}\n"
            # "- Other Customary Conditions: {other_conditions}\n\n"
            "--- Example Output:\n"
            "Subject to majority shareholder approval.\n"
            # "• Parent Share Issuance approved for listing on the NYSE\n"
            # "• Form F-4 effective under the Securities Act\n"
            # "• No Governmental Authority Order or Law enjoining or prohibiting the Merger.\n"
        ),
        "output_field": "additional_conditions",
        "reference_fields": ["conditions_to_closing.target_shareholder_approval_required.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 50,
        "summary_display_section": "Conditions",
        "summary_rank": 6.2,
        "view_prompt": True
},

   
}