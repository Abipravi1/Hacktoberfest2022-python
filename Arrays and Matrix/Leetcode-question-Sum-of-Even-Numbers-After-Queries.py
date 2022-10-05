def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]: 
        s=0
        #firstly calculating all the even numbers sum if the nums
        for j in nums:
            if j%2==0:
                s+=j
                
        r=[]
        for i in range(len(queries)):
            
            #if the previous value at the position of queries[i][1] in nums is even then remove it from s
            #coz when queries[i][1] position in nums will get updated with addition of queries[i][0]
            #to the nums[queries[i][1]]
            
            if nums[queries[i][1]]%2==0:
                s-=nums[queries[i][1]]
                
            #updation 
            nums[queries[i][1]]+=queries[i][0]
            
            #again checking if the updation value is even then add to the s, otherwise not
            if nums[queries[i][1]]%2==0:
                s+=nums[queries[i][1]]
                
            #storing the everytime updating sum
            r.append(s)
            
        return r
