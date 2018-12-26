from bottle import route, run, request, abort, static_file
import pygraphviz
from fsm import TocMachine
from utils import *
import os

PORT = os.environ['PORT']

VERIFY_TOKEN = "eatandcomment"
machine = TocMachine(
    states=[
        'home',
        'temp_home',
        'east_district',
        'west_central_district',
        'north_district',
        'eat_rice',
        'eat_noodles',
        'eat_snack',
        'eat_rice_in_east',
        'eat_snack_in_east',
        'eat_noodles_in_east',
        'eat_rice_in_west',
        'eat_snack_in_west',
        'eat_noodles_in_west',
        'eat_rice_in_north',
        'eat_snack_in_north',
        'eat_noodles_in_north',
        'recommend_rice_in_east',
        'recommend_noodles_in_east',
        'recommend_snack_in_east',
        'recommend_rice_in_west',
        'recommend_snack_in_west',
        'recommend_noodles_in_west',
        'recommend_rice_in_north',
        'recommend_snack_in_north',
        'recommend_noodles_in_north',
        'help'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'home',
            'dest': 'help',
            'conditions': 'is_going_to_help'
        },
        {
            'trigger': 'advance',
            'source': 'home',
            'dest': 'east_district',
            'conditions': 'is_going_to_east_district'
        },
        {
            'trigger': 'advance',
            'source': 'home',
            'dest': 'west_central_district',
            'conditions': 'is_going_to_west_central_district'
        },
        {
            'trigger': 'advance',
            'source': 'home',
            'dest': 'north_district',
            'conditions': 'is_going_to_north_district'
        },
        {
            'trigger': 'advance',
            'source': 'home',
            'dest': 'eat_rice',
            'conditions': 'is_going_to_eat_rice'
        },
        {
            'trigger': 'advance',
            'source': 'home',
            'dest': 'eat_noodles',
            'conditions': 'is_going_to_eat_noodles'
        },
        {
            'trigger': 'advance',
            'source': 'home',
            'dest': 'eat_snack',
            'conditions': 'is_going_to_eat_snack'
        },
        {
            'trigger': 'advance',
            'source': [
                'eat_noodles',
                'east_district'],
            'dest': 'eat_noodles_in_east',
            'conditions': 'is_going_to_eat_noodles_in_east'
        },
        {
            'trigger': 'advance',
            'source': 'eat_noodles_in_east',
            'dest': 'eat_noodles_in_east',
            'conditions': 'is_button_reselect'
        },
        {
            'trigger': 'advance',
            'source': 'eat_noodles_in_east',
            'dest': 'recommend_noodles_in_east',
            'conditions': 'is_recommend'
        },
        {
            'trigger': 'advance',
            'source': [
                'eat_rice',
                'east_district'],
            'dest': 'eat_rice_in_east',
            'conditions': 'is_going_to_eat_rice_in_east'
        },
        {
            'trigger': 'advance',
            'source': 'eat_rice_in_east',
            'dest': 'eat_rice_in_east',
            'conditions': 'is_button_reselect'
        },
        {
            'trigger': 'advance',
            'source': 'eat_rice_in_east',
            'dest': 'recommend_rice_in_east',
            'conditions': 'is_recommend'
        },
        {
            'trigger': 'advance',
            'source': [
                'east_district',
                'eat_snack'],
            'dest': 'eat_snack_in_east',
            'conditions': 'is_going_to_eat_snack_in_east'
        },
        {
            'trigger': 'advance',
            'source': 'eat_snack_in_east',
            'dest': 'eat_snack_in_east',
            'conditions': 'is_button_reselect'
        },
        {
            'trigger': 'advance',
            'source': 'eat_snack_in_east',
            'dest': 'recommend_snack_in_east',
            'conditions': 'is_recommend'
        },
        {
            'trigger': 'advance',
            'source': [
                'west_central_district', 
                'eat_rice'],
            'dest': 'eat_rice_in_west',
            'conditions': 'is_going_to_eat_rice_in_west'
        },
        {
            'trigger': 'advance',
            'source': 'eat_rice_in_west',
            'dest': 'eat_rice_in_west',
            'conditions': 'is_button_reselect'
        },
        {
            'trigger': 'advance',
            'source': 'eat_rice_in_west',
            'dest': 'recommend_rice_in_west',
            'conditions': 'is_recommend'
        },
        {
            'trigger': 'advance',
            'source': [
                'west_central_district',
                'eat_snack'],
            'dest': 'eat_snack_in_west',
            'conditions': 'is_going_to_eat_snack_in_west'
        },
        {
            'trigger': 'advance',
            'source': 'eat_snack_in_west',
            'dest': 'eat_snack_in_west',
            'conditions': 'is_button_reselect'
        },
        {
            'trigger': 'advance',
            'source': 'eat_snack_in_west',
            'dest': 'recommend_snack_in_west',
            'conditions': 'is_recommend'
        },
        {
            'trigger': 'advance',
            'source': [
                'west_central_district',
                'eat_noodles'],
            'dest': 'eat_noodles_in_west',
            'conditions': 'is_going_to_eat_noodles_in_west'
        },
        {
            'trigger': 'advance',
            'source': 'eat_noodles_in_west',
            'dest': 'eat_noodles_in_west',
            'conditions': 'is_button_reselect'
        },
        {
            'trigger': 'advance',
            'source': 'eat_noodles_in_west',
            'dest': 'recommend_noodles_in_west',
            'conditions': 'is_recommend'
        },
        {
            'trigger': 'advance',
            'source': [
                'north_district', 
                'eat_rice'],
            'dest': 'eat_rice_in_north',
            'conditions': 'is_going_to_eat_rice_in_north'
        },
        {
            'trigger': 'advance',
            'source': 'eat_rice_in_north',
            'dest': 'eat_rice_in_north',
            'conditions': 'is_button_reselect'
        },
        {
            'trigger': 'advance',
            'source': 'eat_rice_in_north',
            'dest': 'recommend_rice_in_north',
            'conditions': 'is_recommend'
        },
        {
            'trigger': 'advance',
            'source': [
                'north_district',
                'eat_snack'],
            'dest': 'eat_snack_in_north',
            'conditions': 'is_going_to_eat_snack_in_north'
        },
        {
            'trigger': 'advance',
            'source': 'eat_snack_in_north',
            'dest': 'eat_snack_in_north',
            'conditions': 'is_button_reselect'
        },
        {
            'trigger': 'advance',
            'source': 'eat_snack_in_north',
            'dest': 'recommend_snack_in_north',
            'conditions': 'is_recommend'
        },
        {
            'trigger': 'advance',
            'source': [
                'north_district',
                'eat_noodles'],
            'dest': 'eat_noodles_in_north',
            'conditions': 'is_going_to_eat_noodles_in_north'
        },
        {
            'trigger': 'advance',
            'source': 'eat_noodles_in_north',
            'dest': 'eat_noodles_in_north',
            'conditions': 'is_button_reselect'
        },
        {
            'trigger': 'advance',
            'source': 'eat_noodles_in_north',
            'dest': 'recommend_noodles_in_north',
            'conditions': 'is_recommend'
        },
        {
            'trigger': 'advance',
            'source': [
                'recommend_rice_in_east',
                'recommend_noodles_in_east',
                'recommend_snack_in_east',
                'recommend_rice_in_west',
                'recommend_snack_in_west',
                'recommend_noodles_in_west',
                'recommend_rice_in_north',
                'recommend_snack_in_north',
                'recommend_noodles_in_north'],
            'dest': 'temp_home',
            'conditions': 'is_bye'
        },
        {
            'trigger': 'go_back',
            'source': [
                'temp_home',
                'help'],
            'dest': 'home'
        }
        
    ],
    initial='home',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        if event.get('text') or event.get('postback'):
            machine.advance(event)
        if machine.state == 'home':
            sender_id = event['sender']['id']
            send_text_message(sender_id, "隨便吃嗎？\n我來幫你決定吃什麼吧！\n點擊以下按鈕\n你也可以手動輸入！")
            send_button_message(sender_id, "食物種類", TYPE_BUTTON)
            send_button_message(sender_id, "地區", DIST_BUTTON)
        return 'OK'

@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')



if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
