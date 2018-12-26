from transitions.extensions import GraphMachine
from utils import *
from store import Store
import random

class TocMachine(GraphMachine):

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_help(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "\help"
        return False

    def on_enter_help(self, event):
        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "這是一個幫你決定要吃什麼的機器人～")
        self.go_back()

    def on_exit_help(self, event):
        print('Leaving help state')

    def is_button_reselect(self, event):
        if event.get('postback'):
            if event['postback']['payload'] == 'reselect':
                return True
        if event.get("message"):
            text = event['message']['text']
            return text == '重選'
        return False

    def is_recommend(self, event):
        if event.get('postback'):
            if event['postback']['payload'] == 'satisfied':
                return True
        if event.get("message"):
            text = event['message']['text']
            return text == '滿意'
        return False

    def is_bye(self, event):
        if event.get('postback'):
            if event['postback']['payload'] == 'bye':
                return True
        if event.get("message"):
            text = event['message']['text']
            return text == '拜拜'
        return False

    def on_enter_temp_home(self, event):
        self.go_back()


    def is_going_to_eat_rice(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '飯'
        if event.get('postback'):
            if event['postback']['payload'] == 'rice':
                return True
        return False

    def on_enter_eat_rice(self, event):
        print("I'm going to eat rice")
        sender_id = event['sender']['id']
        response = send_button_message(sender_id, "你想在哪裡吃飯？", DIST_BUTTON)
        
    def on_exit_eat_rice(self, event):
        print('Leaving eat rice')


    def is_going_to_eat_noodles(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '麵'
        if event.get('postback'):
            if event['postback']['payload'] == 'noodles':
                return True
        return False

    def on_enter_eat_noodles(self, event):
        print("I'm going to eat noodles")
        sender_id = event['sender']['id']
        response = send_button_message(sender_id, "你想在哪裡吃麵？", DIST_BUTTON)
        
    def on_exit_eat_noodles(self, event):
        print('Leaving eat noodles')

    def is_going_to_eat_snack(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '點心'
        if event.get('postback'):
            if event['postback']['payload'] == 'snack':
                return True
        return False

    def on_enter_eat_snack(self, event):
        print("I'm going to eat snack")
        sender_id = event['sender']['id']
        response = send_button_message(sender_id, "你想吃哪裏的點心？", DIST_BUTTON)
        
    def on_exit_eat_snack(self, event):
        print('Leaving eat snack')

    def is_going_to_north_district(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '北區'
        if event.get('postback'):
            if event['postback']['payload'] == 'north':
                return True
        return False

    def on_enter_north_district(self, event):
        print("I'm entering east district")
        sender_id = event['sender']['id']
        response = send_button_message(sender_id, "你想在北區吃什麼？", TYPE_BUTTON)
        
    def on_exit_north_district(self, event):
        print('Leaving north district')

    def is_going_to_east_district(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '東區'
        if event.get('postback'):
            if event['postback']['payload'] == 'east':
                return True
        return False

    def on_enter_east_district(self, event):
        print("I'm entering east district")
        sender_id = event['sender']['id']
        response = send_button_message(sender_id, "你想在東區吃什麼？", TYPE_BUTTON)
        
    def on_exit_east_district(self, event):
        print('Leaving east district')

    def is_going_to_west_central_district(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '中西區'
        if event.get('postback'):
            if event['postback']['payload'] == 'west_central':
                return True
        return False

    def on_enter_west_central_district(self, event):
        print("I'm at West Central Dist")
        sender_id = event['sender']['id']
        response = send_button_message(sender_id, "你想在中西區吃什麼？", TYPE_BUTTON)
        #self.go_back()

    def on_exit_west_central_district(self, event):
        print('Leaving west central district')

# rice north
    def is_going_to_eat_rice_in_north(self, event):
        if self.state == 'eat_rice':
            if event.get("message"):
                text = event['message']['text']
                return text == '北區'
            if event.get('postback'):
                if event['postback']['payload'] == 'north':
                    return True
        if self.state == 'north_district':
            if event.get("message"):
                text = event['message']['text']
                return text == '飯'
            if event.get('postback'):
                if event['postback']['payload'] == 'rice':
                    return True
        return False

    def on_enter_eat_rice_in_north(self, event):
        print("I'm want to eat rice in north")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "為你推薦北區的飯館：")
        global key
        key = random.choice(list(Store.info_rice_store_in_north))
        send_text_message(sender_id, Store.info_rice_store_in_north.get(key))
        send_image_url(sender_id, Store.menu_rice_store_in_north.get(key))
        send_button_message(sender_id, "你覺得要重選嗎？", SAT_BUTTON)

    def on_exit_eat_rice_in_north(self, event):
        print('Leaving eat rice in north')

    def on_enter_recommend_rice_in_north(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, Store.recommmend_rice_store_in_north[key]['disc'])
        send_image_url(sender_id, Store.recommmend_rice_store_in_north[key]['img'])
        send_button_message(sender_id, "祝你用餐愉快囉～", BYE_BUTTON)

    def on_exit_recommend_rice_in_north(self, event):
        print("Leaving recommend rice in north")
# snack north
    def is_going_to_eat_snack_in_north(self, event):
        if self.state == 'eat_snack':
            if event.get("message"):
                text = event['message']['text']
                return text == '北區'
            if event.get('postback'):
                if event['postback']['payload'] == 'north':
                    return True
        if self.state == 'north_district':
            if event.get("message"):
                text = event['message']['text']
                return text == '點心'
            if event.get('postback'):
                if event['postback']['payload'] == 'snack':
                    return True
        return False

    def on_enter_eat_snack_in_north(self, event):
        print("I'm want to eat snack in north")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "為你推薦北區的點心：")
        global key
        key = random.choice(list(Store.info_snack_store_in_north))
        send_text_message(sender_id, Store.info_snack_store_in_north.get(key))
        send_image_url(sender_id, Store.menu_snack_store_in_north.get(key))
        send_button_message(sender_id, "你覺得要重選嗎？", SAT_BUTTON)

    def on_exit_eat_snack_in_north(self, event):
        print('Leaving eat snack in north')

    def on_enter_recommend_snack_in_north(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, Store.recommmend_snack_store_in_north[key]['disc'])
        send_image_url(sender_id, Store.recommmend_snack_store_in_north[key]['img'])
        send_button_message(sender_id, "祝你用餐愉快囉～", BYE_BUTTON)

    def on_exit_recommend_snack_in_north(self, event):
        print("Leaving recommend snack in north")
# noodles north
    def is_going_to_eat_noodles_in_north(self, event):
        if self.state == 'eat_noodles':
            if event.get("message"):
                text = event['message']['text']
                return text == '北區'
            if event.get('postback'):
                if event['postback']['payload'] == 'north':
                    return True
        if self.state == 'north_district':
            if event.get("message"):
                text = event['message']['text']
                return text == '麵'
            if event.get('postback'):
                if event['postback']['payload'] == 'noodles':
                    return True
        return False

    def on_enter_eat_noodles_in_north(self, event):
        print("I'm want to eat noodles in north")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "為你推薦北區的麵店：")
        global key
        key = random.choice(list(Store.info_noodles_store_in_north))
        send_text_message(sender_id, Store.info_noodles_store_in_north.get(key))
        send_image_url(sender_id, Store.menu_noodles_store_in_north.get(key))
        send_button_message(sender_id, "你要重選嗎？", SAT_BUTTON)

    def on_exit_eat_noodles_in_north(self, event):
        print('Leaving eat noodles in north')

    def on_enter_recommend_noodles_in_north(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, Store.recommmend_noodles_store_in_north[key]['disc'])
        send_image_url(sender_id, Store.recommmend_noodles_store_in_north[key]['img'])
        send_button_message(sender_id, "祝你用餐愉快囉～", BYE_BUTTON)

    def on_exit_recommend_noodles_in_north(self, event):
        print("Leaving recommend noodles in north")

# rice west
    def is_going_to_eat_rice_in_west(self, event):
        if self.state == 'eat_rice':
            if event.get("message"):
                text = event['message']['text']
                return text == '中西區'
            if event.get('postback'):
                if event['postback']['payload'] == 'west_central':
                    return True
        if self.state == 'west_central_district':
            if event.get("message"):
                text = event['message']['text']
                return text == '飯'
            if event.get('postback'):
                if event['postback']['payload'] == 'rice':
                    return True
        return False

    def on_enter_eat_rice_in_west(self, event):
        print("I'm want to eat rice in west")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "為你推薦中西區的飯館：")
        global key
        key = random.choice(list(Store.info_rice_store_in_west))
        send_text_message(sender_id, Store.info_rice_store_in_west.get(key))
        send_image_url(sender_id, Store.menu_rice_store_in_west.get(key))
        send_button_message(sender_id, "你覺得要重選嗎？", SAT_BUTTON)
        
        #self.go_back()

    def on_exit_eat_rice_in_west(self, event):
        print('Leaving eat rice in west')

    def on_enter_recommend_rice_in_west(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, Store.recommmend_rice_store_in_west[key]['disc'])
        send_image_url(sender_id, Store.recommmend_rice_store_in_west[key]['img'])
        send_button_message(sender_id, "祝你用餐愉快囉～", BYE_BUTTON)

    def on_exit_recommend_rice_in_west(self, event):
        print("Leaving recommend rice in west")
# snack west
    def is_going_to_eat_snack_in_west(self, event):
        if self.state == 'eat_snack':
            if event.get("message"):
                text = event['message']['text']
                return text == '中西區'
            if event.get('postback'):
                if event['postback']['payload'] == 'west_central':
                    return True
        if self.state == 'west_central_district':
            if event.get("message"):
                text = event['message']['text']
                return text == '點心'
            if event.get('postback'):
                if event['postback']['payload'] == 'snack':
                    return True
        return False

    def on_enter_eat_snack_in_west(self, event):
        print("I'm want to eat snack in west")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "為你推薦中西區的點心：")
        global key
        key = random.choice(list(Store.info_snack_store_in_west))
        send_text_message(sender_id, Store.info_snack_store_in_west.get(key))
        send_image_url(sender_id, Store.menu_snack_store_in_west.get(key))
        send_button_message(sender_id, "你覺得要重選嗎？", SAT_BUTTON)

    def on_exit_eat_snack_in_west(self, event):
        print('Leaving eat snack in west')

    def on_enter_recommend_snack_in_west(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, Store.recommmend_snack_store_in_west[key]['disc'])
        send_image_url(sender_id, Store.recommmend_snack_store_in_west[key]['img'])
        send_button_message(sender_id, "祝你用餐愉快囉～", BYE_BUTTON)

    def on_exit_recommend_snack_in_west(self, event):
        print("Leaving recommend snack in west")
# noodles west
    def is_going_to_eat_noodles_in_west(self, event):
        if self.state == 'eat_noodles':
            if event.get("message"):
                text = event['message']['text']
                return text == '中西區'
            if event.get('postback'):
                if event['postback']['payload'] == 'west_central':
                    return True
        if self.state == 'west_central_district':
            if event.get("message"):
                text = event['message']['text']
                return text == '麵'
            if event.get('postback'):
                if event['postback']['payload'] == 'noodles':
                    return True
        return False

    def on_enter_eat_noodles_in_west(self, event):
        print("I'm want to eat noodles in west")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "為你推薦中西區的麵店：")
        global key
        key = random.choice(list(Store.info_noodles_store_in_west))
        send_text_message(sender_id, Store.info_noodles_store_in_west.get(key))
        send_image_url(sender_id, Store.menu_noodles_store_in_west.get(key))
        send_button_message(sender_id, "你要重選嗎？", SAT_BUTTON)

    def on_exit_eat_noodles_in_west(self, event):
        print('Leaving eat noodles in west')

    def on_enter_recommend_noodles_in_west(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, Store.recommmend_noodles_store_in_west[key]['disc'])
        send_image_url(sender_id, Store.recommmend_noodles_store_in_west[key]['img'])
        send_button_message(sender_id, "祝你用餐愉快囉～", BYE_BUTTON)

    def on_exit_recommend_noodles_in_west(self, event):
        print("Leaving recommend noodles in west")

