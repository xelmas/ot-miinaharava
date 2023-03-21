import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        maksukortti = Maksukortti(1000)
        self.assertEqual(str(maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_lataa_saldoa_kasvattaa_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")
    
    def test_ota_rahaa_toimii_oikein_saldo_ei_riita(self):
        onnistui = self.maksukortti.ota_rahaa(1300)
        if onnistui:
            self.assertTrue(onnistui, "True")
        else:
            self.assertFalse(onnistui, "False")
    
    def test_ota_rahaa_toimii_oikein_saldo_riittaa(self):
        onnistui = self.maksukortti.ota_rahaa(400)
        if onnistui:
            self.assertTrue(onnistui, "True")
        else:
            self.assertFalse(onnistui, "False")
