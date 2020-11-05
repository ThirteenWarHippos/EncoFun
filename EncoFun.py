#add: quit button, try/catch pop-ups, dicitonary list, audtodict

import time
from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.clipboard import Clipboard
from kivy.config import Config

Config.set('graphics', 'fullscreen', 'auto')
open_sound = SoundLoader.load('Laugh.mp3')
open_sound.volume = 0.2
encode_sound = SoundLoader.load('Healing.mp3')
encode_sound.volume = 0.2
decode_sound = SoundLoader.load('Pointer.mp3')
decode_sound.volume = 0.2
quit_sound = SoundLoader.load('Run.mp3')
quit_sound.volume = 0.2
error_sound = SoundLoader.load('Li.mp3')
error_sound.volume = 0.2
copy_sound = SoundLoader.load('Save.mp3')
copy_sound.volume = 0.2
paste_sound = SoundLoader.load('SavePoint.mp3')
paste_sound.volume = 0.2

alphadict_q = {1: 'q', 2: 'w', 3: 'e', 4: 'r', 5: 't', 6: 'y', 7: 'u', 8: 'i', 9: 'o', 10: 'p',
                       11: 'a', 12: 's', 13: 'd', 14: 'f', 15: 'g', 16: 'h', 17: 'j', 18: 'k', 19: 'l', 20: 'z',
                       21: 'x', 22: 'c', 23: 'v', 24: 'b', 25: 'n', 26: 'm', 27: '1', 28: '2', 29: '3', 30: '4',
                       31: '5', 32: '6', 33: '7', 34: '8', 35: '9', 36: '0', 37: 'Q', 38: 'W', 39: 'E', 40: 'R',
                       41: 'T', 42: 'Y', 43: 'U', 44: 'I', 45: 'O', 46: 'P', 47: 'A', 48: 'S', 49: 'D', 50: 'F',
                       51: 'G', 52: 'H', 53: 'J', 54: 'K', 55: 'L', 56: 'Z', 57: 'X', 58: 'C', 59: 'V', 60: 'B',
                       61: 'N', 62: 'M', 63: '!', 64: '@', 65: '#', 66: '$', 67: '%', 68: '^', 69: '&', 70: '*',
                       71: '(', 72: ')', 73: '`', 74: '~', 75: '-', 76: '_', 77: '=', 78: '+', 79: ',', 80: '<',
                       81: '.', 82: '>', 83: '/', 84: '?', 85: ';', 86: "'", 87: '"', 88: '[', 89: '{', 90: ']',
                       91: '}', 92: ' ', 93: '|', 94: ':'}
numadict_q = {v: k for k, v in alphadict_q.items()}

alphadict_a = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
                       11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
                       21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: '+', 28: "'", 29: '"', 30: '`',
                       31: '~', 32: '[', 33: ']', 34: '{', 35: '}', 36: ';', 37: '|', 38: 'B', 39: 'C', 40: 'D',
                       41: 'E', 42: 'F', 43: 'G', 44: 'H', 45: 'I', 46: 'J', 47: 'K', 48: 'L', 49: 'M', 50: 'N',
                       51: 'O', 52: 'P', 53: 'Q', 54: 'R', 55: 'S', 56: 'T', 57: 'U', 58: 'V', 59: 'W', 60: 'X',
                       61: 'Y', 62: 'Z', 63: '!', 64: '@', 65: '#', 66: '$', 67: '%', 68: '^', 69: '&', 70: '*',
                       71: '(', 72: ')', 73: ' ', 74: ',', 75: '<', 76: '.', 77: '>', 78: '/', 79: '?', 80: '-',
                       81: '_', 82: '=', 83: '1', 84: '2', 85: '3', 86: '4', 87: '5', 88: '6', 89: '7', 90: '8',
                       91: '9', 92: '0', 93: ':', 94: 'A'}
numadict_a = {v: k for k, v in alphadict_a.items()}

