import poplib
pop3=poplib.POP3_SSL('pop.asia.secureserver.net')
print(pop3.user("info@serdarsezgin.com"))
print(pop3.pass_("11062001"))
mliste=pop3.list()
print(mliste)
#print("resp , metin", oct=pop3.retr(1))
response, metin, oct=pop3.retr('1')

##import StringIO
##hafizados=StringIO.StringIO("\n".join(metin))
##mektup=rfc822.Message(hafizados)
##mektup.keys()
