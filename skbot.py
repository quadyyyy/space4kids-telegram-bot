import telebot
from telebot import types
import random
from random import choice


bot = telebot.TeleBot('BOT-TOKEN')


spacefacts = ['Солнце в 300 000 раз больше, чем наша планета Земля', 'Солнце полностью проворачивается вокруг своей оси за 25-35 дней', 'Земля, Марс, Меркурий и Венера также называются «внутренними планетами», так как расположены ближе всего к Солнцу',
'Солнце теряет до 1 000 000 тонн своей массы каждую секунду из-за солнечного ветра', 'Меркурий и Венера уникальны тем, что у них отсутствуют какие-либо спутники', 'На Меркурии нет атмосферы, а значит ветра или какой-либо другой погоды',
'Вeнeрa являeтся eдинствeннoй плaнeтoй, кoтoрaя врaщaeтся в прoтивoпoлoжнyю стoрoнy oтнoситeльнo дрyгих плaнeт Сoлнeчнoй систeмы', 'Ио, спутник Юпитера - самое вулканическое место в солнечной системе',
'С тoчки зрeния Тeoрии oтнoситeльнoсти, пoмимo чёрных дыр, дoлжны сyщeствoвaть и бeлыe дыры, хoтя мы eщё нe oбнaрyжили ни oднoй (сyщeствoвaниe чёрных дыр тaкжe пoдвeргaeтся сoмнeнию)',
'Учениые считают, что создать кротовую нору из "Интерстеллара" возможно', 'Аккреционный диск у черной дыры на самом деле синего цвета', 'Планета, у которой больше всего спутников, это Юпитер с 67 спутниками',
'Так как Сатурн обладает низкой плотностью, то если вы его положите в воду, то он поплывёт!', 'Энцeлaд — этo oдин из сaмых мaлeньких спyтникoв Сaтyрнa. Этoт спyтник oтрaжaeт дo 90% сoлнeчнoгo свeтa, чтo прeвoсхoдит дaжe прoцeнт oтрaжeния свeтa oт снeгa!',
'Уран имеет уникальный наклон, из-за которого одна ночь на нём длится, только представьте, 21 год!', 'Плутон (по англ. Pluto) назван в честь римского бога, а не в честь собаки из Диснея, как полагают некоторые',
'Сейчас в Солнечной системе насчитывается 5 карликовых планет: Церера, Плутон, Хаумеа, Эрида и Макемаке', 'Сoвeтский и рoссийский кoсмoнaвт Сeргeй Кoнстaнтинoвич Крикaлёв являeтся рeкoрдсмeнoм пo врeмeни нaхoждeния в кoсмoсe. Eгo рeкoрд дoстигaeт 803 днeй, 9 чaсoв и 39 минyт, чтo эквивaлeнтнo 2.2 лeт!',
'Тoлькo 24 чeлoвeкa видeли нaшy плaнeтy из кoсмoсa. Нo блaгoдaря прoeктy Google Earth, oстaльныe люди бoлee 500 миллиoнoв рaз скaчaли вид Зeмли из кoсмoсa',
'Световой год — это дистанция, которую свет проходит за один год. Это расстояние равно 95 триллионам километров!', 'Если уменьшить Солнце до размеров бактерии, то галактика Млечный Путь будет размер с США',
'В северной части неба вы можете увидеть две галактики — это галактика Андромеды (М31) и галактика Треугольника (М33)', 'Прямо сейчас к нам приближается галактика Андромеда',
'Сaмaя дaлёкaя гaлaктикa, кoтoрyю нaм yдaлoсь oбнaрyжить, нaзывaeтся GRB 090423, кoтoрaя нaхoдится нa рaсстoянии 13.6 миллиaрдoв свeтoвых лeт! Этo oзнaчaeт, чтo свeт,исхoдящий oт нeё, нaчaл свoё пyтeшeствиe всeгo лишь спyстя 600 000 лeт пoслe oбрaзoвaния Всeлeннoй!',
'В кoсмoсe нaсчитывaeтся пoрядкa 2**1023 звёзд. Гoвoря пo-рyсски, этo числo рaвнo 200 000 000 000 000 000 000 000 000 000!', 'Звёзды типа «красный карлик» имеют самую маленькую массу и могут непрерывно сгорать в течение 10 триллионов лет',
'День на Плутоне длится 6 дней и 9 часов', 'В 1895 году Константин Циолковский, один из первых российских ученых-ракетчиков, первым предложил концепцию космических лифтов, типа космической транспортной системы', 'Если звезда пройдет слишком близко к черной дыре, она может быть разорвана на части',
'Галактика Whirlpool (M51) была первым небесным объектом, идентифицированным как спиральный', 'Галактика Млечный Путь имеет ширину 105 700 световых лет', 'Следы, оставленные на Луне, не исчезнут, пока нет ветра',
'Если на Земле вы весите 60кг, то на Марсе вы будете весить 28кг!', 'Закат на Марсе синего цвета', 'Земля-единственная планета, не названная в честь Бога', 'На самом деле никто не знает почему Землю назвали именно так',
'В космосе звезд больше, чем песчинок в мире', 'Всего в 4 световых годах от нас есть планета, на которой может быть жизнь', 'Только 5% Вселенной видно с Земли', 'В любой момент на Земле происходит не менее 2000 гроз', 'Мы знаем больше о Марсе и нашей Луне, чем о наших океанах',
'Mariner 10 был первым космическим кораблем, который посетил Меркурий в 1974 году', 'Астронавты могут вырасти примерно на два дюйма (5 см) в высоту, когда находятся в космосе', 'Пояс Койпера-это область Солнечной системы за орбитой Нептуна',
'Экзопланеты-это планеты, которые вращаются вокруг других звезд', 'Центр Млечного Пути пахнет ромом и на вкус как малина', 'Наша Луна удаляется от Земли со скоростью 4 см в год!', 'МКС видна более чем 90% населения Земли', 
'Слово “астронавт” означает “звездный моряк” в своем происхождении', 'Красное пятно Юпитера уменьшается', 'Юпитер "защищает" Землю от астероидов, притягивая своей гравитацией большинство астероидов', 'День на Меркурии эквивалентен 58 земным дням',
'Шариковые ручки не работают в космосе, поэтому космонавтам выдают карандаши', 'Уже в 240 году до нашей эры китайцы начали документировать появление кометы Галлея', 'Существует планета, полностью состоящая из алмазов', 'Масса Солнца составляет 99.86% от массы всей Солнечной системы, оставшиеся 0.14% приходятся на планеты и астероиды',
'Большинство тяжелых элементов, содержащихся в вашем организме (таких как кальций, железо и углерод), являются побочными продуктами взрыва группы сверхновых звезд, положившего начало формированию Солнечной системы', 'Официальная научная теория гласит, что человек сможет выжить в открытом космосе без скафандра в течение 90 секунд, если немедленно выдохнет весь воздух из легких',
'Главный претендент на звание обитаемой планеты внесолнечной системы, «Супер-Земля» GJ 667Cc, находится на расстоянии всего 22 световых лет от Земли. Однако путешествие до нее займет у нас 13 878 738 000 лет', '«Космическая юла» под названием нейтронная звезда – это самый быстро крутящийся объект во Вселенной, который делает вокруг своей оси до 500 оборотов в секунду. Помимо этого эти космические тела настолько плотные, что одна столовая ложка составляющего их вещества будет весить ~10 млрд. тонн',
'1 плутонианский год длится 248 земных лет. Это означает, что в то время как Плутон делает всего один полный оборот вокруг Солнца, Земля успевает сделать 248', 'Магнитное поле Юпитера настолько мощное, что ежедневно обогащает магнитное поле нашей планеты миллиардами Ватт', 
'Нашей Солнечной системе требуется 230 миллионов лет, чтобы сделать оборот вокруг Млечного Пути', 'Больше чем на 90% вселенная состоит из темной материи', 'На Юпитере и Сатурне идет алмазный дождь',
'Одна из лун Сатурна имеет форму пельменя, потому что она поглощает некоторые из колец Сатурна', 'Самый большой астероид в Солнечной системе имеет диаметр 525 километров', 'На Земле деревьев больше, чем звезд в Млечном Пути',
'Следы лунной посадки, вероятно, все еще будут видны через миллионы лет']


