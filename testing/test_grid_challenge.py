import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from functions.grid_challenge import check_all


class TestDataTestCases(unittest.TestCase):

    def test_list_1(self):
        user_lst = ["5\neabcd\nfghij\nolkmn\ntrpqs\nxywuv"]
        if isinstance(user_lst, list):
            result = check_all(user_lst)
        self.assertListEqual(result, ["YES"])

    def test_list_3(self):
        user_lst = ["3\nabc\nlmp\nqrt", "3\nmpxz\nabcd\nwlmf", "4\nabc\nhjk\nmpq\nrtv"]
        if isinstance(user_lst, list):
            result = check_all(user_lst)
        self.assertListEqual(result, ["YES", "NO", "YES"])

    def test_list_5(self):
        user_lst = [
            "1\np",
            "7\nvbznfwg\neacklwk\nbmarzvp\nrwgnjqd\nxqddtln\nwuxtduk\nrzmfcik",
            "5\ntjxxx\nxtxxj\nrzzzz\nzzrzz\nrzzzz",
            "10\nzzzzzzzzzz\nzzzzzzzzzz\nzzzzzzzzzz\nzzzzzzzzzz\nzzzzzzzzzz\nzzzzzzzzzz\nzzzzzzzzzz\nzzzzzzzzzz\nzzzzzzzzzz\nzzzzzzzzzz",
            "8\numcuoqaj\nbbjgbhcr\nlpomaerv\ntknrndsj\nqxyxbtna\nwktoedyl\nkpfyjlpm\ngeixiery",
        ]
        if isinstance(user_lst, list):
            result = check_all(user_lst)
        self.assertListEqual(result, ["YES", "NO", "YES", "YES", "NO"])

    def test_list_3_2(self):
        user_lst = ["3\ngto\nwus\npgr", "5\nnhotm\ngforv\njcbuy\nxuqck\ntfhad", "1\ni"]
        if isinstance(user_lst, list):
            result = check_all(user_lst)
        self.assertListEqual(result, ["NO", "NO", "YES"])

    def test_list_2(self):
        user_lst = ["2\nwe\ntm", "3\njfg\nuzb\neeu"]
        if isinstance(user_lst, list):
            result = check_all(user_lst)
        self.assertListEqual(result, ["NO", "NO"])

    def test_list_4(self):
        user_lst = [
            "3\nuur\nuyc\nico",
            "3\nqvy\nwfe\ndmv",
            "3\nxud\nhsw\nixq",
            "4\niliv\nrpwn\nasvg\nzukt",
        ]
        if isinstance(user_lst, list):
            result = check_all(user_lst)
        self.assertListEqual(result, ["NO", "NO", "NO", "NO"])

    def test_list_6(self):
        user_lst = [
            "3\nppp\naaa\nnnn",
            "3\ncjj\njzk\nufq",
            "7\nzzzzzwz\nzzzzzzw\nwzzzzzz\nzzwzzzz\nzzyzzzz\nzzzzyzz\nzzzzzyz",
            "5\nyclsy\nbplmc\nshpvb\nulpwf\nenuih",
            "8\nwuufaemj\nkmwzzrhq\nlmjbsmkt\nvozjugzk\nrjhivvvk\nqssdyjdp\nlbuqatzy\naadxcxru",
            "5\nzxxzx\nzxxzx\nzxzxx\nxzzxx\nzzxxx",
        ]
        if isinstance(user_lst, list):
            result = check_all(user_lst)
        self.assertListEqual(result, ["NO", "NO", "YES", "NO", "NO", "YES"])

    def test_list_4_2(self):
        user_lst = [
            "100\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp",
            "6\nsvgzym\nrhrulw\nwuojgd\ndovifj\nrlcspn\ncmjzmw",
            "79\nohjkornqysvbjpdoyehwgxggtfkoqihkefkfcdjajailerztolbzelnyagqtlxegyvcliozqqthgryq\nlicoojgfdrejqiabvfvloguhbzqnlcmopmgwtbiwayckdotqvexvwquajtnhbosncleycfufmvwdlzu\nnmhlthgszqukpfeloyuqqrxtmvolrezngtizvhrmgvltlhcufeanznndawedyzrouogwkzwiqlupogg\nrvxzrkvatmnonovtmtpsrkhbkjwopshhswwpbkjcwvsyihgtqjfblzfvozxhglgpotiylqbvfrcldgu\nwiojofogkukbrhyvrhozxsvgbptsowszinanqsfxmbpsjfykdqkuwjtceiscvclzqxmkvonvzjpjllf\nlkpwohjcowvbvjgsegcldhiaebsfzgmhcavoogzkarnwcrinomcdpdanbxdmfdevgvqidgbgrcgmkdj\nviflqaoiutlabqbmnzgbsuwpfnmrzcdgyhqgdzvasokzwbemwzypuhvmpzqdcncvftfgdcphlnircoo\nsronqrigirmfoepzsozacwizxlhpkhlndtnioujmobvfwbuqayvcgailazcppsibkwsbhbybuovcqdn\nwsgftominrtupkwfuhycweupmkwdkmpdmytlhocatywbvbiakcnrdzjgpjffrxtxvuixnjrwzzkdnvn\noxrbbaxgfnixuzshcglvilurkiszgygyrtxzdnptfrxefvojgsvrleaxbzsirofkjvyyizknqvfnank\nkorphnxedsiikijfrpvfvdxmllztnmxlchneebytpxrqsneeovliqdrgjdcykhupefroiqejnklqvbv\nnfrhhmrebefyrbwqksnfehcdcigfhbcaiollgrnokojpefepjxlcdtbkrijmjewithdpqmdjnojsusw\nzpltytuownlswknwqxzlboznsfausfechygnyadlnyrtvhgyhgammcdbqkohckgetnqxgjmbhyryfgi\nimzvakbpddshpjausotkeshggrulkupdqkhoxkdegzlbthhmnodqkdkqlllzugohmfnwervgupwtmgs\nyotvhwssrbegwmntsnxktoyzhnkmcqqyfnuvosuzdigxwwaccezojhvyggtcwrhmtsoekfqxnvoetwk\nrfukzbbuxhoybtkscwvavgunwxeawfuwnidzecxmztuiphqxpyzqbmiyqrwbdcqzbfzxjiulvbsdmxe\npnhfwdaezeojlxbsmgtbnsnrxmzxywbzzlfoouldfocfefokdeqsechzxdkzqmkiftiqyvrigqhnohe\nrrhioibddewxzzaffqdytfaawlseztnzqwlkzvgqjchatzdecnpuvfbozozaktitnvfogolgejvmper\nvgybgsfatwuzgokqniyiqwemgfllalmupogjysdyqdrcdkfksjjrhcrvdhorqqmkghnvxcgjwmjbizz\nbrsrgweqdmjrfnjxjiuswsipmpnebcolutsnnydodbksikcrftpeffufgucvboutfnqjufazmathpbc\nfxwpdfxzqrvarwnueslkmrxyfzddpokjaahnrqrqrycezjitdxbtdwicgbzukcxgdtanjdheyzwhuxd\nochqqaosnqxzzusmxekwaxfhfgucvmhqvxagwujozfdcsopejwcxqzsjtysqluudpzsumttcuigzgwn\nmkiqomvzjhrifmlzrhfzljbhkmakjuxdawsuykpvsrqbwvgqbilcastdlshxogevqxnxhhrrhkwsfpp\nocjludwfxilcqxtzftvjhvdhszngzpgyakfyaicabwdfftrodqxiddpnsedziinorenmlczkfcakphk\nonhiymgagkusvnndmhzfmphjxrvwgmrdfyyvybwdhusczaqpliwrjsbnpgsjzlcfaezwyknaytghqjo\ntpiveslazvbphaqedduzpmchzxnvkwupocwphauimqkhcpxyoalxpkwloclzhjhouyimkdfmqipugtw\ncecniazfshbvmtqksfbllvwiubvwjigaeyxkwotpiawstwhkoeahaaviogczubmeilrafzhvzhqylsm\nbwwjwgeszxhxtcrxppofllzhwochfiuypbjjpwthfcaafhprdzoziihprbjgnhoqzbwhzbtlueapylm\najgyrryqekhykwkwagohyflidwiludxhhcgnfucrxphjibfllwrmlmxylysoalejvdfcxzsqichcrfr\nlcdcmdapbtmfjnlmghqbpsckrehicmuuwitxpjkndovqwjjpgvaaqunhctgmmvunlaxogrartqximjz\noyfmyigglueqgsinmawwjorkypjperwuourlyyvisttutbckjtassdicwwfbpybptwxyvkifcmycjdo\nhwxlxhqxzbupmrprhprnccnpstyjlksznslhxbckylqgwxptjcyxvryfrnscpmjdjjukuviqbubkiod\nkgpstmflxazupzwwkhontonrqlqbahtzcrtxodbzkfwktgfwsmhykwsosnqkhhrazrwfsbqvcxddgzi\nhguocjvwqupypotxclxmpearaumgjdiqpnaxmjrrrtqrswtiylshnzujdgbupexutzrivwztietefel\nipxgwryqclflswwcfdvumldpmxpaqjtggthrcxlvplsflyqmdanjazmsluzvtkxxzjyhgdsmfvvpgzp\nnnstjyrfzqoszzseevlnbfprjadjclgyihqintbmxiwlqwgxhlmzkthbcpaznppaujyhtrthizaxglk\nactvmxxitvaxdqcxqdnstlxpamswfpcrxwloglacthzszqdoznhsadgukdmflihnwklsommhqgisnqy\ntaqdksuoezevixofoiyupocaqmkzpsdzxfkonrmrvkelbbsjgfuiwmmtcvuyvciszkkpwobukcfmrus\nsywyxvbjcsvbtlzzqsffztzbdowewtzjajcbauvcwpkllsypapprxgpnjamryhbnxjmagdouqikklzi\nlnmnkrugditryuyolqayrpbstqquhovaiavdeegqynvzgtefhpsuqapidfjcpzegvndzrfayuepjpnu\nresrzsqewjbieaubmbkabagslnhbvknazxnbzfothtssxjiuiavnccxgsfpigbgimmmjnegedsppzjb\ngqfdywhcoaaahkndfxtftenigyxutpfmobfgxtlcewythrninhhgtabcvrphoncyzutncmwihwcflok\ngafpvowvmfswbsmdfivatwwckpdzqmxfxxgzivlzgexvlsdxswqeqnxlddkeqhwanqxronrkpwletnd\nyqtlynzhcgftwpajbpswksbaaetgzjmruqmmbkszzyuwwwgvejycgpdpthdzhxgpfkpcqyjpwuosduy\ntjcfhwyrtqsavoprezxbsawyhwrcypzszqqemvqkmyudsubhrcaqkbqpwvaucsxghiqyfzovxcijwhc\nszdcgfcoighhqstbfymplcrzxhtwotqacsdozmvztuowwmvygflhhhhipjrfvopjztuctjftzwislqz\nokmdhtktdkhbjfchlosmgachttoyyqiquaddyhdcghfxkzliwdyybynkgjrjogdqtzjigpwxrfstvib\nfotbeuboewlbgteyjpokvfbxbevnderacfnvhccnoqxjinwpeqwikluxhyfqyrsewukdnphfcazsagc\nrbwzdzxzortrknnwwmlxnfomtcdutdiapkmlqdsogyinctgoohudvpebrbhpfoxkfyfxwstwwkoihbt\nuceyzborewfzefgrlhxskzyvyvntcfsspsaabxsgmtevugzgjadfppbenrlfkkcocvynposmtcbeakp\ndhefkplwpvmdbvfirsedxbdycwvkhhqbkofyyyryggeaxmywzwfsywvoenqwcdotyxgbdubnunfqozq\ntubtkxppcykhurtcufcbbjyxxbmjuppqatajefpftqssbsjlcxlzigdzosgshijsgiynpjwjmolikvg\noxywakkdeaiwqmohsbcxxsziozqfcilgyorqbqvunrqaarksdevmotofqijbecgauwjnlkjbhvpycsn\nmbdnvawavwjbyxpvcjnkfxgpacqbhtfaooatqdadyoaawzhczwjulpgdetprlpaqxrxomyhtefkgfbc\nuwsuduetepefwaxnqudzbbpegckxcmeeiogslitiszgqbyywvtoygqfbyouqsyhkdjoejarctttfnqz\ndrlsgljcsvkrfqqxursybhtjaffgsiqvhzhndqpmretwnauosrqdxusmmkpmikaiwemigniuarcsukt\nozkgwywpjtrgjhneosabdeeaidnpciyutsrpqugyfrlkxfncdgdvqaesxxxxygaashczstdbazejklb\nduvsqydsrymmupqlsaxnxqdpvfnszgduqpwrwpypqmfdmomsnvwnxxicgajobtalwkvbpqdovtlipjl\nxiblgwatmdhgrbavzidqcghlshzgfilfpaeyoxgcdlywtttitmdgisoulibvsollcyuikntbvabpbur\nuuseekiwopmcltfehckuigmrjwjduhcffikbhffeeinxiwsdzbyalteiyelswxnstlvsldmfqwdkgcv\nujfdticdsmkzrtgecokxjnnjbfzyhnijwcjrdogmfokfidydqynfjpajvlabxpriwamzmvehgecrnrz\nbwqaipeiqqnsazmezazlveevgjezhrkhiqsomvfppntbsthfsluqgszevczqpupiaoycmwhxrhjzdav\nkajiynezhmvvbuipztmwmaikpubnranpvgbemyxtxaeqgdzyfosabnthbngpnyogfjcrseqjcfxmtpf\nedoklaljfzkvdqgqzlszkjjtcgodjhcjwssqiukyfsrctxrtofesxcbrxbblzcgnegevxtyprrcilyw\ngxqkamblkqvqlpprkydmftvwokhyzqspmlzzykqmohhcvknditzsadypbvzszbetnhrjlxabxhfwlhb\navksfohrpoofxzqmtthsuglptcejvotfrbmwnvnqxuwdzocydzdeeozenaeczoxmuatnxgktopvqwaq\nrjufuysfcnpcozrwscdgmnfnqakhpnlvveclkivkcxhihcslowfxbzdutrigwpfnhpyifmqxpdislwl\nnoliodhuwdsgbybiknrgrmtbgptybqmfqavrifhqzvhtfzaabvegrujalqxagtjfmvnucicqodljzlt\nlmfnknwmqzzddzrkftgswcdnkbmaxyzwfapsnlpzkmmekrbkkeqjgvmybhichupzyxgkdxtwttrtyik\nauwrxylolbifmrgurpqplxdppdjbkxxqeqhqbujqxmkdwbattgovkrvxhyzdftmakawkvypedwkwbtq\nuscyfxekxwtpvrrfcpkwabfqsmtnpsualiobntvrkjebxwtnpqedgzviqzlosuqnntjsupiqetikbuz\nvrseumygahsszsrnirfpaceuerzxbzcwtletahvbbuggsboldormnegbrcaetlmrwgfytkiemgwfpyp\nbtfbizsobrvylbwcmupjyhcdfethovsssacvayqafcxdjqsmnwbsitiqgpqcnihjdwfscejsscsdlod\nneirqmwwkufvuutdwtoupouuygmyvhsjofhabeenwlnlbdyqidwwdqlcknfobytiswyqrsygukjberk\ntfvxtfdrytqkamzdyhwmvmeyqvypnbegcoycwldkpqjyywkyvilfnwmnfhxomzitvwnyglqwafvscsm\nprjqngsofntposeagiwvtxwoecsefkjrtrjpopdchdmoxhkvglesxwijcjuqpxaywanqsxeivkrafwy\nbzwjobzeafcbgakstuzqzljqgdcntujbjwyltiedpxtjjmlnpxgyfhknmfbyhevatprmzsriyamoklr\nlfbcswbwwhtxmsznlpkukwdvrgktqdzumnqhytaottbvxxevxhjdrnllyuxssdmlhsivjhqckozdgtt\ngpsellpppcnfzqcweeibvqolxafdoqybxcctyvvucjhxhprheirqhfmepyhwlhvdvnkankaqhnwslgu",
            "56\neqecfwbulaksvukxraapksfywjozkefottjnahgoxqktxqbwyaizlhcy\nmungsxtreqxywyzytuigjkztznwwyutcmrcexsvqebbwqncqfnkyczhc\nnbjqyzpecepjwdzqrrtvtwbkqzegnvugexxnrtjbhnnjytllabhxfvzh\nxhlbusqahhxcfnmrhpinrewfgbwvcssafgrurxcfqtpqwniwokjwcydk\nqdlwexecyothcujahogjpgncevostjnlzikotghxnofvbmbksfycoiyw\nezqljdwglwhcevszjxxpsrxlpfbyiyarkdmluskkyurwonelucvbocul\ncuifeshrqmmknqjllrnlbpllzfmvyhfkyltufrjyqkqtiooiwbgayvwk\nlctvuxejqdcdwzdfjbifcmpcbaeodwjxgyzsnyfhtisgswrtllcgprri\njppbjmlaadapuuvyubrtzzkejwmvvruogedtnbplgpouwvyeagjanfkr\nsfeflkgztqhsuqgyflynzniqdxzvnkrwgnynxlwrqnpxqmdfrgpigxqr\nayiczvsifuggihrfezcmkgchqzdkaqraixgargeihukgvxcjvdrrnsud\nbfnicfxtuobjnzltwlgrakagalwksqhdhpqnofsekkdwvllvyytxymkx\nkqbawrkklwlfoqenknlheiximrzvrlmbyaseyzjfiabbovfqpdleibvp\njwfrjmdxyvpltdhxwbezlozlypwzkwmgduoqoqqzrftodwpezhzcppvq\nydsbnfztqdbxywpeeeouiibypivjdnerirgpupbhpphpondmnakakvzc\nahyutlmwyjyodenufwhbwzvrwapimrcwvwhzskyvaevnsdmginctwuwa\ndhkkwsfowwjflqwqugnxekihazxsuuomioqezztzxirjrwsgsftcewjz\npvyllboncpbeutcmpqpahmngmomiphbfodcxtwgeqhuuzjowzwpjpgol\numjsegyripdkzkezmgweenyqtrezlhqxudgogtukhemywigllyunmaxc\ntoqlugeuprmxnifugdcqnwlmiamfyssuejmcvplctjlmtyewxbnfpmdf\nircuxwijdafuwatpslvcytpaiwoekhwsmgpwduaeqobazxfgwyuqkbam\ndcgbqapbmkkepaugbojtepsfuvdbpzkwwcggrbmpfjzgrzfpsncuhydd\njqpyzxhhwrhrictpbsthtitlogtrpottggtybbjcqrbrijxzwwykzwqv\nyyxtaikypkfftyydmlpsmgbydjjxxynhlirrcuqvkzxygkvvobzmcrtp\nbxfyyolnsagznvhjgqgxgnfxrsurpfwjrgynkmwekadrqlyizjfpfdpt\nlqsrqypkwukrbouzrqechxusgwdcazoquofjzaagqruudllnfyeqhwtv\ngcyreowgwhnurhzzrooswrtidhrsztlnnqttplrayiukjhwawosrehbc\nujodjhxixhndrktfcavwjjtoelciqwplgwhwqclvtgauqujglfwqqxlg\nawolineipgkcvafzisdwzoplxufjkwdqttaiymmrbrivgjkknsjkvnzc\nxxaqkprquizvfjaedrjbtscskovetelbrefabucwaxlxadggdyufwwev\neyikfygggopsyccxsuqgrysementbzojmdcaazbooglezwfyioyfknvx\npeqgpuibtqvzggyqsmsvmsmaxtvzzbyqfewhgslsaslwssqjgtxppbgj\nqxemnirfdbqsjujndshhmezduwkksmemsqojrvmvjyvmhmhthvrdjzas\nmjvgzuhsjkwpgvsxlkjmpvskkqscwqyhtijryjqtixldgyanubratebk\nqreosrrvwwrvoglabbxuctphmekyjokwxktphmmmnxxfmalcsmmksisp\nshbcmloihvbssgogsgdmnhbixbcgakgtsbsdrpdyivondpzohshkmotm\ngikywjsnjofkmnzygsgpwdvnmucpbrgghlvxorpnhjbnxergqsymtnmw\ncmgnseptjntfkimgowmsnoziajojmdtvjubtuubfjimzghoqrqwmtbaq\nooselihhiuiajzuuocxsqzuvolrkstwocsxebebvlqrsggzxytjnebqt\naveiibadtkwhwkwwgrytfvaodrcmbgipueohvnbktglfcofuwdgexogk\nzratysbokjckbmlhppnrnjeujpcxlvsqefkuwzoehzgaskunlsvhdnrj\nxwybgdsssuthyhkahmgxxctgrqhwkdbnykvjryzoasrodrspjgqerjss\navwxrmgzbidxdfqavgqbtabsajrwabglrhjgabqpswtwohinyxygwhif\ntxcjzdoiclymgztijkfixbpuhxbvjwndrmgpjjmteueyfktyjhldzruc\nhhflcbkvhwnerkqqyeijnxxmrejhmzdqxoyatsbcjqykpffcphitkkzk\neszzyzdbgqhmmjpdlplyrxgwdaqnkbautfxyismlylvfycnhuhwtffkm\nhbpvinkhvkjmazaoftdbkbhykjepekygpzieynsqdjshflkukxgnnkxt\nxuygultsusobfgoyohjtsrpksxsblrysvdiegeoornuufiehcktinaas\nznewajuticnksrmpwwiqzbzkflhwgsykkicrdfdwipqxhcruyscprwmo\nvzkijvzzxlmhehvmhikexayxxsaucsjposklskfqwxnzbhpblkavxomi\njlxashuhnvzsptlbueilakdckfedrsrwlcfmfqsxvtptcjtunpndixqg\ncqdpwbnbzslbprblqyemsmxkniwsydabzzhyvxnicmbnzjmbxwjaefrq\nkljadyrlnysxnlsjzxirhgqrxnbomoxmfnruyolhfyqkdkzwmuqgfkel\nrpcatorlkkkceossfkpthuznxruzyflckiqyymlqddmlgkwtsiwelixb\nsnnmebmocquqkjyroenzwrztmhhlvgygakhlhlxqjarsxzmbvgvkvndb\nxzomwqlhoabhzbdzdwuhxsomosicnofvnewpjqtwgsfhtoaftapunfow",
        ]
        if isinstance(user_lst, list):
            result = check_all(user_lst)
        self.assertListEqual(result, ["YES", "NO", "NO", "NO"])

    def test_list_20(self):
        user_lst = [
            "5\nqwfqi\nudpzy\nklavb\nvuude\nxmsml",
            "1\nl",
            "7\ncfjpwhl\ncnuasqo\nooujxtv\nzrtvzmk\nivaqtjs\nedjlstv\nqjhxetp",
            "7\ncltkfbb\nzbkkqlc\nisfvlfd\nvfjciog\nqowuhxg\niplniiu\nogpkflh",
            "1\nd",
            "5\ndwboz\nwkffs\nuepoo\nktfcv\nzowgx",
            "4\nwbdr\nqein\nncqv\nczyr",
            "1\nm",
            "6\nudlawi\nejmoct\nhyediy\nuilyqx\nhmmmxx\nzkovtd",
            "5\nhbiir\nhxenf\nareag\nnsttm\niiljq",
            "4\nvuwi\nvxqn\nlepv\nxexz",
            "1\na",
            "3\nvpg\nunn\neye",
            "2\nqs\nse",
            "4\nvner\nuhmz\nmxkr\ndqaf",
            "1\nu",
            "2\nzc\nem",
            "2\nxg\nff",
            "3\ntbz\nwml\nlju",
            "4\nsywv\nqmxa\nxrdd\nnlkn",
        ]
        if isinstance(user_lst, list):
            result = check_all(user_lst)
        self.assertListEqual(
            result,
            [
                "NO",
                "YES",
                "NO",
                "NO",
                "YES",
                "NO",
                "NO",
                "YES",
                "NO",
                "NO",
                "NO",
                "YES",
                "NO",
                "NO",
                "NO",
                "YES",
                "NO",
                "NO",
                "NO",
                "NO",
            ],
        )

    def test_list_11(self):
        user_lst = [
            "4\noxsx\nplks\nhnhb\nhhed",
            "6\nzgnhsd\nwlzcxf\nzxtsuq\nrggqwn\nargstk\nkfxbpi",
            "6\nrhclha\nwraely\noyzekc\noxbnef\ndbwqfz\noidqtj",
            "1\np",
            "5\ngwrsa\nyxqsa\nxikao\niqwsh\nowobz",
            "9\nqkwidnvop\npzpmkldme\nrqgaafvko\nfiqnigktu\ndpxzumnxd\nbbaijdenb\nefdzocaum\npsvpgtrnd\nldbrkogcb",
            "2\nfz\nvc",
            "1\nk",
            "2\ngg\ntg",
            "9\npbfredpbm\nlpfsiezcq\nwsajntdpa\nxmrxdddjw\nmyuakowhx\njzvjhdtuj\nhquuwybau\njatttfere\npxhpqqgtc",
            "8\nencfcmrz\nsigafdsy\nmmmrmuzz\nyqhqdaar\nmsnkiaib\nmpbtxvrz\nskltvfjx\ndoidnzze",
        ]
        if isinstance(user_lst, list):
            result = check_all(user_lst)
        self.assertListEqual(
            result,
            ["NO", "NO", "NO", "YES", "NO", "NO", "NO", "YES", "YES", "NO", "NO"],
        )

    def test_list_6_2(self):
        user_lst = [
            "2\nyh\nin",
            "8\nnkgfqnvq\nsprlkapv\nvekpqlxv\nvzjctvqu\nqztfnwqf\necgldehf\nvdbkstuw\niqvcebif",
            "9\ntadohyvno\nfpnmvqkwa\nkdaqlskrz\ntvsqrnpqf\nazmwreljo\nclvtrkaig\nkdfjlebgg\nselshizgp\nkyhzeztux",
            "3\nvyy\njea\nlmj",
            "1\nw",
            "3\nawx\nzus\ndfe",
        ]
        if isinstance(user_lst, list):
            result = check_all(user_lst)
        self.assertListEqual(result, ["NO", "NO", "NO", "NO", "YES", "NO"])

    def test_list_2_2(self):
        user_lst = [
            "4\nuttc\ngcbr\nqaib\nauvk",
            "9\npjcxnszin\nijncqqabu\nbihunrugp\ncuazuxlpi\nnxemmwfzk\njoltruave\nhlahykxpo\niydznearf\npbdstkzir",
        ]
        if isinstance(user_lst, list):
            result = check_all(user_lst)
        self.assertListEqual(result, ["NO", "NO"])

    def test_list_3_3(self):
        user_lst = ["2\nyv\nvm", "3\nhsa\nkma\nyto", "2\nts\nun"]
        if isinstance(user_lst, list):
            result = check_all(user_lst)
        self.assertListEqual(result, ["NO", "NO", "NO"])

    def test_list_100(self):
        user_lst = [
            "4\nkova\naxcw\nhtql\nucde",
            "9\nuwqbphqat\nxyjvxuqxw\niulczyeoc\nesosxlwqu\nkqlkgpudc\npepmdzdgc\npnckqsvak\naiojsvadj\nprilnnuiv",
            "6\nwkhriw\ndtyjdn\nqzoxxg\nkeeerl\nufkdud\nxqetac",
            "5\nvnfmy\ntggin\nklixw\nlzjvd\nseuro",
            "5\njfixn\neijds\nmscha\nbnjej\nczylw",
            "5\nnmvgk\ncnwqg\ndgalz\nnewrk\newdle",
            "8\nsbtlsvgs\ntfvxaqsg\ndwhopgnp\nfydkwpvu\nknmqdpsx\nxielxkpt\nnwimpezy\nrwkyjssl",
            "4\nshbe\nlufm\ncprj\nohtx",
            "10\nzukczmvxmc\nnehcgteokd\nvazyqzhlzt\njjrksojjck\ngmhndnjobd\ntiqwyjeuea\ndzjntfplxg\ndisavylebi\nrroafudrhp\npvilzqlyyx",
            "2\nrv\nbf",
            "5\nfxxmh\nnyhin\nnsbsh\nrqhdi\nczahp",
            "2\nvk\nmr",
            "7\nepzycmj\nptvhyit\npzvqpqo\nwujidvb\nfhmqvjg\nvntqhel\nswihgft",
            "6\nlzkpkd\nejetqr\ndicukr\ntvrbou\nwwvdyr\nsmcrwi",
            "5\newksk\nqxtbc\nenoeo\nueqci\nicpug",
            "11\nybufbcspfay\ntgbxvvuzwjl\ngutxmxtbacp\njjylczsuijx\nxeilyksxfcx\ntmhtwhooeik\ntuhsynzzqjv\ndxkreyxkbdx\naunfjgnyyoi\ncmsermzztoq\nfwamuetmpun",
            "2\nvb\nlt",
            "7\nsaofrtz\nftmtjoe\nxexvrxm\nmpznibf\ndnmzkld\nifdimgp\nnnulrwi",
            "4\npijg\njqsb\ngcbc\nsiqm",
            "5\nqhfsu\nxfhsj\nmwoey\nptcka\ncunyb",
            "6\nzjzzue\njzlmqj\nobbgpb\ntgafjp\niedecc\nuamlll",
            "4\nvbca\nhsxq\nmcmt\nqtzs",
            "5\nqcfrw\neycxq\nrcrgw\nmfxqp\nwmqls",
            "1\nj",
            "2\nkb\nfb",
            "3\nzxp\ntbt\nmek",
            "7\nqpjoogd\nhlweahu\nxtxhtke\njolbpia\nuttkjta\nufvwmtc\ngyipdyi",
            "4\nmpte\nukvj\nxohz\nbmhs",
            "3\npna\nvxi\nsls",
            "5\nwkizi\nydxis\ndjsfc\nkdtsh\nfymoz",
            "7\nhaymsyf\nuuealel\nriawcse\nxtlrbrx\ndyxtpdr\nrtzkxjm\nkymnwbn",
            "6\nelnltf\ndjicqy\njgnegg\nhkvftn\nmcxotr\nlvsmol",
            "1\nf",
            "3\nmsq\ngmo\nfbd",
            "2\njl\nvq",
            "4\nacbw\npeav\njjcf\npdqo",
            "4\nskan\nznxu\nchms\nlzko",
            "6\ngxijho\nbrbbme\nlrhpvn\nnrhzoz\nwjrtot\naseewj",
            "1\ng",
            "6\nzwreub\nwdhoth\nqnwrax\nhnkvrh\nufvefn\nsxbsqm",
            "4\naofd\nkqnf\nhjyh\nxqyt",
            "7\ncgyxehi\nvomftxm\npboaknz\nkvctznq\npuerebv\nhixnqwa\nxflbhpt",
            "4\natui\nwyji\ncqtc\nwinc",
            "2\nvb\nez",
            "6\nqzmeuy\nisgans\npgsexi\ntjdliy\nkvepis\nlogfsf",
            "5\nugcev\nayhlo\naaznq\nyawbq\nzepsi",
            "6\nvykatj\ngvqkbq\npjtpwc\nibnpsg\npbnvue\nzshgvz",
            "3\neol\npeg\ndwa",
            "6\niecxrb\nhbpjjy\nmzntqm\ncprxbv\nrwkqqe\nvopwvo",
            "8\nuhqudsax\notldvyqm\nkkzoarqu\nabmkcnwu\nxrbuozqs\npvhgtyzh\ndllgpegu\nfeddhzps",
            "4\nqaoj\nkbce\nybzs\nlpwp",
            "8\nmxfvvtkc\nmkypxsdj\ngubtgzsf\nzsfmaupn\nxrddruns\nuiayigrp\npuosaepk\nnupdfcxi",
            "9\nhizlbuxgy\niqeyyxnkt\nvoigrxhwh\nyvmnywuec\nocwvzrusl\nsedkbijyj\nayoiznhue\ncbvwbtrpm\ndtxgasdlw",
            "4\nutgc\nfqio\nlzgw\nicwo",
            "1\ns",
            "2\nam\nkj",
            "3\ntam\nymn\ngsr",
            "4\nhvvr\nzqeu\npolt\noqsd",
            "6\nlleugn\nzfdzhr\ninkuxm\nnkcjam\nohcvix\ntqoekc",
            "3\nrzp\nzix\nzmc",
            "5\npjyzo\nvsjrt\nnbrwj\nowgxz\naxwwv",
            "2\ngr\nmu",
            "6\nwdlwxu\nouynqn\nwdctxa\nboucdw\nwdvvzb\npcydbs",
            "3\nqii\ngnp\nhpg",
            "2\nvk\nwh",
            "1\ne",
            "4\noydk\nqsca\nrhra\nliku",
            "5\ntbtqh\niudzb\nntwmi\nreeyz\nbyjqz",
            "7\niflaeyf\nadmstze\njcjekyb\nggnytuf\nahpaumt\nexbmilu\nplhqeuk",
            "6\nrteont\nlxrmbg\nagssqb\nufbdhg\nlzgbjb\nahhcph",
            "4\nlfhw\nkbev\nfxar\njssi",
            "5\nztuef\nfttdg\ntstse\ncrbfu\nedfuz",
            "4\njvmy\nwtsb\ncqfl\nuqdj",
            "1\nb",
            "3\ngbu\nbmk\nblr",
            "1\no",
            "5\nzybfj\norkyv\npnowt\nithks\nfbgwh",
            "7\nhxxgdll\nliefrjh\nrpxhiha\nqlsirto\nqqhdhhi\nmqkkwrk\nkltlpml",
            "8\naxrslqpo\njvvzyxdg\niczrczcq\nshxmyxqi\nxvtswrad\njzqtbtna\ndtdhkrqo\napmrlqlf",
            "3\nded\nomq\nneb",
            "3\naby\nnjt\nwji",
            "1\nn",
            "4\nuzek\ncwex\njnhs\nrsff",
            "2\ngn\nvy",
            "4\nfphc\nehfr\nljon\nmtlw",
            "1\nk",
            "2\nye\nzg",
            "5\nihjgc\ncptha\ntzgmd\neiqgv\nroixf",
            "3\ncvy\nvtv\nria",
            "3\neoa\ngwh\nbmc",
            "1\nq",
            "2\nah\ndc",
            "5\njcgwo\nwifqw\nurjil\nfwnoj\nyexow",
            "4\njjvs\ngpnd\ngupi\ncpcb",
            "1\nu",
            "7\njfcziwq\nvyuwayd\nuxoxkeb\nmnxwndq\ngmtejux\ntvjpejz\nnwylypi",
            "6\nhlmbgo\namjkvn\nfkydkt\nldatdn\nmzppdi\nzdfysb",
            "2\nms\npi",
            "2\nmi\nee",
            "4\nkwhi\nmnwe\nwdhx\nbahc",
        ]
        if isinstance(user_lst, list):
            result = check_all(user_lst)
        self.assertListEqual(
            result,
            [
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "YES",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "YES",
                "NO",
                "YES",
                "NO",
                "NO",
                "NO",
                "YES",
                "NO",
                "NO",
                "NO",
                "NO",
                "YES",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "YES",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "YES",
                "NO",
                "NO",
                "NO",
                "YES",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "YES",
                "NO",
                "YES",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
                "YES",
                "NO",
                "YES",
                "NO",
                "YES",
                "YES",
                "NO",
                "NO",
                "NO",
                "YES",
                "NO",
                "NO",
                "NO",
                "YES",
                "NO",
                "NO",
                "NO",
                "NO",
                "NO",
            ],
        )


if __name__ == "__main__":
    unittest.main()
