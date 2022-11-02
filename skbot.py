import telebot
from telebot import types
import random
from random import choice
import menu


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
# Стартовое меню, выбор языка
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    send_message = (f'<b>Привет {message.from_user.first_name} {message.from_user.last_name} 🇷🇺 Выберите язык / 🇬🇧 Choose your language')
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    final_message = "" # Переменная для финального сообщения после обработки
    # get_message_bot = message.text.strip().lower() # Считывает ввод в нижнем регистре

# Стартовое меню для RU
    if message.text == '🇷🇺 Русский':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
        markup.add(*main_menu.values())
        bot.send_message(message.from_user.id, "👋 Вас приветствует бот для сайта Space4Kids", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')

# Возврат к выбору языка
    elif message.text == '🔙 Вернуться к выбору языка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton('🇬🇧 English')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

# Переход в главное меню
    elif message.text == '🔙 Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
        markup.add(*main_menu.values())
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')

# Случайные факты
    elif message.text == '👀 Ты этого точно не знал!':
        for _i in range(10):
            bot.send_message(message.from_user.id, random.choice(spacefacts))

# Меню "Российский космос"
    elif message.text == '🇷🇺 Российский космос':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*menu.russian_space.values(), main_button)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

# Подменю "Российский космос"
    elif message.text in menu.russian_space_sub:
        markup = types.InlineKeyboardMarkup()
        final_message = menu.russian_space_sub[message.text], reply_markup=markup, parse_mode='Markdown'

# Новости
    elif message.text == '📰 Новости':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Твой раздел: 📰 Новости\n \n👍🏻 Хороший выбор\n \n📲 Перейти к разделу можно по' + ' [ссылке](https://space4kids.ru/101/)', reply_markup=markup, parse_mode='Markdown')

# Меню "Проекты и мероприятия"
    elif message.text == '📁 Проекты и мероприятия':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*menu.projects.values(), main_button)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

# Подменю "Проекты и мероприятия"
    elif message.text in menu.projects_sub:
        markup = types.InlineKeyboardMarkup()
        final_message = menu.projects_sub[message.text], reply_markup=markup, parse_mode='Markdown'

# Меню "Знания"
    elif message.text == '📚 Знания':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*menu.knowledge.values(), main_button)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

# Подменю "Знания и мероприятия"
    elif message.text in menu.knowledge_sub:
        markup = types.InlineKeyboardMarkup()
        final_message = menu.knowledge_sub[message.text], reply_markup=markup, parse_mode='Markdown'

# Меню "Навигация профессий"
    elif message.text == '💻 Навигация профессий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*menu.profession.values(), main_button)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

# Подменю "Навигация профессий"
    elif message.text in menu.profession_sub:
        markup = types.InlineKeyboardMarkup()
        final_message = menu.profession_sub[message.text], reply_markup=markup, parse_mode='Markdown'
   
# Меню "Учителю"
    elif message.text == '👩🏻‍🏫 Учителю':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(*menu.teacher.values(), main_button)
            bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

# Подменю "Учителю"
    elif message.text in menu.teacher_sub:
        markup = types.InlineKeyboardMarkup()
        final_message = menu.teacher_sub[message.text], reply_markup=markup, parse_mode='Markdown'

# Меню "Медиа"
    elif message.text == '🎬 Медиа':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(*menu.media.values(), main_button)
            bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    #🔎 Поиск
    elif message.text == '🔎 Поиск':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, '📲 Чтобы перейти к поиску перейди по [ссылке](https://space4kids.ru/search/)', reply_markup=markup, parse_mode='Markdown')

    #Small talk
    elif message.text.lower() == 'привет!' or message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text.lower() == 'что делаешь?':
        bot.send_message(message.from_user.id, 'Помогаю людям!')

    elif message.text.lower() == 'как дела?' or message.text.lower() == 'как дела':
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