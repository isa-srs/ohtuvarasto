import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellinen_tilavuus_nollataan(self):
        varasto = Varasto(-10)

        self.assertEqual(varasto.tilavuus, 0)

    def test_virheellinen_alkusaldo_nollataan(self):
        varasto = Varasto(50, -20)

        self.assertEqual(varasto.saldo, 0)

    def test_virheellinen_lisays_ei_tee_mitaan(self):
        self.assertEqual(self.varasto.lisaa_varastoon(-10), None)
        self.assertEqual(self.varasto.tilavuus, 10)
    
    def test_varasto_tayttyy_kun_lisataan_enemman_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(20)

        self.assertEqual(self.varasto.paljonko_mahtuu(), 0)
    
    def test_virheellinen_ottaminen_ei_muuta_mitaan(self):
        self.assertEqual(self.varasto.ota_varastosta(-10), 0.0)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ei_voi_ottaa_enemman_kuin_on(self):
        self.varasto.lisaa_varastoon(5)

        self.assertEqual(self.varasto.ota_varastosta(8), 5)
        self.assertEqual(self.varasto.saldo, 0.0)
    
    def test_str_toimii(self):
        self.assertEqual(str(self.varasto), 'saldo = 0, vielä tilaa 10')
