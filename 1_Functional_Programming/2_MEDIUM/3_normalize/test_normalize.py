import unittest
from normalize import normalization_0_1_closed, normalization_0_1_open


class TestNormalize(unittest.TestCase):

    def test_if_returns_0_5(self):
        """
        Tests if returns 0.5 when max(list_) == min(list_).
        """
        data = [47]
        self.assertEqual(normalization_0_1_closed(data), 0.5)
        self.assertEqual(normalization_0_1_open(data), 0.5)

    def test_if_normalizes_closed(self):
        """
        Tests if function for range<0, 1> normalizes data in correct way.
        """
        data = [338, 69103, 4514, 26314, 29618, 34241, 16284, 42666, 93583, 44472, 80158, 95467, 51119, 65816, 80326, 74001, 85730, 73533, 66028, 63983, 16158, 66017, 89922, 56938, 12753, 3278, 7374, 62298, 29627, 82160, 63724, 49434, 6954, 89872, 76108, 4297, 26833, 35748, 71272, 20220, 42560, 61092, 20585, 39810, 43080, 73370, 8728, 4910, 29072, 89361, 42371, 39647, 18047, 68947, 14549, 91208, 65170, 2787, 92207, 40470, 27510, 11187, 85168, 81390, 69358, 48520, 1054, 23075, 50137, 94652, 9412, 13187, 49562, 48522, 64070, 1945, 37207, 49047, 54882, 64620, 10223, 26119, 82029, 75411, 96127, 48282, 91749, 44651, 71208, 1818, 39802, 86363, 1989, 85842, 30782, 95727, 20822, 30478, 15175, 88079, 50621, 95119, 66722, 14773, 67269, 76199, 67950, 84657, 46425, 19916, 80686, 94396, 33715, 31582, 76399, 49766, 51509, 78079, 43430, 12745, 44311, 3247, 74410, 28173, 7216, 17335, 90408, 30807, 51647, 61993, 22058, 98602, 10864, 50092, 64515, 54786, 93544, 47245, 55371, 98616, 38836, 20531, 91328, 26519, 47958, 66456, 58099, 69729, 67881, 14611, 41706, 54182, 83870, 97815, 59873, 56410, 19132, 98846, 18332, 76450, 92730, 15730, 14791, 22184, 95503, 75825, 75706, 36387, 29377, 26481, 31497, 16844, 53528, 49272, 6183, 62813, 62702, 63897, 37951, 92482, 74312, 24345, 54752, 16076, 75225, 18137, 49168, 79165, 35592, 80473, 10821, 4487, 14105, 29791, 54014, 89053, 55281, 89513, 70294, 76136, 75020, 69484, 18213, 22160, 32450, 4093, 46746, 53132, 42140, 35648, 33641, 68876, 2249, 27980, 85458, 17757, 13076, 11104, 5651, 40522, 51713, 17153, 42609, 40959, 70277, 51310, 39894, 66054, 38219, 80447, 93151, 79574, 21900, 35376, 76280, 14512, 92347, 2356, 13616, 88875, 79872, 94165, 16292, 18603, 77184, 83951, 38826, 43629, 40270, 15750, 78764, 13533, 40828, 83750, 7114, 12312, 52161, 96553, 82306, 6678, 16410, 14992, 82077, 35904, 80018, 13203, 43212, 60800, 11134, 4085, 55828, 17774, 8432, 93511, 3785,
                60313, 42622, 92803, 84261, 59123, 54056, 47725, 82187, 30246, 59422, 61764, 17682, 49761, 65645, 83423, 78042, 44376, 93254, 47969, 83769, 19206, 57386, 1703, 22793, 69001, 56876, 74577, 74960, 78983, 25744, 34679, 87386, 99690, 46282, 6620, 99614, 30675, 97260, 6990, 65656, 59089, 62393, 54138, 33786, 63617, 31994, 85561, 23344, 36597, 50716, 42500, 61728, 89637, 14317, 90766, 38579, 10206, 39064, 28711, 74820, 65044, 5395, 30591, 82744, 44280, 16093, 51487, 35528, 21768, 29889, 35939, 50066, 35623, 55152, 1555, 35611, 67736, 21028, 93811, 88188, 21783, 43479, 69641, 48691, 43279, 28346, 19218, 8507, 52534, 80253, 44060, 92937, 28923, 55238, 40164, 12397, 38893, 40729, 31483, 95053, 52373, 68982, 24534, 59155, 61323, 67142, 79710, 23187, 46632, 88802, 12750, 87765, 53870, 48282, 21817, 29621, 700, 36137, 6342, 29894, 65767, 65137, 51077, 13321, 11682]
        result_data = [0.0, 0.0036436105966663984, 0.007206699412190998, 0.012249375956196152, 0.01373902890731943, 0.014896529511232789, 0.016174812786858846, 0.01661768258313874, 0.019234640470247203, 0.02031161929301876, 0.024649730252033174, 0.02927973266768661, 0.02959175456961108, 0.034694822449472584, 0.037714389242290036, 0.03779491102343184, 0.03984821644254771, 0.04176060874466543, 0.042032369756019004, 0.04601819792253805, 0.050899830904259605,
                       0.05347652790079717, 0.058831226346726787, 0.060431596746920044, 0.06322972864159755, 0.0638135115548756, 0.06659151300426766, 0.06695386101940574, 0.06820194862710363, 0.06922860133666156, 0.07081890651421209, 0.08146791207021499, 0.08222280376841935, 0.08444721797246155, 0.09133183026008536, 0.09932361703840889, 0.09949472582333521, 0.10551372896368467, 0.10594653353732185, 0.1083621869715758, 0.10866414365085755, 0.10919760045092197, 0.11417988565907078, 0.12052097592398744, 0.12137651984861905, 0.1248792173282873, 0.12492954344150092, 0.1249597391094291, 0.12821080602302923, 0.1293280457363717, 0.1294890892986553, 0.1306767855704968, 0.13281061277075448, 0.13364602625010066, 0.1385679201223931, 0.14070174732265078, 0.14266446573798214, 0.14303687897576295, 0.14366092277961187, 0.14529148884773332, 0.14547266285530236, 0.14749577260649005, 0.1493377083501087, 0.154923906916821, 0.1551252113696755, 0.1584064739512038, 0.15857758273613012, 0.15923182220790724, 0.16050004026089057, 0.16058056204203236, 0.1617682583138739, 0.1661365649408165, 0.16924671873741848, 0.1710785892583944, 0.17457122151541993, 0.1753261132136243, 0.1754972219985506, 0.1782450277800145, 0.17915089781785973, 0.17991585473870683, 0.18111361623319108, 0.1838412915693695, 0.18916579434737096, 0.1899106208229326, 0.1900314034946453, 0.19705692889926726, 0.2001167565826556, 0.20324704082454303, 0.20379056284725017, 0.20617602061357598, 0.2082494564779773, 0.21569772123359368, 0.21584869957323455, 0.21619091714308722, 0.21702633062243337, 0.2186166357999839, 0.21964328850954182, 0.21988485385296722, 0.22601457444238668, 0.22885296722763507, 0.22998027216362027, 0.23156051211852807, 0.24163579998389564, 0.24353812706337064, 0.25571704646106774, 0.25949150495208956, 0.2614542233674209, 0.26313511554875596, 0.26351759400917946, 0.26667807391899506, 0.2734922296481198, 0.2782228842902005, 0.2801654722602464, 0.2819067557774378, 0.28558056204203236, 0.28771438924229004, 0.289214107416056, 0.2922840003220871, 0.2947097189789838, 0.294739914646912, 0.29480030598276835, 0.29645100249617523, 0.29743739431516225, 0.2974877204283759, 0.301030678798615, 0.30336581045172717, 0.3045031806103551, 0.305348659312344, 0.30642563813511553, 0.30667726870118367, 0.3134813592076657, 0.31362227232466383, 0.31447781624929544, 0.31862468797809806, 0.32321442950318063, 0.33520210967066594, 0.33594693614622756, 0.336661566953861, 0.34124124325630084, 0.3456498107738143, 0.35266527095579353, 0.35419518479748774, 0.3548393590466221, 0.35503059827683386, 0.3551513809485466, 0.35540301151461473, 0.3564095337788872, 0.35797970851115224, 0.3583319913036476, 0.36032490538690715, 0.3628412110475884, 0.36495490780256057, 0.3710946936146228, 0.37858321926081007, 0.3812806989290603, 0.3849041790804413, 0.3873902890731943, 0.3874909412996215, 0.3880646589902569, 0.38978581206216284, 0.3956538368628714, 0.39721394637249374, 0.39729446815363556, 0.3981399468556244, 0.40085755696916014, 0.401924470569289, 0.403937515097834, 0.40446090667525564, 0.4065444077622997, 0.4075408648039295,
                       0.4088594089701264, 0.41637813028424187, 0.42074643691118446, 0.42307150334165394, 0.42436991706256544, 0.4249738304211289, 0.42546702633062244, 0.42559787422497786, 0.42604074402125774, 0.43020774619534585, 0.4315363555841855, 0.43221072550124806, 0.43373057412029953, 0.43422377002979307, 0.4357335534262018, 0.4400716643852162, 0.44228601336661566, 0.44259803526854014, 0.44325227474031725, 0.44421853611401885, 0.44602021096706657, 0.46243658909735086, 0.4638759159352605, 0.46595941702230453, 0.4671068524035752, 0.47212939850229485, 0.4769607053708028, 0.47930590224655767, 0.47941661969562765, 0.4825670343828006, 0.4825670343828006, 0.4849625573717691, 0.4849826878170545, 0.48668371044367503, 0.49026692970448504, 0.4914848216442548, 0.49253160479909813, 0.4941621708672196, 0.49545051936548834, 0.4974534986713906, 0.49750382478460425, 0.5005233915774217, 0.5007850873661326, 0.5012380223850551, 0.506109590144134, 0.5070657862951928, 0.5106993316692165, 0.511122071020211, 0.5130445285449714, 0.5148260729527337, 0.5150475078508736, 0.5164365085755697, 0.5171008132699896, 0.5216100330139303, 0.523743860214188, 0.5253643610596667, 0.5313833642000161, 0.5353691923665351, 0.538811498510347, 0.5402608905708994, 0.5406836299218939, 0.5415089781785973, 0.5419518479748772, 0.5476890248812304, 0.548031242451083, 0.5489975038247846, 0.5517151139383203, 0.5525807230855947, 0.5530135276592318, 0.5539193976970771, 0.5585192044448023, 0.5643771640228682, 0.569067557774378, 0.569691601578227, 0.5742008213221677, 0.5813773250664305, 0.5913418954827281, 0.5916841130525807, 0.5920062001771479, 0.5946936146227555, 0.5992330300346244, 0.6036617279974233, 0.6085634914244303, 0.611502536436106, 0.6138276028665755, 0.617904018036879, 0.6182663660520171, 0.620571302037201, 0.6236411949432321, 0.624597391094291, 0.627707544890893, 0.6288247846042354, 0.6369172236089863, 0.6379942024317578, 0.6397354859489492, 0.6406010950962235, 0.6414767694661406, 0.6459557935421532, 0.6470126419196393, 0.6512802963201546, 0.652216362025928, 0.652548514373138, 0.6573294951284322, 0.6574402125775022, 0.6585574522908447, 0.6590506482003382, 0.6610737579515259, 0.6611844754005959, 0.6614461711893067, 0.6654923906916821, 0.6681697399146469, 0.6723971334245914, 0.6736754167002174, 0.67837587567437, 0.679835332957565, 0.680529833319913, 0.6898502294870763, 0.6905648602947098, 0.6909171430872051, 0.6911083823174169, 0.6921350350269748, 0.6947016668008696, 0.6959698848538529, 0.6975501248087608, 0.6984358644013205, 0.7039516064095338, 0.7041227151944601, 0.7133223286899106, 0.7139665029390451, 0.7350833400434817, 0.7367239713342459,
                       0.7414344955310411, 0.7445647797729286, 0.7455511715919156, 0.7472320637732507, 0.7496779128754328, 0.7510870440454143, 0.7516909574039777, 0.7537543280457364, 0.7556264594572832, 0.758595700136887, 0.7597934616313713, 0.7626419196392624, 0.7629237458732587, 0.7635578548997504, 0.7643731379338111, 0.7655708994282954, 0.7660842257830743, 0.7734720992028343, 0.7821080602302923, 0.7824804734680731, 0.7893751509783397, 0.7915794347370964, 0.7934113052580724, 0.7975279813189468, 0.7988968515983573, 0.8005274176664788, 0.8019969401723166, 0.8034060713422981, 0.8043622674933569, 0.8050970287462759, 0.8063149206860456, 0.8065766164747564, 0.8087205088976568, 0.8158064256381351, 0.8222381029068363, 0.8227212335936871, 0.8235566470730332, 0.8238284080843868, 0.8250261695788711, 0.8294347370963846, 0.8362690232707948, 0.8395603510749657, 0.8397515903051775, 0.8407681777920928, 0.8415834608261534, 0.8447036798453982, 0.8486895080119172, 0.8538328367823497, 0.8567517513487398, 0.8577884692809405, 0.859489491907561, 0.8606167968435462, 0.8658607778404058, 0.8761575006039134, 0.8799722199855061, 0.8831326998953217, 0.8842298091633787, 0.8904098558660117, 0.8911446171189307, 0.8929362267493357, 0.896036315323295, 0.8975662291649892, 0.898814316772687, 0.9011796440937273, 0.9016829052258636, 0.9065746034302279, 0.9101779531363233, 0.9146267815444078, 0.9158346082615347, 0.9200720669941219, 0.9246819389644899, 0.9260910701344713, 0.9274498751912392, 0.929946050406635, 0.930680811659554, 0.932029551493679, 0.9341835091392222, 0.9352202270714228, 0.9378069892906031, 0.938139141637813, 0.9385316853208793, 0.9408265560834206, 0.9443896448989452, 0.9467147113294146, 0.9492914083259522, 0.9533275626056849, 0.9539918673001047, 0.9574945647797729,
                       0.957856912794911, 0.9601115226668814, 0.9641376117239714, 0.9684253965697721, 0.9755415089781786, 0.9811277075448909, 0.9890490377647153, 0.9891899508817135, 0.9915049520895403, 0.9992350430791529, 1.0]
        self.assertEqual(normalization_0_1_closed(data), result_data)

    def test_if_normalizes_open(self):
        """
        Tests if function for range<0, 1) normalizes data in correct way.
        """
        data = [96324, 12420, 77089, 15933, 9423, 40390, 37898, 15733, 23759, 56747, 6863, 2136, 30441, 53403, 35928, 29199, 2227, 40677, 56798, 52690, 95702, 82369, 22829, 33205, 75709, 39799, 22806, 37644, 51236, 84323, 38496, 27851, 76852, 71483, 62274, 88402, 51192, 35557, 11803, 1648, 32821, 92129, 23089, 58237, 25680, 6664, 54006, 3298, 24716, 20543, 57582, 65766, 44099, 66970, 34793, 81093, 91504, 71460, 32638, 35543, 80369, 69148, 14799, 95923, 43996, 87782, 38094, 85046, 76349, 31535, 3051, 88295, 79527, 10331, 94662, 30760, 77874, 47644, 10467, 92174, 99369, 94415, 40847, 69750, 89347, 27692, 61089, 45145, 63900, 76013, 69955, 79011, 39972, 48494, 73544, 38050, 71624, 87138, 3894, 63445, 35200, 8210, 86431, 12891, 11319, 15835, 10955, 79929, 50360, 7609, 56256, 35330, 77746, 48072, 41805, 44121, 45477, 99582, 97821, 43472, 49101, 65444, 91549, 26378, 3651, 24652, 77843, 34124, 66461, 70123, 44449, 8875, 70761, 12952, 6151, 47451, 75735, 24383, 62402, 14630, 64478, 5980, 72907, 26255, 79215, 14277, 17520, 68691,
                85784, 54979, 72884, 84566, 40768, 42916, 24068, 44719, 50727, 2092, 98853, 90990, 49816, 33447, 75142, 16487, 87920, 12183, 23771, 37126, 51867,
                99507, 79088, 27990, 85754, 16620, 64839, 30034, 85306, 57216, 14241, 82395, 53960, 38486, 85664, 52918, 75698, 77291, 83794, 12631, 22789, 41888, 153, 93354, 40086, 31437, 99926, 82131, 59784, 588, 39927, 74874, 56840, 67169, 70776, 77013, 31987, 3452, 96757, 40391, 18279, 41614, 29912, 64516, 85282, 59138, 6793, 94058, 41278, 97949, 43653, 99444, 21943, 83709, 54638, 38953, 82429, 33541, 14279, 24641, 73568, 24210, 56858, 13260, 4207, 69387, 2068, 52045, 84667, 84636, 90557, 46695, 12186, 88379, 52652, 70610, 631, 33811, 88240, 10607, 20219, 44832, 87855, 74281, 98414, 88307, 89029, 34856, 84480, 86149, 44068, 93579, 22401, 16123, 23691, 30423, 22988, 70569, 48131, 68790, 32687, 8239, 53218, 11695, 20046, 92637, 11835, 48956, 42470, 38957, 61668, 25633, 82490, 35427, 66772, 17664, 60590, 85999, 78116, 9440, 73036, 61861, 75000, 13009, 77250, 30505, 12238, 66893, 92623, 36944, 54080, 22053, 304, 5061, 51650, 80181, 92156, 20616, 9431, 80431, 24280, 75024, 69675, 15146, 72493, 25576, 61317, 34084, 82090, 1676, 97293, 65285, 61060, 11837, 8638, 99384, 75231, 23486, 73541, 14938, 16031, 25621, 33106, 19662, 22944, 60503, 18275, 18145, 23642, 4804, 7001, 75738, 57212, 39295, 61307, 98223, 43701, 34608, 76677, 11131, 76846, 60645, 22692, 68719, 3954, 81269, 29378, 91484, 15417, 10224, 22147, 96268, 41984, 2944, 49506, 64276, 38578, 98154, 82040, 21951, 33679, 85920, 53252, 15888, 92669, 4248, 74521, 82357, 31316, 80845, 10924, 32459, 88707, 62313, 10355, 20186, 62011, 74816, 80004, 39706, 10604, 40731, 61433, 65333, 43969, 2952, 42261, 85415, 56966, 80475, 74837, 51421]
        result_data = [0.0, 0.0015134203299456772, 0.004359853268386554, 0.004790827269629362, 0.014983863531581374, 0.015264497764948785, 0.019193377032092528, 0.019433920660693167, 0.01987491731312767, 0.020786978571571753, 0.027973219476015797, 0.028053400685549342, 0.029045643153526972, 0.0315212379978752, 0.03306472628139596, 0.035059233868542906, 0.03749473810812436, 0.038096097179625955, 0.04063182793112434, 0.041042756629983766, 0.0466153506925652, 0.049191172048830355, 0.05840198849399643, 0.060115861847775974, 0.0652574819091146, 0.06655040391284303, 0.06725198949626156, 0.06863511536071522, 0.0747288872852647, 0.08075250065147233, 0.08104315753603143, 0.08504219536151703, 0.08741756369394832, 0.09290997654699622, 0.09299015775652976, 0.093080361617255, 0.10093812015154248, 0.10201054382905367, 0.1022510874576543, 0.10337362439112394, 0.10474672760438591, 0.10477679555796099, 0.10795397598572774, 0.10826467817267023, 0.11002866478240825, 0.11191292320644657, 0.11568144005452322, 0.11676388638322609, 0.11708461122136027, 0.11710465652374366, 0.12057249383606952, 0.1206025617896446, 0.12112373965161265, 0.12294786216850082, 0.1250626415699481, 0.12766853087978833, 0.12827991260248162, 0.12885120372040812, 0.13136688916952313, 0.14119910998857418, 0.14155992543147514, 0.14157997073385853, 0.14509792130214283, 0.146791749353539, 0.14818489786918435, 0.15026960931705655, 0.1529857477900054, 0.15615290556658049, 0.1571752159881332, 0.1577064165012929, 0.15815743580491912, 0.15913965562170507, 0.16006173953134084, 0.16370998456511718, 0.16504299717361237, 0.17406338324613627, 0.1755066450177401, 0.18032754024094452, 0.18163048489586464, 0.18167057550063143, 0.19553190209874316, 0.19938060015635337, 0.20078377132319042, 0.2011145188125163, 0.2043618577986249, 0.2050935113356185, 0.2183935694669954, 0.21847375067652897, 0.21949606109808167, 0.22043819031010084, 0.2229839437127909, 0.22590053520957365, 0.2268727323751679, 0.22704311744542666, 0.2272736384228356, 0.22842624330988032, 0.22886723996231484, 0.22987952773267584, 0.23385852025577805, 0.2354220538416822, 0.23591316375007518, 0.2365947040311103, 0.23671497584541062, 0.23969170324934352, 0.24111491971856394, 0.24181650530198248, 0.24284883837472687, 0.24543468238218374, 0.24554493154529236, 0.24618638122156072, 0.2548058612464169, 0.2552568805500431, 0.25537715236434344, 0.255848216970353, 0.2616112414055766, 0.26284402750215485, 0.27601379116803976, 0.277607392707519, 0.27900054122316437, 0.2911179265139215, 0.29291198107723454, 0.29826407681359873, 0.2994868402589853, 0.303385651572554, 0.30356605929400443, 0.3042075089702728, 0.30676328502415456, 0.31233587908673605, 0.3135486198809309, 0.31453083969771684, 0.3190610780363622, 0.32379176939884136, 0.32558582396215446, 0.3260769338705474, 0.32741996913023436, 0.3302764247198669, 0.33126866718784453, 0.33369414877623427, 0.33463627798825346, 0.3360194038527071, 0.33734239381001063, 0.3400785775853429, 0.3404794836330106, 0.34533044680979014, 0.3471846372802534, 0.34781606430533, 0.3512638563152725, 0.35256680097019266, 0.3535389981357869, 0.3547016256740233, 0.354841942790707, 0.3585603463828252, 0.3687433599935855, 0.37056748251047367, 0.3757592158277708, 0.37830496923046086, 0.3798284122115982, 0.3802694088640327, 0.38419828813117646, 0.3842985146430934, 0.38512037204081223, 0.3888788662376972, 0.38891895684246397, 0.39230661294525626, 0.3964259225850422, 0.39735802914586965, 0.3986409284984064, 0.3990919478020326, 0.4002345300378856, 0.4032814160001604, 0.40329143865135203, 0.40615791689217634, 0.40669914005652774, 0.4070699781506204, 0.40786176759476417, 0.41218153025838394, 0.41554914105879287, 0.4174634674364063, 0.4182953474853168, 0.4192575219997194, 0.4220337963798184, 0.42412853047888227, 0.4285986329103775, 0.4341712269729589, 0.4359853268386554, 0.4364664140958566, 0.43915248461523043, 0.43942309619740616, 0.44014472708320806, 0.4404554292701505, 0.4406759275963678, 0.44396335718724317, 0.44666947300900034, 0.4478020325936617, 0.4509391224166617, 0.4542666426123038, 0.46647423176378616, 0.4740513560647062, 0.47598572774470305, 0.48027542245474775, 0.48086675887505764, 0.4845049812576423, 0.48913544610820453, 0.49058873053100005, 0.4946479042636358, 0.4977549261330607, 0.5032072483813418, 0.5068855613686932, 0.5115460941728306, 0.5119870908252651, 0.5138412812957284, 0.5161364684186261, 0.5183113837272235, 0.5200954156393449, 0.5261791649127027, 0.5265600256579871, 0.5288451901296931, 0.531851985487201, 0.5321927556277186, 0.5337061759576643, 0.5392887926714375, 0.5397498346262554, 0.5404915108144407, 0.5460841501794055, 0.5495018742357728, 0.5623007998075651, 0.5672219215426865, 0.5677330767534629, 0.5681540281035139, 0.5683344358249645, 0.5694168821536673, 0.5718824543468238, 0.5719225449515906, 0.5755908352877503, 0.5821556718183094, 0.5911860805420249, 0.5976607132118588, 0.6048669994186863, 0.6057389700723635, 0.6062902158879067, 0.6104496161324594, 0.6107402730170185, 0.6129252109768076, 0.6130254374887245, 0.6141880650269609, 0.6165433880570088, 0.6184777597370056, 0.6199811574157597, 0.6226171146791749, 0.623007998075651, 0.6239000140317117, 0.6343536392246477, 0.6389139455168681, 0.6426824623649448, 0.6447070379056669, 0.6450878986509512, 0.648325214985868, 0.6527953174173632, 0.6532764046745645, 0.6543889189568425, 0.6576162126405677, 0.6645819552187945, 0.667698999739411, 0.6689117405336059,
                       0.6696834846753663, 0.6716779922625132, 0.6869324673762703, 0.6872131016096378, 0.687924709844248, 0.6915128189708741, 0.6939082326056889, 0.6967947561488965, 0.6975464549882735, 0.6996010984825706, 0.7012849038827751, 0.7057550063142702, 0.7061659350131296, 0.7076793553430754, 0.7078296951109507, 0.7146851885260689, 0.7149157095034778, 0.7163289033215066, 0.725038587207088, 0.7289574438230401, 0.729187964800449, 0.7304808868041774, 0.7355423256559825, 0.7355723936095576, 0.7358129372381582, 0.7429590875378355, 0.7453645238238419, 0.7483212059253914, 0.7485316816004169, 0.7489025196945096, 0.750165373744663, 0.7504059173732636, 0.7515885902138834, 0.752480606169944, 0.7571611842764648, 0.7572714334395735, 0.7575320223705575, 0.7575620903241326, 0.7603183194018481, 0.7636859302022571, 0.7669733597931325, 0.7686671878445286, 0.7687273237516788, 0.7703409705935415, 0.7711026920841101, 0.7727163389259727, 0.7731272676248321, 0.7776875739170526, 0.7786597710826468, 0.7789704732695892, 0.7813959548579791, 0.7903662276745445, 0.7911379718163049, 0.7924108485176499, 0.7955379156894582, 0.7995670214685189, 0.8003187203078959, 0.8020927295688255, 0.8039769879928639, 0.8045983923667489, 0.8050393890191834, 0.8087477699601099, 0.8112333874556498, 0.8129973740653877, 0.8207248381341833, 0.8212259706937679, 0.8216368993926273, 0.82390201856195, 0.8240222903762503, 0.8242828793072343, 0.8246236494477519, 0.8252350311704452, 0.8374526429731193, 0.8383045683244131, 0.8436065508048189, 0.8451801070419147, 0.8460420550444003, 0.8467436406278188, 0.8470543428147613, 0.8508529276164131, 0.8532182732976527, 0.8534588169262534, 0.8545512859061479, 0.8570469260528795, 0.8579489646601319, 0.8582496441958827, 0.859612724757953, 0.8604045142020967,
                       0.8619079118808507, 0.8647342995169082, 0.8718203139094354, 0.8782749012768858, 0.8790065548138793, 0.8796580271413394, 0.8828652755226812, 0.8834165213382243, 0.8835367931525248, 0.8842584240383267, 0.8844889450157356, 0.887545853629202, 0.8907731473129272, 0.8939603503918857, 0.9060877583338345, 0.9104275662998377, 0.9153787559885341, 0.915579209012368, 0.9160302283159941, 0.9218433660071762, 0.922113977589352, 0.9222943853108024, 0.9267945556958727, 0.9269348728125564, 0.9272555976506905, 0.9341211137170005, 0.9363762102351314, 0.9411770601559525, 0.9447551466313869, 0.9472307414757352, 0.9576542987150961, 0.9598693046284603, 0.9633271192895945, 0.9638883877563293, 0.9682281957223324, 0.97360033676108, 0.9788922965902941, 0.9801751959428308, 0.9822298394371279, 0.9829214023693548, 0.9848357287469681, 0.9892356726201215, 0.9944073606350352, 0.9945577004029106, 0.9951590594744122, 0.9957904864994889, 0.9965421853388658, 0.9999899773488083]
        self.assertEqual(normalization_0_1_open(data), result_data)
