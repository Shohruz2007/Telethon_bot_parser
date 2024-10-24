
# for i in range(len(Channels_list)):
#     print(i, Channels_list[0])
#     Channels_list[i]['name'] = Channels_list[i]['name'].lower()


        
    # print(folders)
    
    # print(folders)
    # pprint(me)
    # print(await client.connect())

    # dialogs = await  client.get_dialogs()

    # for dialog in dialogs:
    #     print(dialog.folder_id)
        # if dialog.name == 'TRADING BOT - [VIP]':
        #     print(dialog, '----------------')
        #     if hasattr(dialog.message, "folders"):
        #         for folder in dialog.message.folders:
        #         # if folder.folder_id == 102:
        #             print(folder, '_______________')

    # folder_chat = client.iter_dialogs(folder=10)
    
    # dialogs = await client.get_dialogs()
    
    # print("\n", "=======================\n", dialog)
    # for dialog in dialogs:
        # print(dialog)
    #     if dialog.title.lower() in Channels_list:
    #         print("find! --->", dialog)
    #         messages = client.iter_messages(dialog)
    #         print(
    #             [message.text async for message in messages], "\n ---->", type(messages)
    #         )
    #         time.sleep(1)



    # for i in sorted(list(set(channel_collector))):
    #     if not i in sorted(list(set(All_Channels_names_list))):
    #         my_file = open('former.csv', 'w')
    #         writer = csv.writer(my_file, delimiter =',')
    #         writer.writerow(['Channel_name','Parse_Mode'])
    #         try:
    #             for parse_channel in channel_collector:
    #                 print(parse_channel)
    #                 writer.writerow([parse_channel,False])
    #                 # writer.writerow([parse_channel['name'],parse_channel['is_parse']])
    #         except:
    #             pass
    #         print('NOt Supported Obj ---->',i)
    #     else:
    #         print('\nSUUPEER ____________')
# number = ' 998998024954'
# print(number.strip(' '))
# print(number.rjust(13,'+'))

# from ast import literal_eval


# str_list = '["hello", "hi"]'

# str_list = literal_eval(str_list)
# # print(list(map(str,str_list)))
# print(type(str_list))

# string1 = 'A13 B144'
# for i in string1.split():
#     print(i)
# print(string1.split())


# ned_message = '''|база1|база2|база3|
# 	| 100 |  95 |  25 |

# 	всего 3 базы, в базах 220 каналов
# 	180 - активных
# 	15  - не активных
# 	25  - ждут иннициализацию
# 	5   - добавлено новых за последнии сутки
# 	1   - удалено за последнии сутки
# '''

# exp_dict = {}
# exp_dict.update({'new':'new','old':'olds'})
# print(exp_dict)

# channel_logo = open('bdg/ГI0_1728375520/logo.jpg', 'r')
# print(channel_logo)

# test_str = '/OBJ1/OBJ2'
# # test_strs_list = test_str.split('/')
# # test_strs_list.remove('')
# # print(test_strs_list)

# letters = 'A13'
# words = ['xunter', 'хрюша']

# margin = '10-15x'
# # print(ord('х'))
# # print(ord('x'))

# # print(margin.replace('x','').replace('-','').isalnum())
# # for word in words:
# #     print(('x' in word or 'х' in word) and margin.replace('x','').replace('-','').isalnum())

# print('A' in letters)
# # print(letters.replace('A', ''))
# # print(letters.strip('A'))

# with_scope_obj = 'hi (go hell))'

# import re

# pattern = r"\((.*?)\)"

# matches = re.findall(r"\((.*?)\)", with_scope_obj)

# if matches:
#     content_within_parentheses = matches
#     print(f"Content within parentheses: {content_within_parentheses}")
# else:
#     print("No parentheses found in the string")
    
    

    
# import re


