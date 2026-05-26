from src.utils.io import read_jsonl, write_json
from src.verifier.diagnostic_state import build_diagnostic_state
from src.feedback.feedback_mapper import build_feedback


def main():
    tasks = read_jsonl("data/synthetic_samples/synthetic_tasks_sample.jsonl")
    guidelines = read_jsonl("data/guideline_samples/high_level_guidelines_sample.jsonl")

    task = tasks[0]
    proposal = {
        "proposal_id": "demo_proposal_001",
        "material_structure": "Defect-rich oxide-derived Cu surface",
        "modulation_strategy": "Defect engineering",
        "mechanistic_rationale": (
            "The defect-rich Cu surface can tune intermediate adsorption and "
            "improve product selectivity."
        ),
        "synthesis_route": (
            "Prepare Cu oxide on carbon paper and electrochemically reduce it "
            "under CO2RR conditions."
        )
    }

    diagnostic_state = build_diagnostic_state(task, proposal, guidelines)
    feedback = build_feedback(diagnostic_state)

    output = {
        "task": task,
        "initial_proposal": proposal,
        "diagnostic_state": diagnostic_state,
        "feedback": feedback,
        "note": (
            "This demo stops before calling an external LLM. In the full system, "
            "the feedback is inserted into the revision prompt."
        )
    }
    write_json(output, "examples/demo_feedback_output.json")
    print("Saved refinement demo to examples/demo_feedback_output.json")


if __name__ == "__main__":
    main()