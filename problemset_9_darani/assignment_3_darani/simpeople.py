# Used to store and manage information related to a patient.
class Patient:
    # Creates a patient object.
    def __init__( self, id_num, arrival_time ):
        self._id_num = id_num
        self._arrival_time = arrival_time

   # Gets the patient's id number.
    def id_num( self ) :
        return self._id_num

   # Gets the patient's arrival time.
    def time_arrived( self ) :
        return self._arrival_time

# Used to store and manage information related to a supermarket checkout agent.
class Doctor :
    # Creates a checkout doctor object.
    def __init__( self, id_num ):
        self._id_num = id_num
        self._patient = None
        self._stop_time = -1
        
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
    def start_service( self, cust, stop_time ):
        self._patient = cust
        self._stop_time = stop_time

    # Indicates the  doctor has finished serving the patient.
    def stop_service( self ):
        patient = self._patient
        self._patient = None
        return patient

