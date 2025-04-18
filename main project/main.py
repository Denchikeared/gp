import telebot
import random
from telebot import types
from bot_logic import gen_pass, gen_emodji, flip_coin  # Импортируем функции из bot_logic

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7752025522:AAEcm1qg32ENHvw4TOf7XwT9KDCSP2oa_RM")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот👍. Напиши команду /about_danger чтобы узнать об опасности глобального потепления🤔, /how_to_solve чтобы узнать как решить проблему✌️, /advice чтобы получить памятку😁, /ques_and_answ чтобы узнать ответы на часто задаваемые вопросы🤨, /story чтобы услышать занимательные истории про глобальное потепление😮, /bye чтобы попрощаться👋")


@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи! 😎")
    imgbye = ["images/gb.jpg"]
    selimgbye = random.choice(imgbye)

    with open(selimgbye, 'rb') as photo:
        # Отправляем фото
        bot.send_photo(message.chat.id, photo)
        return


@bot.message_handler(commands=['about_danger'])
def send_image(message):
    img = ["images/368539.jpg", "images/ew.jpg", "images/sfg.jpg", "images/sgsrgr.jpg", "images/sgw.jpg", "images/we.jpg", "images/images (1).jpg", "images/images (2).jpg", "images/images (3).jpg", "", "images/images (4).jpg","images/images (5).jpg","images/za.jpg","images/zb.jpg","images/zc.jpg"]
    selimg = random.choice(img)

    txtext = ["Повышение уровня моря: Таяние ледников и полярных льдов приводит к повышению уровня мирового океана, что угрожает прибрежным городам и островным государствам затоплением.", " Экстремальные погодные условия: Глобальное потепление усиливает частоту и интенсивность экстремальных погодных явлений, таких как засухи, наводнения, штормы и ураганы.", "Нарушение экосистем: Изменение климата нарушает биоразнообразие, приводя к исчезновению видов животных и растений, особенно тех, кто обитает в чувствительных к температуре средах (например, коралловые рифы).", "Опустынивание: Увеличение температуры и снижение осадков приводят к расширению пустынь и ухудшению условий для сельского хозяйства во многих регионах мира.", "Опустынивание: Увеличение температуры и снижение осадков приводят к расширению пустынь и ухудшению условий для сельского хозяйства во многих регионах мира.", "Угрозы здоровью человека: Рост температур способствует распространению инфекционных заболеваний, переносимых насекомыми, таких как малярия и лихорадка денге.", "Экономические потери: Ущерб от природных катастроф, вызванных изменением климата, требует значительных затрат на восстановление инфраструктуры и поддержку пострадавших регионов.", "Миграция населения: Экологические катастрофы вынуждают людей покидать свои дома, создавая потоки беженцев и увеличивая социальное напряжение.", "Риски для водных ресурсов: Потепление климата приводит к уменьшению запасов пресной воды, особенно в горных районах, где тают ледники.", "Кислотность океанов: Увеличение содержания углекислого газа в атмосфере ведёт к увеличению кислотности океанов, что разрушительно воздействует на морские экосистемы."]
    seltxt = random.choice(txtext)

    with open(selimg, 'rb') as photo:
        # Отправляем сообщение
        bot.send_message(message.chat.id, seltxt)
        # Отправляем фото
        bot.send_photo(message.chat.id, photo)
        return
    
