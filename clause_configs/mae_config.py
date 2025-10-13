MAE_CLAUSES = {

    #Concise MAE
        "MAE Non Standard Carveouts - Concise": {
            "question": "Non Standard MAE",
            "conditions": [
                {
                    "question": "MAE - Concise",
                    "if": "material_adverse_effect.mae_carveout.mae_carveout_other_custom_items_present.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "mae_nonstandard": "{{material_adverse_effect.mae_carveout.mae_carveout_other_custom_items_present.clause_text}}"
                        }
                    },
                    "false": {
                        "text_output": "MAE carve-outs appear standard"
                    }
                }
            ],
            "prompt_template": (
                "You are a legal and financial analyst reviewing the Material Adverse Effect (MAE) carveouts in a merger agreement.\n\n"
                "Task:\n"
                "- Write one concise sentence summarizing the nature of the MAE carveouts.\n"
                "- If the carveouts are standard, state: 'MAE carve-outs appear standard.'\n"
                "- If the carveouts include non-standard elements, briefly describe them using the **exact language** from the clause (do not paraphrase or interpret).\n"
                "- You may say: 'MAE carve-outs appear standard but include...' if the clause is mostly standard with one or two specific additions.\n"
                "- Do not include party names, clause references, or commentary.\n\n"
                "-- Clause Text:\n"
                "{mae_nonstandard}\n\n"
                "--- Example Outputs:\n"
                "- MAE carve-outs include adverse occurrences impacting any Company Pipeline Product.\n"
                "- MAE carve-outs appear standard.\n"
                "- MAE carve-outs appear standard but include “any matter disclosed against a representation or warranty” as set forth in non-public Company and Parent Disclosure Letters."
            ),
            "output_field": "mae_summary",
            
            "reference_fields": ["material_adverse_effect.mae_carveout.mae_carveout_other_custom_items_present.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Concise",
            "format_style": "paragraph",
            "max_words": 30,
            "summary_display_section": "Other Items",
            "summary_rank": 6.3,
            "view_prompt": True
        },

    #Fullsome Ordinary Course

        "MAE Standard Carveouts - Fulsome": {
            "question": "Standard MAE",
            "conditions": [
                {
                    "question": "MAE - Concise",
                    "if": "material_adverse_effect.mae_carveout.standard_mae_carveouts_list.answer",
                    "type": "non_empty",
                    "true": {
                        "add_to_prompt": {
                            "mae_standard_answer": "{{material_adverse_effect.mae_carveout.standard_mae_carveouts_list.answer}}",
                            "mae_nonstandard_text": "{{material_adverse_effect.mae_carveout.standard_mae_carveouts_list.clause_text}}"
                        }
                    },
                    "false": {
                        "text_output": ""
                    }
                }
            ],
            "prompt_template": (
                "You are a legal and financial analyst reviewing the Material Adverse Effect (MAE) carveouts in a merger agreement.\n\n"
                "Task:\n"
                "- Write one concise sentence/paragraph detailing the MAE carveouts.\n"
                "- Do not include party names, clause references, or commentary.\n\n"
                "-- Standard MAE Carveout List:\n"
                "{mae_standard_answer}\n"
                "-- Standard MAE Carveout Text:\n"
                "{mae_standard_answer}\n\n"
                "--- Example Outputs:\n"
                "- Material Adverse Effect carve-outs include (i) changes in general economic conditions, (ii) changes generally affecting industries, (iii) decline in market price or volume, (iv) changes in regulatory or political conditions or capital markets in the U.S. or any foreign jurisdiction, (v) failure to meet projections and metrics, (vi) public announcement of the agreement (including impacts on relationships), (vii) changes in Laws, (viii) changes in GAAP, (ix) geopolitical conditions, (x) any action taken at the written request or consent of Parent, (xi) reduction in credit rating, (xii) public health events or natural disasters, (xiii) any proceedings arising from allegations of fiduciary or violation of Applicable Law related to this Agreement, (xiv) any occurrences relating to any Company Pipeline Product.\n"
                "- Material Adverse Effect carve-outs include (a) changes in market price, trading volume or credit rating, (b) the announcement of the agreement (including impact on relationships), (c) general industry conditions or domestic, foreign or global economy generally and financial market conditions, (d) political conditions or capital market conditions (including tariffs and trade wars), (e) geopolitical conditions and hostilities, (f) natural disasters and force majeure events, (g) compliance with applicable law, (h) failure to meet projections or forecasts, (i) any action resulting from the Agreement, (j) any action taken at direction or acknowledgment of Parent, (k) any breach by Parent, (l) changes in Law or GAAP, (m) failure to obtain Required Approvals\n"
                "- Material Adverse Effect carve-outs include (i) changes in general financial markets, (ii) general changes in industries, (iii) changes in Laws or GAAP, (iv) changes in trading price or volume and credit ratings, (v) failure to meet projections and forecasts, (vi) geopolitical hostilities, natural disasters, and epidemics/pandemics, (vii) any action taken or not taken at express request of the parties, (viii) the public announcement of the agreement (including relationships), (ix) matters disclosed in Article III in Company Disclosure Letter or Article IV in the Parent Disclosure Letter."
            ),
            "output_field": "mae_summary",
            
            "reference_fields": ["material_adverse_effect.mae_carveout.mae_carveout_other_custom_items_present.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 60,
            "summary_display_section": "MAE Definitions",
            "summary_rank": 16.1,
            "view_prompt": True
        },

        "MAE Non Standard Carveouts - Fulsome": {
            "question": "Non Standard MAE",
            "conditions": [
                {
                    "question": "MAE - Concise",
                    "if": "material_adverse_effect.mae_carveout.mae_carveout_other_custom_items_present.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "mae_nonstandard": "{{material_adverse_effect.mae_carveout.mae_carveout_other_custom_items_present.clause_text}}"
                        }
                    },
                    "false": {
                        "text_output": "MAE carve-outs appear standard"
                    }
                }
            ],
            "prompt_template": (
                "You are a legal and financial analyst reviewing the Material Adverse Effect (MAE) carveouts in a merger agreement.\n\n"
                "Task:\n"
                "- Write one concise sentence summarizing the nature of the MAE carveouts.\n"
                "- If the carveouts are standard, state: 'MAE carve-outs appear standard.'\n"
                "- If the carveouts include non-standard elements, briefly describe them using the **exact language** from the clause (do not paraphrase or interpret).\n"
                "- You may say: 'MAE carve-outs appear standard but include...' if the clause is mostly standard with one or two specific additions.\n"
                "- Do not include party names, clause references, or commentary.\n\n"
                "-- Clause Text:\n"
                "{mae_nonstandard}\n\n"
                "--- Example Outputs:\n"
                "- MAE carve-outs include adverse occurrences impacting any Company Pipeline Product.\n"
                "- MAE carve-outs appear standard.\n"
                "- MAE carve-outs appear standard but include “any matter disclosed against a representation or warranty” as set forth in non-public Company and Parent Disclosure Letters."
            ),
            "output_field": "mae_summary",
            
            "reference_fields": ["material_adverse_effect.mae_carveout.mae_carveout_other_custom_items_present.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 30,
            "summary_display_section": "MAE Definitions",
            "summary_rank": 16.2,
            "view_prompt": True
        },

        "MAE Disproportionality - Fulsome": {
            "question": "Non Standard MAE",
            "conditions": [
                {
                    "question": "MAE - Concise",
                    "if": "material_adverse_effect.mae_carveback.mae_carveback_disproportionate_effects_included.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "mae_disproportionate_answer": "{{material_adverse_effect.mae_carveback.mae_carveback_disproportionate_effects_explanation.answer}}",
                            "mae_disproportionate_text": "{{material_adverse_effect.mae_carveback.mae_carveback_disproportionate_effects_explanation.clause_text}}"
                        }
                    },
                    "false": {
                        "text_output": ""
                    }
                }
            ],
            "prompt_template": (
                "You are a legal and financial analyst reviewing the Material Adverse Effect (MAE) carveouts in a merger agreement.\n\n"
                "Task:\n"
                "- Write one concise sentence summarizing the nature of the MAE items related to disproportionality.\n"
                "- Do not include party names, clause references, or commentary.\n\n"
                "-- Clause Text:\n"
                "{mae_disproportionate_answer}\n"
                "-- Clause Text:\n"
                "{mae_disproportionate_text}\n\n"
                "--- Example Outputs:\n"
                "- For clauses (i), (ii), (iv), (vii), (viii), (ix) or (xii), unless disproportionate relative to other companies operating in the same industries.\n"
                "- For clauses (c), (d), (e), (f), or (l) unless such event, change, etc. has a materially disproportionate adverse impact relative to similarly situated Persons engaged in the same industries or geographic markets, then the incremental material disproportionate impact shall be taken into account.\n"
                "- For sections (i) through (iii) and (vi), unless disproportionate relative to other industry participants."
            ),
            "output_field": "mae_disproportionality_summary",
            
            "reference_fields": ["material_adverse_effect.mae_carveback.mae_carveback_disproportionate_effects_explanation.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 40,
            "summary_display_section": "MAE Definitions",
            "summary_rank": 16.3,
            "view_prompt": True
        },

        "MAE Facts or Occurances - Fulsome": {
            "question": "Facts or OccurancesE",
            "conditions": [
                {
                    "question": "MAE - Facts or Occurances",
                    "if": "material_adverse_effect.mae_carveback.mae_carveback_causation_based_analysis_included.answer",
                    "type": "boolean",
                    "true": {
                        "add_to_prompt": {
                            "mae_fact_occurances_answer": "{{material_adverse_effect.mae_carveback.mae_carveback_causation_based_analysis_explanation.answer}}",
                            "mae_fact_occurances_text": "{{material_adverse_effect.mae_carveback.mae_carveback_causation_based_analysis_explanation.clause_text}}"
                        }
                    },
                    "false": {
                        "text_output": ""
                    }
                }
            ],
            "prompt_template": (
                "You are a legal and financial analyst reviewing the Material Adverse Effect (MAE) carveouts in a merger agreement.\n\n"
                "Task:\n"
                "- Write one concise sentence summarizing the MAE items related to underlying facts or occurances.\n"
                "- Do not include party names, clause references, or commentary.\n\n"
                "-- MAE Facts and Occurances Answer:\n"
                "{mae_fact_occurances_answer}\n"
                "-- MAE Facts and Occurances Text:\n"
                "{mae_fact_occurances_text}\n\n"
                "--- Example Outputs:\n"
                "- For clauses (iii), (v), and (x), facts or occurrences giving rise to such change may be taken into account.\n"
                "- For clauses (a) and (h), the underlying causes thereof may be considered in determining whether a MAE has occurred.\n"
                "- For sections (iv) and (v), facts or occurrences giving rise to such change may be taken into account."
            ),
            "output_field": "mae__facts_occurances_summary",
            
            "reference_fields": ["material_adverse_effect.mae_carveback.mae_carveback_causation_based_analysis_explanation.reference_section"],
            "use_short_reference": True,
            
            "summary_type": "Fulsome",
            "format_style": "paragraph",
            "max_words": 40,
            "summary_display_section": "MAE Definitions",
            "summary_rank": 16.4,
            "view_prompt": True
        },

}