// 算法描述
// 将该新区间按照左端值插入原区间中，使得原区间左端值是有序的。
// 遍历原区间列表，并把它复制到一个新的answer区间列表当中，answer是最后要返回的结果。
// 遍历时，要记录上一次访问的区间last。若当前区间左端值小于等于last区间的右端值，说明这两区间有重叠，此时仅更新last的右端值为这两区间右端值较大者；若当前区间左端值大于last的右端值，则可以直接加入answer。
// 返回answer。

public class Solution {
    /*
     * @param intervals: Sorted interval list.
     * @param newInterval: new interval.
     * @return: A new interval list.
     */
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        List<Interval> answer = new ArrayList<>();

        int index = 0;
        while (index < intervals.size() && intervals.get(index).start < newInterval.start) {
            index++;
        }
        intervals.add(index, newInterval);

        Interval last = null;
        for (Interval item : intervals) {
            if (last == null || last.end < item.start) {
                answer.add(item);
                last = item;
            } else {
                last.end = Math.max(last.end, item.end); // Modify the element already in list
            }
        }
        return answer;
    }
}