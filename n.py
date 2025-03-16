class N(): 
        
    def smallN(n):
        for SmallZ in range([n, 0, n],
                            [n, n, n],
                            [n, 0, n]):
            return [1,2,3,4,5,6,7,8,9]
                                
    def MiddleN(n):
        for MiddleZ in range([n, 0, 0, n],
                             [n, n, 0, n],
                             [n, 0, n, n],
                             [n, 0, 0, n]):
            return [1,2,3,4,5,6,7,8,9]
                                
    def BigN(n):
        for BigZ in range([n, 0, 0, 0, n],
                          [n, n, 0, 0, n],
                          [n, 0, n, 0, n],
                          [n, 0, 0, n, n],
                          [n, 0, 0, 0, n]):
            return [1,2,3,4,5,6,7,8,9]
