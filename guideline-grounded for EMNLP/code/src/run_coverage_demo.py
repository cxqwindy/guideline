from src.utils.io import read_jsonl, write_json
from src.verifier.coverage_isolation import (
    split_guidelines_by_level,
    flag_overlap_pairs,
)


def main():
    high = read_jsonl("data/guideline_samples/high_level_guidelines_sample.jsonl")
    fine = read_jsonl("data/guideline_samples/fine_grained_guidelines_sample.jsonl")
    guidelines = high + fine

    high_level, fine_grained = split_guidelines_by_level(guidelines)
    flagged = flag_overlap_pairs(high_level, fine_grained, threshold=0.35)

    output = {
        "num_high_level": len(high_level),
        "num_fine_grained": len(fine_grained),
        "num_flagged_pairs": len(flagged),
        "flagged_pairs": flagged,
        "note": (
            "This demo implements lexical overlap filtering only. The full "
            "system additionally applies semantic filtering and manual audit."
        )
    }

    write_json(output, "examples/demo_coverage_isolation_result.json")
    print("Saved coverage isolation demo.")


if __name__ == "__main__":
    main()