package com.lldprep.classic.parkinglot.model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ParkingFloor {
  private final int level;
  private final List<ParkingSpot> spots = new ArrayList<>();

  public ParkingFloor(int level) {
    this.level = level;
  }

  public void addSpot(ParkingSpot spot) {
    spots.add(spot);
  }

  public int getLevel() {
    return level;
  }

  public List<ParkingSpot> getSpots() {
    return Collections.unmodifiableList(spots);
  }
}
