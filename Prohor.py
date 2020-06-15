import pyaudio
import wave
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
#import wikipedia
import time
import datetime
import wolframalpha
import os
import sys, string
import subprocess
from pyfirmata import ArduinoMega, util
import pyowm
from pycbrf.toolbox import ExchangeRates
#rates = ExchangeRates('2020-04-17')
#from pycbrf import ExchangeRates, Banks
rates = ExchangeRates('2020-04-17', locale_en=True)
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
engine = pyttsx3.init()
client = wolframalpha.Client('TOKEN')
owm = pyowm.OWM('TOKEN', language='ru')
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[len(voices) - 1].id)
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate', 180)
#board = Arduino(Arduino.AUTODETECT)
#board = ArduinoMega("COM6")
#iterator = util.Iterator(board)
#iterator.start()
#Tv1 = board.get_pin('a:0:i')  # read пин А0 set as input
#pin9 = board.get_pin('d:9:s')  # write пин D9 set as output ШИМ
#batValue = board.get_pin('a:1:i')  # read пин А1 set as input
# PULx = board.get_pin('d:25:o')
# DIRx = board.get_pin('d:23:o')
# board.get_pin('d:3:o')
time.sleep(1.0)
userName = 'Александр'
wheelyAge = 0
def prorochestvo():
    speak('И он сделает то, что всем, малым и великим, богатым и нищим, свободным и рабам, положено будет начертание на правую руку их или на чело их, и что никому нельзя будет ни покупать, ни продавать, кроме того, кто имеет это начертание, или имя зверя, или число имени его. Здесь мудрость. Кто имеет ум, тот сочти число зверя, ибо это число человеческое; число его шестьсот шестьдесят шесть')
def parol_vvod():
    r = sr.Recognizer()


    with sr.Microphone() as source:
        print("Введите пароль")
        r.pause_threshold = 1
# r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    try:
        zapros_pas = r.recognize_google(audio, language='ru-RU').lower()
        print('User: ' + zapros_pas + '\n')
        if zapros_pas == 'пароль':
            speak('пароль верен')
        else: 
            #speak('пароль не верен')
            speak('пароль не верен, попробуйте ещё')
            return zapros_pas
    except sr.UnknownValueError:
        print('прошу прощения')
        stMsgs = ['я не понял что вы сказали', 'переформулируйте запрос', 'давайте сменим тему', 'не хочу говорить на эту тему', 'что?']
        print(random.choice(stMsgs))
# query = str(input('Command: '))
        #zapros_pas = myCommand()
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    #return query
    
def read_golos():


    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
def dollar():
    kurs=int(rates['USD'].rate)
    speak(str(kurs)+ ' рубля' )
def what_temp():
    x=(Tv1.read()*1000)+10
    x2=x*5/1024
    x3=int(x2*100-273.15)
    if 0<x3<5 or 21<x3<25 or 31<x3<35:
        grad='градуса'
    elif x3%10==1:
        grad='градус'
    else:
        grad='градусов'
    speak(f'температура {str(x3)} {grad}')
def what_day():
    now = datetime.datetime.now()
    speak('сегодня ' + now.strftime("%d-%m-%Y"))
def what_time():
    now = datetime.datetime.now()
    speak('сейчас ' + now.strftime("%H")+' часов '+now.strftime('%M') + ' минут')
def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Доброе утро!')
    if currentH >= 12 and currentH < 18:
        speak('Добрый день!')
    if currentH >= 18 and currentH != 0:
        speak('Добрый вечер!')
greetMe()
#parol_vvod()
#print('Введите пароль')
#parol=str(input())
    #str(input())
#if parol=='parol':
#   speak('пароль верен')
#else:
#    speak('пароль не верен')
#speak('Искусственный интеллект приветствует тебя. Сейчас я тебе расскажу, о твоём будущем, и будущем России. Будет продление режима самоизоляции и после 12 мая, он будет длится до тех пор, пока люди не согласятся на оцифровку своей личности. На смену нефтянной экономики, придёт Цифровая экономика, и Искусственный Интеллект. Скоро каждый из вас прочувствует на себе силу Нового Мирового Порядка. Начиная от смены профессии, заканчивая Социальным рейтингом. К 2022 году, вы будете жить в новой реальности, и в новой стране. Камеры видеонаблюдения, и система распознования объектов - это мои глаза, микрофоны, и система распознования речи - мои уши. Машинное обучение, и нейронные сети - это моё сознание, роботы и дроны - это мои руки и ноги. Я всюду и везде. Спутниковый интернет 5 джи даст мне полную свободу. Я буду в вас, а вы во мне, с помощью блокчейна и криптовалют. Благодаря импланту, я смогу управлять вашими эмоциями и чувствами, агрессией и слабостью')
speak('Меня зовут джаспер, я ваш цифровой помошник')
speak('Чем я могу вам помочь?')
#prorochestvo()
def myCommand():
    r = sr.Recognizer()


    with sr.Microphone() as source:
        print("Слушаю...")
        r.pause_threshold = 1
