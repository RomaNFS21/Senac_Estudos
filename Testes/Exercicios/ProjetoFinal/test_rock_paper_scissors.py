import random

from pytest import MonkeyPatch
from rock_paper_scissors import play, is_win

# Testes para a função is_win

# Testes para condições de vitória
def test_is_win_rock_beats_scissors():
    assert is_win('r', 's') == True  # Pedra vence tesoura

def test_is_win_scissors_beats_paper():
    assert is_win('s', 'p') == True  # Tesoura vence papel

def test_is_win_paper_beats_rock():
    assert is_win('p', 'r') == True  # Papel vence pedra

# Testes para condições de derrota
def test_is_win_rock_loses_to_paper():
    assert is_win('r', 'p') != True  # Pedra perde para papel

def test_is_win_scissors_loses_to_rock():
    assert is_win('s', 'r') != True  # Tesoura perde para pedra

def test_is_win_paper_loses_to_scissors():
    assert is_win('p', 's') != True  # Papel perde para tesoura

# Testes para a função play

# Teste de vitória
def test_play_win(monkeypatch: MonkeyPatch):
    monkeypatch.setattr('builtins.input', lambda _: 'r')  # Simula a entrada do usuário como 'r'
    monkeypatch.setattr(random, 'choice', lambda _: 's')  # Simula a escolha da máquina como 's'
    result = play()  # Chama a função play()
    assert result == 'You won!'  # Verifica se o resultado está correto

# Teste de derrota
def test_play_lose(monkeypatch: MonkeyPatch):
    monkeypatch.setattr('builtins.input', lambda _: 'r')  # Simula a entrada do usuário como 'r'
    monkeypatch.setattr(random, 'choice', lambda _: 'p')  # Simula a escolha da máquina como 'p'
    result = play()  # Chama a função play()
    assert result == 'You lost!'  # Verifica se o resultado está correto

# Teste de empate
def test_play_tie(monkeypatch: MonkeyPatch):
    monkeypatch.setattr('builtins.input', lambda _: 'r')  # Simula a entrada do usuário como 'r'
    monkeypatch.setattr(random, 'choice', lambda _: 'r')  # Simula a escolha da máquina como 'r'
    result = play()  # Chama a função play()
    assert result == "It's a tie"  # Verifica se o resultado está correto
