package com.lldprep.classic.parkinglot.model;

import java.time.Instant;
import java.util.UUID;

public class Ticket {
  private final String id;
  private final ParkingSpot spot;
  private final Instant entryTime;

  public Ticket(ParkingSpot spot) {
    this.id = UUID.randomUUID().toString();
    this.spot = spot;
    this.entryTime = Instant.now();
  }

  public String getId() {
    return id;
  }

  public ParkingSpot getSpot() {
    return spot;
  }

  public Instant getEntryTime() {
    return entryTime;
  }
}