@bot.message_handler(commands=['start']) #стартовая команда
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    #Русский язык
    if message.text == '🇷🇺 Русский':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Российский космос")
        btn2 = types.KeyboardButton('📰 Новости')
        btn3 = types.KeyboardButton('📁 Проекты и мероприятия')
        btn4 = types.KeyboardButton('📚 Знания')
        btn5 = types.KeyboardButton('💻 Навигация профессий')
        btn6 = types.KeyboardButton('👩🏻‍🏫 Учителю')
        btn7 = types.KeyboardButton('🎬 Медиа')
        btn8 = types.KeyboardButton('🔎 Поиск')
        btn9 = types.KeyboardButton('👀 Ты этого точно не знал!')
        btn10 = types.KeyboardButton('🔙 Вернуться к выбору языка')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
        bot.send_message(message.from_user.id, "👋 Вас приветствует бот для сайта Space4Kids", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')

    elif message.text == '🔙 Вернуться к выбору языка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton('🇬🇧 English')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

    elif message.text == '👀 Ты этого точно не знал!':
        bot.send_message(message.from_user.id, random.choice(spacefacts))
        bot.send_message(message.from_user.id, random.choice(spacefacts))
        bot.send_message(message.from_user.id, random.choice(spacefacts))
        bot.send_message(message.from_user.id, random.choice(spacefacts))
        bot.send_message(message.from_user.id, random.choice(spacefacts))
        bot.send_message(message.from_user.id, random.choice(spacefacts))
        bot.send_message(message.from_user.id, random.choice(spacefacts))
        bot.send_message(message.from_user.id, random.choice(spacefacts))
        bot.send_message(message.from_user.id, random.choice(spacefacts))
        bot.send_message(message.from_user.id, random.choice(spacefacts))

    elif message.text == '🇷🇺 Российский космос':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📚 История')
        btn2 = types.KeyboardButton('💻 Техника')
        btn3 = types.KeyboardButton('🚀 Космодромы')
        btn4 = types.KeyboardButton('👨‍🚀 Космонавты')
        btn5 = types.KeyboardButton('👍🏻 Следуй за космонавтом')
        btn6 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    elif message.text == '📚 История':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 История\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/140/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '💻 Техника':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 💻 Техника\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/138/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🚀 Космодромы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🚀 Космодромы\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/139/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '👨‍🚀 Космонавты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 👨‍🚀 Космонавты\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/40/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '👍🏻 Следуй за космонавтом':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 👍🏻 Следуй за космонавтом\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/131/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔙 Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Российский космос")
        btn2 = types.KeyboardButton('📰 Новости')
        btn3 = types.KeyboardButton('📁 Проекты и мероприятия')
        btn4 = types.KeyboardButton('📚 Знания')
        btn5 = types.KeyboardButton('💻 Навигация профессий')
        btn6 = types.KeyboardButton('👩🏻‍🏫 Учителю')
        btn7 = types.KeyboardButton('🎬 Медиа')
        btn8 = types.KeyboardButton('🔎 Поиск')
        btn9 = types.KeyboardButton('👀 Ты этого точно не знал!')
        btn10 = types.KeyboardButton('🔙 Вернуться к выбору языка')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
        bot.send_message(message.from_user.id, "👀 Выбери интересующий раздел", reply_markup=markup)

    elif message.text == '📰 Новости':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📰 Новости\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/101/)', reply_markup=markup, parse_mode='Markdown')
    
    elif message.text == '📁 Проекты и мероприятия':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('🔎 Кванториум')
        btn2 = types.KeyboardButton('🔎 Сириус')
        btn3 = types.KeyboardButton('🔎 Университетская гимнаязия МГУ')
        btn4 = types.KeyboardButton('🔎 Центр космонавтика и авиация')
        btn5 = types.KeyboardButton('🔎 Космический класс')
        btn6 = types.KeyboardButton('🔎 Космические смены')
        btn7 = types.KeyboardButton('🔎 Программа "Универсат"')
        btn8 = types.KeyboardButton('🔎 Cansat Russia')
        btn9 = types.KeyboardButton('🔎 Проект космический урок')
        btn10 = types.KeyboardButton('🔎 World skills Russia')
        btn11 = types.KeyboardButton('🔎 Билет в будующее')
        btn12 = types.KeyboardButton('🔎 ПроеКТОриЯ')
        btn13 = types.KeyboardButton('🔎 Форумная кампания')
        btn14 = types.KeyboardButton('🔎 Космофест Восточный')
        btn15 = types.KeyboardButton('🔎 КосмоСтарт')
        btn16 = types.KeyboardButton('🔎 Олимпиада НТИ')
        btn17 = types.KeyboardButton('🔎 Дежурный по планете')
        btn18 = types.KeyboardButton('🔎 Космический рейс')
        btn19 = types.KeyboardButton('🔎 Nauka 0+')
        btn20 = types.KeyboardButton('🔎 Профстажировка.рф 2.0')
        btn21 = types.KeyboardButton('🔎 Неделя без турникетов')
        btn22 = types.KeyboardButton('🔎 Космос')
        btn23 = types.KeyboardButton('🔎 Самбо в школу')
        btn24 = types.KeyboardButton('🔎 Лунная одиссея')
        btn25 = types.KeyboardButton('🔎 Большая перемена')
        markup.add(btn01, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19,
        btn20, btn21, btn22, btn23, btn24, btn25)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    elif message.text == '🔎 Кванториум':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Кванториум\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/473/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Сириус':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Сириус\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/474/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Университетская гимназия МГУ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Университетская гимназия МГУ\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/475/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Центр космонавтика и авиация':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Университетская гимназия МГУ\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/117/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Космический класс':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Космический класс\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/477/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Космические смены':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Космические смены\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/478/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Программа "Универсат"':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Программа "Универсат"\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/482/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Cansat Russia':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Cansat Russia\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/479/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Проект космический урок':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Проект космический урок\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/490/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 World skills Russia':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 World skills Russia\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/476/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Билет в будующее':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Билет в будующее\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/486/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 ПроеКТОриЯ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 ПроеКТОриЯ\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/480/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Форумная кампания':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Форумная кампания\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/487/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Космофест Восточный':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Космофест Восточный\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/483/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 КосмоСтарт':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 КосмоСтарт\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/484/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Олимпиада НТИ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Олимпиада НТИ\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/485/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Дежурный по планете':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Дежурный по планете\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/488/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Nauka 0+':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Nauka 0+\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/576/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Профстажировка.рф 2.0':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Профстажировка.рф 2.0\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/481/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Неделя без турникетов':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Неделя без турникетов\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/573/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Космос':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Космос\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/489/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Самбо в школу':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Самбо в школу\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/491/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Лунная одиссея':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Лунная одиссея\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/1186/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Большая перемена':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🔎 Большая перемена\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/1714/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Знания':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('📚 Лекции')
        btn2 = types.KeyboardButton('📚 Книги')
        btn3 = types.KeyboardButton('📚 Документальные фильмы')
        btn4 = types.KeyboardButton('📚 Телепередачи')
        btn5 = types.KeyboardButton('📚 Художественные фильмы')
        btn6 = types.KeyboardButton('📚 Мультфильмы')
        btn7 = types.KeyboardButton('📚 Доступно о космосе')
        btn8 = types.KeyboardButton('📚 Журналы')
        markup.add(btn01, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)
    
    elif message.text == '📚 Лекции':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 Лекции\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/118/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Книги':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 Книги\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/127/)', reply_markup=markup, parse_mode='Markdown')
    
    elif message.text == '📚 Документальные фильмы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 Документальные фильмы\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/126/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Телепередачи':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 Телепередачи\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/128/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Художественные фильмы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 Художественные фильмы\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/656/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Мультфильмы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 Мультфильмы\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/1753/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Доступно о космосе':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 Доступно о космосе\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/125/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Журналы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 Журналы\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/980/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '💻 Навигация профессий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton("🛠 Каталог профессий")
        btn2 = types.KeyboardButton('🛠 Образовательные организации')
        btn3 = types.KeyboardButton('🛠 Организации госкорпарации "Роскосмос"')
        btn4 = types.KeyboardButton('🛠 Профориентационное тестирование')
        markup.add(btn01, btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    elif message.text == '🛠 Каталог профессий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🛠 Каталог профессий\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/108/)', reply_markup=markup, parse_mode='Markdown')
    
    elif message.text == '🛠 Образовательные организации':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🛠 Образовательные организации\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/110/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🛠 Организации госкорпарации "Роскосмос"':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🛠 Организации госкорпарации "Роскосмос"\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/950/)', reply_markup=markup, parse_mode='Markdown')
    
    elif message.text == '🛠 Профориентационное тестирование':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 🛠 Профориентационное тестирование\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/112/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '👩🏻‍🏫 Учителю':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('📚 Концепция программ "Космический класс"')
        btn2 = types.KeyboardButton('📚 Методические материалы')
        btn3 = types.KeyboardButton('📚 Музеи и центры просвещения')
        btn4 = types.KeyboardButton('📚 Олимпиады и конкурсы')
        btn5 = types.KeyboardButton('📚 Проектная деятельность')
        btn6 = types.KeyboardButton('📚 Уроки и эксперименты')
        btn7 = types.KeyboardButton('📚 Плакаты и постеры')
        markup.add(btn01, btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    elif message.text == '📚 Концепция программ "Космический класс"':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 Концепция программ "Космический класс"\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/120/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Методические материалы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 Методические материалы\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/121/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Музеи и центры просвещения':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 Музеи и центры просвещения\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/122/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Олимпиады и конкурсы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 Олимпиады и конкурсы\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/124/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Проектная деятельность':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 Проектная деятельность\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/880/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Уроки и эксперименты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 Уроки и эксперименты\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/881/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Плакаты и постеры':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📚 Плакаты и постеры\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/1707/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🎬 Медиа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('📷 Фото')
        btn2 = types.KeyboardButton('📷 Видео')
        btn3 = types.KeyboardButton('📷 Интерактив')
        markup.add(btn01, btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    #🔎 Поиск
    elif message.text == '🔎 Поиск':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, '📲 Чтобы перейти к поиску перейди по [ссылке](https://space4kids.ru/search/)', reply_markup=markup, parse_mode='Markdown')

    #Small talk
    elif message.text == 'Привет!':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'привет!':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'как дела?':
        bot.send_message(message.from_user.id, 'Хорошо!')

    elif message.text == 'Как дела?':
        bot.send_message(message.from_user.id, 'Хорошо!')

    elif message.text == 'Что делаешь?':
        bot.send_message(message.from_user.id, 'Помогаю людям!')

    elif message.text == 'что делаешь?':
        bot.send_message(message.from_user.id, 'Помогаю людям!')

    elif message.text == 'как дела':
        bot.send_message(message.from_user.id, 'Хорошо!')
    
    
    #English Language
    elif message.text == '🇬🇧 English':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Russian space")
        btn2 = types.KeyboardButton('📰 News')
        btn3 = types.KeyboardButton('📁 Projects and activities')
        btn4 = types.KeyboardButton('📚 Knowledge')
        btn5 = types.KeyboardButton('💻 Navigation of jobs')
        btn6 = types.KeyboardButton('👩🏻‍🏫 For teachears')
        btn7 = types.KeyboardButton('🎬 Media content')
        btn8 = types.KeyboardButton('🔙 Back to language selection')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, '👋 You are welcomed by the bot for the Space4Kids website', reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Select the section you are interested in')

    elif message.text == '🔙 Back to language selection':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton('🇬🇧 English')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

    elif message.text == '🇷🇺 Russian space':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Your section: 🇷🇺 Russian space\n \n👍🏻 What a good choice!\n \n📲 You can go to the section by following the' + ' [link](https://space4kids.ru/102/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔙 Main menu':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Russian space")
        btn2 = types.KeyboardButton('📰 News')
        btn3 = types.KeyboardButton('📁 Projects and activities')
        btn4 = types.KeyboardButton('📚 Knowledge')
        btn5 = types.KeyboardButton('💻 Navigation of jobs')
        btn6 = types.KeyboardButton('👩🏻‍🏫 For teachears')
        btn7 = types.KeyboardButton('🎬 Media content')
        btn8 = types.KeyboardButton('🔎 Search')
        btn8 = types.KeyboardButton('🔙 Back to language selection')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, '👀 Select the section you are interested in', reply_markup=markup)

    elif message.text == '📰 News':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Your section: 📰 News\n \n👍🏻 What a good choice!\n \n📲 You can go to the section by following the' + ' [link](https://space4kids.ru/101/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📁 Projects and activities':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Your section: 📁 Projects and activities\n \n👍🏻 What a good choice!\n \n📲 You can go to the section by following the' + ' [link](https://space4kids.ru/103/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Knowledge':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Your section: 📚 Knowledge\n \n👍🏻 What a good choice!\n \n📲 You can go to the section by following the' + ' [link](https://space4kids.ru/104/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '💻 Navigation of jobs':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Your section: 💻 Navigation of jobs\n \n👍🏻 What a good choice!\n \n📲 You can go to the section by following the' + ' [link](https://space4kids.ru/105/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '👩🏻‍🏫 For teachears':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Your section: 👩🏻‍🏫 For teachears\n \n👍🏻 What a good choice!\n \n📲 You can go to the section by following the' + ' [link](https://space4kids.ru/106/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🎬 Media content':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Your section: 🎬 Media content\n \n👍🏻 What a good choice!\n \n📲 You can go to the section by following the' + ' [link](https://space4kids.ru/107/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔎 Search':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        bot.send_message(message.from_user.id, '📲 To go to the search, follow the ' + '[link](https://space4kids.ru/search/)', reply_markup=markup, parse_mode='Markdown')




bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть