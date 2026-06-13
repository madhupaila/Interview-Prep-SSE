package com.lldprep.patterns.strategypayment;

public class StripeProcessor implements PaymentProcessor {
    @Override
    public void pay(double amount) {
        System.out.println("Stripe: charged $" + amount);
    }
}