# rice east
    def is_going_to_eat_rice_in_east(self, event):
        if self.state == 'eat_rice':
            if event.get("message"):
                text = event['message']['text']
                return text == '東區'
            if event.get('postback'):
                if event['postback']['payload'] == 'east':
                    return True
        if self.state == 'east_district':
            if event.get("message"):
                text = event['message']['text']
                return text == '飯'
            if event.get('postback'):
                if event['postback']['payload'] == 'rice':
                    return True
        return False

    def on_enter_eat_rice_in_east(self, event):
        print("I'm want to eat rice")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "為你推薦東區的飯館：")
        global key
        key = random.choice(list(Store.info_rice_store_in_east))
        send_text_message(sender_id, Store.info_rice_store_in_east.get(key))
        send_image_url(sender_id, Store.menu_rice_store_in_east.get(key))
        send_button_message(sender_id, "你覺得要重選嗎？", SAT_BUTTON)
        #self.go_back()

    def on_exit_eat_rice_in_east(self, event):
        print('Leaving eat rice')

    def on_enter_recommend_rice_in_east(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, Store.recommmend_rice_store_in_east[key]['disc'])
        send_image_url(sender_id, Store.recommmend_rice_store_in_east[key]['img'])
        send_button_message(sender_id, "祝你用餐愉快囉～", BYE_BUTTON)

    def on_exit_recommend_rice_in_east(self, event):
        print("Leaving recommend noodles in east")
