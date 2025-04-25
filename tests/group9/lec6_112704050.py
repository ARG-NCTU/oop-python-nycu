#####################################
# EXAMPLE:  Towers of Hanoi
#####################################

# 定義如何顯示移動的過程
def tower(n,fr ,to ,spare):
    moves = []    

    def move(n,fr ,to ,spare):
        if n == 1:
            moves.append((fr ,to))
        else:
            #step 1 : 將n-1個從p1移到p3
            move(n-1 , fr , spare , to)
            #step 2 : 將最下面那一個從p1移到p2
            moves.append((fr ,to))
            #step 3 : 將n-1個從p3移到p2
            move(n-1 , spare , to ,fr)
    
    move(n,fr ,to ,spare)
    return moves
print(tower(5,"p1","p2","p3"))


#####################################
# EXAMPLE:  fibonacci
#####################################
def fib2(x):
    if x == 0 or x==1: #F(0)=0 F(1)=1
        return x
    
    else:
        x = fib2(x-1)+fib2(x-2)
        return x
fib_num = []
for i in range(20):
    fib_num.append(fib2(i))
    print(f"F({i})={fib2(i)}")
print(fib_num)

#####################################
# EXAMPLE:  testing for palindrome 回文
#####################################
        
def palindrome_check(s):

    def delete_non_alpha(s):
        s = s.lower()#轉換為小寫
        ans = ""
        for c in s :
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans
    
    def check(s):
        if len(s) <=1 :
            return True
        else:
            if s[0] == s[-1]:
                return check(s[1:-1])
            else:
                return False
    return check(delete_non_alpha(s))

print(palindrome_check("aba"))
print(palindrome_check("abc"))
print(palindrome_check("ab ba"))
print(palindrome_check("abb a"))
print(palindrome_check("ab,b a"))


#####################################
# EXAMPLE: using dictionaries
#          counting frequencies of words in song lyrics
#####################################

def news_to_frequencies(input):
    myDict = {}
    for word in input:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    to_delete = []
    for k in myDict:
        if myDict[k] <= 5:#刪掉出現太少次的
            to_delete.append(k)
    for i in to_delete:
        #print(i)
        del myDict[i]
    #print(myDict["the"])
    return myDict

def find_the_most_common_words(myDict):
    #print(myDict)
    print("The most common words are:")
    num_max = []
    for i in myDict:
        if myDict[i] == max(myDict.values()):
            print(f"{i}: {myDict[i]}")
            num_max.append(i)

    print("\n")
    print("The least common words are:")
    num_least = []
    for i in myDict:
        if myDict[i] == min(myDict.values()):
            print(f"{i}: {myDict[i]}")
            num_least.append(i)
    return num_max, num_least
    