# Def_signals_list = {'signals': '', 'workspace': 'BitGEt', 'instrument': '', 'tendency': '', 'margin': '', 'margin_type': '', 'entrance_point': '', 'stop_point': '', 'take_profit': ''}
# Signals_list = { 'signals': '', 'workspace': 'Торгуем на бирже', 'instrument': '#', 'tendency': ['Лонг', 'Шорт'], 'margin': 'Плечо -', 'margin_type': '', 'entrance_point': 'Вход - ', 'stop_point': 'Стоп -', 'take_profit': 'Цели - '}
# Not_parse_signals = {'id': '2039724212', 'name': 'Bot testing channel 2', 'channel_link': '', 'admin': '', 'rate': '50', 'confidence_rate': '50', 'signal_rate': '50',}
# # Signals_list.update({'tendency':Signals_list['tendency'].split('/')})
# # print('SIGNALS LIST -->',Signals_list)
# # print('DEF LIST -->',Def_signals_list)


    
# not_parse_signal_name_list = ['id','name','channel_link','admin','rate','confidence_rate','signal_rate']
# not_parse_signals = {}
# for not_parse_signal in not_parse_signal_name_list:
#     if not_parse_signal in Signals_list:
#         not_parse_signals.update({not_parse_signal:Signals_list[not_parse_signal]})

# # signals_values_list = (list(Signals_list.values()))

# must_have_signals_list = ['instrument','tendency','entrance_point','stop_point']


# signals_names_list = list(Signals_list)

# # print('SIGNALS NAMES LIST ---->', signals_names_list)

# not_found_signals = signals_names_list[:]

# found_signals_values = {}

# message_row_list = ['▫️#ID Лонг', '▫️Вход - 0.2934$', '▫️Цели - 0.2963$ - 0.2999$ - 0.3101$- Open', '▫️Плечо - x50 (Сross)', '▫️Стоп - пока не ставлю!', '', 'Торгуем на бирже MEXC,']


# def custom_message_check(message_row, message_row_id):
#     message_row_splitted = message_row.split()
    
#     for message_row_split_id,message_row_split in enumerate(message_row_splitted):
#         # print('message_row_id -->'.upper(), message_row_id,'\n',message_row_split_id in Signals_list['tendency'])
#         if message_row_split.isupper() and  not message_row_split in [tendencies.upper() for tendencies in Signals_list['tendency']]:
#             found_signals_values.update({'instrument':message_row_split})
#             try:
#                 not_found_signals.remove('instrument')
#             except:
#                 pass
        
#         if ('x' in message_row_split or 'х' in message_row_split) and message_row_split.replace('x','').replace('-','').isnumeric():
#             found_signals_values.update({'margin':message_row_split.replace('-','')})
#             try:
#                 not_found_signals.remove('margin')
#             except:
#                 pass
            
        
#     for tendency in [tendencies.upper() for tendencies in Signals_list['tendency']]:
#         if tendency in message_row_splitted:
#             found_signals_values.update({'tendency':tendency})

#             try:
#                 not_found_signals.remove('tendency')
#             except:
#                 pass
    
#     print('\n Custom Check Found Signals -->', found_signals_values)
    
# def get_def_signals():
#     found_signals = []
#     for NF_signal_id,NF_signal in enumerate(not_found_signals):

#         try:
#             def_value = Def_signals_list[NF_signal]
#             # print('Def value found!!', def_value)
#             if not def_value is None and not def_value == '':
#                 found_signals_values.update({NF_signal:def_value})
#                 found_signals.append(not_found_signals[NF_signal_id])
#                 continue
            
#         except:
#             from_info_value = Signals_list[NF_signal]
#             # print('Info file value found!!', from_info_value)
#             if not from_info_value is None and not from_info_value == '':
#                 found_signals_values.update({NF_signal:from_info_value})
#                 found_signals.append(not_found_signals[NF_signal_id])
#                 continue
#     print('\n Def signals Found Signals -->', found_signals_values)
            
#     return found_signals

# def converting_signal_value_to_list(value,signal_name):
#     listed_value = value.split('/')
#     try:
#         listed_value.remove('')
#     except:
#         pass
#     Signals_list.update({signal_name:listed_value})

# for item_signal_name,item_signal_value in Signals_list.items():
#     print('Signal -->',item_signal_name,'; <> ;Signal Value -->',item_signal_value)
#     for message_row_id,message_row in enumerate(message_row_list[:]):
    
