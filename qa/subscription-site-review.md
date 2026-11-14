# Practical AI · структура и оформление сайта

## Что увидели на Claude Training

На [главной Claude Training](https://www.claudetraining.com/) первый экран обращается к компаниям, которые уже оплатили Claude. Далее идут узнаваемые рабочие ситуации, правила проверки результатов, выбор между обучением и внедрением, отзывы, примеры живой практики, материалы и FAQ. Вывод о роли этой последовательности относится к подаче страницы. Данные о её конверсии неизвестны.

## Как это перенесено в Practical AI

На главной открываемся вопросом про уже оплаченный AI. Claude, ChatGPT и Copilot названы в одном предложении. В первом экране показываем задачу ShildPanel и время подготовки отчёта по данным интервью. Дальше идут ситуации команды, подробности двух кейсов, выбор старта, метод, условия диагностики и FAQ. Каждый формат ведёт к своему следующему действию. Проценты использования инструментов, цены и условия конкурента в тексте сайта не используются.

- [ShildPanel](https://practical-ai.pro/ru/cases/shildpanel/) — время отдельных задач со слов клиента.
- [Kerama Marazzi](https://practical-ai.pro/ru/cases/kerama-marazzi/) — программа подготовки внутренних тренеров. 80 коллег — потенциальная аудитория внутреннего обучения.

## Происхождение веб-иллюстраций

Версия-источник — `Systems/brand-studio/output/practical-ai-schools-v5/final/Practical-AI-Schools.pdf`. Числовые значения палитры сверены с её скриптом сборки. Предшествующий референс — `Systems/brand-studio/output/practical-ai-v22-restyle/Practical-AI-Trainings.pdf`. Связь презентаций и происхождение изображений описаны в `Systems/brand-studio/output/practical-ai-schools/final/Источники-и-проверка.md`. Все четыре иллюстрации декоративные. Текст и результаты остаются отдельными HTML-элементами.

| Веб-файл | Источник в сборке презентации | Происхождение и использование |
| --- | --- | --- |
| `lime.webp` | `source-01-00.png` | Лайм из титула корпоративного Practical AI PPTX, перенесён в школьную презентацию и на первый экран сайта |
| `wordmark.svg` | Чёрная капсула `source-02-01.png` | Форма из презентации. На сайте капсула получила стеклянный край и салатовую подсветку текста по уточнению Данила |
| `favicon.svg` | `docs/assets/brand/symbol-primary.svg` | Фирменные диагонали в палитре новой веб-версии |
| `school.webp` | `tile-1.png` | Иллюстрация, созданная для школьной презентации, используется на странице для школ |
| `report.webp` | `case-1.png` | Иллюстрация к карточке времени выполнения отчёта в презентации, используется рядом с ShildPanel |
| `trainers.webp` | `case-3.png` | Иллюстрация к карточке подготовки тренеров в презентации, используется рядом с Kerama Marazzi |

Мастера сохранены в архиве презентации. Растровые веб-копии уменьшены и сохранены в WebP. Inter Variable используется из существующего комплекта сайта по SIL Open Font License.

## Контрольные суммы веб-ассетов

```text
c10b20cf13b5b265116c81f45688cad780c53e08b7861c3cd7be915775485d35  docs/assets/brand/glass/favicon.svg
10544a79ed5cd61d6687cc20c30ed30dbb105ade146a11a01e54e9de525c3cb3  docs/assets/brand/glass/lime.webp
b983243815d36a28b745d5c5e492aaf37ec7eeed9063a8657c2beb4e65bbbc3b  docs/assets/brand/glass/report.webp
ebe9e0e28a33b627d0fa0abe9e279f9808afcbc57be1fdcf8f8a7ca2a406229b  docs/assets/brand/glass/school.webp
c5f6f55e87e550836a6ae35d19f2c40626f4dbe21ccca5ee65c5ce5ec5be7f08  docs/assets/brand/glass/trainers.webp
1bb4dda045b690d912ae177a26550bc9c7bf07009b37c0a273b75606038846ab  docs/assets/brand/glass/wordmark.svg
94fa1b9d0b54021a57a8437e4848d712f43235b90b8000f24ff9680df148f2ab  docs/assets/brand/Inter-Variable.woff2
5dd548d31a85f756e01d63e00d7faf1e324103ed3e9102fcbbabf2cc2db6dd39  docs/assets/brand/OFL.txt
```
