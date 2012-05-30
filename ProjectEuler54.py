#coding:utf-8
#!/usr/bin/env python
"""
Project Euler Problem 54

ポーカーの勝敗判定

カードゲームのポーカーでは, 手札は5枚のカードからなりランク付けされている. 役を低い方から高い方へ順に並べると以下である.

    役無し: 一番値が大きいカード
    ワン・ペア: 同じ値のカードが2枚
    ツー・ペア: 2つの異なる値のペア
    スリーカード: 同じ値のカードが3枚
    ストレート: 5枚の連続する値のカード
    フラッシュ: 全てのカードが同じスート (注: スートとはダイヤ・ハート・クラブ/スペードというカードの絵柄のこと)
    フルハウス: スリーカードとペア
    フォーカード: 同じ値のカードが4枚
    ストレートフラッシュ: ストレートかつフラッシュ
    ロイヤルフラッシュ: 同じスートの10, J, Q, K, A
"""
import time
import math
import Euler
t1=time.time()

cards=open("projecteuler54poker.txt","r")
pair=tuple(open("projecteuler54pair.txt","r").read().split(","))
straight=("23456","34567","45678","56789","6789T","789JT","89JTQ","9JKQT","AJKQT")
four=tuple(open("projecteuler54fourcard.txt","r").read().split(","))
three=tuple(open("projecteuler54threecard.txt","r").read().split(","))
fullhouse=tuple(open("projecteuler54fullhouse.txt","r").read().split(","))
twopair=tuple(open("projecteuler54twopair.txt","r").read().split(","))
flash=("DDDDD","SSSSS","CCCCC","HHHHH")

point_dic={"A":14,"K":13,"Q":12,"J":11,"T":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}
def poi(te):
    if te=="A":
        return 14
    elif te=="K":
        return 13
    elif te=="Q":
        return 12
    elif te=="J":
        return 11
    elif te=="T":
        return 10
    else:
        return int(te)

def load_turn(file):
    one_turn=file.read().split("\n")
    return one_turn

def make_tefuda(li):
    p1=li.strip().split(" ")[0:5]
    p2=li.strip().split(" ")[5:10]
    return (p1,p2)

def win_lose(a,b):
    if a>b:
        return True
    else:
        return False

class Tefuda:
    def __init__(self,seq):
		seq.sort()
		self.cards=seq
		self.suit=seq[0][1]+seq[1][1]+seq[2][1]+seq[3][1]+seq[4][1]
		self.nums=seq[0][0]+seq[1][0]+seq[2][0]+seq[3][0]+seq[4][0]

    def rank(self):
		if self.suit in flash:
			if self.nums=="AJKQT":
				return 9
			elif self.nums in straight:
				return 8
			else:
				return 5
		elif self.nums in four:
				return 7
		elif self.nums in fullhouse:
				return 6
		elif self.nums in straight:
				return 4
		elif self.nums in three:
				return 3
		elif self.nums in twopair:
				return 2
		elif self.nums in pair:
				return 1
		else:
				return 0

    def next(self):
        if self.rank() in (9,8,6,5,4,0):
            if "A" in self.nums:
                return 14
            elif "K" in self.nums:
                return 13
            elif "Q" in self.nums:
                return 12
            elif "J" in self.nums:
                return 11
            elif "T" in self.nums:
                return 10
            else:
                return int(self.nums[-1])
        elif self.rank() in (7,3):
            return poi(self.nums[2])
        elif self.rank()==2:
            if poi(self.nums[1])>poi(self.nums[3]):
                return poi(self.nums[1])
            else:
                return poi(self.nums[3])
        else:                   # <- one pair
            if self.nums.count(self.nums[0])==2:
                return poi(self.nums[0])
            elif self.nums.count(self.nums[2])==2:
                return poi(self.nums[2])
            else:
                return poi(self.nums[4])

def main():
    answer=0
    pokers=open("projecteuler54poker.txt","r")
    turns=load_turn(pokers)
    for trn in turns:
        pl1=make_tefuda(trn)[0]
        pl2=make_tefuda(trn)[1]
        ply1=Tefuda(pl1)
        ply2=Tefuda(pl2)
        if win_lose((ply1.rank(),ply1.next()),(ply2.rank(),ply2.next())):
            answer+=1
    return answer

if __name__ == '__main__':
    answerr=main()

print answerr
print time.time()-t1, "seconds"