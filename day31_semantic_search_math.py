
import math


def dot_product(A, B):
    return sum(a * b for a, b in zip(A, B))


def magnitude(A):
    return math.sqrt(sum(x * x for x in A))


def cosine_similarity(A, B):
    if len(A) != len(B):
        raise ValueError("Vectors must have equal dimensions.")

    mag_a = magnitude(A)
    mag_b = magnitude(B)

    if mag_a == 0 or mag_b == 0:
        raise ValueError("Zero vectors are not allowed.")

    return dot_product(A, B) / (mag_a * mag_b)


def semantic_search(query_vector, documents):
    results = []

    for doc in documents:
        score = cosine_similarity(
            query_vector,
            doc["vector"]
        )

        results.append({
            "text": doc["text"],
            "score": score
        })

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results


documents = [
    {
        "text": "Learn Python programming",
        "vector": [1, 2]
    },
    {
        "text": "Study cooking recipes",
        "vector": [2, 1]
    },
    {
        "text": "Explore machine learning",
        "vector": [1, 3]
    }
]


try:
    raw_query = input(
        "Enter two numbers for your query vector (e.g. 1,2): "
    )

    query_vector = [
        float(number.strip())
        for number in raw_query.split(",")
    ]

    if len(query_vector) != 2:
        raise ValueError("Please enter exactly two numbers.")

    results = semantic_search(query_vector, documents)

    print("\nSearch results:")

    for result in results:
        print(
            f'{result["score"]:.3f} - {result["text"]}'
        )

except ValueError as error:
    print("Input error:", error)