#         # print('NOT Found Signals -->',list(set(not_found_signals)),'\n\n')
#         if '/' in item_signal_value:
#             converting_signal_value_to_list(item_signal_value,item_signal_name)
        
        
#         if type(item_signal_value) is list:
#             continue
        
#         if item_signal_value.lower() in message_row.lower() and not item_signal_value == '':
#             if item_signal_name.lower() == 'instrument'.lower():
#                 print('FOUND INSTRUMENT !! -->', message_row)
#                 message_row_splitted = message_row.split(item_signal_value)[1]
#                 message_value = message_row_splitted.split()[0]
#                 # print('MESSAGE ROW SPLITTED -->', message_row_splitted)
#                 not_found_signals.remove('instrument')
#                 for tendency in Signals_list['tendency']:
#                     if tendency in message_row_splitted:
#                         found_signals_values.update({'tendency':tendency})
        
#                         not_found_signals.remove('tendency')
#                 for message_row_split in message_row_splitted.split():
#                     if ('x' in message_row_split or 'х' in message_row_split) and message_row_split.replace('x','').replace('-','').isnumeric():
#                         found_signals_values.update({'margin':message_row_split.replace('-','')})
#                         not_found_signals.remove('margin')
            
            
#             elif item_signal_name.lower() == 'margin'.lower():
#                 margin_value = message_row.split(item_signal_value)[1]
#                 print('ELIF MARGIN -->', margin_value)

#                 matches = re.findall(r"\((.*?)\)", margin_value)
#                 if matches:
#                     scope_content = matches[0]
#                     found_signals_values.update({'margin_type':scope_content})
#                     print('scope_content -->', scope_content)
#                     message_value = margin_value.replace(f'({scope_content})', '')
#                     print('margin_value -->', margin_value)
#                     print('\nFound Signals inside margin -->', found_signals_values)
#                 else:
#                     message_value = margin_value
            
            
#             else:
#                 # print('NOT Found Signals -->',not_found_signals,'\n')
#                 # print('SIGNAL NAME IN FOUND --->',signals_names_list[value_id])
#                 try:
#                     not_found_signals.remove(item_signal_name)
#                 except:
#                     pass
#                 message_value = message_row.split(item_signal_value)[1]
            
#             # print('SIGNAL NAME --->',signals_names_list[value_id])
#             print('\n ADD MESSAGE VALUE --X-->', {item_signal_name:message_value})
#             found_signals_values.update({item_signal_name:message_value})
#             print('\nMain Found Signals --][-->', found_signals_values)
            
#                 # print('\nMessage Value -->',message_value)
#             message_row_list.pop(message_row_id)
#             continue
#         else:
#             if item_signal_name.lower() == 'instrument'.lower():
#                 custom_message_check(message_row, message_row_id)
                
#                 # not_found_signals.append(signals_names_list[value_id])



#     # print('\nSignals -->', Signals_list)
    
    
# def_found_signals = get_def_signals()
# # print('NOT Found Signals -->',not_found_signals,'\n')


    

# not_found_signals = list(set(not_found_signals)-set(def_found_signals))
# # print('NOT Found Signals -->',not_found_signals,'\n')
# found_signals_values.update(Not_parse_signals)

# print('\nFound Signals -->', found_signals_values)
# # print('\nSignals -->', Signals_list)

# check_important_signal_list = []
# message_constructor = ''


# for signal_name in signals_names_list:
#     if signal_name in found_signals_values:
#         if type(found_signals_values[signal_name]) is list:
#             value_str = ''
#             for value in found_signals_values[signal_name]:
#                 value_str += value+' '
#             found_signals_values.update({signal_name:value_str})
#         message_constructor += f'{signal_name} : {found_signals_values[signal_name]}\n'

# for nf_signal in not_found_signals:
#     if nf_signal in must_have_signals_list:
#         check_important_signal_list.append(nf_signal)
#         message_constructor += f'{nf_signal} :\n'

# print('not_found_signals --->'.upper(), not_found_signals)
# print('check_important_signal_list --->', check_important_signal_list)
# if sorted(must_have_signals_list) == sorted(check_important_signal_list):
#     pass

    
    
    

