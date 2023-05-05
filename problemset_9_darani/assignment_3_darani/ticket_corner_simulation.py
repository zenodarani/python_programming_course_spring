# Implementation of the main simulation class.
from problemset_9_darani.assignment_2_darani.llistqueue import Queue
from simpeople import Doctor, Patient
from random import random
from random import seed


class HospitalSimulation:
    # Create a simulation object.
    def __init__( self, num_doctors, num_minutes, between_time, service_time ):
        # Parameters supplied by the user.
        self._arrive_prob = 1.0 / between_time
        self._service_time = service_time
        self._num_minutes = num_minutes
        
        # Simulation components.
        self._patients_queue = Queue()
        self._doctors = []
        
        for i in range( num_doctors ) :
            self._doctors.append(Doctor(i+1))
            
        # Computed during the simulation.
        self._total_wait_time = 0
        self._num_patients = 0

    # Run the simulation using the parameters supplied earlier.
    def run( self, my_seed ):
        seed(my_seed)
        
        for cur_time in range(self._num_minutes + 1) :
            self._handle_arrival( cur_time )
            self._handle_begin_service( cur_time )
            self._handle_end_service( cur_time )

    # Print the simulation results.
    def print_results(self):
        num_served = self._num_patients - len(self._patients_queue)
        avg_wait = float(self._total_wait_time) / num_served
        print("")
        print("Number of passengers served = ", num_served)
        print("Number of passengers remaining in line = %d" %
              len(self._patients_queue))
        print("The average wait time was %4.2f minutes." % avg_wait)

    def _handle_arrival(self, cur_time ):
        # Handles simulation rule #1.
        if random() < self._arrive_prob:
            self._num_patients += 1
            cust = Patient(self._num_patients, cur_time)
            self._patients_queue.enqueue(cust)
            print("Patient #",self._num_patients, "arrived at time", cur_time)
            print("Queue length is", len(self._patients_queue))

    def _handle_begin_service(self, cur_time ):
        # Handles simulation rule #2.
        # find a free doctor
        doctor = self._doctors[0]
        i=0
        while not doctor.is_free() and i < len(self._doctors):
            doctor = self._doctors[i]
            i += 1
            
        # if a free doctor has been found
        if doctor is not None and doctor.is_free():
            if not self._patients_queue.is_empty():
                cust = self._patients_queue.dequeue()
                doctor.start_service(cust,cur_time + self._service_time)
                print("Agent #", doctor.id_num(), "starts processing Patient #", cust.id_num(), " at time", cur_time)

    def _handle_end_service(self, cur_time ):
        # Handles simulation rule #3.
        for doctor in self._doctors:
            if not doctor.is_free():
                if doctor._stop_time == cur_time:
                    cust=doctor.stop_service()
                    print("Agent #", doctor.id_num(), " finishes processing Patient #", \
                          cust.id_num(), " at time", cur_time)
                    total_time = cur_time - cust._arrival_time
                    
                    print("Patient #", cust.id_num(), " has spent ", total_time, " minutes in the system")
                    print("of which ", total_time - self._service_time, " waiting")
                    self._total_wait_time += total_time - self._service_time