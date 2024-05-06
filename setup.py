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
        print('Running initial config and creating test task')
    task_command = f'{todexe} t q -c Alfred Test Task'
    result = subprocess.run(task_command, shell=True, check=True)
    if result.returncode == 0:
        print ('Configuration completed successfully! Please check your Todoist Inbox for the Alfred Test Task!')
    else:
        print("There was an error with creating the test task. Please run 'tod config reset' and try running setup again.")
# Function for Yes/No response prompts
def yes_no(question: str) -> bool:
    reply = None
    while reply not in ('y', 'n'):
        reply = input(f'{question} (y/n): ').lower()
    return reply == 'y'


if __name__ == '__main__':
    main()