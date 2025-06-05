BEST_EFFORTS_CLAUSES = {

    
    # Concise Best Efforts
    "Best Efforts : Divestiture commitments": {
        "question": "divestiture_commitments?",
        "conditions": [
            {
                "question": "What are the Divestiture Comitments of the Company",
                "if": "best_efforts.divestiture_commitments.divestiture_required.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "target_notes": "best_efforts.divestiture_commitments.divestiture_cap_target_notes.answer",
                         "parent_notes": "best_efforts.divestiture_commitments.divestiture_cap_buyer_notes.answer"
                    }
                },
                "false": {
                        "text_output": "No divestiture commitments are required under the terms of the agreement."
                }
            },
            
           
        ],
        "prompt_template": (
            "You are a legal and finance analyst summarizing M&A contract terms.:\n\n"
            "Write a single concise sentence summarizing the divestiture cap for the target based on the data below. Use professional tone and precise legal language.\n"
            "- Target Divestiture Notes: {target_notes}\n"
            "Write one single concise sentence, that explains the divestiture cap as it applies to the buyer and the buyer's businesses. "
            "Use precise legal language but avoid verbosity. If the buyer is not obligated to take any remedy actions on its business, clearly state that. "
            "If the cap is zero or not applicable, explicitly note it.\n\n"
            "- Parent Divestiture Notes: {parent_notes}"
            "Example Outputs : \n"
            "	There is a divestiture cap on Target businesses that generated $130mm in 2002 sales, and Parent is not required to take any Remedy Action on any of its businesses."
            "	There is a materiality limitation on divestiture and remedial actions relative to the size of the pro forma company."	
        ),
        "output_field": "divestiture_commitments_summary",
        "reference_fields": ["best_efforts.divestiture_commitments.divestiture_required.reference_section"],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words":50,
        "summary_display_section": "Best Efforts",
        "summary_display_sub_section": "Divestiture commitments",
        "summary_rank": 7,
        "view_prompt": True
    },
    
    "Best Efforts : Litigation Commitments": {
    "question": "summarize_litigation_commitment?",
    "conditions": [
        {
        "question": "litigation_requirement_status",
        "if": "best_efforts.litigation_commitments.litigation_requirement_status.answer",
        "type": "enum",
        "enum_cases": {
            "Explicit Requirement to Litigate": {
            "add_to_prompt": {
                "litigation_requirement_status": "best_efforts.litigation_commitments.litigation_requirement_status.clause_text"
            }
            },
            "Explicit Exclusion": {
            "add_to_prompt": {
                "litigation_requirement_status": "best_efforts.litigation_commitments.litigation_requirement_status.clause_text"
            }
            },
            "No Mention": {
            "text_output": "No mention of requirement to litigate"
            }
        },
        "default": {
            "text_output": "Unknown litigation commitment treatment."
        }
        }
    ],
 	"prompt_template": (
                        "### Instruction\n" 
                        "You are a legal analyst reviewing an M&A agreement.\n"
                        "Summarize the litigation requirement status in **one sentence**.\n"
                        "Focus:\n"
                        "Ignore procedural language and extract only whether the Parent is required to defend against litigation to allow the Merger to close.\n\n"
                        "### Input:\n"
                        "{litigation_requirement_status} \n\n"
                        "### Examples:\n"
                        "• Parent is required to defend against any litigation.\n"
                        "• BMY is required to defend against any litigation.\n"
                        "• Nippon is required to defend against any litigatio\n"
                        "Follow the structure and brevity of the examples exactly.\n"
                        
                        ),
    "output_field": "litigation_requirement_summary",
    "reference_fields": [
        "best_efforts.litigation_commitments.litigation_requirement_status.reference_section"
    ],
    "use_short_reference": True,
    "summary_type": "Concise",
    "format_style": "",
    "max_words": 25,
    "summary_display_section": "Best Efforts",
    "summary_display_sub_section": "Litigation commitments",
    "summary_rank": 7,
    "view_prompt": True
    },

    
    "Best Effort : HSR": {
        "question": "HSR",
        "conditions": [
            {
                "question": "HSR",
                "if": "best_efforts.regulatory_fillings_hsr.hsr_required.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "deadline": "best_efforts.regulatory_fillings_hsr.hsr_filing_deadline_days.answer",
                        "notes": "best_efforts.regulatory_fillings_hsr.hsr_notes.answer",
                    }
                },
                "false": {
                    
                        "text_output": "HSR filing is not required under the agreement."
                    
                }
            },
           
        ],
        "prompt_template": (
            "Summarize the filing obligation for HSR in one bullet point.\n"
            "Use acronyms where possible for conciseness\n"
            "Deadline (if any): {deadline}\n"
            "Notes: {notes}\n"
            "Avoid redundancy. If both deadline and notes exist, combine them logically. Be concise and formal.\n"
        ),
        "output_field": "board_approval_summary",
        "reference_fields": ["best_efforts.regulatory_fillings_hsr.hsr_required.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_display_sub_section": "HSR",
        "summary_rank": 7,
        "view_prompt": True
    },
    
    "Best Effort : CFIIUS": {
        "question": "CFIIUS",
        "conditions": [
            {
                "question": "CFIIUS",
                "if": "best_efforts.regulatory_fillings_cfiius.cfiius_required.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "deadline": "best_efforts.regulatory_fillings_cfiius.cfiius_filing_deadline_days.answer",
                        "notes": "best_efforts.regulatory_fillings_cfiius.cfiius_notes.answer"
                    }
                },
                "false": {
                    
                        "text_output": "CFIUS filing is not required under the agreement."
                }
            }
        ],
        "prompt_template": (
            "Summarize the filing obligation for CFIIUS in one bullet point.\n"
            "Deadline (if any): {deadline}\n"
            "Notes: {notes}\n"
            "Avoid redundancy. If both deadline and notes exist, combine them logically. Be concise and formal.\n"
        ),
        "output_field": "CFIIUS_summary",
        "reference_fields": ["best_efforts.regulatory_fillings_cfiius.cfiius_required.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_display_sub_section": "CFIIUS",
        "summary_rank": 7,
        "view_prompt": True
    },
   
    "Best Effort : Foreign Filing": {
        "question": "Foreign Filing",
        "conditions": [
            {
                "question": "Foreign Filing",
                "if": "best_efforts.regulatory_fillings_foreign.foreign_required.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "deadline": "best_efforts.regulatory_fillings_foreign.foreign_filing_deadline_days.answer",
                        "notes": "best_efforts.regulatory_fillings_foreign.foreign_notes.answer"
                    }
                },
                "false": {
                   
                        "text_output": "Foreign regulatory filings are not required under the agreement."
                    
                }
            }
          
          
              
        ],
        "prompt_template": (
            "Summarize the filing obligation for foreign filing in one bullet point.\n"
            "Deadline (if any): {deadline}\n"
            "Notes: {notes}\n"
            "Avoid redundancy. If both deadline and notes exist, combine them logically. Be concise and formal.\n"
        ),
        "output_field": "foreign_filing_summary",
        "reference_fields": ["best_efforts.regulatory_fillings_foreign.foreign_required.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_display_sub_section": "Foreign Filing",
        "summary_rank": 7,
        "view_prompt": True
    },
     
    "Best Effort : Standard": {
        "question": "effort_standard",
        "conditions": [
            {
                "question": "effort_standard",
                "if": "best_efforts.regulatory_efforts.effort_standard.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "standard": "best_efforts.regulatory_efforts.effort_standard.answer",
                        "scope" : "best_efforts.regulatory_efforts.effort_scope.answer"
                    }
                },
                "false": {
                    "text_output": "Effort Standard are not disclosed in the agreement."
                }
            }
        ],
        "prompt_template": ("You are a legal analyst summarizing M&A agreement terms.\n"
        "Write one concise bullet point describing the regulatory effort standard used by the parties.\n"
        "Effort Standard: {standard}\n"
        "Effort Scope: {scope}\n"
        "Use professional legal tone. If applicable, clarify that the standard applies to obtaining regulatory approvals.\n"
        ),
        "output_field": "effort_standard_summary",
        "reference_fields": ["best_efforts.regulatory_efforts.effort_standard.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 100,
        "summary_display_section": "Best Efforts",
        "summary_display_sub_section": "Standard",
        "summary_rank": 7,
        "view_prompt": True
    }, 
    
    "Best Effort : Withdrawal controls": {
        "question": "withdrawal_and_timing_controls_withdrawal",
        "conditions": [
            {
                "question": "withdrawal_and_timing_controls_withdrawal",
                "if": "best_efforts.withdrawal_and_timing_controls_withdrawal.withdrawal_control_type.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "control_type":  "best_efforts.withdrawal_and_timing_controls_withdrawal.withdrawal_control_type.answer",
                        "notes": "best_efforts.withdrawal_and_timing_controls_withdrawal.withdrawal_control_type_notes.answer",
                        
                    }
                },
                "false": {
                    "text_output": "Withdrawal control type are not disclosed in the agreement."
                }
            }
        ],
        "prompt_template": (
             "You are a legal analyst summarizing M&A agreement terms.\n"
            "Write one concise bullet point describing the type of consent required for withdrawal of regulatory filings and any conditions attached.\n"
            "Control Type: {control_type}\n"
            "Notes: {notes}\n"
            "Use professional legal tone. Avoid redundancy.\n"
            
        ),
        "output_field": "withdrawal_controls_summary",
        "reference_fields": ["best_efforts.withdrawal_and_timing_controls_withdrawal.withdrawal_control_type.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 100,
        "summary_display_section": "Best Efforts",
        "summary_display_sub_section": "Withdrawal controls",
        "summary_rank": 7,
        "view_prompt": True
    },
    
    "Best Effort : Timing agreement": {
        "question": "withdrawal_and_timing_controls_timing",
        "conditions": [
            {
                "question": "withdrawal_and_timing_controls_timing",
                "if": "best_efforts.withdrawal_and_timing_controls_timing.timing_agreement_restriction.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "restriction":  "best_efforts.withdrawal_and_timing_controls_timing.timing_agreement_restriction.answer",
                        "notes": "best_efforts.withdrawal_and_timing_controls_timing.timing_agreement_restriction_notes.answer"
                        
                    }
                },
                "false": {
                    "text_output": "Timing agreements are not disclosed in the agreement."
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst summarizing M&A agreement terms.\n"
            "Write one concise bullet point, with no more than 30 words, explaining any restriction on entering timing agreements related to regulatory filings.\n"
            "Ensure the response focuses on restrictions and and consents.\n"
            "Restriction Present: {restriction}\n"
            "Notes: {notes}\n"
            "Use formal legal tone. Avoid redundancy"
            
        ),
        "output_field": "withdrawal_controls_summary",
        "reference_fields": ["best_efforts.withdrawal_and_timing_controls_timing.timing_agreement_restriction_notes.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 100,
        "summary_display_section": "Best Efforts",
        "summary_display_sub_section": "Timing agreement",
        "summary_rank": 7,
        "view_prompt": True
    },
    
     "Best Effort : Divestiture Cap": {
        "question": "Divestiture Cap",
        "conditions": [
            {
                "question": "Divestiture Cap",
                "if": "best_efforts.divestiture_commitments.divestiture_required.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "target_notes": "best_efforts.divestiture_commitments.divestiture_cap_target_notes.answer",
                        "buyer_notes": "best_efforts.divestiture_commitments.divestiture_cap_buyer_notes.answer"
                    }
                },
                "false": {
                    
                        "text_output": "No divestiture commitments apply under the agreement."
                    
                }
            }
        ],
        "prompt_template": (
             "You are a legal analyst summarizing M&A agreement terms.\n"
            "Write a comprehensive summary, not to exceed 250 tokens, for the divestiture cap commitments in the agreement.\n"
            "Clearly distinguish between divestiture cap limitations for the Target vs. the Buyer (Parent).\n"
            "For the Target, explain what types of business units are exempt from remedy obligations due to size thresholds or revenue.\n"
            "For the Buyer, state clearly if the buyer (Parent and its Subsidiaries) is not required to take any remedy actions.\n"
            "Target Cap Notes: {target_notes}\n"
            "Buyer Cap Notes: {buyer_notes}\n"
            "Avoid duplicating contract language. Use a formal legal tone. Write as one complete paragraph. Be concise, and do not state obvious items.\n"
            "End your response cleanly. Avoid trailing phrases that suggest an unfinished conclusion."
            "Summary:"
        ),
        "output_field": "divestiture_cap_summary",
        "reference_fields": ["best_efforts.divestiture_commitments.divestiture_cap_target_notes.reference_section","best_efforts.divestiture_commitments.divestiture_cap_parent_notes.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_display_sub_section": "Divestiture Cap",
        "summary_rank": 7,
        "view_prompt": True
    },
    
     "Best Effort : Prior Approval Commitment": {
        "question": "Prior Approval Commitment",
        "conditions": [
            {
                "question": "Prior Approval Commitment",
                "if": "best_efforts.prior_approval_commitment.prior_approval_commitment_addressed.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "addressed": "best_efforts.prior_approval_commitment.prior_approval_commitment_addressed.answer",
                        "summary": "best_efforts.prior_approval_commitment.prior_approval_commitment_obligations_summary.answer"
                    }
                },
                "false": {
                    
                        "text_output": "Prior Approval Commitment are not disclosed in the agreement."
                    
                }
            }
        ],
        "prompt_template": (
                "You are a legal analyst summarizing M&A agreement terms.\n"
                "Write one concise bullet point summarizing any prior approval commitments under the agreement.\n"
                "Addressed: {addressed}\n"
                "Summary: {summary}\n"
                "Use professional legal tone. Be concise and clear.\n"
                "Bullet:"
        ),
        "output_field": "prior_approval_commitment_summary",
        "reference_fields": ["best_efforts.prior_approval_commitment.prior_approval_commitment_obligations_summary.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_display_sub_section": "Prior Approval Commitment",
        "summary_rank": 7,
        "view_prompt": True
    },
    
     "Best Effort : Transaction Interference": {
        "question": "transaction_interference",
        "conditions": [
            {
                "question": "transaction_interference",
                "if": "best_efforts.transaction_interference.restriction_on_other_transactions.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "restriction": "best_efforts.transaction_interference.restriction_on_other_transactions.answer",
                        "notes" : "best_efforts.transaction_interference.interference_clause_text.answer"
                    }
                },
                "false": {
                    
                        "text_output": "Transaction Interference are not disclosed in the agreement."
                    
                }
            }
        ],
        "prompt_template": (
                 "You are a legal analyst summarizing M&A agreement terms.\n"
                "Write one concise bullet point explaining any restrictions on alternative transactions that could interfere with the agreed merger.\n"
                "Restricted: {restriction}\n"
                "Notes: {notes}\n"
                "Use precise legal language and a formal tone. Be clear and avoid duplication. Do not cite the section number or clause in the sentence — it will be added separately.\n"
                "Start directly with the parties or actions involved.\n"
        ),
        "output_field": "transaction_interference_summary",
        "reference_fields": ["best_efforts.transaction_interference.interference_clause_text.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_display_sub_section": "Transaction Interference",
        "summary_rank": 7,
        "view_prompt": True
    },
        
    "Best Effort : Second Request Certification": {
        "question": "second_request_certification",
        "conditions": [
            {
                "question": "second_request_certification",
                "if": "best_efforts.second_request_certification.second_request_certification_deadline_specified.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "deadline": "best_efforts.second_request_certification.second_request_certification_deadline_specified.answer",
                        "notes" : "best_efforts.second_request_certification.second_request_certification_certification_timeline_notes.answer",
                        "party" :"best_efforts.second_request_certification.second_request_certification_responsibility_party.answer"
                    }
                },
                "false": {
                    
                        "text_output": "Second Request Certification are not disclosed in the agreement."
                    
                }
            }
        ],
        "prompt_template": (
                 "You are a legal analyst summarizing M&A agreement terms.\n"
                "Write one concise bullet point explaining the timing and party responsibility for certifying compliance with a second request under the HSR Act.\n"
                "Deadline Specified: {deadline}\n"
                "Timeline Notes: {notes}\n"
                "Responsible Party: {party}\n"
                "Do not include clause references. Use formal legal tone."
        ),
        "output_field": "transaction_interference_summary",
        "reference_fields": ["best_efforts.second_request_certification.second_request_certification_deadline_specified.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_display_sub_section": "Second Request Certification",
        "summary_rank": 7,
        "view_prompt": True
    },
      
     "Best Effort : FTC Warning Letter Handling": {
        "question": "ftc_warning_letter_handling",
        "conditions": [
            {
                "question": "ftc_warning_letter_handling",
                "if": "best_efforts.ftc_warning_letter_handling.ftc_warning_letter_handling_addressed.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        
                            "addressed" : "best_efforts.ftc_warning_letter_handling.ftc_warning_letter_handling_addressed.answer", 
                            "notes": "best_efforts.ftc_warning_letter_handling.ftc_warning_letter_handling_notes.answer",
                            "closing_impact" : "best_efforts.ftc_warning_letter_handling.ftc_warning_letter_handling_effect_on_closing_condition.answer",
                            "extra" : "best_efforts.ftc_warning_letter_handling.ftc_warning_letter_handling_addressed_notes.answer",
                    }
                },
                "false": {
                    
                        "text_output": "There is no consideration per the contract given to the receipt of an FTC warning letter."
                    
                }
            }
        ],
        "prompt_template": (
                 "You are a legal analyst summarizing M&A agreement terms.\n"
                "Write one concise bullet point explaining how the agreement addresses the receipt of an FTC warning letter.\n"
                "If the letter is addressed, summarize the procedure and clarify whether it affects closing conditions.\n"
                "Addressed: {addressed}\n"
                "Handling Notes: {notes}\n"
                "Effect on Closing: {closing_impact}\n"
                "Additional Notes: {extra}\n"
                "Do not include clause references. Write clearly and formally in one sentence.\n"
        ),
        "output_field": "ftc_warning_letter_handling_summary",
        "reference_fields": ["best_efforts.ftc_warning_letter_handling.ftc_warning_letter_handling_addressed.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_display_sub_section": "FTC Warning Letter Handling",
        "summary_rank": 7,
        "view_prompt": True
    },
   
   
    
      
    
}
