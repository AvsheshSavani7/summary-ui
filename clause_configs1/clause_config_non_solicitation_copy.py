# =========================
# Test Config & Data
# =========================
CLAUSE_CONFIG = {

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
                        "target_notes": "Cap applies to Target units generating more than $140,000,000 in net sales during the Company's 2024 fiscal year."
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "target_notes": "No divestiture commitments are required under the terms of the agreement."
                    }
                }
            },
            {
                "question": "What are the Divestiture Comitments of the Parent",
                "if": "best_efforts.divestiture_commitments.divestiture_required.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "parent_notes": "Parent and its Subsidiaries shall not be required to agree to, commit to, proffer, propose or take any Remedy Actions with respect to any businesses and products of Parent and its Subsidiaries."
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "parent_notes": "No divestiture commitments are required under the terms of the agreement."
                    }
                }
            },
           
        ],
        "prompt_template": (
            "You are a legal and finance analyst summarizing M&A contract terms.:\n\n"
            "Write a single concise bullet summarizing the divestiture cap for the target based on the data below. Use professional tone and precise legal language.\n"
            "- Target Company Board: {target_notes}\n"
            "Write one single **concise bullet point**, no more than **25 words**, that explains the divestiture cap as it applies to the buyer and the buyer's businesses. "
            "Use precise legal language but avoid verbosity. If the buyer is not obligated to take any remedy actions on its business, clearly state that. "
            "If the cap is zero or not applicable, explicitly note it.\n\n"
            "- Parent Unanimity: {parent_notes}"
            "Combine the above into a single bullet point summary .use legal language."
        ),
        "output_field": "divestiture_commitments_summary",
        "reference_fields": ["best_efforts.divestiture_commitments.divestiture_cap_target_notes.reference_section","best_efforts.divestiture_commitments.divestiture_cap_parent_notes.reference_section"],
        "use_short_reference": True,
        "summary_type": "concise",
        "format_style": "bullet",
        "max_words":50,
        "summary_display_section": "Best Efforts",
        "summary_rank": 1,
        "view_prompt": False
    },
    
    "Best Efforts : Litigation Commitments": {
        "question": "summarize_litigation_commitment?",
       
        "conditions": [
            {
                "question": "litigation_requirement_status",
                "if": ".best_efforts.litigation_commitments.litigation_requirement_status.answer",
                "type": "enum",
                "value": "Explicit Requirement to Litigate",
                "true": {
                    "add_to_prompt": {
                        "litigation_requirement_status": "Parent is required to litigate in defense of the transaction."
                    }
                },
                "false": {
                    "litigation_requirement_status": "The agreement does not impose any obligation to litigate in defense of the transaction."
                }
            }
        ],
        "prompt_template": "Summarize the litigation requirement status in one line :\n\n- Details: {litigation_requirement_status}",
        "output_field": "litigation_requirement_summary",
        "reference_fields": ["best_efforts.litigation_commitments.litigation_requirement_status.reference_section"],
        "use_short_reference": True,
        "summary_type": "concise",
        "format_style": "bullet",
        "max_words": 25,
        "summary_display_section": "Best Efforts",
        "summary_rank": 1,
        "view_prompt": False
    },
      
    # FullSome Best Efforts 
    "Best Effort : HSR": {
        "question": "HSR",
        "conditions": [
            {
                "question": "HSR",
                "if": "best_efforts.regulatory_fillings_hsr.hsr_required.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "deadline": 25,
                        "notes": "Must file within 25 business days of signing; filing required under HSR Act as a condition to closing."
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "text_output": "HSR filing is not required under the agreement."
                    }
                }
            },
            #  {
            #     "question": "HSR",
            #     "if": "best_efforts.regulatory_fillings_hsr.hsr_required.answer",
            #     "type": "boolean",
            #     "true": {
            #         "add_to_prompt": {
            #             "notes": "Must file within 25 business days of signing; filing required under HSR Act as a condition to closing."
            #         }
            #     },
            #     "false": {
            #         "add_to_prompt": {
            #             "target_approval": "HSR filing is not required under the agreement."
            #         }
            #     }
            # },
          
              
        ],
        "prompt_template": (
            "Summarize the filing obligation for HSR in one bullet point.\n"
            "Deadline (if any): {deadline}\n"
            "Notes: {notes}\n"
            "Avoid redundancy. If both deadline and notes exist, combine them logically. Be concise and formal.\n"
        ),
        "output_field": "board_approval_summary",
        "reference_fields": ["best_efforts.regulatory_fillings_hsr.hsr_required.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_rank": 5,
        "view_prompt": False
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
                        "deadline": "Not found",
                        "notes": "Not found"
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "text_output": "CFIUS filing is not required under the agreement."
                    }
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
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_rank": 1,
        "view_prompt": False
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
                        "deadline": "Not found",
                        "notes": "Foreign filings may be required under applicable non-U.S. laws"
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "text_output": "Foreign regulatory filings are not required under the agreement."
                    }
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
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_rank": 1,
        "view_prompt": False
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
                        "standard": "Reasonable Best Efforts"
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
        "Use professional legal tone. If applicable, clarify that the standard applies to obtaining regulatory approvals.\n"
        ),
        "output_field": "effort_standard_summary",
        "reference_fields": ["best_efforts.regulatory_efforts.effort_standard.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words": 100,
        "summary_display_section": "Best Efforts",
        "summary_rank": 4,
        "view_prompt": False
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
                        "control_type":  "mutual_consent_required",
                        "notes":"Neither the Company nor Parent will withdraw any such filings or applications without the prior written consent of the other party, such consent not to be unreasonably withheld, conditioned or delayed.",
                        
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
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words": 100,
        "summary_display_section": "Best Efforts",
        "summary_rank": 1,
        "view_prompt": False
    },
    
    "Best Effort : Timing agreement": {
        "question": "withdrawal_and_timing_controls_timing",
        "conditions": [
            {
                "question": "withdrawal_and_timing_controls_timing",
                "if": "best_efforts.withdrawal_and_timing_controls_timing.timing_agreement_restriction.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "restriction": 'true',
                        "notes":"The parties are restricted from withdrawing any filings or applications under the HSR Act without the prior written consent of the other party, and such consent is not to be unreasonably withheld, conditioned, or delayed.",
                        
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
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words": 100,
        "summary_display_section": "Best Efforts",
        "summary_rank": 1,
        "view_prompt": False
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
                        "target_notes": "Cap applies to Target units generating more than $140,000,000 in net sales during the Company's 2024 fiscal year.",
                        "buyer_notes": "Parent and its Subsidiaries shall not be required to agree to, commit to, proffer, propose or take any Remedy Actions with respect to any businesses and products of Parent and its Subsidiaries.",
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "text_output": "No divestiture commitments apply under the agreement."
                    }
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
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_rank": 1,
        "view_prompt": False
    },
    
    "Best Effort : Prior Approval Commitment": {
        "question": "Prior Approval Commitment",
        "conditions": [
            {
                "question": "Prior Approval Commitment",
                "if": "best_efforts.prior_approval_commitment.addressed.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "addressed": 'false',
                        "summary": "Not Found"
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "text_output": "Prior Approval Commitment are not disclosed in the agreement."
                    }
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
        "reference_fields": ["best_efforts.prior_approval_commitment.addressed.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_rank": 1,
        "view_prompt": False
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
                        "restriction": True,
                        "notes" : "sell, divest, hold separate, lease, license, transfer, dispose of or otherwise encumber or impair or take any other action with respect to the Company's or any of their respective Affiliate's assets, properties, businesses or product lines",
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "text_output": "Transaction Interference are not disclosed in the agreement."
                    }
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
        "reference_fields": ["best_efforts.transaction_interference.restriction_on_other_transactions.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_rank": 1,
        "view_prompt": False
    },
        
    "Best Effort : Second Request Certification": {
        "question": "second_request_certification",
        "conditions": [
            {
                "question": "second_request_certification",
                "if": "best_efforts.second_request_certification.deadline_specified.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "deadline": 'Not Specified',
                        "notes" : "as promptly as reasonably practicable, but in any event no later than twenty-five (25) Business Days following the date of this Agreement",
                        "party" : "Both"
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "text_output": "Second Request Certification are not disclosed in the agreement."
                    }
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
        "reference_fields": ["best_efforts.second_request_certification.deadline_specified.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_rank": 1,
        "view_prompt": False
    },
    
    "Best Effort : FTC Warning Letter Handling": {
        "question": "ftc_warning_letter_handling",
        "conditions": [
            {
                "question": "ftc_warning_letter_handling",
                "if": "best_efforts.ftc_warning_letter_handling.addressed.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        
                            "addressed" : "Not Specified", 
                            "deadline": 'Not Specified',
                            "closing_impact" : "Silent",
                            "extra" : "Not Found",
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "text_output": "There is no consideration per the contract given to the receipt of an FTC warning letter."
                    }
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
        "reference_fields": ["best_efforts.ftc_warning_letter_handling.addressed.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Best Efforts",
        "summary_rank": 1,
        "view_prompt": False
    },
   
    #Concise Ordinary Course
    "Ordinary Course Covenant - Concise": {
        "question": "What are the efforts related to Ordinary Course - Concise",
        "conditions": [
            {
                "question": "Ordinary Course Efforts - Concise",
                "if": "ordinary_course.ordinary_course_covenant.concise_standard_summary.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "ordinary_course_info": "ordinary_course.ordinary_course_covenant.concise_standard_summary.clause_text"
                    }
                },
                "false": {
                    "text_output": "Ordinary Course of Business is not disclosed in the agreement."
                }
            }
        ],
        "prompt_template": (
            "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Identify the exact efforts standard stated in the clause.\n"
            "- Return a single sentence that uses the **exact language** from the clause.\n"
            "- Do not paraphrase, generalize, or interpret the meaning.\n"
            "- Do not provide examples, commentary, or additional context.\n"
            "- The sentence should begin naturally (e.g., 'The Company shall...') and reflect only what is written.\n\n"
            "Clause Text:\n"
            "{ordinary_course_info}"
        ),
        "output_field": "concise_standard_summary",
        
        "reference_fields": ["ordinary_course.ordinary_course_covenant.concise_standard_summary.reference_section"],
        "use_short_reference": False,
        
        "summary_type": "concise",
        "format_style": "paragraph",
        "max_words": 20,
        "summary_display_section": "Ordinary Course",
        "summary_rank": 1,
        "view_prompt": False
    },

 #Fullsome Ordinary Course
    "Ordinary Course Covenant - Fulsome": {
        "question": "What are the efforts related to Ordinary Course - Fulsome",
        "conditions": [
            {
                "question": "Ordinary Course Efforts - Fulsome",
                "if": "ordinary_course.ordinary_course_covenant.concise_standard_summary.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "ordinary_course_info": "ordinary_course.ordinary_course_covenant.concise_standard_summary.clause_text"
                    }
                },
                "false": {
                    "text_output": "Ordinary Course of Business is not disclosed in the agreement."
                }
            }
        ],
        "prompt_template": (
            "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Identify the exact efforts standard stated in the clause.\n"
            "- Summarize the clause language without losing any critical details and **exact language** from the clause.\n"
            "- Do not paraphrase, generalize, or interpret the meaning.\n"
            "- Do not provide examples, commentary, or additional context.\n"
            "Clause Text:\n"
            "{ordinary_course_info}"
        ),
        "output_field": "concise_standard_summary",
        
        "reference_fields": ["ordinary_course.ordinary_course_covenant.concise_standard_summary.reference_section"],
        "use_short_reference": False,
        
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words": 125,
        "summary_display_section": "Ordinary Course",
        "summary_rank": 1,
        "view_prompt": False
    },

    # Concise Board Approval
    "Board Approval": {
        "question": "Is board approval specified for the transaction?",
        "conditions": [
            {
                "question": "Target board approval",
                "if": "board_approval.board_approval.target_board_approval.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "target_approval": "The merger has been approved by the board of the Company."
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "target_approval": "The merger has not been approved by the board of the Company."
                    }
                }
            },
            {
                "question": "Target board unanimous",
                "if": "board_approval.board_approval.target_board_unanimous.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "target_unanimous": "The board of the Company approved unanimously."
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "target_unanimous": "The board of the Company did not approve unanimously."
                    }
                }
            },
            {
                "question": "Acquirer board approval",
                "if": "board_approval.board_approval.acquirer_board_approval.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "acquirer_approval": "The merger has been approved by the board of the Parent."
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "acquirer_approval": "The merger has not been approved by the board of the Parent."
                    }
                }
            },
            {
                "question": "Acquirer board unanimous",
                "if": "board_approval.board_approval.acquirer_board_unanimous.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "acquirer_unanimous": "The board of the Parent approved unanimously."
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "acquirer_unanimous": "The board of the Parent did not approve unanimously."
                    }
                }
            }
        ],
        "prompt_template": (
            "Summarize the board approval status for the merger:\n\n"
            "- Target Company Board: {target_approval}\n"
            "- Target Unanimity: {target_unanimous}\n"
            "- Parent Company Board: {acquirer_approval}\n"
            "- Parent Unanimity: {acquirer_unanimous}"
            "Combine the above into a single line summary of the board approval status.use legal language."
        ),
        "output_field": "board_approval_summary",
        "reference_fields": ["board_approval.board_approval.target_board_approval.reference_section"],
        "use_short_reference": True,
        "summary_type": "concise",
        "format_style": "bullet",
        "max_words":50,
        "summary_display_section": "Board Approval",
        "summary_rank": 3,
        "view_prompt": False
    },

    # FullSome Board Approval
    "Board Approval fullsome": {
        "question": "Is board approval specified for the transaction?",
        "conditions": [
            {
                "question": "Target board approval",
                "if": "board_approval.board_approval.target_board_approval.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "target_approval": "The merger has been approved by the board of the Company."
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "target_approval": "The merger has not been approved by the board of the Company."
                    }
                }
            },
            {
                "question": "Target board unanimous",
                "if": "board_approval.board_approval.target_board_unanimous.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "target_unanimous": "The board of the Company approved unanimously."
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "target_unanimous": "The board of the Company did not approve unanimously."
                    }
                }
            },
            {
                "question": "Acquirer board approval",
                "if": "board_approval.board_approval.acquirer_board_approval.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "acquirer_approval": "The merger has been approved by the board of the Parent."
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "acquirer_approval": "The merger has not been approved by the board of the Parent."
                    }
                }
            },
            {
                "question": "Acquirer board unanimous",
                "if": "board_approval.board_approval.acquirer_board_unanimous.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "acquirer_unanimous": "The board of the Parent approved unanimously."
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "acquirer_unanimous": "The board of the Parent did not approve unanimously."
                    }
                }
            }
        ],
        "prompt_template": (
            "Summarize the board approval status for the merger:\n\n"
            "- Target Company Board: {target_approval}\n"
            "- Target Unanimity: {target_unanimous}\n"
            "- Parent Company Board: {acquirer_approval}\n"
            "- Parent Unanimity: {acquirer_unanimous}"
            "Combine the above into a single line summary of the board approval status.use legal language."
        ),
        "output_field": "board_approval_summary",
        "reference_fields": ["board_approval.board_approval.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Board Approval",
        "summary_rank": 3,
        "view_prompt": False
    },

     # Concise Closing Mechanics
   
   # Concise Claosing Mechanics
    "Closing Mechanics": {
        "question": "Does the agreement include a closing date?",
        "conditions": [
            {
                "question": "Is a closing date included?",
                "if": "closing_mechanics.target_date.target_date.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "closing_date": "March 23, 2025"
                    }
                    
                },
                "false": {
                    "text_output": "No closing date is included in the agreement."
                }
            }
           
            
        ],
        "prompt_template": (
            "Summarize the closing date for the merger:\n\n"
            "- Clause Text: {closing_date}"
        ),
        "output_field": "closing_date_summary",
        "reference_fields": [
        "closing_mechanics.target_date.target_date.reference_section"
        ],

        "use_short_reference": True,
        "summary_type": "concise",
        "format_style": "paragraph",
        "max_words": 50,
        "summary_display_section": "Closing Mechanics",
        "summary_rank": 4,
        "view_prompt": False
    },


     # FullSome Closing Mechanics
   
   # FullSome Closing Mechanics
    "Closing Mechanics fullsome": {
        "question": "Is board approval specified for the transaction?",
        "conditions": [
            {
                "question": "Target board approval",
                "if": "closing_mechanics.marketing_period.has_marketing_period.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "marketing_period": "Not found"
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "marketing_period": "The marketing period is not specified in the agreement."
                    }
                }
            },
            {
                "question": "Target board unanimous",
                "if": "closing_mechanics.inside_date.has_inside_date.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "inside_date": "Not found"
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "inside_date": "The inside date is not specified in the agreement."
                    }
                }
            },
            
        ],
        "prompt_template": (
            "Summarize the closing mechanics for the merger:\n\n"
            "- Marketing Period: {marketing_period}\n"
            "- Inside Date: {inside_date}\n"
            "Combine the above into a single line summary of the closing mechanics.use legal language."
        ),
        "output_field": "closing_mechanics_summary",
        "reference_fields": ["closing_mechanics.marketing_period.marketing_period_details.reference_section", "closing_mechanics.inside_date.inside_date_details.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Closing Mechanics",
        "summary_rank": 4,
        "view_prompt": False
    },

    # Concise Non Solicitation
    "Non Solicitation : Match Right": {
        "question": "Is match right specified for the transaction?",
        "conditions": [
            {
                "question": "Match Right",
                "if": "non_solicitation.match_right.match_right_initial_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "match_right": "The Company has provided Parent a copy of the proposed definitive agreements and other proposed transaction documentation between the Company and the Person making such Superior Proposal, if any, (C) for a period of four (4) Business Days following the notice delivered pursuant to clause (A) of this Section 5.6(d), the Company shall have discussed and negotiated in good faith (in each case only if Parent desires to negotiate) with Parent's Representatives any proposed modifications to the terms and conditions of this Agreement or the transactions contemplated by this Agreement so that the Acquisition Proposal is no longer a Superior Proposal.",
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "match_right": "A right-to-match was not included in the merger contract."
                    }
                }
            }
            
        ],
        "prompt_template": (
            "If the text below describes a right-to-match period in a merger agreement, summarize it with the number "
            "of days (in digits) and who holds the right. Format like:\n"
            "- Match Right: {match_right}\n"
            
        ),
        "output_field": "match_right_explanation",
        "reference_fields": ["non_solicitation.match_right.match_right_initial_included.reference_section","non_solicitation.match_right.match_right_explanation.reference_section"],
        "use_short_reference": True,
        "summary_type": "concise",
        "format_style": "bullet",
        "max_words":50,
        "summary_display_section": "Non Solicitation",
        "summary_rank": 5,
        "view_prompt": False
    },

    # Fullsome Non Solicitation

    "Non Solicitation : Go Shop": {
        "question": "Is go shop specified for the transaction?",
        "conditions": [
            {
                "question": "Go Shop",
                "if": "non_solicitation.go_shop.go_shop_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "go_shop": "The Company is permitted to engage with third parties regarding Acquisition Proposals under certain conditions prior to obtaining Company Stockholder Approval.",
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "go_shop": "There is no go-shop or window-shop provision.."
                    }
                }
            },
            
            
        ],
        "prompt_template": (
             "Summarize this go-shop clause in 1–2 sentences. Focus on whether the Company may solicit "
            "competing proposals after signing and any restrictions.\n\nText:\n"
            "- {go_shop}\n"
        ),
        "output_field": "go_shop_explanation",
        "reference_fields": ["non_solicitation.go_shop.go_shop_included.reference_section", "non_solicitation.go_shop.go_shop_explanation.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":60,
        "summary_display_section": "Non Solicitation",
        "summary_rank": 5,
        "view_prompt": False
    }   ,
    
    "Non Solicitation : Notice of Competing Offer": {
        "question": "Is notice of competing offer specified for the transaction?",
        "conditions": [
            {
                "question": "Notice of Competing Offer",
                "if": "non_solicitation.notice_of_competing_offer.notice_of_competing_offer_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "notice_of_competing_offer": "The Company is required to promptly (and in any case within twenty-four (24) hours) provide Parent notice of the receipt of any Acquisition Proposal, which notice shall include a complete, unredacted copy of all written proposals, written indications of interest or draft agreements relating to, or other written materials that describe any of the material terms and conditions of, such Acquisition Proposal, and disclose the identity of the other party (or parties) and the material terms of such inquiry, offer, proposal or request.",
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "notice_of_competing_offer": "The merger contract did not specify any details related to a Notice of Competing Offer."
                    }
                }
            },
            
            
        ],
        "prompt_template": (
            "Summarize the notice requirements below. Focus on what the Company must notify Parent about, "
            "the timing (e.g., 24 hours), and the types of proposals or discussions covered.\n\nText:\n"
            "- {notice_of_competing_offer}\n"
        ),
        "output_field": "notice_of_competing_offer_explanation",
        "reference_fields": ["non_solicitation.no_shop_clause.no_shop_clause_included.reference_section", "non_solicitation.notice_of_competing_offer.notice_of_competing_offer_explanation.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":80,
        "summary_display_section": "Non Solicitation",
        "summary_rank": 5,
        "view_prompt": False
    }   ,
    
    "Non Solicitation : Ongoing Update": {
        "question": "Is ongoing update specified for the transaction?",
        "conditions": [
            {
                "question": "Ongoing Update",
                "if": "non_solicitation.ongoing_update.ongoing_update_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "ongoing_update": "The Company is obligated to promptly provide updates to the Parent within twenty-four (24) hours regarding any Acquisition Proposal, including copies of all written proposals and material terms, and keep Parent informed on a reasonably prompt basis of any significant developments.",
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "ongoing_update": "Ongoing update requirement information is not available."
                    }
                }
            },
            
            
        ],
        "prompt_template": (
             "Summarize the ongoing update requirement. Focus on how frequently the Company must update Parent "
            "(e.g., within 24 hours) and about what kinds of developments.\n\nText:\n"
            " {ongoing_update}\n"
        
        ),
        "output_field": "ongoing_update_explanation",
        "reference_fields": ["non_solicitation.ongoing_update.ongoing_update_included.reference_section", "non_solicitation.ongoing_update.ongoing_update_explanation.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":80,
        "summary_display_section": "Non Solicitation",
        "summary_rank": 5,
        "view_prompt": False
    }   ,
    
    "Non Solicitation : Superior Proposal Engagement": {
        "question": "Is superior proposal engagement specified for the transaction?",
        "conditions": [
            {
                "question": "Superior Proposal Engagement",
                "if": "non_solicitation.superior_proposal_engagement.superior_proposal_engagement_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "superior_proposal_engagement": "The Company is authorized to engage with third parties if a Superior Proposal is received, provided the Company Board determines in good faith that such proposal constitutes or is reasonably likely to constitute a Superior Proposal.",
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "superior_proposal_engagement": "No details available related to Superior Offers."
                    }
                }
            },
            
            
        ],
        "prompt_template": (
             "Summarize the engagement procedure when a Superior Proposal is received. "
            "Describe notice obligations to Parent, initial match rights (e.g., 4 Business Days), "
            "and any follow-on rights if the Superior Proposal changes.\n\nText:\n"
            "-{superior_proposal_engagement}\n"
           
        ),
        "output_field": "superior_proposal_engagement_explanation",
        "reference_fields": ["non_solicitation.superior_proposal_engagement.superior_proposal_engagement_included.reference_section", "non_solicitation.superior_proposal_engagement.superior_proposal_engagement_explanation.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":150,
        "summary_display_section": "Non Solicitation",
        "summary_rank": 5,
        "view_prompt": False
    },

    "Non Solicitation : Adverse Recommendation - Superior Proposal": {
        "question": "Is superior proposal engagement specified for the transaction?",
        "conditions": [
            {
                "question": "Adverse Recommendation - Superior Proposal",
                "if": "non_solicitation.adverse_recommendation_change_superior_proposal_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "adverse_recommendation_change_superior_proposal": "The Company Board is permitted to change its recommendation in response to a Superior Proposal."
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "adverse_recommendation_change_superior_proposal": "No adverse recommendation change provision related to a Superior Proposal was included in the merger contract."
                    }
                }
            },
            
            
        ],
        "prompt_template": (
             "Summarize the Company Board's ability to change its recommendation due to a Superior Proposal. "
            "Explain the fiduciary duty standard, good faith requirements, and any timing or notice obligations.\n\nText:\n"
            "-{adverse_recommendation_change_superior_proposal}\n"
           
        ),
        "output_field": "adverse_recommendation_change_superior_proposal_explanation",
        "reference_fields": ["non_solicitation.adverse_recommendation_change_superior_proposal_included.reference_section", "non_solicitation.adverse_recommendation_change_superior_proposal_explanation.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":150,
        "summary_display_section": "Non Solicitation",
        "summary_rank": 5,
        "view_prompt": False
    },

    "Non Solicitation : Adverse Recommendation - Intervening Event": {
        "question": "Is superior proposal engagement specified for the transaction?",
        "conditions": [
            {
                "question": "Adverse Recommendation - Intervening Event",
                "if": "non_solicitation.adverse_recommendation_change_intervening_event_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "adverse_recommendation_change_intervening_event": "The Company Board may, in response to an Intervening Event, take any action prohibited by clause (i) of Section 5.6(c), only if (i) the Company Board determines in good faith, after consultation with its outside financial advisors and outside legal counsel, that the failure to take such action would be inconsistent with its fiduciary duties under applicable Law, (ii) the Company has notified Parent in writing that the Company Board intends to effect such an Adverse Recommendation Change pursuant to this Section 5.6(e) (which notice shall specify the facts and circumstances providing the basis of the Intervening Event and for the Company Board's determination to effect such an Adverse Recommendation Change in reasonable detail), (iii) for a period of four (4) Business Days following the notice delivered pursuant to clause (ii) of this Section 5.6(e), the Company shall have discussed and negotiated in good faith (in each case only if Parent desires to negotiate) with Parent's Representatives any proposed modifications to the terms and conditions of this Agreement or the transactions contemplated by this Agreement so that the failure to take such action would no longer be inconsistent with the Company Board's fiduciary duties under applicable Law (it being understood and agreed that any material change to the relevant facts and circumstances shall require a new notice and a new negotiation period that shall expire on the later to occur of (A) two (2) Business Days following delivery of such new notice from the Company to Parent and (B) the expiration of the original four (4) Business Day period described above in this clause (iii)), and (iv) no earlier than the end of such negotiation period, the Company Board shall have determined in good faith, after consultation with its outside financial advisors and outside legal counsel, and after considering the terms of any proposed amendment or modification to this Agreement, that the failure to take such action would still be inconsistent with its fiduciary duties under applicable Law.",
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "adverse_recommendation_change_intervening_event": "No adverse recommendation change provision related to an Intervening Event was included in the merger contract."
                    }
                }
            },
            
            
        ],
        "prompt_template": (
             "Summarize the Company Board's right to change its recommendation due to an Intervening Event. "
            "Include fiduciary duty language, good faith standards, and notice obligations.\n\nText:\n"
            "-{adverse_recommendation_change_intervening_event}\n"
           
        ),
        "output_field": "adverse_recommendation_change_intervening_event_explanation",
        "reference_fields": ["non_solicitation.adverse_recommendation_change_intervening_event_included.reference_section", "non_solicitation.adverse_recommendation_change_intervening_event_explanation.reference_section"],
        "use_short_reference": True,
        "summary_type": "fulsome",
        "format_style": "paragraph",
        "max_words":150,
        "summary_display_section": "Non Solicitation",
        "summary_rank": 5,
        "view_prompt": False
    },
    
   
}
print("Config file loaded with clauses:", list(CLAUSE_CONFIG.keys()))