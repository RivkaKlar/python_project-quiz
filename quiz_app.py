import sys
import random

def summary(right_ans,stop_line_number):
    print(f'You answered {right_ans}/{stop_line_number} correctly answers ')


def random_list(ans):
    return random.shuffle(ans)

def print_ques_ans(ques,ans,right_ans):
    """ get a dict and print it with key and value"""
    correct_ans=ans[0]
    print(ques)
    random_list(ans)
    for a, b in enumerate(ans,1) :
        print(f'{a}.{b}')
    num=input()
    if ans[int(num)-1]==correct_ans:
        right_ans+=1
    return right_ans


def open_file(name_file,stop_line_number):
    """ get a name of a file , openes it and takes out all answers to a list """
    right_ans=0
    with open(rf'questions/{name_file}.txt', mode='r') as file:
        for index ,line in  enumerate(file,1):
          if(index > stop_line_number):
                break
          ques,ans=line.split(';' , 1 )  #   divide the line to string of ans 
          ans=ans.replace(' ;',',').replace('\n','')  #   remove ' ;' from ans and replace(change) it to ','
          ans=ans.split(',') #   parse ans(string) to list by ,
          right_ans = print_ques_ans(ques,ans,right_ans)
        summary(right_ans,stop_line_number)

def main():
    # TODO: your code here
    name_file=sys.argv[1]
    stop_line_number=int(sys.argv[2])
    open_file(name_file,stop_line_number)

if __name__ == '__main__':
    main()