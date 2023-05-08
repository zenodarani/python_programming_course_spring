# Used to store and manage information related to a patient.
import random


class Patient:
    # Creates a patient object.
    def __init__( self, id_num, arrival_time ):
        self._id_num = id_num
        self._arrival_time = arrival_time
        # the time the patient has to live
        self._condition_severity = random.randint(15, 240)

    # Gets the patient's id number.
    def id_num( self ) :
        return self._id_num

    # Gets the patient's arrival time.
    def time_arrived( self ) :
        return self._arrival_time

    # Gets the patient condition severity in time to live when the patient arrived
    def condition_severity(self):
        return self._condition_severity

    # Gets if the patient is still alive given the current time
    def is_still_alive(self, current_time: int):
        return current_time - self.time_arrived() <= self.condition_severity()

# Used to store and manage information related to a supermarket checkout agent.
class Doctor :
    # Creates a checkout doctor object.
    def __init__( self, id_num ):
        self._id_num = id_num
        self._patient = None
        self._stop_time = -1
        self._start_time = -1
        
   # Gets the  doctor's id number.
    def id_num( self ):
        return self._id_num
    
    # Determines if the  doctor is free to serve a patient.
    def is_free( self ):
        return self._patient is None

    # Determines if the  doctor has finished serving the patient.
    def is_finished( self, curTime ):
        return self._patient is not None and self._stop_time == curTime

    # Indicates the  doctor has begun serving a patient.
    def cure_patient(self, patient, current_time):
        self._patient = patient
        self._start_time = current_time
        self._stop_time = current_time + random.randint(5, 20)

    # Indicates the  doctor has finished serving the patient.
    def cure_completed(self):
        patient = self._patient
        self._patient = None
        return patient

    # Gets for how long the patient has been treated
    def current_patient_cure_time(self, current_time):
        return current_time - self._start_time
