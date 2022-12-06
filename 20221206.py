olution(s):
        words = list(s.lower())
            
                answer = ''
                    for i in range(len(words)):
                                if words[i] == ' ' and i < len(words)-1:
                                                words[i+1] = words[i+1].upper()
                                                        elif i == 0:
                                                                        words[i] = words[i].upper()
                                                                                answer = ''.join(words)
                                                                                    
                                                                                        return answer
