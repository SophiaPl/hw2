import unittest
from t5 import *


class TestReader(unittest.TestCase):

    def setUp(self):
        self.filename1 = 'genes.fasta'
        self.filename2 = 'genes.fa'
        self.filename3 = 'genes.txt'
        self.filename4 = 1
        self.filename5 = 'nonexistent.fas'
        self.filename6 = 'incorrect.fas'

    def test_FilenameFormat(self):
        self.assertRaises(TypeError, file_reader)
        self.assertRaises(TypeError, file_reader, self.filename4)
        self.assertRaises(TypeError, file_reader, self.filename3)
        self.assertRaises(FileNotFoundError, file_reader, self.filename5)

    def test_FileReader(self):
        self.assertIsNotNone(file_reader(self.filename1))
        self.assertIsNotNone(file_reader(self.filename2))
        self.assertIsNotNone(file_reader(self.filename6))

    def tearDown(self):
        pass


class TestFrames(unittest.TestCase):

    def setUp(self):
        self.seq1 = 'ATGCGARNATAG'
        self.seq2 = 'A56GF'

    def test_CharCorrect(self):
        self.assertIsNone(frames_creator(self.seq2))
        self.assertIsNotNone(frames_creator(self.seq1))

    def test_FramesCreator(self):
        self.assertEqual(frames_creator(self.seq1), (
            'ATGCGARNATAG', 'TGCGARNATAG', 'GCGARNATAG', 'CTATNYTCGCAT', 'TATNYTCGCAT', 'ATNYTCGCAT'))

    def tearDown(self):
        pass


class TestTranslation(unittest.TestCase):

    def setUp(self):
        self.orf1 = ['ATGCNRYWBCGVKHDS', 'CGTAVSRATGWCCC', 'ATGATGCTACTA']

    def test_OrfTranslate(self):
        self.assertEqual(orf_translate(self.orf1), ['MXXRX', 'RXBX', 'MMLL'])

    def tearDown(self):
        pass


class TestORFFinder(unittest.TestCase):

    def setUp(self):
        self.seq1 = 'ATGCGARNATAG'
        self.seq2 = 1

    def test_SeqFormat(self):
        self.assertRaises(TypeError, frames_creator)
        self.assertRaises(TypeError, frames_creator, self.seq2)
        self.assertIsNotNone(frames_creator(self.seq1))

    def test_ORFFinder(self):
        self.assertIsNotNone(orf_finder(self.seq1))

    def tearDown(self):
        pass


class TestORFtodict(unittest.TestCase):

    def setUp(self):
        self.orflist = ['SDGFASDGDAF', 'SHDFAGSFDSAFJH', 'SAHDFAHSDFAFDGKFYSDF', 'JGHGFFGDFST', 'EWEASDGDFH']

    def test_ORFdict(self):
        self.assertEqual(orfdict(self.orflist),
                         {'ORF1': 'SDGFASDGDAF', 'ORF2': 'SHDFAGSFDSAFJH', 'ORF3': 'SAHDFAHSDFAFDGKFYSDF',
                          'ORF4': 'JGHGFFGDFST', 'ORF5': 'EWEASDGDFH'})

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
