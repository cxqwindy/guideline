FEEDBACK_TEMPLATES = {
    "CRITICAL_ERROR": (
        "The proposal contains a critical mechanistic conflict. "
        "Revise the claim that conflicts with known CO2RR constraints before "
        "refining the rest of the mechanism."
    ),
    "LOGIC_FLAW": (
        "The mechanism is internally inconsistent or insufficiently supported. "
        "Clarify how the proposed material structure and modulation strategy "
        "lead to the claimed catalytic effect."
    ),
    "MISSING_MECHANISM": (
        "The proposal is plausible but the causal chain is incomplete. "
        "Add the missing intermediate links from material modification to "
        "intermediate regulation and target product selectivity."
    ),
    "NONE": (
        "No major mechanistic failure is detected. Keep the proposal concise "
        "and preserve the current scientific rationale."
    ),
}