# async def check_message_in_signals(info_file_path, message):

#     # print('MESSAGE TEXT rows--->', message.split('\n'), '\n\n')
#     Def_signals_list = {'id': '2039724212', 'name': 'Bot testing channel 2', 'channel_link': '', 'admin': '/@admin1/@admin2', 'rate': '', 'confidence_rate': '', 'signal_rate': '', 'signals': '', 'workspace': 'Торгуем на бирже', 'instrument': '#', 'tendency': ['Лонг', 'Шорт'], 'margin': 'Плечо -', 'margin_type': '2039724212', 'entrance_point': '', 'stop_point': 'Вход - ', 'take_profit': 'Стоп -'}
#     Signals_list = {'signals': '', 'workspace': 'BitGEt', 'instrument': '', 'tendency': '', 'margin': '', 'margin_type': '', 'entrance_point': '', 'stop_point': '', 'take_profit': ''}
#     Signals_list.update({'tendency':Signals_list['tendency'].split('/')})
#     print('SIGNALS LIST -->',Signals_list)
#     print('DEF LIST -->',Def_signals_list)
    
#     signals_values_list = (list(Signals_list.values()))
    
#     must_have_signals_list = 

    
#     signals_names_list = list(Signals_list)
    
#     # print('SIGNALS NAMES LIST ---->', signals_names_list)
    
#     not_found_signals = signals_names_list[:]
    
#     found_signals_values = {}
    
#     message_row_list = message.split('\n')
    
    
#     def custom_message_check(message_row, message_row_id):
#         message_row_splitted = message_row.split()
        
#         for message_row_split_id,message_row_split in enumerate(message_row_splitted):
#             # print('message_row_id -->'.upper(), message_row_id,'\n',message_row_split_id in Signals_list['tendency'])
#             if message_row_split.isupper() and  not message_row_split in [tendencies.upper() for tendencies in Signals_list['tendency']]:
#                 found_signals_values.update({'instrument':message_row_split})
#                 try:
#                     not_found_signals.remove('instrument')
#                 except:
#                     pass
            
#             if ('x' in message_row_split or 'х' in message_row_split) and message_row_split.replace('x','').replace('-','').isnumeric():
#                 found_signals_values.update({'margin':message_row_split.replace('-','')})
#                 try:
#                     not_found_signals.remove('margin')
#                 except:
#                     pass
                
            
#         for tendency in [tendencies.upper() for tendencies in Signals_list['tendency']]:
#             if tendency in message_row_splitted:
#                 found_signals_values.update({'tendency':tendency})
    
#                 try:
#                     not_found_signals.remove('tendency')
#                 except:
#                     pass
        
#         print('\n Custom Check Found Signals -->', found_signals_values)
        
#     def get_def_signals():
#         found_signals = []
#         for NF_signal_id,NF_signal in enumerate(not_found_signals):

#             try:
#                 def_value = Def_signals_list[NF_signal]
#                 # print('Def value found!!', def_value)
#                 if not def_value is None and not def_value == '':
#                     found_signals_values.update({NF_signal:def_value})
#                     found_signals.append(not_found_signals[NF_signal_id])
#                     continue
                
#             except:
#                 from_info_value = Signals_list[NF_signal]
#                 # print('Info file value found!!', from_info_value)
#                 if not from_info_value is None and not from_info_value == '':
#                     found_signals_values.update({NF_signal:from_info_value})
#                     found_signals.append(not_found_signals[NF_signal_id])
#                     continue
#         print('\n Def signals Found Signals -->', found_signals_values)
                
#         return found_signals
    
#     def converting_signal_value_to_list(value,value_id):
#         listed_value = value.split('/')
#         try:
#             listed_value.remove('')
#         except:
#             pass
#         Signals_list.update({signals_names_list[value_id]:listed_value})
    
#     for value_id,value in enumerate(signals_values_list):
#         for message_row_id,message_row in enumerate(message_row_list[:]):
        
