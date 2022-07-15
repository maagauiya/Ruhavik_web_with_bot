from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "TG BOT"

    def handle(self, *args, **options):
        pass
from datetime import date

import telebot
import pathlib
import certifi
from django.conf import settings
import time
import shutil
from app1.models import *
from telebot import types
bot = telebot.TeleBot("5164041283:AAGxhfZv3IO8k-x-3NJ4lJSb5gWD_zKqnJ4")

ca = certifi.where()



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton(u"Да")
    markup.add(item1)
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    bot.send_message(message.chat.id, f" Здравствуйте, {driver.driver_name} {driver.driver_last_name} \nМашина:{driver.car.car_model} {driver.car.car_number}  \nВы готовы начать поездку?", reply_markup=markup)
    bot.register_next_step_handler(message, poezdka)
    # print()
    # else:
    #     bot.send_message(message.chat.id, "Я не знаю кто ты!")


def camera_checking(message):
    driver = Driver.objects.filter(driver_chat_id = message.chat.id)
    
    if driver.count() >0:

        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Начнем с проверки камеры. Сняли чехол с камеры?",reply_markup=markup)
        bot.register_next_step_handler(message, proverka_constr)
        # bot.register_next_step_handler(message, poezdka)
    else:
        bot.send_message(message.chat.id, "Кто ты, Воин?")


