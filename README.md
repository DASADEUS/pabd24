# Предиктивная аналитика больших данных

Учебный проект для демонстрации основных этапов жизненного цикла проекта предиктивной аналитики.  

## Installation 

Клонируйте репозиторий, создайте виртуальное окружение, активируйте и установите зависимости:  

```sh
@echo off
chcp 65001
git clone https://github.com/DASADEUS/pabd24
cd pabd24
python -m venv venv

source venv/bin/activate  # mac or linux
.\venv\Scripts\activate   # windows

pip install -r requirements.txt
set PYTHONPATH=C:\Users\Dmiry_Shigarov\PycharmProjects\pabd24
```

## Usage

### 1. Сбор данных о ценах на недвижимость 
Запуск парсера квартир сайта Циан
```sh
mkdir data\raw
cd src
python parse_cian.py
```

### 2. Выгрузка данных в хранилище S3 
Для доступа к хранилищу скопируйте файл `.env` в корень проекта. 
Получает доступ к общему S3 хранилищу и загружает указанные данные.
```sh
python upload_to_s3.py
```
### 3. Загрузка данных из S3 на локальную машину
Получает доступ к общему S3 хранилищу и скачивает указанные данные.
```sh
python download_from_s3.py
```
### 4. Предварительная обработка данных  
Скрипт объединяет файлы, выделяет нужные параметры, случайно перемешивает записи.
Разделяет получившиеся данные на обучающую и валидационную выборки в указанном отношении.
```sh
mkdir src\log
mkdir data\proc
python preprocess_data.py
```
### 5. Обучение модели 
```sh
python train_model.py
python test_model.py
todo Описание модели и входных параметров для предсказания здесь.  
```
### 6. Запуск приложения flask 

todo

### 7. Использование сервиса через веб интерфейс 

Для использования сервиса используйте файл `web/index.html`.  

