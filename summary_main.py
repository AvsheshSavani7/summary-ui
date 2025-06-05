# =========================
# Setup and Imports
# =========================
import sys
import os
import json
from docx import Document

sys.path.append(os.path.dirname(__file__))

from summary_engine import process_clause_config, write_docx_summary
from clause_configs.ordinary_course_config import ORDINARY_COURSE_CLAUSES
from clause_configs.best_efforts_config import BEST_EFFORTS_CLAUSES
from clause_configs.termination_config import TERMINATION_CLAUSES
from clause_configs.non_solicitation_config import NON_SOLICITATION_CLAUSES
from clause_configs.condition_to_closing_config import CONDITION_TO_CLOSING_CLAUSES
from clause_configs.financing_summary_config import FINANCING_SUMMARY_CLAUSES
from clause_configs.closing_mechanics_config  import CLOSING_MECHANICS_CLAUSES
from clause_configs.proxy_shareholder_config  import PROXY_SHAREHOLDER_CLAUSES
from clause_configs.specific_performance_config  import SPECIFIC_PERFORMANCE_CLAUSES
from clause_configs.law_jurisdiction_config  import LAW_JURISDICTION_CLAUSES
from clause_configs.party_details_config  import PARTY_DETAILS_CLAUSES
from clause_configs.timeline_config  import TIMELINE_CLAUSES
from clause_configs.outside_date_config  import OUTSIDE_DATE_CLAUSES

# =========================
# Load Config and Schema
# =========================
CLAUSE_CONFIG = {
    **ORDINARY_COURSE_CLAUSES,
    **BEST_EFFORTS_CLAUSES,
    #**TERMINATION_CLAUSES,
    #**NON_SOLICITATION_CLAUSES,
    #**FINANCING_SUMMARY_CLAUSES,
    #**CLOSING_MECHANICS_CLAUSES,
    #**CONDITION_TO_CLOSING_CLAUSES,
    #**PROXY_SHAREHOLDER_CLAUSES,
    #**SPECIFIC_PERFORMANCE_CLAUSES,
    #**LAW_JURISDICTION_CLAUSES,
    #**PARTY_DETAILS_CLAUSES,
    #**TIMELINE_CLAUSES
    # **OUTSIDE_DATE_CLAUSES
}

    # =========================
# Accept JSON filename Hardcoded 
# =========================
# with open("schema.json") as f:
#     EXAMPLE_SCHEMA_DATA = json.load(f)
    
    # =========================
# Accept JSON filename from terminal
# =========================
if len(sys.argv) < 2:
    print("❌ Please provide a JSON file name as an argument.\nUsage: python summary_main.py <filename.json>")
    sys.exit(1)

json_filename = sys.argv[1]

if not os.path.exists(json_filename):
    print(f"❌ File not found: {json_filename}")
    sys.exit(1)

with open(json_filename, "r", encoding="utf-8") as f:
    EXAMPLE_SCHEMA_DATA = json.load(f)
    
    

print("Loaded clause configs:", list(CLAUSE_CONFIG.keys()))

# =========================
# Run Clause Evaluations
# =========================
summary_outputs = []

for clause_name, clause_config in CLAUSE_CONFIG.items():
    print(f"\n→ Evaluating: {clause_name}")
    result = process_clause_config(clause_config, EXAMPLE_SCHEMA_DATA)

    if result["output"] and result["output"] != "No output generated.":
        # Skip concise summaries where view_prompt is False
        if (
            result.get("summary_type", "").lower() == "concise"
            and clause_config.get("view_prompt", True) is False
        ):
            print(f"Skipping {clause_name} (concise, view_prompt=False)")
            continue

        summary_outputs.append({
            "clause_name": clause_name,
           
            **result
        })

        print("=== CLAUSE SUMMARY OUTPUT ===")
        print(f"Clause: {clause_name}")
        if result.get("used_prompt"):
            print("Used Prompt:\n" + result["used_prompt"])
        print("Summary:\n" + result["output"])
        if result.get("references"):
            print("References:")
            for r in result["references"]:
                print("- " + r)
        else:
            print("References: [None found or resolved]")

# =========================
# Write to DOCX
# =========================
summary_outputs_sorted = sorted(summary_outputs, key=lambda x: x['summary_rank'])

write_docx_summary(summary_outputs_sorted)
print("\n✅ DOCX summary written.")





