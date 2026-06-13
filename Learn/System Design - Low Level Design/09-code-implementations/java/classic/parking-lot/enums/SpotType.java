package com.lldprep.classic.parkinglot.enums;

public enum SpotType {
  COMPACT,
  LARGE,
  HANDICAP;

  public boolean fits(VehicleType vehicleType) {
    return switch (vehicleType) {
      case MOTORCYCLE -> true;
      case CAR -> this == COMPACT || this == LARGE || this == HANDICAP;
      case TRUCK -> this == LARGE;
    };
  }
}
