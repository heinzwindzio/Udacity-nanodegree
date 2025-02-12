while True:
    try:
        my_int = int(input("Enter a number: "))
        break
    except ValueError:
        print("There was a problem with the inputs")
    except KeyboardInterrupt:
        break
    finally:
        print("always run")