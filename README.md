# situ-devops-09 Лаб 9. Приложение и CI/CD-пайплайн

## Приложение

`server/application.py` — минимальный HTTP-сервер на стандартной библиотеке Python,
отдающий файлы текущей директории (в т.ч. `index.html`) и содержащий класс `ServerInfo`
с логикой, покрытой тестами.

## Юнит-тесты

`server/test_application.py` — тесты на `pytest`, проверяющие метод `take_four()`
и порт сервера.

## Докеризация

`server/dockerfile` собирает образ на базе `python:3.10-slim`, запускает приложение
от непривилегированного пользователя `runner`, открывает порт `8000`.

## CI: lint, unit-test, build-test

`.github/workflows/cicd.yml` запускается при push в ветку `dev` и содержит три job:

- **lint** — `pylint server/application.py`
- **unit-tests** — `pytest` с выгрузкой отчёта в JUnit-формате
- **build-test** — сборка docker-образа, запуск контейнера и проверка через `curl`
  (зависит от успешного прохождения `lint` и `unit-tests`)

## Kubernetes-манифест

`server-k8s-manifests/devops-course.yml` 

## CD: сборка и публикация образа в Docker Hub

https://hub.docker.com/r/sergeylobaev/devops-course

<img width="2388" height="1138" alt="image" src="https://github.com/user-attachments/assets/c870a1c0-e28e-4110-819c-338c41d50023" />
<img width="2372" height="1044" alt="image" src="https://github.com/user-attachments/assets/df4d6edf-1eab-42b9-8867-267cfc19c42f" />

