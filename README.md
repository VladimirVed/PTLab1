# Лабораторная 1 по дисциплине "Технологии программирования"

Проект `rating` рассчитывает средний рейтинг студентов по дисциплинам. Данные о
студентах и оценках читаются из файла, указанного параметром `-p`.

## Запуск

```bash
pip install -r requirements.txt
python src/main.py -p data/data.txt
```

## Тестирование

```bash
pycodestyle src test
PYTHONPATH=./:./src pytest test
```
