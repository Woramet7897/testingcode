import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from functions.two_charactes import alternate


class TestDataTestCases(unittest.TestCase):
    def test_give_10(self):
        l = 10
        s = "beabeefeab"
        result = alternate(s)
        self.assertEqual(result, 5)

    def test_give_1(self):
        l = 1
        s = "a"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_2(self):
        l = 2
        s = "ab"
        result = alternate(s)
        self.assertEqual(result, 2)

    def test_give_375(self):
        l = 375
        s = "uyetuppelecblwipdsqabzsvyfaezeqhpnalahnpkdbhzjglcuqfjnzpmbwprelbayyzovkhacgrglrdpmvaexkgertilnfooeazvulykxypsxicofnbyivkthovpjzhpohdhuebazlukfhaavfsssuupbyjqdxwwqlicbjirirspqhxomjdzswtsogugmbnslcalcfaxqmionsxdgpkotffycphsewyqvhqcwlufekxwoiudxjixchfqlavjwhaennkmfsdhigyeifnoskjbzgzggsmshdhzagpznkbahixqgrdnmlzogprctjggsujmqzqknvcuvdinesbwpirfasnvfjqceyrkknyvdritcfyowsgfrevzon"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_598(self):
        l = 598
        s = "ezfnjymgqtjnmstbadgdsrxvntnacwljnkgchtjeaoivfcindgxipmrjuqmmcpntpotplodjhijxqpogjmzipygacfdjgmewechuebxvcbnakszzcxkozxwavzgmesrvysonomhvufezislfntgncspthcpneyminpbjildobozfirvcgdratdpmmpkujcywvtzkdytzyfejbytsobvudvutfueveevgrqnxjiwpkrvllsjxmqhotlnpgjxkjnobxfqodlyiqsisdeuwqmntxouzdtisgutdafostmwticvncjwldpknuodmfksusaqpsoosgpiveyxipfklmhypdxpdncpgaswpycoxsuxasqduojpblctcyvyxldcgzevedvxiwinfppkjbtifuuapickknwxxjmjmtxlpfalxdgepmekaxijuphqfafrnezyldokwcnzenhpibktlfuxjfmeqajmvopbhuslnnnlmkmoteceiwbytjhhxqnkuazevswrkaofggfrnapciuoexqogscugzspwuvzkyrdfkhixcaqctfwadewpqksxxvqiigvjjpagvqikuojlwhfyztu"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_141(self):
        l = 141
        s = "cwomzxmuelmangtosqkgfdqvkzdnxerhravxndvomhbokqmvsfcaddgxgwtpgpqrmeoxvkkjunkbjeyteccpugbkvhljxsshpoymkryydtmfhaogepvbwmypeiqumcibjskmsrpllgbvc"
        result = alternate(s)
        self.assertEqual(result, 8)

    def test_give_293(self):
        l = 293
        s = "zxvtsuvazzqsohqvnhqwlcfsdobcggbaomhhvpbhfhstpbbxwwwripixzeqcngvuhalpgzuwonrbgvfpmctcnxarwvbwyoanslcixlmudpixelepyqlpusqgrndcgjumzqgyhpmtzngqkbxgajbmpbxdghmzlimmqfmplhmfpnnawabfvavchimulofnkhbyhkvchqvcniwnowamrsbzldyhekkkskwxrsgprihvsyyvsawqabsgvbbpwrgcrjulrjcdpkotxbkcijtykrqrqjxppanqdxdpewesq"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_42(self):
        l = 42
        s = "nkrtilugufndzwdoabujujdeglaihiutnfjqjoaohr"
        result = alternate(s)
        self.assertEqual(result, 5)

    def test_give_105(self):
        l = 105
        s = "cobmjdczpffbxputsaqrwnfcweuothoygvlzugazulgjdbdbarnlffzpogdprjxvtvbmxjujeubiofecvmjmxvofejdvovtjulhhfyadr"
        result = alternate(s)
        self.assertEqual(result, 8)

    def test_give_187(self):
        l = 187
        s = "tlymrvjcylhqifsqtyyzfaugtibkkghfhyzxqbsizkjguqlqwwetyofqihtpkmpdlgthfybfhhmjerjdkybwppwrdapirukcshkpngayrdruanjtziknnwxmsjpnuswllymhkmztsrcwwzmlbcoakswwffveobbvzinkhnmvwqhpfednhsuzmffaebi"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_28(self):
        l = 28
        s = "asdcbsdcagfsdbgdfanfghbsfdab"
        result = alternate(s)
        self.assertEqual(result, 8)

    def test_give_28_2(self):
        l = 28
        s = "asvkugfiugsalddlasguifgukvsa"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_96(self):
        l = 96
        s = "ptjrwralcwwyaagbrbuwbpdbtcdjpwceqglhpowwmyabhszsrzuqusodssiflgdziorajvzwgnxgfgpvfqmgipdbhycyotfp"
        result = alternate(s)
        self.assertEqual(result, 6)

    def test_give_339(self):
        l = 339
        s = "qdjsvcizyhhlajcsxbiidgrldsxcxrqahktxcomcmbsvxqfyjpvqnworvbofohmrghkjkbdoupsofuslwzgymejwsgokgqpsvgrxlqxpdgbskcsyyatxlzjmfpcoqdigrhmzbvumqzqrkevmjwnymgqnfeibqzhcmiyriarlqyyxojuitacmprrgrdorcccvgigtdbxartiqvjyobdhmbhbkixgyiiejfvprnhcgtoxflqekpyhfouogukupdpatelernxjiypqxvrlhjhxomuilreckkfvpbhbfgobqqlqkqmrsszdrnlyuetlnfdzkdzfjhhljvkkfpsilmqv"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_61(self):
        l = 61
        s = "fehxesdxgkpzyvbljfnahlywnyoqqcqccctzfzcfoljmfyrpyznyxclpmaraq"
        result = alternate(s)
        self.assertEqual(result, 7)

    def test_give_192(self):
        l = 192
        s = "oltlmlkohezjgtilgaoixbzylwtqgmxzpfiupyzmkwkseojushyktgpukeuksomwjezlzghnyniceggseojfdgdgmpweplyrlleypkbizpewlrgzrvpymysjcpyxbhzzntrukqigovujnxlzncjstpmzosnkslrvnkpqoscifyrfsyqusmvfmkapqpvprofk"
        result = alternate(s)
        self.assertEqual(result, 7)

    def test_give_266(self):
        l = 266
        s = "kxqmkqxfpetteodnbezrdsflhitpowogujzelglwjupilrnsrzhgztargjdgmyvbjbwudhvrwfgvoufbgmnuornrioeiftwxyfdlbezpwmvftwnhjmvuwpinxpbxizjpkjyhurvfbrqmjkhxwwgbizbjhkhnxenlesrdzdyexhlgtqtskyegalnffleibubggnnypqkwdaklctqwikgynqloyhfrptldisodpnkutdvrqjwhrhtwwbrawfnfqmrrmygqdsqhua"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_5(self):
        l = 5
        s = "fxbws"
        result = alternate(s)
        self.assertEqual(result, 2)

    def test_give_105_2(self):
        l = 105
        s = "qpcnrvicqrmvdipygvaqiwxzxgisyeemzgvcupiesuzbakdsbmucpbelhgvyplozqobwbapqmfvndfjomznpwzqzuiqsdsgdxoerfebvv"
        result = alternate(s)
        self.assertEqual(result, 6)

    def test_give_462(self):
        l = 462
        s = "ytbsmaxqjjreocwilusmdahfvcdejqkyksdbvkdgtecljeeaqyofqjbnivosaevggtrsbhuwpwznnclyuqiknlqtoajtcgplaihgkahjcwtytnaphudpykxzixrgdfdhmcbfsdoabtkidhxxtsvgrcoilndjmavqtdpysjeeyqrskzbdvbnxdtqkjkrfdtlxradzwwllfdgdrhziehnylkepzdosexmtuyfcjlglodqnbwvwiwswqyfrgvyhqstgqtcbxdvzaqgvszqtxdkipjjtgwbhjjrvngogdnayxdwkswrhmusthczeueabrmecvnikqloremnwwvoigouxjyenfivykpsdrsbluztvyqzehbwitmtohcxmzcpldecpdhnecjfhcwyoluxldzneemhznishtmqtsurtgclnktibnmzjzolchvkkqhjxpxvyewwoyubyicugzi"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_536(self):
        l = 536
        s = "pmnwyyxanoordwtunzyukrspjoqzlhsiflxsgdgmzvcjfhfvcdbezsqrcqirezwgkswvwdxhntwxvrekekqbhsakejpsphewcbpcydvmkdijyiusrhylhmxcclhydzpvasjxygppujkiobtefzbamwakwpihaftjgajqqouyinrdjucgpjfhlajggyyczlinndoogdgitfamtevivtokzrbojavjaobofowwwfohmtarfzikjcxpqthoxtlxfwvzzryudrtaxcfsrpwowjmberlfwpntkcjexfloeumxzastuyboxgynpbzizwxpxnyvgzfejneqsamafcqgcxvrypruyadttmvzmqjnzcvgqfgehzqerjwlszygqxncbyvvtkgabhoretmzrmxkglorrsmlcsneexjnzuiaapwqciugysglqxeoilbbsoawjyyvsuzpdyqjxjcysynhwqptpkdwxjlyrffkmdupxwadagocnfiyrqlrtizysnamthszpzovzrjnzhsmemtpugtesnyg"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_54(self):
        l = 54
        s = "qvkeymtjmeixhefdbuxrvtldoyfldsstwjggkxwjftccaedzdvnxmd"
        result = alternate(s)
        self.assertEqual(result, 7)

    def test_give_97(self):
        l = 97
        s = "zpetctfzhzqkrsbyalpzmqkwloeivrsoxqlhxhyhhndwgtfajyelzvalctnteyfofqclpaqvwggnwlqjqfprwdadypmtgjcmg"
        result = alternate(s)
        self.assertEqual(result, 7)

    def test_give_629(self):
        l = 629
        s = "rmgzuoqbhzfzdzeqgpkbulltktmaybktsfprtxxnnzjngiqbjvnswossqatururfuzobihgkzmhunqstoncojhuqoitrficpdrcantvabdqkzhoabrcptmogtxqfuceyjhtbarkotelcuioluhbzvfycpilmafjshtbtgjgqubwdrokecabnhsoykychaikyuhbcpmejhziigmfejwonfxznmimpiyyqcccsswltliwdzehdjydltqxwduzysqqtxskfmrcwgjvhfyuaymanxroannppbuhfgqhvjqxnxdqnomiqvmbqyezqcsxvfshcrjukvbcadjhseoghkdqxhfihxgdrbolksvbvpsipyrgavrucderyrjdnvmsumhzsvecvgilgdcnokujhvvqwclfouruswsrlejwxbtlsiywauewszdcugbytoidkgckivtpwkvmqbzegylyelafgyhxwsbwacyapkisgdflexhmhalgfqbarpoumavkezicwadelzxwxetvektjcqaeodkzpwfsghgdpycjjihavdayanzisfdyktmbvaunjpomgvgssrcufkqwpnagjippaxvxtqtcqarttlbpwjmfaepxtnisijvwsi"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_575(self):
        l = 575
        s = "hkbyaokbwdtmcmhnikydfpfeoaibbvyokauqwhtsvugymuniqhpmdlkurvlgcdizccnhxmvvwjfzrfblllypgpyqsfzbxjinarcupwcdfjshsbzqqlqpxaxnadgvjowgmgsvzntdczblkzxfbvpfipfuzqvhsakahfgraakuhzxozgxjyjxaqclrbwnoduonigvtpndfzurajsasaacxgalkfrqpbvoiqjqibcghsvfyvjbcpsxmkpwnbvymcvynwuatljtmtphygkytvxwqadnguhobnrnegzfdbmstayukrqsutyrlwijanvvwulqxvljvihmdkramtuixghgwvrzjfjnaquwjmtpbacdyrrjpmfqtedfuzgmuxeklgobmjjzulwhqjsumwjwehiulmxfdrlnwuishdgyeyldxfqymylqposyzouffjxwldabimmpzrtjrgmvhzbfdlyeizokmgdmngmkoeozzxjpcfndugpkthtjqjsatmncszrcdmqyykflltivttcxgzxqanizgzyppfzsbnyrajhbqkjiuymtngfkhhwkgftshhku"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_61_2(self):
        l = 61
        s = "yntwtbyahnzevhriejvxgguntlrcfmxfykajihevmvsxlqbicplkqkrjyusht"
        result = alternate(s)
        self.assertEqual(result, 7)

    def test_give_792(self):
        l = 792
        s = "jwcfrfafpxwwixgsdmasrwkoenwwrekqwjjquysuedzgjqhfbxwjctugtquxjbiqbevxstqwnvetxqsoaufjreqwfqnguuogyynzkjuzvyzoxjhholnpmauvfjqfmbrxydxekxzwqffwjnypmnebgdqewzznhbrfmubuyguswsiovdrounnquvwtfjchvkltacsspvufycdvwvzpffrbzkmydahyvxcrphlivilrppyrskcemezhscsllbceyjqabusyrvamxkuonupntxpmsgxwuxiljbzaczduuxsrsocuakqlbmzttdvtpousjgowisdcbgpzorbugynarowcwoceschscbxgwkedsdwchokalfxgiukouscbpnfamdtiwmdasczfhguwdywniryuahdvriajkdmqbbsqytiqjevnvwlsnecisxinkxlzacfircpfbgddrjcddmqbyhpiyuvezizvnjxtmylfzgjusxmqrgylgcqcdnhkreskonpwksyeglzprtdgiijuviwemgyjtkflkbpciwzuibtbhvlpghaodgjqqmrgmjmmmejvfqqidaadakyjjxwemjwceddbzskmjmczgrftxnjdvrizmhfbabmquowjcwlvvyupnylhdqybrglxirkvxjfufnrqfiemnanrzneleanbjadsdlvgzlehtuztbwyalgprutyspzysxceossnmwwjfnfmfqcueozdonnlutejuqucnrapneviecefuureieuvhcdnjuaxnufmhrwgetlmmiser"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_946(self):
        l = 946
        s = "cvdtdjvcukrpquqgbioouemkzodiswkerscvndcraxzmtzqovwpogrmwproxafbouknveccpjtxyeonyfmwsuwxildkqzjzzfhbvjgzehcxckaydihjziprqlyfxzminvauftppnekiftpskdcrgayvtfscvsgeitirjoihphjwrcuqarhapncytwwfbgkpowpskkanpmydeacsamfqjnpvrllzeonomfmsfmxojyyjswfqtdeihcatcjcpklewrstdlagebwuegnzlhhgepasccfeegczfrewiatbtbcibzwxvoqtvbthlrctsstnpfmoyxlgtyfjtlsfrkehuwepddmnitlsnqtlztodsbktbyotlfkqxedqphznhmpclfpfsznrppcmkfxxqnjrkhyqtyjcdonlfjiuirrznumwrgsfowgulsfhmggkadsccboeszkrnnubuzplkcyluiuuidimiopzwgjvflhbmjlmvrgyszscionxkplhiuwdastxbzpodjsmmdhyuokjfyyfswjypunjtigxzvunegvhetqsbbvpfwliqaxgdpbqdmgnnrsqftryfjzyfsxzvkdqkzexnukoqogsgszylezbbqajgeixmqmoxeqmnrzjertzvtulkyiqoqpvjpdtqsitrougqsomytvgphojioumfeaxckvmpoowxvlykhpiarmaugyanyncyrpeavngggrtubhyenbjsnjkimbzrqfqahswpngmppoqautcezademtxtukmrpwkfrmrtjjpfntotoawhgtburftisouvdxvzntvfpvfrrcfszkzuilievekpwraxyqtgncszcxhryyuptnhhzzbueyywwszmoxsnxoqmmindeaskhbysctswcklsvkgurtdwshouruhtoxnotdqjmmhrybeznduouxhjaxzmohb"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_46(self):
        l = 46
        s = "fhnlztnpoowpsvsqbngskqeulqceizhtyqdojotlphgffw"
        result = alternate(s)
        self.assertEqual(result, 5)

    def test_give_774(self):
        l = 774
        s = "ivveaocwebxdshrrqzlqarxhueqjrajzjeiztzlsfxqekezqczfsamknncuqxiyalmfpkldogiofmhhxrrwitfxcsqkeoirmrwfahirxuiexibztbkzwrobsbidojkkyapvrjxicigiuytoydweuangrwjjggxgreryceazptvqcjjednwozbyijlqyqtkcbngomkflzqbyvkxyaosmezxknyqgkumdygpohcwzfzywhvenfhlwcnppqptwclraocdpcwscdkuitsphibghpopwmcvwgapoovhihrojltvcjwfdgtnoddbkvordiqcurwtbjdcjbhczabzegkpecfqvkrlfsvedxrhitmawsglwnmurvtunajogvobhpbiyraynwtncliurcnvflixhmacnkdvrewnimmwqwgbqjxxwykaruswsphnafqdebnzgcnyqjbqorouatjgtunhyqqendzgnqwxljcajmhcrutckdxlsxucbtlaxygkinxtmlaqwxlphcrwpwiinsrdmwnnrcsaiifdgzctwjyyqjwomzdxgdqcdvlplyyximsoijuffzhaglfhnrhledgbercoetstgretsqoqdmemmfgqgouppuattsfsmexdykishkmbtrrxfklplavboqfmeajdlteniublanfgkccptvbwzrqmvzymlbbyccijcfxpgxnceqwpusxtsailvxjtuxdovssngspliylwtxwdzepuowwanlttacaasmsphvarczbnxtkj"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_26(self):
        l = 26
        s = "aozyqlitiqgpuhzlpvuplllykf"
        result = alternate(s)
        self.assertEqual(result, 5)

    def test_give_938(self):
        l = 938
        s = "wuldmaoojicyeaimijtbdgdgxrojalnkivdsyppvxmlkhlevigupcfzygbxpggingznvzlbwntvplkhrdpbbilgutsebolgkgkjmntorkcxqhatfplbozbhemryvvwnumsuntrxsqqssvlbqldbmdqwjclnynsypsnbykykqtqwmcpzhfcgdqcsqyydrahgvazozjfxtkpnayabcelzkttswvozxoabifmxnnqzhbbfublmfaozcxsloiaxtaobrvxymzllljzazmwrrxvcjqvsmnzwkyexertbajwsamvnmdrifjpnncykixbfpvvbtjqzjyubaeaiksxvivohkgsmpcjqbrdtclphrjwhaevnydpypxyageegiohhdofpebupcdqbsbwpflnczpdortgrxytkmlzzvifxipozpbguglvjyylgevnhfdjlkgjhjtsreoarvhsqnzbaytwilyhtptcpcjwpbaqudhrpqjblzasbvbxvjtvtzolhwzegiqfqagxudcavvnmhdralwpqcunguwtstfckfjejsvykljynbmkvrtgbrfbcrvpftmiegmctoeifofilndvoffzzkonxkxchveemdhmflygmxeiqmikhuzftayvzwbtjfmbcgiugkwouuxmhhypenhppbvrzavqtkryfmvaodpnofbnixzyjdbmjkxtqzmlzcizkrbvdygvknlwgebakcqznhauyjqhyfbffwdjoruuihdnchoizfbvucloyjxefmcalueqihkhkzlkxdolqamvlskkonpteujesctwoqvhgrscdquyzyhxtstvsgbwrltqrqonoswhedwxbvbywmfsahxxywtxyofithngmwyyrhgfelsrldbmgtgupttfdgpydentaehcjscppqqxfcscyqdopjlavhwdbnogoqqty"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_878(self):
        l = 878
        s = "vpyzbtfstpfjfgtxymwpbhgpvzwweqnddzlmdadkhpwtsojqjdolfgryyplypftthjhewvdzicfmmthbjqhphuzqubwajsupxifpypihktneiqoowtkbtidfsdqerticcrtlojolqbwcsruquuqobujanklvmhozpqhphuroksveaafxjndlvclkxeavekzolorgjiefahoqutaspmixjuagxvkoqqapzwpggrbxitsuwvedpxjpyjkwgnfdarwournpowfkgbchjudlwxhbzjhzrtpujfhzychxvcazuprwsqwbyhxhanpuykmavxcwokvbkabqcmklglvviuudkvdyyfesiowlwxrjssportlwbhwuyxjvpdogvyzxljzfldgmflcuzibpoxfkrojhjmxxoxzfefrbylvvwhgzbopewktsaryvwaplitibngrscjklqzmlvasihnvfldnxlhklvzowtmooiadfgycociizbqaifpezkhwgxeqmaxfgyjfqhmgcqrhijlvptobrduczlpevtocynhtyysxlobweowsvnfuwljcamqmznomsazcdhviuskiudygwiodaqymoxrrpmmrrogggcxrdzgvyzxkujcvxsyjtnogqxidiwcsypeyymskvdwivpzroijmdectspaonthwvqsemrfmqdcmotwlznbwmbyaohyvextijkjikswbiehbsfxzamqjlawyryxtxqhqewphfcmrqamlnkfwfovhabxhpxozggiasgwhuyichprwgodxnwbhkyftqnqkkvsljtmoxzopyzqgueqjooojxpzprwmbepptwtrveyxjitqoasskzdcphqjmwzskexqxtzkrdaldxqk"
        result = alternate(s)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
