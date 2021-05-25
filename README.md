# Peptides_extraction
#Extract information and annotation of peptides from output of RiboCode

#The *result.txt and *result.gtf is the output of RiboCode for detecting ORFs using Ribo-seq data. The script, zzz_extract_peptides.py, is used to extract information of small ORFs.
## USEAGE:
python3 zzz_extract_peptides.py Bleaf1.
#The gtf and txt file must be in current directory.

![image](https://user-images.githubusercontent.com/46277338/119521393-ae86e500-bdad-11eb-9aab-83a33202b995.png)

for i in *out.txt;do
name=${i%txt}
gtf=${name}gtf
cat $i >> z_all.txt
cat $gtf >>　zzz_all.gtf
done
head -n1 z_all.txt > zzz_all.txt
grep -v "ORF" z_all.txt >> zzz_all.txt
##各材料的gtf、txt文件顺序对应，想将其写入一个文件（txt有表头注意去掉），在通过加编号去冗余
python3 zzz_merge.py
