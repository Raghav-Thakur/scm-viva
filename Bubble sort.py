def bubblesort(li):
    swapped = False
    a=len(li)
    for n in range(a-1, 0, -1):
        for i in range(n):
            if li[i] > li[i + 1]:
                swapped = True
                li[i], li[i + 1] = li[i + 1], li[i]       
        if not swapped:
            return

print("Enter Your Unsorted List: ")
li = [int(x) for x in input().split()]
bubblesort(li)
print("Sorted List is: ")
print(li)
#kjsdbjhbjdb