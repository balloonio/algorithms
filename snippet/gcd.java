// 辗转相除法
public int gcd(int big, int small) {
    if (small != 0) {
        return gcd(small, big % small);
    } else {
        return big;
    }
}