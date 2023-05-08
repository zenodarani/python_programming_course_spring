# Implementation of the main simulation class.
from problemset_9_darani.assignment_2_darani.llistqueue import Queue
from simpeople import Doctor, Patient
from random import random
from random import seed


class HospitalSimulation:
    # Create a simulation object.
    def __init__( self, num_doctors, num_minutes, between_time):
        # Parameters supplied by the user.
        self._arrive_prob = 1.0 / between_time
        self._num_minutes = num_minutes
        
        # Simulation components.
        self._patients_queue = Queue()
        self._doctors = []
        
        for i in range( num_doctors ) :
            self._doctors.append(Doctor(i+1))
            
        # Computed during the simulation.
        self._total_wait_time = 0
        self._num_patients = 0

        # Results
        self._cured = list()
        self._dead = list()

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
        print("Number of patient served = ", num_served)
        print("Number of patient remaining in line = %d" %
              len(self._patients_queue))
        print("The average wait time was %4.2f minutes." % avg_wait)
        print(f"Cure rate is: {len(self._cured)/num_served:2.2%} ({len(self._cured)})")
        print(f"Death rate is: {len(self._dead)/num_served:2.2%} ({len(self._dead)})")

    def _handle_arrival(self, cur_time ):
        # Handles simulation rule #1.
        if random() < self._arrive_prob:
            self._num_patients += 1
            patient = Patient(self._num_patients, cur_time)
            self._patients_queue.enqueue(patient)
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
                patient = self._patients_queue.dequeue()
                doctor.cure_patient(patient, cur_time)
                print("Doctor #", doctor.id_num(), "starts processing Patient #", patient.id_num(), " at time", cur_time)

    def _handle_end_service(self, cur_time ):
        # Handles simulation rule #3.
        for doctor in self._doctors:
            if not doctor.is_free():
                if doctor._stop_time == cur_time:
                    cure_time = doctor.current_patient_cure_time(cur_time)
                    patient = doctor.cure_completed()
                    print("Doctor #", doctor.id_num(), " finishes processing Patient #",
                          patient.id_num(), " at time", cur_time)
                    total_time = cur_time - patient._arrival_time
                    
                    print("Patient #", patient.id_num(), " has spent ", total_time, " minutes in the system")
                    print("of which ", total_time - cure_time, " waiting")
                    self._total_wait_time += total_time - cure_time
                    # check if the patient is still alive or is dead
                    if patient.is_still_alive(cur_time):
                        self._cured.append(patient)
                    else:
                        self._dead.append(patient)


if __name__ == "__main__":
    sim = HospitalSimulation(3, 1440, 4)
    sim.run(1)
    sim.print_results()
