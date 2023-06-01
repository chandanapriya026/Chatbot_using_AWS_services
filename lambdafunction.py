import json
import datetime
import time

vpizzasize = ['small','medium','large']
vpizzatype = ['cheese','pepparoni', 'veg']
vtoppings = ['mushrooms','olives','tomatoes']

def validate(slots):

    if not slots['quantity']:
        return {
        'isValid': False,
        'violatedSlot': 'quantity'
    }   
       
    if not slots['pizzasize']:
        
        return {
        'isValid': False,
        'violatedSlot': 'pizzasize',
    }
    
    if slots['pizzasize']['value']['originalValue'] not in  vpizzasize:
        
        print("please choose a valid option")
        
        return {
        'isValid': False,
        'violatedSlot': 'pizzasize',
        'message': 'please choose a valid option'
        }    
    
        
    if not slots['pizzatype']:
        return {
        'isValid': False,
        'violatedSlot': 'pizzatype'
    }
    
    if slots['pizzatype']['value']['originalValue'] not in  vpizzatype:
        
        print("please choose a valid option")
        
        return {
        'isValid': False,
        'violatedSlot': 'pizzatype',
        'message': 'please choose a valid option'
        } 
        
    if not slots['toppings']:
        return {
        'isValid': False,
        'violatedSlot': 'toppings'
    }
    
    if slots['toppings']['value']['originalValue'] not in  vtoppings:
        
        print("please choose a valid option")
        
        return {
        'isValid': False,
        'violatedSlot': 'toppings',
        'message': 'please choose a valid option'
        } 

    return {'isValid': True}
    
def lambda_handler(event, context):
    
    # print(event)
    slots = event['sessionState']['intent']['slots']
    intent = event['sessionState']['intent']['name']
    print(event['invocationSource'])
    print(slots)
    print(intent)
    validation_result = validate(slots)
    
    if event['invocationSource'] == 'DialogCodeHook':
        if not validation_result['isValid']:
            
            if 'message' in validation_result:
            
                response = {
                "sessionState": {
                    "dialogAction": {
                        'slotToElicit':validation_result['violatedSlot'],
                        "type": "ElicitSlot"
                    },
                    "intent": {
                        'name':intent,
                        'slots': slots
                        
                        }
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": validation_result['message']
                    }
                ]
               } 
            else:
                response = {
                "sessionState": {
                    "dialogAction": {
                        'slotToElicit':validation_result['violatedSlot'],
                        "type": "ElicitSlot"
                    },
                    "intent": {
                        'name':intent,
                        'slots': slots
                        
                        }
                }
               } 
    
            
           
        else:
            response = {
            "sessionState": {
                "dialogAction": {
                    "type": "Delegate"
                },
                "intent": {
                    'name':intent,
                    'slots': slots
                    
                    }
        
            }
        }
            
    if event['invocationSource'] == 'FulfillmentCodeHook':
        
        response = {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                'name':intent,
                'slots': slots,
                'state':'Fulfilled'
                
                }
    
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": "Request accepted"
            }
        ]
    }
            
    return response
