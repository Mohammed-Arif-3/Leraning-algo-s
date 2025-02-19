def merge_sort(arr):
    if(len(arr)<=1):  # Base case: if the array has one or zero elements, it's already sorted
        return arr
    mid=len(arr)//2   # Find the middle of the array to divide it into two halves
    # Divide the array into two halves: left and right
    l_flow=arr[:mid]
    r_flow=arr[mid:]
    # Recursively sort the left and right halves
    merge_sort(l_flow)
    merge_sort(r_flow)
    # Merge the sorted left and right halves
    return merge(l_flow, r_flow)
def merge(l_flow,r_flow): # a function to merge two sorted arrays
    sorty=[] # Initialize an empty list to store the merged result
    i=j=0
    while i<len(l_flow) and j<len(r_flow): # Compare elements from the left and right arrays and append the smaller one
        if l_flow[i]<r_flow[j]:
            sorty.append(l_flow[i])
            i+=1
        else:
            sorty.append(r_flow[j])
            j+=1
    # Append any remaining elements from the left and right arrays
    sorty.extend(l_flow[i:])
    sorty.extend(r_flow[j:])
    return sorty  # Return the merged and sorted array
arr=list(map(int,input().split())) # take user input and convert it to a list of integers
print(merge_sort(arr)) # Sort the input array using the merge sort algorithm and print the result
