import pickle

total_time = 30*60*60 + 19 * 60 + 45    # total time we need to use
sum_second = 0  # time already used, initial be zero

def data_set_read():
    pickle_file = open('learn_progress.testing','rb')   # load the data
    my_list2 = pickle.load(pickle_file)
    calculate(my_list2)


# calculate the progress
def calculate(my_list2):
    global sum_second
    for each in my_list2:
        sum_second += 60 * int(each[0]) + int(each[1])
    print("miniutes already take: " + str(sum_second/(60*60)) + "/" + str(total_time/(60*60)) + ", " 
        + str((sum_second/(60*60))*100/(total_time/(60*60))) + " %")

data_set_read()