# snack east
    def is_going_to_eat_snack_in_east(self, event):
        if self.state == 'eat_snack':
            if event.get("message"):
                text = event['message']['text']
                return text == '東區'
            if event.get('postback'):
                if event['postback']['payload'] == 'east':
                    return True
        if self.state == 'east_district':
            if event.get("message"):
                text = event['message']['text']
                return text == '點心'
            if event.get('postback'):
                if event['postback']['payload'] == 'snack':
                    return True
        return False

    def on_enter_eat_snack_in_east(self, event):
        print("I'm want to eat snack")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "為你推薦東區的點心：")
        global key
        key = random.choice(list(Store.info_snack_store_in_east))
        send_text_message(sender_id, Store.info_snack_store_in_east.get(key))
        send_image_url(sender_id, Store.menu_snack_store_in_east.get(key))
        send_button_message(sender_id, "你要重選嗎？", SAT_BUTTON)

    def on_exit_eat_snack_in_east(self, event):
        print('Leaving eat snack')

    def on_enter_recommend_snack_in_east(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, Store.recommmend_snack_store_in_east[key]['disc'])
        send_image_url(sender_id, Store.recommmend_snack_store_in_east[key]['img'])
        send_button_message(sender_id, "祝你用餐愉快囉～", BYE_BUTTON)

    def on_exit_recommend_snack_in_east(self, event):
        print("Leaving recommend snack in east")
