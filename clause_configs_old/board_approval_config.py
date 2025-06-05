BOARD_APPROVAL_CLAUSES = {

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
        "summary_type": "Concise",
        "format_style": "bullet",
        "max_words":50,
        "summary_display_section": "Board Approval",
        "summary_display_sub_section": "Board Approval",
        "summary_rank": 2,
        "view_prompt": True
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
        "summary_type": "Fulsome",
        "format_style": "paragraph",
        "max_words":100,
        "summary_display_section": "Board Approval",
        "summary_display_sub_section": "Board Approval",
        "summary_rank": 2,
        "view_prompt": False
    }
}