@bot.message_handler(commands=['how_to_solve'])
def send_image(message):
    img = ["images/368539.jpg", "images/ew.jpg", "images/sfg.jpg", "images/sgsrgr.jpg", "images/sgw.jpg", "images/we.jpg", "images/images (1).jpg", "images/images (2).jpg", "images/images (3).jpg", "", "images/images (4).jpg","images/images (5).jpg","images/za.jpg","images/zb.jpg","images/zc.jpg"]
    selimg = random.choice(img)

    totxtext = ["Снижение выбросов CO₂. Сокращение выбросов углекислого газа является ключевым направлением борьбы с глобальным потеплением. Это включает переход на возобновляемые источники энергии, такие как солнечная, ветровая и гидроэнергетика, а также повышение энергоэффективности зданий и транспорта.", "Переход на экологически чистый транспорт. Развитие общественного транспорта, электромобилей и велосипедной инфраструктуры поможет снизить выбросы от транспортных средств. Электромобили и гибридные автомобили становятся всё более доступными и эффективными.", "Развитие возобновляемой энергетики. Инвестиции в солнечные панели, ветровые турбины и другие формы чистой энергии помогут уменьшить зависимость от ископаемого топлива. Правительства могут стимулировать развитие таких технологий через субсидии и налоговые льготы.", "Охрана лесов и лесовосстановлени. Леса играют важную роль в поглощении углекислого газа. Защита существующих лесных массивов и посадка новых деревьев могут значительно способствовать смягчению последствий изменения климата.", "Устойчивое сельское хозяйство. Переход к методам земледелия, снижающим выбросы парниковых газов, таким как органическое фермерство и агролесоводство, помогает сохранить почву и улучшить её способность удерживать углерод.", "Энергоэффективность в зданиях. Улучшение теплоизоляции домов, использование энергосберегающих приборов и внедрение умных систем управления энергопотреблением снижают количество потребляемого электричества и тепла.", "Международное сотрудничество. Важную роль играет заключение международных соглашений, таких как Парижское соглашение по климату, которое направлено на ограничение роста глобальной средней температуры.", "Образование и информирование. Повышение осведомлённости общества о последствиях изменения климата и способах их предотвращения может мотивировать людей менять своё поведение и поддерживать экологически устойчивые практики.", "Инновационные технологии. Разработка и внедрение новых технологий, таких как улавливание и хранение углекислого газа (CCS), могут помочь сократить выбросы промышленных предприятий.", "Поддержка научных исследований. Продолжающиеся исследования в области изменения климата и разработки адаптационных стратегий необходимы для лучшего понимания проблемы и поиска эффективных решений."]
    toseltxt = random.choice(totxtext)

    with open(selimg, 'rb') as photo:
        # Отправляем сообщение
        bot.send_message(message.chat.id, toseltxt)
        # Отправляем фото
        bot.send_photo(message.chat.id, photo)
        return
@bot.message_handler(commands=['advice'])
def send_image(message):
    imgtr = ["images/ec1.jpg", "images/ec2.jpg", "images/ec3.jpg", "images/ec4.jpg", "images/ec5.jpg"]
    selimgtr = random.choice(imgtr)

    with open(selimgtr, 'rb') as photo:
        # Отправляем фото
        bot.send_photo(message.chat.id, photo)
        return

@bot.message_handler(commands=['ques_and_answ'])
def send_image(message):

    totxtextt = ["Что такое глобальное потепление? Ответ: Глобальное потепление — это долгосрочное повышение средней температуры атмосферы Земли и мирового океана, вызванное увеличением концентрации парниковых газов в атмосфере, таких как углекислый газ (CO₂), метан и другие. Этот процесс приводит к изменению климата и имеет серьезные последствия для природы и человечества.","Каковы основные причины глобального потепления? Ответ: Основные причины глобального потепления связаны с деятельностью человека, особенно сжиганием ископаемого топлива (уголь, нефть, газ), вырубкой лесов и промышленными выбросами. Эти процессы увеличивают концентрацию парниковых газов в атмосфере, что усиливает парниковый эффект и ведет к повышению температуры планеты.","Какие последствия глобального потепления мы уже видим? Ответ: Последствия включают: Повышение уровня моря из-за таяния ледников, Увеличение частоты экстремальных погодных явлений (засухи, наводнения, штормы), Изменение экосистем и исчезновение видов животных и растений, Ухудшение качества воздуха и увеличение числа заболеваний, связанных с жарой.","Можно ли остановить глобальное потепление? Ответ: Остановить полностью уже произошедшие изменения сложно, но замедлить темпы потепления возможно. Для этого нужно значительно сократить выбросы парниковых газов, перейти на возобновляемые источники энергии, восстановить леса и внедрить технологии улавливания и хранения CO₂.","Какая роль лесов в борьбе с глобальным потеплением? Ответ: Леса играют ключевую роль в поглощении углекислого газа из атмосферы, выступая легкими планеты. Вырубка лесов уменьшает эту способность и увеличивает выбросы CO₂. Поэтому защита и восстановление лесных массивов являются важными шагами в борьбе с изменением климата.","Почему важно сокращать использование ископаемого топлива?  Ответ: Ископаемое топливо (уголь, нефть, природный газ) является основным источником выбросов CO₂, который вызывает глобальное потепление. Замена их на возобновляемые источники энергии (солнечная, ветровая, гидроэнергетика) помогает снизить эти выбросы и замедлить изменение климата.","Как изменения климата влияют на здоровье людей? Ответ: Изменения климата приводят к ухудшению качества воздуха, увеличению числа аллергий и респираторных заболеваний, распространению инфекционных болезней, связанным с изменением условий обитания переносчиков инфекций (комаров, клещей). Экстремальная жара также повышает риск сердечно-сосудистых заболеваний и теплового удара.","Что такое Парижское соглашение по климату? Ответ: Парижское соглашение — это международный договор, принятый в 2015 году, целью которого является удержание роста глобальной средней температуры ниже 2°C по сравнению с доиндустриальными уровнями и стремление ограничить этот рост до 1,5°C. Соглашение предусматривает меры по сокращению выбросов парниковых газов и адаптации к последствиям изменения климата.","Какие страны больше всего страдают от последствий глобального потепления? Ответ: Особенно сильно страдают малые островные государства, такие как Мальдивы и Кирибати, которые находятся под угрозой затопления из-за подъема уровня моря. Также уязвимы бедные страны Африки и Азии, где население зависит от сельского хозяйства, которое страдает от засух и наводнений."]
    toseltxtt = random.choice(totxtextt)

    # Отправляем сообщение
    bot.send_message(message.chat.id, toseltxtt)

