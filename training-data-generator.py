import json
import csv
from datetime import datetime
from datetime import timedelta
from array import array
from calendar import monthrange
from random import seed
import random
from random import randint
import numpy as np
import pandas as pd



###################
## Declare constants 
###################
# customer ID start
starting_cust_id=30908

# customer ID end
ending_cust_id=30908+11000

# how many evemts we need?
max_interactions_sequence_count=8000

# starting date of the dataset
event_start_date = datetime(2019, 3, 3)
# datetime.datetime.utcfromtimestamp(0)
epoch_event_start_date = int(event_start_date.strftime('%s'))
# print(epoch_event_start_date)

event_time_range = 31536000 #seconds in a year. 

max_time_between_events = 1059200  
min_time_between_events = 3900 # 3 days. 


# lets createa a set of possible interactions 
# Lets say there are 6 different types of intents. 
# each intent can have a sequence of calls of different types
# we will use these fixed set of interaction sequence to generate synthetic data

intent_type=6 # number denoting the intent
interaction_sequence_length = 5 # this number is denoting event type within a sequence

intent_type=6 # number denoting the intent
interaction_sequence_length = 5 # this number is denoting event type within a sequence

# arr = array('i')
call_matrix  = [[0 for x in range(interaction_sequence_length)] for y in range(intent_type)]


## Intents 
call_matrix[0] = ['HL_NE','HL_AS','HL_DS','HL_RP','HL_CS']  # call sequences
call_matrix[1] = ['CC_NE','CC_CA','CC_AA','CC_LC','CC_CS']  # call sequences
call_matrix[2] = ['AC_NE','AC_AS','AC_PA','AC_AA','AC_CS']  # call sequences
call_matrix[3] = ['FD_NE','FD_NA','FD_AD','FD_PW','FD_CS']  # call sequences
call_matrix[4] = ['LI_NE','LI_AS','LI_PA','LI_SW','LI_CS']  # call sequences
call_matrix[5] = ['TA_NE','HL_AS','HL_DS','HL_RP','TA_CS']  # call sequences

random_sequence_length = ['1','1','1','2','2','2','2','2','2','3','3','3','3','3','3','4','4','5','5','6','7']

#data column headers 
# USER_ID (string), ITEM_ID (string), TIMESTAMP (long), IMPRESSION


with open('interactions.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["USER_ID", "ITEM_ID", "TIMESTAMP"])

    ## Loop for interaction sequences 
    interactions_sequence_count=0 
    while ( interactions_sequence_count <= max_interactions_sequence_count ):

        #pic a customer id randomly 
        customer_id = randint(starting_cust_id, ending_cust_id)

        #pic a event sequence randomly 
        intent_id =  randint(0, intent_type-1)

        # select a event sequence length 
        max_sequence_length = int(random.choice(random_sequence_length))

        sequence_length = 0
        time_lapse_between_event = epoch_event_start_date+event_time_range
        next_event_time =randint(epoch_event_start_date , time_lapse_between_event)

        while (sequence_length <= max_sequence_length):
            if sequence_length >= interaction_sequence_length:
                event_sequence_index = interaction_sequence_length-1
            else:
                event_sequence_index = sequence_length
            writer.writerow([customer_id, call_matrix[intent_id][event_sequence_index] ,next_event_time])
            print(call_matrix[intent_id][event_sequence_index])
            sequence_length+=1
            next_event_time += randint(min_time_between_events, max_time_between_events)

        interactions_sequence_count+=1

file.close()


interactions_df=pd.read_csv("interactions.csv")
print(interactions_df.describe())
interactions_df.head(20)