# noodles east
    def is_going_to_eat_noodles_in_east(self, event):
        if self.state == 'eat_noodles':
            if event.get("message"):
                text = event['message']['text']
                return text == '東區'
            if event.get('postback'):
                if event['postback']['payload'] == 'east':
                    return True
        if self.state == 'east_district':
            if event.get("message"):
                text = event['message']['text']
                return text == '麵'
            if event.get('postback'):
                if event['postback']['payload'] == 'noodles':
                    return True
        return False

    def on_enter_eat_noodles_in_east(self, event):
        print("I'm want to eat noodles")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "為你推薦東區的麵店：")
        global key
        key = random.choice(list(Store.info_noodles_store_in_east))
        send_text_message(sender_id, Store.info_noodles_store_in_east.get(key))
        send_image_url(sender_id, Store.menu_noodles_store_in_east.get(key))
        send_button_message(sender_id, "你要重選嗎？", SAT_BUTTON)

    def on_exit_eat_noodles_in_east(self, event):
        print('Leaving eat noodles')

    def on_enter_recommend_noodles_in_east(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, Store.recommmend_noodles_store_in_east[key]['disc'])
        send_image_url(sender_id, Store.recommmend_noodles_store_in_east[key]['img'])
        send_button_message(sender_id, "祝你用餐愉快囉～", BYE_BUTTON)

    def on_exit_recommend_noodles_in_east(self, event):
        print("Leaving recommend noodles in east")
    
    

    

        

