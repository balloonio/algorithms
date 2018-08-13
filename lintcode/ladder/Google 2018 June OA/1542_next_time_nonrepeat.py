""" 
Description
Give a String, representing the time, such as "12:34", and find its next time does not repeat the number. If it is the largest"23:59", the reply is the smallest"01:23"

1.The given String represents a time of 24 hours
2.The string contains only numeric characters and ":"

Have you met this question in a real interview?  
Example
Given: "23:59"

Return:  "01:23"
"""

class Solution:
    """
    @param time: 
    @return: return a string represents time
    """
    def nextTime(self, time):
        # Write your code here
        if not self.valid_input(time):
            return '-1'
        
        hh_mm = time.split(":")
        hh, mm = [ int(time) for time in hh_mm ]
        
        min_of_day = hh * 60 + mm 
        TOTAL_MIN = 24 * 60
            
        begin_time = min_of_day
        
        min_of_day += 1 
        min_of_day %= TOTAL_MIN
        
        while min_of_day != begin_time:

            time = self.to_time(min_of_day)
            print(time)
            if not self.has_dup(time):
                return time 
            
            min_of_day += 1 
            min_of_day %= TOTAL_MIN            
        
        return "-1"
            
    
    def to_time(self, min_of_day):
        hh = min_of_day // 60
        mm = min_of_day % 60
        
        hh_str = str(hh)
        mm_str = str(mm)
        hh_str = hh_str.zfill(2)
        mm_str = mm_str.zfill(2)
        
        return ":".join([hh_str, mm_str])
    
    def has_dup(self, time):
        char_used = set()
        
        for char in time:
            if char in char_used:
                return True
            char_used.add(char)
        
        return False
        
    def valid_input(self, time):
        if not time or len(time) != 5 or ":" not in time:
            return False
        
        hh_mm = time.split(":")
        hh, mm = [ int(time) for time in hh_mm ]
        
        if hh < 0 or hh >= 24 or mm < 0 or mm >= 60:
            return False
            
        min_of_day = hh * 60 + mm 
        if min_of_day >= 1440:
            return False
        
        return True