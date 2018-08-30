// 缓存和数据库的配合比较像是算法中的记忆化搜索。缓存系统可以理解为一个大的哈希表。

class UserService {
    private String userCacheKey(int userId) {
        return "user::" + userId;
    }

    public User getUser(int userId) {
        String key = userCacheKey(userId);
        User user = Cache.get(key);
        if (user != null) {
            return user;
        }

        user = Database.getUserById(userId);
        # timeout是存在cache里的时间
        # 一般不会设为永不超时，为了避免数据库和缓存的不一致现象（inconsistency）
        Cache.set(key, user, timeout=7 * 86400);
        return user;
    }

    public void setUser(User user) {
        String key = userCacheKey(user.id);
        Database.setUser(user);
        Cache.delete(key);
    }
}