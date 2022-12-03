convert :: Char -> Char
convert 'X' = 'A'
convert 'Y' = 'B'
convert 'Z' = 'C'
convert _ = error ""

value :: Char -> Integer
value 'A' = 1
value 'B' = 2
value 'C' = 3
value _ = error ""

outcome :: Char -> Char -> Integer
outcome 'A' 'C' = 6
outcome 'B' 'A' = 6
outcome 'C' 'B' = 6
outcome us them
  | us == them = 3
  | otherwise = 0

score :: Char -> Char -> Integer
score them us = value us + outcome us them

process :: [(Char, Char)] -> Integer
process = sum . map (uncurry score)

splitMoves :: String -> (Char, Char)
splitMoves [them, _, us] = (them, convert us)
splitMoves x = error x

processInput :: [String] -> [String]
processInput inp = [(show . process . map splitMoves) inp]

main = interact (unlines . processInput . lines)
