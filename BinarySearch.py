

def binary_search(search_array, low, high, goal):
    search_counter = 0
    goal = goal
    search_array = search_array
    low = low
    high = high

    while low <= high:
        search_counter += 1
        middle = low + (high - low) // 2
        middle_value = search_array[middle]
    

        if middle_value == goal:
            return middle, search_counter
        
        elif middle_value < goal:   #Moves the boundary for the guess to ignore other half (now uses higher half)
            low = middle + 1

        else:
            high = middle - 1 #Moves the boundary for the guess to ignore other half (now uses lower half)
        
    return -1, search_counter #this is if the the value doesn't exist within the data


def main():
    search_array = ["a", "b", "c", "d"]
    searches = 0
    goal = input("Please enter a value to be searched for:")
    result_value, searches  = binary_search(search_array, 0, len(search_array) -1, goal)

    print("The value", search_array[result_value], "was found in the data in", searches, "searches")
    

if __name__ == "__main__":
    main()