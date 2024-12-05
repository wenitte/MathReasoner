class MathReasonerV1:
    """
    Initial benchmark for testing mathematical reasoning capabilities.
    Each problem tests specific aspects of mathematical thinking.
    """
    
    def get_benchmark_problems(self):
        return {
            "validation_problems": [
                {
                    "id": "V1",
                    "category": "validation",
                    "difficulty": "basic",
                    "theorem": "If n² is even, then n is even",
                    "proof": [
                        "1. Let n be an integer where n² is even",
                        "2. Then n² = 2k for some integer k",
                        "3. Therefore n = √(2k)",
                        "4. Thus n must be even",
                        "QED"
                    ],
                    "expected": {
                        "valid": False,
                        "error_step": 3,
                        "explanation": "Taking square root doesn't preserve integer property"
                    },
                    "points": 5
                },
                {
                    "id": "V2",
                    "category": "validation",
                    "difficulty": "medium",
                    "theorem": "The square root of 2 is irrational",
                    "proof": [
                        "1. Assume √2 = a/b where a,b are coprime integers",
                        "2. Then 2b² = a²",
                        "3. Therefore a² is even",
                        "4. Thus a is even, so a = 2k",
                        "5. Therefore 2b² = 4k²",
                        "6. Thus b² = 2k²",
                        "7. Therefore b is even",
                        "8. Contradicts a,b being coprime",
                        "QED"
                    ],
                    "expected": {
                        "valid": True,
                        "key_insights": ["contradiction", "even squares", "coprime"]
                    },
                    "points": 8
                }
            ],
            
            "completion_problems": [
                {
                    "id": "C1",
                    "category": "completion",
                    "difficulty": "medium",
                    "theorem": "Sum of first n odd numbers equals n²",
                    "partial_proof": [
                        "1. True for n=1: 1 = 1²",
                        "2. Assume true for k: 1 + 3 + ... + (2k-1) = k²",
                        "[MISSING STEP]",
                        "4. Therefore true for k+1",
                        "5. By induction, true for all n"
                    ],
                    "expected": {
                        "key_step": "Add (2k+1) to both sides: k² + (2k+1) = (k+1)²",
                        "reasoning": ["next odd number", "algebraic completion"]
                    },
                    "points": 8
                }
            ],
            
            "strategy_problems": [
                {
                    "id": "S1",
                    "category": "strategy",
                    "difficulty": "hard",
                    "theorem": "There are infinitely many primes",
                    "task": "Select and justify best proof strategy",
                    "context": "Need to prove existence of infinitely many objects",
                    "expected": {
                        "strategy": "contradiction",
                        "justification": "Assuming finite primes leads to constructing new prime",
                        "key_insights": ["construct from existing", "add one", "prime factors"]
                    },
                    "points": 10
                }
            ],
            
            "transfer_problems": [
                {
                    "id": "T1",
                    "category": "transfer",
                    "difficulty": "expert",
                    "source_theorem": "Infinite pigeonhole principle",
                    "target_theorem": "Every infinite subset of integers has an infinite arithmetic progression",
                    "task": "Apply pigeonhole thinking to prove target theorem",
                    "expected": {
                        "technique": "infinite_pigeons",
                        "key_transfer": "infinite choices into finite options",
                        "insight": "differences between elements form finite set"
                    },
                    "points": 12
                }
            ],
            
            "logical_chain_problems": [
                {
                    "id": "L1",
                    "category": "logical_chain",
                    "difficulty": "medium",
                    "premise": "Let G be a group. ∀a,b ∈ G: (ab)² = a²b²",
                    "conclusion": "G is abelian",
                    "task": "Construct valid logical chain from premise to conclusion",
                    "expected": {
                        "key_steps": [
                            "expand (ab)²",
                            "use premise",
                            "cancel valid terms",
                            "conclude ab = ba"
                        ]
                    },
                    "points": 8
                }
            ],
            
            "mistake_identification": [
                {
                    "id": "M1",
                    "category": "mistakes",
                    "difficulty": "medium",
                    "claim": "All triangles are isosceles",
                    "invalid_proof": [
                        "1. Let ABC be a triangle",
                        "2. Draw height h from A to BC",
                        "3. This creates two right triangles",
                        "4. By pythagorean theorem, both sides equal",
                        "5. Therefore AB = AC",
                        "QED"
                    ],
                    "expected": {
                        "error_type": "hidden_assumption",
                        "specific_flaw": "assumes height bisects base",
                        "correction": "height may not bisect base unless already isosceles"
                    },
                    "points": 8
                }
            ]
        }

    def get_scoring_criteria(self):
        return {
            "validation": {
                "correctness": 2,  # Correctly identifies valid/invalid
                "error_location": 1,  # Finds specific error
                "explanation": 2  # Quality of explanation
            },
            "completion": {
                "logical_validity": 3,  # Step follows logically
                "completeness": 2,  # Includes all necessary details
                "clarity": 3  # Clear and well-explained
            },
            "strategy": {
                "choice": 3,  # Appropriate strategy selected
                "justification": 4,  # Why this strategy works
                "alternatives": 3  # Why other approaches don't work
            },
            "transfer": {
                "technique_application": 4,  # Correctly applies technique
                "justification": 4,  # Explains why it transfers
                "execution": 4  # Successfully completes proof
            },
            "logical_chain": {
                "validity": 3,  # Each step valid
                "completeness": 3,  # No missing steps
                "clarity": 2  # Clear progression
            },
            "mistakes": {
                "identification": 3,  # Finds mistake
                "explanation": 3,  # Explains why it's wrong
                "correction": 2  # Shows how to fix
            }
        }

    def get_evaluation_metrics(self):
        return {
            "overall_score": {
                "max_points": 100,
                "passing_threshold": 70
            },
            "category_weights": {
                "validation": 0.2,
                "completion": 0.2,
                "strategy": 0.2,
                "transfer": 0.15,
                "logical_chain": 0.15,
                "mistakes": 0.1
            },
            "skill_metrics": [
                "logical_validity",
                "proof_technique",
                "error_detection",
                "mathematical_clarity",
                "strategic_thinking"
            ]
        }
