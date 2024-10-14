# dot_product.py
def dot_product(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))

# Example usage:
v1 = [1, 2, 6]
v2 = [4, 5, 6]
print(f"The dot product of the vectors is: {dot_product(v1, v2)}")

