def main():
    print(f"{hello()}")
    
    
def hello():
    name = input("What's your name? ")
    return f"hello, {name}"


if __name__ == "__main__":
    main()