# Лабораторная работа 8

**Работа с SQL-запросами в нашем проекте** 

**Федоров Илья**

**Жардем Алтынай**

**П3А**

Ссылка на проект: 

[Главная — ReRead](https://reread.lyarov22.repl.co/)

## INSERT Запросы

1. INSERT INTO "reSite_book" ("title", "author", "year", "category_id") VALUES ('Война и мир', 'Лев Толстой', 1869, 1);
2. INSERT INTO "reSite_book" ("title", "author", "year", "category_id") VALUES ('Преступление и наказание', 'Фёдор Достоевский', 1866, 2);
3. INSERT INTO "reSite_book" ("title", "author", "year", "category_id") VALUES ('1984', 'Джордж Оруэлл', 1949, 3);
4. INSERT INTO "reSite_book" ("title", "author", "year", "category_id") VALUES ('Мастер и Маргарита', 'Михаил Булгаков', 1967, 4);
5. INSERT INTO "reSite_book" ("title", "author", "year", "category_id") VALUES ('Анна Каренина', 'Лев Толстой', 1877, 5);
6. INSERT INTO "reSite_book" ("title", "author", "year", "category_id") VALUES ('Убить пересмешника', 'Харпер Ли', 1960, 6);
7. INSERT INTO "reSite_book" ("title", "author", "year", "category_id") VALUES ('Гарри Поттер и философский камень', 'Джоан Роулинг', 1997, 7);
8. INSERT INTO "reSite_book" ("title", "author", "year", "category_id") VALUES ('Три товарища', 'Эрих Мария Ремарк', 1936, 8);
9. INSERT INTO "reSite_book" ("title", "author", "year", "category_id") VALUES ('Герой нашего времени', 'Михаил Лермонтов', 1840, 9);
10. INSERT INTO "reSite_book" ("title", "author", "year", "category_id") VALUES ('Маленький принц', 'Антуан де Сент-Экзюпери', 1943, 10);

![Untitled](%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%208%203f71ac92406b42c29be1c25444d6da66/Untitled.png)

## UPDATE Запросы

1. **`UPDATE "reSite_advertisement" SET "price" = 7500 WHERE "unique_number" = 12345;`**
2. **`UPDATE "reSite_advertisement" SET "price" = 6000 WHERE "unique_number" = 54321;`**
3. **`UPDATE "reSite_advertisement" SET "price" = 9000 WHERE "unique_number" = 98765;`**
4. **`UPDATE "reSite_advertisement" SET "price" = 8500 WHERE "unique_number" = 24680;`**
5. **`UPDATE "reSite_advertisement" SET "price" = 7200 WHERE "unique_number" = 13579;`**

```
UPDATE "reSite_book"
SET "category_id" = 5
WHERE "title" = 'Война и мир' AND "author" = 'Лев Толстой';
```

![Untitled](%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%208%203f71ac92406b42c29be1c25444d6da66/Untitled%201.png)

## SELECT Запросы

SELECT * FROM "reSite_category";

SELECT * FROM "reSite_advertisement" WHERE "price" > 5000;

SELECT * FROM "reSite_book" WHERE "author" = 'Лев Толстой';

![Untitled](%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%208%203f71ac92406b42c29be1c25444d6da66/Untitled%202.png)

## DELETE Запросы

```
DELETE FROM "reSite_book"
WHERE "category_id" = 5;
```

![Untitled](%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%208%203f71ac92406b42c29be1c25444d6da66/Untitled%203.png)