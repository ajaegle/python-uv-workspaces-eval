from second import hello as second
from first import call

def main():
    print("Hello from outer!")
    # print(second.main())
    print(call.fetch_data())


if __name__ == "__main__":
    main()