news = ["Getty", "Images","San", "Francisco", "in", "California", "is", "home", "to", "some", "of", "the", "world", "'s", "leading", "tech", "companies", "." , "California", "'s", "economy", "has", "overtaken", "that", "of", "the", "country", "of", "Japan", ",", "making", "the", "US", "state", "the", "fourth", "largest", "global", "economic", "force", "." ,
"Governor", "Gavin", "Newsom", "touted", "new", "data", "from", "the", "International", "Monetary", "Fund", "(", "IMF", ")", "and", "the", "US", "Bureau", "of", "Economic", "Analysis", "showing", "California", "'s", "growth", ".",
"The", "data", "shows", "California", "'s", "gross", "domestic", "product", "(", "GDP", ")", "hit", "$", "4.10", "trillion", "(", "£", "3.08", "trillion", ")", "in", "2024", ",", "surpassing", "Japan", ",", "which", "was", "marked", "at", "$", "4.01", "trillion", ".",
"The", "state", "now", "only", "trails", "Germany", ",", "China", "and", "the", "US", "as", "a", "whole", ".",
"\"", "California", "is", "n't", "just", "keeping", "pace", "with", "the", "world", "-", "we", "'re", "setting", "the", "pace", ",", "\"", "Newsom", "said", ".",
"The", "new", "figures", "come", "as", "Newsom", "has", "spoken", "out", "against", "President", "Donald", "Trump", "'s", "tariffs", "and", "voiced", "concern", "about", "the", "future", "of", "the", "state", "'s", "economy", ".",
"California", "has", "the", "largest", "share", "of", "manufacturing", "and", "agricultural", "production", "in", "the", "US", ".",
"It", "is", "also", "home", "to", "leading", "technological", "innovation", ",", "the", "centre", "of", "the", "world", "'s", "entertainment", "industry", "and", "the", "country", "'s", "two", "largest", "seaports", ".",
"Newsom", ",", "a", "prominent", "Democrat", "and", "possible", "presidential", "candidate", "in", "2028", ",", "filed", "a", "lawsuit", "challenging", "Trump", "'s", "authority", "to", "impose", "the", "levies", ",", "which", "have", "caused", "disruption", "to", "global", "markets", "and", "trade", ".",
"Trump", "has", "enacted", "10", "%", "levies", "on", "almost", "all", "countries", "importing", "to", "the", "US", ",", "after", "announcing", "a", "90-day", "pause", "on", "higher", "tariffs", ".",
"Another", "25", "%", "tariff", "was", "imposed", "on", "Mexico", "and", "Canada", ".",
"The", "levies", "on", "China", ",", "however", ",", "have", "led", "to", "an", "all-out", "trade", "war", "with", "the", "world", "'s", "second", "largest", "economy", ".",
"Trump", "imposed", "import", "taxes", "of", "up", "to", "145", "%", "on", "Chinese", "goods", "coming", "into", "the", "US", "and", "China", "hit", "back", "with", "a", "125", "%", "tax", "on", "American", "products", ".",
"His", "administration", "said", "last", "week", "that", "when", "the", "new", "tariffs", "were", "added", "on", "to", "existing", "ones", ",", "the", "levies", "on", "some", "Chinese", "goods", "could", "reach", "245", "%", ".",
"Newsom", "noted", "his", "worries", "about", "the", "future", "of", "the", "state", "'s", "economy", ".",
"While", "we", "celebrate", "this", "success", ",", "we", "recognise", "that", "our", "progress", "is", "threatened", "by", "the", "reckless", "tariff", "policies", "of", "the", "current", "federal", "administration", ",", "\"", "he", "said", ".",
"California", "'s", "economy", "powers", "the", "nation", ",", "and", "it", "must", "be", "protected", ".", "\"",
"Trump", "has", "argued", "his", "trade", "war", "is", "only", "levelling", "the", "playing", "field", "after", "years", "of", "the", "US", "being", "taken", "advantage", "of", ".",
"The", "tariffs", "are", "an", "effort", "to", "encourage", "factories", "and", "jobs", "to", "return", "to", "the", "US", ".",
"It", "is", "one", "major", "pillar", "of", "his", "economic", "agenda", ",", "as", "is", "a", "cut", "in", "interest", "rates", ",", "aimed", "at", "reducing", "the", "cost", "of", "borrowing", "for", "Americans", ".",
"The", "new", "data", "shows", "California", "'s", "GDP", "behind", "the", "US", "at", "$", "29.18", "trillion", ",", "China", "at", "$", "18.74", "trillion", "and", "Germany", "at", "$", "4.65", "trillion", ".",
"It", "also", "shows", "California", "was", "the", "fastest", "growing", "among", "those", "countries", ".",
"Japan", "'s", "economy", "is", "under", "pressure", "because", "of", "its", "decreasing", "and", "ageing", "population", ",", "which", "means", "its", "workforce", "is", "shrinking", "and", "social", "care", "costs", "are", "ballooning", ".",
"This", "week", ",", "the", "IMF", "cut", "its", "economic", "growth", "forecast", "for", "Japan", "and", "projected", "that", "the", "central", "bank", "would", "raise", "interest", "rates", "more", "slowly", "than", "previously", "expected", "because", "of", "the", "impact", "of", "higher", "tariffs", ".",
"The", "effect", "of", "tariffs", "announced", "on", "April", "2", "and", "associated", "uncertainty", "offset", "the", "expected", "strengthening", "of", "private", "consumption", "with", "above-inflation", "wage", "growth", "boosting", "household", "disposable", "income", ",", "\"", "its", "World", "Economic", "Outlook", "report", "said", "."]

a = news_to_frequencies(news)
print(a)
#find_the_most_common_words(a)
print(find_the_most_common_words(a))