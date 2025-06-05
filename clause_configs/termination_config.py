TERMINATION_CLAUSES = {
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
            "You are a legal analyst reviewing the termination section of a merger agreement.\n\n"
            "Task:\n"
            "- Determine whether a reverse termination fee is payable if the merger is terminated due to a regulatory failure.\n"
            "-- If applicable, identify:\n"
            "   - The amount of the fee\n"
            "   - The triggering regulatory condition (e.g., HSR denial, CFIUS block)\n"
            "   - The responsible party\n"
            "-- If no such fee is payable, state this clearly.\n"
            "- Output a standalone paragraph appropriate for financial and legal audiences. Be specific and do not duplicate phrasing.\n\n"
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
        "summary_type": "Fulsome",
        "format_style": "paragraph_with_bullets",
        "max_words": 35,
        "summary_display_section": "Regulatory",
        "summary_rank": 2,
        "view_prompt": True
    }
}
