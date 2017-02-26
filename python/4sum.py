class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of
              zero.
    """

    # best time O(n^2), worst time O(n^3): use hash
    # TLE!!
    def fourSum(self ,numbers, target):
        A = numbers
        if not A or len(A) < 4:
            return []
        A.sort()
        h = {}
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                key = A[i] + A[j]
                if key not in h:
                    h[key] = []
                h[key].append((i, j))

        result, visited = set(), {}
        for key, pairs in h.items():
            if key in visited:
                continue
            rest = target - key
            if rest in h:
                rest_pairs = h[rest]
                for a, b in pairs:
                    for c, d in rest_pairs:
                        indices = [a, b, c, d]
                        if len(set(indices)) == 4:
                            result.add(tuple(sorted([A[x] for x in indices])))
            visited[rest] = 1
        return [list(x) for x in result]

    # time O(n^3): use 3sum
    def fourSum1(self ,numbers, target):
        A = numbers
        if not A or len(A) < 4:
            return []
        A.sort()
        result = []
        for i in range(len(A) - 3):
            if i > 0 and A[i - 1] == A[i]:
                continue
            for j in range(i + 1, len(A) - 2):
                if j > i + 1 and A[j - 1] == A[j]:
                    continue
                left, right = j + 1, len(A) - 1
                while left < right:
                    rest = target - A[i] - A[j]
                    if A[left] + A[right] == rest:
                        result.append([A[i], A[j], A[left], A[right]])
                        left += 1
                        right -= 1
                        while left < right and A[left - 1] == A[left]:
                            left += 1
                        while left < right and A[right + 1] == A[right]:
                            right -= 1
                    elif A[left] + A[right] < rest:
                        left += 1
                    else:
                        right -= 1
        return result
