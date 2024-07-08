def findTheWinner(n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        i = 0
        table = [x + 1 for x in range(n)]
        while len(table) > 1:
            i += k - 1
            if i >= len(table):
                i = i  % len(table)
            table.pop(i)
        return table[0]
    
n = 6
k = 5
print(findTheWinner(n, k))

##try to think of a recursive approach to this problem