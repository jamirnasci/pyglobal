def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap_penalty=-1):
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)

    score_matrix = [[0] * (len_seq2 + 1) for _ in range(len_seq1 + 1)]

    for i in range(1, len_seq1 + 1):
        score_matrix[i][0] = i * gap_penalty
    for j in range(1, len_seq2 + 1):
        score_matrix[0][j] = j * gap_penalty

    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            match_score = score_matrix[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            delete_score = score_matrix[i - 1][j] + gap_penalty
            insert_score = score_matrix[i][j - 1] + gap_penalty

            score_matrix[i][j] = max(match_score, delete_score, insert_score)


    align1 = ""
    align2 = ""
    matches = 0
    i, j = len_seq1, len_seq2
    while i > 0 or j > 0:
        if i > 0 and j > 0 and score_matrix[i][j] == score_matrix[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch):
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            matches += 1
            i -= 1
            j -= 1
        elif i > 0 and score_matrix[i][j] == score_matrix[i - 1][j] + gap_penalty:
            align1 = seq1[i - 1] + align1
            align2 = "-" + align2
            i -= 1
        else:
            align1 = "-" + align1
            align2 = seq2[j - 1] + align2
            j -= 1
    similarity = matches * 100 / len(align1)
    return {
      "al1": align1,
      "al2": align2, 
      "score": score_matrix[len_seq1][len_seq2], 
      "similarity": similarity        
    } 
