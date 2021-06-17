'''

Sample code to integrate Certificate Generator in existing projects.

The "config.ini" file needs to be setup according to the needs.
Documentation for editing the config file can be found at https://github.com/hm82/award-gen/.

'''

from certificate_generator import Certificate
ct = Certificate("Steve Rogers","Avengers Reboot 2051","1/1/2051","certificate_SteveRogers_2051-1-1.png")
x = ct.create()
if x==1:
	print("\nSTATUS : SUCCESSFUL\n")
else:
	print("\nSTATUS: FAILED\n")
