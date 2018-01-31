from runCertbot import runCertbot
from setupCertbot import setupCertbot


def certifyFromCA(sslRequest):
    setupCertbot()
    runCertbot(sslRequest)


