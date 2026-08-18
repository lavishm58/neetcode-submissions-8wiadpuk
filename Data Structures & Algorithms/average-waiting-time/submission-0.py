class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        
        cust = customers
        n = len(cust)
        if n==0:
            return 0
        cur_time = customers[0][0]
        i=0
        wait_time = 0
        while i< n:
            time, prep = cust[i]
            if cur_time>time:
                cur_time +=prep 
                wait_time += (cur_time-time)
            else:
                cur_time = time + prep
                wait_time += prep
            i+=1
        return wait_time*1.0/n 