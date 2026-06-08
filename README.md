# 1409 SDK — Design System

Пакет компонентов дизайн-системы 1409. Готовые HTML/CSS сниппеты для быстрой разработки интерфейсов.

---

## Быстрый старт

### Локальная разработка

```bash
python app.py
# открыть http://<IP>:5000
```

### Подключение через CDN

```html
<!-- Базовые переменные и сброс стилей -->
<link rel="stylesheet" href="https://api.my1409.ru/static/css/vars.css">

<!-- Кнопки -->
<link rel="stylesheet" href="https://api.my1409.ru/static/css/buttons.css">

<!-- Поповеры / модалки -->
<link rel="stylesheet" href="https://api.my1409.ru/static/css/popover.css">

<!-- Поля ввода -->
<link rel="stylesheet" href="https://api.my1409.ru/static/css/form.css">

<!-- Уведомления (toast + empty state) -->
<link rel="stylesheet" href="https://api.my1409.ru/static/css/toast.css">
```

---

## CSS-файлы

| Файл | Содержимое |
|------|-----------|
| `vars.css` | CSS-переменные темы, сброс стилей, базовая типографика |
| `buttons.css` | `.btn`, `.btn-primary`, `.btn-glass`, `.btn-danger`, `.btn-ghost`, размеры, иконки |
| `popover.css` | `.popover-overlay`, `.popover`, `.popover--bottom`, `.popover--top`, анимации |
| `form.css` | `.form-group`, `.form-label`, `.form-input`, `.form-select`, `.form-textarea`, состояния |
| `toast.css` | `.toast`, `.toast--success/error/warning`, `.empty-state` |

---

## Компоненты

### Кнопки (`buttons.css`)

| Класс | Описание |
|-------|---------|
| `.btn` | Базовый класс кнопки |
| `.btn-primary` | Основная кнопка (акцентный цвет) |
| `.btn-glass` | Стеклянная кнопка (glassmorphism) |
| `.btn-danger` | Деструктивное действие |
| `.btn-ghost` | Прозрачная кнопка |
| `.btn--sm` | Маленький размер |
| `.btn--lg` | Большой размер |
| `.btn--icon` | Только иконка (квадратная) |
| `.btn--full` | Во всю ширину |

### Поля ввода (`form.css`)

| Класс | Описание |
|-------|---------|
| `.form-group` | Обёртка для поля |
| `.form-label` | Подпись поля |
| `.form-label--required` | Метка обязательного поля (добавляет `*`) |
| `.form-input` | Текстовое поле |
| `.form-input--error` | Состояние ошибки |
| `.form-input--success` | Состояние успеха |
| `.form-input-wrap` | Обёртка для поля с иконкой |
| `.form-input-icon` | Иконка внутри поля |
| `.form-textarea` | Многострочное поле |
| `.form-select` | Выпадающий список (кастомный chevron) |
| `.form-hint` | Подсказка под полем |
| `.form-error-msg` | Сообщение об ошибке |
| `.form-success-msg` | Сообщение об успехе |

### Уведомления (`toast.css`)

| Класс | Описание |
|-------|---------|
| `.toast` | Базовый toast (скрыт) |
| `.toast.shown` | Показать toast |
| `.toast--success` | Зелёный toast |
| `.toast--error` | Красный toast |
| `.toast--warning` | Жёлтый toast |
| `.empty-state` | Пустое состояние (иконка + текст) |
| `.empty-state__icon` | Иконка пустого состояния |

### Поповеры и модалки (`popover.css`)

| Класс | Описание |
|-------|---------|
| `.popover-overlay` | Оверлей на весь экран |
| `.popover` | Центральная модалка |
| `.popover--bottom` | Нижний шит (bottom sheet) |
| `.popover--top` | Верхнее уведомление |
| `.popover__title` | Заголовок поповера |
| `.popover__body` | Тело поповера |
| `.popover__footer` | Подвал поповера |

```javascript
// Открыть / закрыть поповер
openPopover('myOverlayId');
closePopover('myOverlayId');
```

---

## Компоненты (HTML-сниппеты)

Сниппеты находятся в `templates/components/`. Каждый файл содержит `<style>` + HTML-разметку.

### Avatar (`avatar.html`)

