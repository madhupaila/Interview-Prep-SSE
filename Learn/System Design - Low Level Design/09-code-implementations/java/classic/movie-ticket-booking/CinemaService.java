package com.lldprep.classic.movieticketbooking;

/**
 * Full reference implementation for LLD: movie-ticket-booking
 * See question: 02-classic-ood/questions or matching track
 */
public class CinemaService {
    private final Cinema domain;

    public CinemaService(Cinema domain) {
        this.domain = domain;
    }

    public void bookSeats() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}
