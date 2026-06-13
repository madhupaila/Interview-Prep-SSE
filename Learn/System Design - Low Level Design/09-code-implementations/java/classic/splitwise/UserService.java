package com.lldprep.classic.splitwise;

/**
 * Full reference implementation for LLD: splitwise
 * See question: 02-classic-ood/questions or matching track
 */
public class UserService {
    private final User domain;

    public UserService(User domain) {
        this.domain = domain;
    }

    public void addExpense() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}
