package com.lldprep.classic.parkinglot.strategy;

import com.lldprep.classic.parkinglot.enums.SpotType;
import com.lldprep.classic.parkinglot.model.ParkingSpot;
import com.lldprep.classic.parkinglot.model.Vehicle;
import java.util.Comparator;
import java.util.List;
import java.util.Optional;

public interface ParkingStrategy {
  Optional<ParkingSpot> findSpot(Vehicle vehicle, List<ParkingSpot> spots);
}

public class NearestFirstStrategy implements ParkingStrategy {
  @Override
  public Optional<ParkingSpot> findSpot(Vehicle vehicle, List<ParkingSpot> spots) {
    return spots.stream()
        .filter(ParkingSpot::isAvailable)
        .filter(s -> s.getType().fits(vehicle.getType()))
        .min(Comparator.comparing(ParkingSpot::getId));
  }
}
