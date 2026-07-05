"""Юнит-тесты для application.py."""

from application import ServerInfo


def test_take_four():
    """Проверяем, что метод take_four возвращает 4."""
    assert ServerInfo().take_four() == 4


def test_port():
    """Проверяем, что сервер настроен на порт 8000."""
    assert ServerInfo().port() == 8000
