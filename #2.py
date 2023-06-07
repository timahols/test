from driver import driver, wait, EC, By

try:
    """Открытие сайта"""
    driver.get("https://ya.ru/")
    print('1) Мы зашли на сайт https://ya.ru/')
    """клик по строке поиска для активации раздела с сервисами"""
    search_bar = wait.until(EC.visibility_of_element_located((By.ID, 'text')))
    search_bar.click()
    driver.find_element(By.ID, 'text').click()
    all_services = driver.find_element(By.CLASS_NAME, 'services-suggest__icons-more')
    print("2) Успешно: кнопка меню присутствует")
    """Клик по кнопке "все сервисе" для выбора "яндекс.картинок"""
    all_services.click()
    """Поиск кнопки в сервисе "яндекс.картинок" и клик по нему для перехода"""
    website_picture = driver.find_element(By.CLASS_NAME, 'services-more-popup__section-content').find_elements(By.TAG_NAME, "a")
    for link in website_picture:
        if link.get_attribute("href") == "https://yandex.ru/images/":
            link.click()
            print('3) Успешно: меню открылось, выбрали "Картинки"')
            break
    """Переход во вторую вкладу"""
    driver.switch_to.window(driver.window_handles[-1])
    """Проверка корректности url сайта"""
    if driver.current_url == "https://yandex.ru/images/":
        print('4) Успешно: мы на сайте "https://yandex.ru/images/"')
    else:
        print(f'4) Ошибка: мы перешли на не тот сайт, сейчас мы находимся здесь: {driver.current_url}')
        driver.close()
        driver.quit()
    """Взятие в переменную название первой котегории"""
    text_the_first_1 = driver.find_element(By.CLASS_NAME, 'PopularRequestList-SearchText').text
    """Открытие первой котегории"""
    driver.find_element(By.CLASS_NAME, 'PopularRequestList-Item_pos_0').click()
    print('5) Успешно: открыли первую категорию')
    """Проверка совпадает ли название первой котегории с текстом в поле поиска"""
    search_field_result = wait.until(EC.visibility_of_element_located((By.NAME, 'text')))
    search_field_result_2 = search_field_result.get_attribute("value")
    if text_the_first_1 == search_field_result_2:
        print('6) Успешно: название категории корректно отображается в поле поиска')
    else:
        print("6) Ошибка: название категории некорректно отображается в поле поиска")
        driver.close()
        driver.quit()
    """Открытие первой картинки"""
    open_first_picture = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'serp-item__preview')))
    open_first_picture.click()
    print('7) Успешно: открываем первую картинку')
    """Проверка открытия картинки"""
    image_element = driver.find_element(By.CSS_SELECTOR, ".MMImage-Origin")
    print('8) Успешно: картина действительно открыта')
    """Проверка смены картинки ПРИ нажатии на кнопку "next"""
    next = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'CircleButton_type_next')))
    next.click()
    print('9) Успешно: мы нажали  вперед')
    """Проверка смены картинки ПОСЛЕ нажатии на кнопку "next"""
    new_image_element = driver.find_element(By.CSS_SELECTOR, '.MMImage-Origin')
    if image_element != new_image_element:
        print('10) Ошибка: картина не сменилась')
        driver.close()
        driver.quit()
    else:
        print("10) Успешно: картина сменилась")
    """Проверка вернется ли назад картинка из 8 пункта ПРИ нажатии на кнопку "back"""
    back = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.CircleButton_type_prev')))
    back.click()
    print('11) Успешно: мы нажали  назад')
    """Проверка вернулась ли назад картинка из 8 пункта ПОСЛЕ нажатии на кнопку "back"""
    back_image_element = driver.find_element(By.CSS_SELECTOR, '.MMImage-Origin')
    if back_image_element == image_element:
        print('12) Успешно: картина вернулась назад')
        driver.close()
        driver.quit()
    else:
        print("12) Ошибка: картина не осталась из пункта 8")
        driver.close()
        driver.quit()
except Exception as ex:
    print(f"Ошибка:{ex}")
    driver.close()
    driver.quit()
finally:
    driver.close()
    driver.quit()
