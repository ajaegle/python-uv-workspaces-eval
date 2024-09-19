from second import hello as second

def main():
    print("Hello from outer!")
    print(second.main())


if __name__ == "__main__":
    main()
