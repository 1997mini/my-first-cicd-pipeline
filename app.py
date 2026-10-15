def add_numbers(x, y):
    return x + y

def test_math():
    # This is our automated test condition
    assert add_numbers(10, 5) == 15
    print("All automated tests passed successfully!")

if __name__ == "__main__":
    test_math()
