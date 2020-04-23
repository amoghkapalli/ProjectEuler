'''Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?'''
import time
start_time = time.time()
name=open('names.txt', 'r')
sort_names=name.read()
name.close()
sort_names=sort_names.replace('"', '')
names=sort_names.split(',')
names.sort()
length_of_names=len(names)
total_final_sum_allw=0
def letter_score(single_char):
    let_val=ord(single_char)-64
    return int(let_val)

def name_worth(ones_name):
    length_of_onename=len(ones_name)
    sum_of_word=0
    for i in range (length_of_onename):
        substr=ones_name[i:i+1]
        sum_of_word+=letter_score(substr)
    return sum_of_word

def name_totpoint_calc(one_name, index):
    name_pt_val=name_worth(one_name)
    total_pt=name_pt_val*(index+1)
    return total_pt

#name_totpoint_calc('COLIN', 938)
print(sum(name_totpoint_calc(names[i], i) for i in range(0, len(names))))
print("--- %s seconds ---" % (time.time() - start_time))


