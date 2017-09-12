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

cmd1="echo \"AAAAA11111222223\" > /proc/nvram/AuthKey"


mac_addr=['02',' ','10',' ','18',' ','01',' ','00',' ','01']
run_rest_cmd = 0
counter= 1

def counter_inc():
	global counter
	if counter == 255:
		counter=1
	else:
		counter=counter+1

	return 

def show():

	promptString = "Base MAC Address                  :"
	crt.Screen.WaitForString(promptString)

	#screenrow = crt.Screen.CurrentRow - 3
	#result = crt.Screen.Get(screenrow, 1, screenrow, 54)
	#result = result[36:53]
	#if mac_addr != result:
	#	crt.Screen.Send(chr(13))
	szResult = crt.Screen.ReadString(promptString)

def mac_cmd_format():
	#mc_list=[]
	#str_len=len(get_mac)
	global counter
	inc_mac="{:0>2x}".format(counter)
	mac_addr[10]=inc_mac
	new_mac=''.join(mac_addr)
	return new_mac

def get_cmdline():
	mac_new=mac_cmd_format()
	str1="echo "
	str2="/proc/nvram/BaseMacAddr"
	str3="\"%s\" > "%mac_new
	cmd_ret=str1+str3+str2
	return cmd_ret

	   
def get_mac():
	global counter
	current_mac=mac_cmd_format()
	
	mac_cmd='cat /proc/nvram/BaseMacAddr'
	
	crt.Screen.Send(mac_cmd + chr(13))
	crt.Screen.WaitForString(">")
	screenrow = crt.Screen.CurrentRow-1
	result = crt.Screen.Get(screenrow, 1, screenrow, 18)
	result = result.rstrip()
	#crt.Dialog.MessageBox(result)
	if current_mac == result:
		
		counter_inc()
		send_cmd=get_cmdline()
		crt.Screen.Send(send_cmd + chr(13))
		crt.Screen.WaitForString(">")
		crt.Screen.Send("reboot" + chr(13))
		#crt.Dialog.MessageBox(send_cmd)
		
	else:
		run_rest_cmd = 2
	return
	
def parser_string(usr_log):
	
	return

def check_uboot():
	global run_rest_cmd
	crt.Screen.WaitForString("Base: 4.16_05")
	#screenrow = crt.Screen.CurrentRow
	szResult = crt.Screen.ReadString("isUbiFlashLayout")
	cmp_str="valid=0"
	if szResult.find(cmp_str) == -1:
		crt.Screen.WaitForString("stop auto run")
		crt.Screen.Send(chr(13))
		crt.Screen.WaitForString("CFE>")
		run_rest_cmd=2
	return
	

def change_mac():
	counter_inc()
	send_cmd=get_cmdline()		
	crt.Screen.Send(send_cmd + chr(13))
	crt.Screen.WaitForString(">")
	crt.Screen.Send("reboot" + chr(13))
	crt.Screen.WaitForString("Restarting system")
	return

def Main():

	szPrompt = "Login:"


	objTab = crt.GetScriptTab()
	objTab.Screen.Synchronous = True


	objTab.Screen.IgnoreEscape = True


	szCommand = "device wl1 entered"
	
	# Wait for the command and the trailing CR to be echoed back from the remote
	# before we start capturing data... Otherwise, we'll capture the command we
	# issued, as well as the results, and in this example, we only want to
	# capture the results.
	objTab.Screen.WaitForString(szCommand)
	objTab.Screen.Send(chr(13))


	objTab.Screen.WaitForString("Login")
	#objTab.Screen.Send(chr(13))
	#objTab.Screen.WaitForString("Inteno login")
	objTab.Screen.Send("admin" + chr(13))
	objTab.Screen.WaitForString("Password")
	objTab.Screen.Send("admin" + chr(13))
	objTab.Screen.WaitForString(">")
	objTab.Screen.Send(cmd1 + chr(13))
	objTab.Screen.WaitForString(">")
	objTab.Screen.WaitForString(">")
	change_mac()
	return

while run_rest_cmd != 2:
	check_uboot()
	Main()
#get_mac()
	#show()
	#Main()
	#counter = counter+1
	#show()

