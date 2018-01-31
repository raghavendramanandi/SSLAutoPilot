import unittest
from unittest import TestCase

from genereateKeystore import getMigrateToPKCS12Command, formDname, getKeyStoreCommand


class TestGenerateKeyStore(TestCase):
    def test_getMigrateToPKCS12Command(self):
        command = getMigrateToPKCS12Command("./mtkeystore", "mypassword")
        self.assertEqual(command,
                         "keytool -importkeystore -srckeystore ./mtkeystore -destkeystore ./mtkeystore deststoretype pkcs12 -noprompt -srcstorepass mypassword")

    def test_formDname(self):
        dname = formDname("ikk.cool", "ikk", "ikk", "BAN", "KA", "IN")
        self.assertEqual(dname, "CN=ikk.cool, OU=ikk, O=ikk, L=BAN, S=KA, C=IN")

    def test_getKeyStoreCommand(self):
        command = getKeyStoreCommand("dname", "location", "password", "keypass")
        self.assertEqual(command, "keytool -genkey -noprompt -alias tomcat -dname \"dname\" -keystore location -storepass password -keypass keypass")

    if __name__ == '__main__':
        unittest.main()
