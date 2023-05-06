import os
import sys
import json
import subprocess

cargopath = os.path.expanduser('~/.cargo/bin/cargo')
todexe = os.path.expanduser('~/.cargo/bin/tod')
configfile = os.path.expanduser('~/Library/Application Support/tod.cfg')

def main():
    print('Checking for Rust...')
    if (os.path.isfile(cargopath)):
        print ('Rust is installed!')
    else:
        auto = yes_no('Rust is not installed. Install Automatically?')
        if auto == False:
            print('Please Install Rust (https://www.rust-lang.org/tools/install)')
            sys.exit(1)
        else:
            rustup_install = 'curl --proto \'=https\' --tlsv1.2 -sSf https://sh.rustup.rs | sh'
            subprocess.run(rustup_install, shell=True, check=True)
    print('Checking for Tod...')
    if (os.path.isfile(todexe)):
        print ('Tod is installed!')
    else:
        auto = yes_no('Install Tod?')
        if auto == False:
            print('Please Install TOD (https://github.com/alanvardy/tod)')
            sys.exit(1)
        else:
            print('Attemping to Install TOD')
            tod_install = f'{cargopath} install tod'
            subprocess.run(tod_install, shell=True, check=True)
    print('Checking for Config File...')
    if (os.path.isfile(configfile)):
        print ('TOD is Configured!')
    else:
        print('Running initial config and creating test task')
        task_command = f'{todexe} -q Alfred TOD Test Task'
        subprocess.run(task_command, shell=True, check=True)

    print ('Configuration completed successfully! Please check your Todoist Inbox!')

# Function for Yes/No response prompts
def yes_no(question: str) -> bool:
    reply = None
    while reply not in ('y', 'n'):
        reply = input(f'{question} (y/n): ').lower()
    return reply == 'y'


if __name__ == '__main__':
    main()