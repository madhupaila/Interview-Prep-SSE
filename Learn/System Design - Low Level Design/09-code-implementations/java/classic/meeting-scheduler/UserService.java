package com.lldprep.classic.meetingscheduler;

/**
 * Full reference implementation for LLD: meeting-scheduler
 * See question: 02-classic-ood/questions or matching track
 */
public class UserService {
    private final User domain;

    public UserService(User domain) {
        this.domain = domain;
    }

    public void schedule() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}
