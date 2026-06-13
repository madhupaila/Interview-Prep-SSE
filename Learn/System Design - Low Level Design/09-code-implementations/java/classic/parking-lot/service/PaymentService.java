package com.lldprep.classic.parkinglot.service;

import com.lldprep.classic.parkinglot.model.Ticket;

public interface PaymentService {
  void charge(Ticket ticket);
}

public class SimplePaymentService implements PaymentService {
  @Override
  public void charge(Ticket ticket) {
    // MVP: no-op or flat fee calculation
  }
}