#             # print('NOT Found Signals -->',list(set(not_found_signals)),'\n\n')
#             if '/' in value:
#                 converting_signal_value_to_list(value,value_id)
            
            
#             if type(value) is list:
#                 continue
            
#             if value.lower() in message_row.lower() and not value == '':
#                 if signals_names_list[value_id].lower() == 'instrument'.lower():
#                     print('FOUND INSTRUMENT !! -->', message_row)
#                     message_row_splitted = message_row.split(value)[1]
#                     message_value = message_row_splitted.split()[0]
#                     # print('MESSAGE ROW SPLITTED -->', message_row_splitted)
#                     not_found_signals.remove('instrument')
#                     for tendency in Signals_list['tendency']:
#                         if tendency in message_row_splitted:
#                             found_signals_values.update({'tendency':tendency})
            
#                             not_found_signals.remove('tendency')
#                     for message_row_split in message_row_splitted.split():
#                         if ('x' in message_row_split or 'х' in message_row_split) and message_row_split.replace('x','').replace('-','').isnumeric():
#                             found_signals_values.update({'margin':message_row_split.replace('-','')})
#                             not_found_signals.remove('margin')
                
                
#                 elif signals_names_list[value_id].lower() == 'margin'.lower():
#                     margin_value = message_row.split(value)[1]
#                     print('ELIF MARGIN -->', margin_value)

#                     matches = re.findall(r"\((.*?)\)", margin_value)
#                     if matches:
#                         scope_content = matches[0]
#                         found_signals_values.update({'margin_type':scope_content})
#                         print('scope_content -->', scope_content)
#                         message_value = margin_value.replace(f'({scope_content})', '')
#                         print('margin_value -->', margin_value)
#                         print('\nFound Signals inside margin -->', found_signals_values)
#                     else:
#                         message_value = margin_value
                
                
#                 else:
#                     # print('NOT Found Signals -->',not_found_signals,'\n')
#                     # print('SIGNAL NAME IN FOUND --->',signals_names_list[value_id])
#                     try:
#                         not_found_signals.remove(signals_names_list[value_id])
#                     except:
#                         pass
#                     message_value = message_row.split(value)[1]
                
#                 # print('SIGNAL NAME --->',signals_names_list[value_id])
#                 print('\n ADD MESSAGE VALUE --X-->', {signals_names_list[value_id]:message_value})
#                 found_signals_values.update({signals_names_list[value_id]:message_value})
#                 print('\nMain Found Signals --][-->', found_signals_values)
                
#                     # print('\nMessage Value -->',message_value)
#                 message_row_list.pop(message_row_id)
#                 continue
#             else:
#                 if signals_names_list[value_id].lower() == 'instrument'.lower():
#                     custom_message_check(message_row, message_row_id)
                    
#                     # not_found_signals.append(signals_names_list[value_id])


#     # print('\nSignals -->', Signals_list)
#     def_found_signals = get_def_signals()
#     # print('NOT Found Signals -->',not_found_signals,'\n')
    
    
        

#     not_found_signals = list(set(not_found_signals)-set(def_found_signals))
#     # print('NOT Found Signals -->',not_found_signals,'\n')
#     print('\nFound Signals -->', found_signals_values)
#     # print('\nSignals -->', Signals_list)
    
#     check_important_signal_list = []
#     message_constructor = ''
    
    
#     for signal_name in signals_names_list:
#         if signal_name in found_signals_values:
#             if type(found_signals_values[signal_name]) is list:
#                 value_str = ''
#                 for value in found_signals_values[signal_name]:
#                     value_str += value+' '
#                 found_signals_values.update({signal_name:value_str})
#             message_constructor += f'{signal_name} : {found_signals_values[signal_name]}\n'
    
#     for nf_signal in not_found_signals:
#         if nf_signal in must_have_signals_list:
#             check_important_signal_list.append(nf_signal)
#             message_constructor += f'{nf_signal} :\n'
    
#     print('not_found_signals --->'.upper(), not_found_signals)
#     print('check_important_signal_list --->', check_important_signal_list)
#     if sorted(must_have_signals_list) == sorted(check_important_signal_list):
#         pass
        
