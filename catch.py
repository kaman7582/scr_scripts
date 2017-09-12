# $language = "python"
# $interface = "1.0"

# echo "00" > /proc/nvram/iAntenna
# echo "04" > /proc/nvram/iVersion
# cat /proc/nvram/iAntenna
# swversion show
# cat /proc/nvram/SerialNumber
# cat /proc/nvram/DesKey
# cat /proc/nvram/WpaKey
# cat /proc/nvram/rfpi
# cat /proc/nvram/AuthKey
# cat /proc/nvram/BaseMacAddr
# ubus call leds set '{"state":"test"}'
# rm /rom/etc/adsl/adsl_phy.bin
# dmesg
# sync
# defaultreset
cmd_list=[ 
        "echo \"00\" > /proc/nvram/iAntenna",
	  "echo \"04\" > /proc/nvram/iVersion",
 	  "cat /proc/nvram/iAntenna",
	  "swversion show",
          "cat /proc/nvram/SerialNumber",
	"cat /proc/nvram/DesKey",
	"cat /proc/nvram/WpaKey",
	"cat /proc/nvram/rfpi",
	"cat /proc/nvram/AuthKey",
	"cat /proc/nvram/BaseMacAddr",
	 "ubus call leds set \'{\"state\":\"test\"}\'",
	"rm /rom/etc/adsl/adsl_phy.bin",
	"dmesg",
	"sync",
	"defaultreset"
]

mac_addr="00 00 00 00 00 02"
run_rest_cmd = 0
def show():

	promptString = "Base MAC Address                  :"
	crt.Screen.WaitForString(promptString)

	#screenrow = crt.Screen.CurrentRow - 3
	#result = crt.Screen.Get(screenrow, 1, screenrow, 54)
	#result = result[36:53]
	#if mac_addr != result:
	#	crt.Screen.Send(chr(13))
	szResult = crt.Screen.ReadString(promptString)

	   
def get_mac():
	crt.Screen.WaitForString("root@Inteno")
	crt.Screen.Send(cmd_list[9]+chr(13))
	crt.Screen.WaitForString("root@Inteno")
	screenrow = crt.Screen.CurrentRow - 1
	result = crt.Screen.Get(screenrow, 1, screenrow, 20)
	if result.rstrip() == mac_addr:
		run_rest_cmd=1
		crt.Screen.Send(chr(13))
	else:
		crt.Dialog.MessageBox("Mac change")
		run_rest_cmd=2


def Main():
	# Here is where we will set the value of the string that will indicate that
	# we have reached the end of the data that we wanted capture with the
	# ReadString method.
	szPrompt = "Login:"

	# Using GetScriptTab() will make this script 'tab safe' in that all of the
	# script's functionality will be carried out on the correct tab. From here
	# on out we'll use the objTab object instead of the crt object.
	objTab = crt.GetScriptTab()
	objTab.Screen.Synchronous = True

	# Instruct WaitForString and ReadString to ignore escape sequences when
	# detecting and capturing data received from the remote (this doesn't
	# affect the way the data is displayed to the screen, only how it is handled
	# by the WaitForString, WaitForStrings, and ReadString methods associated
	# with the Screen object.
	objTab.Screen.IgnoreEscape = True

	# We begin the process by sending some a command. In this example script,
	# we're simply getting a file listing from a remote UNIX system using the
	# "ls -l" command.
	szCommand = "BOS: Exit bosInit"
	
	# Wait for the command and the trailing CR to be echoed back from the remote
	# before we start capturing data... Otherwise, we'll capture the command we
	# issued, as well as the results, and in this example, we only want to
	# capture the results.
	objTab.Screen.WaitForString(szCommand)
	objTab.Screen.Send(chr(13))


	objTab.Screen.WaitForString("Inteno login")
	#objTab.Screen.Send(chr(13))
	#objTab.Screen.WaitForString("Inteno login")
	objTab.Screen.Send("root" + chr(13))
	objTab.Screen.Send("1nten0tech" + chr(13))
	objTab.Screen.WaitForString("activate this console")
	objTab.Screen.Send(chr(13))
	objTab.Screen.WaitForString("Inteno login")
	objTab.Screen.Send("root" + chr(13))
	objTab.Screen.WaitForString("Password")
	objTab.Screen.Send("1nten0tech" + chr(13))
	#objTab.Screen.Send("1nten0tech" + chr(13))
	objTab.Screen.WaitForString("root@Inteno")
	objTab.Screen.Send(cmd_list[9]+chr(13))
	objTab.Screen.WaitForString("root@Inteno")
	screenrow = objTab.Screen.CurrentRow - 1
	result = objTab.Screen.Get(screenrow, 1, screenrow, 20)
	objTab.Screen.Send(chr(13))
	if result.rstrip() == mac_addr:
		for elem in cmd_list:
			objTab.Screen.WaitForString("root@Inteno")
			objTab.Screen.Send(elem+chr(13))
		objTab.Screen.WaitForString("root@Inteno")
		objTab.Screen.Send("reboot"+chr(13))
	else:
		run_rest_cmd=2
	return

while run_rest_cmd != 2:
	#get_mac()
	#show()
	Main()
	#show()
