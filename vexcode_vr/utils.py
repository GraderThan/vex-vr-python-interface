from js import vexcode_api

def stop_project():
    vexcode_api.stopProject()

def monitor_variable(*var_names):
    for var_name in var_names:
        if not isinstance(var_name, str):
            raise TypeError("variable names must be a string")
        vexcode_api.addVariableToMonitor(var_name)

def monitor_sensor(*sensor_names):
    for sensor_name in sensor_names:
        if not isinstance(sensor_name, str):
            raise TypeError("sensor names must be a string")
        vexcode_api.addSensorToMonitor(sensor_name)

__all__ = [
    "stop_project", "monitor_variable", "monitor_sensor"
]
