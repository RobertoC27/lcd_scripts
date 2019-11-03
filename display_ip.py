import lcddriver
from subprocess import check_output


try:
    display = lcddriver.lcd()
    my_ip = str(check_output(['hostname', '-I']), 'utf-8')

    display.lcd_display_string(my_ip,2)


except KeyboardInterrupt:
    print('cleaning up!')
    