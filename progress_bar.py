'''
Program to print custom progress bar
'''
import time
import sys


def main():
    '''
    main function that does all the work using sys and time libraries
    '''
    bar_width = 50

    sys.stdout.write("[%s]" % ('-' * bar_width))
    sys.stdout.flush()
    sys.stdout.write('\b' * (bar_width + 1))

    for _ in range(bar_width):
        time.sleep(0.1)
        sys.stdout.write('>')
        sys.stdout.flush()

    sys.stdout.write(']\n')
    time.sleep(1)
    print('Progress Completed')


if __name__ == '__main__':
    main()
