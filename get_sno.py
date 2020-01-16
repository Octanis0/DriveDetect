import wmi

driveID = ''			#input serial number of specific drive

def detect_drive():
	global driveID
	usb = 0
	c = wmi.WMI()
	for item in c.Win32_PhysicalMedia():
		if item.SerialNumber.strip() == driveID:
			usb = 1
	return usb