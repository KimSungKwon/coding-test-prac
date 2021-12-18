def solution(n, k, arr1, arr2):
    answer = 0

    arr1.sort()
    arr2.sort(reverse=True)

    for i in range(k):
        if arr1[i] < arr2[i]:
            arr1[i], arr2[i] = arr2[i], arr1[i]
        else:
            break;

    return sum(arr1)


print(solution( 5, 3, [1,2,5,4,3], [5,5,6,6,5] ))
