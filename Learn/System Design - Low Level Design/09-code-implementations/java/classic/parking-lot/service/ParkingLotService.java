package com.lldprep.classic.parkinglot.service;

import com.lldprep.classic.parkinglot.enums.VehicleType;
import com.lldprep.classic.parkinglot.exception.InvalidTicketException;
import com.lldprep.classic.parkinglot.exception.LotFullException;
import com.lldprep.classic.parkinglot.model.ParkingLot;
import com.lldprep.classic.parkinglot.model.ParkingSpot;
import com.lldprep.classic.parkinglot.model.Ticket;
import com.lldprep.classic.parkinglot.model.Vehicle;
import com.lldprep.classic.parkinglot.strategy.ParkingStrategy;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.stream.Collectors;

public class ParkingLotService {
  private final ParkingLot lot;
  private final ParkingStrategy strategy;
  private final PaymentService paymentService;
  private final Map<String, Ticket> activeTickets = new ConcurrentHashMap<>();

  public ParkingLotService(
      ParkingLot lot, ParkingStrategy strategy, PaymentService paymentService) {
    this.lot = lot;
    this.strategy = strategy;
    this.paymentService = paymentService;
  }

  public Ticket park(Vehicle vehicle) {
    List<ParkingSpot> available =
        lot.allSpots()
            .filter(ParkingSpot::isAvailable)
            .collect(Collectors.toList());

    ParkingSpot spot =
        strategy
            .findSpot(vehicle, available)
            .orElseThrow(() -> new LotFullException("No spot for " + vehicle.getType()));

    synchronized (spot) {
      if (!spot.isAvailable()) {
        throw new LotFullException("Spot taken concurrently");
      }
      spot.assign(vehicle);
    }

    Ticket ticket = new Ticket(spot);
    activeTickets.put(ticket.getId(), ticket);
    return ticket;
  }

  public void unpark(Ticket ticket) {
    Ticket active =
        activeTickets.get(ticket.getId());
    if (active == null) {
      throw new InvalidTicketException("Unknown ticket: " + ticket.getId());
    }

    paymentService.charge(active);
    synchronized (active.getSpot()) {
      active.getSpot().vacate();
    }
    activeTickets.remove(ticket.getId());
  }

  public boolean isFull(VehicleType type) {
  return lot.allSpots()
        .filter(ParkingSpot::isAvailable)
        .noneMatch(s -> s.getType().fits(type));
  }
}
