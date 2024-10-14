import concurrent.futures

def dot_product(vector1, vector2):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        products = list(executor.map(lambda x: x[0] * x[1], zip(vector1, vector2)))
    return sum(products)

# Example usage:
v1 = [1, 2, 3]
v2 = [4, 5, 6]
print(f"The dot product is: {dot_product(v1, v2)}")

