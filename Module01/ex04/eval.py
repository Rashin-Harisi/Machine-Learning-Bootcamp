#!/usr/bin/env python3

class Evaluator():
    @staticmethod
    def zip_evaluate(coefs: list, words: list):
        if len(words) != len(coefs):
            return -1
        temp_list = []
        for word,coef in zip(words, coefs):
            temp_list.append(len(word) * coef)
        result = sum(temp_list[i] for i in range(len(temp_list)))
        return result

    @staticmethod
    def enumerate_evaluate(coefs:list, words: list):
        if len(words) != len(coefs):
            return -1
        temp_list= []
        for i, word in enumerate(words):
            temp_list.append(len(word) * coefs[i])
        result = sum(temp_list[i] for i in range(len(temp_list)))
        return result