@bot.message_handler(commands=['story'])
def send_image(message):

    totxtexttt = ["Семье Семеновых удалось сократить свои выбросы углекислого газа почти вдвое благодаря нескольким простым шагам.Они начали с установки солнечных панелей на крыше своего загородного дома, что позволило им получать значительную часть электроэнергии из возобновляемых источников. Затем они заменили старые бытовые приборы на энергоэффективные модели, что снизило потребление электричества.Но самое интересное решение пришло неожиданно: семья решила выращивать овощи и зелень прямо на балконе своей городской квартиры. Теперь они реже покупают продукты в супермаркетах, уменьшая количество пластиковых упаковок и сокращая углеродный след от транспортировки еды.Кроме того, Семеновы стали активно пользоваться общественным транспортом и велосипедами, оставив машину для редких поездок.Теперь они гордятся тем, что делают мир немного чище и здоровее для будущих поколений.","Группа студентов из Санкт-Петербургского университета организовала проект по восстановлению городских парков и скверов.Каждый выходной они собирали друзей и местных жителей, чтобы вместе высаживать деревья и кустарники. Деревья помогают очищать воздух, поглощают углекислый газ и создают комфортные условия для жизни в городе.Проект быстро набрал популярность, и вскоре к нему присоединились школы, компании и даже городские власти. Всего за два года студенты высадили более тысячи деревьев, превратив заброшенные участки в зеленые уголки отдыха.Их инициатива показала, что даже молодые люди могут внести значительный вклад в улучшение экологии города.","Сергей Иванов, фермер из Иркутской области, решил кардинально изменить подход к ведению хозяйства.Он отказался от традиционных методов земледелия, которые требуют большого количества удобрений и пестицидов, и перешел на органическое сельское хозяйство. Сергей начал использовать методы севооборота и компостирования, что помогло улучшить качество почвы и сократить выбросы парниковых газов.Его продукция стала популярной среди местных жителей, ведь она была не только вкуснее, но и полезнее для здоровья. Вскоре другие фермеры последовали его примеру, и теперь в регионе растет число органических хозяйств.Сергей верит, что такие изменения помогут сохранить природу для будущих поколений и сделают жизнь на земле более устойчивой.","Группа школьников из Казани создала молодежную организацию Зеленый город.Они решили начать с малого: каждую субботу ребята выходили на улицы, чтобы собрать мусор и провести субботники. Но скоро их деятельность вышла за рамки уборки. Они организовали кампанию по установке контейнеров для раздельного сбора отходов во всех школах района.Затем ребята провели серию лекций и мастер-классов для учеников младших классов, рассказывая о важности переработки и повторного использования материалов. Их усилия привели к значительному снижению объема мусора, отправляемого на свалки.Сейчас Зеленый город стал примером для других регионов, и их опыт распространяется по всей стране.","Анна Петрова, художница из Екатеринбурга, нашла необычный способ привлечь внимание к проблемам изменения климата.Она начала создавать инсталляции из переработанных материалов, которые символизировали разрушение природы. Ее работы были выставлены в центральных галереях города и привлекли внимание широкой публики.Одна из самых известных работ Анны — гигантская скульптура айсберга, сделанная из старых пластиковых бутылок. Эта инсталляция вызвала широкий резонанс и заставила многих задуматься о влиянии пластикового загрязнения на океаны.Анна надеется, что искусство сможет пробудить в людях желание заботиться о планете и вдохновить их на активные действия."]
    toseltxttt = random.choice(totxtexttt)

    # Отправляем сообщение
    bot.send_message(message.chat.id, toseltxttt)
# Запускаем бота
bot.polling()