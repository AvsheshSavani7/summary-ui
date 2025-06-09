NON_SOLICITATION_CLAUSES = {

    #Consise Summaries
    "Non Solicitation : Match Right Concise": {
        "question": "Timing related to Match Right",
        "conditions": [
            {
                "question": "What is the Match Right Timing",
                "if": "non_solicitation.match_right.match_right_initial_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "match_right": "{{non_solicitation.match_right.match_right_initial_explanation.clause_text}}",
                        "match_right_ammended": "{{non_solicitation.match_right.match_right_amended_included.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            }
        ],
        "prompt_template": (
            "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Identify the exact timing allowed for matching an offer.\n"
            "- Include both the initial right-to-match period and, if stated separately, the period for responding to amended or revised proposals.\n"
            "- Return a single concise sentence using the **exact language** from the clause(s) with a focus on timing.\n"
            "- Do not paraphrase, generalize, or interpret the meaning.\n"
            "- Do not provide examples, commentary, or additional context.\n"
            "=== Examples ===\n"
            "Example 1:\n"
            "Reciprocal four Business Day right-to-match any Company/Parent Superior Proposal; and two Business Days for any subsequent amended proposals.\n"
            "\nExample 2:\n"
            "Nippon has a 5 Business Day right-to-match any Superior Proposal; and 3 Business Days for any subsequent amended proposals.\n"
            "\nExample 3:\n"
            "JHX has a four Business Day right-to-match any Acquisition Proposal; and two Business Days for any subsequent amended proposals.\n"
            "\n=== Clause Text to Analyze ===\n"
            "- Initial Right to Match: {match_right}\n"
            "- Amended Right to Match: {match_right_ammended}\n"
        ),
        "output_field": "match_right_explanation",
        "reference_fields": [
            "non_solicitation.match_right.match_right_initial_included.reference_section",
            "non_solicitation.match_right.match_right_explanation.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 20,
        "summary_display_section": "Competing Bid",
        "summary_rank": 5.2,
        "view_prompt": True
    },

    "Non Solicitation : Go Shop": {
        "question": "Is a go-shop specified for the transaction?",
        "conditions": [
            {
                "question": "Is a go-shop specified for the transaction?",
                "if": "non_solicitation.go_shop.go_shop_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "go_shop": "{{non_solicitation.go_shop.go_shop_included.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            }
        ],
        "prompt_template": (
            "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Summarize in 1-2 sentences the go-shop provision details and limitations.\n"
            "- Use the **exact language** from the clause.\n"
            "- Do not paraphrase, generalize, or interpret the meaning.\n"
            "- Do not provide examples, commentary, or additional context.\n\n"
            "-- Clause Text:\n"
            "-- {go_shop}\n"
        ),
        "output_field": "go_shop_explanation",
        "reference_fields": [
            "non_solicitation.go_shop.go_shop_included.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Concise",
        "format_style": "paragraph",
        "max_words": 25,
        "summary_display_section": "Competing Bid",
        "summary_rank": 5.1,
        "view_prompt": True
    },


    #Fulsome Summaries
    "Non Solicitation : Match Right Fulsome": {
        "question": "Timing related to Match Right",
        "conditions": [
            {
                "question": "What is the Match Right Timing",
                "if": "non_solicitation.match_right.match_right_initial_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "match_right": "{{non_solicitation.match_right.match_right_initial_explanation.clause_text}}",
                        "match_right_ammended": "{{non_solicitation.match_right.match_right_amended_included.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            }
        ],
        "prompt_template": (
            "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Identify the exact timing allowed for matching an offer.\n"
            "- Include both the initial right-to-match period and, if stated separately, the period for responding to amended or revised proposals.\n"
            "- Return a single concise sentence using the **exact language** from the clause(s) with a focus on timing.\n"
            "- Do not paraphrase, generalize, or interpret the meaning.\n"
            "- Do not provide examples, commentary, or additional context.\n"
            "=== Examples ===\n"
            "Example 1:\n"
            "Reciprocal four Business Day right-to-match any Company/Parent Superior Proposal; and two Business Days for any subsequent amended proposals.\n"
            "\nExample 2:\n"
            "Nippon has a 5 Business Day right-to-match any Superior Proposal; and 3 Business Days for any subsequent amended proposals.\n"
            "\nExample 3:\n"
            "JHX has a four Business Day right-to-match any Acquisition Proposal; and two Business Days for any subsequent amended proposals.\n"
            "\n=== Clause Text to Analyze ===\n"
            "- Initial Right to Match: {match_right}\n"
            "- Amended Right to Match: {match_right_ammended}\n"
        ),
        "output_field": "match_right_explanation",
        "reference_fields": [
            "non_solicitation.match_right.match_right_initial_included.reference_section",
            "non_solicitation.match_right.match_right_explanation.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 25,
        "summary_display_section": "No Solicitation and Confidentiality Agreement",
        "summary_rank": 8.1,
        "view_prompt": True
    },

    "Non Solicitation : Go Shop": {
        "question": "Is a go-shop specified for the transaction?",
        "conditions": [
            {
                "question": "Is a go-shop specified for the transaction?",
                "if": "non_solicitation.go_shop.go_shop_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "go_shop": "{{non_solicitation.go_shop.go_shop_included.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            }
        ],
        "prompt_template": (
            "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Summarize in 1-2 sentences the go-shop provision details and limitations.\n"
            "- Use the **exact language** from the clause.\n"
            "- Do not paraphrase, generalize, or interpret the meaning.\n"
            "- Do not provide examples, commentary, or additional context.\n\n"
            "-- Clause Text:\n"
            "-- {go_shop}\n"
        ),
        "output_field": "go_shop_explanation",
        "reference_fields": [
            "non_solicitation.go_shop.go_shop_included.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 25,
        "summary_display_section": "No Solicitation and Confidentiality Agreement",
        "summary_rank": 8.3,
        "view_prompt": True
    },


    "Non Solicitation : Notice of Competing Offer": {
        "question": "Timing of Acquisition Offer",
        "conditions": [
            {
                "question": "What is the timing of an acquisition offer",
                "if": "non_solicitation.notice_of_competing_offer.notice_of_competing_offer_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "notice_of_competing_offer": "{{non_solicitation.notice_of_competing_offer.notice_of_competing_offer_included.clause_text}}"
                    }
                },
                "false": {
                    "text_output": ""
                }
            }
        ],
        "prompt_template": (
            "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Summarize in 1 sentence the requirements given a competing offer with a focus on timing and efforts.\n"
            "- Do not paraphrase, generalize, or interpret the meaning.\n"
            "- Do not provide examples, commentary, or additional context.\n"
            "Example text: Company shall promptly, and within XX hours, provide Parent notice of any Acquisition Proposal or other communication initiated by a third party concerning an Acquisition Proposal."
            "Clause Text:\n"
            "- {notice_of_competing_offer}\n"
        ),
        "output_field": "notice_of_competing_offer_explanation",
        "reference_fields": [
            "non_solicitation.notice_of_competing_offer.notice_of_competing_offer_included.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 30,
        "summary_display_section": "No Solicitation and Confidentiality Agreement",
        "summary_rank": 8.4,
        "view_prompt": True
    },

    "Non Solicitation : Ongoing Update": {
        "question": "Is ongoing update specified for the transaction?",
        "conditions": [
            {
                "question": "Ongoing Update",
                "if": "non_solicitation.ongoing_update.ongoing_update_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "ongoing_update": "non_solicitation.ongoing_update.ongoing_update_included.clause_text",
                    }
                },
                "false": {
                    "text_output": "The merger contract did not specify details related to required ongoing updates"
                }
            },
            
        ],
        "prompt_template": (
            "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Summarize as concisely as possible but without losing key details\n"
            "- Use the **exact language** from the clause.\n"
            "- Do not paraphrase, generalize, or interpret the meaning.\n"
            "- Do not provide examples, commentary, or additional context.\n"
            "Clause Text:\n"
            " {ongoing_update}\n"
        
        ),
        "output_field": "ongoing_update_explanation",
        "reference_fields": ["non_solicitation.ongoing_update.ongoing_update_included.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words":80,
        "summary_display_section": "Non Solicitation",
        "summary_rank": 4,
        "view_prompt": True
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
                        "superior_proposal_engagement": "non_solicitation.superior_proposal_engagement.superior_proposal_engagement_included.clause_text",
                    }
                },
                "false": {
                    "text_output": "The merger contract did not specify details related to Superior Proposal Engagement"
                }
            },
            
            
        ],
        "prompt_template": (
            "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Summarize as concisely as possible but without losing key details\n"
            "- Use the **exact language** from the clause.\n"
            "- Do not paraphrase, generalize, or interpret the meaning.\n"
            "- Do not provide examples, commentary, or additional context.\n"
            "Clause Text:\n"
            "-{superior_proposal_engagement}\n"
           
        ),
        "output_field": "superior_proposal_engagement_explanation",
        "reference_fields": ["non_solicitation.superior_proposal_engagement.superior_proposal_engagement_included.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words":20,
        "summary_display_section": "Non Solicitation",
        "summary_rank": 5,
        "view_prompt": True
    },

   "Non Solicitation : Adverse Change Superior Offer": {
        "question": "Can an adverse board change be made for a superior offer",
        "conditions": [
            {
                "question": "Adverse Change Superior Offer",
                "if": "non_solicitation.adverse_recommendation_change.adverse_recommendation_change_superior_proposal_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "adverse_recommendation_change": "non_solicitation.adverse_recommendation_change.adverse_recommendation_change_superior_proposal_explanation.clause_text",
                    }
                },
                "false": {
                    "text_output": "The merger contract did not specify details related to Adverse Changes for a Superior Offer"
                }
            },
            
            
        ],
        "prompt_template": (
            "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Summarize as concisely as possible but without losing any key details\n"
            "- Use the **exact language** from the clause.\n"
            "- Do not paraphrase, generalize, or interpret the meaning.\n"
            "- Do not provide examples, commentary, or additional context.\n"
            "Clause Text:\n"
            "-{adverse_recommendation_change}\n"
           
        ),
        "output_field": "superior_proposal_engagement_explanation",
        "reference_fields": ["non_solicitation.adverse_recommendation_change.adverse_recommendation_change_superior_proposal_explanation.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words":30,
        "summary_display_section": "Non Solicitation",
        "summary_rank": 6,
        "view_prompt": True
    },

    "Non Solicitation : Match Right Fulsome": {
        "question": "Timing related to Match Right",
        "conditions": [
            {
                "question": "What is the Match Right Timing",
                "if": "non_solicitation.match_right.match_right_initial_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "match_right": "{{non_solicitation.match_right.match_right_initial_explanation.clause_text}}",
                        "match_right_ammended": "{{non_solicitation.match_right.match_right_amended_included.clause_text}}"
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
            "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Identify the exact timing allowed for matching an offer.\n"
            "- Include both the initial right-to-match period and, if stated separately, the period for responding to amended or revised proposals.\n"
            "- Return a single sentence using the **exact language** from the clause(s).\n"
            "- Do not paraphrase, generalize, or interpret the meaning.\n"
            "- Do not provide examples, commentary, or additional context.\n"
            "- The sentence should begin naturally (e.g., 'Parent has...') and reflect only what is written.\n\n"
            "=== Examples ===\n"
            "Example 1:\n"
            "Reciprocal four Business Day right-to-match any Company/Parent Superior Proposal; and two Business Days for any subsequent amended proposals.\n"
            "\nExample 2:\n"
            "Nippon has a 5 Business Day right-to-match any Superior Proposal; and 3 Business Days for any subsequent amended proposals.\n"
            "\nExample 3:\n"
            "JHX has a four Business Day right-to-match any Acquisition Proposal; and two Business Days for any subsequent amended proposals.\n"
            "\n=== Clause Text to Analyze ===\n"
            "- Initial Right to Match: {match_right}\n"
            "- Amended Right to Match: {match_right_ammended}\n"
        ),
        "output_field": "match_right_explanation",
        "reference_fields": [
            "non_solicitation.match_right.match_right_initial_included.reference_section",
            "non_solicitation.match_right.match_right_explanation.reference_section"
        ],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words": 20,
        "summary_display_section": "Non Solicitation",
        "summary_rank": 1,
        "view_prompt": True
    },

   "Non Solicitation : Adverse Change Intervening Event": {
        "question": "Can an adverse board change be made for an intervening event",
        "conditions": [
            {
                "question": "Adverse Change Intervening Event",
                "if": "non_solicitation.adverse_recommendation_change.adverse_recommendation_change_intervening_event_included.answer",
                "type": "boolean",
                "true": {
                    "add_to_prompt": {
                        "adverse_recommendation_change_intervening_event_included": "non_solicitation.adverse_recommendation_change.adverse_recommendation_change_intervening_event_included.clause_text",
                    }
                },
                "false": {
                    "text_output": "The merger contract did not specify details related to Adverse Changes for an Intervening Event"
                }
            },
            
            
        ],
        "prompt_template": (
            "You are a legal and financial analyst reviewing a clause in a merger agreement.\n\n"
            "Task:\n"
            "- Summarize as concisely as possible but without losing any key details\n"
            "- Use the **exact language** from the clause.\n"
            "- Do not paraphrase, generalize, or interpret the meaning.\n"
            "- Do not provide examples, commentary, or additional context.\n"
            "Clause Text:\n"
            "-{adverse_recommendation_change_intervening_event_included}\n"
           
        ),
        "output_field": "superior_proposal_engagement_explanation",
        "reference_fields": ["non_solicitation.adverse_recommendation_change.adverse_recommendation_change_intervening_event_included.reference_section"],
        "use_short_reference": True,
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words":30,
        "summary_display_section": "Non Solicitation",
        "summary_rank": 7,
        "view_prompt": True
    }

}
