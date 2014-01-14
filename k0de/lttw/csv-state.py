# core
import csv

# 3rd party
import argh


def process(file_name):

    states = set()

    state_fp = dict()

    def field_names():
        return 'Email,Fname,Lname,Address,City,State,Zip,Phone,IP,Date_and_Time,gender,birth'.split(',')

    def get_state_fp(state):
        if state not in state_fp:
            state_fp[state] = open("{0}.csv".format(state), 'a')
        return state_fp[state]

    def write_state(row):
        fp = get_state_fp(row['State'])
        fp.write(
            " {Phone},{Fname},{Lname},{Address},{City},{State},{Email}\n".format(**row)
        )

    with open(file_name, 'rb') as csvfile:
        lead_reader = csv.DictReader(
            csvfile,
            field_names()
        )
        for row in lead_reader:
            write_state(row)


argh.dispatch_command(process)
