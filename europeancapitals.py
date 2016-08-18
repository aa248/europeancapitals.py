#aa248
#7/15/16

"""A game in which users can guess the capitals of European nations."""

from random import *


def europeancapitals():
    D = {'NETHERLANDS':'AMSTERDAM','ANDORRA':'ANDORRA LA VELLA','GREECE':'ATHENS',
         'SERBIA':'BELGRADE','GERMANY':'BERLIN','SWITZERLAND':'BERN','SLOVAKIA':'BRATISLAVA',
         'BELGIUM':'BRUSSELS','ROMANIA':'BUCHAREST','HUNGARY':'BUDAPEST','MOLDOVA':'CHISINAU',
         'DENMARK':'COPENHAGEN','IRELAND':'DUBLIN', 'FINLAND':'HELSINKI','UKRAINE':'KIEV',
         'PORTUGAL':'LISBON','SLOVENIA':'LJUBLJANA','UNITED KINGDOM':'LONDON','LUXEMBOURG':'LUXEMBOURG',
         'SPAIN':'MADRID','BELARUS':'MINSK','MONACO':'MONACO','RUSSIA':'MOSCOW',
         'CYPRUS':'NICOSIA','GREENLAND':'NUUK','NORWAY':'OSLO','FRANCE':'PARIS','MONTENEGRO':'PODGORICA',
         'CZECH REPUBLIC':'PRAGUE','ICELAND':'REYKJAVIK','LATVIA':'RIGA','ITALY':'ROME','SAN MARINO':'SAN MARINO',
         'BOSNIA AND HERZEGOVINA':'SARAJEVO','MACEDONIA':'SKOPJE','BULGARIA':'SOFIA','SWEDEN':'STOCKHOLM',
         'ESTONIA':'TALLINN','ALBANIA':'TIRANA','LIECHTENSTEIN':'VADUZ','MALTA':'VALLETTA','HOLY SEA':'VATICAN CITY',
         'AUSTRIA':'VIENNA','LITHUANIA':'VILNIUS','POLAND':'WARSAW','CROATIA':'ZAGREB'}
    
    
    
    thekeys = D.keys()
    thekeys.sort()
   # print thekeys 
    thevalues = D.values()
    
    print 'Enter the capital of the given European nation.'
    
    while True:
        randomvalue = randint(0, len(thekeys))
        randomcountry = thekeys[randomvalue]
        #print randomcountry
        while True:
            try:
                
                userinput = raw_input('What is the capital of ' + randomcountry + '?: ')
                userinput = userinput.upper()
                
                
                if D[randomcountry]==userinput:
                    break
            
                else:
                    assert userinput in thevalues
                    print 'This is a European capital, but not the capital of ' +randomcountry + '. Try again!'
                    
            except:
                print 'Your answer is not a European capital. Try again.'
                
                
                
        print 'Great job!'
        print 'The capital of ' + randomcountry + ' is ' + userinput 
        
    
        again = raw_input('Do you want to try another one? Enter Yes or No: ')
        again = again.upper()
        if again != 'YES':
            break
    
    
    
if __name__ == '__main__':
    europeancapitals()
