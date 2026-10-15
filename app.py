def add_numbers(x, y):
    return x + y

def test_math():
    # 1. CI Step: Ensure our logic is flawless
    assert add_numbers(10, 5) == 15
    print("All automated tests passed successfully!")

    # 2. CD Prep Step: Automatically generate a webpage file
    with open("index.html", "w") as f:
        f.write("<h1>My CI/CD Pipeline Works!</h1>")
        f.write("<p>This page was automatically built and deployed via GitHub Actions.</p>")

if __name__ == "__main__":
    test_math()
