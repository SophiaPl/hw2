import unittest
from AmpliconFinder import pattern_creator, amplicon_finder


class TestPattern(unittest.TestCase):

    def setUp(self):
        self.F1, self.R1 = 'atwdgnaaab', 'arykmaattcc'
        self.F2, self.R2 = 'NNACBWYTDW', 'MBDRTGCCTAA'
        self.F3, self.R3 = 1, 1
        self.F4, self.R4 = 'A5T53CGRT', '46454'
        self.F5, self.R5 = '~~', '**'

    def test_PrimersFormat(self):
        self.assertRaises(TypeError, pattern_creator, self.F3, self.R3)
        self.assertRaises(TypeError, pattern_creator, self.F1, self.R3)
        self.assertRaises(TypeError, pattern_creator, self.F1)

    def test_CharCorrect(self):
        self.assertIsNone(pattern_creator(self.F4, self.R4))
        self.assertIsNone(pattern_creator(self.F5, self.R5))

    def test_PatternCreator(self):
        self.assertEqual(pattern_creator(self.F1, self.R1), 'AT[AT][AGT]G[ACGT]AAA[CGT].+GGAATT[TG][CA][GA][CT]T')
        self.assertEqual(pattern_creator(self.F2, self.R2),
                         '[ACGT][ACGT]AC[CGT][AT][CT]T[AGT][AT].+TTAGGCA[CT][TCA][GCA][TG]')

    def tearDown(self):
        pass


class TestFinder(unittest.TestCase):

    def setUp(self):
        self.filename1 = 'genome.fasta'
        self.filename2 = 'жмых.fa'
        self.filename3 = 'жмых2.fas'
        self.filename4 = 'genome.txt'
        self.filename5 = 9
        self.pattern1 = '[ACGT].+[ACGT]'
        self.pattern2 = 666

    def test_filename(self):
        self.assertRaises(TypeError, amplicon_finder, self.filename1)
        self.assertRaises(TypeError, amplicon_finder, self.pattern1)
        self.assertRaises(TypeError, amplicon_finder, self.filename1, self.pattern2)
        self.assertRaises(TypeError, amplicon_finder, self.filename5, self.pattern2)
        self.assertRaises(NameError, amplicon_finder, self.filename4, self.pattern1)

    def test_FileExistence(self):
        self.assertIsNone(amplicon_finder(self.filename2, self.pattern1))
        self.assertIsNone(amplicon_finder(self.filename3, self.pattern1))

    def test_AmpliconFinder(self):
        self.assertIsNotNone(amplicon_finder(self.filename1, self.pattern1))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
