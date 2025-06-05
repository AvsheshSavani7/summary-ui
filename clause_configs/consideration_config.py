CONSIDERATION_CLAUSES = {

    "Consideration Details - Concise": {
        "question": "Consideration Details",
        "conditions": [
            {
                "question": "Consideration Details",
                "if": "complex_consideration_and_dividends.deal_consideration.deal_consideration_details.answer",
                "type": "non_empty",
                "true": {
                    "add_to_prompt": {
                        "consideration_details": "{{complex_consideration_and_dividends.deal_consideration.deal_consideration_details.clause_text}}",
                        "exchange_details": "{{complex_consideration_and_dividends.collar.collar_exists.clause_text}}",
                        "cvr_details": "{{complex_consideration_and_dividends.cvr.cvr_details.clause_text}}"
                    }
                },
                "false": {
                    "text_output": "Consideration details not specified per the contract"
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing the merger consideration terms in a merger agreement.\n\n"
            "Task:\n"
            "- Return a single, consolidated sentence describing what each share of the target company will be entitled to receive.\n"
            "- Start the sentence with the name of the target company followed by 'stockholders are entitled to receive'.\n"
            "- Use only the information that is clearly applicable and stated in the clause text.\n"
            "- Include all consideration elements: cash, stock, and/or CVRs (Contingent Value Rights), if applicable.\n"
            "- If a stock-for-stock component is described but lacks a specific numeric exchange ratio, summarize as 'a number of [Acquirer] shares per [Target] share' or similar.\n"
            "- If parties are not explicitly named in the clause, infer them using surrounding context or typical roles (e.g., Parent = Acquirer, Company = Target).\n"
            "- Do not include extra legal context or phrases like 'from Parent' or 'without interest'.\n"
            "- Be concise but ensure clarity on who gives and who receives in share exchanges.\n\n"
            "-- You are reviewing the following three clauses:\n"
            "1. Consideration Details: {consideration_details}\n"
            "2. Exchange Ratio Details: {exchange_details}\n"
            "3. CVR (Contingent Value Right) Details: {cvr_details}\n\n"
            "--- Examples:\n"
            "CELG stockholders are entitled to receive $50 in cash, 1 BMY share and 1 CVR per CELG share.\n"
            "X shareholders are entitled to receive $55 per share in cash.\n"
            "AZEK stockholders are entitled to receive $26.45 in cash and 1.0340 JHX shares per AZEK share.\n"
            "XYZ stockholders are entitled to receive $42.00 in cash and a number of Acquirer shares per share of XYZ.\n"
            "\n"
            "Format the response in a paragraph style."
        ),


        "output_field": "confidentiality_summary",
        "reference_fields": ["complex_consideration_and_dividends.cvr.cvr_details.reference_section"],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 50,
        "summary_display_section": "Consideration",
        "summary_rank": 1,
        "view_prompt": True
    },

    "Target Dividends - Concise": {
        "question": "Consideration Details",
        "conditions": [
            {
                "question": "Consideration Details",
                "if": "complex_consideration_and_dividends.company_dividends.company_dividends_can_pay.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "company_dividends": "{{complex_consideration_and_dividends.company_dividends.company_dividends_can_pay.clause_text}}"
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "company_dividends": "{{complex_consideration_and_dividends.company_dividends.company_dividends_can_pay.clause_text}}"
                    }
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a merger agreement for dividend-related provisions.\n\n"
            "Task:\n"
            "- Return a single, clear sentence stating whether the target company is permitted to pay dividends prior to closing.\n"
            "- If dividends are permitted, include any relevant details such as limits, timing, or references to other documents (e.g., Company Disclosure Letter).\n"
            "- If dividends are not permitted, state that clearly.\n"
            "- Do not include any legal disclaimers, party names, or interpretation beyond the clause text.\n"
            "- Use concise legal summary language.\n\n"
            "-- You are reviewing the following clause:\n"
            "1. Company Dividends: {company_dividends}\n\n"
            "--- Examples:\n"
            "The Company is not permitted to pay dividends prior to closing.\n"
            "The Company may continue to pay quarterly dividends as specified in the Company Disclosure Letter.\n"
            "Dividends are only allowed if declared in the ordinary course and consistent with past practice.\n\n"
            "Format the response in a paragraph style."
        ),


        "output_field": "company_dividends",
        "reference_fields": ["complex_consideration_and_dividends.company_dividends.company_dividends_can_pay.reference_section"],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 30,
        "summary_display_section": "Consideration",
        "summary_rank": 2,
        "view_prompt": True
    },

    "Parent Dividends - Concise": {
        "question": "Consideration Details",
        "conditions": [
            {
                "question": "Consideration Details",
                "if": "complex_consideration_and_dividends.parent_dividends.parent_dividends_can_pay.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "parent_dividends": "{{ccomplex_consideration_and_dividends.parent_dividends.parent_dividends_can_pay.clause_text}}"
                    }
                },
                "false": {
                    "add_to_prompt": {
                        "parent_dividends": "{{complex_consideration_and_dividends.parent_dividends.parent_dividends_can_pay.clause_text}}"
                    }
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a merger agreement for dividend-related provisions concerning the Parent (acquirer).\n\n"
            "Task:\n"
            "- Return a single, clear sentence stating whether the Parent is permitted to pay dividends prior to closing.\n"
            "- If dividends are permitted, include relevant details such as limits, timing, or references to other documents (e.g., Parent Disclosure Letter).\n"
            "- If dividends are not permitted, state that clearly.\n"
            "- Do not include any legal disclaimers, full party names, or interpretation beyond the clause text.\n"
            "- Use concise legal summary language.\n\n"
            "-- You are reviewing the following clause:\n"
            "1. Parent Dividends: {parent_dividends}\n\n"
            "--- Examples:\n"
            "Parent may pay regular quarterly dividends not to exceed $0.41 per share.\n"
            "Parent is not permitted to declare or pay any dividends prior to closing.\n\n"
            "Format the response in a paragraph style."
        ),

        "output_field": "parent_dividends",
        "reference_fields": ["complex_consideration_and_dividends.parent_dividends.parent_dividends_can_pay.reference_section"],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 30,
        "summary_display_section": "Consideration",
        "summary_rank": 3,
        "view_prompt": True
    },

    "Proration - Concise": {
        "question": "Proration",
        "conditions": [
            {
                "question": "Proration",
                "if": "complex_consideration_and_dividends.proration.proration_exists.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "proration_clause": "{{complex_consideration_and_dividends.proration.proration_exists.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a merger agreement clause for proration mechanics.\n\n"
            "Task:\n"
            "- Determine if the proration clause explicity explains proration mechanics. \n"
            "- If an only if the clause explicitly details proration mechanics, create a summary of those mechanics\n"
            "- If the clause does not explicityly detail specific proration mechanics as they apply to the merger, return nothing, not an explanation explaining why, just nothing\n"
            "-- You are reviewing the following clause:\n"
            "1. Proration Clause: {proration_clause}\n\n"
            "--- Example of valid output:\n"
            "Consideration will be prorated between cash and stock based on aggregate election results and subject to allocation procedures.\n\n"
            "--- If proration is not clearly described:\n"
            "[Return nothing — leave blank]\n\n"
            "Do not exceed 35 words. Format as a single sentence paragraph. Do not return anything unless proration terms are clearly described."

        ),
        "output_field": "proration_summary",
        "reference_fields": ["complex_consideration_and_dividends.proration.proration_exists.reference_section"],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 35,
        "summary_display_section": "Consideration",
        "summary_rank": 4,
        "view_prompt": True
    },

    "Election - Concise": {
        "question": "Election",
        "conditions": [
            {
                "question": "Election",
                "if": "ccomplex_consideration_and_dividends.election.election_exists.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "election_clause": "{{ccomplex_consideration_and_dividends.election.election_exists.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a merger agreement clause for consideration election rights.\n\n"
            "Task:\n"
            "- Determine whether stockholders are permitted to elect the form of merger consideration (e.g., cash vs. stock).\n"
            "- If election rights are clearly described, return a single sentence summarizing the existence of those rights and any relevant limitations or procedures.\n"
            "- If the clause does not clearly state that elections are allowed, return nothing — leave the output blank.\n\n"
            "-- You are reviewing the following clause:\n"
            "1. Consideration Election Clause: {election_clause}\n\n"
            "--- Example of valid output:\n"
            "Stockholders may elect to receive either cash or stock, subject to aggregate limits and allocation procedures.\n\n"
            "--- If election rights are not clearly stated:\n"
            "[Return nothing — leave output blank]\n\n"
            "Do not exceed 30 words. Format as a single-sentence paragraph. Do not interpret beyond the clause text. Only respond if elections are clearly described."
        ),
        "output_field": "election_summary",
        "reference_fields": ["ccomplex_consideration_and_dividends.election.election_exists.reference_section"],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 35,
        "summary_display_section": "Consideration",
        "summary_rank": 5,
        "view_prompt": True
    },

    "CVR - Concise": {
        "question": "CVR",
        "conditions": [
            {
                "question": "CVR",
                "if": "complex_consideration_and_dividends.cvr.cvr_exists.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "cvr_clause": "{{complex_consideration_and_dividends.cvr.cvr_exists.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a merger agreement clause for Contingent Value Rights (CVRs).\n\n"
            "Task:\n"
            "- Determine whether the merger consideration includes CVRs.\n"
            "- If CVRs are clearly included, return a single sentence summarizing their inclusion and any relevant details stated in the clause (e.g., quantity per share, conditions).\n"
            "- If the clause does not clearly mention or describe CVRs, return nothing — leave the output blank.\n\n"
            "-- You are reviewing the following clause:\n"
            "1. CVR Clause: {cvr_clause}\n\n"
            "--- Example of valid output:\n"
            "Each Company share will receive one CVR in addition to the cash and stock consideration.\n\n"
            "--- If CVRs are not clearly included:\n"
            "[Return nothing — leave output blank]\n\n"
            "Format as a single-sentence paragraph. Only respond if CVRs are clearly described."
        ),
        "output_field": "cvr_summary",
        "reference_fields": ["complex_consideration_and_dividends.cvr.cvr_exists.reference_section"],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 35,
        "summary_display_section": "Consideration",
        "summary_rank": 6,
        "view_prompt": True
    },

    "Ticking Fees - Concise": {
        "question": "Ticking Fees",
        "conditions": [
            {
                "question": "Ticking Fees",
                "if": "complex_consideration_and_dividends.ticking_fees.ticking_fees_exists.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "ticking_fees_clause": "{{complex_consideration_and_dividends.ticking_fees.ticking_fees_exists.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a merger agreement clause for ticking fee provisions.\n\n"
            "Task:\n"
            "- Determine whether the agreement includes a ticking fee, which is a per-day or per-share payment triggered by deal delays.\n"
            "- If a ticking fee is clearly described, return a single sentence summarizing its existence, amount, and any relevant timing or conditions.\n"
            "- If the clause does not clearly mention a ticking fee, return nothing — leave the output blank.\n\n"
            "-- You are reviewing the following clause:\n"
            "1. Ticking Fee Clause: {ticking_fees_clause}\n\n"
            "--- Example of valid output:\n"
            "If the transaction is not completed by July 1, 2024, a daily ticking fee of $0.01 per share will be paid to stockholders.\n\n"
            "--- If ticking fees are not clearly included:\n"
            "[Return nothing — leave output blank]\n\n"
            "Format as a single-sentence paragraph. Only respond if ticking fees are clearly described."
        ),
        "output_field": "ticking_fees_summary",
        "reference_fields": ["complex_consideration_and_dividends.ticking_fees.ticking_fees_exists.reference_section"],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 45,
        "summary_display_section": "Consideration",
        "summary_rank": 7,
        "view_prompt": True
    },

    "Collar - Concise": {
        "question": "Collar",
        "conditions": [
            {
                "question": "Collar",
                "if": "complex_consideration_and_dividends.collar.collar_exists.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "collar_clause": "{{complex_consideration_and_dividends.collar.collar_exists.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            }
        ],
        "prompt_template": (
            "You are a legal analyst reviewing a merger agreement clause for collar provisions.\n\n"
            "Task:\n"
            "- Determine whether the merger consideration includes a collar mechanism, typically setting upper and lower bounds on the value of stock consideration based on share price fluctuations.\n"
            "- If a collar is clearly described, return a single sentence summarizing its existence, bounds (e.g., upper/lower limits), and how it affects the exchange ratio or consideration.\n"
            "- If the clause does not clearly mention a collar, return nothing — leave the output blank.\n\n"
            "-- You are reviewing the following clause:\n"
            "1. Collar Clause: {collar_clause}\n\n"
            "--- Example of valid output:\n"
            "The exchange ratio is subject to a collar if Parent’s stock trades outside the $85 to $105 range.\n\n"
            "--- If no collar provisions are clearly included:\n"
            "[Return nothing — leave output blank]\n\n"
            "Format as a single-sentence paragraph. Only respond if a collar is clearly described."
        ),
        "output_field": "collar_summary",
        "reference_fields": ["complex_consideration_and_dividends.collar.collar_exists.reference_section"],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 45,
        "summary_display_section": "Consideration",
        "summary_rank": 8,
        "view_prompt": True
    }

}
