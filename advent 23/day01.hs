removeLetters :: String -> String
removeLetters xs = [ x | x <- xs, x `elem` "1234567890" ]

stringToInt :: String -> Int
stringToInt a = read [head a, last a]

main :: IO ()
main = do
  contents <- readFile "day01.txt"
  
  print (sum (map (stringToInt . removeLetters) (lines contents)))

  