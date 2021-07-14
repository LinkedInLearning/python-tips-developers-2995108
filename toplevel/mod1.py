def fkt1():
    print(__name__)
def fkt2():
    if __name__ == "__main__":
        print("Top Level")
    else:
        print("Nicht Top Level")