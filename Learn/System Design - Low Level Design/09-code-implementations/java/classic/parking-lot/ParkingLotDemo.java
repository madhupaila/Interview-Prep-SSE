package com.lldprep.classic.parkinglot;

import com.lldprep.classic.parkinglot.enums.SpotType;
import com.lldprep.classic.parkinglot.enums.VehicleType;
import com.lldprep.classic.parkinglot.model.ParkingFloor;
import com.lldprep.classic.parkinglot.model.ParkingLot;
import com.lldprep.classic.parkinglot.model.ParkingSpot;
import com.lldprep.classic.parkinglot.model.Vehicle;
import com.lldprep.classic.parkinglot.service.ParkingLotService;
import com.lldprep.classic.parkinglot.service.SimplePaymentService;
import com.lldprep.classic.parkinglot.strategy.NearestFirstStrategy;

public class ParkingLotDemo {
  public static void main(String[] args) {
    ParkingLot lot = new ParkingLot();
    ParkingFloor floor = new ParkingFloor(1);
    floor.addSpot(new ParkingSpot("1A", SpotType.COMPACT));
    floor.addSpot(new ParkingSpot("1B", SpotType.LARGE));
    lot.addFloor(floor);

    ParkingLotService service =
        new ParkingLotService(lot, new NearestFirstStrategy(), new SimplePaymentService());

    var ticket = service.park(new Vehicle("ABC-123", VehicleType.CAR));
    System.out.println("Parked with ticket: " + ticket.getId());
    service.unpark(ticket);
    System.out.println("Unparked successfully");
  }
}
