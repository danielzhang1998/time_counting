import pickle
import easygui as g

# 18 is minutes and 00 is seconds
# add in more time list or edit if need
my_time = [
    [18,00],[13,32],[24,22],[19,28],
    [26,50],[19,00],[16,32],[16,31],
    [12,10],[13,27],[13,29],[13,2],
    [20,18],[15,30],[28,59],[26,23],
    [20,49],[13,55],[16,47],[16,48],
    [19,3],[12,46],[20,48],[18,20],
    [13,26],[17,51],[17,49],[9,43],
    [16,55],[14,43],[23,33],[12,24],
    [12,38],[15,4],[9,37],[14,16]
    ]

# make a new binary file to store the data in list my_time
def add_data_set(my_time):
    # auto create a new file if it not exists, or write into the file directly if the file exists
    pickle_file = open('learn_progress.testing','wb')   # wb is write binary, do not mind the file name, it can be anything
    pickle.dump(my_time,pickle_file)    # dump the list into the file
    pickle_file.close()

def data_set_read():
    pickle_file = open('learn_progress.testing','rb')   # rb is read binary
    my_list2 = pickle.load(pickle_file) # load the binary data
    print(my_list2) # show the data
    length_data_set = len(my_list2)
    g.msgbox('data set insert successful :)' + '\n\n' + 'total insert: ' + str(length_data_set))

add_data_set(my_time)
data_set_read()