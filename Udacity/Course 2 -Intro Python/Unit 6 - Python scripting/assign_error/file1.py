def resource_allocator(resources, tasks):
    try:
        result = resources / tasks
        left_over = resources % tasks
        print(f"Here are how many resources per task: {resources} and here are the number of left overs: {left_over}")
        return result, left_over
    except ZeroDivisionError:
        print("Error: you are dividing by zero")
        return None, None
    

def main():
    while True:
        try:
            resources = int(input("Enter number of cookies:"))
            tasks = int(input("Enter number of people:"))
            if resources<0 or tasks<0:
                print("Numbers should be positive")
                continue
            else:
                result, left_over = resource_allocator(resources, tasks)
                if (result!=None and left_over!=None):
                    print(f"Here is the result: {result}, and here is the left over: {left_over}")
                answer = input("Do you want to continue optimizing? y/n: ")
                if answer=='y':
                    continue
                else:
                    break
        except Exception as e:
            print(f"Exception occurred: {e}")

if __name__=="__main__":
    main()