```html
<!-- Размеры: av-xs, av-sm, av-md, av-lg, av-xl, av-2xl -->
<div class="av av-md"><img src="..." alt="user"></div>

<!-- С инициалами -->
<div class="av av-md" style="background:linear-gradient(135deg,#4446E1,#e63530);">ИИ</div>

<!-- Со статусом -->
<div class="av-wrap">
    <div class="av av-md"><img src="..." alt="user"></div>
    <span class="av-status av-status--online"></span>
</div>

<!-- Группа -->
<div class="av-group">
    <div class="av-wrap"><div class="av av-sm">...</div></div>
    <div class="av-wrap"><div class="av av-sm">...</div></div>
    <div class="av-group-more">+8</div>
</div>
```

| Класс | Описание |
|-------|---------|
| `.av` | Базовый аватар |
| `.av-xs/sm/md/lg/xl/2xl` | Размеры: 22/32/44/64/96/128px |
| `.av--accent` | Акцентная рамка |
| `.av--sq` | Квадратный (скруглённые углы) |
| `.av-wrap` | Обёртка для аватара со статусом |
| `.av-status--online/away/busy/offline` | Индикатор статуса |
| `.av-group` | Группа с наложением |
| `.av-group-more` | "+N" кружок в группе |
| `.av-row` | Аватар + текст в строку |

### Progress (`progress.html`)

```html
<!-- Линейный -->
<div class="progress">
    <div class="progress__bar" style="width:72%;"></div>
</div>

<!-- С подписью -->
<div class="progress-group">
    <div class="progress-header">
        <span class="progress-label">Загрузка</span>
        <span class="progress-value">72%</span>
    </div>
    <div class="progress">
        <div class="progress__bar" style="width:72%;"></div>
    </div>
</div>

<!-- Круговой (SVG) -->
<div class="progress-circle">
    <svg class="progress-circle__svg" width="72" height="72" viewBox="0 0 72 72">
        <circle class="progress-circle__track" cx="36" cy="36" r="30"/>
        <circle class="progress-circle__fill" cx="36" cy="36" r="30"
            stroke-dasharray="188.5" stroke-dashoffset="52.8"/>
    </svg>
    <span class="progress-circle__label">72%</span>
</div>
```

| Класс | Описание |
|-------|---------|
| `.progress` | Базовый прогресс-бар |
| `.progress--sm/lg` | Размеры: 4px / 12px |
| `.progress--indeterminate` | Анимация без значения |
| `.progress__bar` | Заполнение (gradient accent) |
| `.progress__bar--success/warning/danger` | Цветные варианты |
| `.progress-circle` | Круговой прогресс |
| `.stepper` | Горизонтальный степпер |
| `.step` | Шаг степпера |
| `.step.done` | Завершённый шаг |
| `.step.active` | Текущий шаг |

### Switch / Checkbox / Radio (`switch.html`)

```html
<!-- Toggle switch -->
<label class="switch">
    <input class="switch__input" type="checkbox" checked>
    <span class="switch__track"></span>
</label>

<!-- Checkbox -->
<label class="checkbox">
    <input class="checkbox__input" type="checkbox">
    <span class="checkbox__box">
        <svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24">
            <polyline points="20 6 9 17 4 12"/>
        </svg>
    </span>
    <span class="checkbox__label">Текст</span>
</label>

<!-- Radio -->
<label class="radio">
    <input class="radio__input" type="radio" name="group">
    <span class="radio__dot"></span>
    <span class="radio__label">Вариант</span>
</label>
```

| Класс | Описание |
|-------|---------|
| `.switch` | iOS-style тогл |
| `.switch--sm/lg` | Размеры |
| `.switch--green/red/yellow` | Цветные варианты |
| `.setting-row` | Строка настройки (label + switch) |
| `.checkbox` | Кастомный чекбокс |
| `.radio` | Кастомная радио-кнопка |

### Input (`input.html`)

8 готовых вариантов: обычный, с иконкой, пароль с показом, select, textarea, ошибка, успех, disabled.

### Header (`header.html`)

3 варианта шапки приложения: назад + заголовок + действие, заголовок с акцентной кнопкой, строка поиска.

### OTP (`otp.html`)

