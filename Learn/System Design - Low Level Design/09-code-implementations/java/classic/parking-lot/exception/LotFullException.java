package com.lldprep.classic.parkinglot.exception;

public class LotFullException extends RuntimeException {
  public LotFullException(String message) {
    super(message);
  }
}
