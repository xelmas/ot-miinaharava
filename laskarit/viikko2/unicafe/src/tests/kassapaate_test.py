import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_myytyjen_lounaiden_maara_alussa_on_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kassapaatteen_alkusaldo_on_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_edullisesti_kateisella_toimii_maksu_riittaa(self):
        maksu = 260
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(maksu)
        if vaihtoraha >= 0:
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
            self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_kateisella_toimii_maksu_ei_riita(self):
        maksu = 200
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(maksu)
        if vaihtoraha == maksu:
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
            self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_maukkaasti_kateisella_toimii_maksu_riittaa(self):
        maksu = 500
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(maksu)
        if vaihtoraha >= 0:
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
            self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_maukkaasti_kateisella_toimii_maksu_ei_riita(self):
        maksu = 200
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(maksu)
        if vaihtoraha == maksu:
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
            self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_syo_edullisesti_kortilla_toimii_maksu_riittaa(self):
        kortti = Maksukortti(300)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        if onnistui:
            self.assertTrue(onnistui, "True")
        else:
            self.assertFalse(onnistui, "False")

    def test_syo_edullisesti_kortilla_toimii_maksu_ei_riita(self):
        kortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        if onnistui:
            self.assertTrue(onnistui, "True")
        else:
            self.assertFalse(onnistui, "False")
    
    def test_syo_maukkaasti_kortilla_toimii_maksu_riittaa(self):
        kortti = Maksukortti(400)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        if onnistui:
            self.assertTrue(onnistui, "True")
        else:
            self.assertFalse(onnistui, "False")

    def test_syo_maukkaasti_kortilla_toimii_maksu_ei_riita(self):
        kortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        if onnistui:
            self.assertTrue(onnistui, "True")
        else:
            self.assertFalse(onnistui, "False")
    
    def test_lataa_rahaa_muuttaa_saldoa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(str(kortti), "Kortilla on rahaa 15.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
    
    def test_lataa_rahaa_ei_muuta_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -1)
        self.assertEqual(str(kortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
