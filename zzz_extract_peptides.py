import sys
import csv
import pandas as pd
import os

name = sys.argv[1]
txt = name+"result.txt"
gtf = name+"result.gtf"
log = name+"log.txt"
out_gtf = name+"out.gtf"
out_txt = name+"out.txt"

df_txt = pd.read_table(txt,sep="\t")
df_txt = df_txt.loc[:,["ORF_ID","strand","ORF_length","ORF_gstart","ORF_gstop","AAseq"]]
#读取ORF信息
df_txt["number"] = df_txt.index
#因为gtf和txt是一一对应的，因此给ORF编上号
df_txt = df_txt[df_txt["ORF_length"]<=300]
#选取其中的sORF
df_txt = df_txt.drop_duplicates(subset = ["ORF_ID","strand","ORF_length","ORF_gstart","ORF_gstop","AAseq"],keep="first")
#去除重复的ORF信息，保留最先出现的
#df_txt = df_txt.iloc[:,range(0,6)]
df_txt.iloc[:,range(0,6)].to_csv(out_txt,sep="\t",header=True,index=False)

log_obj = open(log,"w")
#中间文件
gtf_obj = open(gtf,'r')
number=-1

while 1:
    line = gtf_obj.readline()
    line = line.strip()
    if line == "":break
    linelist = line.split("\t")
    #print(line)
    term = linelist[2]
    if term == "ORF":
        number+=1
    #print(str(number))
    line = line+"\t"+str(number)
    log_obj.write(line+"\n")
gtf_obj.close()
log_obj.close()
#将加上编号的gtf文件写入log.txt,然后将df_txt里的行号给拿出来

df_log = pd.read_table(log,sep="\t",header=None)
overlap = [(i in df_txt["number"]) for i in df_log[9]]
#将编号对应df_txt中的行号取出
df_gtf = df_log[overlap]
df_gtf = df_gtf.iloc[:,range(0,9)]
df_gtf.to_csv(out_gtf,sep="\t",header=False,index=False,quoting=csv.QUOTE_NONE)
#最后的参数用于解决输出过多引号的问题
os.system("rm "+log)
#删除掉log.txt文件
