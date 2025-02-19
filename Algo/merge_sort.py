# Defined a function to perform the merge sort algorithm
def merge_sort(arr):
    # Base case: if the array has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
                        # Find the middle of the array to divide it into two halves
    mid = len(arr) // 2
    
                        # Divide the array into two halves: left and right
    l_flow = arr[:mid]
    r_flow = arr[mid:]
    
                          # Recursively sort the left and right halves
    l_flow = merge_sort(l_flow)  
    r_flow = merge_sort(r_flow)  
    
    # Merge the sorted left and right halves
    return merge(l_flow, r_flow)

# Define a function to merge two sorted arrays
def merge(l_flow, r_flow):
    # Initialize an empty list to store the merged result
    sorty = []
    
   
    i = j = 0
    
    # Compare elements from the left and right arrays and append the smaller one
    while i < len(l_flow) and j < len(r_flow):
        if l_flow[i] < r_flow[j]:
            sorty.append(l_flow[i])
            i += 1
        else:
            sorty.append(r_flow[j])
            j += 1
    
    # Append any remaining elements from the left and right arrays
    sorty.extend(l_flow[i:])
    sorty.extend(r_flow[j:])
    
    # Return the merged and sorted array
    return sorty

# Get user input and convert it to a list of integers
arr = list(map(int, input().split()))

# Sort the input array using the merge sort algorithm and print the result
print(merge_sort(arr))