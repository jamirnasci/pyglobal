import sys
import readseq
import align

query_path = ""
subjects_path = ''

for key, arg in enumerate(sys.argv):
  if arg == '-q':
    query_path = sys.argv[key + 1]
  elif arg == '-s':
    subjects_path = sys.argv[key+1:len(sys.argv)]

(ref_filename, query_seq) = readseq.read_fasta(query_path)

with open('report.csv', 'w') as result_file:
  result_file.write("Sequence Pair;Score;Similarity\n")
  for subject_path in subjects_path:  
    (sub_filename, subject_seq) = readseq.read_fasta(subject_path)
    res = align.needleman_wunsch(query_seq, subject_seq)
    result_file.write('{} x {};{};{:.2f} %\n'.format(ref_filename, sub_filename, res["score"], res["similarity"]))