def proverka_constr(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    if "выполнил" in message.text.lower():
        cam = CameraCheckin.objects.create(
            driver = driver,
            car = driver.car,
            cover_check = True
        )
        bot.send_message(message.chat.id, "Отправьте пожалуйста фото несущей конструкции для проверки.")
        bot.register_next_step_handler(message, proverka_constr_photo)
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Сняли чехол с камеры? Нажмите выполнил если вы это сделали.",reply_markup=markup)
        bot.register_next_step_handler(message, proverka_constr)
    
def proverka_constr_photo(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    cam  = CameraCheckin.objects.filter(driver__id = driver.id).filter(created__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/support/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)

        cam.support_st_check_photo = f"images/support/{driver.driver_name}_{today}_{raw}.jpg"
        cam.save()
        
        # print(name)
        
        # img = open(name, 'rb')
        # bot.send_photo(message.chat.id, img)
        # print("/".join([path,name]))
        bot.send_message(message.chat.id, "Фото получено. Теперь проверка линз на сколы и потертости (отправьте 4 фото с разных ракурсов по очереди).") #то что пойдет юзеру после отправки сообщения
        bot.register_next_step_handler(message, proverka_constr_photo1)
    else:
        bot.send_message(message.chat.id, "Отправьте пожалуйста фото несущей конструкции для проверки.")
        bot.register_next_step_handler(message, proverka_constr_photo)


def proverka_constr_photo1(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    cam  = CameraCheckin.objects.filter(driver__id = driver.id).filter(created__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/chips/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
        cam.chips_and_abrasions_check_photo1 = f"images/chips/{driver.driver_name}_{today}_{raw}.jpg"
        cam.save() 

        bot.send_message(message.chat.id, "Первое фото получено. Ещё три с других ракурсов.") #то что пойдет юзеру после отправки сообщения
        bot.register_next_step_handler(message, proverka_constr_photo2)
    else:
        bot.send_message(message.chat.id, "Теперь проверка линз на сколы и потертости (отправьте 4 фото с разных ракурсов по очереди).")
        bot.register_next_step_handler(message, proverka_constr_photo1)

def proverka_constr_photo2(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    cam  = CameraCheckin.objects.filter(driver__id = driver.id).filter(created__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/chips/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
        cam.chips_and_abrasions_check_photo2 = f"images/chips/{driver.driver_name}_{today}_{raw}.jpg"
        cam.save()
            

        bot.send_message(message.chat.id, "Второе фото получено. Ещё два с других ракурсов.")
        bot.register_next_step_handler(message, proverka_constr_photo3)
    else:
        bot.send_message(message.chat.id, "Отправьте второе фото линзы, с другого ракурса.")
        bot.register_next_step_handler(message, proverka_constr_photo2)

def proverka_constr_photo3(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    cam  = CameraCheckin.objects.filter(driver__id = driver.id).filter(created__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/chips/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
        cam.chips_and_abrasions_check_photo3 = f"images/chips/{driver.driver_name}_{today}_{raw}.jpg"
        cam.save()
            

        bot.send_message(message.chat.id, "Третье фото получено. Отправьте последнее с другого ракурса.")
        bot.register_next_step_handler(message, proverka_constr_photo4)
    else:
        bot.send_message(message.chat.id, "Отправьте третье фото линзы, с другого ракурса.")
        bot.register_next_step_handler(message, proverka_constr_photo3)

def proverka_constr_photo4(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    cam  = CameraCheckin.objects.filter(driver__id = driver.id).filter(created__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/chips/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
        cam.chips_and_abrasions_check_photo4 = f"images/chips/{driver.driver_name}_{today}_{raw}.jpg"
        cam.save()
            
        bot.send_message(message.chat.id, "Четвертое фото получено. Проверка линз на сколы и потертости закончилась. Следующее запуск камеры, сделайте снимок индикаторов.")
        bot.register_next_step_handler(message, zapusk_camera)
    else:
        bot.send_message(message.chat.id, "Отправьте четвертое фото линзы, с другого ракурса.")
        bot.register_next_step_handler(message, proverka_constr_photo4)

def zapusk_camera(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    cam  = CameraCheckin.objects.filter(driver__id = driver.id).filter(created__date = today)[0]
    if message.content_type == 'photo':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/camera/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        path = str(pathlib.Path().resolve())
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
        
        cam.camera_start_photo = f"images/camera/{driver.driver_name}_{today}_{raw}.jpg"
        cam.save()
        bot.send_message(message.chat.id, "Фото индикаторов получено. Проверьте дату установки диска.", reply_markup=markup)
        bot.register_next_step_handler(message, osmotr_koles)
    else:
        bot.send_message(message.chat.id, "Следующее запуск камеры, сделайте снимок индикаторов.")
        bot.register_next_step_handler(message, zapusk_camera)


def osmotr_koles(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    cam  = CameraCheckin.objects.filter(driver__id = driver.id).filter(created__date = today)[0]
    if "выполнил" in message.text.lower():
        cam.ssd_date_check = True
        cam.save()
        bot.send_message(message.chat.id, "Отлично. Теперь осмотр колес и ходовой части (сделайте 2 фото с двух сторон).")
        st = Start.objects.create(
            driver = driver,
            car = driver.car,
        )
        bot.register_next_step_handler(message, osmotr_koles1)
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Проверьте дату установки диска.", reply_markup=markup)
        bot.register_next_step_handler(message, osmotr_koles)

def osmotr_koles1(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    st  = Start.objects.filter(driver__id = driver.id).filter(start_date__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/gear/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
     
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
            
        st.wheels_and_running_gear_check_photo1 = f"images/gear/{driver.driver_name}_{today}_{raw}.jpg"
        st.save()
        bot.send_message(message.chat.id, "Первое фото получено. Отправьте второе фото с другой стороны.")
        bot.register_next_step_handler(message, osmotr_koles2)
    else:
        bot.send_message(message.chat.id, "Теперь осмотр колес и ходовой части (сделайте 2 фото с двух сторон).")
        bot.register_next_step_handler(message, osmotr_koles1)


def osmotr_koles2(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    st  = Start.objects.filter(driver__id = driver.id).filter(start_date__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/gear/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
     
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
            
        st.wheels_and_running_gear_check_photo2 = f"images/gear/{driver.driver_name}_{today}_{raw}.jpg"
        st.save()
        bot.send_message(message.chat.id, "Второе фото получено. Теперь проверка масла, отправьте фото.")
        bot.register_next_step_handler(message, proverka_masla)
    else:
        bot.send_message(message.chat.id, "Отправьте второе фото с другой стороны.")
        bot.register_next_step_handler(message, osmotr_koles2)

def proverka_masla(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    st  = Start.objects.filter(driver__id = driver.id).filter(start_date__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/oil/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
     
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
            
        st.oil_check_photo2 = f"images/oil/{driver.driver_name}_{today}_{raw}.jpg"
        st.save()
        bot.send_message(message.chat.id, "Фото получено. Теперь показания одометра и приборной панели в целом. Отправьте фото одометра.")
        bot.register_next_step_handler(message, photo_odometr)
    else:
        bot.send_message(message.chat.id, "Теперь проверка масла, отправьте фото.")
        bot.register_next_step_handler(message, proverka_masla)


def photo_odometr(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    st  = Start.objects.filter(driver__id = driver.id).filter(start_date__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/odometer/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
     
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
            
        st.odometer_and_dashboard_readings_data_photo = f"images/odometer/{driver.driver_name}_{today}_{raw}.jpg"
        st.save()
        bot.send_message(message.chat.id, "Фото получено. Введите данные одометра.")
        bot.register_next_step_handler(message, odometr_data)
    else:
        bot.send_message(message.chat.id, "Отправьте фото одометра.")
        bot.register_next_step_handler(message, photo_odometr)

def odometr_data(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    st  = Start.objects.filter(driver__id = driver.id).filter(start_date__date = today)[0]
    st.odometer_and_dashboard_readings_data = message.text
    st.save()
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton(u"Начать")
    markup.add(item1)
    bot.send_message(message.chat.id, "Данные получены. Теперь прогрев двигателя. Нажмите кнопку 'Начать' для начала таймера прогрева двигателя (5 минут)", reply_markup=markup)
    bot.register_next_step_handler(message, timer_dvigatel)

def timer_dvigatel(message):
    if "начать" in message.text.lower():
        
        bot.send_message(message.chat.id, "Отлично, время пошло. Мы вас уведомим об окончании.")
        total_seconds = 300

        while total_seconds > 0:
            time.sleep(1)
            total_seconds-=1
            # print(total_seconds)

            if (total_seconds % 60 == 0):
                # print(int(total_seconds/60))
                bot.send_message(message.chat.id, "Осталось " + str(int(total_seconds/60)) + " минуты.")
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Отлично, 5 минут закончилось. Проверьте подключение планшета к камере.", reply_markup=markup)
        
        bot.register_next_step_handler(message, proverka_plansheta)
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Начать")
        markup.add(item1)
        bot.send_message(message.chat.id, "Теперь прогрев двигателя. Нажмите кнопку 'Начать' для начала таймера прогрева двигателя (5 минут)", reply_markup=markup)
        bot.register_next_step_handler(message, timer_dvigatel)


def proverka_plansheta(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton(u"Выполнил\u2705")
    markup.add(item1)
    if "выполнил" in message.text.lower():
        
        st  = Start.objects.filter(driver__id = driver.id).filter(start_date__date = today)[0]
        st.tablet_connection = True
        st.save()
        bot.send_message(message.chat.id, "Отлично. Теперь заполнение путевого листа.", reply_markup=markup)
        Trip_and_documents.objects.create(
            driver = driver,
            car = driver.car,
        )
        bot.register_next_step_handler(message, putevoi_list)
    else:
        bot.send_message(message.chat.id, "Проверьте подключение планшета к камере", reply_markup=markup)
        bot.register_next_step_handler(message, proverka_plansheta)

def putevoi_list(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    trip  = Trip_and_documents.objects.filter(driver__id = driver.id).filter(check_date__date = today)[0]
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton(u"Выполнил\u2705")
    markup.add(item1)
    if "выполнил" in message.text.lower():
        trip.trip_sheet = True
        trip.save()
        bot.send_message(message.chat.id, "Отлично. Теперь проверка началия документов при себе.", reply_markup=markup)
        bot.register_next_step_handler(message, start_poezdka)
    else:
        bot.send_message(message.chat.id, "Проверьте подключение планшета к камере", reply_markup=markup)
        bot.register_next_step_handler(message, putevoi_list)

def start_poezdka(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    trip  = Trip_and_documents.objects.filter(driver__id = driver.id).filter(check_date__date = today)[0]
    if "выполнил" in message.text.lower():
        trip.documents_check = True
        trip.save()
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Начать")
        markup.add(item1)
        bot.send_message(message.chat.id, "Отлично. Теперь нажмите кнопку 'Начать', для начала поездки.", reply_markup=markup)
        bot.register_next_step_handler(message, poezdka)
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Теперь проверка наличия документов при себе.", reply_markup=markup)
        bot.register_next_step_handler(message, start_poezdka)

def poezdka(message):
    if "начать" or "вернуться" in message.text.lower():
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Смена ССД диска")
        item2=types.KeyboardButton(u"Остановка на заправку")
        item3=types.KeyboardButton(u"Остановила полиция")
        item4=types.KeyboardButton(u"Остановка из-за неисправностей авто")
        item5=types.KeyboardButton(u"Остановка на обед")
        item6=types.KeyboardButton(u"Остановка на ужин")
        item7=types.KeyboardButton(u"Остановка при ДТП или ЧП")
        item8=types.KeyboardButton(u"Завершение поездки")
        markup.row(item1, item2, item3)
        markup.row(item4, item5)
        markup.row(item6, item7)
        markup.row(item8)
        

        bot.send_message(message.chat.id, "Вы начали поездку. Во время поездки выберите ниже действия которые будете делать.", reply_markup=markup)
        bot.register_next_step_handler(message, actions)
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Теперь проверка началия документов при себе.", reply_markup=markup)
        bot.register_next_step_handler(message, start_poezdka)


def actions(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    if "Смена ССД диска" in message.text:
        
        bot.send_message(message.chat.id, "Введите номер снятого диска в цифрах.")
        
        bot.register_next_step_handler(message, smena_ssd)

    elif "Остановка на заправку" in message.text:
        bot.send_message(message.chat.id, "Введите количество залитого топлива.")
        # bot.send_message(message.chat.id, message.text)
        bot.register_next_step_handler(message, zapravka)
    elif "Остановила полиция" in message.text:
        Police_problem.objects.create(
            driver=driver,
            car = driver.car
        )
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Сделайте срочный звонок на номер +7 776 167 0381.", reply_markup=markup)
        bot.register_next_step_handler(message, poezdka)
    elif "Остановка из-за неисправностей авто" in message.text:
        Malfunctions.objects.create(
            driver=driver,
            car = driver.car
        )
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Сделайте срочный звонок на номер +7 776 167 0381.", reply_markup=markup)
        bot.register_next_step_handler(message, poezdka)
    elif "Остановка на обед" in message.text:
        bot.send_message(message.chat.id, "Убедитесь что машина в зоне видимости и сделайте фото.")
        Lunch_stop.objects.create(
            driver = driver,
            car = driver.car,
        )
        bot.register_next_step_handler(message, obed_photo1)
    elif "Остановка на ужин" in message.text:
        bot.send_message(message.chat.id, "Убедитесь что машина в зоне видимости и сделайте фото.")
        Dinner_stop.objects.create(
            driver = driver,
            car = driver.car,
        )
        bot.register_next_step_handler(message, dinner_photo)
    elif "Остановка при ДТП или ЧП" in message.text:
        Dtp_or_chp.objects.create(
            driver = driver,
            car = driver.car
        )
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Сделайте запись кнопкой видеорегистратора.", reply_markup=markup)
        
        bot.register_next_step_handler(message, dtp)
    elif "Завершение поездки":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Вы завершаете поездку. Остановили двигатель?", reply_markup=markup)
        bot.register_next_step_handler(message, dvigatel)


def smena_ssd(message):
    
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    ChangeSSD.objects.create(
            driver = driver,
            car = driver.car,
            ssd_old = message.text
        )
    bot.send_message(message.chat.id, "Номер снятого диска получен. Теперь введите номер установленного диска в цифрах.")
    
    bot.register_next_step_handler(message, smena_ssd1)

def smena_ssd1(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    change_ssd  = ChangeSSD.objects.filter(driver__id = driver.id).filter(change_date__date = today)[0]
    change_ssd.ssd_new = message.text
    change_ssd.save()
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton(u"Вернуться")
    markup.add(item1)
    bot.send_message(message.chat.id, "Номер установленного диска получен. Нажмите кнопку 'Вернуться', чтобы вернуться в меню во время поездки.", reply_markup=markup)
    # bot.send_message(message.chat.id, message.text)
    
    bot.register_next_step_handler(message, poezdka)

def zapravka(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    Refueling.objects.create(
        driver = driver,
        car = driver.car,
        liter = message.text
    )
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton(u"Вернуться")
    markup.add(item1)
    bot.send_message(message.chat.id, "Информация получена. Нажмите кнопку 'Вернуться', чтобы вернуться в меню во время поездки.", reply_markup=markup)
    bot.register_next_step_handler(message, poezdka)

def obed_photo1(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    lunch_stop  = Lunch_stop.objects.filter(driver__id = driver.id).filter(launc_stop__date = today)[0]
    if message.content_type == 'photo':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/car/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)

        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
            
        lunch_stop.car_in_zone_photo = f"images/car/{driver.driver_name}_{today}_{raw}.jpg"
        lunch_stop.save()
        bot.send_message(message.chat.id, "Фото получено. Проверьте активность сигнализации.", reply_markup=markup)
        bot.register_next_step_handler(message, obed_signal1)
    else:
        bot.send_message(message.chat.id, "Убедитесь что машина в зоне видимости и сделайте фото.")
        bot.register_next_step_handler(message, obed_photo1)

def obed_signal1(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    lunch_stop  = Lunch_stop.objects.filter(driver__id = driver.id).filter(launc_stop__date = today)[0]
    if "выполнил" in message.text.lower():
        lunch_stop.alarm_check =True
        lunch_stop.save()
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Вернуться")
        markup.add(item1)
        bot.send_message(message.chat.id, "При выезде осмотрите авто. Нажмите кнопку 'Вернуться', чтобы вернуться в меню во время поездки.", reply_markup=markup)
        lunch_stop.car_checkout =True
        lunch_stop.save()
        bot.register_next_step_handler(message, poezdka)

    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Проверьте активность сигнализации.", reply_markup=markup)
        bot.register_next_step_handler(message, obed_signal1)


def dinner_photo(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    dinner_stop = Dinner_stop.objects.filter(driver__id = driver.id).filter(dinner_date__date = today)[0]
    if message.content_type == 'photo':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/car/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)

        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
            
        dinner_stop.car_in_zone_photo = f"images/car/{driver.driver_name}_{today}_{raw}.jpg"
        dinner_stop.save()
        bot.send_message(message.chat.id, "Фото получено. Проверьте активность сигнализации.", reply_markup=markup)
        bot.register_next_step_handler(message, dinner_signal)
    else:
        bot.send_message(message.chat.id, "Убедитесь что машина в зоне видимости и сделайте фото.")
        bot.register_next_step_handler(message, dinner_photo)

def dinner_signal(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    dinner_stop  = Dinner_stop.objects.filter(driver__id = driver.id).filter(dinner_date__date = today)[0]
    if "выполнил" in message.text.lower():
        dinner_stop.alarm_check =True
        dinner_stop.save()
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Вернуться")
        markup.add(item1)
        bot.send_message(message.chat.id, "При выезде осмотрите авто. Нажмите кнопку 'Вернуться', чтобы вернуться в меню во время поездки.", reply_markup=markup)
        dinner_stop.car_checkout =True
        dinner_stop.save()
        bot.register_next_step_handler(message, poezdka)

    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Проверьте активность сигнализации.", reply_markup=markup)
        bot.register_next_step_handler(message, dinner_signal)


def dtp(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    if "выполнил" in message.text.lower():
        
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Сделайте срочный звонок на номер +7 776 167 0381.", reply_markup=markup)
        bot.register_next_step_handler(message, zvonok)
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Сделайте запись кнопкой видеорегистратора.", reply_markup=markup)
        bot.register_next_step_handler(message, dtp)

def zvonok(message):
    
    if "выполнил" in message.text.lower():
        
        bot.send_message(message.chat.id, "Сделайте фото машины с 4х ракурсо. По очереди.")
        bot.register_next_step_handler(message, photo_dtp)
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Сделайте срочный звонок на номер +7 776 167 0381.", reply_markup=markup)
        bot.register_next_step_handler(message, zvonok)


def photo_dtp(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    dtp_check  = Dtp_or_chp.objects.filter(driver__id = driver.id).filter(dtp_date__date = today)[0]
    if message.content_type == 'photo':
        
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/dtp/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)

        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
        dtp_check.dtp_or_chp_photo1 = f"images/dtp/{driver.driver_name}_{today}_{raw}.jpg"
        dtp_check.save()     

        bot.send_message(message.chat.id, "Первое фото получено. Осталось еще три, с других ракурсов.")
        bot.register_next_step_handler(message, photo_dtp2)
    else:
        bot.send_message(message.chat.id, "Сделайте фото машины с 4х ракурсо. По очереди.")
        bot.register_next_step_handler(message, photo_dtp)


def photo_dtp2(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    dtp_check  = Dtp_or_chp.objects.filter(driver__id = driver.id).filter(dtp_date__date = today)[0]
    if message.content_type == 'photo':
        
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/dtp/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)

        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
        dtp_check.dtp_or_chp_photo2 = f"images/dtp/{driver.driver_name}_{today}_{raw}.jpg"
        dtp_check.save()
        bot.send_message(message.chat.id, "Второе фото получено. Осталось еще два, с других ракурсов.")
        bot.register_next_step_handler(message, photo_dtp3)
    else:
        bot.send_message(message.chat.id, "Сделайте второе фото с другого ракурса.")
        bot.register_next_step_handler(message, photo_dtp2)
    
def photo_dtp3(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    dtp_check  = Dtp_or_chp.objects.filter(driver__id = driver.id).filter(dtp_date__date = today)[0]
    if message.content_type == 'photo':
        
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/dtp/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)

        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
        dtp_check.dtp_or_chp_photo3 = f"images/dtp/{driver.driver_name}_{today}_{raw}.jpg"
        dtp_check.save()
        bot.send_message(message.chat.id, "Третье фото получено. Осталось еще одно, с другого ракурса.")
        bot.register_next_step_handler(message, photo_dtp4)
    else:
        bot.send_message(message.chat.id, "Сделайте третье фото с другого ракурса.")
        bot.register_next_step_handler(message, photo_dtp3)

def photo_dtp4(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    dtp_check  = Dtp_or_chp.objects.filter(driver__id = driver.id).filter(dtp_date__date = today)[0]
    if message.content_type == 'photo':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Вернуться")
        markup.add(item1)
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/camera/{driver.driver_name}_{today}_{raw}.jpg"

        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        path = str(pathlib.Path().resolve())
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
            
        dtp_check.dtp_or_chp_photo4 = f"images/camera/{driver.driver_name}_{today}_{raw}.jpg"
        dtp_check.save()
        bot.send_message(message.chat.id, "Четвертое фото получено. Нажмите кнопку 'Вернуться', чтобы вернуться в меню во время поездки.", reply_markup=markup)
        bot.register_next_step_handler(message, poezdka)
    else:
        bot.send_message(message.chat.id, "Сделайте четвертое фото с другого ракурса.")
        bot.register_next_step_handler(message, photo_dtp4)





def dvigatel(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    if "выполнил" in message.text.lower():
        End.objects.create(
            driver=driver,
            car =driver.car,
            engine_stop = True
        )
        bot.send_message(message.chat.id, "Отлично. Теперь сделайте фото одометра.")
        bot.register_next_step_handler(message, photo_odometr1)
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Вы завершаете поездку. Остановили двигатель?")
        bot.register_next_step_handler(message, dvigatel)


def photo_odometr1(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    end_trip  = End.objects.filter(driver__id = driver.id).filter(end_date__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/odometer/{driver.driver_name}_{today}_{raw}.jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)

        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
            
        end_trip.odometer_and_dashboard_readings_data_photo = f"images/odometer/{driver.driver_name}_{today}_{raw}.jpg"
        end_trip.save()
        bot.send_message(message.chat.id, "Фото получено. Введите данные одометра.")
        bot.register_next_step_handler(message, odometr_data1)
    else:
        bot.send_message(message.chat.id, "Отправьте фото одометра.")
        bot.register_next_step_handler(message, photo_odometr1)

def odometr_data1(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    end_trip  = End.objects.filter(driver__id = driver.id).filter(end_date__date = today)[0]
    end_trip.odometer_and_dashboard_readings_data = message.text
    end_trip.save()
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton(u"Выполнил\u2705")
    markup.add(item1)
    bot.send_message(message.chat.id, "Данные одометра получены. Следующее отключите камеру.", reply_markup=markup)
    bot.register_next_step_handler(message, camera_off)

def camera_off(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    end_trip  = End.objects.filter(driver__id = driver.id).filter(end_date__date = today)[0]
    if "выполнил" in message.text.lower():
        end_trip.camera_stop = True
        end_trip.save()
        bot.send_message(message.chat.id, "Отлично, вы отключили камеру. Теперь проверьте камеру и сделайте 4 фото с разных ракурсов по очереди.")
        bot.register_next_step_handler(message, photo_camera1)
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Отключите камеру.")
        bot.register_next_step_handler(message, camera_off)


def photo_camera1(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    end_trip  = End.objects.filter(driver__id = driver.id).filter(end_date__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/camera/{driver.driver_name}_{today}_{raw}.jpg"

        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
        end_trip.camera_check_photo1 = f"images/camera/{driver.driver_name}_{today}_{raw}.jpg"
        end_trip.save()
        bot.send_message(message.chat.id, "Первое фото получено. Сделайте ещё три с других ракурсов.")
        bot.register_next_step_handler(message, photo_camera2)
    else:
        bot.send_message(message.chat.id, "Отправьте первое фото камеры.")
        bot.register_next_step_handler(message, photo_camera1)


def photo_camera2(message):
    
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    end_trip  = End.objects.filter(driver__id = driver.id).filter(end_date__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/camera/{driver.driver_name}_{today}_{raw}.jpg"

        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
        end_trip.camera_check_photo2 = f"images/camera/{driver.driver_name}_{today}_{raw}.jpg"
        end_trip.save()
        bot.send_message(message.chat.id, "Второе фото получено. Сделайте ещё два с других ракурсов.")
        bot.register_next_step_handler(message, photo_camera3)
    else:
        bot.send_message(message.chat.id, "Отправьте второe фото камеры.")
        bot.register_next_step_handler(message, photo_camera2)


def photo_camera3(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    end_trip  = End.objects.filter(driver__id = driver.id).filter(end_date__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/camera/{driver.driver_name}_{today}_{raw}.jpg"

        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
        end_trip.camera_check_photo3 = f"images/camera/{driver.driver_name}_{today}_{raw}.jpg"
        end_trip.save()
        bot.send_message(message.chat.id, "Третье фото получено. Сделайте ещё одно с другого ракурса.")
        bot.register_next_step_handler(message, photo_camera4)
    else:
        bot.send_message(message.chat.id, "Отправьте третье фото камеры.")
        bot.register_next_step_handler(message, photo_camera3)


def photo_camera4(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    end_trip  = End.objects.filter(driver__id = driver.id).filter(end_date__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/camera/{driver.driver_name}_{today}_{raw}.jpg"

        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
        end_trip.camera_check_photo4 = f"images/camera/{driver.driver_name}_{today}_{raw}.jpg"
        end_trip.save()
        bot.send_message(message.chat.id, "Четвертое фото получено. Проверьте конструкцию и сделайте одно фото.")
        bot.register_next_step_handler(message, photo_constr)
    else:
        bot.send_message(message.chat.id, "Отправьте четвертое фото камеры.")
        bot.register_next_step_handler(message, photo_camera4)


def photo_constr(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    end_trip  = End.objects.filter(driver__id = driver.id).filter(end_date__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/construction/{driver.driver_name}_{today}_{raw}.jpg"

        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
        end_trip.construction_check = f"images/construction/{driver.driver_name}_{today}_{raw}.jpg"
        end_trip.save()
        bot.send_message(message.chat.id, "Фото конструкции получено. Теперь наденьте чехол на конструкцию и сделайте фото.")
        bot.register_next_step_handler(message, chehol_constr)
    else:
        bot.send_message(message.chat.id, "Проверьте конструкцию и сделайте одно фото.")
        bot.register_next_step_handler(message, photo_constr)


def chehol_constr(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    end_trip  = End.objects.filter(driver__id = driver.id).filter(end_date__date = today)[0]
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = f"{settings.MEDIA_ROOT}/images/camera/{driver.driver_name}_{today}_{raw}.jpg"

        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
        end_trip.camera_cover = f"images/camera/{driver.driver_name}_{today}_{raw}.jpg"
        end_trip.save()

        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        
  
        bot.send_message(message.chat.id, "Фото получено. Теперь активируйте сигнализацию.", reply_markup=markup)
        bot.register_next_step_handler(message, active_signal)
    
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Теперь наденьте чехол на конструкцию и сфоткайте.")
        bot.register_next_step_handler(message, chehol_constr)


def active_signal(message):
    driver = Driver.objects.get(driver_chat_id = message.chat.id)
    today = str(date.today())
    print("fdskjflkasjl")
    end_trip  = End.objects.filter(driver__id = driver.id).filter(end_date__date = today)[0]
    if "выполнил" in message.text.lower():
        end_trip.alarm_check = True
        end_trip.save()
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Завершить")
        markup.add(item1)
        bot.send_message(message.chat.id, "Отлично. Теперь нажмите кнопку 'Завершить', чтобы завершить поездку.", reply_markup=markup)
        bot.register_next_step_handler(message, end_of_poezdka)
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Выполнил\u2705")
        markup.add(item1)
        bot.send_message(message.chat.id, "Теперь активируйте сигнализацию.", reply_markup=markup)
        bot.register_next_step_handler(message, active_signal)

def end_of_poezdka(message):
    if "завершить" in message.text.lower():
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"/start")
        markup.add(item1)
        bot.send_message(message.chat.id, "Отлично. Вы завершили поездку, чтобы начать поездку нажмите /start.")
        
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton(u"Завершить")
        markup.add(item1)
        bot.send_message(message.chat.id, "Теперь нажмите кнопку 'Завершить', чтобы завершить поездку.", reply_markup=markup)
        bot.register_next_step_handler(message, end_of_poezdka)


bot.infinity_polling()


