import unittest
from unittest import TestCase

from setupCertbot import getChangePriveledgeOnCertbotCommand


class TestSetupCertbot(TestCase):

    def test_changePriveledgesCommand(self):
        command = getChangePriveledgeOnCertbotCommand(".")
        self.assertEqual(command, 'chmod 777 ./certbot-auto')

    def test_computeNumber(self):
        ipaddress = "52.66.191.170"
        print(ipaddress)
        sum = 0
        for item in ipaddress:
            if item.isnumeric():
                sum = sum + int(item)

        print(sum)
        self.assertEqual(ipaddress, 'chmod 777 ./certbot-auto')

    if __name__ == '__main__':
        unittest.main()