alphadict_z = {1: 'Z', 2: 'z', 3: 'Y', 4: 'y', 5: 'X', 6: 'x', 7: 'W', 8: 'w', 9: 'V', 10: 'v',
                       11: 'U', 12: 'u', 13: 'T', 14: 't', 15: 'S', 16: 's', 17: 'R', 18: 'r', 19: 'Q', 20: 'q',
                       21: 'P', 22: 'p', 23: 'O', 24: 'o', 25: 'N', 26: 'n', 27: 'M', 28: 'm', 29: 'L', 30: 'l',
                       31: 'K', 32: 'k', 33: 'J', 34: 'j', 35: 'I', 36: 'i', 37: 'H', 38: 'h', 39: 'G', 40: 'g',
                       41: 'F', 42: 'f', 43: 'E', 44: 'e', 45: 'D', 46: 'd', 47: 'C', 48: 'c', 49: 'B', 50: 'b',
                       51: 'A', 52: 'a', 53: '0', 54: '9', 55: '8', 56: '7', 57: '6', 58: '5', 59: '4', 60: '3',
                       61: '2', 62: '1', 63: ')', 64: '(', 65: '*', 66: '&', 67: '^', 68: '%', 69: '$', 70: '#',
                       71: '@', 72: '!', 73: '~', 74: '`', 75: '+', 76: '=', 77: '_', 78: '-', 79: ':', 80: ';',
                       81: '"', 82: "'", 83: '<', 84: ',', 85: '>', 86: '.', 87: '?', 88: '/', 89: ' ', 90: '{',
                       91: '}', 92: '[', 93: ']', 94: '|'}
numadict_z = {v: k for k, v in alphadict_z.items()}

dictdict = {"a": (alphadict_a, numadict_a), "q": (alphadict_q, numadict_q), "z": (alphadict_z, numadict_z)}

class GameScreen(Widget):

    dictionary = ObjectProperty(None)
    key = ObjectProperty(None)
    input = ObjectProperty(None)
    output = ObjectProperty(None)

    def encrypt(self):

        coded_list = []
        e_list = []
        new_letters = []
        new_string = ""
        i = 1
        self.output.foreground_color = 1, 1, 1, 1

        try:
            for character in self.input.text:
                if character in dictdict.get(self.dictionary.text)[1]:
                    coded_list.append(dictdict.get(self.dictionary.text)[1][character])

            for number in coded_list:
                number += int(self.key.text) + i * i
                number = number % len(dictdict.get(self.dictionary.text)[1])
                if number == 0:
                    number = len(dictdict.get(self.dictionary.text)[1])
                e_list.append(number)
                i += 1

            for number in e_list:
                if number in alphadict_a:
                    new_letters.append(alphadict_a[number])
            for letter in new_letters:
                new_string += letter


            print(self.input.text)
            print(self.key.text)
            print(self.dictionary.text)
            print(new_string)

            self.output.text = new_string
            encode_sound.play()
            return new_string

        except Exception:
            self.output.foreground_color = 1, 0, 0, 1
            self.output.text = "* * * Error: FUCK YOU * * *"
            error_sound.play()

    def decrypt(self):

        coded_list = []
        e_list = []
        new_letters = []
        new_string = ""
        i = 1
        self.output.foreground_color = 1, 1, 1, 1

        try:
            for character in self.input.text:
                if character in numadict_a:
                    coded_list.append(numadict_a[character])

            for number in coded_list:
                number -= (int(self.key.text) + i * i)
                number = number % len(numadict_a)
                if number == 0:
                    number = len(numadict_a)
                e_list.append(number)
                i += 1

            for number in e_list:
                if number in dictdict.get(self.dictionary.text)[0]:
                    new_letters.append(dictdict.get(self.dictionary.text)[0][number])
            for letter in new_letters:
                new_string += letter


            print(self.input.text)
            print(self.key.text)
            print(self.dictionary.text)
            print(new_string)

            self.output.text = new_string
            decode_sound.play()
            return new_string

        except Exception:
            self.output.foreground_color = 1, 0, 0, 1
            self.output.text = "* * * Error: FUCK YOU * * *"
            error_sound.play()

    def play_quit(self):
        quit_sound.play()
        time.sleep(1)
        Exit()

    def copy_output(self):
        Clipboard.copy(self.output.text)
        copy_sound.play()

    def paste_input(self):
        self.input.text = Clipboard.paste()
        paste_sound.play()

class EncoFunApp(App):
    def build(self):
        time.sleep(0.2)
        open_sound.play()
        return GameScreen()


if __name__ == '__main__':
    EncoFunApp().run()