import unittest
import pygame
from sprites.adjecent import Adjecent
from sprites.empty import Empty
from sprites.flag import Flag
from sprites.mine import Mine
from sprites.unrevealed import Unrevealed


class TestAdjecent(unittest.TestCase):
    def setUp(self) -> None:
        self.x_cor = 62
        self.y_cor = 93
        self.value = 5
        self.adjecent = Adjecent(self.x_cor, self.y_cor, self.value)

    def test_init(self):
        adjecent = self.adjecent
        self.assertEqual(adjecent.value, self.value)
        self.assertEqual(adjecent.rect.x, self.x_cor)
        self.assertEqual(adjecent.rect.y, self.y_cor)


class TestEmpty(unittest.TestCase):
    def setUp(self) -> None:
        self.x_cor = 62
        self.y_cor = 93
        self.empty = Empty(self.x_cor, self.y_cor)

    def test_init(self):
        empty = self.empty
        self.assertEqual(empty.rect.x, self.x_cor)
        self.assertEqual(empty.rect.y, self.y_cor)


class TestFlag(unittest.TestCase):
    def setUp(self) -> None:
        self.x_cor = 62
        self.y_cor = 93
        self.flag = Flag(self.x_cor, self.y_cor)

    def test_init(self):
        flag = self.flag
        self.assertEqual(flag.rect.x, self.x_cor)
        self.assertEqual(flag.rect.y, self.y_cor)


class TestMine(unittest.TestCase):
    def setUp(self) -> None:
        self.x_cor = 62
        self.y_cor = 93
        self.mine = Mine(self.x_cor, self.y_cor)

    def test_init(self):
        mine = self.mine
        self.assertEqual(mine.rect.x, self.x_cor)
        self.assertEqual(mine.rect.y, self.y_cor)


class TestUnrevealed(unittest.TestCase):
    def setUp(self) -> None:
        self.x_cor = 62
        self.y_cor = 93
        self.unrevealed = Unrevealed(self.x_cor, self.y_cor)

    def test_init(self):
        unrevealed = self.unrevealed
        self.assertEqual(unrevealed.rect.x, self.x_cor)
        self.assertEqual(unrevealed.rect.y, self.y_cor)
