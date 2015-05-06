from sdfbuilder import Element, Link
from sdfbuilder.sensor import Sensor as SdfSensor


class Sensor(Element):
    """
    Plugin sensor base class. This is used to communicate sensor
    configuration through the SDF plugin to the model controller
    in Gazebo.
    """
    # SDF tag name, should not be changed in subclass
    TAG_NAME = 'rv:sensor'

    # Sensor type fallback
    SENSOR_TYPE = 'default'

    def __init__(self, part_id, link, sensor, driver=False, sensor_type=None):
        """
        :param part_id: ID of the part this sensor belongs to, required to identify
                        the corresponding input neuron(s).
        :type part_id: str
        :param link: Link containing the sensor
        :type link: Link
        :param sensor:
        :type sensor: SdfSensor
        :param driver: Whether or not this is the "driving" sensor. In the current setup,
                       each robot needs to have at least one sensor that triggers an update
                       of the robot's neural network. When possible, other sensors are updated
                       only at the driver time.
        :type driver: bool
        :param sensor_type: Type of the sensor
        :type sensor_type: str
        :return:
        """
        super(Sensor, self).__init__()
        self.type = sensor_type
        self.link = link
        self.sensor = sensor
        self.part_id = part_id
        self.driver = driver

    def render_attributes(self):
        """
        Adds default sensor attributes before render.
        """
        attrs = super(Sensor, self).render_attributes()
        attrs.update({
            'link': self.link.name,
            'sensor': self.sensor.name,
            'driver': str(self.driver),
            'part_id': self.part_id,
            'type': self.type if self.type is not None else self.SENSOR_TYPE
        })

        return attrs