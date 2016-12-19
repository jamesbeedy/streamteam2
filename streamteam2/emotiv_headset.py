

SENSOR_NAMES =  ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1',
                 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4']


def raw_data_all(packet):
    """Return sensor values and quality values
    """

    def get_gyro(plane):
        """Gyro helper function
        Input: a string of either 'x' or 'y'
        Return: gyro sensor value
        """
        if plane == 'x':
            return packet.gyroX
        elif plane == 'y':
            return packet.gyroY

    def sensor_val(sensor_name):
        """Sensor value helper function
        """
        return packet.sensors[sensor_name]['value']

    def sensor_qual(sensor_name):
        """Sensor quality helper function
        """
        return packet.sensors[sensor_name]['quality']


    return {'values': {k: sensor_val(k) for k in SENSOR_NAMES},
            'quality': {k: sensor_qual(k) for k in SENSOR_NAMES},
            'gyro': {k: get_gyro(k) for k in ['x', 'y']}} 