6-значный ввод кода с автопереходом, вставкой, шейком при ошибке, таймером повтора.

### PIN (`pin.html`)

Ввод PIN-кода с нумпадом (как iOS), анимацией точек, shake при ошибке.

### Bottom Sheet (`bottomsheet.html`)

Нижние панели через `.popover--bottom`: Action Sheet и Picker.

### QR (`qr.html`)

Полноэкранный QR с логотипом по центру, анимацией pulse, кнопкой закрытия.

### Skeleton (`skeleton.html`)

Shimmer-заглушки: `.sk-card`, `.sk-avatar`, `.sk-line`, `.sk-img`, `.sk-pill`.

### Navigation (`navigation.html`)

iOS 26 Liquid Glass tab bar с анимацией активной вкладки.

---

## Базовые CSS-переменные (`vars.css`)

```css
--accent:          #4446E1;   /* основной акцент */
--bg-primary:      /* тёмный фон */
--bg-secondary:    /* вторичный фон */
--bg-hover:        /* фон при ховере */
--glass-bg:        /* стеклянный фон */
--text-primary:    /* основной текст */
--text-secondary:  /* вторичный текст */
--text-muted:      /* приглушённый текст */
--border-color:    /* цвет рамки */
--border-light:    /* светлая рамка */
--radius-sm:       6px
--radius-md:       12px
--radius-lg:       16px
--radius-xl:       20px
--radius-full:     9999px
```

### Переключение темы

```javascript
document.documentElement.setAttribute('data-theme', 'light'); // светлая
document.documentElement.setAttribute('data-theme', 'dark');  // тёмная
```

---

## Структура проекта

```
1409-SDK/
├── app.py                        # Flask-приложение
├── static/
│   ├── css/
│   │   ├── vars.css              # переменные и сброс
│   │   ├── buttons.css           # кнопки
│   │   ├── popover.css           # поповеры / модалки
│   │   ├── form.css              # поля ввода
│   │   └── toast.css             # уведомления
│   ├── default_avatar.png        # дефолтный аватар
│   └── logo.png                  # логотип 1409
├── templates/
│   ├── base.html                 # базовый шаблон
│   ├── preview_shell.html        # оболочка превью компонента
│   ├── admin/
│   │   └── index.html            # админ-панель
│   └── components/
│       ├── avatar.html
│       ├── bottomsheet.html
│       ├── header.html
│       ├── input.html
│       ├── navigation.html
│       ├── otp.html
│       ├── pin.html
│       ├── progress.html
│       ├── qr.html
│       ├── skeleton.html
│       └── switch.html
└── README.md
```

---

## Админ-панель

Доступна по адресу `sdk.my1409.ru` (прод) или `http://<IP>:5000` (дев).

### Функции

- **Сайдбар** — список всех компонентов, поиск по названию
- **Превью** — рендер компонента в iframe
- **Demo triggers** — автоматически появляются кнопки для поповеров / toast
- **Секционные лейблы** — HTML-комментарии `<!-- ── 1. Название ── -->` превращаются в подписи секций
- **Тема** — переключение dark/light прямо в превью
- **Выделить** (`Picker`) — кликни на любой элемент в превью, получи его HTML и соответствующий CSS в боковом ящике
- **Копировать** — скопировать HTML или CSS выделенного элемента

### Горячие клавиши превью

| Кнопка | Действие |
|--------|---------|
| Обновить | Перезагрузить iframe |
| Тема | Переключить dark/light |
| Выделить | Активировать element picker |

---

## API-эндпоинты

| Метод | URL | Описание |
|-------|-----|---------|
| `GET` | `/` | Редирект в `/admin` |
| `GET` | `/admin` | Главная страница админ-панели |
| `GET` | `/preview/<name>` | Превью компонента |
| `GET` | `/static/<path>` | Статические файлы |

---

## Встраивание

Все статические файлы доступны через CDN:

```
https://api.my1409.ru/static/css/<файл>
https://api.my1409.ru/static/<файл>
```

Пример минимального подключения:

```html
<link rel="stylesheet" href="https://api.my1409.ru/static/css/vars.css">
<link rel="stylesheet" href="https://api.my1409.ru/static/css/buttons.css">
```
