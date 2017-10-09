# credit:  http://www.cnblogs.com/grandyang/p/6181626.html
#
#每一个房子是被前后两个heater覆盖，选其中的最小值
#历遍所有房子，取所有radius的最大值
#
#二分用在找第一个大于等于house的heater的位置
#特殊情况第一个和最后一个
#max(i - 1, 0) 表示当i==0时，不越界，只和第一比
#i 永远有效，因为加了哨兵 sys.maxint

import bisect

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        radius = -sys.maxint
        heaters = sorted(heaters + [sys.maxint])
        for house in houses:
            i = bisect.bisect(heaters, house)
            radius = max(radius, min(abs(heater - house) for heater in heaters[max(i-1, 0):i+1]))
        return radius
