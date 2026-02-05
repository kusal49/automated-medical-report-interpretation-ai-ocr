from services.ai_service import run_with_fallback
from config.prompts import (
    MASTER_PROMPT,
    REPORT_PARSER_PROMPT,
    INSIGHT_AGENT_PROMPT,
    LIFESTYLE_AGENT_PROMPT,
    SAFETY_AGENT_PROMPT,
)

def analyze_report(extracted_text: str):

    # 1. Parse report
    structured_data = run_with_fallback(
        REPORT_PARSER_PROMPT,
        extracted_text
    )

    # 2. Generate medical insights
    insights = run_with_fallback(
        INSIGHT_AGENT_PROMPT,
        structured_data
    )

    # 3. Personalization & lifestyle
    lifestyle = run_with_fallback(
        LIFESTYLE_AGENT_PROMPT,
        insights
    )

    # 4. Safety validation
    final_output = run_with_fallback(
        SAFETY_AGENT_PROMPT,
        lifestyle
    )

    return final_output
