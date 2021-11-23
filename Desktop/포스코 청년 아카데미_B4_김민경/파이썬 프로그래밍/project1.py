#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 계속 사용해야하는 위에 기본틀
def printt():
    print('student','\t','\t','Name','\t','\t','   Midterm','\t','\t','Final','\t','\t','Average','\t','Grade')
    print("------------------------------------------------------------------------------------------------------------")


# In[2]:


def search(student):  # 특정 학생 검색
    id_ = input('Student ID : ')
    count = 0   # 카운트 0으로 초기화
    for i in range(len(student)):
        if id_ == student[i][0]:
            count += 1 # 학번이 있다면 1을 더해준다.
            printt()
            for i in student[i]:
                print(i, end='\t\t')  # 해당행을 차례대로 출력
            break  # 출력후 나오기
        
    
    if count ==0:  # 카운트가 한번도 되지 않았다면 없는 학생이다.
        print('NO SUCH PERSON.')  


# In[3]:


def show(student):
    
    student.sort(key=lambda e: e[4],reverse=True)  # 평균점수 기준으로 내림차순 정렬한 후
    printt()
    for i in student:  #학생파일에서 한 행씩
        for j in i:  # 그 한 행에서 한 인덱스씩
            print(j, end='\t\t') 
        print()


# In[4]:


def grade(avg):  # 학점계산해주는 함수
    if avg >= 90:
        grade = 'A'
    elif avg >=80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >=60:
        grade = 'D'
    else:
        grade = 'F'
    
    return grade


# In[5]:


def changescore(student):  #점수 수정
    count=0                 #카운트 초기화
    id_ = input('Student ID : ')
    
    for i in range(len(student)): 
        if id_ == student[i][0]:  # 학번이 있으면
            count +=1             #카운트를 해준다.
            aa = input("'Mid/Final?'")  # 학번이 있을 경우 -> 중간/ 기말
            
            if aa == 'mid':   # mid 라고 입력하면,,,
                score = input("Input new score : ")
                
                if int(score) < 0 or int(score) >100:  # 이상한 점수 입력할 경우
                      break 
                else:   # 알맞은 점수를 입력하면
                    printt()
                    print(student[i][0],'\t','\t',student[i][1],'\t','\t',student[i][2],'\t','\t',student[i][3],
                          '\t','\t',student[i][4],'\t','\t',student[i][5])
                    student[i][2] = score   # 입력 받은 점수를 넣어라
                    avg = (int(student[i][2]) + int(student[i][3])) / 2  # mid 와 final 평균
                    student[i][4]=avg
                    student[i][5]=grade(avg)
                    print('Score changed.')
                    print(student[i][0],'\t','\t',student[i][1],'\t','\t',student[i][2],'\t','\t',student[i][3],
                          '\t','\t',student[i][4],'\t','\t',student[i][5])
                    print()
                    break  #출력하고 나오기
                    
                    
                    
            elif aa == 'final':   # final 라고 입력하면,,,
                score = input("Input new score : ")
                
                if int(score) < 0 or int(score) >100:  # 이상한 점수 입력할 경우
                      break 
                else:   # 알맞은 점수를 입력하면
                    printt()
                    print(student[i][0],'\t','\t',student[i][1],'\t','\t',student[i][2],'\t','\t',student[i][3],
                          '\t','\t',student[i][4],'\t','\t',student[i][5])
                    student[i][3] = score   # 입력 받은 점수를 넣어라
                    avg = (int(student[i][2]) + int(student[i][3])) / 2  # mid 와 final 평균
                    student[i][4]=avg
                    student[i][5]=grade(avg)
                    print('Score changed.')
                    print(student[i][0],'\t','\t',student[i][1],'\t','\t',student[i][2],'\t','\t',student[i][3],
                          '\t','\t',student[i][4],'\t','\t',student[i][5])
                    print()
                    break  # 출력하고 나오기
                             
            else:  # mid 와 final 외의 입력을 했을 때 그냥 나오기
                break
                
    if count ==0:
        print('NO SUCH PERSON.')
        


