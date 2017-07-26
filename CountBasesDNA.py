# -*- coding:utf-8 -*-
#Compatible with Python2

#Insert sequence 
sequence = raw_input("Write your DNA sequence:")
seq = sequence.lower()

#Verify characters of the sequence
ambiguity = ['r','y','s','w','k','m','b','v','d','h','n']
rna = ['u']
error_bases = ['e','f','i','j','l','ñ','ç','o','p','q','x','z']

for letter in ambiguity:
	if letter in seq:
		number_letter = seq.index(letter) + 1
		print("\tIMPORTANT: Ambiguous nucleotide (" + letter + ") in the position " + str(number_letter) + ".")
	else:
		pass
for uracilo in rna:
	if uracilo in seq:
		number_uracilo = seq.index(uracilo) + 1
		print("\tWARNING: Uracilo in the position " + str(number_uracilo) + ".")
	else:
		pass
for error_base in error_bases:
	if error_base in seq:
		number_error = seq.index(error_base) + 1
		print("\tWARNING: Non-nucleotide character (" + error_base + ") in the position " + str(number_error) + ".")
	else:
		pass

if seq.isalpha():
    pass  
else:
    print("\tWARNING: Your sequence contains non alphabetic characters ")

print("\n")

# Count bases
count_a = seq.count('a')
per_a = round(float(count_a)/len(seq),4)*100
count_t = seq.count('t')
per_t = round(float(count_t)/len(seq),4)*100
count_c = seq.count('c')
per_c = round(float(count_c)/len(seq),4)*100
count_g = seq.count('g')
per_g = round(float(count_g)/len(seq),4)*100

#It is or not a coding sequence

coding = raw_input("Are there non-conding regions in the sequence [y/n]?:")
code = coding.lower()

#Separate for codon position
		
while True:
	if code == "y":
		break
	elif code == "n":
		code_position = raw_input("The first base corresponds to which position of the codon [1/2/3]? (or type n if you don't know):")
		position = code_position.lower()
		if position == "1":
			seq_1 = seq[0:len(seq):3]
			seq_2 = seq[1:len(seq):3]
			seq_3 = seq[2:len(seq):3]
			break
		elif position == "2":
			seq_1 = seq[1:len(seq):3]
			seq_2 = seq[2:len(seq):3]
			seq_3 = seq[0:len(seq):3]
			break
			
		elif position == "3":
			seq_1 = seq[2:len(seq):3]
			seq_2 = seq[0:len(seq):3]
			seq_3 = seq[1:len(seq):3]
			break
		
		elif position == "n":
			break

#Results for the total sequence
		
print("\nTotal sequence")
print("\tNumber of A: " + str(count_a) + "\tPercentage of A: " + str(per_a) + "%")
print("\tNumber of T: " + str(count_t) + "\tPercentage of T: " + str(per_t) + "%")
print("\tNumber of C: " + str(count_c) + "\tPercentage of C: " + str(per_c) + "%")
print("\tNumber of G: " + str(count_g) + "\tPercentage of G: " + str(per_g) + "%")

#Verify if seq_1 was calculated 

seq_1_exists = 'seq_1' in locals() or 'seq_1' in globals()

try:
    seq_1
except NameError:
    seq_1_exists = False
else:
    seq_1_exists = True

#Count bases by position

if seq_1_exists == True:
	count_a = seq_1.count('a')
	per_a = round(float(count_a)/len(seq_1),4)*100
	count_t = seq_1.count('t')
	per_t = round(float(count_t)/len(seq_1),4)*100
	count_c = seq_1.count('c')
	per_c = round(float(count_c)/len(seq_1),4)*100
	count_g = seq_1.count('g')
	per_g = round(float(count_g)/len(seq_1),4)*100
	print("\nFirst position")
	print("\tNumber of A: " + str(count_a) + "\tPercentage of A: " + str(per_a) + "%")
	print("\tNumber of T: " + str(count_t) + "\tPercentage of T: " + str(per_t) + "%")
	print("\tNumber of C: " + str(count_c) + "\tPercentage of C: " + str(per_c) + "%")
	print("\tNumber of G: " + str(count_g) + "\tPercentage of G: " + str(per_g) + "%")
	count_a = seq_2.count('a')
	per_a = round(float(count_a)/len(seq_2),4)*100
	count_t = seq_2.count('t')
	per_t = round(float(count_t)/len(seq_2),4)*100
	count_c = seq_2.count('c')
	per_c = round(float(count_c)/len(seq_2),4)*100
	count_g = seq_2.count('g')
	per_g = round(float(count_g)/len(seq_2),4)*100
	print("\nSecond position")
	print("\tNumber of A: " + str(count_a) + "\tPercentage of A: " + str(per_a) + "%")
	print("\tNumber of T: " + str(count_t) + "\tPercentage of T: " + str(per_t) + "%")
	print("\tNumber of C: " + str(count_c) + "\tPercentage of C: " + str(per_c) + "%")
	print("\tNumber of G: " + str(count_g) + "\tPercentage of G: " + str(per_g) + "%")
	count_a = seq_3.count('a')
	per_a = round(float(count_a)/len(seq_3),4)*100
	count_t = seq_3.count('t')
	per_t = round(float(count_t)/len(seq_3),4)*100
	count_c = seq_3.count('c')
	per_c = round(float(count_c)/len(seq_3),4)*100
	count_g = seq_3.count('g')
	per_g = round(float(count_g)/len(seq_3),4)*100
	print("\nThird position")
	print("\tNumber of A: " + str(count_a) + "\tPercentage of A: " + str(per_a) + "%")
	print("\tNumber of T: " + str(count_t) + "\tPercentage of T: " + str(per_t) + "%")
	print("\tNumber of C: " + str(count_c) + "\tPercentage of C: " + str(per_c) + "%")
	print("\tNumber of G: " + str(count_g) + "\tPercentage of G: " + str(per_g) + "%")
	print("\n")
elif seq_1_exists == False:
	print("\n")


#Subset the sequence and search stop codons

stop_codons = ['tga','taa','tag']
codons = []

if seq_1_exists == True:
	print("Stop codons:")
	if position == "1":
		seq_codon = seq[0:len(seq)]
		deleted_bases = 0
	elif position == "2":
		seq_codon = seq[2:len(seq)]
		deleted_bases = 2
	elif position == "3":
		seq_codon = seq[1:len(seq)]
		deleted_bases = 1
	for i in range(0, len(seq_codon), 3):
		codon = seq_codon[i:i+3]
		codons.append(codon)
	for stop_codon in stop_codons:
		if stop_codon in codons:
			number_codon = codons.index(stop_codon) + 1
			position_codon = number_codon*3 - 2 + deleted_bases
			print("\t" + stop_codon + " is present in the position " + str(position_codon) + ".")
		else:
			print("\t" + stop_codon + " is not present in your sequence.")
elif seq_1_exists == False:
	print("\n")
	

print("\n--------* End *--------")