#     elif len(check_important_signal_list)==0:
#         sent_message = await bot.send_message(await get_chat_id(), f'✅\nДанные которые совпали:\n{message_constructor}')
#         await bot.send_message(await get_chat_id(), "\n----------------\n")
#         # print('Sent_message -->',sent_message)
#         # sent_message = await client.get_messages(await get_chat_id(), 2959)
#         # await bot.forward_messages(await get_chat_id(),2959, await get_chat_id())
#     else:
#         send_button = Button.inline('Send to channel', f'send_message channel={Signals_list['id']}')
#         cancel_button = Button.inline('Cancel', b'cancel_message')
#         edit_button_query_data = 'edit '
        
#         # for signal in check_important_signal_list:
#         #     edit_button_query_data += signal+' '
        
#         edit_button_query_data += f'channel={Signals_list['id']}'
#         edit_button = Button.inline('Edit', edit_button_query_data)

#         buttons_row = [send_button,cancel_button,edit_button]
        
#         await bot.send_message(await get_chat_id(), f'⚠️ \n\n Данные которые совпали:\n{message_constructor}  \n\nНе полное информация', buttons=buttons_row)
#         await bot.send_message(await get_chat_id(), "\n__________________________\n")


# a = [2,3, '4']
# print(a.index('4'))


# a = 34
# b = 40
# c = 61
# d = 80
# print(a%20)
# print(b%20)
# print(c%20)
# print(d%20)
# print(a.split(','))


# message = 'Channel1,   CHannel 2  '
# message = [message.strip() for message in message.split(',')]
# print(message)


# title = 'TITLE _'
# # amount = '13'

# for symbol in [' ']:
#     title = title.replace(symbol, '')
# print(f'title --> {title}'.title(),end='\n')
# # print(f'{amount.center(16)}',end='')

# list1 = []
# list1 += [1,2]
# print(list1)

# ls = [0,1,2,3,4,5]
# a  = lambda x,y=None: ls[x:(x+1 if y is None else y)]
# print(a(3,5))


# def env_reader(value:str,is_list=False):
#     env_file = open(Utility.Env_file_path,'r')
#     env = env_file.read()
#     for env_row in env.split('\n'):
#         if value in env_row:
#             env_value = env_row.replace(value+'=', '')
#             if is_list:
#                 env_value = [value for value in env_value.split('/') if not value in ['',' ']]
#             return env_value





# Api_id = env_reader('Api_id')
# Api_hash = env_reader('Api_hash')
# bot_token = env_reader('Bot_token')
# Client_name = env_reader('Client_name')


# bot = TelegramClient('bot-session', Api_id, Api_hash).start(bot_token=bot_token)


# client = TelegramClient(Client_name, Api_id, Api_hash, system_version="4.16.30-vxCUSTOM")

# message = '<b>Bold</b>, <strong>Strong</strong>'
# message += '<i>Italic</i>, <em>Emphasized</em>'
# message += '<u>Underline</u>'
# message += '<s>Strikethrough</s> or <strike>Strikethrough</strike>'
# message += '<code>Monospaced code</code>'
# message += '<pre>Preformatted text</pre>'
# message += '<a href="https://example.com">Hyperlink</a>'

# import re

# string = "<i>italic word<i>"

# italic_words = re.findall(fr"{'<i>'}(.*?){'<i>'}", string)
# print(italic_words)

# await bot.send_message(chat_id, message, parse_mode='html')



# signal = {'stoploss':''}
# stop = signal.get('stoplosss')
# print(type(stop))

# print(open('bdg/bdg_former.csv').readlines())
# open('bdg//info.csv','w')
# l1 = set([1,2,3,4])
# l2 = {3,4,5}
# print(l2-l1)

# import time


# main_list = ['1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10',]


# start_time = time.time()
# list_collector = []
# for list_obj in main_list:
#     list_collector.append(list_obj)


# end_time = time.time()
# first_time = (end_time-start_time)
# print(first_time)

# start_time = time.time()

# list_collector_ternary = [list_obj for list_obj in main_list]
# list_collector_ternary = [list_obj for list_obj in main_list]
# list_collector_ternary = [list_obj for list_obj in main_list]

