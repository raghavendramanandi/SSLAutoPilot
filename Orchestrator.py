###Should Have###
# brew
# java8
# tomcat8
# wget
# internet connection
# This tool internally uses certbot(Which uses ACME protocol)
# certificate from certbot is downloaded to the certbot file location
# certificate file is assumed to have name 0001_cert.perm
# once done add changes to your server.xml
from CACertify import certifyFromCA
from SSLRequest import SSLRequest
from generateCSR import generateCSR
from genereateKeystore import generateKeyStoreFor
from importCertificate import importCertbotCertificate

sslRequest = SSLRequest()
sslRequest.readSLLRequest()
generateKeyStoreFor(sslRequest)
generateCSR(sslRequest)
certifyFromCA(sslRequest)
importCertbotCertificate(sslRequest)
