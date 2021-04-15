def main():
    print(__name__)
    if __name__ == "__main__":
        import sys
        try:
            n = int(sys.argv[1])
            print(n)
        except:
            print("Das Skript benötigt eine Zahl als Parameter")
if __name__ == "__main__":
    main()