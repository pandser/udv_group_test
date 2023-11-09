import ast
import logging
import os

from dotenv import load_dotenv
from netmiko import ConnectHandler
from typing import Type


load_dotenv()

logging.basicConfig(
    filename='report/error.log',
    filemode='w',
)


SEPARATOR = "-"*50
SWITCH = ast.literal_eval(os.getenv('SWITCH'))


def get_version(obj: Type[ConnectHandler]) -> str:
    '''Версия оборудования.'''
    return obj.send_command('sh ver').split('Technical Support')[0]

def get_startup_config(obj: Type[ConnectHandler]) -> str:
    '''Стартовая конфигурация.'''
    return obj.send_command('sh start')

def get_running_config(obj: Type[ConnectHandler]) -> str:
    '''Текущая конфигурация.'''
    return obj.send_command('sh run')

def get_access_lists(obj: Type[ConnectHandler]) -> str:
    '''Списки контроля доступа.'''
    return obj.send_command('sh access-lists')

def get_interface_status(obj: Type[ConnectHandler]) -> str:
    '''Сведения об интерфейсах.'''
    return obj.send_command('sh ip int brief')

def main() -> None:
    try:
        comands = [
                get_version, 
                get_startup_config,
                get_running_config,
                get_access_lists,
                get_interface_status,
                ]
        with ConnectHandler(**SWITCH) as net_connect:
            with open('report/report.txt', 'w', encoding='utf-8') as file:
                file.write(
                    ''.join([(f'{comand.__doc__}\n\n{comand(net_connect)}\n\n'
                        f'{SEPARATOR}\n') for comand in comands])
                )
    except Exception as error:
        logging.error(error)


if __name__ == '__main__':
    main()
    