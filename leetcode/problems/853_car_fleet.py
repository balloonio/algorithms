class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        fleet = list(zip(position, speed))
        fleet.sort()
        time = [ (target - p) / s for (p, s) in fleet]

        result = 0
        while len(time) > 1:
            lead = time.pop()
            if lead < time[-1]:
                result += 1
            else:
                time[-1] = lead

        return result + len(time)
        
"""
按照官方solution写的 很巧妙的做法
判断有没有fleet的办法 如果离终点更远的车按照自己的速度比离终点更近的车更快到达 那么一定会撞到一起生成fleet
使用stack从离终点最近的车开始算 看它会不会卡自己后面的车
"""
