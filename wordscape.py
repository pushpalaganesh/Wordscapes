letters = [['h','o','i','l','d','a','y'],

           ['p', 'r', 'a', 'g', 'r', 'o', 'm', 'i','m','n','g'],

           ['b','a','o','t','c','o','m','p'],

           ['f','l','w','o','c','r','a','t','h'],

           ['w', 'a', 'r', 'd', 'o', 'c', 'e','p','s','s']]

words = [["hi","do","ad","oh","hay","day","had","lay","dal","lad","lid","aid","old","oil","load","hold","lady","hail","idol","halo","dial","ahold","holiday"],

         ["go","an","in","no","on","am","or","pro","map","mom","gap","gag","pig","man","rag","pin","rap","pan","mop","ram","ping",

          "pong","pram","prom","ramp","norm","gram","main","pain","rain","ring","pair","among","groan","organ","major","minor",

          "apron","mango","margin","random","moping","roping","program","roaming","programming"],

         ["am","at","to","cab","cap","cob","cop","map","mop","act","bat","cat","mat","tab","top","pot","boat","boot","camp",

          "comb","boom","pact","atom","coat","tomb","combat","bootcamp"],

         ["of","at","or","to","low","hat","cat","rat","art","car","law","raw","caw","cow","how","who","war","far","calf","claw","flaw","flow",

          "fowl","wolf","crow","half","flat","that","oath","chat","coal","calf","float","wrath","chart","forth","cloth","craft","fatal","worth","afloat","flowchart"],

         ["ad","so","or","we","do","as","ads","pro","are","cap","caw","cop","cow","paw","cod","dew","pad","war","cape","word","ward",

          "cord","drop","scar","soar","spot","cope","crap","crew","crop","pace","spare","roads","scape","scope","rapes","words","sward","space","password","wordscape","wordscapes"]];

lives = 5;

level = 0;

score = 0;

while level < 5 :

    print('Level {}'.format(level+1))

    print('Create 5 words using the given letters')
    
    for c in letters[level]:

        print('{}\t'.format(c),end='');

    print()

    wordCount = 0;

    watch = False;

    word = '';

    oldWord = '';

    while wordCount == 0 or wordCount < 5:

        match = False;       

        word = input('Word: ')

        if not(word.lower() == oldWord.lower()):

            for w in words[level]:

                if(word.lower() == w):

                    wordCount += 1

                    score += 1

                    oldWord = word

                    match = True

                    break

        if not match:

            print('Wrong Guess')

            lives -= 1

        if lives == 0:

            print('Game Over!! Better Luck Next Time!!')

            print('Your score is {}'.format(score))

            break     

    wordCount = 0

    match = False

    word = ''

    if lives == 0:

        break

    if level == 4:

        print('Thanks for playing the game!!!')

        print('Your score is {}'.format(score))

        level += 1

    else:

        choice = input('Do you want to continue to next level? (y/n) ')

        if(choice.lower()[0] == 'y'):

            level += 1

        else:

            print('Thanks for playing the game!!!')

            print('Your score is {}'.format(score))

            break
