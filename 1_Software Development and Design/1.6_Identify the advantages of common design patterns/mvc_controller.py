class Device: # model
    ip = ""
    port = ""

    @staticmethod
    def findDevices():
        devices = []

        d = Device()
        d.ip = "192.168.1.1"
        d.port = "80"
        devices.append(d)

        d = Device()
        d.ip = "192.168.1.2"
        d.port = "81"
        devices.append(d)

        d = Device()
        d.ip = "192.168.1.3"
        d.port = "83"
        devices.append(d)

        return devices

class DevicesView: # view

    def showDevices(self, devices):
        for device in devices:
            print("IP: " + device.ip)
            print("PORT: "+ device.port)

class DevicesController: #controller

    def __init__(self):
        devices = Device.findDevices()
        v = DevicesView()
        v.showDevices(devices)

DevicesController()