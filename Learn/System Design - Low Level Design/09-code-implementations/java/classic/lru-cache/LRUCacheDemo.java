package com.lldprep.classic.lrucache;

public class LRUCacheDemo {
    public static void main(String[] args) {
        LRUCache<Integer, String> cache = new LRUCache<>(2);
        cache.put(1, "a");
        cache.put(2, "b");
        System.out.println(cache.get(1));
        cache.put(3, "c");
        System.out.println(cache.get(2)); // null — evicted
    }
}
