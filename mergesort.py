def merge_sort(arr):
    if(len(arr)<=1):
        return arr
    l_flow=arr[:mid]
    r_flow=arr[mid:]
    merge_sort(l_flow)
    merge_sort(r_flow)
    return merge(l_flow, r_flow)
def merge(l_flow,r_flow):
    sorty=[]
    i=j=0
    while i<l_flow and j<r_flow:
        if l_flow[i]<r_flow[j]:
            sorty.append(l_flow[i])
            i+=1
        else:
            sorty.append(r_flow[j])
            j+=1
    sorty.extend(l_flow[i:])
    sorty.extend(r_flow[j:])
    return sorty
arr=list(map(int,input().split()))
print(merge_sort(arr))