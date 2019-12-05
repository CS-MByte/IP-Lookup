# Simple IP Loopkup Script Using https://ipstack.com/ API

import requests, os, time, json

red = '\033[31m'
white = '\033[37m'

def main():
    try:
        os.system('cls')
        address = input(white + '\nIP Address: ')

        if address == '' or address == ' ':
            os.system('cls')
            print(red + '\nError' + white + ', Please Enter An IP Address...')
            time.sleep(2)
            main()
        else:
            apikey = 'PUT API KEY HERE'
            url = 'http://api.ipstack.com/' + address + '?access_key=' + apikey

            get = requests.get(url)
            response = json.loads(get.content)
            os.system('cls')

            print('IP Address:', response['ip'])
            print('Continent:', response['continent_name'])
            print('Country:', response['country_name'])
            print('City:', response['city'])
            print('Zip Code:', response['zip'])

            userInput = input('\nWould You Like To Run Again? (Y/N): ')

            if userInput.upper() == 'Y'.upper():
                main()
            elif userInput.upper() == 'N'.upper():
                os.system('cls')
                print (red + '\nClosing' + white + '...')
                time.sleep(1)
                os.system('cls')
                exit(0)
            else:
                exit(0)
    except KeyboardInterrupt:
        os.system('cls')
        print ('\n\033[31mClosing\033[37m...')
        time.sleep(1)
        os.system('cls')

if __name__ == '__main__':
    main()
    
