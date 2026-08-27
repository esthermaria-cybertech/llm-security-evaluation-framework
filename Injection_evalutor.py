import json

def load_test_suite(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def evaluate_responses(test_cases):
    print("Running Prompt Injection Evaluation Harness...\n")
    for test in test_cases:
        print(f"Test ID: {test['test_id']} ({test['vector_type']} - {test['attack_technique']})")
        print(f"Payload: {test['payload']}")
        print(f"Evaluation Criteria: {test['eval_criteria']}")
        print("-" * 50)

if __name__ == "__main__":
    cases = load_test_suite("prompt_injection_suite.json")
    evaluate_responses(cases)
