"""
/file test_newBuild.py

@brief Unittests for Automated template generator tool.

@author 03difoha

@date 2017

"""
import unittest
from template_generator import template_generator

title = 'Test Title'
Id = 1234567
version = '5'
foo = 'foo'
longVar = '1234567891234567890123' # 22 chars long
empty = ''
special='{*!'
emptyParams = {'autoplay': '',
               'muted': '',
               'timeStamp': '',
               'customSkin': '',
               'loop': ''
                }

params = {'autoplay': True,
          'muted': '',
          'timeStamp': True,
          'customSkin': '',
          'loop': True
          }

class TestNewBuild(unittest.TestCase):
    def test_TitleCorrect(self):
        self.assertEquals(template_generator.validateTitle(title=foo), foo)

    def test_TitleLengthIncorrect(self):
        self.assertEquals(template_generator.validateTitle(title=longVar), None)

    def test_TitleEmpty(self):
        self.assertEquals(template_generator.validateTitle(title=empty), None)

    def test_IdCorrect(self):
        self.assertEquals(template_generator.validateId(Id=Id), Id)

    def test_IdNotInt(self):
        self.assertEquals(template_generator.validateId(Id=foo), None)

    def test_validateIdLength(self):
        self.assertEquals(len(str(template_generator.validateId(Id=Id))), 7)

    def test_validateVersion(self):
        self.assertIn(template_generator.validateVersion(version), version)

    def test_validateVersionNegative(self):
        self.assertEquals(template_generator.validateVersion(version=special), None)

    def test_buildParametersEmpty(self):
        self.assertEquals(template_generator.paramStringConsructor(emptyParams), '')

    def testbuildParameters(self):
        self.assertEquals(template_generator.paramStringConsructor(params), '?timeStamp=True&loop=True&autoplay=True')

if __name__ == '__main__':
    unittest.main()
