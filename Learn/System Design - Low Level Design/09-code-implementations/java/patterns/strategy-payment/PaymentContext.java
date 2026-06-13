package com.lldprep.patterns.strategypayment;

public class PaymentContext {
    private PaymentProcessor processor;

    public void setProcessor(PaymentProcessor processor) {
        this.processor = processor;
    }

    public void checkout(double amount) {
        processor.pay(amount);
    }
}
