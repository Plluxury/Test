from number1 import prime_number
from number3 import roman_numerals_to_int
from number2 import text_stat


def test_number1():
    assert prime_number(2, 30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert prime_number(192913, 193000) == [192917, 192923, 192931, 192949, 192961, 192971, 192977, 192979, 192991]
    assert prime_number(-2, 30) == []
    assert prime_number(20, 3) == []


def test_number2():
    assert text_stat('../Files_for_number2/2file.txt') == {'paragraph_amount': 3, 'word_amount': 17, 'bilingual_word_amount': 1, 'l': (3, 0.17647058823529413), 'o': (4, 0.17647058823529413), 'r': (5, 0.29411764705882354), 'e': (9, 0.35294117647058826), 'm': (5, 0.23529411764705882), 'i': (10, 0.4117647058823529), 'p': (2, 0.11764705882352941), 's': (11, 0.5294117647058824), 'u': (5, 0.29411764705882354), 'd': (6, 0.29411764705882354), 't': (9, 0.4117647058823529), 'a': (8, 0.4117647058823529), 'c': (6, 0.29411764705882354), 'n': (6, 0.23529411764705882), 'g': (2, 0.11764705882352941), 'x': (1, 0.058823529411764705), 'v': (1, 0.058823529411764705), 'f': (5, 0.17647058823529413), 'ы': (2, 0.058823529411764705), 'ф': (2, 0.058823529411764705), 'в': (2, 0.058823529411764705)}
    assert text_stat('../Files_for_number2/1file.txt') == {'paragraph_amount': 3, 'word_amount': 229, 'bilingual_word_amount': 0, 'l': (84, 0.28820960698689957), 'o': (57, 0.2183406113537118), 'r': (78, 0.30131004366812225), 'e': (144, 0.4978165938864629), 'm': (63, 0.24890829694323144), 'i': (144, 0.5021834061135371), 'p': (27, 0.11790393013100436), 's': (119, 0.4104803493449782), 'u': (110, 0.4497816593886463), 'd': (44, 0.19213973799126638), 't': (93, 0.37554585152838427), 'a': (105, 0.39737991266375544), 'c': (57, 0.22707423580786026), 'n': (80, 0.3231441048034934), 'g': (14, 0.0611353711790393), 'b': (17, 0.07423580786026202), 'f': (8, 0.03056768558951965), 'q': (8, 0.034934497816593885), 'j': (3, 0.013100436681222707), 'h': (6, 0.026200873362445413), 'v': (17, 0.06986899563318777), 'x': (2, 0.008733624454148471)}
    assert text_stat('../Files_for_number2/file.txt') == {'error': FileNotFoundError(2, 'No such file or directory')}


def test_number3():
    assert roman_numerals_to_int("I") == 1
    assert roman_numerals_to_int("IX") == 9
    assert roman_numerals_to_int("XXX") == 30
    assert roman_numerals_to_int('MCDXI') == 1411
    assert roman_numerals_to_int('MCDXIX') == 1419
    assert roman_numerals_to_int(" ") is None
    assert roman_numerals_to_int("абв") is None
    assert roman_numerals_to_int("Iа") is None
    assert roman_numerals_to_int("Ix") is None
    assert roman_numerals_to_int("Ik") is None
