# PicFinder

---
Инструмент для сбора изображений через Google Images с применением фильтров, чтобы убедиться, что изображения подходят под указанные критерии.

### Основные файлы

- **`main.py`**: главный файл, который отвечает за процесс поиска изображений и сохранения ссылок.
- **`validator.py`**: файл содержащий скрипт для фильтрации изображений на основе фона. Проверяет, имеют ли изображения белый или прозрачный фон.


## Установка

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/EgorLaptev/pic-finder.git
   cd picfinder
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

Оформлю раздел более детально и структурированно, чтобы он был удобен для понимания.

---

## Примеры использования

В примерах ниже показаны параметры фона и процесс обработки, а также примеры входных и выходных данных.

### Параметры фильтрации изображений
Для фильтрации изображений по фону использованы следующие параметры:
- `border_ratio = 0.1` — определяет границу в 10% от размеров изображения для анализа фона.
- `threshold = 0.2` — пороговое значение для определения допустимой доли белого или прозрачного фона.

### Пример входных и выходных данных

#### Входной файл (`data.txt`)
```json
{
  "data": [
    "cat",
    "dog",
    "man",
    "The Su-27 hypersonic fighter"
  ]
}
```

#### Выходной файл (`data/links-<timestamp>.json`)
```json
{
    "links": [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQN2_cAOypMH0H-t7XqaDRBuTYKp-hJ4hiZJsAV2_bSKJeAbcQyalGp2H4OS3w&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRy8hVeFjxLXrzFToZQMHAO_ZM3jivJqCMpC_nyBoBtQ0zZo2v6Qj-zRDQjBJU&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4Za-mYunUCRxcb1nVFNG8J52WVHO-YPoTks3a3_tdQEHD72v11VRijl5szw&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSz4keuflpA7HDAb3FKrnOvAD2tIlsaHghp_M0YvlSN_QgyOaC1y8ZHIEptpI&s"
    ]
}
```

### Примеры полученных изображений

На изображениях ниже показаны примеры изображений, ссылки на которые были найдены для объектов в `data.txt`:

| Объект                         | Изображение                                                                                   |
|--------------------------------|-----------------------------------------------------------------------------------------------|
| **cat**                        | ![cat](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQN2_cAOypMH0H-t7XqaDRBuTYKp-hJ4hiZJsAV2_bSKJeAbcQyalGp2H4OS3w&s) |
| **dog**                        | ![dog](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRy8hVeFjxLXrzFToZQMHAO_ZM3jivJqCMpC_nyBoBtQ0zZo2v6Qj-zRDQjBJU&s) |
| **man**                        | ![man](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4Za-mYunUCRxcb1nVFNG8J52WVHO-YPoTks3a3_tdQEHD72v11VRijl5szw&s) |
| **The Su-27 hypersonic fighter** | ![Su-27](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSz4keuflpA7HDAb3FKrnOvAD2tIlsaHghp_M0YvlSN_QgyOaC1y8ZHIEptpI&s) |

