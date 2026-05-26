from src.utils.io import read_jsonl, write_json
from src.retrieval.retrieve_examples import retrieve_topk_examples


def main():
    tasks = read_jsonl("data/synthetic_samples/synthetic_tasks_sample.jsonl")
    examples = read_jsonl("data/factual_examples_sample/factual_examples_sample.jsonl")

    task = tasks[0]
    retrieved = retrieve_topk_examples(task, examples, top_k=3)

    output = {
        "task": task,
        "retrieved_examples": retrieved,
    }
    write_json(output, "examples/demo_retrieval_result.json")
    print("Saved retrieval demo to examples/demo_retrieval_result.json")


if __name__ == "__main__":
    main()