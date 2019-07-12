output_file = open("output.txt", "r", encoding="utf-8")
answer_file = open("answer.txt", "r", encoding="utf-8")

out_sentences = output_file.readlines()
ans_sentences = answer_file.readlines()

output, answer = [], []
sum_precision, sum_recall = 0, 0
avg_precision, avg_recall = 0, 0

length = 9  # 카테고리 개수
max_idx = 0

for sentence in out_sentences:
    probability = []
    probability2 = sentence.split("\t")
    for j in probability2:
        probability.append(float(j))

    for idx in range(len(probability)):
        if probability[idx] > probability[max_idx]:
            max_idx = idx
    output.append(max_idx)

for sentence in ans_sentences:
    tmp = sentence.split('\n')
    answer.append(int(tmp[0]))

# 리스트 초기화 안하면 에러남;
TP = [0] * length
FN = [0] * length
FP = [0] * length
TN = [0] * length

# TP, FN, FP 계산. TN은 필요없당.
for i in range(len(output)):
    if output[i] == answer[i]:
        TP[output[i]] += 1
    elif output[i] is not answer[i]:
        FN[answer[i]] += 1
        FP[output[i]] += 1

total_TP, total_FP, total_FN = 0, 0, 0

for i in range(length):
    total_TP += TP[i]
    total_FP += FP[i]
    total_FN += FN[i]

# 초기화
precision = [0] * length
recall = [0] * length

# 카테고리 별 precision 이랑 recall 계산
for i in range(length):
    if TP[i] == 0:
        precision[i] = 0
        recall[i] = 0
    else:
        precision[i] = TP[i] / (TP[i] + FP[i])
        recall[i] = TP[i] / (TP[i] + FN[i])

for i in range(length):
    sum_precision += precision[i]
    sum_recall += recall[i]

# 카테고리 별 precision, recall 평균
avg_precision = sum_precision / length
avg_recall = sum_recall / length

macro_averaging_F1 = (2 * avg_precision * avg_recall) / (avg_precision + avg_recall)

# 카테고리 상관 없는 micro F1
precision2 = total_TP / (total_TP + total_FP)
recall2 = total_TP / (total_TP + total_FN)

micro_averaging_F1 = (2 * precision2 * recall2) / (precision2 + recall2)

print(">> Performance")
print(" - Macro_F1 : " + str("%.4f" % macro_averaging_F1) + "\n")
print(" - Prediction : " + str("%.4f" % precision2))
print(" - Recall : " + str("%.4f" % recall2))
print(" - Micro_F1 : " + str("%.4f" % micro_averaging_F1))
