# Домашки по курсу Advanced Python 2024 ИТМО

Автор: Утков Александр

Сборка контейнера:
```
docker build . --tag=advanced_python -f HW2/Dockerfile
```


Запуск контейнера:
```
docker run --rm -itd -v $(pwd):/usr/src/app advanced_python
```
