from agno.eval.accuracy import AccuracyEval,AccuracyResult
from Inventory_Agent import agent

def test_inventory_agent():

    test_cases = [
        {
            "query": "I want to buy a google phone. is it available and which phone is avail?",
            "expected_response": "The google pixel 7 pro is In Stock with 10 available items.",
            "min_score": 0.9
        },
        {
            "query": "Is the iPhone 14 pro max in stock?",
            "expected_response": "The iPhone 14 pro max is In Stock with 25 available items.",
            "min_score": 0.9
        },
        {
            "query": "Do you have the samsung galaxy s23 ultra available?",
            "expected_response": "The samsung galaxy s23 ultra is Out of Stock with 0 available items.",
            "min_score": 0.9
        },
        {
            "query": "Do you have any information about the availability of the google pixel 7 pro?",
            "expected_response": "The google pixel 7 pro is In Stock with 10 available items.",
            "min_score": 0.9
        }
    ]
    for test in test_cases:
        evaluator = AccuracyEval(
            agent=agent,
            question=test["query"],
            expected_answer=test["expected_response"],
            num_iterations = 1
        )
        print(f"Evaluating: {test['question']}")
        evaluator.run(print_results=True)


if __name__ == "__main__":
    test_inventory_agent()