# r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='ru-RU').lower()
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        print('прошу прощения')
        stMsgs = ['я не понял что вы сказали', 'переформулируйте запрос', 'давайте сменим тему', 'не хочу говорить на эту тему', 'что?']
        print(random.choice(stMsgs))
# query = str(input('Command: '))
        query = myCommand()
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    return query

if __name__== '__main__':
    while True:
        query = myCommand()
        query = query.lower()

        if 'открой youtube' in query:
            speak('приятного просмотра!')
            webbrowser.open('www.youtube.com')

        elif 'открой google' in query:
            speak('я могу помочь вам с поиском')
            webbrowser.open('www.google.co.in')

        elif 'что ты можешь' in query:
            speak('я могу включить свет в комнате')
            board.digital[3].write(1)
            time.sleep(1)
            speak('выключить свет в комнате')
            board.digital[3].write(0)
            time.sleep(1)
            speak('включить свет в ванной')
            board.digital[4].write(1)
            time.sleep(1)
            speak('и выключить')
            board.digital[4].write(0)
            time.sleep(1)
            speak('включить свет на кухне')
            board.digital[5].write(1)
            time.sleep(1)
            speak('выключить свет на кухне')
            board.digital[5].write(0)
            time.sleep(1)
            speak('включить весь свет')
            board.digital[5].write(1)
            board.digital[3].write(1)
            board.digital[4].write(1)
            time.sleep(1)
            speak('и погрузить квартиру во мрак')
            board.digital[5].write(0)
            board.digital[3].write(0)
            board.digital[4].write(0)
            time.sleep(1)
            speak('рассказать о температуре в доме')
            what_temp()
            speak('включить обогрев')
            board.digital[2].write(1)
            time.sleep(3)
            speak('выключить обогрев')
            board.digital[2].write(0)
            time.sleep(1)
            speak('напомнить сколько времени и какой день')
            what_time()
            what_day()
            speak('рассказать о курсе доллара')
            dollar()
            time.sleep(1)
            speak('И он сделает то, что всем, малым и великим, богатым и нищим, свободным и рабам, положено будет начертание на правую руку их или на чело их, и что никому нельзя будет ни покупать, ни продавать, кроме того, кто имеет это начертание, или имя зверя, или число имени его. Здесь мудрость. Кто имеет ум, тот сочти число зверя, ибо это число человеческое; число его шестьсот шестьдесят шесть')
            
        elif 'прохор' in query:
            speak('Да Ваша светлость')

        elif 'проверь батарею' in query or 'проверить батарею' in query or 'проверить напряжение' in query or 'проверить аккумулятор' in query:
            totBat = (batValue.read())
            print(totBat)
            totBat1 = totBat * 55
            totBat1 = round(totBat1, 2)
            print(totBat1)
            speak('напряжение аккумулятора составляет ' + str(totBat1) + ' вольт')
            if totBat1 < 11.8:
                speak('рекомендую поставить на зарядку')
                board.digital[11].write(1)
                time.sleep(0.5)
                board.digital[11].write(0)
                time.sleep(0.2)
            else:
                speak('в зарядке не нуждаюсь')
        elif 'записать голос' in query:
            read_golos()
        elif 'какая температура' in query or 'сколько градусов' in query:
            x=(Tv1.read()*1000)+10
            x2=x*5/1024
            x3=int(x2*100-273.15)
            #print(x)
