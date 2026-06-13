package com.lldprep.classic.parkinglot.model;

import com.lldprep.classic.parkinglot.enums.SpotType;

public class ParkingSpot {
  private final String id;
  private final SpotType type;
  private Vehicle vehicle;

  public ParkingSpot(String id, SpotType type) {
    this.id = id;
    this.type = type;
  }

  public synchronized boolean isAvailable() {
    return vehicle == null;
  }

  public synchronized void assign(Vehicle vehicle) {
    if (!isAvailable()) {
      throw new IllegalStateException("Spot " + id + " is occupied");
    }
    this.vehicle = vehicle;
  }

  public synchronized void vacate() {
    this.vehicle = null;
  }

  public String getId() {
    return id;
  }

  public SpotType getType() {
    return type;
  }
}
