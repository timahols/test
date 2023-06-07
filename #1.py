from driver import driver, ENTER, wait, EC, By

try:
    """Открытие сайта"""
    driver.get("https://ya.ru/")
    print('1) Мы зашли на сайт https://ya.ru/')
    """Ввод слова Тензор"""
    search_bar = wait.until(EC.visibility_of_element_located((By.ID, 'text')))
    search_bar.send_keys(f"Тензор")
    print("2) Успешно: строка поиска существует")
    print('3) Успешно: мы ввели в поиск Тензор')
    """Проверка появления таблицы suggest"""
    suggest = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.mini-suggest__item')))
    print("4) Успешно: таблица с подсказками (suggest) появилась")
    search_bar.send_keys(ENTER)
    print('5) Успешно: мы нажали на enter')
    """Проверка появления страницы результата"""
    search_result = driver.find_element(By.ID, 'search-result')
    print("6) Успешно: страница результатов поиска появилась")
    """Проверка куда ведет первый сайт страницы в окне результата поиска"""
    website_tensor = driver.find_element(By.ID, 'search-result').find_element(By.TAG_NAME, "a")
    if website_tensor.get_attribute('href') == "https://tensor.ru/":
        print("7) Успешно: 1 ссылка ведет на сайт tensor.ru")
except Exception as ex:
    print(f"Ошибка:{ex}")
    driver.close()
    driver.quit()
finally:
    driver.close()
    driver.quit()
