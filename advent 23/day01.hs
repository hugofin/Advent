removeLetters :: String -> String
removeLetters xs = [ x | x <- xs, x `elem` "1234567890" ]

stringToInt :: String -> Int
stringToInt a = read [head a, last a]

checkForNum :: String -> String
checkForNum [] = []
checkForNum ('o':'n':'e'        :ys) = '1':checkForNum ('n':'e':ys)
checkForNum ('t':'w':'o'        :ys) = '2':checkForNum ('w':'o':ys)
checkForNum ('t':'h':'r':'e':'e':ys) = '3':checkForNum ('h':'r':'e':'e':ys)
checkForNum ('f':'o':'u':'r'    :ys) = '4':checkForNum ('o':'u':'r':ys)
checkForNum ('f':'i':'v':'e'    :ys) = '5':checkForNum ('i':'v':'e':ys)
checkForNum ('s':'i':'x'        :ys) = '6':checkForNum ('i':'x':ys)
checkForNum ('s':'e':'v':'e':'n':ys) = '7':checkForNum ('e':'v':'e':'n':ys)
checkForNum ('e':'i':'g':'h':'t':ys) = '8':checkForNum ('i':'g':'h':'t':ys)
checkForNum ('n':'i':'n':'e'    :ys) = '9':checkForNum ('i':'n':'e':ys)
checkForNum ( y                 :ys) =  y :checkForNum ys

main :: IO ()
main = do
  contents <- readFile "day01.txt"
  print ( sum (map (stringToInt . removeLetters . checkForNum) (lines contents)))