# In[6]:


def searchgrade(student):
    blank = []
    grade = input('Grade to search :')  # 학점 입력
    if grade in['A', 'B','C','D','F']:  
        
        for i in range(len(student)):
            if grade ==student[i][5] :  # 입력한 학점이 그 행에 있다면
                blank.append(i)  # 빈리스트에 그 학점이 있는 행번호를 넣는다.
                
        if blank ==[]: # 입력한 학점이 없다면 빈리스트만 남게된다
            print('NO RESULTS.')
                
        else:
            printt()
            for i in blank:  # 학점이 있는 행번호가 담긴 리스트
                for j in student[i]:  # 그 행을 for문으로 이용하여 출력
                    print(j, end='\t\t')
                print()  


# In[23]:


def add(student):
    id_ = input('Student ID : ')
    dd=[]  # 빈 리스트 생성
    count =0  #  카운트 초기화
    
    for i in range(len(student)):
        if id_ == student[i][0]:   #입력한 학번과 같으면
            count +=1              # 카운트를 증가
            print('ALREADY EXITS.')   # 이미 존재하다고 출력
            
    if count ==0:   # 카운트가 0일경우 = 학번이 없다면
        for i in range(1):
            name = input('Name: ')
            mid = input('Midterm Score: ')
            final = input('Final Score: ')
            print('student added')
            avg = (int(mid) + int(final)) /2   # 평균
            g = grade(avg)   # 학점
            dd.append(id_)   # append 이용하여 빈리스트에 추가
            dd.append(name)
            dd.append(mid)
            dd.append(final)
            dd.append(avg)
            dd.append(g)
            student.append(dd)
            break
   


# In[17]:


def remove(student):
    id_ = input('Student ID : ')
    count = 0   # 카운트 0으로 초기화
    
    if len(student)==0:   # student이 0이면 아무 값도 없는 것임.
        return print('List is empty.')
           
    else:
        for line in student:
            if id_ == line[0]:  # 첫 행의 첫 인덱스 = 학번
                count += 1 # 학번이 있다면 1을 더해준다.
                student.remove(line)  # 그 라인(행)을 지운다.
                print('Student removed.')
        
    
    if count ==0:  # 카운트가 한번도 되지 않았다면 없는 학생이다.
        return print('NO SUCH PERSON.')


# In[31]:


def quit(student):
    save = input('Save data?[yes/no]')
    if save == 'yes':
        file__name =input('File name: ')
        file = open(file__name,'w')  # 파일은 쓰기모드로 연다.
        temp =''  # 텍스트를 담을 빈 공간
        
        for i in range(len(student)):  
            for j in range(6):
                temp += str(student[i][j]) + '\t'   # temp에 더해주는 형식
            temp += '\n'
        file.write(temp)
        file.close()
 


# In[33]:


import sys

def main():

    if len(sys.argv) ==2:
        file_name =sys.argv[1]
    else:
        file_name ='students.txt'
    
    student =[] # 데이터 받을 빈 리스트

    file = open(file_name,'r')  # 파일 읽기
    for line in file:
        line = line.strip()
        line = line.split('\t')  # 탭 기준으로 분리
        avg = (int(line[2])+int(line[3])) /2  # 평균 구하기
        g = grade(avg)
        line.append(avg)
        line.append(g)
        student.append(line)  # student의 빈 리스트에 담아줌


    student.sort(key=lambda e: e[4],reverse=True)  #평균 점수를 기준으로 내림차순 정렬


    print()
    show(student)

    while True:
        print()
        aa = input("#") 
        bb = aa.lower()  # 입력값을 소문자로 변환
        if bb =='show':
            show(student)
            
        elif bb =='changescore':
            changescore(student)
        
        elif bb =='search':
            search(student)
            
        elif bb =='searchgrade':
            searchgrade(student)
        
        elif bb =='add':
            add(student)
            
        elif bb =='remove':
            remove(student)
            
        elif bb =='quit':
            quit(student)
            break

        else:
            continue  # 다른 값을 입력 시 처음으로 돌아감

main()

