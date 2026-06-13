package com.lldprep.classic.parkinglot.model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Stream;

public class ParkingLot {
  private final List<ParkingFloor> floors = new ArrayList<>();

  public void addFloor(ParkingFloor floor) {
    floors.add(floor);
  }

  public List<ParkingFloor> getFloors() {
    return Collections.unmodifiableList(floors);
  }

  public Stream<ParkingSpot> allSpots() {
    return floors.stream().flatMap(f -> f.getSpots().stream());
  }
}
