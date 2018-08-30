// recursion
int power(int x, int n) {
    if (n == 0) return 1;
    if (n % 2 == 0) {
        int tmp = power(x, n / 2);
        return tmp * tmp;
    } else {
        int tmp = power(x, n / 2);
        return tmp * tmp * x;
    }
}

// non-recursion
int power(int x, int n) {
    int ans = 1, base = x;
    while (n != 0) {
        if (n % 2 == 1) {
            ans *= base;
        }
        base *= base;
        n = n / 2;
    }
    return ans;
}