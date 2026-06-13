package com.lldprep.patterns.strategypayment;

/**
 * Full reference implementation for LLD: strategy-payment
 * See question: 02-classic-ood/questions or matching track
 */
public class PaymentProcessorService {
    private final PaymentProcessor domain;

    public PaymentProcessorService(PaymentProcessor domain) {
        this.domain = domain;
    }

    public void process() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}