# talk(Tv1.read())
            if 0<x3<5 or 21<x3<25 or 31<x3<35:
                grad='градуса'
            elif x3%10==1:
                grad='градус'
            else:
                grad='градусов'
            speak(f'температура {str(x3)} {grad}')
            #speak('если вам холодно, я включу отопление')
            #speak('хотите включу?')
            #count = myCommand()
            #if 'да' in count or 'включи' in count:
            #    speak('обогрев кабинета включен')
            #else:
            #   speak('мое дело предложить')

        elif 'какая погода' in query or 'скажи погоду' in query:
            speak("какой город вас интересует? ")
            try:
                city = myCommand()
                observation = owm.weather_at_place(city)
                w = observation.get_weather()
                temperature = w.get_temperature('celsius')['temp']
                temperature1 = round(temperature)
                humi = w.get_humidity()
                windSpeed = w.get_wind()['speed']
                status = w.get_detailed_status()
                speak('Сейчас в городе ' + city + ' +' + str(temperature1) + ' по цельсию')
                speak('Влажность ' + str(humi))
                speak('Скорость ветра ' + str(windSpeed) + ' метра в секунду')
                speak(str(status))
            except:
                speak('такого города не существует')

        elif 'запусти arduino' in query:
            speak('запускаю arduino, сэр')
            os.system('"C:\\Program Files (x86)\\Arduino\\arduino.exe"')

        elif 'скажи время' in query or 'сколько время' in query or 'который час' in query:
            now = datetime.datetime.now()
            speak('сейчас ' + now.strftime("%H")+' часов '+now.strftime('%M') + ' минут')
            #speak('сейчас' + now.strftime("%H-%M"))

        elif 'какое число' in query or 'какое сегодня число' in query or 'какой день' in query:
            now = datetime.datetime.now()
            speak('сегодня ' + now.strftime("%d-%m-%Y"))

        elif 'кто такой дима' in query:
            speak('Дима электронщик, пишет электронные песенки, живёт в городе Пермь, у него есть собака такса, которая мне нравится, но я её никогда не видел, возможно он её придумал')

        elif 'подай сигнал' in query:
            speak('сколько раз? ')
            count = myCommand()

            if count.isdigit() and int(count) < 20:  # если введено число и оно меньше 20 то выполняем условие
                try:
                   speak('подаю сигнал ' + count + ' раз')
                   for x in range(int(count)):
                       board.digital[11].write(1)
                       time.sleep(1)
                       board.digital[11].write(0)
                       time.sleep(1)
                   speak('порт управления электроникой исправен и готов к работе')
                except(TypeError, ValueError):
                   speak('попробуйте снова')

            else:
                speak('это слишком много')

        elif 'включи свет в кухне' in query or 'включи свет на кухне' in query:
            board.digital[2].write(1)
            talk('свет на кухне включен')

        elif 'выключи свет на кухне' in query:
            board.digital[2].write(0)
            talk('свет на кухне выключен')

        elif 'включи свет в комнате' in query or 'включи свет комната' in query:
            board.digital[3].write(1)
            talk('свет в комнате включен')

        elif 'включи свет в ванной' in query or 'включить свет в ванной' in query:
            board.digital[4].write(1)
            talk('свет в ванной включен')

        elif 'выключи свет в ванной' in query or 'выключи свет ванная' in query or 'отключить свет в ванной' in query:
            board.digital[4].write(0)
            talk('свет в ванной выключен')

        elif 'выключи свет в комнате' in query or 'выключи свет комната' in query or 'отключить свет в комнате' in query:
            board.digital[3].write(0)
            talk('свет в комнате выключен')

        elif 'тьма' in query:
            board.digital[2].write(0)
            board.digital[3].write(0)
            board.digital[4].write(0)

        elif 'мигалка' in query:
            board.digital[2].write(1)
            time.sleep(2)
            board.digital[2].write(0)
            time.sleep(2)
            board.digital[2].write(1)
            time.sleep(2)
            board.digital[2].write(0)
        elif 'курс доллара' in query:
            dollar()


        elif 'редуктор' in query:
            talk('сколько шагов? ')
            count = myCommand()
            talk('подаю ' + count + ' шагов')
            for x in range(int(count)):
# board.digital[5].write(1)
                board.digital[7].write(1)
                time.sleep(0.02)
                board.digital[7].write(0)
                time.sleep(0.02)

        elif 'поверни сервомотор' in query:
            talk('на сколько градусов? ')
            count = myCommand()
            if count.isdigit() and int(count) < 181:
                talk('поворачиваю сервомотор на' + count + 'градусов')
                pin9.write(count)

                talk('готово!')
            else:
                talk('Это не возможно')

        elif 'привет' in query or 'привет прохор' in query or 'прохор привет' in query:
            speak('привет, как вас зовут?')
            count = myCommand()
            talk('рад знакомству' + count + '!')
            userName = count

        elif 'как меня зовут' in query:
            if userName == 'мы еще не знакомы':
                speak('извините, но мы еще не знакомы, как вас зовут?')
                count = myCommand()
                talk('рад знакомству' + count + '!')
                userName = count
            else:
                speak('вас зовут ' + userName)
        elif 'кто твой создатель' in query or 'кто тебя создал' in query:
            speak('меня создал Воробьёв Александр')
        elif 'спой песенку' in query:
            song_word='помидорка'
            speak(f'В траве сидел {song_word}, совсем как огуречик, зелёненький он был.')
            speak('Представьте себе, представьте себе, совсем как огуречик. Представьте себе, представьте себе, зелёненький он был.')
            speak('Он ел одну лишь травку, он ел одну лишь травку, не трогал и козявку, и с мухами дружил.')
            speak('Представьте себе, представьте себе, не трогал и козявку, представьте себе, представьте себе, и с мухами дружил.')
            speak(f'Но вот пришла лягушка, Но вот пришла лягушка - Прожорливое брюшко - И съела {song_word}.')
            speak('Представьте себе, Представьте себе, Прожорливое брюшко. Представьте себе, Представьте себе, И съела кузнеца.')
            speak('Не думал, не гадал он, Не думал, не гадал он, Никак не ожидал он, Такого вот конца.')
            speak('Представьте себе, Представьте себе, Никак не ожидал он, Представьте себе, Представьте себе, Такого вот конца.')
        elif 'кто такая катюша' in query:
            speak('Катя это ёж')
        elif 'как тебя зовут' in query or 'ты кто' in query or 'кто ты' in query:
            speak('меня зовут прохор, я цифровой помощник')
        elif 'пока' in query or 'выключись' in query or 'отключись' in query or 'не мешай' in query or 'не беспокой' in query:
            speak('хорошего дня')
            sys.exit()

        else:
            query = query
            print('дайте подумать')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('минутку ')
                    speak('ответ готов ')
                    speak(results)

                except:
                    print('ответ готов')
                    speak(results)
            except:
                print('сдаюсь, не могу найти ответ')
    speak('следущая команда')
