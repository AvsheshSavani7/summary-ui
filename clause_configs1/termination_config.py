TERMINATION_CLAUSES = {
    
    #Concise Summary

    "RTF for Regulatory - Concise": {
        "question": "RTF for Regulatory?",
        "conditions": [
            {
                "question": "RTF for Regulatory?",
                "if": "termination.reverse_termination_fee_regulatory.reverse_termination_fee_regulatory.answer",
                "type": "enum",
                "not_in": ["", "Not found", None],
                "true": {
                    "add_to_prompt": {
                        "reverse_termination_fee_regulatory": "{{reverse_termination_fee_regulatory.reverse_termination_fee_regulatory.clause_text}}",
                        "reverse_termination_fee_regulatory_text": "{{termination.reverse_termination_fee_regulatory.reverse_termination_fee_regulatory.clause_text}}"
                    }
                },
                "false": {}
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the termination provisions in a merger agreement.\n\n"
            "Task:\n"
            "- Determine whether a **reverse termination fee** is payable **due to a regulatory failure**.\n"
            "- If such a fee is specified:\n"
            "   - State the amount\n"
            "   - Identify the regulatory trigger (e.g., HSR denial, CFIUS block)\n"
            "   - Specify the party responsible for payment\n"
            "- If **no regulatory-based reverse termination fee** is specified, simply state:\n"
            "  'No reverse termination fee is payable due to regulatory failure.'\n"
            "- Do not reference or summarize any other fees or clauses.\n"
            "- Output a single sentence appropriate for legal and financial audiences.\n\n"
            "--- Clause: Summary Field\n"
            "{reverse_termination_fee_regulatory}\n\n"
            "--- Clause: Full Text Field\n"
            "{reverse_termination_fee_regulatory_text}\n\n"
            ">>> Example Output:\n"
            "Nippon owes a $565,000,000 reverse termination fee for failure to receive any required regulatory approval."
        ),
        "output_field": "rtf_regulatory",
        "reference_fields": [
            "termination.reverse_termination_fee_regulatory.reverse_termination_fee_regulatory.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph_with_bullets",
        "max_words": 25,
        "summary_display_section": "Regulatory",
        "summary_rank": 4.2,
        "view_prompt": True
    },

    "Termination for Superior Bid - Concise": {
        "question": "Termination for Superior Bid?",
        "conditions": [
            {
                "question": "Termination for Superior Bid?",
                "if": "termination.termination_fee_superior_proposal.termination_fee_superior_proposal_exists.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "termination_superior_bid": "{{termination.termination_fee_superior_proposal.termination_fee_superior_proposal_exists.clause_text}}",
                        "termination_superior_bid_amount": "{{termination.termination_fee_superior_proposal.termination_fee_superior_proposal.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the termination section of a merger agreement.\n\n"
            "Task:\n"
            "- Determine whether a reverse termination fee is payable if the merger is terminated due to a superior offer.\n"
            "-- If applicable, identify:\n"
            "   - The amount of the fee\n"
            "   - The triggering condition for the superior offer (e.g., HSR denial, CFIUS block)\n"
            "   - The responsible party\n"
            "-- If no such fee is payable, state this clearly.\n"
            "- Output a standalone paragraph appropriate for financial and legal audiences. Be specific and do not duplicate phrasing.\n\n"
            "--- Clause: Termination Fee for Superior Amoutn Details\n"
            "{termination_superior_bid}\n\n"
            "--- Clause: Termination Fee Amount for Superior Bid\n"
            "{termination_superior_bid_amount}\n\n"
            ">>> Example Output:\n"
            "X owes a $565,000,000 termination fee in connection with accepting a competing bid."
            "Termination fee of $272,000,000 for various reasons in connection with a Superior Proposal."
            "Reciprocal termination fees of $2.2bn in connection with accepting a competing bid."
        ),
        "output_field": "superior_offer",
        "reference_fields": [
            "termination.termination_fee_superior_proposal.termination_fee_superior_proposal.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 35,
        "summary_display_section": "Competing Bid",
        "summary_rank": 5.3,
        "view_prompt": True
    },

    "Reimbursement Expenses Identified - Concise": {
        "question": "Termination for Company Shareholder Approval Failure",
        "conditions": [
            {
                "question": "Target Reimbursements",
                "if": "termination.reimbursement_obligations.target_reimbursement_obligations.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "company_reimbursement_answer": "{{termination.reimbursement_obligations.target_reimbursement_obligations.answer}}",
                        "company_reimbursement_text": "{{termination.reimbursement_obligations.target_reimbursement_obligations.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            },

            {
                "question": "Parent Reimbursements",
                "if": "termination.reimbursement_obligations.parent_reimbursement_obligations.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "parent_reimbursement_answer": "{{termination.reimbursement_obligations.parent_reimbursement_obligations.answer}}",
                        "parent_reimbursement_text": "{{termination.reimbursement_obligations.parent_reimbursement_obligations.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            },
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the termination section of a merger agreement.\n\n"
            "Task:\n"
            "- Identify whether the agreement explicitly requires an expense reimbursement if the merger is terminated due to failure to obtain shareholder approval by either the company or the parent.\n"
            "- If an expense reimbursement is required under a termination provision that includes failure to receive shareholder approval as a cause, extract the relevant details.\n"
            "- Output one precise paragraph identifying:\n"
            "   - The amount of the reimbursement\n"
            "   - The conditions under which it applies (e.g., vote failure at shareholder meeting, with or without related conditions)\n"
            "   - The responsible party (Company or Parent)\n"
            "- If no such reimbursement obligation exists for vote failure, output: 'No reimbursement fees apply for failure to obtain shareholder approval.'\n\n"
            "-- Clause Texts\n"
            "-- Reimbursement Details Company\n"
            "{company_reimbursement_answer}\n\n"
            "-- Reimbursement Text Company\n"
            "{company_reimbursement_text}\n"
            "-- Reimbursement Details Parent\n"
            "{parent_reimbursement_answer}\n\n"
            "-- Reimbursement Text Parent\n"
            "{parent_reimbursement_text}\n\n"
            "--- Example Output:\n"
            "Reciprocal expense reimbursements up to $40,000,000 for failure to receive shareholder approval not in connection with an acquisition proposal."
        ),
        "output_field": "reimbursement_expenses",
        "reference_fields": [
            "termination.reimbursement_obligations.target_reimbursement_obligations.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 50,
        "summary_display_section": "Competing Bid",
        "summary_rank": 5.4,
        "view_prompt": True
    },

    "Termination for Parent Shareholder Approval Failure": {
        "question": "Termination for Parent Shareholder Approval Failure",
        "conditions": [
            {
                "question": "Termination for Parent Shareholder Approval Failure",
                "if": "termination.reverse_termination_fee_shareholder_approval.reverse_termination_fee_shareholder_approval_failure_exists.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "parent_shareholder_vote_approval": "{{termination.reverse_termination_fee_shareholder_approval.reverse_termination_fee_shareholder_approval_failure_exists.clause_text}}",
                        "parent_shareholder_vote_approval_details": "{{termination.reverse_termination_fee_shareholder_approval.reverse_termination_fee_shareholder_approval_failure.clause_text}}"
                    }
                },
                "false": {}
            },

            {
                "question": "Termination for Company Shareholder Approval Failure",
                "if": "termination.reimbursement_obligations.parent_reimbursement_obligations.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "parent_reimbursement_answer": "{{termination.reimbursement_obligations.parent_reimbursement_obligations.answer}}",
                        "parent_reimbursement_text": "{{termination.reimbursement_obligations.parent_reimbursement_obligations.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the termination section of a merger agreement.\n\n"
            "Task:\n"
            "- Determine whether a termination fee or expense reimbursement is explicitly payable if the merger is terminated **solely** due to failure to receive the **Parent’s** shareholder approval and **not** in connection with a superior offer or acquisition proposal.\n"
            "- This analysis must **exclude** any scenarios that involve, reference, or are conditioned on a superior proposal or acquisition proposal (e.g., proposals made, disclosed, not withdrawn, or consummated).\n"
            "- Do not infer a fee based on clauses that only apply when an acquisition proposal is present.\n"
            "- If an explicit standalone fee or reimbursement applies to this Parent vote failure scenario, output one clear paragraph identifying:\n"
            "   - The amount of the fee or reimbursement\n"
            "   - The conditions under which it applies (e.g., vote failure at Parent shareholder meeting)\n"
            "   - The responsible party\n"
            "- If **no such fee** is explicitly stated for this scenario, **state clearly that no fee applies.**\n"
            "- Write one paragraph suitable for a legal and financial audience. Use precise language, avoid duplication, and be specific.\n\n"
            "-- Clause: Parent Shareholder Vote Failure Scenario\n"
            "{parent_shareholder_vote_approval}\n\n"
            "-- Clause: Termination Fee or Expense Reimbursement Amount\n"
            "{parent_shareholder_vote_approval_details}\n\n"
            "-- Clause: Reimbursement Details\n"
            "{parent_reimbursement_answer}\n\n"
            "-- Clause: Reimbursement Text\n"
            "{parent_reimbursement_text}\n\n"
            "--- Example Output:\n"
            "The Parent is required to reimburse the Company up to $25,000,000 if the merger is terminated due to failure to obtain Parent shareholder approval, provided the failure is not connected to an acquisition proposal."
        ),
        "output_field": "parent_shareholder_vote_failure",
        "reference_fields": [
            "termination.reverse_termination_fee_shareholder_approval.reverse_termination_fee_shareholder_approval_failure_exists.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "OFF",
        "format_style": "paragraph",
        "max_words": 35,
        "summary_display_section": "Competing Bid",
        "summary_rank": 1,
        "view_prompt": True
    },

    #Fulsome Summary

    "Termination Mutual - Fulsome": {
        "question": "Termination Parent + Company",
        "conditions": [
            {
                "question": "Termination Parent + Company",
                "if": "termination.termination_rights.mutual_termination_rights.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "termination_mutual_answer": "{{termination.termination_rights.mutual_termination_rights.answer}}",
                        "termination_mutual_text": "{{termination.termination_rights.mutual_termination_rights.clause_text}}"
                    }
                },
                "false": {}
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the termination provisions in a merger agreement.\n\n"
            "Task:\n"
            "- Summarize the terminations available to both the parent and the company with a focus on clarity and not missing any details..\n"
            "- Do not reference or summarize any other clauses.\n"
            "- Output a single sentence appropriate for legal and financial audiences.\n\n"
            "--- Clause: Mutual Termination Answer\n"
            "{termination_mutual_answer}\n\n"
            "--- Clause: Mutual Termination Text\n"
            "{termination_mutual_text}\n\n"
            ">>> Example Output:\n"
            "Agreement may be terminated by either Company or Parent, if (i) the Merger shall not have been consummated by the End Date, (ii) an Order prevents closing, such order being final and non-appealable (provided such right shall not be available to any party whose breach has been the proximate cause of such Order), or either the (iii) Company Stockholder Approval or (iv) Parent Stockholder Approval has not been obtained.\n"
            "Agreement may be terminated by either Company or Parent, if (i) the Merger shall not have been consummated by the End Date, (ii) upon issuance of a final and non-appealable Legal Restraint (provided such right shall not be available to any party whose breach shall have proximately caused such Legal Restraint), or (iii) the Required Company Stockholder Vote was note received.\n"
            "Agreement may be terminated by either Parent of the Company if (i) the Merger shall not have been consummated on or before the Termination Date, (ii) any Restraint or Order has been enacted to prevent closing, such order being final and non-appealable (so long as such party hasn’t breached its obligations under Section 5.4), or (iii) AZEK has failed to receive shareholder approval.\n"
        ),
        "output_field": "mutual_termination",
        "reference_fields": [
            "termination.termination_rights.mutual_termination_rights.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 90,
        "summary_display_section": "Termination Rights",
        "summary_rank": 11.1,
        "view_prompt": True
    },

    "Termination Parent - Fulsome": {
        "question": "Termination Parent + Company",
        "conditions": [
            {
                "question": "Termination Parent + Company",
                "if": "termination.termination_rights.parent_termination_rights.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "termination_parent_answer": "{{termination.termination_rights.parent_termination_rights.answer}}",
                        "termination_parent_text": "{{termination.termination_rights.parent_termination_rights.clause_text}}"
                    }
                },
                "false": {}
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the termination provisions in a merger agreement.\n\n"
            "Task:\n"
            "- Summarize the terminations available to the parent without missing any key details.\n"
            "- Use the same numbering as found in the legal document if applicable.\n"
            "- Do not reference or summarize any other clauses.\n"
            "- Output a single sentence appropriate for legal and financial audiences.\n\n"
            "--- Clause: Parent Termination Answer\n"
            "{termination_parent_answer}\n\n"
            "--- Clause: Parent Termination Text\n"
            "{termination_parent_text}\n\n"
            ">>> Example Output:\n"
            "Agreement may be terminated by Parent (i) if a Company Adverse Recommendation Change has occurred or, following a Company Acquisition Proposal (including any material modification thereto), the Company board fails to publicly confirm the Company Board Recommendation within 10 Business Days of a written request from Parent; or (ii) if Company shall have breached or failed to perform any of its reps, warranties, covenants or other agreements, and such breach is either not capable of being cured or has not been cured by the earlier of the End Date or the date that is thirty calendar days following written notice of such breach (unless Parent is also in breach); or (iii) to agree to a Parent Superior Proposal.\n"
            "Agreement may be terminated by Parent if Company shall have breached or failed to perform any of its reps, warranties, covenants or other agreements, and such breach cannot be cured by the End Date or, if curable, is not cured within thirty Business Days following notice of such breach (provided Parent is not then in material breach).\n"
            "Agreement may be terminated by Parent if (i) Company shall have breached or failed to perform any of its reps, warranties, covenants or other agreements, and such breach is either not capable of being cured or has not been cured by the earlier of the Termination Date or the date that is thirty calendar days following written notice of such breach (unless Parent is also in breach) or (ii) the Company Board makes an Adverse Recommendation Change or fails to publicly reaffirm the Company Recommendation within 10 Business Days of a written request from Parent following receipt by the Company of an Acquisition Proposal, including any changes to price or other material terms of such proposal.\n"
        ),
        "output_field": "parent_termination",
        "reference_fields": [
            "termination.termination_rights.parent_termination_rights.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 125,
        "summary_display_section": "Termination Rights",
        "summary_rank": 11.2,
        "view_prompt": True
    },

    "Termination Company - Fulsome": {
        "question": "Termination Company",
        "conditions": [
            {
                "question": "Termination Company",
                "if": "termination.termination_rights.company_termination_rights.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "termination_company_answer": "{{termination.termination_rights.company_termination_rights.answer}}",
                        "termination_company_text": "{{termination.termination_rights.company_termination_rights.clause_text}}"
                    }
                },
                "false": {}
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the termination provisions in a merger agreement.\n\n"
            "Task:\n"
            "- Summarize the terminations available to the company without missing any key details.\n"
            "- Use the same numbering as found in the legal document if applicable.\n"
            "- Do not reference or summarize any other clauses.\n"
            "- Output a single sentence appropriate for legal and financial audiences.\n\n"
            "--- Clause: Company Termination Answer\n"
            "{termination_company_answer}\n\n"
            "--- Clause: Company Termination Text\n"
            "{termination_company_text}\n\n"
            ">>> Example Output:\n"
            "Agreement may be terminated by Company (i) if a Parent Adverse Recommendation Change has occurred or, following a Parent Acquisition Proposal (including any material modification thereto), the Parent board fails to publicly confirm the Parent Board Recommendation within 10 Business Days of a written request from Company; or (ii) if Parent shall have breached or failed to perform any of its reps, warranties, covenants or other agreements, and such breach is either not capable of being cured or has not been cured by the earlier of the End Date or the date that is thirty calendar days following written notice of such breach (unless Company is also in breach); or (iii) to agree to a Company Superior Proposal\n"
            "Agreement may be terminated by Company if Parent shall have breached or failed to perform any of its reps, warranties, covenants or other agreements, and such breach cannot be cured by the End Date or, if curable, is not cured within thirty Business Days following notice of such breach (provided Company is not then in material breach).\n"
            "Agreement may be terminated by the Company if (i) Parent shall have breached or failed to perform any of its reps, warranties, covenants or other agreements, and such  breach is either not capable of being cured or has not been cured by the earlier of the Termination Date or the date that is thirty calendar days following written notice of such breach (unless Company is also in breach) or (ii) the Company enters into a definitive agreement with respect to a Superior Proposal and pays the Termination Amount\n"
        ),
        "output_field": "company_termination",
        "reference_fields": [
            "termination.termination_rights.company_termination_rights.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 125,
        "summary_display_section": "Termination Rights",
        "summary_rank": 11.3,
        "view_prompt": True
    },

    "Termination Fee Amount - Fulsome": {
        "question": "Termination Company",
        "conditions": [
            {
                "question": "Termination Company",
                "if": "termination.termination_fee.termination_fee.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "termination_fee": "{{termination.termination_fee.termination_fee.answer}}",
                        "termination_fee_text": "{{termination.termination_fee.termination_fee.clause_text}}"
                    }
                },
                "false": {}
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the termination provisions in a merger agreement.\n\n"
            "Task:\n"
            "- Summarize concisely the termination fee amount.\n"
            "- Start with 'Company Termination Fee is'\n"
            "- Do not reference or summarize any other clauses.\n"
            "- Output a single phrase appropriate for legal and financial audiences.\n\n"
            "--- Clause: Termination Fee Amount:\n"
            "{termination_fee}\n\n"
            "--- Clause: Termination Fee Text\n"
            "{termination_fee_text}\n\n"
            ">>> Example Output:\n"
            "Company Termination Fee is equal to $2.2 billion.\n"
            "Company Termination Fee is equal to $565,000,000.\n"
            "Termination Amount is equal to $272,000,000.\n"
        ),
        "output_field": "termination_fee_amount",
        "reference_fields": [
            "termination.termination_fee.termination_fee.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 15,
        "summary_display_section": "Termination Fee Amounts",
        "summary_rank": 12.1,
        "view_prompt": True
    },

    "Termination Reverse Termination Amount - Fulsome": {
        "question": "Termination Company",
        "conditions": [
            {
                "question": "Termination Company",
                "if": "termination.reverse_termination_fee_exist.reverse_termination_fee_exist.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "reverse_termination_answer": "{{termination.reverse_termination_fee.reverse_termination_fee.answer}}",
                        "reverse_termination_text": "{{termination.reverse_termination_fee.reverse_termination_fee.clause_text}}"
                    }
                },
                "false": {
                    "text_output": "The contract does not specify a Reverse Termination Fee"
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the termination provisions in a merger agreement.\n\n"
            "Task:\n"
            "- Summarize concisely the reverse terminations without missing any key details if it exists, otherwise state 'There is no reverse termination fee.'\n"
            "- Use the same numbering as found in the legal document if applicable.\n"
            "- If there is a reverse termination fee start with 'Parent Termination Fee is'\n"
            "- Do not reference or summarize any other clauses.\n"
            "- Output a single phrase appropriate for legal and financial audiences.\n\n"
            "--- Clause: Company Termination Answer\n"
            "{reverse_termination_answer}\n\n"
            "--- Clause: Company Termination Text\n"
            "{reverse_termination_text}\n\n"
            ">>> Example Output:\n"
            "Parent Termination Fee is equal to $2.2 billion.\n"
            "Parent Termination Fee is equal to $565,000,000.\n"
            "There is no reverse termination fee.\n"
        ),
        "output_field": "company_termination",
        "reference_fields": [
            "termination.termination_rights.company_termination_rights.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 15,
        "summary_display_section": "Termination Fee Amounts",
        "summary_rank": 12.2,
        "view_prompt": True
    },

    "Termination Company Shall Pay Termination - Fulsome": {
        "question": "Termination Fee List",
        "conditions": [
            {
                "question": "Termination Fee List",
                "if": "termination.termination_fee_events.company_termination_fee_events.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "termination_fee_events_answer": "{{termination.termination_fee_events.company_termination_fee_events.answer}}",
                        "termination_fee_events_text": "{{termination.termination_fee_events.company_termination_fee_events.clause_text}}"
                    }
                },
                "false": {}
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the termination provisions in a merger agreement.\n\n"
            "Task:\n"
            "- Summarize the terminations fee events without missing any key details.\n"
            "- Use the same numbering as found in the legal document if applicable.\n"
            "- Do not reference or summarize any other clauses.\n"
            "- Output a single sentence appropriate for legal and financial audiences.\n\n"
            "--- Clause: Company Termination Answer\n"
            "{termination_fee_events_answer}\n\n"
            "--- Clause: Company Termination Text\n"
            "{termination_fee_events_text}\n\n"
            ">>> Example Output:\n"
            "Company shall pay the Company Termination Fee if the Agreement is terminated for various reasons related to a Company Acquisition Proposal.  If terminated by Company pursuant to Section 8.1(g)(i) [to enter into a Superior Proposal], then the fee is payable prior to or concurrently with termination.  If terminated by Parent pursuant to Section 8.1 (g)(ii) [Change of Recommendation], then fee is payable within 3 Business Days.  If terminated by either party pursuant to Section 8.1(d) [failure to receive the Required Company Stockholder vote] and an acquisition proposal was publicly disclosed and not withdrawn at least 2 Business Days prior to the Company Stockholders’ Meeting and an Alternative Proposal is entered into within 9 months of such termination, then the fee is payable within 3 Business Days of completing such transaction.\n"
        ),
        "output_field": "company_fee_termination",
        "reference_fields": [
            "termination.termination_fee_events.company_termination_fee_events.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 125,
        "summary_display_section": "Termination Fee Amounts",
        "summary_rank": 12.4,
        "view_prompt": True
    },

    "Termination Parent Shall Pay Reverse Termination - Fulsome": {
        "question": "Reverse Termination Fee List",
        "conditions": [
            {
                "question": "Reverse Termination Fee List",
                "if": "termination.termination_fee_events.parent_reverse_termination_fee_events.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "reverse_termination_fee_events_answer": "{{termination.termination_fee_events.parent_reverse_termination_fee_events.answer}}",
                        "reverse_termination_fee_events_text": "{{termination.termination_fee_events.parent_reverse_termination_fee_events.clause_text}}"
                    }
                },
                "false": {}
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the termination provisions in a merger agreement.\n\n"
            "Task:\n"
            "- Summarize the parent reverse termination fee events without missing any key details.\n"
            "- Use the same numbering as found in the legal document if applicable.\n"
            "- Do not reference or summarize any other clauses.\n"
            "- Output a single sentence appropriate for legal and financial audiences.\n\n"
            "--- Clause: Parent Reverse Termination Answer\n"
            "{reverse_termination_fee_events_answer}\n\n"
            "--- Clause: Parent Reverse Termination Text\n"
            "{reverse_termination_fee_events_text}\n\n"
            ">>> Example Output:\n"
            "Company shall pay the Company Termination Fee if the Agreement is terminated for various reasons related to a Company Acquisition Proposal.  If terminated by Company pursuant to Section 8.1(g)(i) [to enter into a Superior Proposal], then the fee is payable prior to or concurrently with termination.  If terminated by Parent pursuant to Section 8.1 (g)(ii) [Change of Recommendation], then fee is payable within 3 Business Days.  If terminated by either party pursuant to Section 8.1(d) [failure to receive the Required Company Stockholder vote] and an acquisition proposal was publicly disclosed and not withdrawn at least 2 Business Days prior to the Company Stockholders’ Meeting and an Alternative Proposal is entered into within 9 months of such termination, then the fee is payable within 3 Business Days of completing such transaction.\n"
        ),
        "output_field": "company_fee_termination",
        "reference_fields": [
            "termination.termination_fee_events.parent_reverse_termination_fee_events.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 125,
        "summary_display_section": "Termination Fee Amounts",
        "summary_rank": 12.5,
        "view_prompt": True
    },

    "Reimbursement Expenses Identified - Fusome": {
        "question": "Termination for Company Shareholder Approval Failure",
        "conditions": [
            {
                "question": "Target Reimbursements",
                "if": "termination.reimbursement_obligations.target_reimbursement_obligations.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "company_reimbursement_answer": "{{termination.reimbursement_obligations.target_reimbursement_obligations.answer}}",
                        "company_reimbursement_text": "{{termination.reimbursement_obligations.target_reimbursement_obligations.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            },

            {
                "question": "Parent Reimbursements",
                "if": "termination.reimbursement_obligations.parent_reimbursement_obligations.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "parent_reimbursement_answer": "{{termination.reimbursement_obligations.parent_reimbursement_obligations.answer}}",
                        "parent_reimbursement_text": "{{termination.reimbursement_obligations.parent_reimbursement_obligations.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            },
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the termination section of a merger agreement.\n\n"
            "Task:\n"
            "- Identify whether the agreement explicitly requires an expense reimbursement if the merger is terminated due to failure to obtain shareholder approval by either the company or the parent.\n"
            "- If an expense reimbursement is required under a termination provision that includes failure to receive shareholder approval as a cause, extract the relevant details.\n"
            "- Output one precise paragraph identifying:\n"
            "   - The amount of the reimbursement\n"
            "   - The conditions under which it applies (e.g., vote failure at shareholder meeting, with or without related conditions)\n"
            "   - The responsible party (Company or Parent)\n"
            "- If no such reimbursement obligation exists for vote failure, output: 'No reimbursement fees apply for failure to obtain shareholder approval.'\n\n"
            "-- Clause Texts\n"
            "-- Reimbursement Details Company\n"
            "{company_reimbursement_answer}\n\n"
            "-- Reimbursement Text Company\n"
            "{company_reimbursement_text}\n"
            "-- Reimbursement Details Parent\n"
            "{parent_reimbursement_answer}\n\n"
            "-- Reimbursement Text Parent\n"
            "{parent_reimbursement_text}\n\n"
            "--- Example Output:\n"
            "Reciprocal expense reimbursements up to $40,000,000 for failure to receive shareholder approval not in connection with an acquisition proposal."
        ),
        "output_field": "reimbursement_expenses",
        "reference_fields": [
            "termination.reimbursement_obligations.target_reimbursement_obligations.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 50,
        "summary_display_section": "Termination Rights",
        "summary_rank": 11.5,
        "view_prompt": True
    },

}
