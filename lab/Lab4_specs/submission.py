## import modules here 

################# Question 1 #################

def multinomial_nb(training_data, sms):# do not change the heading of the function
    spam = {}
    ham = {}
    count_s = 0
    count_h = 0
    spam_prob = {}
    ham_prob = {}
    words = set()
    for data in training_data:
        if data[1] == 'ham':
            count_h += 1
            for i in data[0]:
                if i not in ham:
                    ham[i] = data[0][i]
                else:
                    ham[i] += data[0][i]
        elif data[1] == 'spam':
            count_s += 1
            for i in data[0]:
                if i not in spam:
                    spam[i] = data[0][i]
                else:
                    spam[i] += data[0][i]
        for i in data[0]:
            words.add(i)
    prior_ham = count_h / len(training_data)
    prior_spam = count_s / len(training_data)
    for w in words:
        if w in ham:
            ham_prob[w] = (ham[w] + 1) / (sum(ham.values()) + len(words))
        else:
            ham_prob[w] = 1 / (sum(ham.values()) + len(words))
        if w in spam:
            spam_prob[w] = (spam[w] + 1) / (sum(spam.values()) + len(words))
        else:
            spam_prob[w] = 1 / (sum(spam.values()) + len(words))
    sms_dic = {}
    for i in set(sms):
        sms_dic[i] = sms.count(i)
    result_s = prior_spam
    result_h = prior_ham
    for i in sms_dic:
        if i in words:
            result_s *= spam_prob[i] ** sms_dic[i]
            result_h *= ham_prob[i] ** sms_dic[i]
    return result_s / result_h
