# $language = "python"
# $interface = "1.0"

# This automatically generated script may need to be
# edited in order to work correctly.

def Main():
	crt.Screen.Synchronous = True
	crt.Screen.Send("root" + chr(13))
	crt.Screen.WaitForString("Password: ")
	crt.Screen.Send("1nten0tech" + chr(13))

Main()
