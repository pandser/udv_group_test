from netmiko import ConnectHandler


def get_version(obj):
    return obj.send_command('sh ver').split('Technical Support')[0]

def get_startup_config(obj):
    return obj.send_command('sh start')

def get_running_config(obj):
    return obj.send_command('sh run')

def get_access_lists(obj):
    return obj.send_command('sh access-lists')

def get_interface_status(obj):
    return obj.send_command('sh ip int brief')

if __name__ == '__main__':
    try:
        with ConnectHandler(
            device_type = 'cisco_ios_telnet',
            host='192.168.122.2',
            username='admin',
            password='cisco',
        ) as net_connect:
            with open('report/report.txt', 'w', encoding='utf-8') as file:
                file.write(
                    f'Версия:\n{get_version(net_connect)}\n\n'
                    f'{"-"*50}\n'
                    f'Стартовая конфигурация:\n'
                    f'{get_startup_config(net_connect)}\n\n'
                    f'{"-"*50}\n'
                    f'Текущая конфигурация:\n'
                    f'{get_running_config(net_connect)}\n\n'
                    f'{"-"*50}\n'
                    f'Списки контроля доступа:\n'
                    f'{get_access_lists(net_connect)}\n\n'
                    f'{"-"*50}\n'
                    f'Сведения об интерфейсах:\n'
                    f'{get_interface_status(net_connect)}'
                )
    except Exception as error:
        with open('report/report.txt', 'w', encoding='utf-8') as file:
                file.write(str(error))
