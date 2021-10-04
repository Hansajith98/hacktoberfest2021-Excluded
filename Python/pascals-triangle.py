class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # initializing triangle's 1st level
        res=[[1]]
        for i in range(1,numRows):
            n=len(res)
            # initializing array at level n to have length n
            row=[0]*(i+1)
            # iterating over array at level n
            for j in range(len(row)):
                # 1st ele = ele to top-left to this ele in the triangle 
                a=res[n-1][j-1] if j>0 else 0
                # 2nd ele = ele to top-right to this ele in the triangle
                b=res[n-1][j] if j<n else 0
                # 1st+2nd to get the current ele
                row[j]=a+b
            # add the row to the triangle
            res.append(row)
        return res
