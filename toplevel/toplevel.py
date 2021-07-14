import mod1
print("Name Top-Level-Module", __name__)
mod1.fkt1()
print("Name importiertes Module", mod1.__name__)

if __name__ == "__main__":
    print("Top Level")
mod1.fkt2()