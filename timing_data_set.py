import pickle

my_time = [
    [18,00],[13,32],[24,22],[19,28],
    [26,50],[19,00],[16,32],[16,31],
    [12,10],[13,27],[13,29],[13,2],
    [20,18],[15,30],[28,59],[26,23],
    [20,49],[13,55],[16,47],[16,48],
    [19,3],[12,46],[20,48],[18,20],
    [13,26],[17,51],[17,49],[9,43],
    [16,55],[14,43],[23,33],[12,24],
    [12,38]
    ]

def add_data_set(my_time):
    pickle_file = open('learn_progress.testing','wb')
    pickle.dump(my_time,pickle_file)
    pickle_file.close()

def data_set_read():
    pickle_file = open('learn_progress.testing','rb')
    my_list2 = pickle.load(pickle_file)
    print(my_list2)
    #print(len(my_list2))

add_data_set(my_time)
data_set_read()