package com.lldprep.concurrency.producerconsumer;

/**
 * Full reference implementation for LLD: producer-consumer
 * See question: 02-classic-ood/questions or matching track
 */
public class ProducerService {
    private final Producer domain;

    public ProducerService(Producer domain) {
        this.domain = domain;
    }

    public void produce() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}
