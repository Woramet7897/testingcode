import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from functions.caesar_cipher import caesarCipher
import unittest


class PrimeListTest(unittest.TestCase):
    def test_give_Lipps_Asvph(self):
        n = 12
        s = "Hello_World"
        k = 4
        result = caesarCipher(s, k)
        self.assertEqual(result, "Lipps_Asvph")

    def test_give_Ciphering(self):
        n = 10
        s = "Ciphering"
        k = 26
        result = caesarCipher(s, k)
        self.assertEqual(result, "Ciphering")

    def test_give_fff_jkl_gh(self):  # fff.jkl.gh
        n = 10
        s = "www.abc.xy"
        k = 87
        result = caesarCipher(s, k)
        self.assertEqual(result, "fff.jkl.gh")

    def test_give_159357fwzx(self):
        n = 10
        s = "159357lcfd"
        k = 98
        result = caesarCipher(s, k)
        self.assertEqual(result, "159357fwzx")

    def test_give_D3q4(self):
        n = 4
        s = "D3q4"
        k = 0
        result = caesarCipher(s, k)
        self.assertEqual(result, "D3q4")

    def test_give_okffng_Qwvb(self):  # okffng-Qwvb
        n = 11
        s = "middle-Outz"
        k = 2
        result = caesarCipher(s, k)
        self.assertEqual(result, "okffng-Qwvb")

    def test_give_90_string(
        self,
    ):  #!w-bL`-yX!.G`mVKmFlX/MaCyyvSS!CSwts.!g/`He`eJk1DGZBa`eBLdyu`hZD`vV-jZDm.LCBSre..-!.!dmv!-E
        n = 90
        s = "!m-rB`-oN!.W`cLAcVbN/CqSoolII!SImji.!w/`Xu`uZa1TWPRq`uRBtok`xPT`lL-zPTc.BSRIhu..-!.!tcl!-U"
        k = 62
        result = caesarCipher(s, k)
        self.assertEqual(
            result,
            "!w-bL`-yX!.G`mVKmFlX/MaCyyvSS!CSwts.!g/`He`eJk1DGZBa`eBLdyu`hZD`vV-jZDm.LCBSre..-!.!dmv!-E",
        )

    def test_give_Dn__oW_X_SjthvUV(self):  # Dn-/oW/X`SjthvUV
        n = 16
        s = "Pz-/aI/J`EvfthGH"
        k = 66
        result = caesarCipher(s, k)
        self.assertEqual(result, "Dn-/oW/X`SjthvUV")

    def test_give_100_string(
        self,
    ):  # WGYcqh?u5a*5<EPuzl6?O5{3F].1aZ)io1OPj4(!][WS3Z)kbLC.VfNc9]7Zse?OrxC2wBIXP4ZRP*lvM8(oan9pVk]j!7xrthr.
        n = 100
        s = "DNFjxo?b5h*5<LWbgs6?V5{3M].1hG)pv1VWq4(!][DZ3G)riSJ.CmUj9]7Gzl?VyeJ2dIPEW4GYW*scT8(vhu9wCr]q!7eyaoy."
        k = 45
        result = caesarCipher(s, k)
        self.assertEqual(
            result,
            "WGYcqh?u5a*5<EPuzl6?O5{3F].1aZ)io1OPj4(!][WS3Z)kbLC.VfNc9]7Zse?OrxC2wBIXP4ZRP*lvM8(oan9pVk]j!7xrthr.",
        )

    def test_give_53_string(
        self,
    ):  # 6MFE95QigCLQY85mee3WH2laic1jX8s6p2iBMeODrSs6GFMuIeWWa
        n = 53
        s = "6DWV95HzxTCHP85dvv3NY2crzt1aO8j6g2zSDvFUiJj6XWDlZvNNr"
        k = 87
        result = caesarCipher(s, k)
        self.assertEqual(
            result, "6MFE95QigCLQY85mee3WH2laic1jX8s6p2iBMeODrSs6GFMuIeWWa"
        )

    def test_give_78_string(
        self,
    ):  # 1Y7U4WsDt23l4ww08E6zR3T19H4sWQ188N9bivyC6k1uNHAt1n10fz7fVk62XW2fyMU4D83am7R80N
        n = 78
        s = "1X7T4VrCs23k4vv08D6yQ3S19G4rVP188M9ahuxB6j1tMGZs1m10ey7eUj62WV2exLT4C83zl7Q80M"
        k = 27
        result = caesarCipher(s, k)
        self.assertEqual(
            result,
            "1Y7U4WsDt23l4ww08E6zR3T19H4sWQ188N9bivyC6k1uNHAt1n10fz7fVk62XW2fyMU4D83am7R80N",
        )

    def test_give_38_string(self):  # Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj
        n = 38
        s = "Always-Look-on-the-Bright-Side-of-Life"
        k = 5
        result = caesarCipher(s, k)
        self.assertEqual(result, "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj")


if __name__ == "__main__":
    unittest.main()