# print(111)
# end_time = time.time()
# second_time = (end_time-start_time)
# print(second_time)
# print(second_time<first_time,f'\n{second_time-first_time}')


# def replace_russian_letters(text):
#     replacements = {'а': 'a','б': 'b','в': 'v','г': 'g','д': 'd','е': 'e','ё': 'e','ж': 'j','з': 'z','и': 'i','й': 'y','к': 'k','л': 'l','м': 'm','н': 'n','о': 'o','п': 'p','р': 'r','с': 's','т': 't','у': 'u','ф': 'f','х': 'x','ц': 's','ч': 'ch','ш': 'sh','щ': 'sh','ъ': '','ы': 'y','ь': '','э': 'e','ю': 'u','я': 'a'}


#     result = ''
#     for char in text:
#         if char.lower() in replacements:
#             replacement = replacements[char.lower()]
#             if char.isupper():
#                 result += replacement.capitalize()
#             else:
#                 result += replacement[0]

#         else:
#             result += char

#     return result



# def path_maker(channel_id,channel_name:str):
#     Path_title = ''
#     channel_name_parts_list = channel_name.split()
#     channel_name_parts_list = [name_part for name_part in channel_name_parts_list if name_part.isalpha()]
    

#     for name_part_id,channel_name_part in enumerate(channel_name_parts_list):
#         letter_collector = []
#         for name_letter_id,channel_name_letter in enumerate(channel_name_part):

#             if channel_name_letter.isalpha():
#                 letter_collector.append(name_letter_id)
                
#         if len(letter_collector) != 0:
#             Path_title += channel_name_part[min(letter_collector)]

#     if len(channel_name_parts_list) <= 2 and not len(channel_name_parts_list) == 0:
#         Path_title += channel_name_part[len(channel_name_part)//2]
#         if len(channel_name_parts_list)==1:
#             Path_title += channel_name_part[len(channel_name_part)-1]
#         print(channel_name_parts_list)
            

#     Path_title = replace_russian_letters(Path_title)

#     Path_full = f"{Path_title[:3].upper()}_{channel_id}"

#     return Path_full


# print(path_maker(1557909953, '📰'))


# signal = {'take_profit': ' 0.7842'}

# print(bool([]))

# rows = [
# '1. рынок 0,01698',
# '2. рынок 0,01698',
# '3. рынок 0,01698',
# '',
# '🎯 тэйк-профит:',
# ]

# for row in rows:
#     print(row.startswith(tuple(map(str, range(1,10)))))

# channel_info_collector_sorted = [{'Programmer & IT Memes': 'Trading'}, {'CryptoLab': 'Trading'}, {'TRADING BOT - [VIP]': 'Trading'}, {'Trade Indicator 🚀': 'Trading'}, {'Bot Testing channel': 'Trading'}, {'Bot testing channel 2': 'Trading'}, {'Litvinoff': 'trading2'}, {'ITLES | Уроки программирования': 'trading2'}, {'PRO4EX FOREX TRADING SIGNALS': 'trading2'}]

# All_channels_in_base = [{'CryptoLab': 'Trading'}, {'Programmer & IT Memes': 'Trading'}, {'Bot Testing channel': 'Trading'}, {'TRADING BOT - [VIP]': 'Trading'}, {'Trade Indicator 🚀': 'Trading'}, {'Litvinoff': 'trading2'}, {'ITLES | Уроки программирования': 'trading2'}, {'PRO4EX FOREX TRADING SIGNALS': 'trading2'}, {'Bot testing channel 2': 'trading2'}]

# channel_check_list = [check_channel in All_channels_in_base for check_channel in channel_info_collector_sorted]

# print(channel_check_list)
# print(all(channel_check_list))

# import re


# temp = ' моя твх <num>'.replace('<num>', r'(\d+(\.\d+)?)').strip()

# exm = 'моя твх 0.2663'.strip()

# pattern = re.compile(temp)
# match = pattern.match(exm)


# for obj in match.groups()[::2]:
    
#     print(obj)


print('hello'.replace('l','',1))